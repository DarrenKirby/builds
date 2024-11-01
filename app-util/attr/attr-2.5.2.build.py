#    app-util/attr/attr-2.5.2.build.py
#    Thu Oct 31 21:52:45 UTC 2024

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
    return os.system(f"./configure --prefix={self.seg_dir} --disable-static")


def make(self):
    return os.system(f"make {cf.config['makeopts']}")


def make_install(self):
    return os.system("make install")


def install(self):
    self.inst_binary(f"{self.seg_dir}/bin/attr", cf.paths['ub'])
    self.inst_binary(f"{self.seg_dir}/bin/getfattr", cf.paths['ub'])
    self.inst_binary(f"{self.seg_dir}/bin/setfattr", cf.paths['ub'])

    self.inst_config(f"{self.seg_dir}/etc/xattr.conf", cf.paths['e'])

    self.inst_library(f"{self.seg_dir}/lib/libattr.so.1.1.2502", cf.paths['ul'])
    self.inst_symlink(f"{cf.paths['ul']}/libattr.so.1.1.2502", f"{cf.paths['ul']}/libattr.so")
    self.inst_symlink(f"{cf.paths['ul']}/libattr.so.1.1.2502", f"{cf.paths['ul']}/libattr.so.1")

    self.inst_manpage(f"{self.seg_dir}/share/man/man1/attr.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/getfattr.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/setfattr.1", cf.paths['man1'])

    self.inst_manpage(f"{self.seg_dir}/share/man/man3/attr_get.3", cf.paths['man3'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man3/attr_list.3", cf.paths['man3'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man3/attr_multi.3", cf.paths['man3'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man3/attr_remove.3", cf.paths['man3'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man3/attr_set.3", cf.paths['man3'])

    self.inst_symlink(f"{cf.paths['man3']}/attr_get.3", f"{cf.paths['man3']}/attr_getf.3")
    self.inst_symlink(f"{cf.paths['man3']}/attr_list.3", f"{cf.paths['man3']}/attr_listf.3")
    self.inst_symlink(f"{cf.paths['man3']}/attr_multi.3", f"{cf.paths['man3']}/attr_multif.3")
    self.inst_symlink(f"{cf.paths['man3']}/attr_remove.3", f"{cf.paths['man3']}/attr_removef.3")
    self.inst_symlink(f"{cf.paths['man3']}/attr_set.3", f"{cf.paths['man3']}/attr_setf.3")
