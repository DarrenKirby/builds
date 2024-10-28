#    lib-util/liburcu/liburcu-0.14.1.build.py
#    Fri Oct 25 22:14:14 UTC 2024

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



#tarball name does not match package name
def install_source_posthook(self):
    os.rename(f"userspace-rcu-{self.version}", f"liburcu-{self.version}")


def configure(self):
    return os.system(f"./configure --prefix={self.seg_dir} --disable-static")


def make(self):
    return os.system("make")


def make_install(self):
    return os.system("make install")


def install(self):
    cf.do_hdr(f"{self.seg_dir}/include/urcu-bp.h", cf.paths['ui'])
    cf.do_hdr(f"{self.seg_dir}/include/urcu-call-rcu.h", cf.paths['ui'])
    cf.do_hdr(f"{self.seg_dir}/include/urcu-defer.h", cf.paths['ui'])
    cf.do_hdr(f"{self.seg_dir}/include/urcu-flavor.h", cf.paths['ui'])
    cf.do_hdr(f"{self.seg_dir}/include/urcu-pointer.h", cf.paths['ui'])
    cf.do_hdr(f"{self.seg_dir}/include/urcu-qsbr.h", cf.paths['ui'])
    cf.do_hdr(f"{self.seg_dir}/include/urcu.h", cf.paths['ui'])
    cf.do_dir(f"{self.seg_dir}/include/urcu/", f"{cf.paths[ui]}/urcu/")

    cf.do_lib(f"{self.seg_dir}/lib/liburcu-bp.so.8.1.0", cf.paths['ul'])
    cf.do_sym(f"{cf.paths['ul']}/liburcu-bp.so.8.1.0", f"{cf.paths['ul']}/liburcu-bp.so")
    cf.do_sym(f"{cf.paths['ul']}/liburcu-bp.so.8.1.0", f"{cf.paths['ul']}/liburcu-bp.so.8")

    cf.do_lib(f"{self.seg_dir}/lib/liburcu-cds.so.8.1.0", cf.paths['ul'])
    cf.do_sym(f"{cf.paths['ul']}/liburcu-cds.so.8.1.0", f"{cf.paths['ul']}/liburcu-cds.so")
    cf.do_sym(f"{cf.paths['ul']}/liburcu-cds.so.8.1.0", f"{cf.paths['ul']}/liburcu-cds.so.8")

    cf.do_lib(f"{self.seg_dir}/lib/liburcu-common.so.8.1.0", cf.paths['ul'])
    cf.do_sym(f"{cf.paths['ul']}/liburcu-common.so.8.1.0", f"{cf.paths['ul']}/liburcu-common.so")
    cf.do_sym(f"{cf.paths['ul']}/liburcu-common.so.8.1.0", f"{cf.paths['ul']}/liburcu-common.so.8")

    cf.do_lib(f"{self.seg_dir}/lib/liburcu-mb.so.8.1.0", cf.paths['ul'])
    cf.do_sym(f"{cf.paths['ul']}/liburcu-mb.so.8.1.0", f"{cf.paths['ul']}/liburcu-mb.so")
    cf.do_sym(f"{cf.paths['ul']}/liburcu-mb.so.8.1.0", f"{cf.paths['ul']}/liburcu-mb.so.8")

    cf.do_lib(f"{self.seg_dir}/lib/liburcu-memb.so.8.1.0", cf.paths['ul'])
    cf.do_sym(f"{cf.paths['ul']}/liburcu-memb.so.8.1.0", f"{cf.paths['ul']}/liburcu-memb.so")
    cf.do_sym(f"{cf.paths['ul']}/liburcu-memb.so.8.1.0", f"{cf.paths['ul']}/liburcu-memb.so.8")

    cf.do_lib(f"{self.seg_dir}/lib/liburcu-qsbr.so.8.1.0", cf.paths['ul'])
    cf.do_sym(f"{cf.paths['ul']}/liburcu-qsbr.so.8.1.0", f"{cf.paths['ul']}/liburcu-qsbr.so")
    cf.do_sym(f"{cf.paths['ul']}/liburcu-qsbr.so.8.1.0", f"{cf.paths['ul']}/liburcu-qsbr.so.8")

    cf.do_lib(f"{self.seg_dir}/lib/liburcu-signal.so.8.1.0", cf.paths['ul'])
    cf.do_sym(f"{cf.paths['ul']}/liburcu-signal.so.8.1.0", f"{cf.paths['ul']}/liburcu-signal.so")
    cf.do_sym(f"{cf.paths['ul']}/liburcu-signal.so.8.1.0", f"{cf.paths['ul']}/liburcu-signal.so.8")

    cf.do_lib(f"{self.seg_dir}/lib/liburcu.so.8.1.0", cf.paths['ul'])
    cf.do_sym(f"{cf.paths['ul']}/liburcu.so.8.1.0", f"{cf.paths['ul']}/liburcu.so")
    cf.do_sym(f"{cf.paths['ul']}/liburcu.so.8.1.0", f"{cf.paths['ul']}/liburcu.so.8")


