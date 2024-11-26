#    dev-lib/libtasn1/libtasn1-4.19.0.build.py
#    Tue Nov 26 21:45:31 UTC 2024

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


def configure(self):
    return os.system(".configure --prefix=/usr --disable-static")


def make(self):
    return os.system(f"make  {cf.config['makeopts']}")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} install")


def install(self):
    pass
    #self.inst_binary(f"{self.p['_ub']}/psl", self.p['ub'])
    #self.inst_script(f"{self.p['_ub']}/psl-make-dafsa", self.p['ub'])

    #self.inst_header(f"{self.p['_ui']}/libpsl.h", self.p['ui'])

    #self.inst_library(f"{self.p['_ul']}/libpsl.so.5.3.5", self.p['ul'])
    #self.inst_symlink(f"{self.p['ul']}/libpsl.so.5.3.5", f"{self.p['ul']}/libpsl.so.5")
    #self.inst_symlink(f"{self.p['ul']}/libpsl.so.5", f"{self.p['ul']}/libpsl.so")

    #self.inst_file(f"{self.p['_ul']}/pkgconfig/libpsl.pc", f"{self.p['ul']}/pkgconfig/")

    #self.inst_manpage(f"{self.p['_man1']}/psl.1", self.p['man1'])
    #self.inst_manpage(f"{self.p['_man1']}/psl-make-dafsa.1", self.p['man1'])
