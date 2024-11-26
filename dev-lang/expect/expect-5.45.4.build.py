#    dev-lang/expect/expect-5.45.4.build.py
#    Sat Nov 23 03:17:49 UTC 2024

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

depend = "dev-lang/tcl"


def fetch_prehook(self):
    patchname = "expect-5.45.4-gcc14-1.patch"
    cf.bold(f"Downloading {patchname}...")
    cf.download(f"https://www.linuxfromscratch.org/patches/lfs/12.2/{patchname}",
                f"{cf.config['builds_root']}/distfiles/{patchname}")
    cf.bold("...done.")


def install_source_posthook(self):
    # non-standard source tree name
    cf.bold(f"Renaming expect{self.version} to {self.package_dir}")
    os.rename(f"expect{self.version}", self.package_dir)

    os.chdir(self.package_dir)
    patchname = "expect-5.45.4-gcc14-1.patch"
    os.system(f"patch -Np1 -i {cf.config['builds_root']}/distfiles/{patchname}")
    os.chdir(self.work_dir)


def configure(self):
    return os.system("./configure --prefix=/usr "
                     "--with-tcl=/usr/lib64 "
                     "--enable-shared "
                     "--disable-rpath "
                     "--mandir=/usr/share/man "
                     "--with-tclinclude=/usr/include ")


def make(self):
    return os.system(f"make {cf.config['makeopts']}")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} install")


def install(self):
    for file in os.listdir(self.p['_ub']):
        if file in ["expect"]:
            self.inst_binary(f"{self.p['_ub']}/{file}", self.p['ub'])
        else:
            self.inst_script(f"{self.p['_ub']}/{file}", self.p['ub'])

    for header in os.listdir(self.p['_ui']):
        self.inst_header(f"{self.p['_ui']}/{header}", self.p['ui'])

    self.inst_directory(self.p['_ul'] + f"/expect{self.version}/", self.p['_ul'] + f"/expect{self.version}/")

    for manpage in os.listdir(self.p['_man1']):
        self.inst_manpage(f"{self.p['_man1']}/{manpage}", self.p['man1'])

    self.inst_manpage(self.p['_man3'] + "/libexpect.3", self.p['man3'])
