#    app-util/xfsprogs/xfsprogs-6.9.0.build.py
#    Tue Oct 29 21:39:35 UTC 2024

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


depend="dev-lib/inih,lib-util/liburcu"


def configure(self):
    return os.system(f"./configure --prefix={self.seg_dir} --enable-static=no")


def make(self):
    # BUG: This hack will likely break on systemd systems,
    # or to be sure, it won't fix the underlying issue.
    # Prevent install script from installing xfs.rules to
    # /usr/lib/udev/rules.d/
    os.system("sed -i -e 's/install-udev//' scrub/Makefile")
    return os.system("make DEBUG=-DNDEBUG")


def make_install(self):
    return os.system("make install")


def install(self):
    self.inst_library(f"{self.seg_dir}/lib64/libhandle.so.1.0.3", cf.paths['ul'])
    self.inst_symlink(f"{cf.paths['ul']}/libhandle.so.1.0.3", f"{cf.paths['ul']}/libhandle.so.1")

    for file in os.listdir(f"{cf.config['builds_root']}/app-util/xfsprogs/work/seg/sbin"):
        self.inst_binary(f"{self.seg_dir}/sbin/{file}", cf.paths['us'])

    self.inst_manpage(f"{self.seg_dir}/share/man/man5/projects.5", cf.paths['man5'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man5/projid.5", cf.paths['man5'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man5/xfs.5", cf.paths['man5'])

    for file in os.listdir(f"{cf.config['builds_root']}/app-util/xfsprogs/work/seg/share/man/man8"):
        self.inst_manpage(f"{self.seg_dir}/share/man/man8/{file}", cf.paths['man8'])

    self.inst_directory(f"{self.seg_dir}/share/xfsprogs/", f"{cf.paths['ush']}/xfsprogs/")

    # Install xfs.rules to /usr/lib/udev/rules.d
    self.inst_file("./scrub/xfs.rules", f"{cf.paths['ul']}/udev/rules.d/64-xfs.rules")
