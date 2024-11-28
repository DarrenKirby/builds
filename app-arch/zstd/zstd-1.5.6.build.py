#    app-arch/zstd/zstd-1.5.6-.build.py
#    Thu Nov 28 00:07:55 UTC 2024

#    Copyright:: (c) 2024
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
    return self.do(f"make prefix={self.seg_dir}")


def make_install(self):
    return self.do(f"make prefix={self.seg_dir} install")


def install(self):
    self.inst_library(f"{self.p['_l']}/libzstd.so.1.5.6", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libzstd.so.1.5.6", f"{self.p['ul']}/libzstd.so")
    self.inst_symlink(f"{self.p['ul']}/libzstd.so.1.5.6", f"{self.p['ul']}/libzstd.so.1")

    self.inst_header(f"{self.p['_i']}/zdict.h", self.p['ui'])
    self.inst_header(f"{self.p['_i']}/zstd.h", self.p['ui'])
    self.inst_header(f"{self.p['_i']}/zstd_errors.h", self.p['ui'])

    self.inst_binary(f"{self.p['_b']}/zstd", f"{self.p['ub']}")
    self.inst_script(f"{self.p['_b']}/zstdgrep", f"{self.p['ub']}")
    self.inst_script(f"{self.p['_b']}/zstdless", f"{self.p['ub']}")

    self.inst_symlink(f"{self.p['ub']}/zstd", f"{self.p['ub']}/unzstd")
    self.inst_symlink(f"{self.p['ub']}/zstd", f"{self.p['ub']}/zstdcat")
    self.inst_symlink(f"{self.p['ub']}/zstd", f"{self.p['ub']}/zstdmt")

    self.inst_manpage(f"{self.seg_dir}/share/man/man1/zstd.1", self.p['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/zstdgrep.1", self.p['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/zstdless.1", self.p['man1'])

    self.inst_symlink(f"{self.p['man1']}/zstd.1.bz2", f"{self.p['man1']}/unzstd.1")
    self.inst_symlink(f"{self.p['man1']}/zstd.1.bz2", f"{self.p['man1']}/zstdcat.1")
