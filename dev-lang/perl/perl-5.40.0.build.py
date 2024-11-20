#    dev-lang/perl/perl-5.40.0.build.py
#    Wed Nov 20 03:10:18 UTC 2024

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
    return os.system("sh Configure -des "
                     "-D prefix=/usr "
                     "-D vendorprefix=/usr "
                     "-D privlib=/usr/lib/perl5/5.40/core_perl "
                     "-D archlib=/usr/lib/perl5/5.40/core_perl "
                     "-D sitelib=/usr/lib/perl5/5.40/site_perl "
                     "-D sitearch=/usr/lib/perl5/5.40/site_perl "
                     "-D vendorlib=/usr/lib/perl5/vendor_perl "
                     "-D vendorarch=/usr/lib/perl5/vendor_perl "
                     "-D man1dir=/usr/share/man/man1 "
                     "-D man3dir=/usr/share/man/man3 "
                     "-D pager='/usr/bin/less -isR' "
                     "-D useshrplib "
                     "-D usethreads")

def make(self):
    return os.system(f"make {cf.config['makeopts']}")


def make_install(self):
    return os.system(f"make install DESTDIR={self.seg_dir}")


def install(self):
    for file in os.listdir(self.p['_ub']):
        if file in ["perl"]:
            self.inst_binary(f"{self.p['_ub']}/{file}", self.p['ub'])
        else:
            self.inst_script(f"{self.p['_ub']}/{file}", self.p['ub'])

    self.inst_directory(f"{self.p['_ul']}/perl5/", f"{self.p['ul']}/perl5/")

    for file in os.listdir(self.p['_man1']):
        # hardlink to perlthanks.1
        if file not in ['perlbug.1']:
            self.inst_manpage(f"{self.p['_man1']}/{file}", self.p['man1'])
    self.inst_symlink(f"{self.p['man1']}/perlthanks.1.bz2", f"{self.p['man1']}/perlbug.1")

    for file in os.listdir(self.p['_man3']):
        self.inst_manpage(f"{self.p['_man3']}/{file}", self.p['man3'])
