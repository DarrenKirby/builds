#    lib-util/liburcu/liburcu-0.14.1.build.py
#    Fri Oct 25 22:14:14 UTC 2024

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


# tarball name does not match package name
def install_source_posthook(self):
    os.rename(f"userspace-rcu-{self.version}", f"liburcu-{self.version}")


def configure(self):
    return self.do("./configure --prefix=/usr --disable-static")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_header(f"{self.p['_ui']}/urcu-bp.h", self.p['ui'])
    self.inst_header(f"{self.p['_ui']}/urcu-call-rcu.h", self.p['ui'])
    self.inst_header(f"{self.p['_ui']}/urcu-defer.h", self.p['ui'])
    self.inst_header(f"{self.p['_ui']}/urcu-flavor.h", self.p['ui'])
    self.inst_header(f"{self.p['_ui']}/urcu-pointer.h", self.p['ui'])
    self.inst_header(f"{self.p['_ui']}/urcu-qsbr.h", self.p['ui'])
    self.inst_header(f"{self.p['_ui']}/urcu.h", self.p['ui'])
    self.inst_directory(f"{self.p['_ui']}/urcu/", f"{self.p['ui']}/urcu/")

    self.inst_library(f"{self.p['_ul']}/liburcu-bp.so.8.1.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/liburcu-bp.so.8.1.0", f"{self.p['ul']}/liburcu-bp.so")
    self.inst_symlink(f"{self.p['ul']}/liburcu-bp.so.8.1.0", f"{self.p['ul']}/liburcu-bp.so.8")

    self.inst_library(f"{self.p['_ul']}/liburcu-cds.so.8.1.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/liburcu-cds.so.8.1.0", f"{self.p['ul']}/liburcu-cds.so")
    self.inst_symlink(f"{self.p['ul']}/liburcu-cds.so.8.1.0", f"{self.p['ul']}/liburcu-cds.so.8")

    self.inst_library(f"{self.p['_ul']}/liburcu-common.so.8.1.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/liburcu-common.so.8.1.0", f"{self.p['ul']}/liburcu-common.so")
    self.inst_symlink(f"{self.p['ul']}/liburcu-common.so.8.1.0", f"{self.p['ul']}/liburcu-common.so.8")

    self.inst_library(f"{self.p['_ul']}/liburcu-mb.so.8.1.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/liburcu-mb.so.8.1.0", f"{self.p['ul']}/liburcu-mb.so")
    self.inst_symlink(f"{self.p['ul']}/liburcu-mb.so.8.1.0", f"{self.p['ul']}/liburcu-mb.so.8")

    self.inst_library(f"{self.p['_ul']}/liburcu-memb.so.8.1.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/liburcu-memb.so.8.1.0", f"{self.p['ul']}/liburcu-memb.so")
    self.inst_symlink(f"{self.p['ul']}/liburcu-memb.so.8.1.0", f"{self.p['ul']}/liburcu-memb.so.8")

    self.inst_library(f"{self.p['_ul']}/liburcu-qsbr.so.8.1.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/liburcu-qsbr.so.8.1.0", f"{self.p['ul']}/liburcu-qsbr.so")
    self.inst_symlink(f"{self.p['ul']}/liburcu-qsbr.so.8.1.0", f"{self.p['ul']}/liburcu-qsbr.so.8")

    self.inst_library(f"{self.p['_ul']}/liburcu-signal.so.8.1.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/liburcu-signal.so.8.1.0", f"{self.p['ul']}/liburcu-signal.so")
    self.inst_symlink(f"{self.p['ul']}/liburcu-signal.so.8.1.0", f"{self.p['ul']}/liburcu-signal.so.8")

    self.inst_library(f"{self.p['_ul']}/liburcu.so.8.1.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/liburcu.so.8.1.0", f"{self.p['ul']}/liburcu.so")
    self.inst_symlink(f"{self.p['ul']}/liburcu.so.8.1.0", f"{self.p['ul']}/liburcu.so.8")
