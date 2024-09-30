#    /usr/builds/scripts/search_package.py
#    Wed Sep 25 23:30:16 UTC 2024

#    Core functionality of the bld command
#
#    Copyright:: (c) 2024 Darren Kirby
#    Author:: Darren Kirby (mailto:bulliver@gmail.com)

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.


import dbm
import argparse

import common_functions as cf


def do_search(args: argparse.Namespace, config: dict) -> None:
    """Search string arguments against db names and descriptions"""
    to_search = args.pkg_atom
    match = False

    with dbm.open(config['db_file']) as db:
        for pkg in to_search:
            for k in db.keys():
                if isinstance(k, bytes):
                    name = k.decode('UTF-8')
                if isinstance(db[k], bytes):
                    val = db[k].decode('UTF-8')
                a = val.split(",")

                if (name.find(pkg) != -1) or (a[5].find(pkg) != -1):
                    cf.print_bold("Category/Name ")
                    cf.green(a[0])
                    cf.print_bold("      Version ")
                    cf.green(a[1])
                    cf.print_bold("  Description ")
                    cf.green(a[5])
                    cf.print_bold("     Homepage ")
                    cf.green(a[4])
                    print()
                    match = True

    if not match:
        print(f"Could not find package(s) matching `{', '.join(to_search)}`")
        print()


def do_info(args, config):
    pass
