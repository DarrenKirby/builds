#    <category>/<name>/<name>.build.py
#    `date --utc`

#    Copyright:: (c) 2024 <name>
#    Author:: <name> (mailto:<email>)

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


# If there are no dependencies then comment this line out,
# otherwise, add all dependencies to this list as strings ie:
# depend=['dev-lang/ruby', 'dev-editor/nano']
# All 'system' packages are implicit dependencies, and do not
# need to be listed here as they are already installed.
depend = []


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


# install() MUST be defined in the build file.
# Use the helper functions in common_functions.py
# to install binaries, scripts, libraries, headers,
# documentation (man pages), and to create symlinks.
def install(self):
    pass


# Use these two as pre/post hooks into the cleanup process
# def fetch_prehook(self):
#     pass
#
# def fetch_posthook(self):
#     pass


# Write each installed file one per line in the commented section below.
# This is the list that `bld uninstall` uses to know which files to remove.
"""
/etc/foo.conf
/usr/bin/foo
/usr/include/foo.h
/usr/lib/libfoo.so
/usr/lib/libfoo.so.5.2
/usr/share/man/man1/foo.1
"""
