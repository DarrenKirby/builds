"""
    /var/builds/scripts/config.py
    Thu Oct 24 02:03:14 UTC 2024

    Configuration data needed across program modules

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
    along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

import os
import sys
import logging as log


def get_config() -> dict:
    """Read the builds.conf configuration file """

    if os.path.isfile(f'{os.path.expanduser("~")}/.config/builds/builds.conf'):
        conf_file = f'{os.path.expanduser("~")}/.config/builds/builds.conf'
    elif os.path.isfile('/etc/builds.conf'):
        conf_file = '/etc/builds.conf'
    else:
        print("Cannot find builds.conf")
        sys.exit(-1)

    _config = {}
    with open(conf_file, "r", encoding='utf-8') as f:
        for line in f.readlines():
            if line.startswith("#"):
                pass
            elif line in ('\n', ''):
                pass
            else:
                c = line.split("=")
                _config[c[0].strip()] = c[1].strip()

    if os.environ.get("NO_COLOR"):
        _config['color'] = False

    if 'makeopts' not in _config:
        _config['makeopts'] = '-j1'

    return _config


config = get_config()

# Initialize logger
#   call: logging.warning("File: '%s' does not exist", filename)
# output: 2024-07-22 09:55 - WARNING - File 'foo.txt' does not exist
log.basicConfig(
    filename=config['log_file'],
    encoding="utf-8",
    filemode="a",
    format="[{levelname:^9}] | {asctime} | {message}",
    # format="%(asctime)s | %(levelname)s | %(message)s",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=log.INFO
)
