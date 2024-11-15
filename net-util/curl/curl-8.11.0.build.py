#    net-util/curl/curl-8.11.0.build.py
#    `date --utc`

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
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


# If there are no dependencies then comment or delete this line
# out, otherwise, add all dependencies to this variable as strings ie:
# depend="dev-lang/ruby,app-editor/nano"
# All 'system' packages are implicit dependencies, and do not
# need to be listed here as they are (presumably) already installed.
# depend = ""


# Use these two as pre/post hooks into the fetch process
# def fetch_prehook(self):
#     pass
#
# def fetch_posthook(self):
#     pass


# Use these two as pre/post hooks into the source-install process
# def install_source_prehook(self):
#     pass
#
# def install_source_posthook(self):
#     pass


# Use configure() to run configure scripts
# def configure(self):
#     return os.system("./configure --prefix=/usr")


# Use make() to make the package
# def make(self):
#     return os.system("make")


# Use make_install() to install the built files into a segregated directory
# def make_install(self):
#     return os.system(f"make DESTDIR={self.seg_dir} install")

# The above three functions need to return 0 to the caller
# so bld knows the commands ran without error, and can continue.


# install() MUST be defined in the build file.
# Use the helper functions in build_package.py
# to install binaries, scripts, libraries, headers,
# documentation (man pages), and to create symlinks.

# You can also install whole directories, or individual
# files that don't fit the above categories.
# def install(self):
#     self.inst_binary(f"{self.p['_ub']}/fooapp", self.p['ub'])
#     self.inst_library(f"{self.p['_ul']}/libfooapp.so", self.p['ul'])
#     self.inst_header(f"{self.p['_ui']}/libfooapp.h", self.p['ui'])
#     self.inst_manpage(f"{self.p['_man1']}/fooapp.1", self.p['man1'])
#     self.inst_manpage(f"{self.p['_man3']}/libfooapp.3", self.p['man3'])


# Use these two as pre/post hooks into the cleanup process
# def cleanup_prehook(self):
#     pass
#
# def cleanup_posthook(self):
#     pass
