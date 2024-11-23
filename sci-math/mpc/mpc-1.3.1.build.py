#    sci-math/mpc/mpc-1.3.1.build.py
#    Sat Nov 16 21:33:14 UTC 2024

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
    #self.inst_binary(f"{self.p['_ub']}/bc", self.p['ub'])
    #self.inst_symlink(f"{self.p['ub']}/bc", f"{self.p['ub']}/dc")

    #self.inst_manpage(f"{self.p['_man1']}/bc.1", self.p['man1'])
    #self.inst_manpage(f"{self.p['_man1']}/dc.1", self.p['man1'])
