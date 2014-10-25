#    /usr/builds/scripts/Builds.rb
#    Sun Oct 19 03:34:12 UTC 2014

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


APPNAME    = "bld"
APPVERSION = "0.0.1"
QUIP       = "By far the best software available for turtle stacking"

KNOWN_COMMANDS = %w[install uninstall search info]

require 'CommonFunctions'
require 'BuildPackage'

def process_cliopts()
    require 'getoptlong'
    cliopts = GetoptLong.new(
    [ "--help",         "-h",  GetoptLong::NO_ARGUMENT ],
    [ "--fetch",        "-f",  GetoptLong::NO_ARGUMENT ],
    [ "--pretend",      "-p",  GetoptLong::NO_ARGUMENT ],
    [ "--ask",          "-a",  GetoptLong::NO_ARGUMENT ],
    )
    cliopts.quiet = TRUE
    begin
        cliopts.each do |opt, arg|
            show_usage if ( opt == '-h' ) || ( opt == '--help' )
        end
    rescue GetoptLong::InvalidOption
        yellow("#{cliopts.error_message}")
        yellow("Hint: try '#{APPNAME} --help' for usage details")
        puts
        exit 1
    rescue GetoptLong::NeedlessArgument
        yellow("#{cliopts.error_message}")
        yellow("Hint: try '#{APPNAME} --help' for usage details")
        puts
        exit 1
    rescue GetoptLong::MissingArgument
        yellow("#{cliopts.error_message}")
        yellow("Hint: try '#{APPNAME} --help' for usage details")
        puts
        exit 1
    end
    command = ARGV.shift
    argv = ARGV
    return command, argv
end

def do_main()
    puts "#{APPNAME} version #{APPVERSION} (#{QUIP})"
    puts "Written by Darren Kirby :: d@curseofknowledge.com :: http://www.curseofknowledge.com/unix/bld/"
    puts "Released under the GPL"
    puts
    command, args = process_cliopts()
    unless KNOWN_COMMANDS.include? command
        yellow("no such command: '#{command}'")
        yellow("Hint: try '#{APPNAME} --help' for usage details")
    end
    if (command == "search") || (command == "info") && (args.length > 1)
        yellow("'#{command}' can only operate on one pkg_atom at a time")
        yellow("Hint: try '#{APPNAME} --help' for usage details")
    end
    if command == "search"

        do_search(args[0])
    elsif command == "info"
        do_info(args[0])
    elsif command == "uninstall"
        do_uninstall(args[0])
    else
        require 'DepResolve'
        builds_to_build = resolve_dependancies(args)
    end
    builds_to_build.each do |build|
        bold("starting build for #{build}")
        bld = BuildPackage.new(build)
        green("Fetching package")
        bld.fetch()
        green("fetch complete")
    end
    #puts command
    #puts args
    #puts $man1
end

