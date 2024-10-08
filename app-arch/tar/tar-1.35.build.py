#    app-arch/tar/tar-1.35.build.py
#    Fri Sep 27 20:45:32 UTC 2024

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



def configure_source(self):
    os.chdir(f"{self.work_dir}/{self.package_dir}")
    os.system(f"./configure --prefix={self.work_dir} --bindir={self.work_dir}/bin")

def make_source(self):
    os.system("make")

def install():
    os.chdir(work_dir)
    do_bin(f"./bin/tar", "{b}/tar")
    do_bin(f"./libexec/rmt", "{sb}/rmt")
    do_man(f"./share/man/man1/tar.1" "{man1}/tar.1.bz2")
    do_man(f"./share/man/man8/rmt.8" "{man8}/rmt.8.bz2")

"""
/bin/tar
/sbin/rmt
/usr/share/man/man1/tar.1.bz2
/usr/share/man/man8/rmt.8.bz2
"""
