#    lib-util/libevent/libevent-2.1.12.build.py
#    Sun Dec  1 18:40:08 UTC 2024
import os


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
    os.rename(f"libevent-{self.version}-stable", f"libevent-{self.version}")


def configure(self):
    self.do("sed -i 's/python/&3/' event_rpcgen.py")
    return self.do("./configure --prefix=/usr --disable-static")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_script(self.p['_ub'] + "/event_rpcgen.py", self.p['ub'])

    self.inst_header(self.p['_ui'] + "/evdns.h", self.p['ui'])
    self.inst_header(self.p['_ui'] + "/event.h", self.p['ui'])
    self.inst_header(self.p['_ui'] + "/evhttp.h", self.p['ui'])
    self.inst_header(self.p['_ui'] + "/evrpc.h", self.p['ui'])
    self.inst_header(self.p['_ui'] + "/evutil.h", self.p['ui'])

    self.inst_directory(f"{self.p['_ui']}/event2/", f"{self.p['ui']}/event2/")

    self.inst_library(f"{self.p['_ul']}/libevent-2.1.so.7.0.1", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libevent-2.1.so.7.0.1", f"{self.p['ul']}/libevent.so")
    self.inst_symlink(f"{self.p['ul']}/libevent-2.1.so.7.0.1", f"{self.p['ul']}/libevent-2.1.so.7")

    self.inst_library(f"{self.p['_ul']}/libevent_core-2.1.so.7.0.1", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libevent_core-2.1.so.7.0.1", f"{self.p['ul']}/libevent_core.so")
    self.inst_symlink(f"{self.p['ul']}/libevent_core-2.1.so.7.0.1", f"{self.p['ul']}/libevent_core-2.1.so.7")

    self.inst_library(f"{self.p['_ul']}/libevent_extra-2.1.so.7.0.1", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libevent_extra-2.1.so.7.0.1", f"{self.p['ul']}/libevent_extra.so")
    self.inst_symlink(f"{self.p['ul']}/libevent_extra-2.1.so.7.0.1", f"{self.p['ul']}/libevent_extra-2.1.so.7")

    self.inst_library(f"{self.p['_ul']}/libevent_openssl-2.1.so.7.0.1", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libevent_openssl-2.1.so.7.0.1", f"{self.p['ul']}/libevent_openssl.so")
    self.inst_symlink(f"{self.p['ul']}/libevent_openssl-2.1.so.7.0.1", f"{self.p['ul']}/libevent_openssl-2.1.so.7")

    self.inst_library(f"{self.p['_ul']}/libevent_pthreads-2.1.so.7.0.1", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libevent_pthreads-2.1.so.7.0.1", f"{self.p['ul']}/libevent_pthreads-2.1.so")
    self.inst_symlink(f"{self.p['ul']}/libevent_pthreads-2.1.so.7.0.1", f"{self.p['ul']}/libevent_pthreads-2.1.so.7")

    for file in os.listdir(self.p['_ul'] + "/pkgconfig/"):
        self.inst_file(f"{self.p['_ul']}/pkgconfig/{file}", self.p['ul'] + "/pkgconfig/")
