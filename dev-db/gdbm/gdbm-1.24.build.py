#    dev-db/gdbm/gdbm-1.24.build.py
#    Sat Nov 16 21:52:39 UTC 2024

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


def configure(self):
    return self.do("./configure --prefix=/usr --disable-static --enable-libgdbm-compat")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_binary(f"{self.p['_ub']}/gdbm_dump", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/gdbm_load", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/gdbmtool", self.p['ub'])

    self.inst_library(f"{self.p['_ul']}/libgdbm.so.6.0.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libgdbm.so.6.0.0", f"{self.p['ul']}/libgdbm.so.6")
    self.inst_symlink(f"{self.p['ul']}/libgdbm.so.6.0.0", f"{self.p['ul']}/libgdbm.so")

    self.inst_library(f"{self.p['_ul']}/libgdbm_compat.so.4.0.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libgdbm_compat.so.4.0.0", f"{self.p['ul']}/libgdbm_compat.so.4")
    self.inst_symlink(f"{self.p['ul']}/libgdbm_compat.so.4.0.0", f"{self.p['ul']}/libgdbm_compat.so")

    self.inst_header(f"{self.p['_ui']}/dbm.h", self.p['ui'])
    self.inst_header(f"{self.p['_ui']}/gdbm.h", self.p['ui'])
    self.inst_header(f"{self.p['_ui']}/ndbm.h", self.p['ui'])

    self.inst_manpage(f"{self.p['_man3']}/gdbm.3", self.p['man3'])
    self.inst_manpage(f"{self.p['_man1']}/gdbm_dump.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/gdbm_load.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/gdbmtool.1", self.p['man1'])
