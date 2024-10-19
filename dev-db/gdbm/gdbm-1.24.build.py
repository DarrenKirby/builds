#    dev-db/gdbm/gdbm-1.24.build.py
#    Fri Oct 18 23:27:51 UTC 2024

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
    return os.system(f"./configure --prefix={self.seg_dir} --disable-static --enable-libgdbm-compat")

def make(self):
    return os.system("make")

def make_install(self):
    return os.system("make install")

def install(self):
    cf.do_bin(f"{self.seg_dir}/bin/gdbm_dump", cf.paths['ub'])
    cf.do_bin(f"{self.seg_dir}/bin/gdbm_load", cf.paths['ub'])
    cf.do_bin(f"{self.seg_dir}/bin/gdbmtool", cf.paths['ub'])

    cf.do_lib(f"{self.seg_dir}/lib/libgdbm.so.6.0.0", cf.paths['ul'])
    cf.do_sym(f"{cf.paths['ul']}/libgdbm.so.6.0.0", f"{cf.paths['ul']}/libgdbm.so.6")
    cf.do_sym(f"{cf.paths['ul']}/libgdbm.so.6.0.0", f"{cf.paths['ul']}/libgdbm.so")

    cf.do_lib(f"{self.seg_dir}/lib/libgdbm_compat.so.4.0.0", cf.paths['ul'])
    cf.do_sym(f"{cf.paths['ul']}/libgdbm_compat.so.4.0.0", f"{cf.paths['ul']}/libgdbm_compat.so.4")
    cf.do_sym(f"{cf.paths['ul']}/libgdbm_compat.so.4.0.0", f"{cf.paths['ul']}/libgdbm_compat.so")

    cf.do_hdr(f"{self.seg_dir}/include/dbm.h", cf.paths['ui'])
    cf.do_hdr(f"{self.seg_dir}/include/gdbm.h", cf.paths['ui'])
    cf.do_hdr(f"{self.seg_dir}/include/ndbm.h", cf.paths['ui'])

    cf.do_man(f"{self.seg_dir}/share/man/man3/gdbm.3", cf.paths['man3'])
    cf.do_man(f"{self.seg_dir}/share/man/man3/gdbm_dump.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man3/gdbm_load.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man3/gdbmtool.1", cf.paths['man1'])

"""
/usr/bin/gdbm_dump
/usr/bin/gdbm_load
/usr/bin/gdbmtool
/usr/include/dbm.h
/usr/include/gdbm.h
/usr/include/ndbm.h
/usr/lib/libgdbm.so.6.0.0
/usr/lib/libgdbm.so.6
/usr/lib/libgdbm.so
/usr/lib/libgdbm_compat.so.4.0.0
/usr/lib/libgdbm_compat.so.4
/usr/lib/libgdbm_compat.so
/usr/share/man/man3/gdbm.3.bz2
/usr/share/man/man1/gdbm_dump.1.bz2
/usr/share/man/man1/gdbm_load.1.bz2
/usr/share/man/man1/gdbmtool.1.bz2
"""
