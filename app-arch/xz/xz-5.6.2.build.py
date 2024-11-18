#    app-arch/xz/xz-5.6.2.build
#    Thu Nov  7 01:21:57 UTC 2024

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
    return os.system("./configure --prefix=/usr --disable-static --disable-doc")


def make(self):
    return os.system("make")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_library(f"{self.seg_dir}/usr/lib/liblzma.so.5.6.2", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/liblzma.so.5.6.2", f"{self.p['ul']}/liblzma.so")
    self.inst_symlink(f"{self.p['ul']}/liblzma.so.5.6.2", f"{self.p['ul']}/liblzma.so.5")

    self.inst_header(f"{self.seg_dir}/usr/include/lzma.h", self.p['ui'])
    # Recursively copy the header directory
    self.inst_directory(f"{self.seg_dir}/usr/include/lzma/", f"{self.p['ui']}/lzma/")

    self.inst_binary(f"{self.p['_ub']}/lzmadec", f"{self.p['ub']}")
    self.inst_binary(f"{self.p['_ub']}/lzmainfo", f"{self.p['ub']}")
    self.inst_binary(f"{self.p['_ub']}/xz", f"{self.p['ub']}")
    self.inst_binary(f"{self.p['_ub']}/xzdec", f"{self.p['ub']}")
    self.inst_script(f"{self.p['_ub']}/xzdiff", f"{self.p['ub']}")
    self.inst_script(f"{self.p['_ub']}/xzgrep", f"{self.p['ub']}")
    self.inst_script(f"{self.p['_ub']}/xzless", f"{self.p['ub']}")
    self.inst_script(f"{self.p['_ub']}/xzmore", f"{self.p['ub']}")

    self.inst_symlink(f"{self.p['ub']}/xz", f"{self.p['ub']}/lzcat")
    self.inst_symlink(f"{self.p['ub']}/xz", f"{self.p['ub']}/lzma")
    self.inst_symlink(f"{self.p['ub']}/xz", f"{self.p['ub']}/unlzma")
    self.inst_symlink(f"{self.p['ub']}/xz", f"{self.p['ub']}/unxz")
    self.inst_symlink(f"{self.p['ub']}/xz", f"{self.p['ub']}/xzcat")
    self.inst_symlink(f"{self.p['ub']}/xzdiff", f"{self.p['ub']}/lzcmp")
    self.inst_symlink(f"{self.p['ub']}/xzdiff", f"{self.p['ub']}/lzdiff")
    self.inst_symlink(f"{self.p['ub']}/xzdiff", f"{self.p['ub']}/xzcmp")
    self.inst_symlink(f"{self.p['ub']}/xzgrep", f"{self.p['ub']}/lzegrep")
    self.inst_symlink(f"{self.p['ub']}/xzgrep", f"{self.p['ub']}/lzfgrep")
    self.inst_symlink(f"{self.p['ub']}/xzgrep", f"{self.p['ub']}/lzgrep")
    self.inst_symlink(f"{self.p['ub']}/xzgrep", f"{self.p['ub']}/xzegrep")
    self.inst_symlink(f"{self.p['ub']}/xzgrep", f"{self.p['ub']}/xzfgrep")
    self.inst_symlink(f"{self.p['ub']}/xzless", f"{self.p['ub']}/lzless")
    self.inst_symlink(f"{self.p['ub']}/xzmore", f"{self.p['ub']}/lzmore")

    for file in os.listdir(self.p['_man1']):
        self.inst_manpage(f"{self.p['_man1']}/{file}", self.p['man1'])
