// +------------------------------------------------------------------+
// |             ____ _               _        __  __ _  __           |
// |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
// |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
// |           | |___| | | |  __/ (__|   <    | |  | | . \            |
// |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
// |                                                                  |
// | Copyright Mathias Kettner 2014             mk@mathias-kettner.de |
// +------------------------------------------------------------------+
//
// This file is part of Check_MK.
// The official homepage is at http://mathias-kettner.de/check_mk.
//
// check_mk is free software;  you can redistribute it and/or modify it
// under the  terms of the  GNU General Public License  as published by
// the Free Software Foundation in version 2.  check_mk is  distributed
// in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
// out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
// PARTICULAR PURPOSE. See the  GNU General Public License for more de-
// ails.  You should have  received  a copy of the  GNU  General Public
// License along with GNU Make; see the file  COPYING.  If  not,  write
// to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
// Boston, MA 02110-1301 USA.

#ifndef TableServices_h
#define TableServices_h

#include "config.h"  // IWYU pragma: keep
#include <string>
#include "Table.h"
#include "nagios.h"  // IWYU pragma: keep
#ifdef CMC
#include <mutex>
#include "Core.h"
#else
class DowntimesOrComments;
#endif
class Query;

class TableServices : public Table {
public:
#ifdef CMC
    TableServices(const Core::_notes_t &downtimes_holder,
                  const Core::_notes_t &comments_holder,
                  std::recursive_mutex &holder_lock);
    static void addColumns(Table *, std::string prefix, int indirect_offset,
                           bool add_hosts,
                           const Core::_notes_t &downtimes_holder,
                           const Core::_notes_t &comments_holder,
                           std::recursive_mutex &holder_lock);
#else
    TableServices(const DowntimesOrComments &downtimes_holder,
                  const DowntimesOrComments &comments_holder);
    static void addColumns(Table *, std::string prefix, int indirect_offset,
                           bool add_hosts,
                           const DowntimesOrComments &downtimes_holder,
                           const DowntimesOrComments &comments_holder);
#endif
    const char *name() override { return "services"; }
    bool isAuthorized(contact *, void *) override;
    void *findObject(char *objectspec) override;
    void answerQuery(Query *) override;
};

#endif  // TableServices_h
