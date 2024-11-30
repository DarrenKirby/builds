#    app-util/kbd/kbd-2.6.4.build.py
#    Thu Nov 21 16:33:12 UTC 2024

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
    patchname = "kbd-2.6.4-backspace-1.patch"
    cf.bold(f"Downloading {patchname}...")
    cf.download(f"https://www.linuxfromscratch.org/patches/lfs/12.2/{patchname}",
                f"{cf.config['builds_root']}/distfiles/{patchname}")
    cf.bold("...done.")


def install_source_posthook(self):
    os.chdir(self.package_dir)
    patchname = "kbd-2.6.4-backspace-1.patch"
    cf.bold(f"Applying {patchname}")
    self.do(f"patch -Np1 -i {cf.config['builds_root']}/distfiles/{patchname}")
    os.chdir(self.work_dir)


def configure(self):
    # Prevent static libs
    self.do("sed -i '/RESIZECONS_PROGS=/s/yes/no/' configure")
    self.do("sed -i 's/resizecons.8 //' docs/man/man8/Makefile.in")
    return self.do("./configure --prefix=/usr --disable-vlock")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    pass