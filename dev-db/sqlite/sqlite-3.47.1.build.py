#    dev-db/sqlite/sqlite-3.47.1.build.py
#    Sat Nov 30 22:23:18 UTC 2024

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
    sqlite_pkg = glob.glob("./sqlite-*")[0]
    os.rename(sqlite_pkg, f"sqlite-{self.version}")


def configure(self):
    return self.do("./configure --prefix=/usr "
                   "--disable-static "
                   "--enable-fts4 "
                   "--enable-fts5 "
                   "CPPFLAGS='-D SQLITE_ENABLE_COLUMN_METADATA=1 "
                   "-D SQLITE_ENABLE_UNLOCK_NOTIFY=1 "
                   "-D SQLITE_ENABLE_DBSTAT_VTAB=1 "
                   "-D SQLITE_SECURE_DELETE=1'")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    pass
    self.inst_binary(f"{self.p['_ub']}/sqlite3", self.p['ub'])

    self.inst_header(f"{self.p['_ui']}/sqlite3.h", self.p['ui'])
    self.inst_header(f"{self.p['_ui']}/sqlite3ext.h", self.p['ui'])

    self.inst_library(f"{self.p['_ul']}/libsqlite3.so.0.8.6", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libsqlite3.so.0.8.6", f"{self.p['ul']}/libsqlite3.so.0")
    self.inst_symlink(f"{self.p['ul']}/libsqlite3.so.0.8.6", f"{self.p['ul']}/libsqlite3.so")

    self.inst_file(self.p['_ul'] + "/pkgconfig/sqlite3.pc", self.p['ul'] + "/pkgconfig/")

    self.inst_manpage(f"{self.p['_man1']}/sqlite3.1", self.p['man1'])
