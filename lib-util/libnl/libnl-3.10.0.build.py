#    lib-util/libnl/libnl-3.10.0.build.py
#    Sun Dec  1 19:19:50 UTC 2024

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
    conf_d = '/etc' if cf.config['user'] == 'root' else '/usr/etc'
    return self.do("./configure --prefix=/usr "
                   f"--sysconfdir={conf_d} "
                   "--disable-static")


def make(self):
    return self.do("make")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    for file in os.listdir(self.p['_ub']):
        self.inst_binary(f"{self.p['_ub']}/{file}", self.p['ub'])

    conf_d = 'e' if cf.config['user'] == 'root' else 'ue'
    self.inst_directory(f"{self.p['_' + conf_d]}/libnl/", f"{self.p[conf_d]}/libnl/")

    self.inst_directory(f"{self.p['_ui']}/libnl3/", f"{self.p['ui']}/libnl3/")
    self.inst_directory(f"{self.p['_ul']}/libnl/", f"{self.p['ul']}/libnl/")

    self.inst_library(f"{self.p['_ul']}/libnl-3.so.200.26.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libnl-3.so.200.26.0", f"{self.p['ul']}/libnl-3.so")
    self.inst_symlink(f"{self.p['ul']}/libnl-3.so.200.26.0", f"{self.p['ul']}/libnl-3.so.200")

    self.inst_library(f"{self.p['_ul']}/libnl-cli-3.so.200.26.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libnl-cli-3.so.200.26.0", f"{self.p['ul']}/libnl-cli-3.so")
    self.inst_symlink(f"{self.p['ul']}/libnl-cli-3.so.200.26.0", f"{self.p['ul']}/libnl-cli-3.so.200")

    self.inst_library(f"{self.p['_ul']}/libnl-genl-3.so.200.26.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libnl-genl-3.so.200.26.0", f"{self.p['ul']}/libnl-genl-3.so")
    self.inst_symlink(f"{self.p['ul']}/libnl-genl-3.so.200.26.0", f"{self.p['ul']}/libnl-genl-3.so.200")

    self.inst_library(f"{self.p['_ul']}/libnl-idiag-3.so.200.26.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libnl-idiag-3.so.200.26.0", f"{self.p['ul']}/libnl-idiag-3.so")
    self.inst_symlink(f"{self.p['ul']}/libnl-idiag-3.so.200.26.0", f"{self.p['ul']}/libnl-idiag-3.so.200")

    self.inst_library(f"{self.p['_ul']}/libnl-nf-3.so.200.26.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libnl-nf-3.so.200.26.0", f"{self.p['ul']}/libnl-nf-3.so")
    self.inst_symlink(f"{self.p['ul']}/libnl-nf-3.so.200.26.0", f"{self.p['ul']}/libnl-nf-3.so.200")

    self.inst_library(f"{self.p['_ul']}/libnl-route-3.so.200.26.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libnl-route-3.so.200.26.0", f"{self.p['ul']}/libnl-route-3.so")
    self.inst_symlink(f"{self.p['ul']}/libnl-route-3.so.200.26.0", f"{self.p['ul']}/libnl-route-3.so.200")

    self.inst_library(f"{self.p['_ul']}/libnl-xfrm-3.so.200.26.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libnl-xfrm-3.so.200.26.0", f"{self.p['ul']}/libnl-xfrm-3.so")
    self.inst_symlink(f"{self.p['ul']}/libnl-xfrm-3.so.200.26.0", f"{self.p['ul']}/libnl-xfrm-3.so.200")

    for file in os.listdir(self.p['_ul'] + "/pkgconfig/"):
        self.inst_file(f"{self.p['_ul']}/pkgconfig/{file}", self.p['ul'] + "/pkgconfig/")

    for file in os.listdir(self.p['_man8']):
        self.inst_manpage(f"{self.p['_man8']}/{file}", self.p['man8'])
