"""
    /var/builds/scripts/initialize_builds_tree.py
    Sun Nov 17 20:41:14 UTC 2024

    A script which installs the bld app, and initializes the db file

    Copyright:: (c) 2024
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
import datetime
import pwd
import grp
from pathlib import Path

import common_functions as cf

banner_text = """
                                                                                           
bbbbbbbb                                                          dddddddd                 
b::::::b                                iiii  lllllll             d::::::d                 
b::::::b                               i::::i l:::::l             d::::::d                 
b::::::b                                iiii  l:::::l             d::::::d                 
 b:::::b                                      l:::::l             d:::::d                  
 b:::::bbbbbbbbb    uuuuuu    uuuuuu  iiiiiii  l::::l     ddddddddd:::::d     ssssssssss   
 b::::::::::::::bb  u::::u    u::::u  i:::::i  l::::l   dd::::::::::::::d   ss::::::::::s  
 b::::::::::::::::b u::::u    u::::u   i::::i  l::::l  d::::::::::::::::d ss:::::::::::::s 
 b:::::bbbbb:::::::bu::::u    u::::u   i::::i  l::::l d:::::::ddddd:::::d s::::::ssss:::::s
 b:::::b    b::::::bu::::u    u::::u   i::::i  l::::l d::::::d    d:::::d  s:::::s  ssssss 
 b:::::b     b:::::bu::::u    u::::u   i::::i  l::::l d:::::d     d:::::d    s::::::s      
 b:::::b     b:::::bu::::u    u::::u   i::::i  l::::l d:::::d     d:::::d       s::::::s   
 b:::::b     b:::::bu:::::uuuu:::::u   i::::i  l::::l d:::::d     d:::::d ssssss   s:::::s 
 b:::::bbbbbb::::::bu:::::::::::::::uui::::::il::::::ld::::::ddddd::::::dds:::::ssss::::::s
 b::::::::::::::::b  u:::::::::::::::ui::::::il::::::l d:::::::::::::::::ds::::::::::::::s 
 b:::::::::::::::b    uu::::::::uu:::ui::::::il::::::l  d:::::::::ddd::::d s:::::::::::ss  
 bbbbbbbbbbbbbbbb       uuuuuuuu  uuuuiiiiiiiillllllll   ddddddddd   ddddd  sssssssssss    
                                                                                           
                                                                                 
"""

print(banner_text)

BUILDS_ROOT = os.path.abspath(os.pardir)

if os.geteuid() != 0:
    print("Hi there. I see you are not root, and therefore would like to ")
    print("install builds in your user directory. Is that correct?")
    if input(">>> ") in ['n', 'N', 'no', 'No']:
        sys.exit(1)

    print("OK.")
    print(f"So you want to keep build root as ", end="")
    cf.print_bold(f"{BUILDS_ROOT}?\n")
    if input(">>> ") in ['n', 'N', 'no', 'No']:
        sys.exit(1)

    CONF_PATH = f"{os.environ['HOME']}/.config/builds/builds.conf"
    CONF_DIR = f"{os.environ['HOME']}/.config/builds/"

    print("OK. So we will write a configuration file to: ")
    cf.bold(CONF_PATH)

    os.makedirs(CONF_DIR, exist_ok=True)
    LOG_PATH = BUILDS_ROOT + "/builds.log"
    DB_PATH = BUILDS_ROOT + "/scripts/builds-stable"

    print()
    print("Now, we have to decide where to install the live files.")
    print("The default, provided build scripts install files using ")
    print("'--prefix=/usr', so if we use your home directory all files ")
    print("will be installed in ~/usr/bin, ~/usr/include, ~/usr/lib ")
    print("and so on. Is this satisfactory?")
    if input(">>> ") in ['n', 'N', 'no', 'No']:
        print("OK. Then tell me where to put them. Please use an ABSOLUTE path ")
        print("with no trailing slash. It needs to be either under your home ")
        print("directory, or somewhere else you have write permissions...")
        INSTALL_ROOT = input("(type install root) >>> ")
    else:
        INSTALL_ROOT = str(Path.home())

    print("Cool. ", end="")
    cf.print_bold(INSTALL_ROOT)
    print(" it is then.")
    print("We need to initialize a filesystem structure now. I will create ")
    print(f"some empty directories under {INSTALL_ROOT} to install files to.")

    try:
        for directory in ["/usr/bin",
                          "/usr/sbin",
                          "/usr/etc",
                          "/usr/include/sys",
                          "/usr/libexec",
                          "/usr/lib/pkgconfig",
                          "/usr/lib/udev/rules.d/",
                          "/usr/share/misc",
                          "/usr/share/man/man1",
                          "/usr/share/man/man2",
                          "/usr/share/man/man3",
                          "/usr/share/man/man4",
                          "/usr/share/man/man5",
                          "/usr/share/man/man6",
                          "/usr/share/man/man7",
                          "/usr/share/man/man8",
                          "/usr/local"
                          ]:
            os.makedirs(f"{INSTALL_ROOT}{directory}", exist_ok=True)
            print(f"Created: {INSTALL_ROOT}{directory}")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit()

    USER = pwd.getpwuid(os.getuid()).pw_name
    GRP = grp.getgrgid(os.getgid()).gr_name

else:
    print("Hi there. I see you are root, and therefore would like to ")
    print("install builds system wide. Is that correct?")
    if input(">>> ") in ['n', 'N', 'no', 'No']:
        sys.exit(1)

    print("OK.")
    print(f"So you want to keep build root as ", end="")
    cf.print_bold(f"{BUILDS_ROOT}?")
    if input(">>> ") in ['n', 'N', 'no', 'No']:
        sys.exit(1)

    CONF_PATH = "/etc/builds.conf"
    LOG_PATH = "/var/log/builds.log"
    DB_PATH = BUILDS_ROOT + "/scripts/builds-stable"
    USER = "root"
    GRP = "root"
    INSTALL_ROOT = ""


current_time = datetime.datetime.now(datetime.UTC)

HEADER = f"""
#    {CONF_PATH}
#    {current_time.strftime('%a %b %d %H:%M:%S UTC %Y')}

