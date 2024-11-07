#    app-shell/tcsh/tcsh-6.24.13.build.py
#    Thu Nov  7 04:29:59 UTC 2024

#    Copyright:: (c) 2024
#    Author:: Darren Kirby (mailto:Darren Kirby)

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
    return os.system("make")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} install install.man")


def install(self):
    self.inst_binary(f"{self.p['_ub']}/tcsh", self.p['ub'])
    self.inst_manpage(f"{self.p['_man1']}/tcsh.1", self.p['man1'])
