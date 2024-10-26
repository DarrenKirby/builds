#    app-util/gawk/gawk-5.3.1.build.py
#    Fri Oct 25 16:48:44 UTC 2024

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
    cf.bold("Removing gawk extras from makefile...")
    try:
        os.system("sed -i 's/extras//' Makefile.in")
    except:
        cf.yellow("sed command failed: non fatal")
    return os.system(f"./configure --prefix={self.seg_dir}")


def make(self):
    return os.system("make")


def make_install(self):
    return os.system("make install")


def install(self):
    cf.do_bin(f"{self.seg_dir}/bin/gawk", cf.paths['ub'])
    cf.do_bin(f"{self.seg_dir}/bin/gawk-5.3.1", cf.paths['ub'])
    cf.do_scr(f"{self.seg_dir}/bin/gawkbug", cf.paths['ub'])
    # link awk -> gawk
    cf.do_sym(f"{cf.paths['ub']}/gawk", f"{cf.paths['ub']}/awk")

    cf.do_hdr(f"{self.seg_dir}/include/gawkapi.h", cf.paths['ui'])

    cf.do_dir(f"{self.seg_dir}/lib/gawk/", f"{cf.paths['ul']}/gawk/")

    cf.do_dir(f"{self.seg_dir}/libexec/awk/", f"{cf.paths['ule']}/awk/")

    cf.do_man(f"{self.seg_dir}/share/man/man1/gawk.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/gawkbug.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/pm-gawk.1", cf.paths['man1'])
    # link  awk.1 -> gawk1.bz2
    cf.do_sym(f"{cf.paths['man1']}/gawk.1.bz2", f"{cf.paths['man1']}/awk.1")

    cf.do_man(f"{self.seg_dir}/share/man/man3/filefuncs.3am", cf.paths['man3'])
    cf.do_man(f"{self.seg_dir}/share/man/man3/fnmatch.3am", cf.paths['man3'])
    cf.do_man(f"{self.seg_dir}/share/man/man3/fork.3am", cf.paths['man3'])
    cf.do_man(f"{self.seg_dir}/share/man/man3/inplace.3am", cf.paths['man3'])
    cf.do_man(f"{self.seg_dir}/share/man/man3/ordchr.3am", cf.paths['man3'])
    cf.do_man(f"{self.seg_dir}/share/man/man3/readdir.3am", cf.paths['man3'])
    cf.do_man(f"{self.seg_dir}/share/man/man3/readfile.3am", cf.paths['man3'])
    cf.do_man(f"{self.seg_dir}/share/man/man3/revoutput.3am", cf.paths['man3'])
    cf.do_man(f"{self.seg_dir}/share/man/man3/revtwoway.3am", cf.paths['man3'])
    cf.do_man(f"{self.seg_dir}/share/man/man3/rwarray.3am", cf.paths['man3'])
    cf.do_man(f"{self.seg_dir}/share/man/man3/time.3am", cf.paths['man3'])


"""
/usr/bin/awk
/usr/bin/gawk
/usr/bin/gawk-5.3.1
/usr/bin/gawkbug
/usr/include/gawkapi.h
/usr/lib/gawk/
/usr/lib/gawk/filefuncs.so
/usr/lib/gawk/fnmatch.so
/usr/lib/gawk/fork.so
/usr/lib/gawk/inplace.so
/usr/lib/gawk/intdiv.so
/usr/lib/gawk/ordchr.so
/usr/lib/gawk/readdir.so
/usr/lib/gawk/readfile.so
/usr/lib/gawk/revoutput.so
/usr/lib/gawk/revtwoway.so
/usr/lib/gawk/rwarray.so
/usr/lib/gawk/time.so
/usr/libexec/awk/
/usr/libexec/awk/grcat
/usr/libexec/awk/pwcat
/usr/share/man/man1/gawk.1.bz2
/usr/share/man/man1/awk.1
/usr/share/man/man1/gawkbug.1.bz2
/usr/share/man/man1/pm-gawk.1.bz2
/usr/share/man/man3/filefuncs.3am.bz2
/usr/share/man/man3/fnmatch.3am.bz2
/usr/share/man/man3/fork.3am.bz2
/usr/share/man/man3/inplace.3am.bz2
/usr/share/man/man3/ordchr.3am.bz2
/usr/share/man/man3/readdir.3am.bz2
/usr/share/man/man3/readfile.3am.bz2
/usr/share/man/man3/revoutput.3am.bz2
/usr/share/man/man3/revtwoway.3am.bz2
/usr/share/man/man3/rwarray.3am.bz2
/usr/share/man/man3/time.3am.bz2
"""
