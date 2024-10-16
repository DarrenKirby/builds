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
import sys
import os
import os.path
import datetime


BUILDS_ROOT = os.path.abspath("..")

# check if root, else print message about non-privileged install
if os.geteuid() != 0:
    print("Not root!")
    print("Can only install builds in user directory!")
    print(f"installing build root as {BUILDS_ROOT}")
    CONF_PATH = f"{os.path.expanduser("~")}/.builds.conf"
    LOG_PATH = BUILDS_ROOT + "/builds.log"
    DB_PATH = BUILDS_ROOT + "/scripts/builds"
else:
    print("Installing builds systemwide as root")
    print(f"configuring build root as {BUILDS_ROOT}")
    CONF_PATH = "/etc/builds.conf"
    LOG_PATH = "/var/log/builds.log"
    DB_PATH = BUILDS_ROOT + "/scripts/builds-stable"

print(f"Writing configuration file at '{CONF_PATH}'")
current_time = datetime.datetime.now(datetime.UTC)

header = f"""
#    {CONF_PATH}
#    {current_time.strftime('%a %b %d %H:%M:%S UTC %Y')}

#    The builds system configuration file
#
#    Copyright:: (c) 2024 Darren Kirby
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
#    along with this program. If not, see <http://www.gnu.org/licenses/>.


"""
if os.path.isfile(CONF_PATH):
    print(f"{CONF_PATH} exists...")
    if input("overwrite? (y/n)") == 'n':
        sys.exit(1)


print(f"Writing {CONF_PATH}...")
print("...please check default values.")
with open(CONF_PATH, 'w', encoding="utf-8") as conf_file:
    conf_file.write(header)
    conf_file.write(f"builds_root={BUILDS_ROOT}\n")
    conf_file.write(f"distfiles={BUILDS_ROOT}/distfiles\n")
    conf_file.write(f"log_file={LOG_PATH}\n")
    conf_file.write(f"db_file={BUILDS_ROOT}/scripts/builds-stable\n")
    conf_file.write("color=True")

if not os.path.exists(f"{BUILDS_ROOT}/distfiles"):
    os.mkdir(f"{BUILDS_ROOT}/distfiles")

print(f"Writing log file at {LOG_PATH}...")
print(f"Initializing database at {BUILDS_ROOT}/scripts/builds-stable...")

with dbm.open(f'{BUILDS_ROOT}/scripts/builds-stable', 'c') as db:
    with open(f'{BUILDS_ROOT}/scripts/builds-stable.csv', newline='', encoding='UTF8') as f:
        reader = csv.reader(f)
        for row in reader:
            db[row[0]] = ','.join(row[1:])
