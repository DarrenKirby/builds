"""
    /usr/builds/scripts/builds.py
    Mon Sep 30 03:13:31 UTC 2024

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
import logging as log

import common_functions as cf
import build_package
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

    # Global options
    global_parser.add_argument('-h', '--help', action='store_true')
    global_parser.add_argument('-v', '--verbose', action='store_true')

    # 'install' command options
    install_parser = subparsers.add_parser("install")
    install_parser.add_argument('-f', '--fetch', action='store_true')
    install_parser.add_argument('-p', '--pretend', action='store_true')
    install_parser.add_argument('-a', '--ask', action='store_true')
    install_parser.add_argument("pkg_atom", action="extend", nargs="+", type=str)

    # 'uninstall' command options
    uninstall_parser = subparsers.add_parser("uninstall")
    uninstall_parser.add_argument('-p', '--pretend', action='store_true')
    uninstall_parser.add_argument('-a', '--ask', action='store_true')
    uninstall_parser.add_argument("pkg_atom", action="extend", nargs="+", type=str)

    # 'search' command options
    search_parser = subparsers.add_parser("search")
    search_parser.add_argument('-n', '--nameonly', action='store_true')
    search_parser.add_argument("pkg_atom", action="extend", nargs="+", type=str)

    # 'info' command options
    info_parser = subparsers.add_parser("info")
    info_parser.add_argument("pkg_atom", action="extend", nargs="+", type=str)

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
    print()

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
        builds_to_build = dep_resolve.resolve_dependencies(args, config)

    # Initialize logger
    #   call: logging.warning("File: '%s' does not exist", filename)
    # output: 2024-07-22 09:55 - WARNING - File 'foo.txt' does not exist
    log.basicConfig(
        filename=config['logfile'],
        encoding="utf-8",
        filemode="a",
        format="%(asctime)s - %(levelname)s - %(message)s",
        #format="{asctime} - {levelname} - {message}",
        style="%",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=log.INFO
    )

    n_builds = len(builds_to_build)
    this_build = 1

    cf.green("builds to build:")
    print()
    for name, version in builds_to_build:
        cf.print_bold(f">>> {name} ")
        cf.print_green(f"{version}\n")
    print()

    if args.pretend:
        sys.exit(0)

    for build in builds_to_build:
        if args.ask:
            cont = input("...continue with these builds? [y/n] ")
            if cont in ['n', 'N']:
                cf.red("aborting")
                sys.exit(1)

        print()
        start_time = datetime.datetime.now()
        log.info('Starting build of %s', build[0])

        cf.print_bold("starting build ")
        cf.print_green(this_build)
        cf.print_bold(" of ")
        cf.print_green(n_builds)
        cf.print_bold(f" {build[0]}\n")
        print()
        this_build += 1

        bld = build_package.BuildPackage(build[0], config, args)
        bld.fetch()
        if args.fetch:
            continue
        bld.install_source()
        bld.configure()
        bld.make()
        bld.make_inst()
        bld.cleanup()

        finish_time = datetime.datetime.now()
        elapsed = finish_time - start_time
        cf.bold(f"build of {build[0]} version {build[1]} complete in {elapsed}.")
        log.info('build of %s version %s complete' % build[0],build[1])


def show_usage() -> None:
    """Prints usage details to the screen"""
    print(f"""
Usage: {APPNAME} [general options] command [command options] pkg_atom [pkg_atom...]

    Commands:
        'install'   pkg_atom [pkg_atom...]  install one or more packages and dependancies
        'uninstall' pkg_atom                uninstall package
        'search'    string                  search the package db for package names matching string
        'info'      pkg_atom                print info on packages if installed

    General Options:
        '-h'   or '--help'                  show these usage details
        '-v'   or '--verbose'               make bld more chatty

    install/uninstall Options:
        '-f'   or '--fetch'                 download packages but do not install
        '-p'   or '--pretend'               only show which packages would be built
        '-a'   or '--ask'                   prompt before installing/uninstalling package(s)

""")
