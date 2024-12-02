#    net-util/inetutils/inetutils-2.5.build.py
#    Sat Nov 16 21:11:57 UTC 2024

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
    self.do("sed -i 's/def HAVE_TERMCAP_TGETENT/ 1/' telnet/telnet.c")
    return self.do(f"./configure --prefix=/usr "
                   "--bindir=/usr/bin "
                   "--localstatedir=/var "
                   "--disable-logger "
                   "--disable-whois "
                   "--disable-rcp "
                   "--disable-rexec "
                   "--disable-rlogin "
                   "--disable-rsh "
                   "--disable-servers")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    # ping, ping6, and traceroute will fail to install as root user
    self.do(f"chmod 755 {self.p['_ub']}/ping")
    self.do(f"chmod 755 {self.p['_ub']}/ping6")
    self.do(f"chmod 755 {self.p['_ub']}/traceroute")

    self.inst_binary(f"{self.p['_ub']}/dnsdomainname", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/ftp", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/hostname", self.p['ub'])
    # ifconfig to /usr/sbin
    self.inst_binary(f"{self.p['_ub']}/ifconfig", self.p['us'])
    self.inst_binary(f"{self.p['_ub']}/ping", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/ping6", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/telnet", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/tftp", self.p['ub'])
    self.inst_binary(f"{self.p['_ub']}/traceroute", self.p['ub'])

    for man in os.listdir(self.p['_man1']):
        if man in ['ifconfig.1']:
            os.rename(f"{self.p['_man1']}/{man}", self.p['_man1'] + "/ifconfig.8")
            self.inst_manpage(f"{self.p['_man1']}/ifconfig.8", self.p['man8'])
        else:
            self.inst_manpage(f"{self.p['_man1']}/{man}", self.p['man1'])



