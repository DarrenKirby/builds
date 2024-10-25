#    app-util/e2fsprogs/e2fsprogs-1.47.1.build.py
#    Thu Oct 24 23:51:59 UTC 2024

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
    # The E2fsprogs documentation recommends that the package
    # be built in a subdirectory of the source tree
    os.mkdir("build")
    os.chdir("build")

    return os.system(f"../configure --prefix={self.seg_dir} "
                    f"--enable-elf-shlibs "
                    f"--disable-libblkid "
                    f"--disable-libuuid "
                    f"--disable-uuidd "
                    f"--disable-fsck")


def make(self):
    return os.system("make")


def make_install(self):
    return os.system("make install")


def install(self):
    cf.do_bin(f"{self.seg_dir}/bin/chattr", cf.paths['ub'])
    cf.do_bin(f"{self.seg_dir}/bin/fuse2fs", cf.paths['ub'])
    cf.do_bin(f"{self.seg_dir}/bin/lsattr", cf.paths['ub'])

    cf.do_bin(f"{self.seg_dir}/sbin/badblocks", cf.paths['us'])
    cf.do_bin(f"{self.seg_dir}/sbin/debugfs", cf.paths['us'])
    cf.do_bin(f"{self.seg_dir}/sbin/dumpe2fs", cf.paths['us'])
    cf.do_bin(f"{self.seg_dir}/sbin/e2freefrag", cf.paths['us'])
    cf.do_bin(f"{self.seg_dir}/sbin/e2fsck", cf.paths['us'])
    cf.do_bin(f"{self.seg_dir}/sbin/e2image", cf.paths['us'])
    cf.do_bin(f"{self.seg_dir}/sbin/e2label", cf.paths['us'])
    cf.do_bin(f"{self.seg_dir}/sbin/e2mmpstatus", cf.paths['us'])
    cf.do_bin(f"{self.seg_dir}/sbin/e2undo", cf.paths['us'])
    cf.do_bin(f"{self.seg_dir}/sbin/e4crypt", cf.paths['us'])
    cf.do_bin(f"{self.seg_dir}/sbin/e4defrag", cf.paths['us'])
    cf.do_bin(f"{self.seg_dir}/sbin/filefrag", cf.paths['us'])
    cf.do_bin(f"{self.seg_dir}/sbin/fsck.ext2", cf.paths['us'])
    cf.do_bin(f"{self.seg_dir}/sbin/fsck.ext3", cf.paths['us'])
    cf.do_bin(f"{self.seg_dir}/sbin/fsck.ext4", cf.paths['us'])
    cf.do_bin(f"{self.seg_dir}/sbin/logsave", cf.paths['us'])
    cf.do_bin(f"{self.seg_dir}/sbin/mke2fs", cf.paths['us'])
    cf.do_bin(f"{self.seg_dir}/sbin/mkfs.ext2", cf.paths['us'])
    cf.do_bin(f"{self.seg_dir}/sbin/mkfs.ext3", cf.paths['us'])
    cf.do_bin(f"{self.seg_dir}/sbin/mkfs.ext4", cf.paths['us'])
    cf.do_bin(f"{self.seg_dir}/sbin/mklost+found", cf.paths['us'])
    cf.do_bin(f"{self.seg_dir}/sbin/resize2fs", cf.paths['us'])
    cf.do_bin(f"{self.seg_dir}/sbin/tune2fs", cf.paths['us'])

    cf.do_lib(f"{self.seg_dir}/lib/e2initrd_helper", cf.paths['ul'])

    cf.do_con(f"{self.seg_dir}/etc/mke2fs.conf", cf.paths['e'])

    cf.do_man(f"{self.seg_dir}/share/man/man1/chattr.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/fuse2fs.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/lsattr.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man5/e2fsck.conf.5", cf.paths['man5'])
    cf.do_man(f"{self.seg_dir}/share/man/man5/ext2.5", cf.paths['man5'])
    cf.do_man(f"{self.seg_dir}/share/man/man5/ext3.5", cf.paths['man5'])
    cf.do_man(f"{self.seg_dir}/share/man/man5/ext4.5", cf.paths['man5'])
    cf.do_man(f"{self.seg_dir}/share/man/man5/mke2fs.conf.5", cf.paths['man5'])
    cf.do_man(f"{self.seg_dir}/share/man/man8/badblocks.8", cf.paths['man8'])
    cf.do_man(f"{self.seg_dir}/share/man/man8/debugfs.8", cf.paths['man8'])
    cf.do_man(f"{self.seg_dir}/share/man/man8/dumpe2fs.8", cf.paths['man8'])
    cf.do_man(f"{self.seg_dir}/share/man/man8/e2freefrag.8", cf.paths['man8'])
    cf.do_man(f"{self.seg_dir}/share/man/man8/e2fsck.8", cf.paths['man8'])
    cf.do_man(f"{self.seg_dir}/share/man/man8/e2image.8", cf.paths['man8'])
    cf.do_man(f"{self.seg_dir}/share/man/man8/e2label.8", cf.paths['man8'])
    cf.do_man(f"{self.seg_dir}/share/man/man8/e2mmpstatus.8", cf.paths['man8'])
    cf.do_man(f"{self.seg_dir}/share/man/man8/e2undo.8", cf.paths['man8'])
    cf.do_man(f"{self.seg_dir}/share/man/man8/e4crypt.8", cf.paths['man8'])
    cf.do_man(f"{self.seg_dir}/share/man/man8/e4defrag.8", cf.paths['man8'])
    cf.do_man(f"{self.seg_dir}/share/man/man8/filefrag.8", cf.paths['man8'])
    cf.do_man(f"{self.seg_dir}/share/man/man8/fsck.ext2.8", cf.paths['man8'])
    cf.do_man(f"{self.seg_dir}/share/man/man8/fsck.ext3.8", cf.paths['man8'])
    cf.do_man(f"{self.seg_dir}/share/man/man8/fsck.ext4.8", cf.paths['man8'])
    cf.do_man(f"{self.seg_dir}/share/man/man8/logsave.8", cf.paths['man8'])
    cf.do_man(f"{self.seg_dir}/share/man/man8/mke2fs.8", cf.paths['man8'])
    cf.do_man(f"{self.seg_dir}/share/man/man8/mkfs.ext2.8", cf.paths['man8'])
    cf.do_man(f"{self.seg_dir}/share/man/man8/mkfs.ext3.8", cf.paths['man8'])
    cf.do_man(f"{self.seg_dir}/share/man/man8/mkfs.ext4.8", cf.paths['man8'])
    cf.do_man(f"{self.seg_dir}/share/man/man8/mklost+found.8", cf.paths['man8'])
    cf.do_man(f"{self.seg_dir}/share/man/man8/resize2fs.8", cf.paths['man8'])
    cf.do_man(f"{self.seg_dir}/share/man/man8/tune2fs.8", cf.paths['man8'])


