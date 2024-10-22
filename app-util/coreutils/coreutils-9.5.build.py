#    app-util/coreutils/coreutils-9.5.build
#    Tue Oct 22 02:20:15 UTC 2024

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



def fetch_prehook(self):
    patchname = "coreutils-9.5-i18n-2.patch"
    cf.bold(f"Downloading {patchname}...")
    cf.download("https://www.linuxfromscratch.org/patches/lfs/12.2/coreutils-9.5-i18n-2.patch",
                f"{self.config['builds_root']}/distfiles/{patchname}")
    cf.bold("...done.")



def install_source_posthook(self):
    os.chdir(self.package_dir)
    patchname = "coreutils-9.5-i18n-2.patch"
    es = os.system(f"patch -Np1 -i {self.config['builds_root']}/distfiles/{patchname}")
    os.chdir(self.work_dir)
    return es


def configure(self):
    es1 = os.system("autoreconf -fiv")
    es2 = os.system(f"FORCE_UNSAFE_CONFIGURE=1 ./configure --prefix={self.seg_dir} --enable-no-install-program=kill,uptime")
    if es1 == 0 and es2 == 0:
        return 0
    return 12


def make(self):
    return os.system("make")


def make_install(self):
    return os.system("make install")


def install(self):
    # FHS says chroot should be in sbin
    cf.do_bin(f"{self.seg_dir}/bin/chroot", cf.paths['us'])
    os.remove(f"{self.seg_dir}/bin/chroot")

    os.rename(f"{self.seg_dir}/share/man/man1/chroot.1", f"{self.seg_dir}/share/man/man1/chroot.8")
    cf.do_man(f"{self.seg_dir}/share/man/man1/chroot.8", cf.paths['man8'])

    for app in glob.glob(f"{self.seg_dir}/bin/*"):
        cf.do_bin(f"{self.seg_dir}/bin/{app}", cf/paths['ub'])

    for manpage in glob.glob(f"{self.seg_dir}/share/man/man1/*.1"):
        cf.do_man(f"{self.seg_dir}/share/man/man1/{manpage}", cf.paths['man1'])

    os.mkdirs(f"{cf.paths['ul']}exec/coreutils/", mode=0o755)
    cf.do_lib(f"{self.seg_dir}/libexec/coreutils/libstdbuf.so", f"{cf.paths['ul']}exec/coreutils/")


