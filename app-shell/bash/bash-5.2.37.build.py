#    app-shell/bash/bash-5.2.37.build.py
#    Thu Nov  7 04:18:15 UTC 2024

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
    return os.system("./configure --prefix=/usr "
                     f"--without-bash-malloc "
                     f"--with-installed-readline "
                     f"bash_cv_strtold_broken=no")


def make(self):
    return os.system(f"make {cf.config['makeopts']}")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_binary(f"{self.p['_ub']}/bash", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/bashbug", self.p['ub'])

    # headers
    self.inst_directory(f"{self.p['_ui']}/bash/", f"{self.p['ui']}/bash/")
    # builtins
    self.inst_directory(f"{self.p['_ul']}/bash/", f"{self.p['ul']}/bash/")

    self.inst_manpage(f"{self.p['_man1']}/share/man/man1/bash.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/share/man/man1/bashbug.1", self.p['man1'])


def cleanup_posthook(self):
    print()
    cf.yellow("Make /bin/sh link to /usr/bin/bash ? (y/n)")
    if input(">>> ") not in ['n', 'N', 'No', 'no']:
        self.inst_symlink("/usr/bin/bash", "/bin/sh")
    cf.bold("Run...")
    print("\texec /usr/bin/bash --login")
    cf.bold("...to load new bash shell immediatly")
