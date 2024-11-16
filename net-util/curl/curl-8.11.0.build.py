#    net-util/curl/curl-8.11.0.build.py
#    Fri Nov 15 23:58:41 UTC 2024

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


depend = "dev-lib/libpsl"

def configure(self):
    return os.system("./configure --prefix=/usr "
                     "--disable-static "
                     "--with-openssl "
                     "--enable-threaded-resolver "
                     # "--with-libssh2 "
                     "--with-ca-path=/etc/ssl/certs")


def make(self):
    return os.system(f"make {cf.config['makeopts']}")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_binary(f"{self.p['_ub']}/curl", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/curl-config", self.p['ub'])

    self.inst_directory(f"{self.p['_ui']}/curl/", f"{self.p['ui']}/curl/")

    self.inst_library(f"{self.p['_ul']}/libcurl.so.4.8.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libcurl.so.4.8.0", f"{self.p['ul']}/libcurl.so")
    self.inst_symlink(f"{self.p['ul']}/libcurl.so.4.8.0", f"{self.p['ul']}/libcurl.so.4")

    self.inst_file(f"{self.p['_ul']}/pkgconfig/libcurl.pc", f"{self.p['ul']}/pkgconfig/")
    self.inst_file(f"{self.p['_ush']}/aclocal/libcurl.m4", f"{self.p['ush']}/aclocal/")

    self.inst_manpage(f"{self.p['_man1']}/curl-config.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/curl.1", self.p['man1'])

    for file in os.listdir(self.p['_man3']):
        self.inst_manpage(f"{self.p['_man3']}/{file}", self.p['man3'])
