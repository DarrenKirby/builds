#    app-arch/lz4/lz4-1.10.0.build.py
#    Thu Nov 28 00:05:28 UTC 2024

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
    return self.do(f"make BUILD_STATIC=no PREFIX={self.seg_dir}/usr")


def make_install(self):
    return self.do(f"make BUILD_STATIC=no PREFIX={self.seg_dir}/usr install")


def install(self):
    self.inst_library(f"{self.p['_ul']}/liblz4.so.1.10.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/liblz4.so.1.10.0", f"{self.p['ul']}/liblz4.so.1")
    self.inst_symlink(f"{self.p['ul']}/liblz4.so.1.10.0", f"{self.p['ul']}/liblz4.so")

    self.inst_header(f"{self.p['_ui']}/lz4.h", self.p['ui'])
    self.inst_header(f"{self.p['_ui']}/lz4frame.h", self.p['ui'])
    self.inst_header(f"{self.p['_ui']}/lz4hc.h", self.p['ui'])

    self.inst_binary(f"{self.p['_ub']}/lz4", f"{self.p['ub']}")
    self.inst_symlink(f"{self.p['ub']}/lz4", f"{self.p['ub']}/lz4c")
    self.inst_symlink(f"{self.p['ub']}/lz4", f"{self.p['ub']}/lz4cat")
    self.inst_symlink(f"{self.p['ub']}/lz4", f"{self.p['ub']}/unlz4")

    self.inst_manpage(f"{self.p['_man1']}/lz4.1", self.p['man1'])
    self.inst_symlink(f"{self.p['man1']}/lz4.1.bz2", f"{self.p['man1']}/lz4c.1")
    self.inst_symlink(f"{self.p['man1']}/lz4.1.bz2", f"{self.p['man1']}/lz4cat.1")
    self.inst_symlink(f"{self.p['man1']}/lz4.1.bz2", f"{self.p['man1']}/unlz4.1")
