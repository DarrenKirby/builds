#    app-shell/zsh/zsh-5.9.build.py
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
    cf.do_bin(f"{self.seg_dir}/bin/zsh", cf.paths['ub'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/zsh.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/zshall.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/zshbuiltins.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/zshcalsys.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/zshcompctl.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/zshcompsys.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/zshcompwid.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/zshcontrib.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/zshexpn.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/zshmisc.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/zshmodules.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/zshoptions.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/zshparam.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/zshroadmap.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/zshtcpsys.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/zshzftpsys.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/zshzle.1", cf.paths['man1'])
    cf.do_dir(f"{self.seg_dir}/lib/zsh/", f"{cf.paths['ul']}/zsh/")


"""
/usr/bin/zsh
/usr/lib/zsh/
/usr/lib/zsh/5.9/
/usr/lib/zsh/5.9/zsh/
/usr/lib/zsh/5.9/zsh/cap.so
/usr/lib/zsh/5.9/zsh/clone.so
/usr/lib/zsh/5.9/zsh/compctl.so
/usr/lib/zsh/5.9/zsh/complete.so
/usr/lib/zsh/5.9/zsh/complist.so
/usr/lib/zsh/5.9/zsh/computil.so
/usr/lib/zsh/5.9/zsh/curses.so
/usr/lib/zsh/5.9/zsh/datetime.so
/usr/lib/zsh/5.9/zsh/deltochar.so
/usr/lib/zsh/5.9/zsh/example.so
/usr/lib/zsh/5.9/zsh/files.so
/usr/lib/zsh/5.9/zsh/langinfo.so
/usr/lib/zsh/5.9/zsh/mapfile.so
/usr/lib/zsh/5.9/zsh/mathfunc.so
/usr/lib/zsh/5.9/zsh/nearcolor.so
/usr/lib/zsh/5.9/zsh/newuser.so
/usr/lib/zsh/5.9/zsh/parameter.so
/usr/lib/zsh/5.9/zsh/regex.so
/usr/lib/zsh/5.9/zsh/rlimits.so
/usr/lib/zsh/5.9/zsh/sched.so
/usr/lib/zsh/5.9/zsh/stat.so
/usr/lib/zsh/5.9/zsh/system.so
/usr/lib/zsh/5.9/zsh/termcap.so
/usr/lib/zsh/5.9/zsh/terminfo.so
/usr/lib/zsh/5.9/zsh/watch.so
/usr/lib/zsh/5.9/zsh/zftp.so
/usr/lib/zsh/5.9/zsh/zle.so
/usr/lib/zsh/5.9/zsh/zleparameter.so
/usr/lib/zsh/5.9/zsh/zprof.so
/usr/lib/zsh/5.9/zsh/zpty.so
/usr/lib/zsh/5.9/zsh/zselect.so
/usr/lib/zsh/5.9/zsh/zutil.so
/usr/lib/zsh/5.9/zsh/db/
/usr/lib/zsh/5.9/zsh/db/gdbm.so
/usr/lib/zsh/5.9/zsh/net/
/usr/lib/zsh/5.9/zsh/net/socket.so
/usr/lib/zsh/5.9/zsh/net/tcp.so
/usr/lib/zsh/5.9/zsh/param/
/usr/lib/zsh/5.9/zsh/param/private.so
/usr/share/man/man1/zsh.1.bz2
/usr/share/man/man1/zshall.1.bz2
/usr/share/man/man1/zshbuiltins.1.bz2
/usr/share/man/man1/zshcalsys.1.bz2
/usr/share/man/man1/zshcompctl.1.bz2
/usr/share/man/man1/zshcompsys.1.bz2
/usr/share/man/man1/zshcompwid.1.bz2
/usr/share/man/man1/zshcontrib.1.bz2
/usr/share/man/man1/zshexpn.1.bz2
/usr/share/man/man1/zshmisc.1.bz2
/usr/share/man/man1/zshmodules.1.bz2
/usr/share/man/man1/zshoptions.1.bz2
/usr/share/man/man1/zshparam.1.bz2
/usr/share/man/man1/zshroadmap.1.bz2
/usr/share/man/man1/zshtcpsys.1.bz2
/usr/share/man/man1/zshzftpsys.1.bz2
/usr/share/man/man1/zshzle.1.bz2attr.so
"""