"""
/usr/include/urcu-bp.h
/usr/include/urcu-call-rcu.h
/usr/include/urcu-defer.h
/usr/include/urcu-flavor.h
/usr/include/urcu-pointer.h
/usr/include/urcu-qsbr.h
/usr/include/urcu.h
/usr/include/urcu/
/usr/include/urcu/arch.h
/usr/include/urcu/assert.h
/usr/include/urcu/call-rcu.h
/usr/include/urcu/cds.h
/usr/include/urcu/compiler.h
/usr/include/urcu/config.h
/usr/include/urcu/debug.h
/usr/include/urcu/defer.h
/usr/include/urcu/flavor.h
/usr/include/urcu/futex.h
/usr/include/urcu/hlist.h
/usr/include/urcu/lfstack.h
/usr/include/urcu/list.h
/usr/include/urcu/pointer.h
/usr/include/urcu/rcuhlist.h
/usr/include/urcu/rculfhash.h
/usr/include/urcu/rculfqueue.h
/usr/include/urcu/rculfstack.h
/usr/include/urcu/rculist.h
/usr/include/urcu/ref.h
/usr/include/urcu/syscall-compat.h
/usr/include/urcu/system.h
/usr/include/urcu/tls-compat.h
/usr/include/urcu/uatomic.h
/usr/include/urcu/uatomic_arch.h
/usr/include/urcu/urcu-bp.h
/usr/include/urcu/urcu-futex.h
/usr/include/urcu/urcu-mb.h
/usr/include/urcu/urcu-memb.h
/usr/include/urcu/urcu-poll.h
/usr/include/urcu/urcu-qsbr.h
/usr/include/urcu/urcu-signal.h
/usr/include/urcu/urcu.h
/usr/include/urcu/urcu_ref.h
/usr/include/urcu/wfcqueue.h
/usr/include/urcu/wfqueue.h
/usr/include/urcu/wfstack.h
/usr/include/urcu/arch/
/usr/include/urcu/arch/aarch64.h
/usr/include/urcu/arch/alpha.h
/usr/include/urcu/arch/arm.h
/usr/include/urcu/arch/gcc.h
/usr/include/urcu/arch/generic.h
/usr/include/urcu/arch/hppa.h
/usr/include/urcu/arch/ia64.h
/usr/include/urcu/arch/loongarch.h
/usr/include/urcu/arch/m68k.h
/usr/include/urcu/arch/mips.h
/usr/include/urcu/arch/nios2.h
/usr/include/urcu/arch/ppc.h
/usr/include/urcu/arch/riscv.h
/usr/include/urcu/arch/s390.h
/usr/include/urcu/arch/sparc64.h
/usr/include/urcu/arch/tile.h
/usr/include/urcu/arch/x86.h
/usr/include/urcu/map/
/usr/include/urcu/map/clear.h
/usr/include/urcu/map/urcu-bp.h
/usr/include/urcu/map/urcu-mb.h
/usr/include/urcu/map/urcu-memb.h
/usr/include/urcu/map/urcu-qsbr.h
/usr/include/urcu/map/urcu-signal.h
/usr/include/urcu/map/urcu.h
/usr/include/urcu/static/
/usr/include/urcu/static/lfstack.h
/usr/include/urcu/static/pointer.h
/usr/include/urcu/static/rculfqueue.h
/usr/include/urcu/static/rculfstack.h
/usr/include/urcu/static/urcu-bp.h
/usr/include/urcu/static/urcu-common.h
/usr/include/urcu/static/urcu-mb.h
/usr/include/urcu/static/urcu-memb.h
/usr/include/urcu/static/urcu-qsbr.h
/usr/include/urcu/static/urcu-signal-nr.h
/usr/include/urcu/static/urcu-signal.h
/usr/include/urcu/static/urcu.h
/usr/include/urcu/static/wfcqueue.h
/usr/include/urcu/static/wfqueue.h
/usr/include/urcu/static/wfstack.h
/usr/include/urcu/uatomic/
/usr/include/urcu/uatomic/aarch64.h
/usr/include/urcu/uatomic/alpha.h
/usr/include/urcu/uatomic/arm.h
/usr/include/urcu/uatomic/gcc.h
/usr/include/urcu/uatomic/generic.h
/usr/include/urcu/uatomic/hppa.h
/usr/include/urcu/uatomic/ia64.h
/usr/include/urcu/uatomic/loongarch.h
/usr/include/urcu/uatomic/m68k.h
/usr/include/urcu/uatomic/mips.h
/usr/include/urcu/uatomic/nios2.h
/usr/include/urcu/uatomic/ppc.h
/usr/include/urcu/uatomic/riscv.h
/usr/include/urcu/uatomic/s390.h
/usr/include/urcu/uatomic/sparc64.h
/usr/include/urcu/uatomic/tile.h
/usr/include/urcu/uatomic/x86.h
/usr/lib/liburcu-bp.so
/usr/lib/liburcu-bp.so.8
/usr/lib/liburcu-bp.so.8.1.0
/usr/lib/liburcu-cds.so
/usr/lib/liburcu-cds.so.8
/usr/lib/liburcu-cds.so.8.1.0
/usr/lib/liburcu-common.so
/usr/lib/liburcu-common.so.8
/usr/lib/liburcu-common.so.8.1.0
/usr/lib/liburcu-mb.so
/usr/lib/liburcu-mb.so.8
/usr/lib/liburcu-mb.so.8.1.0
/usr/lib/liburcu-memb.so
/usr/lib/liburcu-memb.so.8
/usr/lib/liburcu-memb.so.8.1.0
/usr/lib/liburcu-qsbr.so
/usr/lib/liburcu-qsbr.so.8
/usr/lib/liburcu-qsbr.so.8.1.0
/usr/lib/liburcu-signal.so
/usr/lib/liburcu-signal.so.8
/usr/lib/liburcu-signal.so.8.1.0
/usr/lib/liburcu.so
/usr/lib/liburcu.so.8
/usr/lib/liburcu.so.8.1.0
"""
