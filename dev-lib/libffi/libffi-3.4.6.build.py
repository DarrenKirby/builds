#    dev-lib/libffi/libffi-3.4.6.build.py
#    Thu Nov 21 16:33:12 UTC 2024

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
    # Prevent static libs
    return self.do("./configure --prefix=/usr --disable-static --with-gcc-arch=native")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_header(f"{self.p['_ui']}/ffi.h", self.p['ui'])
    self.inst_header(f"{self.p['_ui']}/ffitarget.h", self.p['ui'])

    self.inst_file(self.p['_ul'] + "/pkgconfig/libffi.pc", self.p['ul'] + "/pkgconfig/")

    self.inst_library(f"{self.p['_ul']}/libffi.so.8.1.4", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libffi.so.8.1.4", f"{self.p['ul']}/libffi.so")
    self.inst_symlink(f"{self.p['ul']}/libffi.so.8.1.4", f"{self.p['ul']}/libffi.so.8")

    self.inst_manpage(f"{self.p['_man3']}/ffi.3", self.p['man3'])
    self.inst_manpage(f"{self.p['_man3']}/ffi_call.3", self.p['man3'])
    self.inst_manpage(f"{self.p['_man3']}/ffi_prep_cif.3", self.p['man3'])
    self.inst_manpage(f"{self.p['_man3']}/ffi_prep_cif_var.3", self.p['man3'])
