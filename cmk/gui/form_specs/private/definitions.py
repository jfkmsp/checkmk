#!/usr/bin/env python3
# Copyright (C) 2024 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from dataclasses import dataclass
from typing import Any

from cmk.gui.valuespec import ValueSpec

from cmk.rulesets.v1.form_specs import FormSpec


@dataclass(frozen=True, kw_only=True)
class LegacyValueSpec(FormSpec[Any]):
    valuespec: ValueSpec[Any]


@dataclass(frozen=True, kw_only=True)
class UnknownFormSpec(FormSpec[Any]):
    pass
