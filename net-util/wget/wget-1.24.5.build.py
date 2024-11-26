#    net-util/wget/wget-1.24.5.build.py
#    Sat Nov 16 21:11:57 UTC 2024

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
    return os.system(f"./configure --prefix=/usr --with-ssl=openssl")


def make(self):
    return os.system(f"make {cf.config['makeopts']}")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_binary(f"{self.p['_ub']}/wget", self.p['ub'])
    self.inst_manpage(f"{self.p['_man1']}/wget.1", self.p['man1'])
    self.inst_config(f"{self.p['_ue']}/wgetrc", self.p['e'] if cf.config['user'] == 'root' else self.p['ue'])
