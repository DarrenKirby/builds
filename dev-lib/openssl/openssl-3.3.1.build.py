#    dev-lib/openssl/openssl-3.3.1.build.py
#    Wed Dec  4 18:53:09 UTC 2024

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
    return self.do("./configure --prefix=/usr "
                   "--openssldir=/etc/ssl "
                   "--libdir=lib "
                   "shared "
                   "zlib-dynamic")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    self.do("sed -i '/INSTALL_LIBS/s/libcrypto.a libssl.a//' Makefile")
    return self.do(f"make DESTDIR={self.seg_dir} MANSUFFIX=ssl install")


def install(self):
    pass