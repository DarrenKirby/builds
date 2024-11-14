#    app-util/file/file-5.45.build.py
#    Tue Oct 22 21:19:20 UTC 2024

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
    return os.system("./configure --prefix=/usr")


def make(self):
    return os.system(f"make {cf.config['makeopts']}")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} install")


def install(self):
    cf.do_lib(f"{self.seg_dir}/lib/libmagic.so.1.0.0", cf.paths['ul'])
    cf.do_sym(f"{cf.paths['ul']}/libmagic.so.1.0.0", f"{cf.paths['ul']}/libmagic.so")
    cf.do_sym(f"{cf.paths['ul']}/libmagic.so.1.0.0", f"{cf.paths['ul']}/libmagic.so.1")

    cf.do_hdr(f"{self.seg_dir}/include/magic.h", cf.paths['ui'])

    cf.do_bin(f"{self.seg_dir}/bin/file", f"{cf.paths['ub']}")

    cf.do_man(f"{self.seg_dir}/share/man/man1/file.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man3/libmagic.3", cf.paths['man3'])
    cf.do_man(f"{self.seg_dir}/share/man/man4/magic.4", cf.paths['man4'])

    os.system("mkdir -p /usr/share/misc")
    cf.do_bin(f"{self.seg_dir}/share/misc/magic.mgc", "/usrshare/misc/magic.mgc")


