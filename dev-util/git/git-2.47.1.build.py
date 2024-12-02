#    dev-util/git/git-2.47.1.build.py
#    Wed Nov 27 05:49:06 UTC 2024

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


depend = "net-util/curl"


def fetch_posthook(self):
    url = f"https://www.kernel.org/pub/software/scm/git/git-manpages-{self.version}.tar.xz"
    cf.bold(f"Fetching {url.split('/')[-1]}")
    cf.download(url, url.split('/')[-1])


def install_source_posthook(self):
    import shutil
    shutil.unpack_archive(f"{self.builds_root}/distfiles/git-manpages-{self.version}.tar.xz", ".")


def configure(self):
    return os.system("./configure --prefix=/usr "
                     "--with-gitconfig=/etc/gitconfig "
                     "--with-python=python3")


def make(self):
    return os.system("make")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} install")


def install(self):
    for file in os.listdir(self.p['_ub']):
        if file in ["git-cvsserver", "gitk"]:
            self.inst_script(f"{self.p['_ub']}/{file}", self.p['ub'])
        else:
            self.inst_binary(f"{self.p['_ub']}/{file}", self.p['ub'])

    self.inst_directory(f"{self.p['_ule']}/git-core/", f"{self.p['ule']}/git-core/")
    self.inst_directory(f"{self.p['_ush']}/git-core/", f"{self.p['ush']}/git-core/")
    self.inst_directory(f"{self.p['_ush']}/git-gui/", f"{self.p['ush']}/git-gui/")
    self.inst_directory(f"{self.p['_ush']}/gitk/", f"{self.p['ush']}/gitk/")
    self.inst_directory(f"{self.p['_ush']}/gitweb/", f"{self.p['ush']}/gitweb/")
    # self.inst_directory(f"{self.p['_ush']}/locale/", f"{self.p['ush']}/locale/")
    # Perl modules
    self.inst_directory(f"{self.p['_ush']}/perl5/Git/", f"{self.p['ul']}/perl5/5.40/site_perl/Git/")
    self.inst_directory(f"{self.p['_ush']}/perl5/FromCPAN/", f"{self.p['ul']}/perl5/5.40/site_perl/FromCPAN/")
    self.inst_file(f"{self.p['_ush']}/perl5/Git.pm", f"{self.p['ul']}/perl5/5.40/site_perl/")

    for file in os.listdir(f"{self.work_dir}/man1/"):
        self.inst_manpage(f"{self.work_dir}/man1/{file}", self.p['man1'])

    for file in os.listdir(f"{self.work_dir}/man5/"):
        self.inst_manpage(f"{self.work_dir}/man5/{file}", self.p['man5'])

    for file in os.listdir(f"{self.work_dir}/man7/"):
        self.inst_manpage(f"{self.work_dir}/man7/{file}", self.p['man7'])
