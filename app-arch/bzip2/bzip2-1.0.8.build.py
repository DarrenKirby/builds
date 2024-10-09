#    app-arch/bzip2/bzip2-1.0.8.build.py
#    Tue Oct  8 18:43:05 UTC 2024

#    Copyright:: (c) 2024 Darren Kirby
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
    # Ensure symbolic links are relative
    exit1 = os.system("sed -i 's@\(ln -s -f \)$(PREFIX)/bin/@\1@' Makefile")
    # Fix manpage installation PATH
    exit2 = os.system('sed -i "s@(PREFIX)/man@(PREFIX/share/man@g)" Makefile')
    if (exit1 == 0) and (exit2 == 0):
        return 0
    return 1

def make(self):
    # Build shared lib, and use Makefile which links binaries against it
    exit1 = os.system("make -f Makefile-libbz2_so")
    exit2 = os.system("make clean")
    if (exit1 != 0) and (exit2 != 0):
        return 1
    return os.system("make")

def make_install(self):
    return os.system(f"make PREFIX={self.seg_dir} install")

def install(self):
    cf.do_lib("libbz2.so.1.0.8", cf.paths['ul'])
    cf.do_sym(f"{cf.paths['ul']}/libbz2.so.1.0.8", f"{cf.paths['ul']}/libbz2.so")
    cf.do_sym(f"{cf.paths['ul']}/libbz2.so.1.0.8", f"{cf.paths['ul']}/libbz2.so.1.0")

    cf.do_hdr(f"{self.seg_dir}/include/bzlib.h", cf.paths['ui'])

    cf.do_bin("bzip2-shared", f"{cf.paths['ub']}/bzip2")
    cf.do_sym(f"{cf.paths['ub']}/bzip2", f"{cr.paths['ub']}/bzat")
    cf.do_sym(f"{cf.paths['ub']}/bzip2", f"{cr.paths['ub']}/bunzip2")

    cf.do_bin(f"{self.seg_dir}/bin/bzdiff", f"{cf.paths['ub']}")
    cf.do_bin(f"{self.seg_dir}/bin/bzgrep", f"{cf.paths['ub']}")
    cf.do_bin(f"{self.seg_dir}/bin/bzmore", f"{cf.paths['ub']}")

    cf.do_sym(f"{cf.paths['ub']}/bzdiff", f"{cf.paths['ub']}/bzcmp")
    cf.do_sym(f"{cf.paths['ub']}/bzgrep", f"{cf.paths['ub']}/bzegrep")
    cf.do_sym(f"{cf.paths['ub']}/bzgrep", f"{cf.paths['ub']}/bzfgrep")
    cf.do_sym(f"{cf.paths['ub']}/bzmore", f"{cf.paths['ub']}/bzless")

    cf.do_man(f"{self.seg_dir}/share/man/man1/bzcmp.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/bzdiff.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/bzegrep.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/bzfgrep.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/bzgrep.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/bzip2.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/bzless.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/bzmore.1", cf.paths['man1'])

"""
/usr/lib/libbz2.so.1.0.8
/usr/lib/libbz2.so.1.0
/usr/lib/libbz2.so
/usr/include/bzlib.h
/usr/bin/bzip2
/usr/bin/bzcat
/usr/bin/bunzip2
/usr/bin/bzdiff
/usr/bin/bzgrep
/usr/bin/bzegrep
/usr/bin/bzfgrep
/usr/bin/bzmore
/usr/bin/bzless
/usr/bin/bzcmp
/usr/share/man/man1/bzcmp.1.bz2
/usr/share/man/man1/bzdiff.1.bz2
/usr/share/man/man1/bzgrep.1.bz2
/usr/share/man/man1/bzegrep.1.bz2
/usr/share/man/man1/bzfgrep.1.bz2
/usr/share/man/man1/bzip2.1.bz2
/usr/share/man/man1/bzmore.1.bz2
/usr/share/man/man1/bzless.1.bz2
"""
