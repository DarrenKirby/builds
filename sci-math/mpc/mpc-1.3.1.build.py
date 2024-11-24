#    sci-math/mpc/mpc-1.3.1.build.py
#    Sun Nov 24 00:17:36 UTC 2024

#    Copyright:: (c)
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
    return os.system("./configure --prefix=/usr --disable-static")


def make(self):
    return os.system(f"make {cf.config['makeopts']}")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_header(f"{self.p['_ui']}/mpc.h", self.p['ui'])

    self.inst_library(f"{self.p['_ul']}/libmpc.so.3.3.1", self.p['ul'])
    self.inst_symlink(self.p['ul'] + "/libmpc.so.3.3.1", self.p['ul'] + "/libmpc.so.3")
    self.inst_symlink(self.p['ul'] + "/libmpc.so.3.3.1", self.p['ul'] + "/libmpc.so")

