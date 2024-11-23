#    dev-tool/bison/bison-3.8.2.build.py
#    Sat Nov 23 00:24:10 UTC 2024

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
    self.inst_script(self.p['_ub'] + "/yacc", self.p['ub'])
    self.inst_binary(self.p['_ub'] + "/bison", self.p['ub'])

    # this library is not very useful, but POSIX requires it
    self.inst_library(self.p['_ul'] + "/liby.a", self.p['ul'])

    # Make sure usr/share/aclocal exists
    os.makedirs(f"{self.p['ush']}/aclocal/", exist_ok=True)
    self.inst_file(self.p['_ush'] + "/aclocal/bison-i18n.m4", self.p['ush'] + "/aclocal/")
    self.inst_directory(f"{self.p['_ush']}/bison/", f"{self.p['ush']}/bison/")

    self.inst_manpage(self.p['_man1'] + "/bison.1", self.p['man1'])
    self.inst_manpage(self.p['_man1'] + "/yacc.1", self.p['man1'])