#    app-editor/vim/vim-9.0.build.py
#    Thu Nov 28 00:14:14 UTC 2024

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


def install_source_posthook(self):
    # extracted directory does not match tarball
    try:
        os.rename(self.package_dir.replace('-', '').replace('.', ''), self.package_dir)
    except OSError as e:
        cf.red(f"rename failed: {e}")

def configure(self):

    # change the default location of the vimrc configuration file to /etc
    with open("src/feature.h", 'a', encoding='utf-8') as f:
        f.write('#define SYS_VIMRC_FILE "/etc/vimrc"')

    return self.do(f"./configure --prefix=/usr --with-x=no --disable-gui")


def make(self):
    return self.do("make")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_binary(f"{self.p['_ub']}/vim", self.p['ub'])
    self.inst_script(f"{self.p['_ub']}/vimtutor", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/xxd", self.p['ub'])

    self.inst_symlink(f"{self.p['ub']}/vim", f"{self.p['ub']}/ex")
    self.inst_symlink(f"{self.p['ub']}/vim", f"{self.p['ub']}/rview")
    self.inst_symlink(f"{self.p['ub']}/vim", f"{self.p['ub']}/rvim")
    self.inst_symlink(f"{self.p['ub']}/vim", f"{self.p['ub']}/view")
    self.inst_symlink(f"{self.p['ub']}/vim", f"{self.p['ub']}/vimdiff")

    # make the vi symlink
    self.inst_symlink(f"{self.p['ub']}/vim", f"{self.p['ub']}/vi")

    self.inst_manpage(f"{self.p['_man1']}/evim.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/vim.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/vimdiff.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/vimtutor.1", self.p['man1'])
    self.inst_manpage(f"{self.p['_man1']}/xxd.1", self.p['man1'])

    self.inst_symlink(f"{self.p['man1']}/vim.1.bz2", f"{self.p['man1']}/ex.1")
    self.inst_symlink(f"{self.p['man1']}/vim.1.bz2", f"{self.p['man1']}/rview.1")
    self.inst_symlink(f"{self.p['man1']}/vim.1.bz2", f"{self.p['man1']}/rvim.1")
    self.inst_symlink(f"{self.p['man1']}/vim.1.bz2", f"{self.p['man1']}/view.1")
    self.inst_symlink(f"{self.p['man1']}/vim.1.bz2", f"{self.p['man1']}/vi.1")

    self.inst_directory(f"{self.p['_ush']}/vim/", f"{self.p['ush']}/vim/")
