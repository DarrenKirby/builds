#    app-shell/zsh/zsh-5.9.build.py
#    Thu Nov  7 04:40:49 UTC 2024

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
    # Fix configure files as per:
    # https://www.linuxfromscratch.org/blfs/view/stable/postlfs/zsh.html
    os.system("sed -e 's/set_from_init_file/texinfo_&/' -i Doc/Makefile.in")
    os.system("sed -e 's/^main/int &/' -e 's/exit(/return(/' -i aczsh.m4 configure.ac")
    os.system("sed -e 's/test = /&(char**)/' -i configure.ac")
    os.system("autoconf")

    return os.system("./configure --prefix=/usr --enable-cap --enable-gdbm ")


def make(self):
    return os.system(f"make {cf.config['makeopts']}")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_binary(f"{self.p['_ub']}/zsh", self.p['ub'])

    self.inst_manpage(f"{self.p['_man1']}/zsh.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/zshall.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/zshbuiltins.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/zshcalsys.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/zshcompctl.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/zshcompsys.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/zshcompwid.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/zshcontrib.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/zshexpn.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/zshmisc.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/zshmodules.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/zshoptions.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/zshparam.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/zshroadmap.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/zshtcpsys.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/zshzftpsys.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/zshzle.1", self.p['man1'])

    self.inst_directory(f"{self.p['_ul']}/zsh/", f"{self.p['ul']}/zsh/")
