#    app-arch/tar/tar-1.35.build.py
#    Thu Nov  7 01:08:57 UTC 2024

#    Copyright:: (c) 2024 Darren Kirby
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
    # FIXME: There is some sort of bug here; unsure if in tar configure script or elsewhere
    # This fails when running a system builds install, even after setting EUID to non-privileged.
    # line 39027 in the tar configure script explicitly tests EUID:
    # if (geteuid () == ROOT_UID) return 99;
    # However, it still fails with non-root EUID; so a sed hack to remove the line,
    # until I can figure it out.
    os.system("sed -i '/if (geteuid () == ROOT_UID) return 99/d' configure")
    return os.system(f"./configure --prefix=/usr")


def make(self):
    return os.system("make")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_binary(f"{self.p['_ub']}/tar", self.p['ub'])
    self.inst_binary(f"{self.p['_ule']}/rmt", self.p['ub'])
    self.inst_manpage(f"{self.p['_man1']}/tar.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man8']}/rmt.8", self.p['man8'])
