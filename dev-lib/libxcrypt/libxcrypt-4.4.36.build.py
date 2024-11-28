#    dev-lib/libxcrypt/libxcrypt-4.4.36.build.py
#    Thu Nov 21 16:38:30 UTC 2024

#    Copyright:: (c) 2024
#    Author:: Darren Kirby (mailto:bulliver)

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
    return self.do("./configure --prefix=/usr "
                   "--enable-hashes=strong,glibc "
                   "--enable-obsolete-api=no "
                   "--disable-static "
                   "--disable-failure-tokens")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_header(f"{self.p['_ui']}/crypt.h", self.p['ui'])

    self.inst_library(f"{self.p['_ul']}/libcrypt.so.2.0.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libcrypt.so.2.0.0", f"{self.p['ul']}/libcrypt.so.2")
    self.inst_symlink(f"{self.p['ul']}/libcrypt.so.2.0.0", f"{self.p['ul']}/libcrypt.so")

    self.inst_file(f"{self.p['_ul']}/pkgconfig/libxcrypt.pc", self.p['ul'] + "/pkgconfig/")
    self.inst_symlink(self.p['ul'] + "/pkgconfig/libxcrypt.pc", self.p['ul'] + "/pkgconfig/libcrypt.pc")

    self.inst_manpage(f"{self.p['_man5']}/crypt.5", self.p['man5'])

    for file in os.listdir(self.p['_man3']):
        self.inst_manpage(f"{self.p['_man3']}/{file}", self.p['man3'])
