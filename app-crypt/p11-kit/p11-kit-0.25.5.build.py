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
    self.do("sed '20,$ d' -i trust/trust-extract-compat")
    with open("trust/trust-extract-compat", "a", encoding='utf-8') as f:
        f.write(text)
    os.chdir(self.work_dir)

def configure(self):
    os.mkdir("build")
    os.chdir("build")
    return self.do("meson setup --prefix=/usr --buildtype=release -D trust_paths=/etc/pki/anchors")


def make(self):
    return self.do("ninja")


def make_install(self):
    return self.do(f"DESTDIR={self.seg_dir} ninja install")


def install(self):
    pass

