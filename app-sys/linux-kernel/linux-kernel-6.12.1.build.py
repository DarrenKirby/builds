#    app-sys/linux-kernel/linux-kernel-6.12.1.build.py
#    Sun Dec  1 18:59:05 UTC 2024

#    Copyright:: (c) 2024
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


def fetch_posthook(self):
    print()
    cf.print_green(f"The sources for linux-{self.version} have been downloaded to: ")
    cf.print_bold(f"{cf.config['distfiles']}.\n")
    cf.print_green("To configure and build from these sources")
    cf.print_green(" move to an appropriate directory ")
    cf.print_yellow("(NOT /usr/src/) ")
    cf.print_green("and run: \n")
    print()
    cf.bold(f"\t$ cp {cf.config['distfiles']}/{self.package} .")
    cf.bold(f"\t$ tar xf {self.package}")
    return True


def install(self):
    pass
