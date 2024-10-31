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
    self.inst_library(f"{self.seg_dir}/lib/liblz4.so.1.10.0", cf.paths['ul'])
    self.inst_symlink(f"{cf.paths['ul']}/liblz4.so.1.10.0", f"{cf.paths['ul']}/liblz4.so.1")
    self.inst_symlink(f"{cf.paths['ul']}/liblz4.so.1.10.0", f"{cf.paths['ul']}/liblz4.so")

    self.inst_header(f"{self.seg_dir}/include/lz4.h", cf.paths['ui'])
    self.inst_header(f"{self.seg_dir}/include/lz4frame.h", cf.paths['ui'])
    self.inst_header(f"{self.seg_dir}/include/lz4hc.h", cf.paths['ui'])

    self.inst_binary(f"{self.seg_dir}/bin/lz4", f"{cf.paths['ub']}")
    self.inst_symlink(f"{cf.paths['ub']}/lz4", f"{cf.paths['ub']}/lz4c")
    self.inst_symlink(f"{cf.paths['ub']}/lz4", f"{cf.paths['ub']}/lz4cat")
    self.inst_symlink(f"{cf.paths['ub']}/lz4", f"{cf.paths['ub']}/unlz4")

    self.inst_manpage(f"{self.seg_dir}/share/man/man1/lz4.1", cf.paths['man1'])
    self.inst_symlink(f"{cf.paths['man1']}/lz4.1.bz2", f"{cf.paths['man1']}/lz4c.1")
    self.inst_symlink(f"{cf.paths['man1']}/lz4.1.bz2", f"{cf.paths['man1']}/lz4cat.1")
    self.inst_symlink(f"{cf.paths['man1']}/lz4.1.bz2", f"{cf.paths['man1']}/unlz4.1")
