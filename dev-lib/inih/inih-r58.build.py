#    dev-lib/inih/inih-r58.build.py
#    Fri Oct 25 22:12:18 UTC 2024

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
    os.mkdir("build")
    os.chdir("build")
    return os.system(f"meson setup --prefix={self.seg_dir} "
                     f"--buildtype=release ..")


def make(self):
    return os.system("ninja")


def make_install(self):
    return os.system("ninja install")


def install(self):
    pass


"""
"""
