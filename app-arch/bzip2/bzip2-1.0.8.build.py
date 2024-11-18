#    app-arch/bzip2/bzip2-1.0.8.build.py
#    Tue Nov  5 23:04:26 UTC 2024

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


def make(self):
    # Build shared lib, and use Makefile which links binaries against it
    exit1 = os.system("make -f Makefile-libbz2_so")
    exit2 = os.system("make clean")
    if (exit1 != 0) and (exit2 != 0):
        return 1
    return os.system("make")


def make_install(self):
    return os.system(f"make PREFIX={self.seg_dir}/usr install")


def install(self):
    self.inst_library("libbz2.so.1.0.8", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libbz2.so.1.0.8", f"{self.p['ul']}/libbz2.so")
    self.inst_symlink(f"{self.p['ul']}/libbz2.so.1.0.8", f"{self.p['ul']}/libbz2.so.1.0")

    self.inst_header(f"{self.p['_ui']}/bzlib.h", self.p['ui'])

    os.rename("bzip2-shared", f"{self.p['_ub']}/bzip2")
    self.inst_binary(f"{self.p['_ub']}/bzip2", f"{self.p['ub']}")
    self.inst_symlink(f"{self.p['ub']}/bzip2", f"{self.p['ub']}/bzat")
    self.inst_symlink(f"{self.p['ub']}/bzip2", f"{self.p['ub']}/bunzip2")

    self.inst_script(f"{self.p['_ub']}/bzdiff", f"{self.p['ub']}")
    self.inst_script(f"{self.p['_ub']}/bzgrep", f"{self.p['ub']}")
    self.inst_script(f"{self.p['_ub']}/bzmore", f"{self.p['ub']}")
    self.inst_binary(f"{self.p['_ub']}/bzip2recover", f"{self.p['ub']}")

    self.inst_symlink(f"{self.p['ub']}/bzdiff", f"{self.p['ub']}/bzcmp")
    self.inst_symlink(f"{self.p['ub']}/bzgrep", f"{self.p['ub']}/bzegrep")
    self.inst_symlink(f"{self.p['ub']}/bzgrep", f"{self.p['ub']}/bzfgrep")
    self.inst_symlink(f"{self.p['ub']}/bzmore", f"{self.p['ub']}/bzless")

    self.inst_manpage(f"{self.p['_man1']}/bzcmp.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/bzdiff.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/bzegrep.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/bzfgrep.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/bzgrep.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/bzip2.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/bzless.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/bzmore.1", self.p['man1'])
