#    app-arch/lz4/lz4-1.10.0.build.py
#    Tue Oct  8 21:47:45 UTC 2024

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


def make(self):
    return os.system(f"make BUILD_STATIC=no PREFIX={self.seg_dir}")

def make_install(self):
    return os.system(f"make BUILD_STATIC=no PREFIX={self.seg_dir} install")

def install(self):
    cf.do_lib(f"{self.seg_dir}/lib/liblz4.so.1.10.0", cf.paths['ul'])
    cf.do_sym(f"{cf.paths['ul']}/liblz4.so.1.10.0", f"{cf.paths['ul']}/liblz4.so.1")
    cf.do_sym(f"{cf.paths['ul']}/liblz4.so.1.10.0", f"{cf.paths['ul']}/liblz4.so")

    cf.do_hdr(f"{self.seg_dir}/include/lz4.h", cf.paths['ui'])
    cf.do_hdr(f"{self.seg_dir}/include/lz4frame.h", cf.paths['ui'])
    cf.do_hdr(f"{self.seg_dir}/include/lz4hc.h", cf.paths['ui'])

    cf.do_bin(f"{self.seg_dir}/bin/lz4", f"{cf.paths['ub']}")
    cf.do_sym(f"{cf.paths['ub']}/lz4", f"{cf.paths['ub']}/lz4c")
    cf.do_sym(f"{cf.paths['ub']}/lz4", f"{cf.paths['ub']}/lz4cat")
    cf.do_sym(f"{cf.paths['ub']}/lz4", f"{cf.paths['ub']}/unlz4")

    cf.do_man(f"{self.seg_dir}/share/man/man1/lz4.1", cf.paths['man1'])
    cf.do_sym(f"{cf.paths['man1']}/lz4.1.bz2", f"{cf.paths['man1']}/lz4c.1")
    cf.do_sym(f"{cf.paths['man1']}/lz4.1.bz2", f"{cf.paths['man1']}/lz4cat.1")
    cf.do_sym(f"{cf.paths['man1']}/lz4.1.bz2", f"{cf.paths['man1']}/unlz4.1")

"""
/usr/lib/liblz4.so.1.10.0
/usr/lib/liblz4.so.1
/usr/lib/liblz4.so
/usr/include/lz4.h
/usr/include/lz4frame.h
/usr/include/lz4hc.h
/usr/bin/lz4
/usr/bin/lz4c
/usr/bin/lz4cat
/usr/bin/unlz4
/usr/share/man/man1/lz4.1.bz2
/usr/share/man/man1/lz4c.1
/usr/share/man/man1/lz4cat.1
/usr/share/man/man1/unlz4.1
"""
