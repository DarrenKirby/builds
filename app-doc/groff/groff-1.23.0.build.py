#    app-doc/groff/groff-1.23.0.build.py
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
    return self.do("./configure --prefix=/usr")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    for binary in os.listdir(self.p['_ub']):
        if binary in ["afmtodit", "chem", "eqn2graph", "gdiffmk", "glilypond", "gperl", "gpinyin", "grap2graph",
                      "grog", "gropdf", "mmroff", "neqn", "nroff", "pdfmom", "pdfroff", "pic2graph"]:
            self.inst_script(f"{self.p['_ub']}/{binary}", self.p['ub'])
        else:
            self.inst_binary(f"{self.p['_ub']}/{binary}", self.p['ub'])

    self.inst_directory(self.p['_ul'] + '/X11/', self.p['ul'] + '/X11/')
    self.inst_directory(self.p['_ul'] + '/groff/', self.p['ul'] + '/groff/')
    self.inst_directory(self.p['_ush'] + '/groff/', self.p['ush'] + '/groff/')

    # install manpages
    for file in os.listdir(self.p['_man1']):
        self.inst_manpage(f"{self.p['_man1']}/{file}", self.p['man1'])

    for file in os.listdir(self.p['_man5']):
        self.inst_manpage(f"{self.p['_man5']}/{file}", self.p['man5'])

    for file in os.listdir(self.p['_man7']):
        self.inst_manpage(f"{self.p['_man7']}/{file}", self.p['man7'])
