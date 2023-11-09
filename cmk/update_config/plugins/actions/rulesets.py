#!/usr/bin/env python3
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from collections.abc import Container, Mapping, Sequence
from logging import Logger
from re import Pattern
from typing import Any

import cmk.utils.store as store
from cmk.utils import debug
from cmk.utils.labels import single_label_group_from_labels
from cmk.utils.log import VERBOSE
from cmk.utils.rulesets.definition import RuleGroup
from cmk.utils.rulesets.ruleset_matcher import RulesetName, RuleSpec

from cmk.checkengine.checking import CheckPluginName

from cmk.gui.exceptions import MKUserError
from cmk.gui.watolib.hosts_and_folders import Folder, folder_tree
from cmk.gui.watolib.rulesets import AllRulesets, RulesetCollection

from cmk.update_config.plugins.actions.replaced_check_plugins import REPLACED_CHECK_PLUGINS
from cmk.update_config.registry import update_action_registry, UpdateAction
from cmk.update_config.update_state import format_warning, UpdateActionState

REPLACED_RULESETS: Mapping[RulesetName, RulesetName] = {
    "checkgroup_parameters:fileinfo-groups": "checkgroup_parameters:fileinfo_groups_checking",
    "static_checks:fileinfo-groups": "static_checks:fileinfo_groups_checking",
}

DEPRECATED_RULESET_PATTERNS: list[Pattern] = []


class UpdateRulesets(UpdateAction):
    def __call__(self, logger: Logger, update_action_state: UpdateActionState) -> None:
        # To transform the given ruleset config files before initialization, we cannot call
        # AllRulesets.load_all_rulesets() here.
        raw_rulesets = AllRulesets(RulesetCollection._initialize_rulesets())
        root_folder = folder_tree().root_folder()
        all_rulesets = _transform_label_conditions_in_all_folders(logger, raw_rulesets, root_folder)

        _delete_deprecated_wato_rulesets(
            logger,
            all_rulesets,
            DEPRECATED_RULESET_PATTERNS,
        )
        _transform_replaced_wato_rulesets(
            logger,
            all_rulesets,
            REPLACED_RULESETS,
        )
        _transform_wato_rulesets_params(
            logger,
            all_rulesets,
        )
        _remove_removed_check_plugins_from_ignored_checks(
            all_rulesets,
            REPLACED_CHECK_PLUGINS,
        )
        _validate_rule_values(logger, all_rulesets)
        all_rulesets.save()


update_action_registry.register(
    UpdateRulesets(
        name="rulesets",
        title="Rulesets",
        sort_index=30,
    )
)


def _transform_label_conditions_in_all_folders(
    logger: Logger, all_rulesets: AllRulesets, folder: Folder
) -> AllRulesets:
    for subfolder in folder.subfolders():
        _transform_label_conditions_in_all_folders(logger, all_rulesets, subfolder)

    loaded_file_config = store.load_mk_file(
        folder.rules_file_path(),
        {
            **RulesetCollection._context_helpers(folder),
            **RulesetCollection._prepare_empty_rulesets(),
        },
    )

    for varname, ruleset_config in all_rulesets.get_ruleset_configs_from_file(
        folder, loaded_file_config
    ):
        if not ruleset_config:
            continue  # Nothing configured: nothing left to do

        # Transform parameters per rule
        for rule_config in ruleset_config:
            _transform_label_conditions(rule_config)

        # Overwrite rulesets
        if varname in all_rulesets._rulesets:
            all_rulesets._rulesets[varname].replace_folder_config(folder, ruleset_config)
        else:
            all_rulesets._unknown_rulesets.setdefault(folder.path(), {})[varname] = ruleset_config

    return all_rulesets


def _transform_label_conditions(rule_config: RuleSpec[object]) -> None:
    if any(key.endswith("_labels") for key in rule_config.get("condition", {})):
        rule_config["condition"] = transform_condition_labels_to_label_groups(  # type: ignore[typeddict-item]
            rule_config.get("condition", {})  # type: ignore[arg-type]
        )


def transform_condition_labels_to_label_groups(conditions: dict[str, Any]) -> dict[str, Any]:
    for what in ["host", "service"]:
        old_key = f"{what}_labels"
        new_key = f"{what}_label_groups"
        if old_key in conditions:
            conditions[new_key] = (
                single_label_group_from_labels(conditions[old_key]) if conditions[old_key] else []
            )
            del conditions[old_key]
    return conditions


