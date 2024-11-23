#    dev-tool/dejagnu/dejagnu-1.6.3.build.py
#    Sat Nov 23 00:24:10 UTC 2024

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

depend = "dev-lang/expect"


def configure(self):
    os.mkdir("build")
    os.chdir("build/")
    return os.system("../configure --prefix=/usr")


def make(self):
    os.system("makeinfo --html --no-split -o doc/dejagnu.html ../doc/dejagnu.texi")
    return os.system("makeinfo --plaintext -o doc/dejagnu.txt  ../doc/dejagnu.texi")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} install")


def install(self):
    pass