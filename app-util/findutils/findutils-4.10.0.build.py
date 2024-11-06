#    app-util/findutils/findutils-4.10.0.build.py
#    Wed Nov  6 00:10:25 UTC 2024

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
    return os.system("./configure --prefix=/usr")


def make(self):
    return os.system("make")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_binary(f"{self.p['_ub']}/find", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/locate", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/updatedb", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/xargs", self.p['ub'])

    self.inst_binary(f"{self.p['_ule']}/frcode", self.p['ule'])

    for file in os.listdir(self.p['_man1']):
        self.inst_manpage(f"{self.p['_man1']}/{file}", self.p['man1'])

    self.inst_manpage(f"{self.p['_man5']}/locatedb.5", self.p['man5'])




