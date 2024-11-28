#    sci-math/gmp/gmp-6.3.0.build.py
#    Sun Nov 24 00:15:32 UTC 2024

#    Copyright:: (c)
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
    return self.do("./configure --prefix=/usr --enable-cxx --disable-static")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_header(f"{self.p['_ui']}/gmp.h", self.p['ui'])
    self.inst_header(f"{self.p['_ui']}/gmpxx.h", self.p['ui'])

    self.inst_library(f"{self.p['_ul']}/libgmp.so.10.5.0", self.p['ul'])
    self.inst_symlink(self.p['ul'] + "/libgmp.so.10.5.0", self.p['ul'] + "/libgmp.so")
    self.inst_symlink(self.p['ul'] + "/libgmp.so.10.5.0", self.p['ul'] + "/libgmp.so.10")

    self.inst_library(f"{self.p['_ul']}/libgmpxx.so.4.7.0", self.p['ul'])
    self.inst_symlink(self.p['ul'] + "/libgmpxx.so.4.7.0", self.p['ul'] + "/libgmpxx.so")
    self.inst_symlink(self.p['ul'] + "/libgmpxx.so.4.7.0", self.p['ul'] + "/libgmpxx.so.4")

    self.inst_file(self.p['_ul'] + "/pkgconfig/gmp.pc", self.p['ul'] + "/pkgconfig/")
    self.inst_file(self.p['_ul'] + "/pkgconfig/gmpxx.pc", self.p['ul'] + "/pkgconfig/")
