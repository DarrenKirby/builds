#    app-editor/nano/nano-8.2.build.py
#    Sun Oct 20 02:21:00 UTC 2024

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
    return os.system(f"./configure --prefix={self.seg_dir} --enable-utf8")


def make(self):
    return os.system("make")


def make_install(self):
    return os.system("make install")


def install(self):
    cf.do_bin(f"{self.seg_dir}/bin/nano", cf.paths['ub'])
    cf.do_sym(f"{cf.paths['ub']}/nano", f"{cf.paths['ub']}/rnano")
    cf.do_man(f"{self.seg_dir}/share/man/man1/nano.1", {cf.paths['man1']})
    cf.do_man(f"{self.seg_dir}/share/man/man1/rnano.1", {cf.paths['man1']})
    cf.do_man(f"{self.seg_dir}/share/man/man5/nanorc.5", {cf.paths['man8']})


"""
/usr/bin/nano
/usr/bin/rnano
/usr/share/man/man1/nano.1.bz2
/usr/share/man/man1/rnano.1.bz2
/usr/share/man/man5/nanorc.5.bz2
"""
