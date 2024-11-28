#    app-arch/gzip/gzip-1.13.build.py
#    Thu Nov 28 00:04:29 UTC 2024

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
    return self.do(f"./configure --prefix=/usr")


def make(self):
    return self.do("make")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_binary(f"{self.p['_ub']}/gzip", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/gunzip", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/gzexe", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/uncompress", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/zcat", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/zcmp", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/zdiff", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/zegrep", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/zfgrep", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/zforce", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/zgrep", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/zless", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/zmore", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/znew", self.p['ub'])

    for file in os.listdir(self.p['_man1']):
        self.inst_manpage(file, self.p['man1'])
