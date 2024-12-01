"""
    /var/builds/scripts/search_package.py
    Thu Oct 24 02:29:05 UTC 2024

    Search the db file and logs for package information

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
import re
import sys
from datetime import datetime

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
                    name = k.decode('utf-8')
                if isinstance(db[k], bytes):
                    val = db[k].decode('utf-8')
                a = val.split(";")

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


def parse_log(package_name: str, log_file: str = "builds.log") -> list[dict]:
    """
    Parse builds.log for lines matching package_name.
    """
    results = []
    with open(log_file, "r") as log_f:
        lines = log_f.readlines()

    for i, line in enumerate(lines):
        if "build started" in line and package_name in line:
            # Extract the start time and package version
            start_time_str = re.search(r"\| (.*?) \|", line).group(1)
            start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
            # package_version = re.search(rf"{package_name} ([^\s]+)", line).group(1)
            package_version = re.search(rf"{package_name} (\S+)", line).group(1)

            # Check the next relevant lines
            for j in range(i + 1, len(lines)):
                next_line = lines[j]
                if package_name not in next_line:
                    break
                if "build complete" in next_line:
                    # Extract build duration
                    duration = re.search(r"in ([\d:.]+)", next_line).group(1)
                    results.append({
                        "status": "complete",
                        "start_time": start_time,
                        "package": package_name,
                        "version": package_version,
                        "duration": duration
                    })
                    break
                elif "build failure:" in next_line:
                    # Extract failure reason from the consistent token
                    failure_reason = next_line.split("build failure:", 1)[1].strip()
                    results.append({
                        "status": "failed",
                        "start_time": start_time,
                        "package": package_name,
                        "version": package_version,
                        "failure_reason": failure_reason
                    })
                    break

    # Sort results by start_time in descending order (most recent first)
    sorted_results = sorted(results, key=lambda x: x["start_time"], reverse=True)
    return sorted_results


def format_results(results: list[dict]) -> None:
    """
    Take the results of parse_log() and print them in human-readable format.
    """
    for result in results:
        start_time_formatted = result["start_time"].strftime("%a, %b %d, %Y at %I:%M%p")
        if result["status"] == "complete":
            # Convert duration to human-readable format
            duration_parts = result["duration"].split(":")
            duration_parts[-1] = duration_parts[-1].split(".")[0]
            hours, minutes, seconds = map(int, duration_parts)
            duration_text = []
            if hours > 0:
                duration_text.append(f"{hours} hours")
            if minutes > 0:
                duration_text.append(f"{minutes} minutes")
            if seconds > 0:
                duration_text.append(f"{seconds} seconds")
            duration_readable = ", ".join(duration_text)
            print(f"Build of {result['package']} {result['version']} started on {start_time_formatted}")
            print(f"Build of {result['package']} {result['version']} complete in {duration_readable}.")
            print()
        elif result["status"] == "failed":
            print(f"Build of {result['package']} {result['version']} started on {start_time_formatted}")
            print(f"Build of {result['package']} {result['version']} failed: {result['failure_reason']}")
            print()


def do_info(args):
    """
    Print information about an installed package
    """
    to_get_info = args.pkg_atom

    for pkg in to_get_info:
        inst = None
        pkg_info = cf.get_db_info(pkg)

        installed_version = cf.get_installed_version(pkg)

        if installed_version == [None]:
            inst = False
            cf.yellow(f"{pkg} is not currently installed")
        else:
            inst = True
            cf.print_bold("Current installed version of ")
            cf.print_green(installed_version[0])
            cf.print_bold(" is ")
            cf.print_green(installed_version[1])
            print("\n")

        cf.print_bold("Current database information:")
        print()
        print_pkg_info(pkg_info[1:])

        cf.print_bold("Local builds information:")
        print()
        results = parse_log(pkg, config['log_file'])
        if results:
            format_results(results)
        else:
            print(f"No builds found for package {pkg}.")

        if args.verbose and inst:
            manifest_file = f"{cf.config['builds_root']}/{installed_version[0]}/"
            manifest_file += f"{pkg_info[0]}-{pkg_info[2]}.manifest"

            manifest = cf.get_manifest(manifest_file)
            manifest_length = len(manifest)
            cf.print_bold(f"{manifest_length} files installed by {pkg}: \n")

            if manifest_length > 30:
                # Only show head and tail of large manifests
                for line in manifest[0:15]:
                    print(f">>> {line}")
                print()
                print("     ...")
                print()
                for line in manifest[-16:]:
                    print(f">>> {line}")
            else:
                for line in manifest:
                    print(f">>> {line}")
            print()
