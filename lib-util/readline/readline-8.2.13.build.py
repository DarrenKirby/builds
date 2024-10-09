#    lib-util/readline/readline-8.2.13.build.py
#    Wed Oct  9 01:29:57 UTC 2024

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
    os.system("sed -i '/MV.*old/d' Makefile.in")
    os.system("sed -i '/{OLDSUFF}/c:' support/shlib-install")
    os.system("sed -i 's/-Wl,-rpath,[^ ]*//' support/shobj-conf")

    return os.system(f"./configure --prefix={self.seg_dir} --disable-static --with-curses")

def make(self):
    return os.system('make SHLIB_LIBS="-lncursesw"')

def make_install(self):
    return os.system('make SHLIB_LIBS="-lncursesw" install')

def install(self):
    cf.do_lib(f"{self.seg_dir}/lib/libhistory.so.8.2", cf.paths['ul'])
    cf.do_sym(f"{cf.paths['ul']}/libhistory.so.8.2", f"{cf.paths['ul']}/libhistory.so")
    cf.do_sym(f"{cf.paths['ul']}/libhistory.so.8.2", f"{cf.paths['ul']}/libhistory.so.8")
    cf.do_lib(f"{self.seg_dir}/lib/libreadline.so.8.2", cf.paths['ul'])
    cf.do_sym(f"{cf.paths['ul']}/libreadline.so.8.2", f"{cf.paths['ul']}/libreadline.so")
    cf.do_sym(f"{cf.paths['ul']}/libreadline.so.8.2", f"{cf.paths['ul']}/libreadline.so.8")

    # Recursively copy the header directory
    os.system(f"cp -a {self.seg_dir}/include/readline {cf.paths['ui']}/readline")

    cf.do_man(f"{self.seg_dir}/share/man/man3/history.3", cf.paths['man3'])
    cf.do_man(f"{self.seg_dir}/share/man/man3/readlines.3", cf.paths['man3'])

"""
/usr/lib/libhistory.so
/usr/lib/libhistory.so.8
/usr/lib/libhistory.so.8.2
/usr/lib/libreadline.so
/usr/lib/libreadline.so.8
/usr/lib/libreadline.so.8.2
/usr/include/readline
/usr/include/readline/chardefs.h
/usr/include/readline/history.h
/usr/include/readline/keymaps.h
/usr/include/readline/readline.h
/usr/include/readline/rlconf.h
/usr/include/readline/rlstdc.h
/usr/include/readline/rltypedefs.h
/usr/include/readline/tilde.h
"""
