"""
    /var/builds/scripts/builds.py
    Thu Oct 24 02:16:07 UTC 2024

    Core functionality of the bld command

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

import argparse
import datetime
import sys
import logging as log
import os

import common_functions as cf
import build_package
import search_package
import dep_resolve
import uninstall
from config import config

APPNAME = "bld"
APPVERSION = "0.5.3"
QUIP = "By far the best software available for turtle stacking"


class CustomArgumentParser(argparse.ArgumentParser):
    """
    Overrides the default argparse error handling
    """

    def error(self, message: str) -> None:
        """Print argparse error in red"""
        cf.red(message)
        show_usage()
        sys.exit(-1)


def process_args() -> argparse.Namespace:
    """
    Process command line arguments
    """

    global_parser = CustomArgumentParser(add_help=False)
    subparsers = global_parser.add_subparsers(dest="command")

    # Global options
    global_parser.add_argument('-h', '--help', action='store_true')
    global_parser.add_argument('-v', '--verbose', action='store_true')
    global_parser.add_argument('-n', '--nocolor', action='store_true')
    global_parser.add_argument('-V', '--version', action='store_true')

    # 'install' command options
    install_parser = subparsers.add_parser("install")
    install_parser.add_argument('-f', '--fetch', action='store_true')
    install_parser.add_argument('-p', '--pretend', action='store_true')
    install_parser.add_argument('-a', '--ask', action='store_true')
    install_parser.add_argument('-d', '--dontclean', action='store_true')
    install_parser.add_argument('-t', '--test', action='store_true')
    install_parser.add_argument("pkg_atom", action="extend", nargs="+", type=str)

    # 'update' command options
    install_parser = subparsers.add_parser("update")
    install_parser.add_argument('-f', '--fetch', action='store_true')
    install_parser.add_argument('-p', '--pretend', action='store_true')
    install_parser.add_argument('-a', '--ask', action='store_true')
    install_parser.add_argument('-d', '--dontclean', action='store_true')
    install_parser.add_argument('-t', '--test', action='store_true')
    install_parser.add_argument('-b', '--backup', action='store_true')
    install_parser.add_argument("pkg_atom", action="extend", nargs="+", type=str)

    # 'uninstall' command options
    uninstall_parser = subparsers.add_parser("uninstall")
    uninstall_parser.add_argument('-b', '--backup', action='store_true')
    uninstall_parser.add_argument('-a', '--ask', action='store_true')
    uninstall_parser.add_argument("pkg_atom", action="extend", nargs="+", type=str)

    # 'search' command options
    search_parser = subparsers.add_parser("search")
    search_parser.add_argument('-n', '--nameonly', action='store_true')
    search_parser.add_argument("pkg_atom", action="extend", nargs="+", type=str)

    # 'info' command options
    info_parser = subparsers.add_parser("info")
    info_parser.add_argument("pkg_atom", action="extend", nargs="+", type=str)

    # 'initdb' command options
    initdb_parser = subparsers.add_parser("initdb")
    initdb_parser.add_argument("db_file", action="extend", nargs="+", type=str)

    # 'cleantree' command options
    cleantree_parser = subparsers.add_parser("cleantree")
    cleantree_parser.add_argument("category", action="extend", nargs="*", type=str)

    args = global_parser.parse_args()
    return args


def do_main() -> None:
    """
    The main dispatch loop.

    This function dispatches out all commands that are not `install`,
    or builds the list of packages to install and feeds them one by one
    to the BuildPackage class.
    """
    # Drop privs
    with cf.PrivDropper():
        args = process_args()
        if args.help:
            show_usage()
            sys.exit(0)

        if args.nocolor:
            config['color'] = False

        # Print banner
        cf.print_green(f"{APPNAME} ")
        print("version ", end='')
        cf.print_green(f"{APPVERSION} ")
        print("(", end='')
        cf.print_bold(f"{QUIP}")
        print(")")
        print()

        if args.version:
            sys.exit(0)

        if args.command == 'search':
            search_package.do_search(args)
            sys.exit(0)
        elif args.command == 'info':
            search_package.do_info(args)
            sys.exit(0)
        elif args.command == 'initdb':
            cf.do_initdb(args)
            sys.exit(0)
        elif args.command == 'cleantree':
            num_cleaned = 0
            if len(args.category) == 0:
                num_cleaned = cf.clean_tree(f"{config['builds_root']}", args)
            else:
                for cat in args.category:
                    num_cleaned = cf.clean_tree(f"{config['builds_root']}/{cat}", args)
            cf.print_bold("cleaned ")
            cf.print_green(str(num_cleaned))
            cf.print_bold(" directory\n" if num_cleaned == 1 else " directories\n")
            sys.exit(0)

    # Need priv to uninstall/update
    if args.command == 'uninstall':
        uninstall.do_uninstall(args)
        sys.exit(0)

    if args.command == 'update':
        uninstall.do_update(args)

    with cf.PrivDropper():
        builds_to_build = dep_resolve.resolve_dependencies(args)

        n_builds = len(builds_to_build)
        this_build = 1

        cf.green("builds to build:")
        for name, version in builds_to_build:
            cf.print_bold(f">>> {name} ")
            cf.print_green(f"{version}\n")
        print()

        if args.pretend:
            sys.exit(0)

        if args.ask:
            cont = input("...continue with these builds? [y/n] ")
            if cont in ['n', 'N']:
                cf.red("aborting")
                sys.exit(1)

    for build in builds_to_build:
        with cf.PrivDropper():
            already_installed = False
            check = cf.get_installed_version(build[0])
            if check != [None] and build[1] == check[1]:
                already_installed = True
                cf.yellow(f"{build[0]} version {build[1]} already installed!")
                print("Install again? ")
                if input(">>> ") in ['n', 'N']:
                    cf.red("aborting")
                    sys.exit(1)

            print()
            start_time = datetime.datetime.now()
            log.info('%s %s build started', build[0], build[1])

            cf.print_bold("starting build ")
            cf.print_green(str(this_build))
            cf.print_bold(" of ")
            cf.print_green(str(n_builds))
            cf.print_bold(f" {build[0]}\n")
            print()

            # xterm titlebar
            if config['xterm']:
                os.system(f'echo -e "\033]0; build {this_build} of {n_builds}: {build[0]}\a"')

            this_build += 1

            bld = build_package.BuildPackage(build[0], args)
            if bld.fetch():
                continue

            if args.fetch:
                continue

            bld.install_source()
            bld.configure_src()
            bld.make_src()
            bld.make_inst()

        # These two need priv
        bld.inst()
        bld.cleanup()

        with cf.PrivDropper():
            print()
            if not args.test:
                cf.green(f"Recording {build[0]} {build[1]} in 'sets/installed'...")
                if not already_installed:
                    cf.add_to_installed(build[0], build[1])
                print(">>> ...done!")

            finish_time = datetime.datetime.now()
            elapsed = finish_time - start_time
            print()
            cf.bold(f"build of {build[0]} version {build[1]} complete in {elapsed}.")
            log.info('%s %s build complete in %s', build[0], build[1], elapsed)

    print()
    cf.green("Finished all builds. Exiting...")
    sys.exit(0)


def show_usage() -> None:
    """
    Prints usage details to the screen
    """
    print(f"""
