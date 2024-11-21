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
    return os.system(f"sed -e 's/^#if.*XOPEN.*$/#if 1/' -i {self.p['_ui']}/curses.h")

def install(self):
    for file in os.listdir(self.p['_ub']):
        if file not in ["captoinfo", "infotocap", "reset"]:
            self.inst_script(f"{self.p['_ub']}/{file}", self.p['ub'])

    self.inst_symlink(f"{self.p['ub']}/tic", f"{self.p['ub']}/captoinfo")
    self.inst_symlink(f"{self.p['ub']}/tic", f"{self.p['ub']}/infotocap")
    self.inst_symlink(f"{self.p['ub']}/tset", f"{self.p['ub']}/reset")

    for file in glob.glob(f"{self.p['_ui']}/*.h"):
        if file not in [f"{self.p['_ui']}/ncurses.h"]:
            self.inst_header(file, self.p['ui'])

    self.inst_symlink(f"{self.p['ui']}/curses.h", f"{self.p['ui']}/ncurses.h")

    for file in ["libformw.so.6.5", "libmenuw.so.6.5", "libncurses++w.so.6.5", "libncursesw.so.6.5",
                 "libpanelw.so.6.5"]:
        self.inst_library(f"{self.p['_ul']}/{file}", self.p['ul'])

    self.inst_symlink(f"{self.p['ul']}/libformw.so.6.5", f"{self.p['ul']}/libformw.so.6")
    self.inst_symlink(f"{self.p['ul']}/libformw.so.6", f"{self.p['ul']}/libformw.so")
    self.inst_symlink(f"{self.p['ul']}/libmenuw.so.6.5", f"{self.p['ul']}/libmenuw.so.6")
    self.inst_symlink(f"{self.p['ul']}/libmenuw.so.6", f"{self.p['ul']}/libmenuw.so")
    self.inst_symlink(f"{self.p['ul']}/libncurses++w.so.6.5", f"{self.p['ul']}/libncurses++w.so.6")
    self.inst_symlink(f"{self.p['ul']}/libncurses++w.so.6", f"{self.p['ul']}/libncurses++w.so")
    self.inst_symlink(f"{self.p['ul']}/libncursesw.so.6.5", f"{self.p['ul']}/libncursesw.so.6")
    self.inst_symlink(f"{self.p['ul']}/libncursesw.so.6", f"{self.p['ul']}/libncursesw.so")
    self.inst_symlink(f"{self.p['ul']}/libpanelw.so.6.5", f"{self.p['ul']}/libpanelw.so.6")
    self.inst_symlink(f"{self.p['ul']}/libpanelw.so.6", f"{self.p['ul']}/libpanelw.so")

    for file in glob.glob(f"{self.p['_ul']}/pkgconfig/*.pc"):
        self.inst_file(file, self.p['ul'] + "/pkgconfig/")

    self.inst_directory(self.p['_ush'] + "/terminfo/", self.p['ush'] + "/terminfo/")
    self.inst_directory(self.p['_ush'] + "/tabset/", self.p['ush'] + "/tabset/")

    self.inst_symlink(f"{self.p['ush']}/terminfo/", f"{self.p['ul']}/terminfo")

    links_to_make = []
    for file in glob.glob(f"{self.p['_man1']}/*"):
        if os.path.islink(file):
            links_to_make.append((os.readlink(file), file.split("/")[-1]))
        else:
            self.inst_manpage(file, self.p['man1'], compress=False)
    for link in links_to_make:
        self.inst_symlink(f"{self.p['man1']}/{link[0]}", f"{self.p['man1']}/{link[1]}")

    links_to_make = []
    for file in glob.glob(f"{self.p['_man3']}/*"):
        if os.path.islink(file):
            links_to_make.append((os.readlink(file), file.split("/")[-1]))
        else:
            self.inst_manpage(file, self.p['man3'], compress=False)
    for link in links_to_make:
        self.inst_symlink(f"{self.p['man3']}/{link[0]}", f"{self.p['man3']}/{link[1]}")

    for file in os.listdir(self.p['_man5']):
        self.inst_script(f"{self.p['_man5']}/{file}", self.p['man5'])

    for file in os.listdir(self.p['_man8']):
        self.inst_script(f"{self.p['_man8']}/{file}", self.p['man8'])

    # Trick some applications into linking against the wide-character libs
    for lib in ["ncurses", "form", "panel", "menu"]:
        self.inst_symlink(f"{self.p['ul']}/lib{lib}w.so", f"{self.p['ul']}/lib{lib}.so")
        self.inst_symlink(f"{self.p['ul']}/pkgconfig/{lib}w.pc", f"{self.p['ul']}/pkgconfig/{lib}.pc")
