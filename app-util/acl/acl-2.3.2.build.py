#    app-util/acl/acl-2.3.2.build.py
#    Wed Nov 13 00:51:21 UTC 2024

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
    return self.do(f"./configure --prefix=/usr --disable-static")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_binary(f"{self.p['_ub']}/chacl", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/getfacl", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/setfacl", self.p['ub'])

    self.inst_directory(f"{self.p['_ui']}/acl/", f"{self.p['ui']}/acl/")
    self.inst_header(f"{self.p['_ui']}/sys/acl.h", f"{self.p['ui']}/sys")

    self.inst_library(f"{self.p['_ul']}/libacl.so.1.1.2302", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libacl.so.1.1.2302", f"{self.p['ul']}/libacl.so.1")
    self.inst_symlink(f"{self.p['ul']}/libacl.so.1.1.2302", f"{self.p['ul']}/libacl.so")
    self.inst_file(f"{self.p['_ul']}/pkgconfig/libacl.pc", f"{self.p['ul']}/pkgconfig/libacl.pc")

    self.inst_manpage(f"{self.p['_man1']}/chacl.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/getfacl.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/setfacl.1", self.p['man1'])

    for manpage in os.listdir(f"{self.p['_man3']}/"):
        self.inst_manpage(f"{self.p['_man3']}/{manpage}", self.p['man3'])

    self.inst_manpage(f"{self.p['_man5']}/acl.5", self.p['man5'])
