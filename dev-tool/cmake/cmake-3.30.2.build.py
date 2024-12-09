#    dev-tool/cmake/cmake-3.30.2.build.py
#    Sun Dec  8 03:06:54 UTC 2024

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

depend = "net-util/curl,dev-util/libarchive,dev-util/libuv,dev-util/nghttp2"


def configure(self):
    try:
        self.do("""
        sed -i '/"lib64"/s/64//' Modules/GNUInstallDirs.cmake
        """)
        self.do("./bootstrap --prefix=/usr "
                "--system-libs "
                "--mandir=/share/man "
                "--no-system-jsoncpp "
                "--no-system-cppdap "
                "--no-system-librhash")
        return 0
    except OSError as e:
        return 12


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    pass
