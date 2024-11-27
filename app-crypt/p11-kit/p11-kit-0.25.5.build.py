#    app-crypt/p11-kit/p11-kit-0.25.5.build.py
#    Tue Nov 26 21:42:40 UTC 2024

#    Copyright:: (c) 2024
#    Author:: Darren Kirby (mailto:Darren Kirby)

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

depend = "dev-lib/libtasn1"


# Prepare LFS/BLFS specific anchor hook
def install_source_posthook(self):
    # Bail if not root
    if cf.config['user'] != 'root':
        return

    text = """
# Copy existing anchor modifications to /etc/ssl/local
/usr/libexec/make-ca/copy-trust-modifications

# Update trust stores
/usr/sbin/make-ca -r    
"""
    os.chdir(self.package_dir)
    os.system("sed '20,$ d' -i trust/trust-extract-compat")
    with open("trust/trust-extract-compat", "a", encoding='utf-8') as f:
        f.write(text)
    os.chdir(self.work_dir)

def configure(self):
    os.mkdir("build")
    os.chdir("build")
    return os.system("meson setup --prefix=/usr --buildtype=release -D trust_paths=/etc/pki/anchors")


def make(self):
    return os.system("ninja")


def make_install(self):
    return os.system(f"DESTDIR={self.seg_dir} ninja install")


def install(self):
    pass
    #self.inst_binary(f"{self.p['_ub']}/psl", self.p['ub'])
    #self.inst_script(f"{self.p['_ub']}/psl-make-dafsa", self.p['ub'])

    #self.inst_header(f"{self.p['_ui']}/libpsl.h", self.p['ui'])

    #self.inst_library(f"{self.p['_ul']}/libpsl.so.5.3.5", self.p['ul'])
    #self.inst_symlink(f"{self.p['ul']}/libpsl.so.5.3.5", f"{self.p['ul']}/libpsl.so.5")
    #self.inst_symlink(f"{self.p['ul']}/libpsl.so.5", f"{self.p['ul']}/libpsl.so")

    #self.inst_file(f"{self.p['_ul']}/pkgconfig/libpsl.pc", f"{self.p['ul']}/pkgconfig/")

    #self.inst_manpage(f"{self.p['_man1']}/psl.1", self.p['man1'])
    #self.inst_manpage(f"{self.p['_man1']}/psl-make-dafsa.1", self.p['man1'])