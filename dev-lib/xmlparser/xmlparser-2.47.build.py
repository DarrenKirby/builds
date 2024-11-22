#    dev-lib/xmlparser/xmlparser-2.47.build.py
#    Fri Nov 22 00:54:16 UTC 2024

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
    # non-standard source tree name
    cf.bold(f" Renaming XML-Parser-{self.version} to {self.package_dir}")
    os.rename(f"XML-Parser-{self.version}", self.package_dir)

def configure(self):
    return os.system(f"perl Makefile.PL EXPATLIBPATH={self.p['ui']} EXPATINCPATH={self.p['ui']}")


def make(self):
    return os.system("make")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} install")


def install(self):
    pass

