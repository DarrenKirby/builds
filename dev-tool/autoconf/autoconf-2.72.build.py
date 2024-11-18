#    dev-tool/autoconf/autoconf-2.7.2.build.py
#    Wed Oct 23 01:38:36 UTC 2024

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


def configure(self):
    return os.system("./configure --prefix=/usr")


def make(self):
    return os.system(f"make {cf.config['makeopts']}")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_script(f"{self.p['_ub']}/autoconf", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/autoheader", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/autom4te", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/autoreconf", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/autoscan", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/autoupdate", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/ifnames", self.p['ub'])

    self.inst_directory(f"{self.p['_ush']}/autoconf/", f"{self.p['ush']}/autoconf")

    self.inst_manpage(f"{self.p['_man1']}/autoconf.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/autoheader.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/autom4te.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/autoreconf.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/autoscan.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/autoupdate.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/ifnames.1", self.p['man1'])
