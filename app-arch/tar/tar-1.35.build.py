#    app-arch/tar/tar-1.35.build.py
#    Thu Oct 31 02:40:37 UTC 2024

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
    self.inst_binary(f"{self.seg_dir}/bin/tar", cf.paths['b'])
    self.inst_binary(f"{self.seg_dir}/libexec/rmt", cf.paths['s'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/tar.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man8/rmt.8", cf.paths['man8'])
