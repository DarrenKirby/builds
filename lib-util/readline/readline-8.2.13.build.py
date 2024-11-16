#    lib-util/readline/readline-8.2.13.build.py
#    Sat Nov 16 22:25:34 UTC 2024

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
    os.system("sed -i '/MV.*old/d' Makefile.in")
    os.system("sed -i '/{OLDSUFF}/c:' support/shlib-install")
    os.system("sed -i 's/-Wl,-rpath,[^ ]*//' support/shobj-conf")

    return os.system("./configure --prefix=/usr --disable-static --with-curses")


def make(self):
    return os.system(f'make SHLIB_LIBS="-lncursesw" {cf.config["makeopts"]}')


def make_install(self):
    return os.system(f'make DESTDIR={self.seg_dir} SHLIB_LIBS="-lncursesw" install')


def install(self):
    self.inst_library(f"{self.p['_ul']}/libhistory.so.8.2", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libhistory.so.8.2", f"{self.p['ul']}/libhistory.so.8")
    self.inst_symlink(f"{self.p['ul']}/libhistory.so.8", f"{self.p['ul']}/libhistory.so")
    self.inst_library(f"{self.p['_ul']}/libreadline.so.8.2", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libreadline.so.8.2", f"{self.p['ul']}/libreadline.so.8")
    self.inst_symlink(f"{self.p['ul']}/libreadline.so.8", f"{self.p['ul']}/libreadline.so")

    # Recursively copy the header directory
    self.inst_directory(f"{self.p['_ui']}/readline/", f"{self.p['ui']}/readline/")

    # Copy over pkgconfig files
    self.inst_file(f"{self.p['_ul']}/pkgconfig/history.pc", f"{self.p['ul']}/pkgconfig/")
    self.inst_file(f"{self.p['_ul']}/pkgconfig/readline.pc", f"{self.p['ul']}/pkgconfig/")

    self.inst_manpage(f"{self.p['_man3']}/history.3", self.p['man3'])
    self.inst_manpage(f"{self.p['_man3']}/readlines.3", self.p['man3'])
