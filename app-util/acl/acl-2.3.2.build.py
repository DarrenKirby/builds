#    app-util/acl/acl-2.3.2.build.py
#    Mon Oct 21 18:02:24 UTC 2024

#    Copyright:: (c) 2024 Darren
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
    return os.system(f"./configure --prefix={self.seg_dir} --disable-static")


def make(self):
    return os.system("make")


def make_install(self):
    return os.system("make install")


def install(self):
    cf.do_bin(f"{self.seg_dir}/bin/", cf.paths['ub'])
    cf.do_bin(f"{self.seg_dir}/bin/", cf.paths['ub'])
    cf.do_bin(f"{self.seg_dir}/bin/", cf.paths['ub'])

    os.mkdir("/usr/include/acl", 0o755)
    cf.do_hdr(f"{self.seg_dir}/include/acl/libacl.h", f"{cf.paths['ui']}/acl/")
    cf.do_hdr(f"{self.seg_dir}/include/sys/acl.h", f"{cf.paths['ui']}/sys/")

    cf.do_lib(f"{self.seg_dir}/lib/libacl.so.1.1.2302", cf.paths['ul'])
    cf.do_sym(f"{cf.paths['ul']}/libacl.so.1.1.2302", f"{cf.paths['ul']}/libacl.so.1")
    cf.do_sym(f"{cf.paths['ul']}/libacl.so.1.1.2302", f"{cf.paths['ul']}/libacl.so")

    cf.do_man(f"{self.seg_dir}/share/man/man1/chacl.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/getfacl.1", cf.paths['man1'])
    cf.do_man(f"{self.seg_dir}/share/man/man1/setfacl.1", cf.paths['man1'])

    for manpage in glob.glob(f"{self.seg_dir}/share/man/man3/acl_*.3"):
        cf.do_man(manpage, cf.paths['man3'])

    cf.do_man(f"{self.seg_dir}/share/man/man5/acl.5", cf.paths['man5'])



"""
/usr/bin/chacl
/usr/bin/getfacl
/usr/bin/setfacl
/usr/include/acl/libacl.h
/usr/include/sys/acl.h
/usr/lib/libacl.so
/usr/lib/libacl.so.1
/usr/lib/libacl.so.1.1.2302
/usr/share/man/man1/chacl.1.bz2
/usr/share/man/man1/getfacl.1.bz2
/usr/share/man/man1/setfacl.1.bz2
/usr/share/man/man3/acl_add_perm.3.bz2
/usr/share/man/man3/acl_calc_mask.3.bz2
/usr/share/man/man3/acl_check.3.bz2
/usr/share/man/man3/acl_clear_perms.3.bz2
/usr/share/man/man3/acl_cmp.3.bz2
/usr/share/man/man3/acl_copy_entry.3.bz2
/usr/share/man/man3/acl_copy_ext.3.bz2
/usr/share/man/man3/acl_copy_int.3.bz2
/usr/share/man/man3/acl_create_entry.3.bz2
/usr/share/man/man3/acl_delete_def_file.3.bz2
/usr/share/man/man3/acl_delete_entry.3.bz2
/usr/share/man/man3/acl_delete_perm.3.bz2
/usr/share/man/man3/acl_dup.3.bz2
/usr/share/man/man3/acl_entries.3.bz2
/usr/share/man/man3/acl_equiv_mode.3.bz2
/usr/share/man/man3/acl_error.3.bz2
/usr/share/man/man3/acl_extended_fd.3.bz2
/usr/share/man/man3/acl_extended_file.3.bz2
/usr/share/man/man3/acl_extended_file_nofollow.3.bz2
/usr/share/man/man3/acl_free.3.bz2
/usr/share/man/man3/acl_from_mode.3.bz2
/usr/share/man/man3/acl_from_text.3.bz2
/usr/share/man/man3/acl_get_entry.3.bz2
/usr/share/man/man3/acl_get_fd.3.bz2
/usr/share/man/man3/acl_get_file.3.bz2
/usr/share/man/man3/acl_get_perm.3.bz2
/usr/share/man/man3/acl_get_permset.3.bz2
/usr/share/man/man3/acl_get_qualifier.3.bz2
/usr/share/man/man3/acl_get_tag_type.3.bz2
/usr/share/man/man3/acl_init.3.bz2
/usr/share/man/man3/acl_set_fd.3.bz2
/usr/share/man/man3/acl_set_file.3.bz2
/usr/share/man/man3/acl_set_permset.3.bz2
/usr/share/man/man3/acl_set_qualifier.3.bz2
/usr/share/man/man3/acl_set_tag_type.3.bz2
/usr/share/man/man3/acl_size.3.bz2
/usr/share/man/man3/acl_to_any_text.3.bz2
/usr/share/man/man3/acl_to_text.3.bz2
/usr/share/man/man3/acl_valid.3.bz2
/usr/share/man/man5/acl.5.bz2
"""
