"""
    /usr/builds/scripts/builds.py
    Wed Sep 25 23:30:16 UTC 2024

    Core functionality of the bld command

    Copyright:: (c) 2024 Darren Kirby
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


import argparse
import datetime
import sys

import common_functions as cf
import search_package
import dep_resolve


APPNAME = "bld"
APPVERSION = "0.3.1"
QUIP = "By far the best software available for turtle stacking"


class CustomArgumentParser(argparse.ArgumentParser):
    """Overrides the default argparse error handling"""
    def error(self, message):
        cf.red(message)
        show_usage()
        sys.exit(-1)


def process_args():
    """Process command line arguments"""

    global_parser = CustomArgumentParser(add_help=False)
    subparsers = global_parser.add_subparsers(dest="command")

    global_parser.add_argument('-h', '--help', action='store_true')

    install_parser = subparsers.add_parser("install")
    install_parser.add_argument('-f', '--fetch', action='store_true')
    install_parser.add_argument('-p', '--pretend', action='store_true')
    install_parser.add_argument('-a', '--ask', action='store_true')

    uninstall_parser = subparsers.add_parser("uninstall")
    search_parser = subparsers.add_parser("search")
    info_parser = subparsers.add_parser("info")

    args = global_parser.parse_args()
    return args


def do_main():
    """
    The main dispatch loop.

    This function dispatches out all commands that are not `install`,
    or builds the list of packages to install and feeds them one by one
    to the BuildPackage class.
    """

    # Print banner
    cf.print_green(f"{APPNAME} ")
    print("version ", end='')
    cf.print_green(f"{APPVERSION} ")
    print("(", end='')
    cf.print_bold(f"{QUIP}")
    print(")")

    args = process_args()
    if args.help:
        show_usage()
        sys.exit(0)

    print(args)

    config = cf.get_config()

    if args.command == 'search':
        search_package.do_search(args, config)
        sys.exit(0)
    elif args.command == 'info':
        search_package.do_info(args, config)
        sys.exit(0)
    elif args.command == 'uninstall':
        do_uninstall(args, config)
        sys.exit(0)
    else:
        builds_to_build = dep_resolve.resolve_dependencies()

    n_builds = len(builds_to_build)
    this_build = 1

    for build in builds_to_build:
        start_time = datetime.datetime.now()


def show_usage() -> None:
    """Prints usage details to the screen"""
    print(f"""
Usage: {APPNAME} [options] command pkg_atom [pkg_atom...]
    General Options:
        '-h'   or '--help'                  show usage details
        '-f'   or '--fetch'                 download packages but do not install
        '-p'   or '--pretend'               only show which packages would be built
        '-a'   or '--ask'                   prompt before building packages

    Commands:
        'install'   pkg_atom [pkg_atom...]  install one or more packages and dependancies
        'uninstall' pkg_atom                uninstall package
        'search'    string                  search the package db for package names matching string
        'info'      pkg_atom                print info on packages if installed
""")
