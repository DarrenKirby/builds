#    app-arch/xz/xz-5.6.2.build
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
    return os.system(f"./configure --prefix={self.seg_dir} --disable-static --disable-doc")

def make(self):
    return os.system("make")

def make_install(self):
    return os.system("make install")

def install(self):
    self.inst_library(f"{self.seg_dir}/lib/liblzma.so.5.6.2", cf.paths['ul'])
    self.inst_symlink(f"{cf.paths['ul']}/liblzma.so.5.6.2", f"{cf.paths['ul']}/liblzma.so")
    self.inst_symlink(f"{cf.paths['ul']}/liblzma.so.5.6.2", f"{cf.paths['ul']}/liblzma.so.5")

    self.inst_header(f"{self.seg_dir}/include/lzma.h", cf.paths['ui'])
    # Recursively copy the header directory
    #os.system(f"cp -a {self.seg_dir}/include/lzma {cf.paths['ui']}/lzma")
    self.inst_directory(f"{self.seg_dir}/include/lzma/", f"{cf.paths['ui']}/lzma/")

    self.inst_binary(f"{self.seg_dir}/bin/lzmadec", f"{cf.paths['ub']}")
    self.inst_binary(f"{self.seg_dir}/bin/lzmainfo", f"{cf.paths['ub']}")
    self.inst_binary(f"{self.seg_dir}/bin/xz", f"{cf.paths['ub']}")
    self.inst_binary(f"{self.seg_dir}/bin/xzdec", f"{cf.paths['ub']}")
    self.inst_binary(f"{self.seg_dir}/bin/xzdiff", f"{cf.paths['ub']}")
    self.inst_binary(f"{self.seg_dir}/bin/xzgrep", f"{cf.paths['ub']}")
    self.inst_binary(f"{self.seg_dir}/bin/xzless", f"{cf.paths['ub']}")
    self.inst_binary(f"{self.seg_dir}/bin/xzmore", f"{cf.paths['ub']}")

    self.inst_symlink(f"{cf.paths['ub']}/xz", f"{cf.paths['ub']}/lzcat")
    self.inst_symlink(f"{cf.paths['ub']}/xz", f"{cf.paths['ub']}/lzma")
    self.inst_symlink(f"{cf.paths['ub']}/xz", f"{cf.paths['ub']}/unlzma")
    self.inst_symlink(f"{cf.paths['ub']}/xz", f"{cf.paths['ub']}/unxz")
    self.inst_symlink(f"{cf.paths['ub']}/xz", f"{cf.paths['ub']}/xzcat")
    self.inst_symlink(f"{cf.paths['ub']}/xzdiff", f"{cf.paths['ub']}/lzcmp")
    self.inst_symlink(f"{cf.paths['ub']}/xzdiff", f"{cf.paths['ub']}/lzdiff")
    self.inst_symlink(f"{cf.paths['ub']}/xzdiff", f"{cf.paths['ub']}/xzcmp")
    self.inst_symlink(f"{cf.paths['ub']}/xzgrep", f"{cf.paths['ub']}/lzegrep")
    self.inst_symlink(f"{cf.paths['ub']}/xzgrep", f"{cf.paths['ub']}/lzfgrep")
    self.inst_symlink(f"{cf.paths['ub']}/xzgrep", f"{cf.paths['ub']}/lzgrep")
    self.inst_symlink(f"{cf.paths['ub']}/xzgrep", f"{cf.paths['ub']}/xzegrep")
    self.inst_symlink(f"{cf.paths['ub']}/xzgrep", f"{cf.paths['ub']}/xzfgrep")
    self.inst_symlink(f"{cf.paths['ub']}/xzless", f"{cf.paths['ub']}/lzless")
    self.inst_symlink(f"{cf.paths['ub']}/xzmore", f"{cf.paths['ub']}/lzmore")

    self.inst_manpage(f"{self.seg_dir}/share/man/man1/lzcat.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/lzcmp.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/lzdiff.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/lzegrep.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/lzfgrep.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/lzgrep.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/lzless.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/lzma.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/lmzadec.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/lzmainfo.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/lzmore.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/unlmza.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/unxz.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/xz.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/xzcat.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/xzcmp.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/xzdec.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/xzdiff.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/xzegrep.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/xzfgrep.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/xzgrep.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/xzless.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/xzmore.1", cf.paths['man1'])
