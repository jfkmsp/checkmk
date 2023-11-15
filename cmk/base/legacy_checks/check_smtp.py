#!/usr/bin/env python3
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.


from cmk.utils.hostaddress import HostName  # pylint: disable=cmk-module-layer-violation

from cmk.base.check_api import host_name, is_ipv6_primary, passwordstore_get_cmdline
from cmk.base.config import active_check_info


# TODO: rename to params. not now to keep change small.
def check_smtp_arguments(settings):  # pylint: disable=too-many-branches
    args = []

    if "expect" in settings:
        args += ["-e", settings["expect"]]

    if "port" in settings:
        args += ["-p", settings["port"]]

    # Use the address family of the monitored host by default
    address_family = settings.get("address_family")
    if address_family is None:
        address_family = "ipv6" if is_ipv6_primary(HostName(host_name())) else "ipv4"

    if address_family == "ipv6":
        args.append("-6")
        address = "$_HOSTADDRESS_6$"
    else:
        args.append("-4")
        address = "$_HOSTADDRESS_4$"

    for s in settings.get("commands", []):
        args += ["-C", s]

    for s in settings.get("command_responses", []):
        args += ["-R", s]

    if settings.get("from"):
        args += ["-f", settings["from"]]

    if "response_time" in settings:
        warn, crit = settings["response_time"]
        args += ["-w", "%0.4f" % warn]
        args += ["-c", "%0.4f" % crit]

    if "timeout" in settings:
        args += ["-t", settings["timeout"]]

    if "auth" in settings:
        username, password = settings["auth"]
        args += ["-A", "LOGIN", "-U", username, "-P", passwordstore_get_cmdline("%s", password)]

    if settings.get("starttls", False):
        args.append("-S")

    if "fqdn" in settings:
        args += ["-F", settings["fqdn"]]

    if "cert_days" in settings:
        warn, crit = settings["cert_days"]
        args += ["-D", "%d,%d" % (warn, crit)]

    if "hostname" in settings:
        args += ["-H", settings["hostname"]]
    else:
        args += ["-H", address]

    return args


def check_smtp_desc(params):
    if (name := params["name"]).startswith("^"):
        return name[1:]
    return f"SMTP {name}"


active_check_info["smtp"] = {
    "command_line": "check_smtp $ARG1$",
    "argument_function": check_smtp_arguments,
    "service_description": check_smtp_desc,
}
