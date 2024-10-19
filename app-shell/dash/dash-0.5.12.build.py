#    app-shell/dash/dash-0.5.12.build.py
#    Fri Oct 18 21:02:47 UTC 2024
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
    cf.do_bin(f"{self.seg_dir}/bin/dash", cf.paths['b'])
    cf.do_man(f"{self.seg_dir}share/man/man1/dash.1", cf.paths['man1'])


def cleanup_prehook(self):
    print()
    cf.print_yellow("Note: ")
    cf.print_bold("If you want dash to be a link to /bin/sh,\n")
    cf.print_bold("you must make this link yourself. Also, don't\n")
    cf.print_bold("forget to add '/bin/dash' to /etc/shells by running:\n\n")
    print("cat >> /etc/shells << 'EOF'")
    print("/bin/dash")
    print("EOF")
    print()


"""
/bin/dash
/usr/share/man/man1/dash.1.bz2
"""