def _delete_deprecated_wato_rulesets(
    logger: Logger,
    all_rulesets: RulesetCollection,
    deprecated_ruleset_patterns: Sequence[Pattern],
) -> None:
    for ruleset_name in list(all_rulesets.get_rulesets()):
        if any(p.match(ruleset_name) for p in deprecated_ruleset_patterns):
            logger.log(VERBOSE, f"Removing ruleset {ruleset_name}")
            all_rulesets.delete(ruleset_name)
            continue


def _transform_replaced_wato_rulesets(
    logger: Logger,
    all_rulesets: RulesetCollection,
    replaced_rulesets: Mapping[RulesetName, RulesetName],
) -> None:
    deprecated_ruleset_names: set[RulesetName] = set()
    for ruleset_name, ruleset in all_rulesets.get_rulesets().items():
        if ruleset_name not in replaced_rulesets:
            continue

        new_ruleset = all_rulesets.get(replaced_rulesets[ruleset_name])

        if not new_ruleset.is_empty():
            logger.log(VERBOSE, "Found deprecated ruleset: %s" % ruleset_name)

        logger.log(VERBOSE, f"Replacing ruleset {ruleset_name} with {new_ruleset.name}")
        for folder, _folder_index, rule in ruleset.get_rules():
            new_ruleset.append_rule(folder, rule)

        deprecated_ruleset_names.add(ruleset_name)

    for deprecated_ruleset_name in deprecated_ruleset_names:
        all_rulesets.delete(deprecated_ruleset_name)


def _transform_wato_rulesets_params(
    logger: Logger,
    all_rulesets: RulesetCollection,
) -> None:
    for ruleset in all_rulesets.get_rulesets().values():
        valuespec = ruleset.valuespec()
        for folder, folder_index, rule in ruleset.get_rules():
            try:
                rule.value = valuespec.transform_value(rule.value)
            except Exception as e:
                if debug.enabled():
                    raise
                logger.error(
                    "ERROR: Failed to transform rule: (Ruleset: %s, Folder: %s, "
                    "Rule: %d, Value: %s: %s",
                    ruleset.name,
                    folder.path(),
                    folder_index,
                    rule.value,
                    e,
                )


def _validate_rule_values(
    logger: Logger,
    all_rulesets: RulesetCollection,
) -> None:
    rulesets_skip = {
        # the valid choices for this ruleset are user-dependent (SLAs) and not even an admin can
        # see all of them
        RuleGroup.ExtraServiceConf("_sla_config"),
    }

    n_invalid = 0
    for ruleset in all_rulesets.get_rulesets().values():
        if ruleset.name in rulesets_skip:
            continue

        for folder, index, rule in ruleset.get_rules():
            try:
                ruleset.rulespec.valuespec.validate_value(
                    rule.value,
                    "",
                )
            except MKUserError as excpt:
                n_invalid += 1
                logger.warning(
                    format_warning(
                        "WARNING: Invalid rule configuration detected (Ruleset: %s, Title: %s, "
                        "Folder: %s,\nRule nr: %s, Exception: %s)"
                    ),
                    ruleset.name,
                    ruleset.title(),
                    folder.path(),
                    index + 1,
                    excpt,
                )

    if n_invalid:
        logger.warning(
            format_warning(
                "Detected %s issue(s) in configured rules.\n"
                "To correct these issues, we recommend to open the affected rules in the GUI.\n"
                "Upon attempting to save them, any problematic fields will be highlighted."
            ),
            n_invalid,
        )


def _remove_removed_check_plugins_from_ignored_checks(
    all_rulesets: RulesetCollection,
    removed_check_plugins: Container[CheckPluginName],
) -> None:
    ignored_checks_ruleset = all_rulesets.get("ignored_checks")
    for _folder, _index, rule in ignored_checks_ruleset.get_rules():
        if plugins_to_keep := [
            plugin_str
            for plugin_str in rule.value
            if CheckPluginName(plugin_str).create_basic_name() not in removed_check_plugins
        ]:
            rule.value = plugins_to_keep
        else:
            ignored_checks_ruleset.delete_rule(
                rule,
                create_change=False,
            )
