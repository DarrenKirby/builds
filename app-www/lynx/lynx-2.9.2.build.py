#    app-www/lynx/lynx-2.9.2.build.py
#    Sun Dec  1 03:55:11 UTC 2024

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
    os.rename(f"lynx{self.version}", f"lynx-{self.version}")


def configure(self):
    conf_d = '/etc/lynx' if cf.config['user'] == 'root' else '/usr/etc/lynx'
    return self.do("./configure --prefix=/usr "
                   f"--sysconfdir={conf_d} "
                   "--with-zlib "
                   "--with-bzlib "
                   "--with-ssl "
                   "--with-screen=ncursesw "
                   "--enable-locale-charset")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    self.inst_binary(self.p['_ub'] + "/lynx", self.p['ub'])

    self.inst_manpage(self.p['_man1'] + "/lynx.1", self.p['man1'])

    conf_d = 'e' if cf.config['user'] == 'root' else 'ue'
    self.inst_directory(f"{self.p['_' + conf_d]}/lynx/", f"{self.p['_' + conf_d]}/lynx/")
