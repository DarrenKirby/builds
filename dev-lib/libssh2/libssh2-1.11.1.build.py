#    dev-lib/libssh2/libssh2-1.11.1.build.py
#    Sun Nov 24 00:38:22 UTC 2024

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
    return os.system("./configure --prefix=/usr "
                     "--disable-docker-tests "
                     "--disable-static")


def make(self):
    return os.system(f"make {cf.config['makeopts']}")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_header(f"{self.p['_ui']}/libssh2.h", self.p['ui'])
    self.inst_header(f"{self.p['_ui']}/libssh2_publickey.h", self.p['ui'])
    self.inst_header(f"{self.p['_ui']}/libssh2_sftp.h", self.p['ui'])

    self.inst_library(f"{self.p['_ul']}/libssh2.so.1.0.1", self.p['ul'])
    self.inst_symlink(self.p['ul'] + "/libssh2.so.1.0.1", self.p['ul'] + "/libssh2.so.1")
    self.inst_symlink(self.p['ul'] + "/libssh2.so.1.0.1", self.p['ul'] + "/libssh2.so")

    self.inst_file(self.p['_ul'] + "/pkgconfig/libssh2.pc", self.p['ul'] + "/pkgconfig/")

    for manpage in os.listdir(self.p['_man3']):
        self.inst_manpage(f"{self.p['_man3']}/{manpage}", self.p['man3'])
