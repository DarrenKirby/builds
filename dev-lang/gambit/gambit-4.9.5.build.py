#    dev-lang/gambit/gambit-4.9.5.build.py
#    Thu Nov 28 21:53:25 UTC 2024

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
    os.rename(f"gambit-v{self.version.replace('.', '_')}", f"gambit-{self.version}")


def configure(self):
    return self.do("./configure --prefix=/usr --enable-single-host "
                   "--enable-march=native "
                   "--disable-absolute-shared-libs ")


def make(self):
    try:
        self.do(f"make {cf.config['makeopts']}")
        self.do("make check")
        self.do(f"make {cf.config['makeopts']} modules")
        return 0
    except subprocess.CalledProcessError:
        return 1


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    for file in glob.glob(f"{self.p['_ub']}/gamb*"):
        self.inst_script(file, self.p['ub'])

    self.inst_binary(self.p['_ub'] + "/gsc", self.p['ub'])
    self.inst_binary(self.p['_ub'] + "/gsi", self.p['ub'])

    self.inst_symlink(self.p['ub'] + "/gsc", self.p['ub'] + "/gsc-script")
    self.inst_symlink(self.p['ub'] + "/gsi", self.p['ub'] + "/gsi-script")
    self.inst_symlink(self.p['ub'] + "/gsi", self.p['ub'] + "/scheme-ieee-1178-1990")
    self.inst_symlink(self.p['ub'] + "/gsi", self.p['ub'] + "/scheme-r4rs")
    self.inst_symlink(self.p['ub'] + "/gsi", self.p['ub'] + "/scheme-r5rs")
    self.inst_symlink(self.p['ub'] + "/gsi", self.p['ub'] + "/scheme-srfi-0")
    self.inst_symlink(self.p['ub'] + "/gsi", self.p['ub'] + "/six")
    self.inst_symlink(self.p['ub'] + "/gsi", self.p['ub'] + "/six-script")

    self.inst_header(f"{self.p['_ui']}/gambit-not409005.h", self.p['ui'])
    self.inst_header(f"{self.p['_ui']}/gambit.h", self.p['ui'])

    self.inst_directory(f"{self.p['_ul']}/_base64/", f"{self.p['ul']}/_base64/")
    self.inst_directory(f"{self.p['_ul']}/_define-library/", f"{self.p['ul']}/_define-library/")
    self.inst_directory(f"{self.p['_ul']}/_digest/", f"{self.p['ul']}/_digest/")
    self.inst_directory(f"{self.p['_ul']}/_geiser/", f"{self.p['ul']}/_geiser/")
    self.inst_directory(f"{self.p['_ul']}/_git/", f"{self.p['ul']}/_git/")
    self.inst_directory(f"{self.p['_ul']}/_hamt/", f"{self.p['ul']}/_hamt/")
    self.inst_directory(f"{self.p['_ul']}/_http/", f"{self.p['ul']}/_http/")
    self.inst_directory(f"{self.p['_ul']}/_match/", f"{self.p['ul']}/_match/")
    self.inst_directory(f"{self.p['_ul']}/_pkg/", f"{self.p['ul']}/_pkg/")
    self.inst_directory(f"{self.p['_ul']}/_six/", f"{self.p['ul']}/_six/")
    self.inst_directory(f"{self.p['_ul']}/_tar/", f"{self.p['ul']}/_tar/")
    self.inst_directory(f"{self.p['_ul']}/_test/", f"{self.p['ul']}/_test/")
    self.inst_directory(f"{self.p['_ul']}/_uri/", f"{self.p['ul']}/_uri/")
    self.inst_directory(f"{self.p['_ul']}/_zlib/", f"{self.p['ul']}/_zlib/")
    self.inst_directory(f"{self.p['_ul']}/gambit/", f"{self.p['ul']}/gambit/")
    self.inst_directory(f"{self.p['_ul']}/scheme/", f"{self.p['ul']}/scheme/")
    self.inst_directory(f"{self.p['_ul']}/srfi/", f"{self.p['ul']}/srfi/")
    self.inst_directory(f"{self.p['_ul']}/termite/", f"{self.p['ul']}/termite/")

    for file in glob.glob(f"{self.p['_ul']}/*.scm"):
        self.inst_file(file, self.p['ul'])

    self.inst_file(f"{self.p['_ul']}/_gambit.c", self.p['ul'])
    self.inst_file(f"{self.p['_ul']}/_gambit.js", self.p['ul'])
    self.inst_file(f"{self.p['_ul']}/_gambitgsc.c", self.p['ul'])
    self.inst_file(f"{self.p['_ul']}/_gambitgsi.c", self.p['ul'])

    self.inst_manpage(f"{self.p['_man1']}/gsi.1", self.p['man1'])

    # I'm a vim guy, not Emacs. Not sure where to put the 'gambit.el' file.
    # Let me know, and I'll put it there (or send a pull request :-)
