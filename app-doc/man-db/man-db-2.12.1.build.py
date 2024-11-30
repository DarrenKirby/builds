#    app-doc/man-db/man-db-2.12.1.build.py
#    Thu Nov 28 22:38:24 UTC 2024

#    Copyright:: (c) 2024
#    Author:: Darren Kirby (mailto:Darren Kirby)

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
    confd = "/etc" if cf.config['user'] == 'root' else "/usr/etc"
    return self.do("./configure --prefix=/usr "
                   f"--sysconfdir={confd} "
                   "--disable-setuid "
                   "--enable-cache-owner=bin "
                   "--with-browser=/usr/bin/lynx "
                   "--with-vgrind=/usr/bin/vgrind "
                   "--with-grap=/usr/bin/grap "
                   "--with-systemdtmpfilesdir= "
                   "--with-systemdsystemunitdir=")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    confd = "e" if cf.config['user'] == 'root' else "ue"
    self.inst_config(self.p['_' + confd] + "/man_db.conf", self.p[confd])

    for binary in os.listdir(self.p['_ub']):
        if binary not in ["apropos"]:
            self.inst_binary(f"{self.p['_ub']}/{binary}", self.p['ub'])

    self.inst_symlink(self.p['ub'] + "/whatis", self.p['ub'] + "/apropos")

    os.makedirs(self.p['ul'] + "/man-db/", exist_ok=True)
    self.inst_library(f"{self.p['_ul']}/man-db/libman-2.12.1.so", self.p['ul'] + "/man-db/")
    self.inst_symlink(f"{self.p['ul']}/man-db/libman-2.12.1.so", f"{self.p['ul']}/man-db/libman.so")

    self.inst_library(f"{self.p['_ul']}/man-db/libmandb-2.12.1.so", self.p['ul'] + "/man-db/")
    self.inst_symlink(f"{self.p['ul']}/man-db/libmandb-2.12.1.so", f"{self.p['ul']}/man-db/libmandb.so")

    self.inst_directory(f"{self.p['_ule']}/man-db/", f"{self.p['ule']}/man-db/")

    self.inst_binary(f"{self.p['_us']}/accessdb", self.p['us'])

    # install manpages
    for file in os.listdir(self.p['_man1']):
        self.inst_manpage(f"{self.p['_man1']}/{file}", self.p['man1'])

    for file in os.listdir(self.p['_man5']):
        self.inst_manpage(f"{self.p['_man5']}/{file}", self.p['man5'])

    for file in os.listdir(self.p['_man8']):
        self.inst_manpage(f"{self.p['_man8']}/{file}", self.p['man8'])
