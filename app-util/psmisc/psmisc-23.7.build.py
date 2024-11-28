#    app-util/psmisc/psmisc-23.7.build.py
#    Thu Nov 14 19:05:59 UTC 2024

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
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_binary(f"{self.p['_ub']}/fuser", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/killall", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/peekfd", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/prtstat", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/pslog", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/pstree", self.p['ub'])

    self.inst_symlink(f"{self.p['ub']}/pstree", f"{self.p['ub']}/pstree.x11")

    self.inst_manpage(f"{self.p['_man1']}/fuser.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/killall.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/peekfd.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/prtstat.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/pslog.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/pstree.1", self.p['man1'])
