#    /usr/builds/scripts/DepResolve.rb
#    Sat Oct 25 01:21:41 UTC 2014

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

require 'CommonFunctions'
require 'gdbm'

def resolve_dependancies(args)
    db = GDBM.open("#{$builds_root}/scripts/builds.db", 0666, GDBM::READER)
    atoms = []
    packages_to_build = []
    args.each do |arg|
        if arg.include? "/"
            atoms << arg
        else
            if db.has_key?(arg)
                atoms << db[arg].split(",")[0]
            else
                red("'#{arg}' does not appear to be a valid package name")
                yellow("try \"#{APPNAME} search 'package'\"")
                exit 1
            end
        end
    end
    db.close
    # This is a _REALLY_ naive implementation of a dependancy tree
    # This will have to be refactored and improved when the rest
    # of the scaffolding is up...
    atoms.each do |atom|
        build_file = Dir.glob("#{$builds_root}/#{atom}/*.build")
        File.readlines(build_file[0]).each do |line|
            if line.include? "depend"
                packages_to_build += line.split[-1][1..-2].split(",")
                break
            end
        end
    end
    packages_to_build += atoms
end
