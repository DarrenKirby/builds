#    dev-lib/ncurses/ncurses-6.5.build.py
#    Thu Nov 21 16:55:06 UTC 2024

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
    return os.system("./configure --prefix=/usr "
                     "--mandir=/usr/share/man "
                     "--with-shared "
                     "--without-debug "
                     "--without-normal "
                     "--with-cxx-shared "
                     "--enable-pc-files "
                     "--with-pkg-config-libdir=/usr/lib/pkgconfig")


def make(self):
    return os.system(f"make {cf.config['makeopts']}")


def make_install(self):
    try:
        os.system(f"make DESTDIR={self.seg_dir} install")
    except OSError as e:
        cf.yellow(f"make_install failed: {e}")
        return 1
    # Edit header file
    os.system(f"sed -e 's/^#if.*XOPEN.*$/#if 1/' -i {self.p['_ui']}/curses.h")

def install(self):
    pass