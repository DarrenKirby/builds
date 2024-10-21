#    app-arch/zlib/zlib-1.3.1.build.py
#    Thu Oct 3 20:44:51 UTC 2024

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
    cf.do_lib(f"{self.seg_dir}/lib/libz.so.1.3.1", cf.paths['ul'])
    cf.do_sym(f"{cf.paths['ul']}/libz.so.1.3.1", f"{cf.paths['ul']}/libz.so.1")
    cf.do_sym(f"{cf.paths['ul']}/libz.so.1.3.1", f"{cf.paths['ul']}/libz.so")
    cf.do_hdr(f"{self.seg_dir}/include/zconf.h", cf.paths['ui'])
    cf.do_hdr(f"{self.seg_dir}/include/zlib.h", cf.paths['ui'])
    cf.do_man(f"{self.seg_dir}/share/man/man3/zlib.3", cf.paths['man3'])


"""
/usr/lib/libz.so.1.3.1
/usr/lib/libz.so.1
/usr/lib/libz.so
/usr/include/zconf.h
/usr/include/zlib.h
/usr/share/man/man3/zlib.3.bz2
"""
