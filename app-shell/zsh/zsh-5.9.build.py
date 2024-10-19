#    app-shell/zsh/zsh-5.9.buildpy
#    Fri Oct 18 22:51:29 UTC 2024

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


depend = 'gdbm'

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
    cf.do_bin(f"{self.seg_dir}/bin/dash", cf.paths['b'])
    cf.do_man(f"{self.seg_dir}share/man/man1/dash.1", cf.paths['man1'])

"""
/usr/bin/zsh
"""
