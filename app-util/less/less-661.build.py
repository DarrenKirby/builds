#    app-util/less/less-661.build.py
#    Mon Oct 21 22:52:42 UTC 2024

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
    cf.do_bin(f"{self.seg_dir}/bin/less", cf.paths['ub'])
    cf.do_bin(f"{self.seg_dir}/bin/lessecho", cf.paths['ub'])
    cf.do_bin(f"{self.seg_dir}/bin/lesskey", cf.paths['ub'])

    cf.do_man(f"{self.seg_dir}/share/man/man1/less.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/lessecho.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/lesskey.1", cf.paths['man1'])

"""
/usr/bin/less
/usr/bin/lessecho
/usr/bin/lesskey
/usr/share/man/man1/less.1.bz2
/usr/share/man/man1/lessecho.1.bz2
/usr/share/man/man1/lesskey.1.bz2
"""
