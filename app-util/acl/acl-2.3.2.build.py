#    app-util/acl/acl-2.3.2.build.py
#    Thu Oct 31 21:58:49 UTC 2024

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
    return os.system(f"./configure --prefix={self.seg_dir} --disable-static")


def make(self):
    return os.system(f"make {cf.config['makeopts']}")


def make_install(self):
    return os.system("make install")


def install(self):
    self.inst_binary(f"{self.seg_dir}/bin/", cf.paths['ub'])
    self.inst_binary(f"{self.seg_dir}/bin/", cf.paths['ub'])
    self.inst_binary(f"{self.seg_dir}/bin/", cf.paths['ub'])

    self.inst_directory(f"{self.seg_dir}/include/acl/", f"{cf.paths['ui']}/acl/")
    self.inst_header(f"{self.seg_dir}/include/sys/acl.h", f"{cf.paths['ui']}/sys")

    self.inst_library(f"{self.seg_dir}/lib/libacl.so.1.1.2302", cf.paths['ul'])
    self.inst_symlink(f"{cf.paths['ul']}/libacl.so.1.1.2302", f"{cf.paths['ul']}/libacl.so.1")
    self.inst_symlink(f"{cf.paths['ul']}/libacl.so.1.1.2302", f"{cf.paths['ul']}/libacl.so")

    self.inst_manpage(f"{self.seg_dir}/share/man/man1/chacl.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/getfacl.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/setfacl.1", cf.paths['man1'])

    for manpage in glob.glob(f"{self.seg_dir}/share/man/man3/acl_*.3"):
        self.inst_manpage(manpage, cf.paths['man3'])

    self.inst_manpage(f"{self.seg_dir}/share/man/man5/acl.5", cf.paths['man5'])
