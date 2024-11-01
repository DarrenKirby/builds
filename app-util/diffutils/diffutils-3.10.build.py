#    app-util/diffutils/diffutils-3.10.build.py
#    Thu Oct 31 21:09:52 UTC 2024

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
    self.inst_binary(f"{self.seg_dir}/bin/cmp", cf.paths['ub'])
    self.inst_binary(f"{self.seg_dir}/bin/diff", cf.paths['ub'])
    self.inst_binary(f"{self.seg_dir}/bin/diff3", cf.paths['ub'])
    self.inst_binary(f"{self.seg_dir}/bin/sdiff", cf.paths['ub'])

    self.inst_manpage(f"{self.seg_dir}/share/man/man1/cmp.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/diff.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/diff3.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/sdiff.1", cf.paths['man1'])
