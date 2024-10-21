#    net-util/wget/wget-1.24.5.build.py
#    Mon Oct 21 20:14:02 UTC 2024

#    Copyright:: (c) 2024 Darren Kirby
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
    return os.system(f"./configure --prefix={self.seg_dir}")


def make(self):
    return os.system("make")


def make_install(self):
    return os.system("make install")


def install(self):
    cf.do_bin(f"{self.seg_dir}/bin/wget", cf.paths['ub'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/wget.1", cf.paths['man1'])
    cf.do_con(f"{self.seg_dir}/etc/wgetrc", cf.paths['e'])


"""
/etc/wgetrc
/usr/bin/wget
/usr/share/man/man1/wget.1.bz2
"""
