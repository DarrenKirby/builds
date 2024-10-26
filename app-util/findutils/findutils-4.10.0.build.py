#    app-util/findutils/findutils-4.10.0.build.py
#    Fri Oct 25 01:31:58 UTC 2024

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


# BUG: Default db location must be specified at compile time.
#      How to resolve with temp install directory? As-is, the
#      make_install step will fail on permissions for non-system install
def configure(self):
    return os.system(f"./configure --prefix={self.seg_dir} "
                     f"--localstatedir={self.seg_dir}/var/lib/locate")


def make(self):
    return os.system("make")


def make_install(self):
    return os.system("make install")


def install(self):
    pass


"""
/usr/bin/find
/usr/bin/locate
/usr/bin/updatedb
/usr/bin/xargs
/usr/libexec/frcode
/usr/share/man/man1/find.1
/usr/share/man/man1/flocate.1
/usr/share/man/man1/fupdatedb.1
/usr/share/man/man1/fxargs.1
/usr/share/man/man5/flocatedb.5
"""
