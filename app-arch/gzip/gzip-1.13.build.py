#    app-arch/gzip/gzip-1.13.build.py
#    Sun Oct 20 22:39:54 UTC 2024

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
    self.inst_binary(f"{self.seg_dir}/bin/gzip", cf.paths['b'])
    self.inst_script(f"{self.seg_dir}/bin/gunzip", cf.paths['b'])
    self.inst_script(f"{self.seg_dir}/bin/gzexe", cf.paths['b'])
    self.inst_script(f"{self.seg_dir}/bin/uncompress", cf.paths['b'])
    self.inst_script(f"{self.seg_dir}/bin/zcat", cf.paths['b'])
    self.inst_script(f"{self.seg_dir}/bin/zcmp", cf.paths['b'])
    self.inst_script(f"{self.seg_dir}/bin/zdiff", cf.paths['b'])
    self.inst_script(f"{self.seg_dir}/bin/zegrep", cf.paths['b'])
    self.inst_script(f"{self.seg_dir}/bin/zfgrep", cf.paths['b'])
    self.inst_script(f"{self.seg_dir}/bin/zforce", cf.paths['b'])
    self.inst_script(f"{self.seg_dir}/bin/zgrep", cf.paths['b'])
    self.inst_script(f"{self.seg_dir}/bin/zless", cf.paths['b'])
    self.inst_script(f"{self.seg_dir}/bin/zmore", cf.paths['b'])
    self.inst_script(f"{self.seg_dir}/bin/znew", cf.paths['b'])

    for manpage in glob.glob(f"{self.seg_dir}/share/man/man1/*.1"):
        self.inst_manpage(manpage, cf.paths['man1'])
