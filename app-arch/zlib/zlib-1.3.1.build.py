#    app-arch/zlib/zlib-1.3.1.build.py
#    Thu Oct 31 02:40:37 UTC 2024

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
    return os.system(f"./configure --prefix={self.seg_dir}")


def make(self):
    return os.system("make")


def make_install(self):
    return os.system("make install")


def install(self):
    self.inst_library(f"{self.seg_dir}/lib/libz.so.1.3.1", cf.paths['ul'])
    self.inst_symlink(f"{cf.paths['ul']}/libz.so.1.3.1", f"{cf.paths['ul']}/libz.so.1")
    self.inst_symlink(f"{cf.paths['ul']}/libz.so.1.3.1", f"{cf.paths['ul']}/libz.so")
    self.inst_header(f"{self.seg_dir}/include/zconf.h", cf.paths['ui'])
    self.inst_header(f"{self.seg_dir}/include/zlib.h", cf.paths['ui'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man3/zlib.3", cf.paths['man3'])
