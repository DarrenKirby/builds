#    dev-lang/ruby/ruby-3.3.6.build.py
#    Wed Nov 27 05:07:28 UTC 2024

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

depend = "dev-lib/libyaml"


def configure(self):
    return self.do("./configure --prefix=/usr "
                   "--disable-static "
                   "--disable-rpath "
                   "--enable-shared "
                   "--without-valgrind "
                   "--without-baseruby "
                   "ac_cv_func_qsort_r=no")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    for file in os.listdir(self.p['_ub']):
        if file in ["ruby"]:
            self.inst_binary(f"{self.p['_ub']}/{file}", self.p['ub'])
        else:
            self.inst_script(f"{self.p['_ub']}/{file}", self.p['ub'])

    self.inst_directory(f"{self.p['_ui']}/ruby-3.3.0", f"{self.p['ui']}/ruby-3.3.0")

    self.inst_library(self.p['_ul'] + "/libruby.so.3.3.6", self.p['ul'])
    self.inst_symlink(self.p['ul'] + "/libruby.so.3.3.6", self.p['ul'] + "/libruby.so.3.3")
    self.inst_symlink(self.p['ul'] + "/libruby.so.3.3.6", self.p['ul'] + "/libruby.so")

    self.inst_file(self.p['_ul'] + "/pkgconfig/ruby-3.3.pc", self.p['ul'] + "/pkgconfig/")

    self.inst_directory(f"{self.p['_ul']}/ruby", f"{self.p['ul']}/ruby")

    self.inst_directory(f"{self.p['_ush']}/ri", f"{self.p['ush']}/ri")

    self.inst_manpage(f"{self.p['_man1']}/erb.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/irb.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/ri.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/ruby.1", self.p['man1'])
