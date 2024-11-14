#    app-util/gawk/gawk-5.3.1.build.py
#    Thu Nov 14 19:59:55 UTC 2024

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
    cf.bold("Removing gawk extras from makefile...")
    try:
        os.system("sed -i 's/extras//' Makefile.in")
    except:
        cf.yellow("sed command failed: non fatal")
    return os.system("./configure --prefix=/usr")


def make(self):
    return os.system(f"make {cf.config['makeopts']}")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_binary(f"{self.p['_ub']}/gawk", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/gawk-5.3.1", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/gawkbug", self.p['ub'])
    # link awk -> gawk
    self.inst_symlink(f"{self.p['ub']}/gawk", f"{self.p['ub']}/awk")

    self.inst_header(f"{self.p['_ui']}/gawkapi.h", self.p['ui'])

    self.inst_directory(f"{self.p['_ul']}/gawk/", f"{self.p['ul']}/gawk/")

    self.inst_directory(f"{self.p['_ule']}/awk/", f"{self.p['ule']}/awk/")

    self.inst_manpage(f"{self.p['_man1']}/gawk.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/gawkbug.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/pm-gawk.1", self.p['man1'])
    # link  awk.1 -> gawk1.bz2
    self.inst_symlink(f"{self.p['man1']}/gawk.1.bz2", f"{self.p['man1']}/awk.1")

    for file in os.listdir(self.p['_man3']):
        self.inst_manpage(f"{self.p['_man3']}/{file}", self.p['man3'])
