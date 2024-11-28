#    dev-tool/automake/automake-1.17.build.py
#    Wed Oct 23 01:40:25 UTC 2024

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


def configure(self):
    return self.do("./configure --prefix=/usr")


def make(self):
    return self.do("make")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_script(f"{self.p['_ub']}/aclocal", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/aclocal-1.17", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/automake", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/automake-1.17", self.p['ub'])

    self.inst_directory(f"{self.p['_ush']}/aclocal/", f"{self.p['ush']}/aclocal/")
    self.inst_directory(f"{self.p['_ush']}/aclocal-1.17/", f"{self.p['ush']}/aclocal-1.17/")
    self.inst_directory(f"{self.p['_ush']}/automake-1.17/", f"{self.p['ush']}/automake-1.17")

    self.inst_manpage(f"{self.p['_man1']}/aclocal-1.17.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/aclocal.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/automake-1.17.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/automake.1", self.p['man1'])
