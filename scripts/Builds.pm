# /usr/constructs/scripts/Constructs.pm
# Sun Oct 19 04:28:01 UTC 2014
#
#

package Builds;
require Exporter;

our @ISA     = qw(Exporter);
our @EXPORT  = qw(bold green yellow red $builds $distfiles $conf
                  $b $s $ub $us $ui $ul $ulb $uls $uli $ull
                  $man1 $man2 $man3 $man4 $man5 $man6 $man7 $man8
                  $ins_bin $ins_scr $ins_lib $ins_hdr $ins_man);


# Useful variables used by all builds. These are
# theoretically hackable to systemwide effect

# general paths
$builds    = "/usr/builds";
$distfiles = "/usr/ports/distfiles";
$conf      = "/etc/build.conf";

# Install paths
$b   = "/bin";
$s   = "/sbin";
$l   = "/lib";
$ub  = "/usr/bin";
$us  = "/usr/sbin";
$ui  = "/usr/include";
$ul  = "/usr/lib";
$ulb = "/usr/local/bin";
$uls = "/usr/local/sbin";
$uli = "/usr/local/include";
$ull = "/usr/local/lib";

# Man paths
$man1 = "/usr/share/man/man1";
$man2 = "/usr/share/man/man2";
$man3 = "/usr/share/man/man3";
$man4 = "/usr/share/man/man4";
$man5 = "/usr/share/man/man5";
$man6 = "/usr/share/man/man6";
$man7 = "/usr/share/man/man7";
$man8 = "/usr/share/man/man8";

# Common options for 'install'
$ins_bin = "install -v -o root -g root -m 755 -s";
$ins_scr = "install -v -o root -g root -m 755";
$ins_lib = "install -v -o root -g root -m 755";
$ins_hdr = "install -v -o root -g root -m 644";
$ins_man = "install -v -o root -g root -m 644";

# Functions used globally
#


# Coloured output
sub bold {
    system('echo -en $"\\033[1;37m"');
    print ">>> " . $_[0];
    system('echo -en $"\\033[0;39m"');
}

sub green {
    system('echo -en $"\\033[0;32m"');
    print ">>> " . $_[0];
    system('echo -en $"\\033[0;39m"');
}

sub yellow {
    system('echo -en $"\\033[1;33m"');
    print ">>> " . $_[0];
    system('echo -en $"\\033[0;39m"');
}

sub red {
    system('echo -en $"\\033[1;31m"');
    print ">>> " . $_[0];
    system('echo -en $"\\033[0;39m"');
}


