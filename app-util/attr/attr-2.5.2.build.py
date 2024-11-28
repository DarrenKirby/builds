#    app-util/attr/attr-2.5.2.build.py
#    Wed Nov 13 01:29:24 UTC 2024

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
    return self.do(f"./configure --prefix=/usr --disable-static")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_binary(f"{self.p['_ub']}/attr", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/getfattr", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/setfattr", self.p['ub'])

    self.inst_config(f"{self.seg_dir}/usr/etc/xattr.conf", self.p['e'] if cf.config['user'] == 'root' else self.p['ue'])

    self.inst_library(f"{self.p['_ul']}/libattr.so.1.1.2502", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libattr.so.1.1.2502", f"{self.p['ul']}/libattr.so")
    self.inst_symlink(f"{self.p['ul']}/libattr.so.1.1.2502", f"{self.p['ul']}/libattr.so.1")

    self.inst_manpage(f"{self.p['_man1']}/attr.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/getfattr.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/setfattr.1", self.p['man1'])

    self.inst_manpage(f"{self.p['_man3']}/attr_get.3", self.p['man3'])
    self.inst_manpage(f"{self.p['_man3']}/attr_list.3", self.p['man3'])
    self.inst_manpage(f"{self.p['_man3']}/attr_multi.3", self.p['man3'])
    self.inst_manpage(f"{self.p['_man3']}/attr_remove.3", self.p['man3'])
    self.inst_manpage(f"{self.p['_man3']}/attr_set.3", self.p['man3'])

    self.inst_symlink(f"{self.p['man3']}/attr_get.3.bz2", f"{self.p['man3']}/attr_getf.3")
    self.inst_symlink(f"{self.p['man3']}/attr_list.3.bz2", f"{self.p['man3']}/attr_listf.3")
    self.inst_symlink(f"{self.p['man3']}/attr_multi.3.bz2", f"{self.p['man3']}/attr_multif.3")
    self.inst_symlink(f"{self.p['man3']}/attr_remove.3.bz2", f"{self.p['man3']}/attr_removef.3")
    self.inst_symlink(f"{self.p['man3']}/attr_set.3.bz2", f"{self.p['man3']}/attr_setf.3")
