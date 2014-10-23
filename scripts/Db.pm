#    /usr/builds/scripts/Db.pm
#    Sun Oct 19 23:28:35 UTC 2014
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


package Db;
require Exporter;

our @ISA     = qw(Exporter);
our @EXPORT  = qw(format_time $db_path);

use vars       qw($db_path);

$db_path    = "/var/lib/builds";

sub add_to_db {

}

sub retrieve_from_db {

}

sub format_time {
    my $elapsed = shift(@_);
    my $one_min  = 60;
    my $one_hour = 3600;

    if ($elapsed < 60) {
        return "$elapsed seconds";
    } else {
        my $minutes = $elapsed / $one_min;
        my $seconds = $elapsed - ($minutes * $one_min);
        return "$minutes minutes and $seconds seconds";
    }
}