"""
/usr/bin/[
/usr/bin/b2sum
/usr/bin/base32
/usr/bin/base64
/usr/bin/basename
/usr/bin/basenc
/usr/bin/cat
/usr/bin/chcon
/usr/bin/chgrp
/usr/bin/chmod
/usr/bin/chown
/usr/bin/cksum
/usr/bin/comm
/usr/bin/cp
/usr/bin/csplit
/usr/bin/cut
/usr/bin/date
/usr/bin/dd
/usr/bin/df
/usr/bin/dir
/usr/bin/dircolors
/usr/bin/dirname
/usr/bin/du
/usr/bin/echo
/usr/bin/env
/usr/bin/expand
/usr/bin/expr
/usr/bin/factor
/usr/bin/false
/usr/bin/fmt
/usr/bin/fold
/usr/bin/groups
/usr/bin/head
/usr/bin/hostid
/usr/bin/id
/usr/bin/install
/usr/bin/join
/usr/bin/link
/usr/bin/ln
/usr/bin/logname
/usr/bin/ls
/usr/bin/md5sum
/usr/bin/mkdir
/usr/bin/mkfifo
/usr/bin/mknod
/usr/bin/mktemp
/usr/bin/mv
/usr/bin/nice
/usr/bin/nl
/usr/bin/nohup
/usr/bin/nproc
/usr/bin/numfmt
/usr/bin/od
/usr/bin/paste
/usr/bin/pathchk
/usr/bin/pinky
/usr/bin/pr
/usr/bin/printenv
/usr/bin/printf
/usr/bin/ptx
/usr/bin/pwd
/usr/bin/readlink
/usr/bin/realpath
/usr/bin/rm
/usr/bin/rmdir
/usr/bin/runcon
/usr/bin/seq
/usr/bin/sha1sum
/usr/bin/sha224sum
/usr/bin/sha256sum
/usr/bin/sha384sum
/usr/bin/sha512sum
/usr/bin/shred
/usr/bin/shuf
/usr/bin/sleep
/usr/bin/sort
/usr/bin/split
/usr/bin/stat
/usr/bin/stdbuf
/usr/bin/stty
/usr/bin/sum
/usr/bin/sync
/usr/bin/tac
/usr/bin/tail
/usr/bin/tee
/usr/bin/test
/usr/bin/timeout
/usr/bin/touch
/usr/bin/tr
/usr/bin/true
/usr/bin/truncate
/usr/bin/tsort
/usr/bin/tty
/usr/bin/uname
/usr/bin/unexpand
/usr/bin/uniq
/usr/bin/unlink
/usr/bin/users
/usr/bin/vdir
/usr/bin/wc
/usr/bin/who
/usr/bin/whoami
/usr/bin/yes
/usr/libexec/coreutils/
/usr/libexec/coreutils/libstdbuf.so
/usr/sbin/chroot
/usr/share/man/man1/b2sum.1
/usr/share/man/man1/base32.1
/usr/share/man/man1/base64.1
/usr/share/man/man1/basename.1.bz2
/usr/share/man/man1/basenc.1.bz2
/usr/share/man/man1/cat.1.bz2
/usr/share/man/man1/chcon.1.bz2
/usr/share/man/man1/chgrp.1.bz2
/usr/share/man/man1/chmod.1.bz2
/usr/share/man/man1/chown.1.bz2
/usr/share/man/man1/cksum.1.bz2
/usr/share/man/man1/comm.1.bz2
/usr/share/man/man1/cp.1.bz2
/usr/share/man/man1/csplit.1.bz2
/usr/share/man/man1/cut.1.bz2
/usr/share/man/man1/date.1.bz2
/usr/share/man/man1/dd.1.bz2
/usr/share/man/man1/df.1.bz2
/usr/share/man/man1/dir.1.bz2
/usr/share/man/man1/dircolors.1.bz2
/usr/share/man/man1/dirname.1.bz2
/usr/share/man/man1/du.1.bz2
/usr/share/man/man1/echo.1.bz2
/usr/share/man/man1/env.1.bz2
/usr/share/man/man1/expand.1.bz2
/usr/share/man/man1/expr.1.bz2
/usr/share/man/man1/factor.1.bz2
/usr/share/man/man1/false.1.bz2
/usr/share/man/man1/fmt.1.bz2
/usr/share/man/man1/fold.1.bz2
/usr/share/man/man1/groups.1.bz2
/usr/share/man/man1/head.1.bz2
/usr/share/man/man1/hostid.1.bz2
/usr/share/man/man1/id.1.bz2
/usr/share/man/man1/install.1.bz2
/usr/share/man/man1/join.1.bz2
/usr/share/man/man1/link.1.bz2
/usr/share/man/man1/ln.1.bz2
/usr/share/man/man1/logname.1.bz2
/usr/share/man/man1/ls.1.bz2
/usr/share/man/man1/md5sum.1.bz2
/usr/share/man/man1/mkdir.1.bz2
/usr/share/man/man1/mkfifo.1.bz2
/usr/share/man/man1/mknod.1.bz2
/usr/share/man/man1/mktemp.1.bz2
/usr/share/man/man1/mv.1.bz2
/usr/share/man/man1/nice.1.bz2
/usr/share/man/man1/nl.1.bz2
/usr/share/man/man1/nohup.1.bz2
/usr/share/man/man1/nproc.1.bz2
/usr/share/man/man1/numfmt.1.bz2
/usr/share/man/man1/od.1.bz2
/usr/share/man/man1/paste.1.bz2
/usr/share/man/man1/pathchk.1.bz2
/usr/share/man/man1/pinky.1.bz2
/usr/share/man/man1/pr.1.bz2
/usr/share/man/man1/printenv.1.bz2
/usr/share/man/man1/printf.1.bz2
/usr/share/man/man1/ptx.1.bz2
/usr/share/man/man1/pwd.1.bz2
/usr/share/man/man1/readlink.1.bz2
/usr/share/man/man1/realpath.1.bz2
/usr/share/man/man1/rm.1.bz2
/usr/share/man/man1/rmdir.1.bz2
/usr/share/man/man1/runcon.1.bz2
/usr/share/man/man1/seq.1.bz2
/usr/share/man/man1/sha1sum.1.bz2
/usr/share/man/man1/sha224sum.1.bz2
/usr/share/man/man1/sha256sum.1.bz2
/usr/share/man/man1/sha384sum.1.bz2
/usr/share/man/man1/sha512sum.1.bz2
/usr/share/man/man1/shred.1.bz2
/usr/share/man/man1/shuf.1.bz2
/usr/share/man/man1/sleep.1.bz2
/usr/share/man/man1/sort.1.bz2
/usr/share/man/man1/split.1.bz2
/usr/share/man/man1/stat.1.bz2
/usr/share/man/man1/stdbuf.1.bz2
/usr/share/man/man1/stty.1.bz2
/usr/share/man/man1/sum.1.bz2
/usr/share/man/man1/sync.1.bz2
/usr/share/man/man1/tac.1.bz2
/usr/share/man/man1/tail.1.bz2
/usr/share/man/man1/tee.1.bz2
/usr/share/man/man1/test.1.bz2
/usr/share/man/man1/timeout.1.bz2
/usr/share/man/man1/touch.1.bz2
/usr/share/man/man1/tr.1.bz2
/usr/share/man/man1/true.1.bz2
/usr/share/man/man1/truncate.1.bz2
/usr/share/man/man1/tsort.1.bz2
/usr/share/man/man1/tty.1.bz2
/usr/share/man/man1/uname.1.bz2
/usr/share/man/man1/unexpand.1.bz2
/usr/share/man/man1/uniq.1.bz2
/usr/share/man/man1/unlink.1.bz2
/usr/share/man/man1/users.1.bz2
/usr/share/man/man1/vdir.1.bz2
/usr/share/man/man1/wc.1.bz2
/usr/share/man/man1/who.1.bz2
/usr/share/man/man1/whoami.1.bz2
/usr/share/man/man1/yes.1.bz2
/usr/share/man/man8/chroot.8.bz2
"""
