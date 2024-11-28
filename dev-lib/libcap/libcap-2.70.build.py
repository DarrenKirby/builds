#    dev-lib/libcap/libcap-2.70.build.py
#    Thu Nov 21 16:33:12 UTC 2024

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
    # Prevent static libs
    return self.do("sed -i '/install -m.*STA/d' libcap/Makefile")


def make(self):
    return self.do(f"make {cf.config['makeopts']} prefix={self.seg_dir}/usr lib=lib")


def make_install(self):
    return self.do(f"make prefix={self.seg_dir}/usr lib=lib install")


def install(self):
    self.inst_header(self.p['_ui'] + "/sys/capability.h", self.p['ui'] + "/sys/")
    self.inst_header(self.p['_ui'] + "/sys/psx_syscall.h", self.p['ui'] + "/sys/")

    self.inst_library(f"{self.p['_ul']}/libcap.so.2.70", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libcap.so.2.70", f"{self.p['ul']}/libcap.so.2")
    self.inst_symlink(f"{self.p['ul']}/libcap.so.2", f"{self.p['ul']}/libcap.so")

    self.inst_library(f"{self.p['_ul']}/libpsx.so.2.70", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libpsx.so.2.70", f"{self.p['ul']}/libpsx.so.2")
    self.inst_symlink(f"{self.p['ul']}/libpsx.so.2", f"{self.p['ul']}/libpsx.so")

    self.inst_file(self.p['_ul'] + "/security/pam_cap.so", self.p['ul'] + "/security/pam_cap.so")
    self.inst_file(self.p['_ul'] + "/pkgconfig/libcap.pc", self.p['ul'] + "/pkgconfig/libcap.pc")
    self.inst_file(self.p['_ul'] + "/pkgconfig/libpsx.pc", self.p['ul'] + "/pkgconfig/libpsx.pc")

    for file in os.listdir(self.p['_us']):
        self.inst_binary(f"{self.p['_us']}/{file}", self.p['us'])

    self.inst_manpage(self.p['_man1'] + "/capsh.1", self.p['man1'])
    self.inst_manpage(self.p['_man5'] + "/capability.conf.5", self.p['man5'])

    for file in os.listdir(self.p['_man3']):
        self.inst_manpage(f"{self.p['_man3']}/{file}", self.p['man3'])

    for file in os.listdir(self.p['_man8']):
        self.inst_manpage(f"{self.p['_man8']}/{file}", self.p['man8'])
