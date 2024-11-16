"""
#    /var/builds/scripts/dep_resolve.py
#    Thu Oct 24 02:23:33 UTC 2024

#    Naïve dependency resolver
#
#    Copyright:: (c) 2024
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
from config import config


def already_installed(p):
    """
    Check to see if dependency is already installed
    """
    if cf.get_installed_version(p) == [None]:
        return False
    return True


def process_set(set_file: str) -> list:
    """
    Read a set file into a list of packages
    """
    with open(f"{config['builds_root']}/sets/{set_file}", 'r', encoding='utf-8') as f:
        try:
            lines = f.readlines()
        except IOError as e:
            cf.yellow(f"cannot open set: {set_file}: ")
            print(e)

    return [line[:-1] for line in lines if line[0] != "#" and line != '\n']


def process_packages(args: argparse.Namespace) -> list:
    """
    Converts package args and set args into a single list
    """
    pkgs = []
    for arg in args.pkg_atom:
        if arg[0] == '@':
            pkgs.extend(process_set(arg[1:]))
        else:
            pkgs.append(arg)
    return pkgs


def get_deps(build_file: str) -> list:
    """
    Get dependancies for each package from build file.
    """
    deps = []
    with open(build_file, 'r', encoding='utf-8') as fh:
        lines = fh.readlines()
        for line in lines:
            if line.startswith('depend'):
                pkgs = line.split('=')[-1].strip()
                pkgs = pkgs[1:-1]  # remove quotes
                for pkg in pkgs.split(','):
                    if not already_installed(pkg):
                        deps.append(pkg)
    return deps


def get_version(package: str) -> tuple[str, str]:
    """
    Return version number in db given a package.
    """
    with dbm.open(config['db_file']) as db:
        if package.find('/') != -1:
            db_string = db[package.split('/')[1]].decode()
            pkg_name = db_string.split(',')[0]
            # atom not in db...
            if not pkg_name == package:
                cf.red(f"{package} does not appear to be a valid package atom.")
                cf.yellow(f"Try: 'bld search {package}'")
                sys.exit(2)

        else:
            try:
                db_string = db[package].decode()

            except IndexError:
                cf.red(f"'{package}' does not appear to be a valid package name.")
                cf.yellow(f"Try: 'bld search {package}'")
                sys.exit(2)
        # Append tuple of atom and version
        db_list = db_string.split(',')
        return db_list[0], db_list[1]


def topological_sort(graph: dict) -> list:
    """
    Perform topological sorting on a dependency graph.
    Ensures that dependencies are built before the packages that depend on them.
    """
    from collections import defaultdict, deque

    # Calculate in-degrees for each node
    in_degree = defaultdict(int)
    for node in graph:
        for dep in graph[node]:
            in_degree[dep] += 1

    # Initialize the queue with nodes that have no incoming edges
    queue = deque([node for node in graph if in_degree[node] == 0])
    sorted_order = []

    while queue:
        current = queue.popleft()
        sorted_order.append(current)

        for dep in graph[current]:
            in_degree[dep] -= 1
            if in_degree[dep] == 0:
                queue.append(dep)

    # Check for cycles
    if len(sorted_order) != len(graph):
        raise ValueError("Circular dependency detected in dependency graph")

    sorted_order.reverse()
    return sorted_order


def resolve_dependencies(args: argparse.Namespace) -> list:
    """
    Resolve package dependencies, perform a topological sort, and
    return a list of (expanded_name, version) tuples in build order.
    """
    pkg_atoms = process_packages(args)  # Initial packages from the command line
    version_dict = {}
    dep_graph = {}

    # Build the initial version dictionary and dependency graph
    for pkg in pkg_atoms:
        name, version = get_version(pkg)
        version_dict[name] = version
        dep_graph[name] = get_deps(f"{config['builds_root']}/{name}/{name.split('/')[-1]}-{version}.build.py")

    # Recursively resolve dependencies
    to_process = list(dep_graph.keys())  # Queue of packages to process
    while to_process:
        current = to_process.pop(0)
        for dep in dep_graph[current]:
            if dep not in dep_graph:  # If dependency hasn't been processed yet
                dep_name, dep_version = get_version(dep)
                version_dict[dep_name] = dep_version
                dep_graph[dep_name] = get_deps(
                    f"{config['builds_root']}/{dep_name}/{dep_name.split('/')[-1]}-{dep_version}.build.py"
                )
                to_process.append(dep_name)  # Add new dependency to processing queue

    # Perform topological sort
    build_order = topological_sort(dep_graph)

    # Construct the final list of (name, version) tuples
    return [(name, version_dict[name]) for name in build_order]
