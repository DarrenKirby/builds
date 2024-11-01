#    app-util/e2fsprogs/e2fsprogs-1.47.1.build.py
#    Thu Oct 31 22:20:22 UTC 2024

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

    return os.system(f"../configure --prefix=/usr "
                    f"--enable-elf-shlibs "
                    f"--disable-libblkid "
                    f"--disable-libuuid "
                    f"--disable-uuidd "
                    f"--disable-fsck")


def make(self):
    return os.system(f"make {cf.config['makeopts']}")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_binary(f"{self.p['_ub']}/chattr", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/fuse2fs", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/lsattr", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/compile_et", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/mk_cmds", self.p['ub'])

    for file in os.listdir(self.p['_us']):
        self.inst_binary(f"{self.p['_us']}/{file}", self.p['us'])

    for file in os.listdir(f"{self.p['_ul']}/udev/rules.d/"):
        self.inst_file(f"{self.p['_ul']}/udev/rules.d/{file}", f"{self.p['ul']}/udev/rules.d/")

    for file in os.listdir(f"{self.p['_ul']}/pkgconfig/"):
        self.inst_file(f"{self.p['_ul']}/pkgconfig/{file}", f"{self.p['ul']}/pkgconfig/")

    self.inst_library(f"{self.p['_ul']}/e2initrd_helper", self.p['ul'])
    self.inst_library(f"{self.p['_ul']}/libcom_err.so.2.1", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libcom_err.so.2.1", f"{self.p['ul']}/libcom_err.so.2")
    self.inst_symlink(f"{self.p['ul']}/libcom_err.so.2", f"{self.p['ul']}/libcom_err.so")

    self.inst_library(f"{self.p['_ul']}/libe2p.so.2.3", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libe2p.so.2.3", f"{self.p['ul']}/libe2p.so.2")
    self.inst_symlink(f"{self.p['ul']}/libe2p.so.2", f"{self.p['ul']}/libe2p.so")

    self.inst_library(f"{self.p['_ul']}/libext2fs.so.2.4", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libext2fs.so.2.4", f"{self.p['ul']}/libext2fs.so.2")
    self.inst_symlink(f"{self.p['ul']}/libext2fs.so.2", f"{self.p['ul']}/libext2fs.so")

    self.inst_library(f"{self.p['_ul']}/libss.so.2.0", self.p['ul'])
    self.inst_symlink(f"{self.p['ul']}/libss.so.2.0", f"{self.p['ul']}/libss.so.2")
    self.inst_symlink(f"{self.p['ul']}/libss.so.2", f"{self.p['ul']}/libss.so")

    self.inst_config(f"{self.seg_dir}/etc/mke2fs.conf", self.p['e'])

    self.inst_manpage(f"{self.p['_man1']}/chattr.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/fuse2fs.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/lsattr.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man5']}/e2fsck.conf.5", self.p['man5'])
    self.inst_manpage(f"{self.p['_man5']}/ext2.5", self.p['man5'])
    self.inst_manpage(f"{self.p['_man5']}/ext3.5", self.p['man5'])
    self.inst_manpage(f"{self.p['_man5']}/ext4.5", self.p['man5'])
    self.inst_manpage(f"{self.p['_man5']}/mke2fs.conf.5", self.p['man5'])

    for file in os.listdir(self.p['_man8']):
        self.inst_manpage(f"{self.p['_man8']}/{file}", self.p['man8'])
    # self.inst_manpage(f"{self.p['_man8']}/badblocks.8", self.p['man8'])
    # self.inst_manpage(f"{self.p['_man8']}/debugfs.8", self.p['man8'])
    # self.inst_manpage(f"{self.p['_man8']}/dumpe2fs.8", self.p['man8'])
    # self.inst_manpage(f"{self.p['_man8']}/e2freefrag.8", self.p['man8'])
    # self.inst_manpage(f"{self.p['_man8']}/e2fsck.8", self.p['man8'])
    # self.inst_manpage(f"{self.p['_man8']}/e2image.8", self.p['man8'])
    # self.inst_manpage(f"{self.p['_man8']}/e2label.8", self.p['man8'])
    # self.inst_manpage(f"{self.p['_man8']}/e2mmpstatus.8", self.p['man8'])
    # self.inst_manpage(f"{self.p['_man8']}/e2undo.8", self.p['man8'])
    # self.inst_manpage(f"{self.p['_man8']}/e4crypt.8", self.p['man8'])
    # self.inst_manpage(f"{self.p['_man8']}/e4defrag.8", self.p['man8'])
    # self.inst_manpage(f"{self.p['_man8']}/filefrag.8", self.p['man8'])
    # self.inst_manpage(f"{self.p['_man8']}/fsck.ext2.8", self.p['man8'])
    # self.inst_manpage(f"{self.p['_man8']}/fsck.ext3.8", self.p['man8'])
    # self.inst_manpage(f"{self.p['_man8']}/fsck.ext4.8", self.p['man8'])
    # self.inst_manpage(f"{self.p['_man8']}/logsave.8", self.p['man8'])
    # self.inst_manpage(f"{self.p['_man8']}/mke2fs.8", self.p['man8'])
    # self.inst_manpage(f"{self.p['_man8']}/mkfs.ext2.8", self.p['man8'])
    # self.inst_manpage(f"{self.p['_man8']}/mkfs.ext3.8", self.p['man8'])
    # self.inst_manpage(f"{self.p['_man8']}/mkfs.ext4.8", self.p['man8'])
    # self.inst_manpage(f"{self.p['_man8']}/mklost+found.8", self.p['man8'])
    # self.inst_manpage(f"{self.p['_man8']}/resize2fs.8", self.p['man8'])
    # self.inst_manpage(f"{self.p['_man8']}/tune2fs.8", self.p['man8'])
