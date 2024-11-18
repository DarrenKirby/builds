#    app-util/coreutils/coreutils-9.5.build
#    Wed Nov 13 02:07:51 UTC 2024

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



def fetch_prehook(self):
    patchname = "coreutils-9.5-i18n-2.patch"
    cf.bold(f"Downloading {patchname}...")
    cf.download("https://www.linuxfromscratch.org/patches/lfs/12.2/coreutils-9.5-i18n-2.patch",
                f"{cf.config['builds_root']}/distfiles/{patchname}")
    cf.bold("...done.")



def install_source_posthook(self):
    os.chdir(self.package_dir)
    patchname = "coreutils-9.5-i18n-2.patch"
    es = os.system(f"patch -Np1 -i {cf.config['builds_root']}/distfiles/{patchname}")
    os.chdir(self.work_dir)
    return es


def configure(self):
    es1 = os.system("autoreconf -fiv")
    es2 = os.system("FORCE_UNSAFE_CONFIGURE=1 "
                    "./configure --prefix=/usr "
                    "--enable-no-install-program=kill,uptime")

    if es1 == 0 and es2 == 0:
        return 0
    return 12


def make(self):
    return os.system(f"make {cf.config['makeopts']}")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} install")


def install(self):
    # FHS says chroot should be in sbin
    self.inst_binary(f"{self.p['_ub']}/chroot", self.p['us'])
    os.remove(f"{self.p['_ub']}/chroot")

    os.rename(f"{self.p['_man1']}/chroot.1", f"{self.p['_man1']}/chroot.8")
    self.inst_manpage(f"{self.p['_man1']}/chroot.8", self.p['man8'])
    # We need to remove chroot.8.bz2 or bzip2 will fail
    # trying to compress it again in the second inst_manpage() call
    os.remove(f"{self.p['_man1']}/chroot.8.bz2")

    for file in os.listdir(self.p['_ub']):
        self.inst_binary(f"{self.p['_ub']}/{file}", self.p['ub'])

    for file in os.listdir(self.p['_man1']):
        self.inst_manpage(f"{self.p['_man1']}/{file}", self.p['man1'])

    self.inst_directory(f"{self.p['_ule']}/coreutils/", f"{self.p['ule']}/coreutils/")
