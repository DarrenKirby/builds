#    app-util/file/file-5.45.build.py
#    Thu Nov 14 21:19:00 UTC 2024

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
    return self.do("./configure --prefix=/usr")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_library(f"{self.p['_ul']}/libmagic.so.1.0.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libmagic.so.1.0.0", f"{self.p['ul']}/libmagic.so")
    self.inst_symlink(f"{self.p['ul']}/libmagic.so.1.0.0", f"{self.p['ul']}/libmagic.so.1")

    self.inst_header(f"{self.p['_ui']}/magic.h", self.p['ui'])

    self.inst_binary(f"{self.p['_ub']}/file", f"{self.p['ub']}")

    self.inst_manpage(f"{self.p['_man1']}/file.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man3']}/libmagic.3", self.p['man3'])
    self.inst_manpage(f"{self.p['_man4']}/magic.4", self.p['man4'])

    self.inst_file(f"{self.p['_ush']}/misc/magic.mgc", f"{self.p['ush']}/misc/magic.mgc")
    self.inst_file(f"{self.p['_ul']}/pkgconfig/libmagic.pc", f"{self.p['ul']}/pkgconfig/")

