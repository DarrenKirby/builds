#    dev-tool/binutils/binutils-2.43.1.build.py
#    Sat Nov 23 19:37:47 UTC 2024

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
    os.mkdir("build")
    os.chdir("build/")
    return os.system("../configure --prefix=/usr "
                     f"--sysconfdir={'/etc' if cf.config['user'] == 'root' else '/usr/etc'} "
                     "--enable-gold "
                     "--enable-ld=default "
                     "--enable-plugins "
                     "--enable-shared "
                     "--disable-werror "
                     "--enable-64-bit-bfd "
                     "--enable-new-dtags "
                     "--with-system-zlib "
                     "--enable-default-hash-style=gnu")


def make(self):
    return os.system("make tooldir=/usr")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} tooldir=/usr install")


def install(self):
    for file in os.listdir(self.p['_ub']):
        if file not in ["gp-display-html"]:
            self.inst_binary(f"{self.p['_ub']}/{file}", self.p['ub'])
        else:
            self.inst_script(f"{self.p['_ub']}/{file}", self.p['ub'])

    # install configuration file
    conf_d = 'e' if cf.config['user'] == 'root' else 'ue'
    self.inst_config(self.p['_' + conf_d] + '/gprofng.rc', self.p[conf_d])

    for header in os.listdir(self.p['_ui']):
        self.inst_header(f"{self.p['_ui']}/{header}", self.p['ui'])

    # Not ideal hard coding the versions, but we can serch/replacethem when the package updates
    for file in ["libbfd-2.43.1.so", "libctf-nobfd.so.0.0.0", "libctf.so.0.0.0", "libgprofng.so.0.0.0",
                 "libopcodes-2.43.1.so", "libsframe.so.1.0.0"]:
        self.inst_library(f"{self.p['_ul']}/{file}", self.p['ul'])

    # links
    self.inst_symlink(self.p['ul'] + "/libbfd-2.43.1.so", self.p['ul'] + "/libbfd.so")
    self.inst_symlink(self.p['ul'] + "/libctf-nobfd.so.0.0.0", self.p['ul'] + "/libctf-nobfd.so")
    self.inst_symlink(self.p['ul'] + "/libctf-nobfd.so.0.0.0", self.p['ul'] + "/libctf-nobfd.so.0")
    self.inst_symlink(self.p['ul'] + "/libctf.so.0.0.0", self.p['ul'] + "/libctf.so")
    self.inst_symlink(self.p['ul'] + "/libctf.so.0.0.0", self.p['ul'] + "/libctf.so.0")
    self.inst_symlink(self.p['ul'] + "/libgprofng.so.0.0.0", self.p['ul'] + "/libgprofng.so")
    self.inst_symlink(self.p['ul'] + "/libgprofng.so.0.0.0", self.p['ul'] + "/libgprofng.so.0")
    self.inst_symlink(self.p['ul'] + "/libopcodes-2.43.1.so", self.p['ul'] + "/libopcodes.so")
    self.inst_symlink(self.p['ul'] + "/libsframe.so.1.0.0", self.p['ul'] + "/libsframe.so")
    self.inst_symlink(self.p['ul'] + "/libsframe.so.1.0.0", self.p['ul'] + "/libsframe.so.1")

    # Directories
    for directory in ["/bfd-plugins/", "/gprofng/", "/ldscripts/"]:
        self.inst_directory(self.p['_ul'] + directory, self.p['ul'] + directory)

    for manpage in os.listdir(self.p['_man1']):
        self.inst_manpage(f"{self.p['_man1']}/{manpage}", self.p['man1'])
