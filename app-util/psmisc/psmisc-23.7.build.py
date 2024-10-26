#    app-util/psmisc/psmisc-23.7.build.py
#    Fri Oct 25 20:43:30 UTC 2024

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
    return os.system(f"./configure --prefix={self.seg_dir}")


def make(self):
    return os.system("make")


def make_install(self):
    return os.system("make install")


def install(self):
    cf.do_bin(f"{self.seg_dir}/bin/fuser", cf.paths['ub'])
    cf.do_bin(f"{self.seg_dir}/bin/killall", cf.paths['ub'])
    cf.do_bin(f"{self.seg_dir}/bin/peekfd", cf.paths['ub'])
    cf.do_bin(f"{self.seg_dir}/bin/prtstat", cf.paths['ub'])
    cf.do_bin(f"{self.seg_dir}/bin/pslog", cf.paths['ub'])
    cf.do_bin(f"{self.seg_dir}/bin/pstree", cf.paths['ub'])

    cf.do_sym(f"{cf.paths['ub']}/pstree", f"{cf.paths['ub']}/pstree.x11")

    cf.do_man(f"{self.seg_dir}/share/man/man1/fuser.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/killall.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/peekfd.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/prtstat.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/pslog.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/pstree.1", cf.paths['man1'])


"""
/usr/bin/fuser
/usr/bin/killall
/usr/bin/peekfd
/usr/bin/prtstat
/usr/bin/pslog
/usr/bin/pstree
/usr/bin/pstree.x11
/usr/share/man/man1/fuser.1
/usr/share/man/man1/killall.1
/usr/share/man/man1/peekfd.1
/usr/share/man/man1/prtstat.1
/usr/share/man/man1/pslog.1
/usr/share/man/man1/pstree.1
"""
