#    app-shell/bash/bash-5.2.37.build.py
#    Sat Oct 19 21:11:53 UTC 2024

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
    return os.system(f"./configure --prefix={self.seg_dir} "
                     f"--without-bash-malloc "
                     f"--with-installed-readline "
                     f"bash_cv_strtold_broken=no")


def make(self):
    return os.system("make")


def make_install(self):
    return os.system("make install")


def install(self):
    cf.do_bin(f"{self.seg_dir}/bin/bash", cf.paths['ub'])
    cf.do_scr(f"{self.seg_dir}/bin/bashbug", cf.paths['ub'])

    # headers
    cf.do_dir(f"{self.seg_dir}/include/bash/", f"{cf.paths['ui']}/bash/")
    # builtins
    cf.do_dir(f"{self.seg_dir}/lib/bash/", f"{cf.paths['ul']}/bash/")

    cf.do_man(f"{self.seg_dir}/share/man/man1/bash.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/bashbug.1", cf.paths['man1'])


def cleanup_posthook(self):
    cf.yellow("Make /bin/sh link to /usr/bin/bash ? (y/n)")
    if input() not in ['n', 'N', 'No', 'no']:
        cf.do_sym("/usr/bin/bash", "/bin/sh")
    cf.bold("Run...")
    print("\texec /usr/bin/bash --login")
    cf.bold("...to load new bash shell immediatly")


"""
/usr/bin/bash
/usr/bin/bashbug
/usr/include/bash/
/usr/include/bash/alias.h
/usr/include/bash/array.h
/usr/include/bash/arrayfunc.h
/usr/include/bash/assoc.h
/usr/include/bash/bashansi.h
/usr/include/bash/bashintl.h
/usr/include/bash/bashjmp.h
/usr/include/bash/bashtypes.h
/usr/include/bash/builtins.h
/usr/include/bash/command.h
/usr/include/bash/config-bot.h
/usr/include/bash/config-top.h
/usr/include/bash/config.h
/usr/include/bash/conftypes.h
/usr/include/bash/dispose_cmd.h
/usr/include/bash/error.h
/usr/include/bash/execute_cmd.h
/usr/include/bash/externs.h
/usr/include/bash/general.h
/usr/include/bash/hashlib.h
/usr/include/bash/jobs.h
/usr/include/bash/make_cmd.h
/usr/include/bash/pathnames.h
/usr/include/bash/quit.h
/usr/include/bash/shell.h
/usr/include/bash/sig.h
/usr/include/bash/siglist.h
/usr/include/bash/signames.h
/usr/include/bash/subst.h
/usr/include/bash/syntax.h
/usr/include/bash/unwind_prot.h
/usr/include/bash/variables.h
/usr/include/bash/version.h
/usr/include/bash/xmalloc.h
/usr/include/bash/y.tab.h
/usr/include/bash/builtins/
/usr/include/bash/builtins/bashgetopt.h
/usr/include/bash/builtins/builtext.h
/usr/include/bash/builtins/common.h
/usr/include/bash/builtins/getopt.h
/usr/include/bash/include/
/usr/include/bash/include/ansi_stdlib.h
/usr/include/bash/include/chartypes.h
/usr/include/bash/include/filecntl.h
/usr/include/bash/include/gettext.h
/usr/include/bash/include/maxpath.h
/usr/include/bash/include/memalloc.h
/usr/include/bash/include/ocache.h
/usr/include/bash/include/posixdir.h
/usr/include/bash/include/posixjmp.h
/usr/include/bash/include/posixstat.h
/usr/include/bash/include/posixtime.h
/usr/include/bash/include/posixwait.h
/usr/include/bash/include/shmbchar.h
/usr/include/bash/include/shmbutil.h
/usr/include/bash/include/shtty.h
/usr/include/bash/include/stat-time.h
/usr/include/bash/include/stdc.h
/usr/include/bash/include/systimes.h
/usr/include/bash/include/typemax.h
/usr/include/bash/include/unionwait.h
/usr/lib/bash/
/usr/lib/bash/Makefile.inc
/usr/lib/bash/Makefile.sample
/usr/lib/bash/accept
/usr/lib/bash/basename
/usr/lib/bash/csv
/usr/lib/bash/cut
/usr/lib/bash/dirname
/usr/lib/bash/dsv
/usr/lib/bash/fdflags
/usr/lib/bash/finfo
/usr/lib/bash/getconf
/usr/lib/bash/head
/usr/lib/bash/id
/usr/lib/bash/ln
/usr/lib/bash/loadables.h
/usr/lib/bash/logname
/usr/lib/bash/mkdir
/usr/lib/bash/mkfifo
/usr/lib/bash/mktemp
/usr/lib/bash/mypid
/usr/lib/bash/pathchk
/usr/lib/bash/print
/usr/lib/bash/printenv
/usr/lib/bash/push
/usr/lib/bash/realpath
/usr/lib/bash/rm
/usr/lib/bash/rmdir
/usr/lib/bash/seq
/usr/lib/bash/setpgid
/usr/lib/bash/sleep
/usr/lib/bash/stat
/usr/lib/bash/strftime
/usr/lib/bash/sync
/usr/lib/bash/tee
/usr/lib/bash/truefalse
/usr/lib/bash/tty
/usr/lib/bash/uname
/usr/lib/bash/unlink
/usr/lib/bash/whoami
/usr/share/man/man1/bash.1.bz2
/usr/share/man/man1/bashbug.1.bz2
"""
