#    app-util/grep/grep-3.11.build.py
#    Fri Oct 25 20:43:30 UTC 2024

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
    return os.system(f"make {cf.config['makeopts']}")


def make_install(self):
    return os.system("make install")


def install(self):
    cf.do_bin(f"{self.seg_dir}/bin/grep", cf.paths['ub'])
    cf.do_scr(f"{self.seg_dir}/bin/egrep", cf.paths['ub'])
    cf.do_scr(f"{self.seg_dir}/bin/fgrep", cf.paths['ub'])

    cf.do_man(f"{self.seg_dir}/share/man/man1/grep.1", cf.paths['man1'])


"""
/usr/bin/grep
/usr/bin/egrep
/usr/bin/fgrep
/usr/share/man/man1/grep.1.bz2
"""
