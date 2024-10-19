"""
#    /usr/builds/scripts/dep_resolve.py
#    Mon Sep 30 02:10:47 UTC 2024

#    Naïve dependency resolver
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
"""

import dbm
import sys
import glob
import argparse

import common_functions as cf


def resolve_dependencies(args: argparse.Namespace, config: dict) -> list:
    """
    Translate package names into atoms, and check for dependencies
    """
    atoms = []
    pkgs_to_build = []
    with dbm.open(config['db_file']) as db:
        for arg in args.pkg_atom:
            if arg.find('/') != -1:
                db_string = db[arg.split('/')[1]].decode()
                pkg_name = db_string.split(',')[0]
                # atom not in db...
                if not pkg_name == arg:
                    cf.red(f"{arg} does not appear to be a valid package atom.")
                    cf.yellow(f"Try: 'bld search {arg}'")
                    sys.exit(2)

            else:
                try:
                    db_string = db[arg].decode()

                except IndexError:
                    cf.red(f"'{arg}' does not appear to be a valid package name.")
                    cf.yellow(f"Try: 'bld search {arg}'")
                    sys.exit(2)
            # Append tuple of atom and version
            db_list = db_string.split(',')
            atoms.append((db_list[0], db_list[1]))

    # This is a _REALLY_ naive implementation of a dependency tree
    # This will have to be refactored and improved when the rest
    # of the scaffolding is up...
    for atom in atoms:
        build_file = glob.glob(f"{config['builds_root']}/{atom[0]}/*.build.py")[0]
        with open(build_file, 'r', encoding='utf-8') as fh:
            lines = fh.readlines()
            for line in lines:
                if line.startswith('depend'):
                    pkgs = line.split('=')[-1].strip()
                    pkgs = pkgs[1:-1]  # remove quotes
                    for pkg in pkgs.split(','):
                        with dbm.open(config['db_file']) as db:
                            db_string = db[pkg].decode()
                            db_list = db_string.split(",")

                            # We do not yet distinguish between build dependencies and run dependencies,
                            # (let alone optional dependencies) so for now we just insert dependencies
                            # at the beginning of the list so that they get built first.
                            pkgs_to_build.insert(0, (db_list[0], db_list[1]))

    pkgs_to_build += atoms
    return pkgs_to_build
