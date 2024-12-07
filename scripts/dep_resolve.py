"""
    /var/builds/scripts/dep_resolve.py
    Sat Nov 16 05:26:26 UTC 2024

    Naïve dependency resolver

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
import sys
import argparse
import logging as log

import common_functions as cf
from config import config


def already_installed(p: str) -> bool:
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


def process_packages(args: list) -> list:
    """
    Converts package args and set args into a single list
    """
    pkgs = []
    for arg in args:
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
    try:
        with open(build_file, 'r', encoding='utf-8') as fh:
            lines = fh.readlines()
            for line in lines:
                if line.startswith('depend'):
                    pkgs = line.split('=')[-1].strip()
                    pkgs = pkgs[1:-1]  # remove quotes
                    for pkg in pkgs.split(','):
                        if not already_installed(pkg):
                            deps.append(pkg)
    except FileNotFoundError:
        cf.red(f"Cannot find {build_file}.")
        sys.exit(3)
    return deps


def get_version(package: str, spec_version: [str, None] = None) -> tuple[str, str]:
    """
    Return version number in db given a package.
    """
    with dbm.open(config['db_file'], flag='r') as db:
        if package.find('/') != -1:
            db_string = db[package.split('/')[1]].decode()
            pkg_name = db_string.split(';')[0]
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
        db_list = db_string.split(';')

        # Check for multiple versions
        if db_list[1].count(",") > 0:
            versions = db_list[1].split(",")
            if spec_version:
                if spec_version not in versions:
                    cf.red(f"{spec_version} is not available for {package}")
                    sys.exit(23)
                else:
                    version = spec_version
            else:
                version = cf.VersionComparator().higher(versions[0], versions[1])
        else:
            version = db_list[1]
        return db_list[0], version


def topological_sort(graph: dict) -> list:
    """
    Perform topological sort on the dependency graph using DFS.
    Detect and report circular dependencies.
    """
    visited = set()
    stack = []
    cycle = []

    def dfs(node, path):
        """
        Perform depth-first search (DFS) to detect cycles and build
        the topological order.
        """
        nonlocal visited, stack, cycle
        if node in path:  # Cycle detected!
            # Include the starting node to complete the cycle
            cycle.extend(path[path.index(node):] + [node])
            return

        if node not in visited:
            visited.add(node)
            path.append(node)
            for neighbor in graph[node]:
                dfs(neighbor, path)
            path.pop()
            stack.append(node)

    for outer_node in graph:
        if outer_node not in visited:
            dfs(outer_node, [])

    if cycle:
        log.critical("Circular dependency detected: %s", ' -> '.join(cycle))
        cf.yellow(f"Circular dependency detected: {' -> '.join(cycle)}")
        cf.red("Aborting build")
        sys.exit(100)

    return stack


def resolve_dependencies(args: [argparse.Namespace, list]) -> list[tuple]:
    """
    Resolve package dependencies, perform a topological sort, and
    return a list of (name, version) tuples in correct build order.
    """
    if type(args) == argparse.Namespace:
        cli_args = args.pkg_atom
    else:
        cli_args = args
    pkg_atoms = process_packages(cli_args)  # Initial packages from the command line
    version_dict = {}
    dep_graph = {}

    # Build the initial version dictionary and dependency graph
    for pkg in pkg_atoms:
        # Normalize to short name
        if pkg.count("/") == 1:
            pkg = pkg.split("/")[1]
        # If version attatched to pkg_atom
        if pkg.count("-") == 1:
            n, v = pkg.split("-")
            try:
                name, version = get_version(n, v)
            except KeyError:
                cf.red(f"{pkg} is not a valid package atom.")
                print(f"Try 'bld search {pkg}'")
                sys.exit(2)
        else:
            try:
                name, version = get_version(pkg)
            except KeyError:
                cf.red(f"{pkg} is not a valid package atom.")
                print(f"Try 'bld search {pkg}'")
                sys.exit(2)
        version_dict[name] = version
        dep_graph[name] = get_deps(f"{config['builds_root']}/{name}/{name.split('/')[-1]}-{version}.build.py")

    # Recursively resolve dependencies
    to_process = list(dep_graph.keys())  # Queue of packages to process
    while to_process:
        current = to_process.pop(0)
        for dep in dep_graph[current]:
            if dep not in dep_graph:
                dep_name, dep_version = get_version(dep)
                version_dict[dep_name] = dep_version
                dep_graph[dep_name] = get_deps(
                    f"{config['builds_root']}/{dep_name}/{dep_name.split('/')[-1]}-{dep_version}.build.py"
                )
                to_process.append(dep_name)  # Add new dependency to processing queue

    # Perform topological sort
    build_order = topological_sort(dep_graph)

    # do_main(), the caller, expects (name, version) tuples
    return [(name, version_dict[name]) for name in build_order]
