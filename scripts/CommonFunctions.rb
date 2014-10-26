#    /usr/builds/scripts/CommonFunctions.rb
#    Fri Oct 24 19:29:21 UTC 2014

#    Helper module for the builds source building tree
#
#    Copyright:: (c) 2014 Darren Kirby
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
#

$distfiles = "#{$builds_root}/distfiles"
$conf      = "/etc/build.conf"
$logfile   = "#{$builds_root}/builds.log"

# Install paths
$b   = "/bin"
$s   = "/sbin"
$l   = "/lib"
$ub  = "/usr/bin"
$us  = "/usr/sbin"
$ui  = "/usr/include"
$ul  = "/usr/lib"
$ulb = "/usr/local/bin"
$uls = "/usr/local/sbin"
$uli = "/usr/local/include"
$ull = "/usr/local/lib"

# Man paths
$man1 = "/usr/share/man/man1"
$man2 = "/usr/share/man/man2"
$man3 = "/usr/share/man/man3"
$man4 = "/usr/share/man/man4"
$man5 = "/usr/share/man/man5"
$man6 = "/usr/share/man/man6"
$man7 = "/usr/share/man/man7"
$man8 = "/usr/share/man/man8"

# Common options for 'install'
$ins_bin = "install -v -o root -g root -m 755 -s"
$ins_scr = "install -v -o root -g root -m 755"
$ins_lib = "install -v -o root -g root -m 755"
$ins_hdr = "install -v -o root -g root -m 644"
$ins_man = "install -v -o root -g root -m 644"

# Coloured output
def bold(msg)
    system('echo -en $"\\033[1;37m"')
    puts ">>>  #{msg}"
    system('echo -en $"\\033[0;39m"')
end

def green(msg)
    system('echo -en $"\\033[0;32m"')
    puts ">>>  #{msg}"
    system('echo -en $"\\033[0;39m"')
end

def yellow(msg)
    system('echo -en $"\\033[1;33m"')
    puts ">>>  #{msg}"
    system('echo -en $"\\033[0;39m"')
end

def red(msg)
    system('echo -en $"\\033[1;31m"')
    puts ">>> #{msg}"
    system('echo -en $"\\033[0;39m"')
end

def get_elapsed(start, finish)
    seconds = finish - start
    if seconds < 60
        return "#{seconds} seconds"
    else
        minutes = seconds / 60
        seconds = seconds % 60
        return "#{minutes} minute#{minutes > 1 ? "s" : ""} and #{seconds} seconds"
    end
end

def show_usage
  print <<USAGE
Usage: #{APPNAME} [options] command pkg_atom [pkg_atom...]
    General Options:
        '-h'   or '--help'                  show usage details
        '-f'   or '--fetch'                 download packages but do not install
        '-p'   or '--pretend'               only show which packages would be built
        '-a'   or '--ask'                   prompt before building packages

    Commands:
        'install'   pkg_atom [pkg_atom...]  install one or more packages and dependancies
        'uninstall' pkg_atom                uninstall package
        'search'    string                  search the package db for package names matching string
        'info'      pkg_atom                print info on package if installed
USAGE
  exit
end

