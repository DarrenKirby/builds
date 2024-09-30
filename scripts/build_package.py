"""
    /usr/builds/scripts/build_package.py
    Wed Sep 25 23:30:16 UTC 2024

    Class definition of BuildPackage, which builds and installs
    software from source code

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
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import importlib.util
import dbm
import sys
import argparse
from os import chdir, mkdir
from os.path import exists
from shutil import unpack_archive, rmtree

import common_functions as cf


# pylint: disable=too-many-instance-attributes
class BuildPackage:
    """Implements the main logic for building packages"""
    def __init__(self, build: str, config: dict, args: argparse.Namespace) -> None:
        """
         The '__init__' and '_resolve_paths' methods create a bunch of useful
         instance variables which can be used in the build scripts.
         Assuming package 'tar' and source tarball 'tar-1.28.tar.xz' they expand
         as such (also assuming $builds_root is '/usr/builds'):

         build       = 'app-arch/tar'
         name        = 'tar'
         version     = '1.28'
         sha256sum   = '9599b22ecd1d5787ad7d3b7bf0c59f312b3396d1e281175dd1f8a4014da621ff'
         src_url     = 'http://ftp.gnu.org/gnu/tar/tar-1.28.tar.xz'
         build_dir   = '/usr/builds/app-arch/tar'
         build_file  = '/usr/builds/app-arch/tar/tar-1.28.build'
         work_dir    = '/usr/builds/app-arch/tar/work'
         package     = 'tar-1.28.tar.xz'
         package_dir = 'tar-1.28'

         The config dictionary passed to __init__ also contains some useful
         system-wide values:

         config['builds_root'] = '/usr/builds' (default)
         config['distfiles']   = '/usr/builds/distfiles'
         config['db_file']     = 'builds-stable' (default)
         config['logfile']     = '/usr/builds/builds.log'
         config['cflags']      = empty by default
         config['cxxflags']    = empty by default
        """
        self.config = config
        self.build = build
        self.name = build.split('/')[1]
        with dbm.open(f"{self.config['builds_root']}/db/{self.config['db_file']}") as db:
            a = db[self.name].split(",")

        self.version = a[1]
        self.sha256sum = a[2]
        self.src_url = a[3]

        self._resolve_paths()
        self.build_module = self._load_build_file()

    def fetch(self) -> None:
        """Fetch the package source code and check sha256sum"""
        self._run_buildfile_method('fetch_prehook')

        chdir(self.config['distfiles'])
        if exists(self.package):
            cf.bold(f"...{self.package} already downloaded...")
        else:
            cf.bold(f"...downloading {self.package}")
            cf.download(self.src_url, self.package)

        print("...done. Checking sha256sum...")

        if cf.get_sha256sum(self.package) == self.sha256sum:
            cf.green("sha256sum matches ;-)")
        else:
            cf.red(f"sha256sum of download {self.package} does not match!")
            sys.exit(-1)

        self._run_buildfile_method('fetch_posthook')

    def install_source(self) -> None:
        """Extract the source into the work directory"""
        self._run_buildfile_method('install_source_prehook')

        mkdir(self.work_dir)
        chdir(self.work_dir)
        unpack_archive(f"{self.config['distfiles']}/{self.package}", self.package_dir)

        self._run_buildfile_method('install_source_posthook')

    def configure(self) -> None:
        """
        Configure the source code and build environment

        configure_source() MUST be defined in the package.build file. If the
        package does not need configuration then it is good form to just do:

        def configure_source():
            print("Nothing to configure")

        """
        self._run_buildfile_method('configure_source')

    def make(self) -> None:
        """
        Compile and link the source code.

        make_source() MUST be defined in the package.build file. If the package
        does not need to compile anything then it is good form to just do:

        def make_source():
            print("Nothing to make")

        """
        self._run_buildfile_method('make_source')

    def make_inst(self) -> None:
        """
        Install the compiled program into the live filesystem.

        make_install() MUST be defined in the package.build file.
        """
        self._run_buildfile_method('make_install')

    def cleanup(self) -> None:
        """
        Remove the source tree and work directory.

        This is also a good place to perform any other necessary
        post-installation tasks
        """
        self._run_buildfile_method('cleanup_prehook')
        chdir(self.build_dir)
        rmtree(self.work_dir)
        self._run_buildfile_method('cleanup_posthook')

    def _resolve_paths(self) -> None:
        self.build_dir = f"{self.config['builds_root']}/{self.build}"
        self.build_file = f"{self.build_dir}/{self.name}-{self.version}.build"
        self.work_dir = f"{self.config['builds_root']}/{self.build}/work"
        self.src_url = self.src_url.replace("VVV", self.version)
        self.package = self.src_url.split("/")[-1]
        self.package_dir = f"{self.name}-{self.version}"

    # The following methods are 'private', that is, they are
    # not intended for use outside this class.

    def _load_module_from_path(self, module_name: str, path: str):
        """Read the package.build file and return as eecutable code"""
        spec = importlib.util.spec_from_file_location(module_name, path)
        if spec is None:
            raise ImportError(f"Cannot find module at {path}")
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return module

    def _load_build_file(self):
        """Dynamically load the package-specific build module"""
        return self._load_module_from_path("build_module", self.build_file)

    def _run_buildfile_method(self, method_name: str) -> None:
        """Helper method to run custom behavior if defined."""
        if self.build_module and hasattr(self.build_file, method_name):
            custom_method = getattr(self.build_file, method_name)
            custom_method(self)
