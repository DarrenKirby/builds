#    app-util/less/less-661.build.py
#    Thu Nov 14 19:10:05 UTC 2024

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
    return os.system("./configure --prefix=/usr")


def make(self):
    return os.system(f"make {cf.config['makeopts']}")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_binary(f"{self.p['_ub']}/less", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/lessecho", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/lesskey", self.p['ub'])

    self.inst_manpage(f"{self.p['_man1']}/less.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/lessecho.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/lesskey.1", self.p['man1'])
