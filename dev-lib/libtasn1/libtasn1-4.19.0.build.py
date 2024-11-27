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
    return os.system("./configure --prefix=/usr --disable-static")


def make(self):
    return os.system(f"make  {cf.config['makeopts']}")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_binary(f"{self.p['_ub']}/asn1Coding", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/asn1Decoding", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/asn1Parser", self.p['ub'])

    self.inst_header(f"{self.p['_ui']}/libtasn1.h", self.p['ui'])

    self.inst_library(f"{self.p['_ul']}/libtasn1.so.6.6.3", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libtasn1.so.6.6.3", f"{self.p['ul']}/libtasn1.so.6")
    self.inst_symlink(f"{self.p['ul']}/libtasn1.so.6.6.3", f"{self.p['ul']}/libtasn1.so")

    self.inst_file(f"{self.p['_ul']}/pkgconfig/libtasn1.pc", f"{self.p['ul']}/pkgconfig/")

    self.inst_manpage(f"{self.p['_man1']}/asn1Coding.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/asn1Decoding.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/asn1Parser.1", self.p['man1'])

    for manpage in os.listdir(self.p['_man3']):
        self.inst_manpage(f"{self.p['_man3']}/{manpage}", self.p['man3'])
