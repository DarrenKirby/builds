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
import types
import argparse
import os
from os.path import exists
from shutil import unpack_archive, rmtree

import common_functions as cf


# pylint: disable=too-many-instance-attributes
class BuildPackage:
    """
    Implements the main logic for building packages
    """
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
         build_file  = '/usr/builds/app-arch/tar/tar-1.28.build.py'
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
        with dbm.open(f"{self.config['builds_root']}/scripts/{self.config['db_file']}") as db:
            a = db[self.name].decode().split(",")

        self.version = a[1]
        self.sha256sum = a[2]
        self.src_url = a[3]

        self._resolve_paths()

        # Load build_file methods as a module
        self._load_buildfile_methods()

    def fetch(self) -> None:
        """
        Fetch the package source code and check sha256sum
        """

        if hasattr(self, 'fetch_prehook'):
            self.fetch_prehook()

        cf.bold(f"Fetching {self.package}...")

        os.chdir(self.config['distfiles'])
        if exists(self.package):
            cf.bold(f"...{self.package} already downloaded.")
        else:
            cf.bold(f"Fetching {self.package}")
            cf.download(self.src_url, self.package)

        cf.bold("Checking sha256sum...")

        if cf.get_sha256sum(self.package) == self.sha256sum:
            cf.green("sha256sum matches ;-)")
        else:
            cf.red(f"sha256sum of download {self.package} does not match!")
            sys.exit(-1)

        if hasattr(self, 'fetch_posthook'):
            self.fetch_posthook()

    def install_source(self) -> None:
        """
        Extract the source into the work directory
        """

        if hasattr(self, 'install_source_prehook'):
            self.install_source_prehook()

        cf.bold(f"Extracting {self.package} into {self.work_dir}")

        os.mkdir(self.work_dir)
        os.chdir(self.work_dir)
        unpack_archive(f"{self.config['distfiles']}/{self.package}", ".")
        cf.green("Source tree installed.")

        if hasattr(self, 'install_source_posthook'):
            self.install_source_posthook()

    def configure(self) -> None:
        """
        Configure the source code and build environment
        """
        cf.bold("Configuring package...")
        if hasattr(self, 'configure_source'):
            self.configure_source()
            cf.green("Package successfully configured.")
        else:
            cf.bold("Nothing to configure.")


    def make(self) -> None:
        """
        Compile and link the source code.
        """
        cf.bold("Running `make`...")

        if hasattr(self, 'make_source'):
            self.make_source()
            cf.green("`make` successful.")
        else:
            cf.bold("Nothing to make.")

    def make_inst(self) -> None:
        """
        Install the compiled program into the live filesystem.

        make_install() MUST be defined in the package.build file.
        """
        if hasattr(self, 'make_install'):
            self.make_install()
        else:
            cf.red(f"{self.build_file} has no `make_install()` method defined")
            cf.yellow("All build files must define `make_install()`")
            self.cleanup()
            sys.exit(5)

    def cleanup(self) -> None:
        """
        Remove the source tree and work directory.

        This is also a good place to perform any other necessary
        post-installation tasks
        """
        if hasattr(self,'cleanup_prehook'):
            self.cleanup_prehook()

        cf.bold("Cleaning up work directory...")

        os.chdir(self.build_dir)
        rmtree(self.work_dir)

        cf.green("Clean up successful")
        cf.green(f"Build of {self.name} {self.version} complete.")

        if hasattr(self, 'cleanup_posthook'):
            self.cleanup_posthook()

    # The following methods are 'private', that is, they are
    # not intended for use outside this class.

    def _resolve_paths(self) -> None:
        """
        Resolve pathnames and create useful instance attributes.
        """
        self.build_dir = f"{self.config['builds_root']}/{self.build}"
        self.build_file = f"{self.build_dir}/{self.name}-{self.version}.build.py"
        self.work_dir = f"{self.config['builds_root']}/{self.build}/work"
        self.src_url = self.src_url.replace("VVV", self.version)
        self.package = self.src_url.split("/")[-1]
        self.package_dir = f"{self.name}-{self.version}"

    def _load_buildfile_methods(self):
        """
        Bind the build_file methods to the class instance
        """

        # Dynamically import the package-specific module
        module = self._load_module_from_path('bld_mod', self.build_file)

        # Inject any required globals into the module's namespace
        module_globals = module.__dict__
        module_globals['os'] = os  # Inject os into the namespace
        module_globals['cf'] = cf  # Inject cf into the namespace

        # Iterate over methods defined in the module
        for name in dir(module):
            if not name.startswith("_"):  # Ignore private methods
                method = getattr(module, name)
                if callable(method):
                    # Bind the method to the class instance
                    bound_method = types.MethodType(method, self)
                    # Set it as a method on the class instance
                    setattr(self, name, bound_method)

    def _load_module_from_path(self, module_name: str, path: str):
        """
        Read the package.build.py file and return as a module
        """
        spec = importlib.util.spec_from_file_location(module_name, path)

        if spec is None:
            raise ImportError(f"Cannot find module at {path}")

        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)

        return module
