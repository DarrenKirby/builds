#    app-arch/zstd/zstd-1.5.6-.build.py
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


def make(self):
    return os.system(f"make prefix={self.seg_dir}")

def make_install(self):
    return os.system(f"make prefix={self.seg_dir} install")

def install(self):
    self.inst_library(f"{self.seg_dir}/lib/libzstd.so.1.5.6", cf.paths['ul'])
    self.inst_symlink(f"{cf.paths['ul']}/libzstd.so.1.5.6", f"{cf.paths['ul']}/libzstd.so")
    self.inst_symlink(f"{cf.paths['ul']}/libzstd.so.1.5.6", f"{cf.paths['ul']}/libzstd.so.1")

    self.inst_header(f"{self.seg_dir}/include/zdict.h", cf.paths['ui'])
    self.inst_header(f"{self.seg_dir}/include/zstd.h", cf.paths['ui'])
    self.inst_header(f"{self.seg_dir}/include/zstd_errors.h", cf.paths['ui'])

    self.inst_binary(f"{self.seg_dir}/bin/zstd", f"{cf.paths['ub']}")
    self.inst_binary(f"{self.seg_dir}/bin/zstdgrep", f"{cf.paths['ub']}")
    self.inst_binary(f"{self.seg_dir}/bin/zsrdless", f"{cf.paths['ub']}")

    self.inst_symlink(f"{cf.paths['ub']}/zstd", f"{cf.paths['ub']}/unzstd")
    self.inst_symlink(f"{cf.paths['ub']}/zstd", f"{cf.paths['ub']}/zstdcat")
    self.inst_symlink(f"{cf.paths['ub']}/zstd", f"{cf.paths['ub']}/zstdmt")

    self.inst_manpage(f"{self.seg_dir}/share/man/man1/zstd.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/zstdgrep.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/zstdless.1", cf.paths['man1'])

    self.inst_symlink(f"{cf.paths['man1']}/zstd.1.bz2", f"{cf.paths['man1']}/unzstd.1")
    self.inst_symlink(f"{cf.paths['man1']}/zstd.1.bz2", f"{cf.paths['man1']}/zstdcat.1")
