#    net-util/dhcpcd/dhcpcd-10.0.8.build.py
#    Sun Dec  1 19:19:50 UTC 2024

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
    conf_d = '/etc' if cf.config['user'] == 'root' else '/usr/etc'
    return self.do("./configure --prefix=/usr "
                   f"--sysconfdir={conf_d} "
                   "--libexecdir=/usr/lib/dhcpcd "
                   "--dbdir=/var/lib/dhcpcd "
                   "--runstatedir=/run "
                   "--disable-privsep")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    pass
