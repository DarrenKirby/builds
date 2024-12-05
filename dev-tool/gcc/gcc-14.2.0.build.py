#    dev-tool/gcc/gcc-14.2.0.build.py
#    Wed Dec  4 19:01:19 UTC 2024

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
    if os.uname()[-1] == 'x86_64':
        self.do("sed -e '/m64=/s/lib64/lib/' -i.orig gcc/config/i386/t-linux64")
    os.mkdir("build")
    os.chdir("build")
    return self.do("../configure --prefix=/usr "
                   "LD=ld "
                   "LDFLAGS='-L/usr/lib64' "
                   "--enable-languages=c,c++ "
                   "--enable-default-pie "
                   "--enable-default-ssp "
                   "--enable-host-pie "
                   "--disable-multilib "
                   "--disable-fixincludes "
                   "--with-system-zlib")


def make(self):
    return self.do(f"make")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    pass