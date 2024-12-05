#    app-doc/texinfo/texinfo-7.1.build.py
#    Wed Dec  4 03:50:15 UTC 2024
import os


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
    return self.do("./configure --prefix=/usr")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    try:
        self.do(f"make DESTDIR={self.seg_dir} install")
        self.do(f"make DESTDIR={self.seg_dir} TEXMF=/usr/share/texmf install-tex")
        return 0
    except OSError as e:
        cf.red(f"Installing texinfo failed: {e}")
        return 1


def install(self):
    for file in os.listdir(self.p['_ub']):
        if file in ["makeinfo"]:
            pass
        elif file in ["info", "install-info"]:
            self.inst_binary(f"{self.p['_ub']}/{file}", self.p['ub'])
        else:
            self.inst_script(f"{self.p['_ub']}/{file}", self.p['ub'])
    self.inst_symlink(self.p['ub'] + "/texi2any", self.p['ub'] + "/makeinfo")

    self.inst_directory(self.p['_ul'] + "/texinfo/", self.p['ul'] + "/texinfo/")
    self.inst_directory(self.p['_ush'] + "/texinfo/", self.p['ush'] + "/texinfo/")
    self.inst_directory(self.p['_ush'] + "/texmf/", self.p['ush'] + "/texmf/")

    for manpage in os.listdir(self.p['_man1']):
        self.inst_manpage(f"{self.p['_man1']}/{manpage}", self.p['man1'])

    for manpage in os.listdir(self.p['_man5']):
        self.inst_manpage(f"{self.p['_man5']}/{manpage}", self.p['man5'])
