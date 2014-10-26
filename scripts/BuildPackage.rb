#    /usr/builds/scripts/BuildPackage.rb
#    Sat Oct 25 18:27:06 UTC 2014

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

class BuildPackage
    def initialize(build)
        @build = build
        @name = build.split("/")[1]
        db = GDBM.open("#{$builds_root}/scripts/builds.db", 0666, GDBM::READER)
        a = db[@name].split(",")
        db.close()
        @version = a[1]
        @md5sum  = a[2]
        @src_url = a[3]
        resolve_paths
        load @build_file
    end

    def fetch
        Dir.chdir($distfiles)
        unless File.exists? @package
            Thread.new {
                fd = File.open($logfile, "a")
                fd.write("#{Time.now.asctime} >>> downloading #{@package}\n")
                fd.close
            }
            system("wget #{@src_url}")
        else
            bold("nothing to download...")
        end
        if `md5sum #{@package}`.split[0] == @md5sum
            green("md5sums match ;-)")
        else
            red("md5sums do not match!")
            exit 1
        end
    end

    def install_source
        Dir.mkdir(@work_dir)
        Dir.chdir(@work_dir)
        unless system("tar xf #{$distfiles}/#{@package} -C .")
            red("install source failed!")
            exit 1
        end

    end

    def configure
    end

    def make
    end

    def make_install
    end

    def install
    end

    def clean
    end
    private

    def resolve_paths
        @build_dir = "#{$builds_root}/#{@build}"
        @build_file = "#{@build_dir}/#{@name}-#{@version}.build"
        @work_dir = "#{$builds_root}/#{@build}/work"
        @src_url.count("VVV").times do
            @src_url.gsub!("VVV", @version)
        end
        @package = @src_url.split("/")[-1]
    end
end

