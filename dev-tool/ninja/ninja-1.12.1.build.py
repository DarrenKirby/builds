#    dev-tool/ninja/ninja-1.12.1.build.py
#    Sat Dec  7 00:57:24 UTC 2024

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


def make(self):
    return self.do("python3 configure.py --bootstrap")


def install(self):
    self.inst_binary(f"{self.work_dir}/{self.package_dir}/ninja", self.p['ub'])

    self.install_file(f"{self.work_dir}/{self.package_dir}/misc/bash-completion",
                      self.p['ush'] + "/bash-completion/completions/ninja")
    self.install_file(f"{self.work_dir}/{self.package_dir}/misc/zsh-completion",
                      self.p['ush'] + "/zsh/site-functions/_ninja")
