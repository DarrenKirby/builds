#    net-util/openssh/openssh-9.9p1.build.py
#    Tue Nov 26 19:14:43 UTC 2024

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
    conf_d = '/etc/ssh' if cf.config['user'] == 'root' else '/usr/etc/ssh'
    return self.do("./configure --prefix=/usr "
                   f"--sysconfdir={conf_d} "
                   "--with-privsep-path=/var/lib/sshd "
                   "--with-default-path=/usr/bin "
                   "--with-superuser-path=/usr/sbin:/usr/bin "
                   "--with-pid-dir=/run")


def make(self):
    return self.do(f"make {cf.config['makeopts']}")


def make_install(self):
    return self.do(f"make DESTDIR={self.seg_dir} install")


def install(self):
    # Get all files in work/seg/usr/bin/, and install to /usr/bin/
    for file in os.listdir(self.p['_ub']):
        self.inst_script(f"{self.p['_ub']}/{file}", self.p['ub'])

    # install sshd
    self.inst_script(f"{self.p['_us']}/sshd", self.p['us'])

    # install helper programs to /usr/libexec
    for file in os.listdir(self.p['_ule']):
        self.inst_script(f"{self.p['_ule']}/{file}", self.p['ule'])

    # install manpages
    for file in os.listdir(self.p['_man1']):
        self.inst_manpage(f"{self.p['_man1']}/{file}", self.p['man1'])

    for file in os.listdir(self.p['_man5']):
        self.inst_manpage(f"{self.p['_man5']}/{file}", self.p['man5'])

    for file in os.listdir(self.p['_man8']):
        self.inst_manpage(f"{self.p['_man8']}/{file}", self.p['man8'])

    # install configuration files
    conf_d = 'e' if cf.config['user'] == 'root' else 'ue'
    self.inst_directory(self.p['_' + conf_d] + '/ssh/', self.p[conf_d] + '/ssh/')

    # Install ssh-copy-id and manpage
    self.inst_script(f"{self.work_dir}/{self.package_dir}/contrib/ssh-copy-id", self.p['ub'])
    self.inst_manpage(f"{self.work_dir}/{self.package_dir}/contrib/ssh-copy-id.1", self.p['man1'])


# This will only work on a system install.
def cleanup_posthook(self):
    if cf.config['user'] != 'root':
        return
    # Check if sshd user already exists...
    import pwd
    try:
        pwd.getpwnam("sshd")
        return
    except KeyError:
        pass
    try:
        # UID/GID 50 to match LFS/BLFS
        cf.bold("Creating user/group 'sshd'")
        self.sudo("install -v -g sys -m700 -d /var/lib/sshd")
        self.sudo("groupadd -g 50 sshd")
        self.sudo("useradd -c 'sshd PrivSep' -d /var/lib/sshd -g sshd -s /bin/false -u 50 sshd")
    except OSError as e:
        cf.yellow(f"Adding user/group 'sshd' failed: {e}")
