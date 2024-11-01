#    app-util/coreutils/coreutils-9.5.build
#    Thu Oct 31 21:14:16 UTC 2024

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
    es2 = os.system(f"FORCE_UNSAFE_CONFIGURE=1 "
                    f"./configure --prefix={self.seg_dir} "
                    f"--enable-no-install-program=kill,uptime")

    if es1 == 0 and es2 == 0:
        return 0
    return 12


def make(self):
    return os.system(f"make {cf.config['makeopts']}")


def make_install(self):
    return os.system("make install")


def install(self):
    # FHS says chroot should be in sbin
    self.inst_binary(f"{self.seg_dir}/bin/chroot", cf.paths['us'])
    os.remove(f"{self.seg_dir}/bin/chroot")

    os.rename(f"{self.seg_dir}/share/man/man1/chroot.1", f"{self.seg_dir}/share/man/man1/chroot.8")
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/chroot.8", cf.paths['man8'])

    for app in glob.glob(f"{self.seg_dir}/bin/*"):
        self.inst_binary(f"{self.seg_dir}/bin/{app}", cf.paths['ub'])

    for manpage in glob.glob(f"{self.seg_dir}/share/man/man1/*.1"):
        self.inst_manpage(f"{self.seg_dir}/share/man/man1/{manpage}", cf.paths['man1'])

    self.inst_directory(f"{self.seg_dir}/libexec/coreutils/", f"{cf.paths['ul']}exec/coreutils/")
