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
from build_package import BuildPackage

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

        manifest = cf.get_manifest(self.manifest_file)
        self.manifest = [Path(file) for file in manifest]
        self.args = args

    def backup(self):
        pass


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
                path.unlink()  # Remove the symlink itself, not the target
            elif path.is_dir():
                # Handle directories
                if self.args.verbose:
                    cf.print_green("Deleting directory: ")
                    cf.print_bold(f"{path}\n")
                shutil.rmtree(path)  # Recursively delete the directory and its contents
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
    if args.pretend:
        print("Uninstalling:")
        for arg in args.pkg_atom:
            cf.yellow(f"\t{arg}")
        sys.exit(0)

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
        uninstaller.delete()
        uninstaller.delete_manifest_file()
        with cf.PrivDropper():
            uninstaller.delete_from_installed_file()

        cf.print_bold(f"Package deleted: ")
        cf.green(f" {pkg_info[0]} - {pkg_info[1]}")
        log.warning(f"package uninstalled: {pkg_info[0]} - {pkg_info[1]}")
        return

def do_update(args):
    pass
