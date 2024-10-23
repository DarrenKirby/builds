#    sci-math/bc/bc-6.7.6.build.py
#    Tue Oct 22 23:29:21 UTC 2024

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
    # -N: --disable-nls, as --prefix is not honoured for locale installation
    return os.system(f"CC=gcc ./configure --prefix={self.seg_dir} -G -N -O3 -r")


def make(self):
    return os.system("make")


def make_install(self):
    return os.system("make install")


def install(self):
    cf.do_bin(f"{self.seg_dir}/bin/bc", cf.paths['ub'])
    cf.do_sym(f"{cf.paths['ub']}/bc", f"{cf.paths['ub']}/dc")

    cf.do_man(f"{self.seg_dir}/share/man/man1/bc.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/dc.1", cf.paths['man1'])


"""
/usr/bin/bc
/usr/bin/dc
/usr/share/man/man1/bc.1.bz2
/usr/share/man/man1/dc.1.bz2
"""
