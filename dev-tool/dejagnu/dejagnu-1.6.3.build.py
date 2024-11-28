#    dev-tool/dejagnu/dejagnu-1.6.3.build.py
#    Wed Nov 27 02:33:45 UTC 2024

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

depend = "dev-lang/expect"


def configure(self):
    os.mkdir("build")
    os.chdir("build/")
    return self.do("../configure --prefix=/usr")


def make(self):
    self.do("makeinfo --html --no-split -o doc/dejagnu.html ../doc/dejagnu.texi")
    return self.do("makeinfo --plaintext -o doc/dejagnu.txt  ../doc/dejagnu.texi")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_script(f"{self.p['_ub']}/dejagnu", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/runtest", self.p['ub'])

    self.inst_header(f"{self.p['_ui']}/dejagnu.h", self.p['ui'])

    self.inst_directory(self.p['_ush'] + f"/dejagnu/", self.p['ush'] + "/dejagnu/")

    self.inst_manpage(self.p['_man1'] + "/dejagnu-help.1", self.p['man1'])
    self.inst_manpage(self.p['_man1'] + "/dejagnu-report-card.1", self.p['man1'])
    self.inst_manpage(self.p['_man1'] + "/dejagnu.1", self.p['man1'])
    self.inst_manpage(self.p['_man1'] + "/runtest.1", self.p['man1'])
