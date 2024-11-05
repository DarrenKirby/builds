"""
    /var/builds/scripts/search_package.py
    Thu Oct 24 02:29:05 UTC 2024

    Search the db file for package information

    Copyright:: (c) 2024
    Author:: Darren Kirby (mailto:bulliver@gmail.com)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

import dbm
import argparse

import common_functions as cf
from config import config


def print_pkg_info(_a: list) -> None:
    """
    Print formatted package info to the screen
    """
    cf.print_bold("Category/Name ")
    cf.green(_a[0])
    cf.print_bold("      Version ")
    cf.green(_a[1])
    cf.print_bold("  Description ")
    cf.green(_a[5])
    cf.print_bold("     Homepage ")
    cf.green(_a[4])
    print()


def do_search(args: argparse.Namespace) -> None:
    """
    Search string arguments against db names and descriptions
    """
    to_search = args.pkg_atom
    match = False

    with dbm.open(config['db_file']) as db:
        for search_string in to_search:

            for k in db.keys():
                if isinstance(k, bytes):
                    name = k.decode('UTF-8')
                if isinstance(db[k], bytes):
                    val = db[k].decode('UTF-8')
                a = val.split(",")

                if args.nameonly:
                    if name.find(search_string) != -1:
                        print_pkg_info(a)
                        match = True
                else:
                    if (name.find(search_string) != -1) or (a[5].lower().find(search_string) != -1):
                        print_pkg_info(a)
                        match = True

    if not match:
        print(f"Could not find package(s) matching '{', '.join(to_search)}'")
        print()


def do_info(args):
    """
    Print information about an installed package
    """
    to_get_info = args.pkg_atom
    match = False

    for pkg in to_get_info:
        pkg_info = cf.get_db_info(pkg)
