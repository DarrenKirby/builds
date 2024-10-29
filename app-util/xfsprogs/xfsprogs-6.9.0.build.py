#    app-util/xfsprogs/xfsprogs-6.9.0.build.py
#    Tue Oct 29 21:39:35 UTC 2024

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



depend="dev-lib/inih,lib-util/liburcu"


def configure(self):
    return os.system(f"./configure --prefix={self.seg_dir} --enable-static=no")


def make(self):
    # BUG: This hack will likely break on systemd systems,
    # or to be sure, it won't fix the underlying issue.
    # Prevent install script from installing xfs.rules to
    # /usr/lib/udev/rules.d/
    os.system("sed -i -e 's/install-udev//' scrub/Makefile")
    return os.system("make DEBUG=-DNDEBUG")


def make_install(self):
    return os.system("make install")


def install(self):
    cf.do_lib(f"{self.seg_dir}/lib64/libhandle.so.1.0.3", cf.paths['ul'])
    cf.do_sym(f"{cf.paths['ul']}/libhandle.so.1.0.3", f"{cf.paths['ul']}/libhandle.so.1")

    for file in os.listdir("./app-util/xfsprogs/work/seg/sbin"):
        cf.do_bin(f"{self.seg_dir}/sbin/{file}", cf.paths['us'])

    cf.do_man(f"{self.seg_dir}/share/man/man5/projects.5", cf.paths['man5'])
    cf.do_man(f"{self.seg_dir}/share/man/man5/projid.5", cf.paths['man5'])
    cf.do_man(f"{self.seg_dir}/share/man/man5/xfs.5", cf.paths['man5'])


    for file in os.listdir("./app-util/xfsprogs/work/seg/share/man/man8"):
        cf_do_man(f"{self.seg_dir}/share/man/man8/{file}", cf.paths['man8'])

    cf.do_dir(f"{self.seg_dir}/share/xfsprogs/", f"{cf.paths['ush']}/xfsprogs/")

    # Install xfs.rules to /usr/lib/udev/rules.d
    # Using 'do_hdr' as it installs with 644 perms
    cf.do_hdr("./scrub/xfs.rules", f"{cf.paths['ul']}/udev/rules.d/64-xfs.rules")


"""
/usr/sbin/fsck.xfs
/usr/sbin/mkfs.xfs
/usr/sbin/xfs_admin
/usr/sbin/xfs_bmap
/usr/sbin/xfs_copy
/usr/sbin/xfs_db
/usr/sbin/xfs_estimate
/usr/sbin/xfs_freeze
/usr/sbin/xfs_fsr
/usr/sbin/xfs_growfs
/usr/sbin/xfs_info
/usr/sbin/xfs_io
/usr/sbin/xfs_logprint
/usr/sbin/xfs_mdrestore
/usr/sbin/xfs_metadump
/usr/sbin/xfs_mkfile
/usr/sbin/xfs_ncheck
/usr/sbin/xfs_quota
/usr/sbin/xfs_repair
/usr/sbin/xfs_rtcp
/usr/sbin/xfs_scrub
/usr/sbin/xfs_scrub_all
/usr/sbin/xfs_spaceman
/usr/share/man/man5/projects.5.bz2
/usr/share/man/man5/projid.5.bz2
/usr/share/man/man5/xfs.5.bz2
/usr/share/man/man8/fsck.xfs.8.bz2
/usr/share/man/man8/mkfs.xfs.8.bz2
/usr/share/man/man8/xfs_admin.8.bz2
/usr/share/man/man8/xfs_bmap.8.bz2
/usr/share/man/man8/xfs_copy.8.bz2
/usr/share/man/man8/xfs_db.8.bz2
/usr/share/man/man8/xfs_estimate.8.bz2
/usr/share/man/man8/xfs_freeze.8.bz2
/usr/share/man/man8/xfs_fsr.8.bz2
/usr/share/man/man8/xfs_growfs.8.bz2
/usr/share/man/man8/xfs_info.8.bz2
/usr/share/man/man8/xfs_io.8.bz2
/usr/share/man/man8/xfs_logprint.8.bz2
/usr/share/man/man8/xfs_mdrestore.8.bz2
/usr/share/man/man8/xfs_metadump.8.bz2
/usr/share/man/man8/xfs_mkfile.8.bz2
/usr/share/man/man8/xfs_ncheck.8.bz2
/usr/share/man/man8/xfs_quota.8.bz2
/usr/share/man/man8/xfs_repair.8.bz2
/usr/share/man/man8/xfs_rtcp.8.bz2
/usr/share/man/man8/xfs_scrub.8.bz2
/usr/share/man/man8/xfs_scrub_all.8.bz2
/usr/share/man/man8/xfs_spaceman.8.bz2
/usr/share/xfsprogs/
/usr/share/xfsprogs/xfs_scrub_all.cron
/usr/share/xfsprogs/mkfs/
/usr/share/xfsprogs/mkfs/dax_x86_64.conf
/usr/share/xfsprogs/mkfs/lts_4.19.conf
/usr/share/xfsprogs/mkfs/lts_5.10.conf
/usr/share/xfsprogs/mkfs/lts_5.15.conf
/usr/share/xfsprogs/mkfs/lts_5.4.conf
/usr/share/xfsprogs/mkfs/lts_6.1.conf
/usr/share/xfsprogs/mkfs/lts_6.6.conf
"""
