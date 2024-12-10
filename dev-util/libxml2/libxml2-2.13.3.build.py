#    dev-util/libxml2/libxml2-2.13.3.build.py
#    Sun Dec  8 03:38:26 UTC 2024

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

depend = "dev-util/icu"


def fetch_prehook(self):
    patchname = "libxml2-2.13.3-upstream_fix-2.patch"
    cf.bold(f"Downloading {patchname}...")
    cf.download(f"https://www.linuxfromscratch.org/patches/blfs/12.2/{patchname}",
                f"{cf.config['builds_root']}/distfiles/{patchname}")
    cf.bold("...done.")


def install_source_posthook(self):
    os.chdir(self.package_dir)
    patchname = "libxml2-2.13.3-upstream_fix-2.patch"
    self.do(f"patch -Np1 -i {cf.config['builds_root']}/distfiles/{patchname}")
    os.chdir(self.work_dir)


def configure(self):
    confd = "/etc" if cf.config['user'] == 'root' else "/usr/etc"
    return self.do("./configure --prefix=/usr "
                   f"--sysconfdir={confd} "
                   "--disable-static "
                   "--with-history "
                   "--with-icu "
                   "PYTHON=/usr/bin/python3")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    import sys
    # Get, say "3.12"
    pyth_mm = ".".join(sys.version.split(".")[0:2])
    pp = f"/python{pyth_mm}/site-packages/"

    self.inst_script(self.p['_ub'] + "/xml2-config", self.p['ub'])
    self.inst_binary(self.p['_ub'] + "/xmlcatalog", self.p['ub'])
    self.inst_binary(self.p['_ub'] + "/xmllint", self.p['ub'])

    self.inst_directory(self.p['_ui'] + "/libxml2/", self.p['ui'] + "/libxml2/")

    self.inst_library(self.p['_ul'] + "/libxml2.so.2.13.3", self.p['ul'])
    self.inst_symlink(self.p['ul'] + "/libxml2.so.2.13.3", self.p['ul'] + "/libxml2.so")
    self.inst_symlink(self.p['ul'] + "/libxml2.so.2.13.3", self.p['ul'] + "/libxml2.so.2")

    self.inst_directory(self.p['_ul'] + "/cmake/libxml2/", self.p['ul'] + "/cmake/libxml2/")
    self.inst_file(self.p['_ul'] + "/pkgconfig/libxml-2.0.pc", self.p['ul'] + "/pkgconfig/")

    self.inst_script(self.p['_ul'] + pp + "drv_libxml2.py", self.p['ul'] + pp)
    self.inst_script(self.p['_ul'] + pp + "libxml2.py", self.p['ul'] + pp)
    self.inst_library(self.p['_ul'] + pp + "libxml2mod.la", self.p['ul'] + pp)
    self.inst_library(self.p['_ul'] + pp + "libxml2mod.so", self.p['ul'] + pp)

    self.inst_file(self.p['_ush'] + "/aclocal/libxml.m4", self.p['ush'] + "/aclocal/")
    for file in os.listdir(self.p['_man1']):
        self.inst_binary(f"{self.p['_man1']}/{file}", self.p['man1'])
