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
    return os.system(f"./configure --prefix={self.seg_dir} --disable-static")


def make(self):
    return os.system("make")


def make_install(self):
    return os.system("make install")


def install(self):
    self.inst_header(f"{self.seg_dir}/include/urcu-bp.h", cf.paths['ui'])
    self.inst_header(f"{self.seg_dir}/include/urcu-call-rcu.h", cf.paths['ui'])
    self.inst_header(f"{self.seg_dir}/include/urcu-defer.h", cf.paths['ui'])
    self.inst_header(f"{self.seg_dir}/include/urcu-flavor.h", cf.paths['ui'])
    self.inst_header(f"{self.seg_dir}/include/urcu-pointer.h", cf.paths['ui'])
    self.inst_header(f"{self.seg_dir}/include/urcu-qsbr.h", cf.paths['ui'])
    self.inst_header(f"{self.seg_dir}/include/urcu.h", cf.paths['ui'])
    self.inst_directory(f"{self.seg_dir}/include/urcu/", f"{cf.paths['ui']}/urcu/")

    self.inst_library(f"{self.seg_dir}/lib/liburcu-bp.so.8.1.0", cf.paths['ul'])
    self.inst_symlink(f"{cf.paths['ul']}/liburcu-bp.so.8.1.0", f"{cf.paths['ul']}/liburcu-bp.so")
    self.inst_symlink(f"{cf.paths['ul']}/liburcu-bp.so.8.1.0", f"{cf.paths['ul']}/liburcu-bp.so.8")

    self.inst_library(f"{self.seg_dir}/lib/liburcu-cds.so.8.1.0", cf.paths['ul'])
    self.inst_symlink(f"{cf.paths['ul']}/liburcu-cds.so.8.1.0", f"{cf.paths['ul']}/liburcu-cds.so")
    self.inst_symlink(f"{cf.paths['ul']}/liburcu-cds.so.8.1.0", f"{cf.paths['ul']}/liburcu-cds.so.8")

    self.inst_library(f"{self.seg_dir}/lib/liburcu-common.so.8.1.0", cf.paths['ul'])
    self.inst_symlink(f"{cf.paths['ul']}/liburcu-common.so.8.1.0", f"{cf.paths['ul']}/liburcu-common.so")
    self.inst_symlink(f"{cf.paths['ul']}/liburcu-common.so.8.1.0", f"{cf.paths['ul']}/liburcu-common.so.8")

    self.inst_library(f"{self.seg_dir}/lib/liburcu-mb.so.8.1.0", cf.paths['ul'])
    self.inst_symlink(f"{cf.paths['ul']}/liburcu-mb.so.8.1.0", f"{cf.paths['ul']}/liburcu-mb.so")
    self.inst_symlink(f"{cf.paths['ul']}/liburcu-mb.so.8.1.0", f"{cf.paths['ul']}/liburcu-mb.so.8")

    self.inst_library(f"{self.seg_dir}/lib/liburcu-memb.so.8.1.0", cf.paths['ul'])
    self.inst_symlink(f"{cf.paths['ul']}/liburcu-memb.so.8.1.0", f"{cf.paths['ul']}/liburcu-memb.so")
    self.inst_symlink(f"{cf.paths['ul']}/liburcu-memb.so.8.1.0", f"{cf.paths['ul']}/liburcu-memb.so.8")

    self.inst_library(f"{self.seg_dir}/lib/liburcu-qsbr.so.8.1.0", cf.paths['ul'])
    self.inst_symlink(f"{cf.paths['ul']}/liburcu-qsbr.so.8.1.0", f"{cf.paths['ul']}/liburcu-qsbr.so")
    self.inst_symlink(f"{cf.paths['ul']}/liburcu-qsbr.so.8.1.0", f"{cf.paths['ul']}/liburcu-qsbr.so.8")

    self.inst_library(f"{self.seg_dir}/lib/liburcu-signal.so.8.1.0", cf.paths['ul'])
    self.inst_symlink(f"{cf.paths['ul']}/liburcu-signal.so.8.1.0", f"{cf.paths['ul']}/liburcu-signal.so")
    self.inst_symlink(f"{cf.paths['ul']}/liburcu-signal.so.8.1.0", f"{cf.paths['ul']}/liburcu-signal.so.8")

    self.inst_library(f"{self.seg_dir}/lib/liburcu.so.8.1.0", cf.paths['ul'])
    self.inst_symlink(f"{cf.paths['ul']}/liburcu.so.8.1.0", f"{cf.paths['ul']}/liburcu.so")
    self.inst_symlink(f"{cf.paths['ul']}/liburcu.so.8.1.0", f"{cf.paths['ul']}/liburcu.so.8")
