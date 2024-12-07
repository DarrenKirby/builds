"""
    /var/builds/scripts/uninstall.py
    Tue Nov 19 03:53:10 UTC 2024

    Core logic for uninstalling files and packages.

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
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import argparse
import os
from pathlib import Path
import shutil
import sys
import logging as log

from config import config
import common_functions as cf
import dep_resolve


class Uninstaller:
    """
    Core logic for uninstalling files and packages.
    """

    def __init__(self, manifest_file: str, args: argparse.Namespace):
        self.manifest_file = manifest_file
        # Get package longname and version from manifest file name
        parts = self.manifest_file.split("/")
        self.package = "/".join(parts[-3:-1])
        self.version = parts[-1].split("-")[1].rsplit(".", 1)[0]

        self.manifest_list = cf.get_manifest(self.manifest_file)
        self.manifest = [Path(file) for file in self.manifest_list]
        self.args = args
        self.backup_root = f"{cf.config['builds_root']}/{self.package}/backup.{self.version}"
        print(self.backup_root)

    def backup(self):
        """
        Back up files and directories listed in the manifest to self.backup_root.
        """
        backup_dir = Path(self.backup_root)
        # Ensure the backup root directory exists
        backup_dir.mkdir(parents=True, exist_ok=True)

        for item in self.manifest:
            # Resolve the relative path within the backup root
            relative_path = item.relative_to("/")
            target_path = backup_dir / relative_path

            if item.is_symlink():
                # Handle symbolic links
                link_target = item.readlink()
                target_path.parent.mkdir(parents=True, exist_ok=True)
                target_path.symlink_to(link_target)
            elif item.is_file():
                # Handle files
                target_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, target_path)
            elif item.is_dir():
                # Handle directories
                target_path.mkdir(parents=True, exist_ok=True)
            else:
                print(f"Skipping unknown file type: {item}")

    def delete(self):
        """
        Delete all files listed in the manifest
        """
        for path in self.manifest:
            if path.is_symlink():
                # Handle symbolic links
                if self.args.verbose:
                    cf.print_green("Deleting link:      ")
                    cf.print_bold(f"{path}\n")
                path.unlink()
            elif path.is_dir():
                # Handle directories
                if self.args.verbose:
                    cf.print_green("Deleting directory: ")
                    cf.print_bold(f"{path}\n")
                shutil.rmtree(path)
            elif path.is_file():
                # Handle files
                if self.args.verbose:
                    cf.print_green(f"Deleting file:      ")
                    cf.print_bold(f"{path}\n")
                path.unlink()
            else:  # Already deleted
                pass

    def delete_manifest_file(self):
        """
        Delete the manifest file.
        """
        os.remove(self.manifest_file)
        if self.args.verbose:
            print()
            cf.print_green("Removed: ")
            cf.bold(self.manifest_file + "\n")

    def delete_from_installed_file(self):
        """
        Removes the package from sets/installed.
        """
        cf.delete_from_installed(self.package)


def do_uninstall(args: argparse.Namespace) -> None:
    """
    Uninstall a package
    """
    for pkg in args.pkg_atom:
        pkg_info = cf.get_installed_version(pkg)
        c, n = pkg_info[0].split('/')
        manifest_file = f"{config['builds_root']}/{c}/{n}/{n}-{pkg_info[1]}.manifest"

        if args.ask:
            print(f"Uninstall package {pkg}? (y/n/quit) ")
            choice = input(">>> ")
            if choice in ['n', 'N', 'no', 'No']:
                cf.yellow(f"skipping uninstall of {pkg}")
                continue
            elif choice in ['q', 'quit', 'Quit']:
                sys.exit(1)

        # Looks like we really want to delete it...
        uninstaller = Uninstaller(manifest_file, args)
        if args.backup:
            uninstaller.backup()
        uninstaller.delete()
        uninstaller.delete_manifest_file()
        with cf.PrivDropper():
            uninstaller.delete_from_installed_file()

        cf.print_bold(f"Package deleted: ")
        cf.green(f" {pkg_info[0]} - {pkg_info[1]}")
        log.warning(f"package uninstalled: {pkg_info[0]} {pkg_info[1]}")
        return


def do_update(args) -> list:
    """
    Update packages with newer versions available
    """
    cli_args = args.pkg_atom
    pkg_atoms = dep_resolve.process_packages(cli_args)
    pkg_to_update = []
    for pkg in pkg_atoms:
        installed_version = cf.get_installed_version(pkg)
        avail_version = cf.get_latest_avail_version(pkg)

        if installed_version[1] == avail_version:
            cf.green(f"{pkg}: Version {installed_version[1]} is already up to date.")
        if cf.VersionComparator().is_lower(installed_version[1], avail_version):
            cf.green(f"{pkg}: Version {installed_version[1]} will be updated to {avail_version}.")
            pkg_to_update.append(f"{pkg}-{avail_version}")

    pkgs_to_update = dep_resolve.resolve_dependencies(pkg_to_update)
    return pkgs_to_update
