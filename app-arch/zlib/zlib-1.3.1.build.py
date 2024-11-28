#    app-arch/zlib/zlib-1.3.1.build.py
#    Thu Nov 28 00:07:13 UTC 2024

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
    return self.do("./configure --prefix=/usr")


def make(self):
    return self.do("make")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_library(f"{self.p['_ul']}/libz.so.1.3.1", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libz.so.1.3.1", f"{self.p['ul']}/libz.so.1")
    self.inst_symlink(f"{self.p['ul']}/libz.so.1.3.1", f"{self.p['ul']}/libz.so")
    self.inst_header(f"{self.p['_ui']}/zconf.h", self.p['ui'])
    self.inst_header(f"{self.p['_ui']}/zlib.h", self.p['ui'])
    self.inst_manpage(f"{self.p['_man3']}/zlib.3", self.p['man3'])
