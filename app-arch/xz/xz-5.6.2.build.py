#    app-arch/xz/xz-5.6.2.build
#    Tue Oct  8 21:03:01 UTC 2024

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
    return os.system(f"./configure --prefix={self.seg_dir} --disable-static --disable-doc")

def make(self):
    return os.system("make")

def make_install(self):
    return os.system("make install")

def install(self):
    cf.do_lib(f"{self.seg_dir}/lib/liblzma.so.5.6.2", cf.paths['ul'])
    cf.do_sym(f"{cf.paths['ul']}/liblzma.so.5.6.2", f"{cf.paths['ul']}/liblzma.so")
    cf.do_sym(f"{cf.paths['ul']}/liblzma.so.5.6.2", f"{cf.paths['ul']}/liblzma.so.5")

    cf.do_hdr(f"{self.seg_dir}/include/lzma.h", cf.paths['ui'])
    # Recursively copy the header directory
    os.system(f"cp -a {self.seg_dir}/include/lzma {cf.paths['ui']}/lzma")

    cf.do_bin(f"{self.seg_dir}/bin/lzmadec", f"{cf.paths['ub']}")
    cf.do_bin(f"{self.seg_dir}/bin/lzmainfo", f"{cf.paths['ub']}")
    cf.do_bin(f"{self.seg_dir}/bin/xz", f"{cf.paths['ub']}")
    cf.do_bin(f"{self.seg_dir}/bin/xzdec", f"{cf.paths['ub']}")
    cf.do_bin(f"{self.seg_dir}/bin/xzdiff", f"{cf.paths['ub']}")
    cf.do_bin(f"{self.seg_dir}/bin/xzgrep", f"{cf.paths['ub']}")
    cf.do_bin(f"{self.seg_dir}/bin/xzless", f"{cf.paths['ub']}")
    cf.do_bin(f"{self.seg_dir}/bin/xzmore", f"{cf.paths['ub']}")

    cf.do_sym(f"{cf.paths['ub']}/xz", f"{cf.paths['ub']}/lzcat")
    cf.do_sym(f"{cf.paths['ub']}/xz", f"{cf.paths['ub']}/lzma")
    cf.do_sym(f"{cf.paths['ub']}/xz", f"{cf.paths['ub']}/unlzma")
    cf.do_sym(f"{cf.paths['ub']}/xz", f"{cf.paths['ub']}/unxz")
    cf.do_sym(f"{cf.paths['ub']}/xz", f"{cf.paths['ub']}/xzcat")
    cf.do_sym(f"{cf.paths['ub']}/xzdiff", f"{cf.paths['ub']}/lzcmp")
    cf.do_sym(f"{cf.paths['ub']}/xzdiff", f"{cf.paths['ub']}/lzdiff")
    cf.do_sym(f"{cf.paths['ub']}/xzdiff", f"{cf.paths['ub']}/xzcmp")
    cf.do_sym(f"{cf.paths['ub']}/xzgrep", f"{cf.paths['ub']}/lzegrep")
    cf.do_sym(f"{cf.paths['ub']}/xzgrep", f"{cf.paths['ub']}/lzfgrep")
    cf.do_sym(f"{cf.paths['ub']}/xzgrep", f"{cf.paths['ub']}/lzgrep")
    cf.do_sym(f"{cf.paths['ub']}/xzgrep", f"{cf.paths['ub']}/xzegrep")
    cf.do_sym(f"{cf.paths['ub']}/xzgrep", f"{cf.paths['ub']}/xzfgrep")
    cf.do_sym(f"{cf.paths['ub']}/xzless", f"{cf.paths['ub']}/lzless")
    cf.do_sym(f"{cf.paths['ub']}/xzmore", f"{cf.paths['ub']}/lzmore")

    cf.do_man(f"{self.seg_dir}/share/man/man1/lzcat.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/lzcmp.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/lzdiff.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/lzegrep.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/lzfgrep.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/lzgrep.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/lzless.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/lzma.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/lmzadec.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/lzmainfo.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/lzmore.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/unlmza.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/unxz.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/xz.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/xzcat.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/xzcmp.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/xzdec.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/xzdiff.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/xzegrep.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/xzfgrep.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/xzgrep.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/xzless.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/xzmore.1", cf.paths['man1'])

"""
/usr/lib/liblzma.so.5.6.2
/usr/lib/liblzma.so
/usr/lib/liblzma.so.5
/usr/include/lzma.h
/usr/include/lzma/
/usr/include/lzma/base.h
/usr/include/lzma/bcj.h
/usr/include/lzma/block.h
/usr/include/lzma/check.h
/usr/include/lzma/container.h
/usr/include/lzma/delta.h
/usr/include/lzma/filter.h
/usr/include/lzma/hardware.h
/usr/include/lzma/index.h
/usr/include/lzma/index-hash.h
/usr/include/lzma/lzma12.h
/usr/include/lzma/stream_flags.h
/usr/include/lzma/version.h
/usr/include/lzma/vli.h
/usr/bin/lzmadec
/usr/bin/lzmainfo
/usr/bin/xz
/usr/bin/xzdec
/usr/bin/xzdiff
/usr/bin/xzgrep
/usr/bin/xzless
/usr/bin/xzmore
/usr/bin/lzcat
/usr/bin/lzma
/usr/bin/unlzma
/usr/bin/unxz
/usr/bin/xzcat
/usr/bin/lzcmp
/usr/bin/lzegrep
/usr/bin/lzfgrep
/usr/bin/lzgrep
/usr/bin/xzegrep
/usr/bin/xzfgrep
/usr/bin/lzless
/usr/bin/lzmore
/usr/bin/xzcmp
/usr/bin/lzdiff
/usr/share/man/man1/lzcat.1.bz2
/usr/share/man/man1/lzcmp.1.bz2
/usr/share/man/man1/lzdiff.1.bz2
/usr/share/man/man1/lzegrep.1.bz2
/usr/share/man/man1/lzfgrep.1.bz2
/usr/share/man/man1/lzgrep.1.bz2
/usr/share/man/man1/lzless.1.bz2
/usr/share/man/man1/lzma.1.bz2
/usr/share/man/man1/lmzadec.1.bz2
/usr/share/man/man1/lzmainfo.1.bz2
/usr/share/man/man1/lzmore.1.bz2
/usr/share/man/man1/unlmza.1.bz2
/usr/share/man/man1/unxz.1.bz2
/usr/share/man/man1/xz.1.bz2
/usr/share/man/man1/xzcat.1.bz2
/usr/share/man/man1/xzcmp.1.bz2
/usr/share/man/man1/xzdec.1.bz2
/usr/share/man/man1/xzdiff.1.bz2
/usr/share/man/man1/xzegrep.1.bz2
/usr/share/man/man1/xzfgrep.1.bz2
/usr/share/man/man1/xzgrep.1.bz2
/usr/share/man/man1/xzless.1.bz2
/usr/share/man/man1/xzmore.1.bz2
"""
