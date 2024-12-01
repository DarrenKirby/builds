#    net-util/iproute2/iproute2-6.11.0.build.py
#    Sun Dec  1 00:37:10 UTC 2024
import os


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
    # arpd is not getting installed
    os.unlink("man/man8/arpd.8")
    return self.do("./configure --prefix=/usr --color=auto")


def make(self):
    return self.do("make NETNS_RUN_DIR=/run/netns")


def make_install(self):
    return self.do(f"make SBINDIR=/usr/sbin DESTDIR={self.seg_dir} install")


def install(self):
    for file in os.listdir(self.p['_us']):
        if file not in ["ctstat", "routel", "rtstat"]:
            self.inst_binary(f"{self.p['_us']}/{file}", self.p['us'])

    self.inst_script(self.p['_us'] + "/routel", self.p['us'])
    self.inst_symlink(self.p['us'] + "/lnstat", self.p['us'] + "/ctstat")
    self.inst_symlink(self.p['us'] + "/lnstat", self.p['us'] + "/rtstat")

    self.inst_directory(f"{self.p['_ul']}/tc/", f"{self.p['ul']}/tc/")
    self.inst_directory(f"{self.p['_ui']}/iproute2/", f"{self.p['ui']}/iproute2/")

    self.inst_directory(f"{self.p['_ush']}/iproute2/", f"{self.p['ush']}/iproute2/")

    #
    self.inst_file(self.p['_ush'] + "/bash-completion/completions/devlink",
                   self.p['ush'] + "/bash-completion/completions/")
    self.inst_file(self.p['_ush'] + "/bash-completion/completions/tc",
                   self.p['ush'] + "/bash-completion/completions/")

    self.inst_manpage(f"{self.p['_man3']}/libnetlink.3", self.p['man3'])
    self.inst_manpage(f"{self.p['_man7']}/tc-hfsc.7", self.p['man7'])

    for file in os.listdir(self.p['_man8']):
        self.inst_manpage(f"{self.p['_man8']}/{file}", self.p['man8'])
