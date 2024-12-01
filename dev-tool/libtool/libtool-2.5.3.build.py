#    dev-tool/libtool/libtool-2.5.3.build.py
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
    return self.do("./configure --prefix=/usr")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_binary(f"{self.p['_ub']}/libtool", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/libtoolize", self.p['ub'])

    self.inst_header(f"{self.p['_ui']}/ltdl.h", self.p['ui'])
    self.inst_directory(f"{self.p['_ui']}/libltdl/", f"{self.p['ui']}/libltdl/")

    self.inst_library(f"{self.p['_ul']}/libltdl.so.7.3.2", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libltdl.so.7.3.2", f"{self.p['ul']}/libltdl.so.7")
    self.inst_symlink(f"{self.p['ul']}/libltdl.so.7.3.2", f"{self.p['ul']}/libltdl.so")

    self.inst_directory(f"{self.p['_ush']}/libtool/", f"{self.p['ush']}/libtool/")

    for file in os.listdir(self.p['_ush'] + "/aclocal"):
        self.inst_file(f"{self.p['_ush']}/aclocal/{file}", f"{self.p['_ush']}/aclocal/")

    self.inst_manpage(f"{self.p['_man1']}/libtool.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/libtoolize.1", self.p['man1'])
