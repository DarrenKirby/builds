#    dev-tool/autoconf/autoconf-2.7.2.build.py
#    Wed Oct 23 01:38:36 UTC 2024

#    Copyright:: (c) 2024 Darren Kirby
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
    return os.system(f"./configure --prefix={self.seg_dir}")


def make(self):
    return os.system("make")


def make_install(self):
    return os.system("make install")


def install(self):
    cf.do_bin(f"{self.seg_dir}/bin/", cf.paths['ub'])
    cf.do_bin(f"{self.seg_dir}/bin/", cf.paths['ub'])
    cf.do_bin(f"{self.seg_dir}/bin/", cf.paths['ub'])
    cf.do_bin(f"{self.seg_dir}/bin/", cf.paths['ub'])
    cf.do_bin(f"{self.seg_dir}/bin/", cf.paths['ub'])
    cf.do_bin(f"{self.seg_dir}/bin/", cf.paths['ub'])
    cf.do_bin(f"{self.seg_dir}/bin/", cf.paths['ub'])

    cf.do_dir(f"{self.seg_dir}/share/autoconf/", f"{cf.paths['ush']}/autoconf")

    cf.do_man(f"{self.seg_dir}/share/man/man1/autoconf.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/autoheader.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/autom4te.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/autoreconf.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/autoscan.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/autoupdate.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/ifnames.1", cf.paths['man1'])


"""
/usr/bin/autoconf
/usr/bin/autoheader
/usr/bin/autom4te
/usr/bin/autoreconf
/usr/bin/autoscan
/usr/bin/autoupdate
/usr/bin/ifnames
/usr/share/autoconf/
/usr/share/autoconf/INSTALL
/usr/share/autoconf/autom4te.cfg
/usr/share/autoconf/version.m4
/usr/share/autoconf/Autom4te/
/usr/share/autoconf/Autom4te/C4che.pm
/usr/share/autoconf/Autom4te/ChannelDefs.pm
/usr/share/autoconf/Autom4te/Channels.pm
/usr/share/autoconf/Autom4te/Config.pm
/usr/share/autoconf/Autom4te/Configure_ac.pm
/usr/share/autoconf/Autom4te/FileUtils.pm
/usr/share/autoconf/Autom4te/General.pm
/usr/share/autoconf/Autom4te/Getopt.pm
/usr/share/autoconf/Autom4te/Request.pm
/usr/share/autoconf/Autom4te/XFile.pm
/usr/share/autoconf/autoconf/
/usr/share/autoconf/autoconf/autoconf.m4
/usr/share/autoconf/autoconf/autoconf.m4f
/usr/share/autoconf/autoconf/autoheader.m4
/usr/share/autoconf/autoconf/autoscan.m4
/usr/share/autoconf/autoconf/autotest.m4
/usr/share/autoconf/autoconf/autoupdate.m4
/usr/share/autoconf/autoconf/c.m4
/usr/share/autoconf/autoconf/erlang.m4
/usr/share/autoconf/autoconf/fortran.m4
/usr/share/autoconf/autoconf/functions.m4
/usr/share/autoconf/autoconf/general.m4
/usr/share/autoconf/autoconf/go.m4
/usr/share/autoconf/autoconf/headers.m4
/usr/share/autoconf/autoconf/lang.m4
/usr/share/autoconf/autoconf/libs.m4
/usr/share/autoconf/autoconf/oldnames.m4
/usr/share/autoconf/autoconf/programs.m4
/usr/share/autoconf/autoconf/specific.m4
/usr/share/autoconf/autoconf/status.m4
/usr/share/autoconf/autoconf/trailer.m4
/usr/share/autoconf/autoconf/types.m4
/usr/share/autoconf/autoscan/
/usr/share/autoconf/autoscan/autoscan.list
/usr/share/autoconf/autotest/
/usr/share/autoconf/autotest/autotest.m4
/usr/share/autoconf/autotest/autotest.m4f
/usr/share/autoconf/autotest/general.m4
/usr/share/autoconf/autotest/specific.m4
/usr/share/autoconf/build-aux/
/usr/share/autoconf/build-aux/config.guess
/usr/share/autoconf/build-aux/config.sub
/usr/share/autoconf/build-aux/install-sh
/usr/share/autoconf/m4sugar/
/usr/share/autoconf/m4sugar/foreach.m4
/usr/share/autoconf/m4sugar/m4sh.m4
/usr/share/autoconf/m4sugar/m4sh.m4f
/usr/share/autoconf/m4sugar/m4sugar.m4
/usr/share/autoconf/m4sugar/m4sugar.m4f
/usr/share/man/man1/autoconf.1.bz2
/usr/share/man/man1/autoheader.1.bz2
/usr/share/man/man1/autom4te.1.bz2
/usr/share/man/man1/autoreconf.1.bz2
/usr/share/man/man1/autoscan.1.bz2
/usr/share/man/man1/autoupdate.1.bz2
/usr/share/man/man1/ifnames.1.bz2
"""
