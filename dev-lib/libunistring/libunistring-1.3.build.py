#    dev-lib/libunistring/libunistring-1.3.build.py
#    Sat Nov 16 01:02:22 UTC 2024

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
    return self.do("./configure --prefix=/usr "
                   "--disable-static")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    for file in glob.glob(f"{self.p['_ui']}/*.h"):
        self.inst_header(file, self.p['ui'])

    self.inst_directory(f"{self.p['_ui']}/unistring/", f"{self.p['ui']}/unistring/")

    self.inst_library(f"{self.p['_ul']}/libunistring.so.5.2.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libunistring.so.5.2.0", f"{self.p['ul']}/libunistring.so.5")
    self.inst_symlink(f"{self.p['ul']}/libunistring.so.5.2.0", f"{self.p['ul']}/libunistring.so")
