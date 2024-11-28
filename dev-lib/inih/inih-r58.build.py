#    dev-lib/inih/inih-r58.build.py
#    Thu Nov 14 18:34:16 UTC 2024

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
    os.mkdir("build")
    os.chdir("build")
    return self.do("meson setup --prefix=/usr "
                   "--libdir=lib --buildtype=release ..")


def make(self):
    return self.do("ninja")


def make_install(self):
    return self.do(f"DESTDIR={self.seg_dir} ninja install")


def install(self):
    self.inst_header(f"{self.p['_ui']}/INIReader.h", self.p['ui'])
    self.inst_header(f"{self.p['_ui']}/ini.h", self.p['ui'])

    self.inst_library(f"{self.p['_ul']}/libINIReader.so.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libINIReader.so.0", f"{self.p['ul']}/libINIReader.so")
    self.inst_library(f"{self.p['_ul']}/libinih.so.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libinih.so.0", f"{self.p['ul']}/libinih.so")

    self.inst_file(f"{self.p['_ul']}/pkgconfig/INIReader.pc", f"{self.p['ul']}/pkgconfig/")
    self.inst_file(f"{self.p['_ul']}/pkgconfig/inih.pc", f"{self.p['ul']}/pkgconfig/")
