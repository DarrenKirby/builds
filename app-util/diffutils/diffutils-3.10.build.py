#    app-util/diffutils/diffutils-3.10.build.py
#    Thu Oct 24 23:32:27 UTC 2024

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
    return os.system(f"./configure --prefix={self.seg_dir}")


def make(self):
    return os.system("make")


def make_install(self):
    return os.system("make install")


def install(self):
    cf.do_bin(f"{self.seg_dir}/bin/cmp", cf.paths['ub'])
    cf.do_bin(f"{self.seg_dir}/bin/diff", cf.paths['ub'])
    cf.do_bin(f"{self.seg_dir}/bin/diff3", cf.paths['ub'])
    cf.do_bin(f"{self.seg_dir}/bin/sdiff", cf.paths['ub'])

    cf.do_man(f"{self.seg_dir}/share/man/man1/cmp.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/diff.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/diff3.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/sdiff.1", cf.paths['man1'])


"""
/usr/bin/cmp
/usr/bin/diff
/usr/bin/diff3
/usr/bin/sdiff
/usr/share/man/man1/cmp.1.bz2
/usr/share/man/man1/diff.1.bz2
/usr/share/man/man1/diff3.1.bz2
/usr/share/man/man1/sdiff.1.bz2
"""
