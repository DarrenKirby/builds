#    /usr/builds/scripts/Builds.pm
#    Sun Oct 19 04:28:01 UTC 2014

#    Copyright:: (c) 2014 Darren  Kirby
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

use strict;
use warnings;

package Builds;
require Exporter;

our @ISA     = qw(Exporter);
our @EXPORT  = qw(bold green yellow red $builds $distfiles $conf
                  $b $s $ub $us $ui $ul $ulb $uls $uli $ull do_dl
                  $man1 $man2 $man3 $man4 $man5 $man6 $man7 $man8
                  $ins_bin $ins_scr $ins_lib $ins_hdr $ins_man
                  parse_config_file check_md5sum fetch_wrapper
                  install_src_wrapper configure_wrapper make_wrapper
                  make_install_wrapper sys_install_wrapper clean_wrapper
                  get_tokens @valid_commands do_download);

use vars       qw($builds $distfiles $conf $b $s $l $ub $us $ui $ul
                  $ulb $uls $uli $ull $man1 $man2 $man3 $man4 $man5
                  $man6 $man7 $man8 $ins_bin $ins_scr $ins_lib $ins_hdr
                  $ins_man @valid_commands);


# Useful variables used by all builds. These are
# theoretically hackable to systemwide effect

# general paths
$builds    = "/usr/builds";
$distfiles = "$builds/distfiles";
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

# Valid commands
@valid_commands = qw/install fetch install_src configure
                     make make_install sys_install clean/;


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

# Download distfiles
sub do_download {
    if (-e "$distfiles/" . $_[0]) {
        bold "Nothing to fetch...\n";
    } else {
        chdir $distfiles;
        unless (system("wget " . $_[0]) == 0) {
            red "fetch failed\n";
            die;
        }
    }
}

# Check for a config file and parse it if it exists
sub parse_config_file {
    if (-e $conf) {
        require $conf;
    }

    if (defined $cflags) {
        $ENV{'CFLAGS'} = $cflags;
    }
    if (defined $cxxflags) {
        $ENV{'CXXFLAGS'} = $cxxflags;
    }
}

# Make sure downloaded tarballs match what we expect.
sub check_md5sum {
    my @array = split /\s+/, `md5sum $distfiles/$PN`;
    if ($md5sum ne $array[0]) {
        red "md5sums do not match\n";
        die;
    }
    green "md5sums match ;-)\n";
    return 0;
}

# These wrapper functions define the default action for each step.
# Defaults can generally be used if the software follows the usual
# './configure, make, make install' three-step. If special rules or
# commands are needed to build a packages, you can define the non-
# wrapper equivalent in the *.build file and those sub routines will
# replace the default actions. This is a binary operation: either
# the commands in the .build file will run, or the defaults defined
# here will, not a mix of both.

sub fetch_wrapper {
    green "fetching files...\n";

    if (defined &fetch) {
        unless (&fetch() == 0) {
            red "fetch failed!\n";
            die;
        }
    } else {
        do_download($src_url);
    }

    chdir $here;
    check_md5sum();
    green "fetch complete\n";
}

sub install_src_wrapper {
    green "installing source...\n";

    if (defined &install_src) {
        unless (&install_src() == 0) {
            red "source install failed!\n";
            die;
        }
    } else {
        mkdir "build";
        chdir "build";
        unless (system("tar xf $distfiles/$PN -C .") == 0) {
            red "source install failed!\n";
            die;
        }
    }

    green "source installed\n";
}

sub configure_wrapper {
    green "running configure...\n";
    chdir $here . "/build/" . $PD;

    if (defined &configure) {
        unless (&configure() == 0) {
            red "configure failed!\n";
            die;
        }
    } else {
        unless (system("./configure --prefix=$here/build $CONFIG_OPTS") == 0) {
            red "configure failed!\n";
            die;
        }
    }

    green "configure complete\n";
}

sub make_wrapper {
    green "running make...\n";
    chdir $here . "/build/" . $PD;

    if (defined &make) {
        unless (&make() == 0) {
            red "make failed!\n";
            die;
        }
    } else {
        unless (system("make $MAKEOPTS") == 0) {
            red "make failed!\n";
            die;
        }
    }

    green "make complete\n";
}

sub make_install_wrapper {
    green "installing to temporary root...\n";
    chdir $here . "/build/" . $PD;

    if (defined &make_install) {
        unless (&make_install() == 0) {
            red "make install failed!\n";
            die;
        }
    } else {
        unless (system("make install") == 0) {
            red "make install failed!";
            die;
        }
    }
}

# This sub MUST be defined in the build script.
sub sys_install_wrapper {
    green "installing to system...\n";
    chdir $here . "/build/";

    unless (&sys_install() == 0) {
        red "install failed!\n";
        die;
    }
    green "installed files:\n";
    @files = sort(@files);
    foreach my $file (@files) {
        if (-l $file) {
            bold "[L] $file\n";
        } elsif (-d $file) {
            bold "[D] $file\n";
        } else {
            bold "\t$file\n";
        }
    }
    green "install complete\n";
}

sub clean_wrapper {
    green "cleaning up...\n";

    if (defined &clean) {
        unless (&clean() == 0) {
            red "clean failed!\n";
            die;
        }
    } else {
        chdir $here;
        unless (system("rm -rf build") == 0) {
            yellow "clean failed, please remove build directory manually\n";
        }
    }

    green "   done.\n";

    bold "regenerating ld.so.cache...\n";
    unless (system("ldconfig") == 0) {
        yellow "ldconfig failed\n";
        yellow "Package $PD installed, but with issues\n";
    }
}

sub do_all {
    &fetch_wrapper();
    &install_src_wrapper();
    &configure_wrapper();
    &make_wrapper();
    &make_install_wrapper();
    &sys_install_wrapper();
    &clean_wrapper();
}

# This subroutine creates some useful automatic variables.
#   Given 'tar-1.28.build'' and 'tar-1.28.tar.xz':
#   $N  => 'tar'
#   $V  => '1.28'
#   $PD => 'tar-1.28'
#
sub get_tokens {
    my @arr = split /-/, $build;
    # 'tar-1.28.build' => 'tar', '1.28.build'
    $N = $arr[0];
    my @arr2 = split /\./, $arr[1];
    # '1.28.build' => '1', '28', 'build'
    pop @arr2; # Discard 'build'
    $V = join ".", @arr2;
    $PD = join "-", ($N, $V);
}
