#    app-util/gawk/gawk-5.3.1.build.py
#    Thu Oct 31 22:11:26 UTC 2024

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
    cf.bold("Removing gawk extras from makefile...")
    try:
        os.system("sed -i 's/extras//' Makefile.in")
    except:
        cf.yellow("sed command failed: non fatal")
    return os.system(f"./configure --prefix={self.seg_dir}")


def make(self):
    return os.system(f"make {cf.config['makeopts']}")


def make_install(self):
    return os.system(f"make  {cf.config['makeopts']}install")


def install(self):
    self.inst_binary(f"{self.seg_dir}/bin/gawk", cf.paths['ub'])
    self.inst_binary(f"{self.seg_dir}/bin/gawk-5.3.1", cf.paths['ub'])
    self.inst_script(f"{self.seg_dir}/bin/gawkbug", cf.paths['ub'])
    # link awk -> gawk
    self.inst_symlink(f"{cf.paths['ub']}/gawk", f"{cf.paths['ub']}/awk")

    self.inst_header(f"{self.seg_dir}/include/gawkapi.h", cf.paths['ui'])

    self.inst_directory(f"{self.seg_dir}/lib/gawk/", f"{cf.paths['ul']}/gawk/")

    self.inst_directory(f"{self.seg_dir}/libexec/awk/", f"{cf.paths['ule']}/awk/")

    self.inst_manpage(f"{self.seg_dir}/share/man/man1/gawk.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/gawkbug.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/pm-gawk.1", cf.paths['man1'])
    # link  awk.1 -> gawk1.bz2
    self.inst_symlink(f"{cf.paths['man1']}/gawk.1.bz2", f"{cf.paths['man1']}/awk.1")

    self.inst_manpage(f"{self.seg_dir}/share/man/man3/filefuncs.3am", cf.paths['man3'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man3/fnmatch.3am", cf.paths['man3'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man3/fork.3am", cf.paths['man3'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man3/inplace.3am", cf.paths['man3'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man3/ordchr.3am", cf.paths['man3'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man3/readdir.3am", cf.paths['man3'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man3/readfile.3am", cf.paths['man3'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man3/revoutput.3am", cf.paths['man3'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man3/revtwoway.3am", cf.paths['man3'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man3/rwarray.3am", cf.paths['man3'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man3/time.3am", cf.paths['man3'])
