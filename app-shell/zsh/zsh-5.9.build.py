#    app-shell/zsh/zsh-5.9.build.py
#    Thu Oct 31 03:40:54 UTC 2024

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
    # Fix configure files as per:
    # https://www.linuxfromscratch.org/blfs/view/stable/postlfs/zsh.html
    os.system("sed -e 's/set_from_init_file/texinfo_&/' -i Doc/Makefile.in")
    os.system("sed -e 's/^main/int &/' -e 's/exit(/return(/' -i aczsh.m4 configure.ac")
    os.system("sed -e 's/test = /&(char**)/' -i configure.ac")
    os.system("autoconf")

    return os.system(f"./configure --prefix={self.seg_dir} --enable-cap --enable-gdbm ")


def make(self):
    return os.system("make")


def make_install(self):
    return os.system("make install")


def install(self):
    self.inst_binary(f"{self.seg_dir}/bin/zsh", cf.paths['ub'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/zsh.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/zshall.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/zshbuiltins.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/zshcalsys.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/zshcompctl.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/zshcompsys.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/zshcompwid.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/zshcontrib.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/zshexpn.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/zshmisc.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/zshmodules.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/zshoptions.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/zshparam.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/zshroadmap.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/zshtcpsys.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/zshzftpsys.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/zshzle.1", cf.paths['man1'])
    self.inst_directory(f"{self.seg_dir}/lib/zsh/", f"{cf.paths['ul']}/zsh/")
