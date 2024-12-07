#    dev-lib/openssl/openssl-3.3.2.build.py
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
    confd = "/etc/ssl" if cf.config['user'] == 'root' else "/usr/etc/ssl"
    return self.do("./config --prefix=/usr "
                   f"--openssldir={confd} "
                   "--libdir=lib "
                   "shared "
                   "zlib-dynamic")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    self.do("sed -i '/INSTALL_LIBS/s/libcrypto.a libssl.a//' Makefile")
    return self.do(f"make DESTDIR={self.seg_dir} MANSUFFIX=ssl install")


def install(self):
    confd = "e" if cf.config['user'] == 'root' else "ue"
    self.inst_directory(self.p['_' + confd] + "/ssl", self.p[confd] + "/ssl")

    self.inst_script(self.p['_ub'] + "/c_rehash", self.p['ub'])
    self.inst_binary(self.p['_ub'] + "/openssl", self.p['ub'])

    self.inst_directory(self.p['_ui'] + "/openssl", self.p['ui'] + "/openssl")

    self.inst_directory(self.p['_ul'] + "/cmake/OpenSSL/", self.p['ul'] + "//cmake/OpenSSL/")
    self.inst_directory(self.p['_ul'] + "/engines-3/", self.p['ul'] + "/engines-3/")
    self.inst_directory(self.p['_ul'] + "/ossl-modules/", self.p['ul'] + "/ossl-modules/")

    self.inst_library(self.p['_ul'] + "/libcrypto.so.3", self.p['ul'])
    self.inst_symlink(self.p['ul'] + "/libcrypto.so.3", self.p['ul'] + "/libcrypto.so")

    self.inst_library(self.p['_ul'] + "/libssl.so.3", self.p['ul'])
    self.inst_symlink(self.p['ul'] + "/libssl.so.3", self.p['ul'] + "/libssl.so")

    self.inst_file(self.p['_ul'] + "/pkgconfig/libcrypto.pc", self.p['ul'] + "/pkgconfig/")
    self.inst_file(self.p['_ul'] + "/pkgconfig/libssl.pc", self.p['ul'] + "/pkgconfig/")
    self.inst_file(self.p['_ul'] + "/pkgconfig/openssl.pc", self.p['ul'] + "/pkgconfig/")

    for file in os.listdir(self.p['_man1']):
        if os.path.islink(f"{self.p['_man1']}/{file}"):
            # We need to copy symlinks, and add to manifest manually
            os.rename(f"{self.p['_man1']}/{file}", f"{self.p['man1']}/{file}")
            self.manifest.append(f"{self.p['man1']}/{file}")
        else:
            self.inst_manpage(f"{self.p['_man1']}/{file}", self.p['man1'], compress=False)

    for file in os.listdir(self.p['_man3']):
        if os.path.islink(f"{self.p['_man3']}/{file}"):
            # We need to copy symlinks, and add to manifest manually
            os.rename(f"{self.p['_man3']}/{file}", f"{self.p['man3']}/{file}")
            self.manifest.append(f"{self.p['man3']}/{file}")
        else:
            self.inst_manpage(f"{self.p['_man3']}/{file}", self.p['man3'], compress=False)

    for file in os.listdir(self.p['_man5']):
        if os.path.islink(f"{self.p['_man5']}/{file}"):
            # We need to copy symlinks, and add to manifest manually
            os.rename(f"{self.p['_man5']}/{file}", f"{self.p['man5']}/{file}")
            self.manifest.append(f"{self.p['man5']}/{file}")
        else:
            self.inst_manpage(f"{self.p['_man5']}/{file}", self.p['man5'], compress=False)

    for file in os.listdir(self.p['_man7']):
        if os.path.islink(f"{self.p['_man7']}/{file}"):
            # We need to copy symlinks, and add to manifest manually
            os.rename(f"{self.p['_man7']}/{file}", f"{self.p['man7']}/{file}")
            self.manifest.append(f"{self.p['man7']}/{file}")
        else:
            self.inst_manpage(f"{self.p['_man7']}/{file}", self.p['man7'], compress=False)
