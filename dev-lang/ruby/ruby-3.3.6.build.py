#    dev-lang/ruby/ruby-3.3.6.build.py
#    Wed Nov 27 05:07:28 UTC 2024

#    Copyright:: (c) 2024
#    Author:: Darren Kirby (mailto:Darren Kirby)

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

depend = "dev-lib/libyaml"


def configure(self):
    return os.system("./configure --prefix=/usr "
                     "--disable-static "
                     "--disable-rpath "
                     "--enable-shared "
                     "--without-valgrind "
                     "--without-baseruby "
                     "ac_cv_func_qsort_r=no")


def make(self):
    return os.system(f"make {cf.config['makeopts']}")


def make_install(self):
    return os.system(f"make DESTDIR={self.seg_dir} install")


def install(self):
    pass
