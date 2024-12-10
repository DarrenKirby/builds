#    dev-util/icu/icu-75.1.build.py
#    Mon Dec  9 23:48:32 UTC 2024

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


def install_source_posthook(self):
    os.rename("icu", f"icu-{self.version}")


def configure(self):
    os.chdir("source")
    return self.do("./configure --prefix=/usr")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    for file in os.listdir(self.p['_ub']):
        if file in ["icu-config"]:
            self.inst_script(f"{self.p['_ub']}/{file}", self.p['ub'])
        else:
            self.inst_binary(f"{self.p['_ub']}/{file}", self.p['ub'])

    self.inst_directory(self.p['_ui'] + "/unicode/", self.p['ui'] + "/unicode/")

    self.inst_directory(self.p['_ul'] + "/icu/", self.p['ul'] + "/icu/")

    self.inst_library(self.p['_ul'] + "/libicudata.so.75.1", self.p['ul'])
    self.inst_symlink(self.p['ul'] + "/libicudata.so.75.1", self.p['ul'] + "/libicudata.so")
    self.inst_symlink(self.p['ul'] + "/libicudata.so.75.1", self.p['ul'] + "/libicudata.so.75")

    self.inst_library(self.p['_ul'] + "/libicui18n.so.75.1", self.p['ul'])
    self.inst_symlink(self.p['ul'] + "/libicui18n.so.75.1", self.p['ul'] + "/libicui18n.so")
    self.inst_symlink(self.p['ul'] + "/libicui18n.so.75.1", self.p['ul'] + "/libicui18n.so.75")

    self.inst_library(self.p['_ul'] + "/libicuio.so.75.1", self.p['ul'])
    self.inst_symlink(self.p['ul'] + "/libicuio.so.75.1", self.p['ul'] + "/libicuio.so")
    self.inst_symlink(self.p['ul'] + "/libicuio.so.75.1", self.p['ul'] + "/libicuio.so.75")

    self.inst_library(self.p['_ul'] + "/libicutest.so.75.1", self.p['ul'])
    self.inst_symlink(self.p['ul'] + "/libicutest.so.75.1", self.p['ul'] + "/libicutest.so")
    self.inst_symlink(self.p['ul'] + "/libicutest.so.75.1", self.p['ul'] + "/libicutest.so.75")

    self.inst_library(self.p['_ul'] + "/libicutu.so.75.1", self.p['ul'])
    self.inst_symlink(self.p['ul'] + "/libicutu.so.75.1", self.p['ul'] + "/libicutu.so")
    self.inst_symlink(self.p['ul'] + "/libicutu.so.75.1", self.p['ul'] + "/libicutu.so.75")

    self.inst_library(self.p['_ul'] + "/libicuuc.so.75.1", self.p['ul'])
    self.inst_symlink(self.p['ul'] + "/libicuuc.so.75.1", self.p['ul'] + "/libicuuc.so")
    self.inst_symlink(self.p['ul'] + "/libicuuc.so.75.1", self.p['ul'] + "/libicuuc.so.75")

    self.inst_file(self.p['_ul'] + "/pkgconfig/icu-i18n.pc", self.p['ul'] + "/pkgconfig/")
    self.inst_file(self.p['_ul'] + "/pkgconfig/icu-io.pc", self.p['ul'] + "/pkgconfig/")
    self.inst_file(self.p['_ul'] + "/pkgconfig/icu-uc.pc", self.p['ul'] + "/pkgconfig/")

    for file in os.listdir(self.p['_us']):
        self.inst_binary(f"{self.p['_us']}/{file}", self.p['us'])

    self.inst_directory(self.p['_ush'] + "/icu/", self.p['ush'] + "/icu/")

    for file in os.listdir(self.p['_man1']):
        self.inst_manpage(f"{self.p['_man1']}/{file}", self.p['man1'])

    for file in os.listdir(self.p['_man8']):
        self.inst_manpage(f"{self.p['_man8']}/{file}", self.p['man8'])
