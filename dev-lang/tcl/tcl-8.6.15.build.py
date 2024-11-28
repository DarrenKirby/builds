#    dev-lang/tcl/tcl-8.6.15.build.py
#    Sat Nov 23 03:01:32 UTC 2024

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
    # non-standard source tree name
    cf.bold(f"Renaming tcl{self.version} to {self.package_dir}")
    os.rename(f"tcl{self.version}", self.package_dir)


def configure(self):
    print(os.getcwd())
    os.chdir("unix")
    return self.do("./configure --prefix=/usr "
                   "--mandir=/usr/share/man "
                   "--disable-rpath")


def make(self):
    print(os.getcwd())
    pwd = self.package_dir
    print(pwd)
    self.do(f"make {cf.config['makeopts']}")
    try:
        self.do(f'sed -e "s|{pwd}/unix|/usr/lib|" -e "s|{pwd}|/usr/include|" -i tclConfig.sh')
        self.do(f'sed -e "s|{pwd}/unix/pkgs/tdbc1.1.7|/usr/lib/tdbc1.1.7|" '
                f'-e "s|{pwd}/pkgs/tdbc1.1.7/generic|/usr/include|" '
                f'-e "s|{pwd}/pkgs/tdbc1.1.7/library|/usr/lib/tcl8.6|" '
                f'-e "s|{pwd}/pkgs/tdbc1.1.7|/usr/include|" '
                '-i pkgs/tdbc1.1.7/tdbcConfig.sh')
        self.do(f'sed -e "s|{pwd}/unix/pkgs/itcl4.2.4|/usr/lib/itcl4.2.4|" '
                f'-e "s|{pwd}/pkgs/itcl4.2.4/generic|/usr/include|" '
                f'-e "s|{pwd}/pkgs/itcl4.2.4|/usr/include|" '
                '-i pkgs/itcl4.2.4/itclConfig.sh')
        return 0
    except OSError:
        return 1


def make_install(self):
    try:
        self.do(f"make DESTDIR={self.seg_dir} install")
        self.do(f"make DESTDIR={self.seg_dir} install-private-headers")
        # Need to make this lib writable to strip
        os.chmod(self.p['_ul'] + "/libtcl8.6.so", 0o755)
        return 0
    except OSError:
        return 1


def install(self):
    self.inst_script(self.p['_ub'] + "/sqlite3_analyzer", self.p['ub'])
    self.inst_binary(self.p['_ub'] + "/tclsh8.6", self.p['ub'])
    self.inst_symlink(self.p['ub'] + "/tclsh8.6", self.p['ub'] + "/tclsh")

    for header in os.listdir(self.p['_ui']):
        self.inst_header(f"{self.p['_ui']}/{header}", self.p['ui'])

    self.inst_library(self.p['_ul'] + "/libtcl8.6.so", self.p['ul'])
    self.inst_library(self.p['_ul'] + "/libtclstub8.6.a", self.p['ul'])

    self.inst_script(self.p['_ul'] + "/tclConfig.sh", self.p['ul'])
    self.inst_script(self.p['_ul'] + "/tclooConfig.sh", self.p['ul'])

    for directory in ["itcl4.3.0", "sqlite3.45.3", "tcl8", "tcl8.6", "tdbc1.1.9", "tdbcmysql1.1.9", "tdbcodbc1.1.9",
                      "tdbcpostgres1.1.9", "thread2.8.10"]:
        self.inst_directory(f"{self.p['_ul']}/{directory}", f"{self.p['ul']}/{directory}")

    self.inst_file(self.p['_ul'] + "/pkgconfig/tcl.pc", self.p['ul'] + "/pkgconfig/")

    self.inst_manpage(self.p['_man1'] + "/tclsh.1", self.p['man1'])

    # Thread.3 collides with a manpage from Perl. Since the Perl page describes a
    # deprecated threading interface, I think the TCL page should have dibs on the
    # original name, but I change it here to be consistent with Linux from Scratch:
    # https://www.linuxfromscratch.org/lfs/view/stable/chapter08/tcl.html
    os.rename(self.p['_man3'] + "/Thread.3", self.p['_man3'] + "/Tcl_Thread.3")

    for manpage in os.listdir(self.p['_man3']):
        self.inst_manpage(f"{self.p['_man3']}/{manpage}", self.p['man3'], compress=False)

    # Make usr/share/man/mann if it doesn't already exist.
    os.makedirs(f"{self.p['ush']}/man/mann/", exist_ok=True)

    for manpage in os.listdir(self.p['_ush'] + "/man/mann"):
        self.inst_manpage(f"{self.p['_ush']}/man/mann/{manpage}", self.p['ush'] + "/man/mann/", compress=False)
