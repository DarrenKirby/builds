#    dev-lang/python/python-3.12.8.build.py
#    Tue Dec 10 23:26:11 UTC 2024

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
    os.rename(f"Python-{self.version}", f"python-{self.version}")


def configure(self):
    return self.do("./configure --prefix=/usr "
                   "--enable-optimizations "
                   "--with-system-expat "
                   "--enable-shared ")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    v = self.version[0:5]
    self.inst_binary(self.p['_ub'] + f"/python{v}", self.p['ub'])
    self.inst_script(self.p['_ub'] + f"/python{v}-config", self.p['ub'])
    self.inst_script(self.p['_ub'] + f"/2to3-{v}", self.p['ub'])
    self.inst_script(self.p['_ub'] + f"/idle{v}", self.p['ub'])
    self.inst_script(self.p['_ub'] + f"/pydoc{v}", self.p['ub'])

    self.inst_symlink(self.p['ub'] + f"/python{v}", self.p['ub'] + "/python3")
    self.inst_symlink(self.p['ub'] + f"/python{v}-config", self.p['ub'] + "/python3-config")
    self.inst_symlink(self.p['ub'] + f"/2to3-{v}", self.p['ub'] + "/2to3")
    self.inst_symlink(self.p['ub'] + f"/idle{v}", self.p['ub'] + "/idle3")
    self.inst_symlink(self.p['ub'] + f"/pydoc{v}", self.p['ub'] + "/pydoc3")

    self.inst_directory(self.p['_ui'] + f"/python{v}/", self.p['ui'] + f"/python{v}/")

    self.inst_directory(self.p['_ul'] + f"/python{v}/", self.p['ul'] + f"/python{v}/")

    self.inst_library(self.p['_ul'] + f"/libpython{v}.so.1.0", self.p['ul'])
    self.inst_library(self.p['_ul'] + "/libpython3.so", self.p['ul'])
    self.inst_symlink(self.p['ul'] + f"/libpython{v}.so.1.0", self.p['ul'] + f"/libpython{v}.so")

    self.inst_file(self.p['_ul'] + f"/pkgconfig/python-{v}-embed.pc", self.p['ul'] + "/pkgconfig/")
    self.inst_file(self.p['_ul'] + f"/pkgconfig/python-{v}.pc", self.p['ul'] + "/pkgconfig/")
    self.inst_symlink(self.p['ul'] + f"/pkgconfig/python-{v}-embed.pc", self.p['ul'] + "/pkgconfig/python3-embed.pc")
    self.inst_symlink(self.p['ul'] + f"/pkgconfig/python-{v}.pc", self.p['ul'] + f"/pkgconfig/python-{v}.pc")

    self.inst_manpage(self.p['_man1'] + f"/python{v}.1", self.p['man1'])
    self.inst_symlink(f"{self.p['man1']}/python{v}.1.bz2", f"{self.p['man1']}/python3.1.bz2")
