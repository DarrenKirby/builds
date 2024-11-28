#    dev-lib/libiffi/libiffi-3.4.6.build.py
#    Thu Nov 21 16:33:12 UTC 2024

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
    # Prevent static libs
    return self.do("sed -i '/install -m.*STA/d' libcap/Makefile")


def make(self):
    return self.do(f"make {cf.config['makeopts']} prefix={self.seg_dir}/usr lib=lib")


def make_install(self):
    return self.do(f"make prefix={self.seg_dir}/usr lib=lib install")


def install(self):
    pass