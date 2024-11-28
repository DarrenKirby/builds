"""
    /var/builds/scripts/build_package.py
    Wed Oct 30 22:26:43 UTC 2024

    Class definition of BuildPackage, which builds and installs
    software from source code

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

import importlib.util
import dbm
import sys
import types
import argparse
import os
import glob
import subprocess
from shutil import unpack_archive, rmtree
import subprocess as sp
import shlex
import logging as log

import common_functions as cf
from config import config


class FileInstaller:
    """
    Implements several methods for installing files to the live filesystem
    and keeps track of these files to write a manifest
    """

    def __init__(self, args, seg):
        self.manifest = []
        self.args = args
        # Needed for inst_directory()
        self.seg = seg

        # Useful paths for install functions
        ir = config['install_root']
        self.p = {

            'b': f"{ir}/bin",
            's': f"{ir}/sbin",
            'l': f"{ir}/lib",
            'e': f"{ir}/etc",
            'i': f"{ir}/include",
            'ub': f"{ir}/usr/bin",
            'ue': f"{ir}/usr/etc",
            'us': f"{ir}/usr/sbin",
            'ui': f"{ir}/usr/include",
            'ul': f"{ir}/usr/lib",
            'ule': f"{ir}/usr/libexec",
            'ulb': f"{ir}/usr/local/bin",
            'uls': f"{ir}/usr/local/sbin",
            'uli': f"{ir}/usr/local/include",
            'ull': f"{ir}/usr/local/lib",
            'ush': f"{ir}/usr/share",
            'man1': f"{ir}/usr/share/man/man1",
            'man2': f"{ir}/usr/share/man/man2",
            'man3': f"{ir}/usr/share/man/man3",
            'man4': f"{ir}/usr/share/man/man4",
            'man5': f"{ir}/usr/share/man/man5",
            'man6': f"{ir}/usr/share/man/man6",
            'man7': f"{ir}/usr/share/man/man7",
            'man8': f"{ir}/usr/share/man/man8",

            '_b': self.seg + "/bin",
            '_s': self.seg + "/sbin",
            '_l': self.seg + "/lib",
            '_e': self.seg + "/etc",
            '_i': self.seg + "/include",
            '_ub': self.seg + "/usr/bin",
            '_ue': self.seg + "/usr/etc",
            '_us': self.seg + "/usr/sbin",
            '_ui': self.seg + "/usr/include",
            '_ul': self.seg + "/usr/lib",
            '_ule': self.seg + "/usr/libexec",
            '_ulb': self.seg + "/usr/local/bin",
            '_uls': self.seg + "/usr/local/sbin",
            '_uli': self.seg + "/usr/local/include",
            '_ull': self.seg + "/usr/local/lib",
            '_ush': self.seg + "/usr/share",
            '_man1': self.seg + "/usr/share/man/man1",
            '_man2': self.seg + "/usr/share/man/man2",
            '_man3': self.seg + "/usr/share/man/man3",
            '_man4': self.seg + "/usr/share/man/man4",
            '_man5': self.seg + "/usr/share/man/man5",
            '_man6': self.seg + "/usr/share/man/man6",
            '_man7': self.seg + "/usr/share/man/man7",
            '_man8': self.seg + "/usr/share/man/man8"
        }

    def inst_binary(self, frm: str, to: str) -> None:
        """
        Install a binary to the live filesystem
        """
        if not self.args.test:
            try:
                sp.run(
                    shlex.split(f"install -v -o {cf.config['user']} -g {cf.config['group']} -m 755 -s {frm} {to}"),
                    check=True)
            except sp.CalledProcessError as e:
                cf.red(f"Install of {frm} failed: ")
                print(e)
                log.error("build failure: install of %s failed: %s", frm, e)
                sys.exit(-1)

        abspath = f"{to}/{frm.split('/')[-1]}"
        self.manifest.append(abspath)

    def inst_script(self, frm: str, to: str) -> None:
        """
        Install a script to the live filesystem
        """
        if not self.args.test:
            try:
                sp.run(shlex.split(f"install -v -o {cf.config['user']} -g {cf.config['group']} -m 755 {frm} {to}"),
                       check=True)
            except sp.CalledProcessError as e:
                cf.red(f"Install of {frm} failed: ")
                print(e)
                log.error("build failure: install of %s failed: %s", frm, e)
                sys.exit(-1)

        abspath = f"{to}/{frm.split('/')[-1]}"
        self.manifest.append(abspath)

    def inst_library(self, frm: str, to: str) -> None:
        """
        Install a library to the live filesystem
        """
        if not self.args.test:
            try:
                sp.run(shlex.split(f"install -v -o {cf.config['user']} -g {cf.config['group']} -m 755 {frm} {to}"),
                       check=True)
            except sp.CalledProcessError as e:
                cf.red(f"Install of {frm} failed: ")
                print(e)
                log.error("build failure: install of %s failed: %s", frm, e)
                sys.exit(-1)

        abspath = f"{to}/{frm.split('/')[-1]}"
        self.manifest.append(abspath)

    def inst_header(self, frm: str, to: str) -> None:
        """
        Install a header file to the live filesystem
        """
        if not self.args.test:
            try:
                sp.run(shlex.split(f"install -v -o {cf.config['user']} -g {cf.config['group']} -m 644 {frm} {to}"),
                       check=True)
            except sp.CalledProcessError as e:
                cf.red(f"Install of {frm} failed: ")
                print(e)
                log.error("build failure: install of %s failed: %s", frm, e)
                sys.exit(-1)

        abspath = f"{to}/{frm.split('/')[-1]}"
        self.manifest.append(abspath)

    def inst_manpage(self, frm: str, to: str, compress: bool = True) -> None:
        """
        Compress and install a manpage to the live filesystem
        """
        if not self.args.test:
            try:
                if compress:
                    sp.run(shlex.split(f"bzip2 {frm}"), check=True)
                    frm += ".bz2"
                sp.run(
                    shlex.split(f"install -Dv -o {cf.config['user']} -g {cf.config['group']} -m 644 {frm} {to}"),
                    check=True)
            except sp.CalledProcessError as e:
                cf.red(f"Install of {frm} failed: ")
                print(e)
                log.error("build failure: install of %s failed: %s.", frm, e)
                sys.exit(-1)

        abspath = f"{to}/{frm.split('/')[-1]}"
        self.manifest.append(abspath)

    def inst_symlink(self, target: str, name: str) -> None:
        """
        Make a symbolic link in the live filesystem
        """
        if not self.args.test:
            try:
                sp.run(shlex.split(f"ln -srvf {target} {name}"), check=True)
            except sp.CalledProcessError as e:
                cf.red(f"Install of {name} failed: ")
                print(e)
                log.error("build failure: symbolic link of %s failed: %s.", name, e)
                sys.exit(-1)

        abspath = name
        self.manifest.append(abspath)

    def inst_directory(self, src: str, dst: str) -> None:
        """
        Recursively install a directory of files

        This is intended to be used with packages that create
        deep nested directories of library files or other data
        """
        if not self.args.test:
            try:
                # os.rename fails if destdir is not empty
                if os.path.exists(dst):
                    # Check if the directory is populated with files or subdirectories
                    if any(os.scandir(dst)):  # True if directory is not empty
                        for item in os.scandir(dst):
                            item_path = os.path.join(dst, item.name)
                            if item.is_file() or item.is_symlink():
                                os.unlink(item_path)
                            elif item.is_dir():
                                rmtree(item_path)
                else:
                    # os.rename fails if intermediate directories do not exist.
                    os.makedirs(dst, exist_ok=True)
                os.rename(src, dst)
            except OSError as e:
                cf.red("Call to inst_directory() failed: ")
                print(e)
                log.error("build failure: call to inst_directory() failed: %s", e)
                sys.exit(-1)

        # If we are using --test and the files are not actually installed
        # we still need to generate a manifest
        if self.args.test:
            seg_files = self._list_all_paths(src)
            real_paths = []
            for file in seg_files:
                file = file.replace(self.seg, config['install_root'])
                real_paths.append(file)
        else:
            real_paths = self._list_all_paths(dst)
        self.manifest += real_paths

    def inst_config(self, frm: str, to: str) -> None:
        """
        Install a configuration file to the live filesystem.
        """
        if not self.args.test:
            try:
                sp.run(shlex.split(f"install -bv -o {cf.config['user']} -g {cf.config['group']} -m 644 {frm} {to}"),
                       check=True)
            except sp.CalledProcessError as e:
                cf.red(f"Install of {frm} failed: ")
                print(e)
                log.error("build failure: install of %s failed: %s", frm, e)
                sys.exit(-1)

        abspath = f"{to}/{frm.split('/')[-1]}"
        self.manifest.append(abspath)

    def inst_file(self, frm: str, to: str, mode: int = 644) -> None:
        """
        Install a generic file to the live filesystem
        with 644 permisions
        """
        if to[-1] == '/':
            absfile = f"{to}{frm.split('/')[-1]}"
            to = absfile
        else:
            absfile = to

        if not self.args.test:
            try:
                # os.makedirs(absdir, exist_ok=True)
                sp.run(
                    shlex.split(f"install -Dv -o {cf.config['user']} -g {cf.config['group']} -m {mode} {frm} {to}"),
                    check=True)
            except sp.CalledProcessError as e:
                cf.red(f"Install of {frm} failed: ")
                print(e)
                log.error("build failure: install of %s failed: %s", frm, e)
                sys.exit(-1)

        self.manifest.append(absfile)

    @staticmethod
    def do(cmd: str) -> int:
        """
        Helper function for running shell commands in a build script.
        """
        try:
            sp.run(shlex.split(cmd), check=True)
            return 0
        except sp.CalledProcessError as e:
            cf.red(f"command: {cmd} failed: ")
            print(e)
            log.error("build failure: command '%s' failed: %s", cmd, e)
            sys.exit(-1)

    @staticmethod
    def _list_all_paths(directory_path):
        all_paths = []
        for root, dirs, files in os.walk(directory_path):
            # Add directories with a trailing slash
            for dir_name in dirs:
                all_paths.append(os.path.join(root, dir_name) + '/')
            for file_name in files:
                all_paths.append(os.path.join(root, file_name))
            all_paths.append(root)
        return cf.uniq_list(all_paths)


# pylint: disable=too-many-instance-attributes
class BuildPackage(FileInstaller):
    """
    Implements the main logic for building packages
    """

    def __init__(self, build: str, args: argparse.Namespace) -> None:
        """
         The '__init__' and '_resolve_paths' methods create a bunch of useful
         instance variables which can be used in the build scripts.
         Assuming package 'tar' and source tarball 'tar-1.28.tar.xz' they expand
         as such (also assuming $builds_root is '/var/builds'):

         build       = 'app-arch/tar'
         name        = 'tar'
         version     = '1.28'
         sha256sum   = '9599b22ecd1d5787ad7d3b7bf0c59f312b3396d1e281175dd1f8a4014da621ff'
         src_url     = 'http://ftp.gnu.org/gnu/tar/tar-1.28.tar.xz'
         builds_root = '/var/builds'
         build_dir   = '/var/builds/app-arch/tar'
         build_file  = '/var/builds/app-arch/tar/tar-1.28.build.py'
         work_dir    = '/var/builds/app-arch/tar/work'
         seg_dir     - '/var/builds/app-arch/tar/work/seg'
         package     = 'tar-1.28.tar.xz'
         package_dir = 'tar-1.28'

        """
        self.build = build
        self.name = build.split('/')[1]
        with dbm.open(config['db_file']) as db:
            a = db[self.name].decode().split(";")

        self.version = a[1]
        self.sha256sum = a[2]
        self.src_url = a[3]

        self._resolve_paths()
        super().__init__(args, self.seg_dir)
        # Load build_file methods as a module
        self._load_buildfile_methods()

    def fetch(self) -> None:
        """
        Fetch the package source and check sha256sum
        """
        os.chdir(config['distfiles'])

        if hasattr(self, 'fetch_prehook'):
            self.fetch_prehook()

        cf.download(self.src_url, self.package)

        cf.bold("Checking sha256sum...")

        if cf.get_sha256sum(self.package) == self.sha256sum:
            cf.green("sha256sum matches ;-)")
        else:
            cf.red(f"sha256sum of download {self.package} does not match!")
            log.critical(f"build failure: sha256sum  of {self.package} does not match")
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

        if os.path.exists(self.work_dir):
            cf.yellow(f"{self.work_dir} already exists!")
            if input("Overwrite (y/n) ") in ['n', 'N', 'no', 'No']:
                cf.red("Aborting...")
                log.warning(f"build failure: build of {self.package} aborted due to existing work directory")
                sys.exit(5)
            else:
                rmtree(self.work_dir)

        os.mkdir(self.work_dir)
        os.chdir(self.work_dir)
        unpack_archive(f"{config['distfiles']}/{self.package}", ".")
        cf.green("Source tree installed.")

        if hasattr(self, 'install_source_posthook'):
            self.install_source_posthook()

    def configure_src(self) -> None:
        """
        Configure the source code and build environment
        """
        print(f"Effective UID (from inside configure_src()): {os.geteuid()}")
        os.chdir(self.package_dir)
        cf.bold("Configuring package...")
        print()
        if hasattr(self, 'configure'):
            if self.configure() == 0:
                print()
                cf.green("Package successfully configured.")
            else:
                cf.red("Configure failed")
                cf.log.critical(f"build failure: configure of {self.name} {self.version} failed")
                sys.exit(12)
        else:
            cf.bold("Nothing to configure.")

    def make_src(self) -> None:
        """
        Compile and link the source code.
        """
        cf.bold("Running `make`...")
        print()

        if hasattr(self, 'make'):
            if self.make() == 0:
                print()
                cf.green("`make` successful.")
            else:
                cf.red("`make` failed")
                cf.log.critical(f"build failure: make of {self.name} {self.version} failed")
                sys.exit(13)
        else:
            cf.bold("Nothing to make.")

    def make_inst(self) -> None:
        """
        Install the compiled program into a segregated directory.
        """
        # Make directory as 'builds'
        os.mkdir(self.seg_dir)

        if hasattr(self, 'make_install'):
            cf.green("Installing components into segregated directory...")
            print()
            if self.make_install() != 0:
                cf.red("`make install` failed")
                cf.log.critical(f"build failure: make of {self.name}  {self.version} failed")
                sys.exit(13)
            print()

    def inst(self) -> None:
        """
        Install the program files into the live filesystem.

        make_install() MUST be defined in the package.build.py file.
        """
        if hasattr(self, 'install'):
            cf.green("Installing components into live filesystem...")
            self.install()
        else:
            cf.red(f"{self.build_file} has no 'install()' method defined")
            cf.yellow("All build files must define `install()`")
            cf.log.critical(f"build failure: {self.build_file.split('/')[-1]} has no install() method defined")
            sys.exit(5)

        if self.args.verbose:
            print()
            cf.green(f"Files installed for {self.name} {self.version}: ")
            for filename in sorted(self.manifest):
                cf.bold(f"\t{filename}")

    def cleanup(self) -> None:
        """
        Remove the source tree and work directory, and write the manifest

        This is also a good place to perform any other necessary
        post-installation tasks
        """
        if hasattr(self, 'cleanup_prehook'):
            self.cleanup_prehook()

        print()
        with cf.PrivDropper:
            cf.green("Writing manifest file...")
            if self._write_manifest_file():
                print(">>> ...done.")

        if not self.args.dontclean:
            cf.bold("Cleaning up work directory...")
            os.chdir(self.build_dir)
            rmtree(self.work_dir)

        if hasattr(self, 'cleanup_posthook'):
            self.cleanup_posthook()

        cf.green("Clean up successful")

    # The following methods are 'private', that is, they are
    # not intended for use outside this class.

    def _write_manifest_file(self):
        manifest_file = f"{config['builds_root']}/{self.build}/"
        manifest_file += f"{self.package_dir}.manifest"

        try:
            with open(manifest_file, 'w', encoding='utf-8') as f:
                for file in sorted(self.manifest):
                    f.write(f"{file}\n")
        except IOError as e:
            cf.red(f"Error writing: {manifest_file}")
            log.warning(f"Could not write: {manifest_file}")
            print(e)
            return False
        return True

    def _resolve_paths(self) -> None:
        """
        Resolve pathnames and create useful instance attributes.
        """
        self.build_dir = f"{config['builds_root']}/{self.build}"
        self.builds_root = config['builds_root']
        self.build_file = f"{self.build_dir}/{self.name}-{self.version}.build.py"
        self.work_dir = f"{config['builds_root']}/{self.build}/work"
        self.seg_dir = f"{self.work_dir}/seg"
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
        module_globals['subprocess'] = subprocess  # Inject subprocess into the namespace
        module_globals['glob'] = glob  # Inject glob into the namespace

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
            cf.red(f"Cannot find build file at {path}")
            cf.log.critical(f"build failure: {self.build_file.split('/')[-1]} not found - aborting")
            sys.exit(25)

        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)

        return module
