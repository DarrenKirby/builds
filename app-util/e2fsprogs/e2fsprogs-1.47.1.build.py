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

    return os.system("../configure --prefix=/usr "
                     "--enable-elf-shlibs "
                     "--disable-libblkid "
                     "--disable-libuuid "
                     "--disable-uuidd "
                     "--disable-fsck")


def make(self):
    return os.system(f"make {cf.config['makeopts']}")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_binary(f"{self.p['_ub']}/chattr", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/fuse2fs", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/lsattr", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/compile_et", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/mk_cmds", self.p['ub'])

    # Rather than pick through them, we'll skip stripping and do it after
    for file in os.listdir(self.p['_us']):
        self.inst_script(f"{self.p['_us']}/{file}", self.p['us'])

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

    self.inst_config(f"{self.p['_ue']}/mke2fs.conf", self.p['ue'])
    self.inst_config(f"{self.p['_ue']}/e2scrub.conf", self.p['ue'])

    for file in os.listdir(self.p['_man1']):
        self.inst_manpage(f"{self.p['_man1']}/{file}", self.p['man1'])

    for file in os.listdir(self.p['_man5']):
        self.inst_manpage(f"{self.p['_man5']}/{file}", self.p['man5'])

    for file in os.listdir(self.p['_man8']):
        self.inst_manpage(f"{self.p['_man8']}/{file}", self.p['man8'])

    for file in ["badblocks",
                 "debugfs",
                 "dumpe2fs",
                 "e2freefrag",
                 "e2fsck",
                 "e2image",
                 "e2undo",
                 "e4crypt",
                 "e4defrag",
                 "filefrag",
                 "logsave",
                 "mke2fs",
                 "mklost+found",
                 "resize2fs",
                 "tune2fs"]:
        os.system(f"strip {self.p['us']}/{file}")
        print(f"stripping {self.p['us']}/{file}")
