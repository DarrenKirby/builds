"""
    /usr/builds/scripts/initialize_builds_tree.py
    Wed Sep 25 23:30:16 UTC 2024

    A script which installs the bld app, and initializes the db file

    Copyright:: (c) 2024 Darren Kirby
    Author:: Darren Kirby (mailto:bulliver@gmail.com)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import csv
import dbm
import os
import os.path


BUILDS_ROOT = '/Users/darrenkirby/code/builds'

# check if root, else print message about non-privileged install
if os.geteuid() != 0:
    print("not root!")

with dbm.open(f'{BUILDS_ROOT}/scripts/builds-stable', 'c') as db:
    with open(f'{BUILDS_ROOT}/scripts/builds-stable.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            db[row[0]] = ','.join(row[1:])

