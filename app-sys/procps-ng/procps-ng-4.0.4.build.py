#    app-sys/procps/procps-4.0.4.build.py
#    Thu Nov 28 22:39:58 UTC 2024

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


def install_source_posthook(self):
    os.rename(f"procps-v{self.version}", f"procps-ng-{self.version}")


def configure(self):
    if not os.path.exists("./configure"):
        self.do("./autogen.sh")
    return self.do("./configure --prefix=/usr --disable-static --disable-kill")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    for binary in os.listdir(self.p['_ub']):
        self.inst_binary(f"{self.p['_ub']}/{binary}", self.p['ub'])

    self.inst_directory(self.p['_ui'] + '/libproc2/', self.p['ui'] + '/libproc2/')

    self.inst_library(f"{self.p['_ul']}/libproc2.so.0.0.2", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libproc2.so.0.0.2", f"{self.p['ul']}/libproc2.so")
    self.inst_symlink(f"{self.p['ul']}/libproc2.so.0.0.2", f"{self.p['ul']}/libproc2.so.0")

    self.inst_file(self.p['_ul'] + "/pkgconfig/libproc2.pc", self.p['ul'] + "/pkgconfig/")

    self.inst_binary(f"{self.p['_us']}/sysctl", self.p['us'])

    for file in os.listdir(self.p['_man1']):
        self.inst_manpage(f"{self.p['_man1']}/{file}", self.p['man1'])

    for file in os.listdir(self.p['_man3']):
        self.inst_manpage(f"{self.p['_man3']}/{file}", self.p['man3'])

    for file in os.listdir(self.p['_man8']):
        self.inst_manpage(f"{self.p['_man8']}/{file}", self.p['man8'])

    self.inst_manpage(self.p['_man5'] + "/sysctl.conf.5", self.p['man5'])
