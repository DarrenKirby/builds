#    app-shell/bash/bash-5.2.37.build.py
#    Thu Oct 31 03:43:21 UTC 2024

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
    return os.system(f"./configure --prefix={self.seg_dir} "
                     f"--without-bash-malloc "
                     f"--with-installed-readline "
                     f"bash_cv_strtold_broken=no")


def make(self):
    return os.system("make")


def make_install(self):
    return os.system("make install")


def install(self):
    self.inst_binary(f"{self.seg_dir}/bin/bash", cf.paths['ub'])
    self.inst_script(f"{self.seg_dir}/bin/bashbug", cf.paths['ub'])

    # headers
    self.inst_directory(f"{self.seg_dir}/include/bash/", f"{cf.paths['ui']}/bash/")
    # builtins
    self.inst_directory(f"{self.seg_dir}/lib/bash/", f"{cf.paths['ul']}/bash/")

    self.inst_manpage(f"{self.seg_dir}/share/man/man1/bash.1", cf.paths['man1'])
    self.inst_manpage(f"{self.seg_dir}/share/man/man1/bashbug.1", cf.paths['man1'])


def cleanup_posthook(self):
    cf.yellow("Make /bin/sh link to /usr/bin/bash ? (y/n)")
    if input() not in ['n', 'N', 'No', 'no']:
        cf.do_sym("/usr/bin/bash", "/bin/sh")
    cf.bold("Run...")
    print("\texec /usr/bin/bash --login")
    cf.bold("...to load new bash shell immediatly")
