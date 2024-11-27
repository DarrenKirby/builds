#    dev-tool/gettext/gettext-0.22.5.build.py
#    Wed Nov 27 00:22:11 UTC 2024

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
    return os.system("./configure --prefix=/usr --disable-static")


def make(self):
    return os.system(f"make {cf.config['makeopts']}")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} install")


def install(self):
    for file in os.listdir(self.p['_ub']):
        # Scripts...
        if file in ["autopoint", "gettext.sh", "gettextize"]:
            self.inst_script(f"{self.p['_ub']}/{file}", self.p['ub'])
        else:
            self.inst_binary(f"{self.p['_ub']}/{file}", self.p['ub'])

    self.inst_header(self.p['_ui'] + "/autosprintf.h", self.p['ui'])
    self.inst_header(self.p['_ui'] + "/gettext-po.h", self.p['ui'])
    self.inst_header(self.p['_ui'] + "/textstyle.h", self.p['ui'])

    self.inst_directory(self.p['_ui'] + "/textstyle/", self.p['ui'] + "/textstyle/")

    self.inst_library(f"{self.p['_ul']}/libasprintf.so.0.0.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libasprintf.so.0.0.0", f"{self.p['ul']}/libasprintf.so.0")
    self.inst_symlink(f"{self.p['ul']}/libasprintf.so.0.0.0", f"{self.p['ul']}/libasprintf.so")

    self.inst_library(f"{self.p['_ul']}/libgettextlib-0.22.5.so", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libgettextlib-0.22.5.so", f"{self.p['ul']}/libgettextlib.so")

    self.inst_library(f"{self.p['_ul']}/libgettextpo.so.0.5.10", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libgettextpo.so.0.5.10", f"{self.p['ul']}/libgettextpo.so.0")
    self.inst_symlink(f"{self.p['ul']}/libgettextpo.so.0.5.10", f"{self.p['ul']}/libgettextpo.so")

    self.inst_library(f"{self.p['_ul']}/libgettextsrc-0.22.5.so", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libgettextsrc-0.22.5.so", f"{self.p['ul']}/libgettextsrc.so")

    self.inst_library(f"{self.p['_ul']}/libtextstyle.so.0.2.1", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libtextstyle.so.0.2.1", f"{self.p['ul']}/libtextstyle.so.0")
    self.inst_symlink(f"{self.p['ul']}/libtextstyle.so.0.2.1", f"{self.p['ul']}/libtextstyle.so")

    self.inst_library(f"{self.p['_ul']}/preloadable_libintl.so", self.p['ul'])

    self.inst_directory(self.p['_ul'] + "/gettext/", self.p['ul'] + "/gettext/")

    self.inst_directory(self.p['_ush'] + "/gettext/", self.p['ush'] + "/gettext/")
    self.inst_directory(self.p['_ush'] + "/gettext-0.22.5/", self.p['ush'] + "/gettext-0.22.5/")

    for file in os.listdir(self.p['_ush'] + "/aclocal"):
        self.inst_file(f"{self.p['_ush']}/aclocal/{file}", self.p['ush'] + "/aclocal/")

    for manpage in os.listdir(self.p['_man1']):
        self.inst_manpage(f"{self.p['_man1']}/{manpage}", self.p['man1'])

    # Hardlinked manpages
    for manpage in os.listdir(self.p['_man3']):
        self.inst_manpage(f"{self.p['_man3']}/{manpage}", self.p['man3'], compress=False)