"""
/usr/bin/chattr
/usr/bin/fuse2fs
/usr/bin/lsattr
/etc/mke2fs.conf
/usr/lib/e2initrd_helper
/usr/sbin/badblocks
/usr/sbin/debugfs
/usr/sbin/dumpe2fs
/usr/sbin/e2freefrag
/usr/sbin/e2fsck
/usr/sbin/e2image
/usr/sbin/e2label
/usr/sbin/e2mmpstatus
/usr/sbin/e2undo
/usr/sbin/e4crypt
/usr/sbin/e4defrag
/usr/sbin/filefrag
/usr/sbin/fsck.ext2
/usr/sbin/fsck.ext3
/usr/sbin/fsck.ext4
/usr/sbin/logsave
/usr/sbin/mke2fs
/usr/sbin/mkfs.ext2
/usr/sbin/mkfs.ext3
/usr/sbin/mkfs.ext4
/usr/sbin/mklost+found
/usr/sbin/resize2fs
/usr/sbin/tune2fs
/usr/share/man/man1/chattr.1.bz2
/usr/share/man/man1/fuse2fs.1.bz2
/usr/share/man/man1/lsattr.1.bz2
/usr/share/man/man5/e2fsck.conf.5.bz2
/usr/share/man/man5/ext2.5.bz2
/usr/share/man/man5/ext3.5.bz2
/usr/share/man/man5/ext4.5.bz2
/usr/share/man/man5/mke2fs.conf.5.bz2
/usr/share/man/man8/badblocks.8.bz2
/usr/share/man/man8/debugfs.8.bz2
/usr/share/man/man8/dumpe2fs.8.bz2
/usr/share/man/man8/e2freefrag.8.bz2
/usr/share/man/man8/e2fsck.8.bz2
/usr/share/man/man8/e2image.8.bz2
/usr/share/man/man8/e2label.8.bz2
/usr/share/man/man8/e2mmpstatus.8.bz2
/usr/share/man/man8/e2undo.8.bz2
/usr/share/man/man8/e4crypt.8.bz2
/usr/share/man/man8/e4defrag.8.bz2
/usr/share/man/man8/filefrag.8.bz2
/usr/share/man/man8/fsck.ext2.8.bz2
/usr/share/man/man8/fsck.ext3.8.bz2
/usr/share/man/man8/fsck.ext4.8.bz2
/usr/share/man/man8/logsave.8.bz2
/usr/share/man/man8/mke2fs.8.bz2
/usr/share/man/man8/mkfs.ext2.8.bz2
/usr/share/man/man8/mkfs.ext3.8.bz2
/usr/share/man/man8/mkfs.ext4.8.bz2
/usr/share/man/man8/mklost+found.8.bz2
/usr/share/man/man8/resize2fs.8.bz2
/usr/share/man/man8/tune2fs.8.bz2
"""
