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
        # The 'initialize' and 'resolve_paths' methods create a bunch of useful
        # instance variables which can be used in the build scripts.
        # Assuming package 'tar' and source tarball 'tar-1.28.tar.xz' they expand
        # as such (also assuming $builds_root is '/usr/builds'):
        #
        # @build       = 'app-arch/tar'
        # @name        = 'tar'
        # @version     = '1.28'
        # @md5sum      = '49b6306167724fe48f419a33a5beb857'
        # @src_url     = 'http://ftp.gnu.org/gnu/tar/tar-1.28.tar.xz'
        # @build_dir   = '/usr/builds/app-arch/tar'
        # @build_file  = '/usr/builds/app-arch/tar/tar-1.28.build'
        # @work_dir    = '/usr/builds/app-arch/tar/work'
        # @package     = 'tar-1.28.tar.xz'
        # @package_dir = 'tar-1.28'
        #
        # Note that some packages untar to a non-standard directory name, that is, one
        # that cannot be sussed out from the tarball name. In these cases @package_dir
        # will not be correct until the source_install phase, where it is actually un-tarred.
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
        if self.respond_to?(:fetch_pre_hook)
            self.fetch_pre_hook
        end

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

        if self.respond_to?(:fetch_post_hook)
            self.fetch_post_hook
        end
    rescue
        log_fail
        red("fetch failed!")
        exit 1
    end

    def install_source
        if self.respond_to?(:install_source_pre_hook)
            self.send :install_source_pre_hook
        end

        Dir.mkdir(@work_dir)
        Dir.chdir(@work_dir)
        system("tar xf #{$distfiles}/#{@package} -C .")

        if self.respond_to?(:install_source_post_hook)
            self.send :install_source_post_hook
        end
    rescue
        log_fail
        red("install source failed!")
        exit 1
    end

    def configure
        if self.respond_to?(:configure_pre_hook)
            self.configure_pre_hook
        end

        Dir.chdir(@work_dir)
        if File.exists? @package_dir
            Dir.chdir(@package_dir)
        else
            Dir.chdir(get_package_dir())
        end
        system("./configure --prefix=#{@work_dir}")

        if self.respond_to?(:configure_post_hook)
            self.configure_post_hook
        end
    rescue
        log_fail
        red("configure failed!")
        exit 1
    end

    def make
        if self.respond_to?(:make_pre_hook)
            self.make_pre_hook
        end

        system("make")

        if self.respond_to?(:make_post_hook)
            self.make_post_hook
        end
    rescue
        log_fail
        red("make failed!")
        exit 1
    end

    def make_install
        if self.respond_to?(:make_install_pre_hook)
            self.make_install_pre_hook
        end

        system("make install")

        if self.respond_to?(:make_install_post_hook)
            self.make_install_post_hook
        end
    rescue
        log_fail
        red("make install failed!")
        exit 1
    end

    def install
    # MUST be defined in the build file
    rescue
        log_fail
        red("install failed!")
        exit 1
    end

    def clean
        if self.respond_to?(:clean_pre_hook)
            self.clean_pre_hook
        end

        Dir.chdir(@build_dir)
        system("rm -rf work")

        if self.respond_to?(:clean_post_hook)
            self.clean_post_hook
        end
    rescue
        log_fail
        red("clean failed!")
        exit 1
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
        @package_dir = "#{@name}-#{@version}"
    end

    def log_fail
        Thread.new {
            fd = File.open($logfile, "a")
            fd.write("#{Time.now.asctime} !!! build of #{@package} failed: #{Kernel.caller[0]}\n")
            fd.close
        }
    end
end

