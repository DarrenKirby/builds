#    app-arch/zstd/zstd-1.5.6-.build.py
#    Tue Oct  8 23:59:38 UTC 2024

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
    return os.system(f"make prefix={self.seg_dir}")

def make_install(self):
    return os.system(f"make prefix={self.seg_dir} install")

def install(self):
    cf.do_lib(f"{self.seg_dir}/lib/libzstd.so.1.5.6", cf.paths['ul'])
    cf.do_sym(f"{cf.paths['ul']}/libzstd.so.1.5.6", f"{cf.paths['ul']}/libzstd.so")
    cf.do_sym(f"{cf.paths['ul']}/libzstd.so.1.5.6", f"{cf.paths['ul']}/libzstd.so.1")

    cf.do_hdr(f"{self.seg_dir}/include/zdict.h", cf.paths['ui'])
    cf.do_hdr(f"{self.seg_dir}/include/zstd.h", cf.paths['ui'])
    cf.do_hdr(f"{self.seg_dir}/include/zstd_errors.h", cf.paths['ui'])

    cf.do_bin(f"{self.seg_dir}/bin/zstd", f"{cf.paths['ub']}")
    cf.do_bin(f"{self.seg_dir}/bin/zstdgrep", f"{cf.paths['ub']}")
    cf.do_bin(f"{self.seg_dir}/bin/zsrdless", f"{cf.paths['ub']}")

    cf.do_sym(f"{cf.paths['ub']}/zstd", f"{cf.paths['ub']}/unzstd")
    cf.do_sym(f"{cf.paths['ub']}/zstd", f"{cf.paths['ub']}/zstdcat")
    cf.do_sym(f"{cf.paths['ub']}/zstd", f"{cf.paths['ub']}/zstdmt")

    cf.do_man(f"{self.seg_dir}/share/man/man1/zstd.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/zstdgrep.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/zstdless.1", cf.paths['man1'])

    cf.do_sym(f"{cf.paths['man1']}/zstd.1.bz2", f"{cf.paths['man1']}/unzstd.1")
    cf.do_sym(f"{cf.paths['man1']}/zstd.1.bz2", f"{cf.paths['man1']}/zstdcat.1")

"""
/usr/bin/zstd
/usr/bin/zstdgrep
/usr/bin/zstdless
/usr/bin/unzstd
/usr/bin/zstdcat
/usr/bin/zstdmt
/usr/include/zdict.h
/usr/include/zstd.h
/usr/include/zstd_errors.h
/usr/lib/libzstd.so.1.5.6
/usr/lib/libzstd.so.1
/usr/lib/libzstd.so
/usr/share/man/man1/zstd.1.bz2
/usr/share/man/man1/zstdgrep.1.bz2
/usr/share/man/man1/zstdless.1.bz2
/usr/share/man/man1/unzstd.1
/usr/share/man/man1/zstdcat.1
"""
