#    dev-util/libarchive/libarchive-3.7.4.build.py
#    Tue Dec 10 23:45:57 UTC 2024

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

depend = "dev-util/libxml2"


def configure(self):
    return self.do("./configure --prefix=/usr --disable-static --without-expat")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_binary(self.p['_ub'] + "/bsdcat", self.p['ub'])
    self.inst_binary(self.p['_ub'] + "/bsdcpio", self.p['ub'])
    self.inst_binary(self.p['_ub'] + "/bsdtar", self.p['ub'])
    self.inst_binary(self.p['_ub'] + "/bsdunzip", self.p['ub'])

    self.inst_header(self.p['_ui'] + "/archive.h", self.p['ui'])
    self.inst_header(self.p['_ui'] + "/archive_entry.h", self.p['ui'])

    self.inst_library(self.p['_ul'] + "/libarchive.so.13.7.4", self.p['ul'])
    self.inst_symlink(self.p['ul'] + "/libarchive.so.13.7.4", self.p['ul'] + "/libarchive.so")
    self.inst_symlink(self.p['ul'] + "/libarchive.so.13.7.4", self.p['ul'] + "/libarchive.so.13")

    self.inst_file(self.p['_ul'] + "/pkgconfig/libarchive.pc", self.p['ul'] + "/pkgconfig/")

    for file in os.listdir(self.p['_man1']):
        self.inst_manpage(f"{self.p['_man1']}/{file}", self.p['man1'])

    for file in os.listdir(self.p['_man3']):
        self.inst_manpage(f"{self.p['_man3']}/{file}", self.p['man3'])

    for file in os.listdir(self.p['_man5']):
        self.inst_manpage(f"{self.p['_man5']}/{file}", self.p['man5'])