Usage: {APPNAME} [general options] command [command options] arg [arg2...]

    Commands:
        'install'   pkg_atom [pkg_atom...]  install one or more packages and dependancies
        'update'    pkg_atom [pkg_atom...]  update one or more packages
        'uninstall' pkg_atom                uninstall package
        'search'    string                  search the package db for package names matching string
        'info'      pkg_atom [pkg_atom...]  print info on packages if installed
        'initdb'    csv_file [csv_file...]  initialze a build db with data from csv_file
        'cleantree' [category...]           delete all 'work' directories, or just under [categories]

    General Options:
        '-h'   or '--help'                  show these usage details
        '-v'   or '--verbose'               make bld more chatty
        '-n'   or '--nocolor'               disable color output
        '-V'   or '--version'               print version information and exit

    install/update Options:
        '-f'   or '--fetch'                 download packages but do not install
        '-p'   or '--pretend'               show which packages would be built then exit
        '-a'   or '--ask'                   prompt before installing package(s)
        '-d'   or '--dontclean'             don't delete the package 'work' tree after installation
        '-t'   or '--test'                  build source but do not install to live filesystem
        '-b'   or '--backup'                backup installed files to '<cat>/<pkg>/backup' before updating
        
    uninstall Options:
        '-a'   or '--ask'                   prompt before uninstalling package(s)
        '-b'   or '--backup'                backup installed files to '<cat>/<pkg>/backup' before uninstalling
        
    search Options:
        '-n'   or '--nameonly'              only search package names for match, skip descriptions

""")
