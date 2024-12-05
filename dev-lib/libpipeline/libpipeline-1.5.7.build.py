#    dev-lib/libpipeline/libpipeline-1.5.7.build.py
#    Wed Dec  4 18:48:09 UTC 2024

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
    self.inst_header(self.p['_ui'] + "/pipeline.h", self.p['ui'])

    self.inst_file(self.p['_ul'] + "/pkgconfig/libpipeline.pc", self.p['ul'] + "/pkgconfig/")

    self.inst_library(f"{self.p['_ul']}/libpipeline.so.1.5.7", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libpipeline.so.1.5.7", f"{self.p['ul']}/libpipeline.so")
    self.inst_symlink(f"{self.p['ul']}/libpipeline.so.1.5.7", f"{self.p['ul']}/libpipeline.so.1")

    self.inst_manpage(f"{self.p['_man3']}/libpipeline.3", self.p['man3'])
    for manpage in os.listdir(self.p['_man3']):
        if manpage not in ["libpipeline.3.bz2"]:
            # Symlinks to compressed manpages must also have .bz2 extension, or man won't decompress
            # the page that is the link target
            self.inst_symlink(f"{self.p['man3']}/libpipeline.3.bz2", f"{self.p['man3']}/{manpage}.bz2")
