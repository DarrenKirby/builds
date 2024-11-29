#    app-sys/kmod/kmod-33.build.py
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


def configure(self):
    return self.do("./configure --prefix=/usr "
                   "--sysconfdir=/etc "
                   "--with-openssl "
                   "--with-xz "
                   "--with-zstd "
                   "--with-zlib "
                   "--disable-manpages")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_binary(self.p['_ub'] + "/kmod", self.p['ub'])

    self.inst_symlink(f"{self.p['ub']}/kmod", f"{self.p['ub']}/depmod")
    self.inst_symlink(f"{self.p['ub']}/kmod", f"{self.p['ub']}/insmod")
    self.inst_symlink(f"{self.p['ub']}/kmod", f"{self.p['ub']}/lsmod")
    self.inst_symlink(f"{self.p['ub']}/kmod", f"{self.p['ub']}/modinfo")
    self.inst_symlink(f"{self.p['ub']}/kmod", f"{self.p['ub']}/modprobe")
    self.inst_symlink(f"{self.p['ub']}/kmod", f"{self.p['ub']}/rmmod")

    self.inst_header(f"{self.p['_ui']}/libkmod.h", self.p['ui'])

    self.inst_library(f"{self.p['_ul']}/libkmod.so.2.5.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libkmod.so.2.5.0", f"{self.p['ul']}/libkmod.so")
    self.inst_symlink(f"{self.p['ul']}/libkmod.so.2.5.0", f"{self.p['ul']}/libkmod.so.2")

    self.inst_file(self.p['ul'] + "/pkgconfig/libkmod.pc", self.p['ul'] + "/pkgconfig/")

    os.makedirs(self.p['ush'] + "/bash-completion/completions/", exist_ok=True)
    os.makedirs(self.p['ush'] + "/pkgconfig/", exist_ok=True)

    self.inst_file(self.p['_ush'] + "/bash-completion/completions/kmod",
                   self.p['ush'] + "/bash-completion/completions/")
    self.inst_file(self.p['_ush'] + "/pkgconfig/kmod.pc", self.p['ush'] + "/pkgconfig/")







