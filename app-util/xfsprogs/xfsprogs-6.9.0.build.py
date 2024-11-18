#    app-util/xfsprogs/xfsprogs-6.9.0.build.py
#    Mon Nov 18 20:33:19 UTC 2024

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


depend="dev-lib/inih,lib-util/liburcu"


def configure(self):
    return os.system("./configure --prefix=/usr --libdir=/usr/lib --enable-static=no")


def make(self):
    return os.system(f"make DEBUG=-DNDEBUG {cf.config['makeopts']}")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} install")


def install(self):
    # xfsprogs is not honouring --prefix=/usr and --libdir=/usr/lib
    self.inst_library(f"{self.seg_dir}/lib64/libhandle.so.1.0.3", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libhandle.so.1.0.3", f"{self.p['ul']}/libhandle.so.1")

    for file in os.listdir(self.p['_s']):
        self.inst_script(f"{self.p['_s']}/{file}", self.p['us'])

    self.inst_manpage(f"{self.p['_man5']}/projects.5", self.p['man5'])
    self.inst_manpage(f"{self.p['_man5']}/projid.5", self.p['man5'])
    self.inst_manpage(f"{self.p['_man5']}/xfs.5", self.p['man5'])

    for file in os.listdir(self.p['_man8']):
        self.inst_manpage(f"{self.p['_man8']}/{file}", self.p['man8'])

    self.inst_directory(f"{self.p['_ush']}/xfsprogs/", f"{self.p['ush']}/xfsprogs/")

    # Install xfs.rules to /usr/lib/udev/rules.d
    self.inst_file(f"{self.p['_ul']}/udev/rules.d/64-xfs.rules", f"{self.p['ul']}/udev/rules.d/64-xfs.rules")

    # Strip the binaries
    for file in ["mkfs.xfs", "xfs_repair"]:
        os.system(f"strip -v {self.p['us']}/{file}")
