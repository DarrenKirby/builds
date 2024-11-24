#    sci-math/mpfr/mpfr-4.2.1.build.py
#    Sun Nov 24 00:21:20 UTC 2024

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
    return os.system("./configure --prefix=/usr --disable-static --enable-thread-safe")


def make(self):
    return os.system(f"make {cf.config['makeopts']}")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_header(f"{self.p['_ui']}/mpf2mpfr.h", self.p['ui'])
    self.inst_header(f"{self.p['_ui']}/mpfr.h", self.p['ui'])

    self.inst_library(f"{self.p['_ul']}/libmpfr.so.6.2.1", self.p['ul'])
    self.inst_symlink(self.p['ul'] + "/libmpfr.so.6.2.1", self.p['ul'] + "/libmpfr.so.6")
    self.inst_symlink(self.p['ul'] + "/libmpfr.so.6.2.1", self.p['ul'] + "/libmpfr.so")

    self.inst_file(self.p['_ul'] + "/pkgconfig/mpfr.pc", self.p['ul'] + "/pkgconfig/")
