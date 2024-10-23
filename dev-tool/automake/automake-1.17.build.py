#    dev-tool/automake/automake-1.17.build.py
#    Wed Oct 23 01:40:25 UTC 2024

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
    return os.system(f"./configure --prefix={self.seg_dir}")


def make(self):
    return os.system("make")


def make_install(self):
    return os.system("make install")


def install(self):
    cf.do_scr(f"{self.seg_dir}/bin/aclocal", cf.paths['ub'])
    cf.do_scr(f"{self.seg_dir}/bin/aclocal-1.17", cf.paths['ub'])
    cf.do_scr(f"{self.seg_dir}/bin/automake", cf.paths['ub'])
    cf.do_scr(f"{self.seg_dir}/bin/automake-1.17", cf.paths['ub'])

    cf.do_dir(f"{self.seg_dir}/share/aclocal/", f"{cf.paths['ush']}/aclocal/")
    cf.do_dir(f"{self.seg_dir}/share/aclocal-1.17/", f"{cf.paths['ush']}/aclocal-1.17/")
    cf.do_dir(f"{self.seg_dir}/share/automake-1.17/", f"{cf.paths['ush']}/automake-1.17")

    cf.do_man(f"{self.seg_dir}/share/man/man1/aclocal-1.17.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/aclocal.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/automake-1.17.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/automake.1", cf.paths['man1'])


"""
/usr/bin/aclocal
/usr/bin/aclocal-1.17
/usr/bin/automake
/usr/bin/automake-1.17
/usr/share/aclocal/
/usr/share/aclocal/README
/usr/share/aclocal-1.17/
/usr/share/aclocal-1.17/amversion.m4
/usr/share/aclocal-1.17/ar-lib.m4
/usr/share/aclocal-1.17/as.m4
/usr/share/aclocal-1.17/auxdir.m4
/usr/share/aclocal-1.17/cond-if.m4
/usr/share/aclocal-1.17/cond.m4
/usr/share/aclocal-1.17/depend.m4
/usr/share/aclocal-1.17/depout.m4
/usr/share/aclocal-1.17/dmalloc.m4
/usr/share/aclocal-1.17/extra-recurs.m4
/usr/share/aclocal-1.17/gcj.m4
/usr/share/aclocal-1.17/init.m4
/usr/share/aclocal-1.17/install-sh.m4
/usr/share/aclocal-1.17/lead-dot.m4
/usr/share/aclocal-1.17/lex.m4
/usr/share/aclocal-1.17/lispdir.m4
/usr/share/aclocal-1.17/maintainer.m4
/usr/share/aclocal-1.17/make.m4
/usr/share/aclocal-1.17/missing.m4
/usr/share/aclocal-1.17/mkdirp.m4
/usr/share/aclocal-1.17/obsolete.m4
/usr/share/aclocal-1.17/options.m4
/usr/share/aclocal-1.17/prog-cc-c-o.m4
/usr/share/aclocal-1.17/python.m4
/usr/share/aclocal-1.17/rmf.m4
/usr/share/aclocal-1.17/runlog.m4
/usr/share/aclocal-1.17/sanity.m4
/usr/share/aclocal-1.17/silent.m4
/usr/share/aclocal-1.17/strip.m4
/usr/share/aclocal-1.17/substnot.m4
/usr/share/aclocal-1.17/tar.m4
/usr/share/aclocal-1.17/upc.m4
/usr/share/aclocal-1.17/vala.m4
/usr/share/aclocal-1.17/xargsn.m4
/usr/share/aclocal-1.17/internal/
/usr/share/aclocal-1.17/internal/ac-config-macro-dirs.m4
/usr/share/automake-1.17/
/usr/share/automake-1.17/COPYING
/usr/share/automake-1.17/INSTALL
/usr/share/automake-1.17/ar-lib
/usr/share/automake-1.17/compile
/usr/share/automake-1.17/config.guess
/usr/share/automake-1.17/config.sub
/usr/share/automake-1.17/depcomp
/usr/share/automake-1.17/install-sh
/usr/share/automake-1.17/mdate-sh
/usr/share/automake-1.17/missing
/usr/share/automake-1.17/mkinstalldirs
/usr/share/automake-1.17/py-compile
/usr/share/automake-1.17/tap-driver.sh
/usr/share/automake-1.17/test-driver
/usr/share/automake-1.17/texinfo.tex
/usr/share/automake-1.17/ylwrap
/usr/share/automake-1.17/am/
/usr/share/automake-1.17/am/check.am
/usr/share/automake-1.17/am/check2.am
/usr/share/automake-1.17/am/clean-hdr.am
/usr/share/automake-1.17/am/clean.am
/usr/share/automake-1.17/am/compile.am
/usr/share/automake-1.17/am/configure.am
/usr/share/automake-1.17/am/data.am
/usr/share/automake-1.17/am/dejagnu.am
/usr/share/automake-1.17/am/depend.am
/usr/share/automake-1.17/am/depend2.am
/usr/share/automake-1.17/am/distdir.am
/usr/share/automake-1.17/am/footer.am
/usr/share/automake-1.17/am/header-vars.am
/usr/share/automake-1.17/am/header.am
/usr/share/automake-1.17/am/inst-vars.am
/usr/share/automake-1.17/am/install.am
/usr/share/automake-1.17/am/java.am
/usr/share/automake-1.17/am/lang-compile.am
/usr/share/automake-1.17/am/lex.am
/usr/share/automake-1.17/am/library.am
/usr/share/automake-1.17/am/libs.am
/usr/share/automake-1.17/am/libtool.am
/usr/share/automake-1.17/am/lisp.am
/usr/share/automake-1.17/am/ltlib.am
/usr/share/automake-1.17/am/ltlibrary.am
/usr/share/automake-1.17/am/mans-vars.am
/usr/share/automake-1.17/am/mans.am
/usr/share/automake-1.17/am/program.am
/usr/share/automake-1.17/am/progs.am
/usr/share/automake-1.17/am/python.am
/usr/share/automake-1.17/am/remake-hdr.am
/usr/share/automake-1.17/am/scripts.am
/usr/share/automake-1.17/am/subdirs.am
/usr/share/automake-1.17/am/tags.am
/usr/share/automake-1.17/am/texi-vers.am
/usr/share/automake-1.17/am/texibuild.am
/usr/share/automake-1.17/am/texinfos.am
/usr/share/automake-1.17/am/vala.am
/usr/share/automake-1.17/am/yacc.am
/usr/share/man/man1/aclocal-1.17.1.bz2
/usr/share/man/man1/aclocal.1.bz2
/usr/share/man/man1/automake-1.17.1.bz2
/usr/share/man/man1/automake.1.bz2
"""
