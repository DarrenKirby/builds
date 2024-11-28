#    dev-lib/libyaml/libyaml-0.2.5.build.py
#    Wed Nov 27 04:50:09 UTC 2024

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


# tarball name does not match package name
def install_source_posthook(self):
    os.rename(f"yaml-{self.version}", f"libyaml-{self.version}")


def configure(self):
    return self.do("./configure --prefix=/usr --disable-static")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_header(self.p['_ui'] + "/yaml.h", self.p['ui'])

    self.inst_library(self.p['_ul'] + "/libyaml-0.so.2.0.9", self.p['ul'])
    self.inst_symlink(self.p['ul'] + "/libyaml-0.so.2.0.9", self.p['ul'] + "/libyaml-0.so.2")
    self.inst_symlink(self.p['ul'] + "/libyaml-0.so.2.0.9", self.p['ul'] + "/libyaml-0.so")

    self.inst_file(self.p['_ul'] + "/pkgconfig/yaml-0.1.pc", self.p['ul'] + "/pkgconfig/")