#    The builds system configuration file
#
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
#    along with this program. If not, see <http://www.gnu.org/licenses/>.


"""

clobber = True
if os.path.isfile(CONF_PATH):
    print(f"{CONF_PATH} exists...")
    if input(">>> overwrite? (y/n) ") in ['n', 'N', 'no', 'No']:
        clobber = False

if clobber:
    print(f"Writing {CONF_PATH}...")
    print("Please check default values, and edit as necessary")
    print("Leave 'install_root=' for system-wide installs.")
    print()
    with open(CONF_PATH, 'w', encoding="utf-8") as conf_file:
        conf_file.write(HEADER)
        conf_file.write(f"builds_root={BUILDS_ROOT}\n")
        conf_file.write(f'install_root={INSTALL_ROOT}\n')
        conf_file.write(f"distfiles={BUILDS_ROOT}/distfiles\n")
        conf_file.write(f"log_file={LOG_PATH}\n")
        conf_file.write(f"db_file={BUILDS_ROOT}/scripts/builds-stable\n")
        conf_file.write("color=True\n")
        conf_file.write(f"user={USER}\n")
        conf_file.write(f"group={GRP}\n")

if not os.path.exists(f"{BUILDS_ROOT}/distfiles"):
    os.mkdir(f"{BUILDS_ROOT}/distfiles")

print(f"Writing log file at {LOG_PATH}")
print(f"Initializing database at {BUILDS_ROOT}/scripts/builds-stable")

with dbm.open(f'{BUILDS_ROOT}/scripts/builds-stable', 'c') as db:
    with open(f'{BUILDS_ROOT}/scripts/builds-stable.csv', newline='', encoding='UTF8') as f:
        reader = csv.reader(f)
        for row in reader:
            db[row[0]] = ','.join(row[1:])

print("...Done")

try:
    import requests

    print("'requests' is installed! Good!")
except ImportError:
    print("'requests' HTTP library is not installed.")
    print("This library is needed to download packages.")
    print("Please run 'pip3 install requests' to install it...")
    print()
try:
    import tqdm

    print("'tqdm' is installed! Good!")
except ImportError:
    print("'tqdm' library is not installed.")
    print("This library is needed for a download progress bar.")
    print("Please run 'pip3 install tqdm' to install it...")
    print()

install_file = "../sets/installed"
with open(install_file, 'a'):
    os.utime(install_file, None)

print("builds is now installed.")
print(f"Please do not forget to review and edit {CONF_PATH}")
print("as necessary before the first run.")
print()
print(f"You should also copy (or move) '{BUILDS_ROOT}/scripts/bld' to an")
print("appropriate location within a system or user PATH")
