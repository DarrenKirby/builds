#!/usr/bin/ruby

#    /usr/builds/scripts/initialize_builds_tree.rb
#    Fri Oct 24 22:04:05 UTC 2014

#    A simple script to initialize the builds source building tree
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


require 'etc'
require 'dbm'
require 'csv'
require 'fileutils'

$builds_root = "/home/bulliver/code/builds"

#if Etc.getlogin != "root"
#    puts "you must be root to run this script"
#    exit 1
#end

if File.exists? "#{$builds_root}/scripts/builds.db"
    puts "db already initialized. To re-initialize please"
    puts "delete #{$builds_root}/scripts/builds.dbm manually"
    puts "and run this script again"
end

#Install 'bld' into PATH
#Fileutils.remove_file("/usr/bin/bld", force = true)
#Fileutils.cp("#{$builds_root}/scripts/bld","/usr/bin/bld")

db = DBM.open("#{$builds_root}/scripts/builds", 0660, DMB::NEWDB)
CSV.foreach("#{$builds_root}/scripts/builds.csv") do |row|
    db[row.shift] = row.join(",")
end
