#    app-sys/util-linux/util-linux-2.40.2.build.py
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
    user_disable = ""
    if cf.config['user'] != 'root':
        cf.yellow("Many of the binaries installed by util-linux require superuser")
        cf.yellow("privileges to install and use correctly. This will cause failures")
        cf.yellow("during the 'make install' step, so this build file disables chown,")
        cf.yellow("chmod, and setuid commands for all user installs of builds.")
        user_disable += "--disable-use-tty-group --disable-makeinstall-chown --disable-makeinstall-setuid"
    if not os.path.exists("./configure"):
        self.do("./autogen.sh")
    return self.do("./configure --bindir=/usr/bin "
                   "--libdir=/usr/lib "
                   "--runstatedir=/run "
                   "--sbindir=/usr/sbin "
                   "--disable-chfn-chsh "
                   "--disable-login "
                   "--disable-nologin "
                   "--disable-su "
                   "--disable-setpriv "
                   "--disable-runuser "
                   "--disable-pylibmount "
                   "--disable-liblastlog2 "
                   "--disable-static "
                   "--without-python "
                   "--without-systemd "
                   "--without-systemdsystemunitdir "
                   f"ADJTIME_PATH=/var/lib/hwclock/adjtime {user_disable}")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    for binary in os.listdir(self.p['_ub']):
        self.inst_binary(f"{self.p['_ub']}/{binary}", self.p['ub'])

    for binary in os.listdir(self.p['_us']):
        self.inst_binary(f"{self.p['_us']}/{binary}", self.p['us'])

    self.inst_library(f"{self.p['_ul']}/libblkid.so.1.1.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libblkid.so.1.1.0", f"{self.p['ul']}/libblkid.so")
    self.inst_symlink(f"{self.p['ul']}/libblkid.so.1.1.0", f"{self.p['ul']}/libblkid.so.1")

    self.inst_library(f"{self.p['_ul']}/libfdisk.so.1.1.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libfdisk.so.1.1.0", f"{self.p['ul']}/libfdisk.so")
    self.inst_symlink(f"{self.p['ul']}/libfdisk.so.1.1.0", f"{self.p['ul']}/libfdisk.so.1")

    self.inst_library(f"{self.p['_ul']}/libmount.so.1.1.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libmount.so.1.1.0", f"{self.p['ul']}/libmount.so")
    self.inst_symlink(f"{self.p['ul']}/libmount.so.1.1.0", f"{self.p['ul']}/libmount.so.1")

    self.inst_library(f"{self.p['_ul']}/libsmartcols.so.1.1.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libsmartcols.so.1.1.0", f"{self.p['ul']}/libsmartcols.so")
    self.inst_symlink(f"{self.p['ul']}/libsmartcols.so.1.1.0", f"{self.p['ul']}/libsmartcols.so.1")

    self.inst_library(f"{self.p['_ul']}/libuuid.so.1.3.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libuuid.so.1.3.0", f"{self.p['ul']}/libuuid.so")
    self.inst_symlink(f"{self.p['ul']}/libuuid.so.1.3.0", f"{self.p['ul']}/libuuid.so.1")
