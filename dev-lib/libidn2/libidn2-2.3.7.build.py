#    dev-lib/libidn2/libidn2-2.3.7.build.py
#    Sat Nov 16 00:39:45 UTC 2024

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
    return self.do("./configure --prefix=/usr "
                   "--disable-static")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_binary(f"{self.p['_ub']}/idn2", self.p['ub'])

    self.inst_header(f"{self.p['_ui']}/idn2.h", self.p['ui'])

    self.inst_library(f"{self.p['_ul']}/libidn2.so.0.4.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libidn2.so.0.4.0", f"{self.p['ul']}/libidn2.so.0")
    self.inst_symlink(f"{self.p['ul']}/libidn2.so.0.4.0", f"{self.p['ul']}/libidn2.so")

    self.inst_file(f"{self.p['_ul']}/pkgconfig/libidn2.pc", f"{self.p['ul']}/pkgconfig/")

    self.inst_manpage(f"{self.p['_man1']}/idn2.1", self.p['man1'])

    for file in os.listdir(self.p['_man3']):
        self.inst_manpage(f"{self.p['_man3']}/{file}", self.p['man3'])
