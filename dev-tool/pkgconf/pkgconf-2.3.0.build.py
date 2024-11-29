#    dev-tool/pkgconf/pkgconf-2.3.0.build.py
#    Sat Nov 16 22:06:52 UTC 2024

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
    return self.do("./configure --prefix=/usr --disable-static")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_binary(f"{self.p['_ub']}/bomtool", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/pkgconf", self.p['ub'])

    self.inst_directory(self.p['_ui'] + '/pkgconf/', self.p['ui'] + '/pkgconf/')

    self.inst_library(f"{self.p['_ul']}/libpkgconf.so.5.0.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libpkgconf.so.5.0.0", f"{self.p['ul']}/libpkgconf.so")
    self.inst_symlink(f"{self.p['ul']}/libpkgconf.so.5.0.0", f"{self.p['ul']}/libpkgconf.so.5")

    self.inst_file(self.p['ul'] + "/pkgconfig/libpkgconf.pc", self.p['ul'] + "/pkgconfig/")
    self.inst_file(self.p['ul'] + "/aclocal/pkg.m4", self.p['ul'] + "/aclocal/")

    self.inst_manpage(f"{self.p['_man1']}/pkgconf.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man5']}/pc.5", self.p['man5'])
    self.inst_manpage(f"{self.p['_man5']}/pkgconf-personality.5", self.p['man5'])
    self.inst_manpage(f"{self.p['_man7']}/pkg.m4.7", self.p['man7'])
