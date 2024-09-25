#    /usr/builds/scripts/build_package.py
#    Wed Sep 25 01:10:46 UTC 2024

#    Helper module for the builds source building tree
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
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


import importlib
import dbm
import sys
from os import chdir, mkdir
from os.path import exists
from shutil import unpack_archive, rmtree

import common_functions

class BuildPackage:
    def __init__(self, build):
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

         Note that some packages untar to a non-standard directory name, that is, one
         that cannot be sussed out from the tarball name. In these cases package_dir
         will not be correct until the source_install phase, where it is actually un-tarred.
        """
        self.build = build
        self.name = build.split('/')[1]
        with dbm.open(f"{BUILDS_ROOT}/db/{db_file}") as db:
            a = db[self.name].split(",")

        self.version = a[1]
        self.sha256sum = a[2]
        self.src_url = a[3]

        self._resolve_paths()
        self.build_module = self.load_build_file()


    def load_build_file(self):
        """Dynamically load the package-specific build module"""
        return load_module_from_path("build_module", self.build_file)


    def run_buildfile_method(self, method_name):
        """Helper method to run custom behavior if defined."""
        if self.build_module and hasattr(self.build_file, method_name):
            custom_method = getattr(self.build_file, method_name)
            custom_method(self)


    def fetch(self):
        """Fetch the package source code and check sha256sum"""
        self.run_buildfile_method('fetch_prehook')

        chdir(DISTFILES)
        if exists(self.package):
            bold(f"{self.package} already downloaded...")
        else:
            download(self.source_url, self.package)

        if get_sha256sum(self.package) == self.sha256sum:
            green("sha256sum matches ;-)")
        else:
            red(f"sha256sum of download {self.package} does not match!")
            sys.exit(-1)

        self.run_buildfile_method('fetch_posthook')


    def install_source(self):
        """Extract the source into the work directory"""
        self.run_buildfile_method('unpack_source_prehook')

        mkdir(self.work_dir)
        chdir(self.work_dir)
        unpack_archive(f"{DISTFILES}/{self.package}", self.package_dir)

        self.run_buildfile_method('unpack_source_posthook')


    def configure(self):
        """
        Configure the source code and build environment

        configure() MUST be defined in the package.build file. If the package
        does not need configuration then it is good form to just do:

        def configure():
            print("Nothing to configure")

        """
        self.run_buildfile_method('configure_source')


    def make(self):
        """
        Compile and link the source code.

        make() MUST be defined in the package.build file. If the package
        does not need to compile anything then it is good form to just do:

        def make():
            print("Nothing to make")

        """
        self.run_buildfile_method('make_source')


    def make_install(self):
        """
        Install the compiled program into the live filesystem.

        make_install() MUST be defined in the package.build file.
        """
        self.run_buildfile_method('make_install')


    def cleanup(self):
        """
        Remove the source tree and work directory.

        This is also a good place to perform any other necessary
        post-installation tasks
        """
        self.run_buildfile_method('cleanup_prehook')
        chdir(self.build_dir)
        rmtree(self.work_dir)
        self.run_buildfile_method('cleanup_posthook')

    def _resolve_paths(self):
        self.build_dir = f"{BUILDS_ROOT}/{self.build}"
        self.build_file = f"{self.build_dir}/{self.name}-{self.version}.build"
        self.work_dir = f"{BUILDS_ROOT}/{self.build}/work"
        self.src_url = self.src_url.replace("VVV", self.version)
        self.package = self.src_url.split("/")[-1]
        self.package_dir = f"#{self.name}-#{self.version}"

