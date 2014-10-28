#    /usr/builds/scripts/SearchPackage.rb
#    Tue Oct 28 02:42:41 UTC 2014

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

require 'gdbm'

def do_search(str)
    found = false
    db = GDBM.open("#{$builds_root}/scripts/builds.db", 0666, GDBM::READER)
    db.each_key do |key|
        if key.include? str
            a = db.fetch(key).split(",")
            print "Category/Name: "; green(a[0])
            print "  Description: "; green(a[5])
            print "      Version: "; green(a[1])
            print "     Homepage: "; green(a[4])
            puts
            found = true
        end
    end
    db.close
    unless found
        bold("no match for '#{str}'")
    end
    exit 0
end
