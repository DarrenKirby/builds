"""
    /var/builds/scripts/uninstall.py
    Tue Nov 19 03:53:10 UTC 2024

    Core logic for uninstalling files and packages.

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

import argparse
from pathlib import Path
#import sys
#import os
#import csv
#import dbm
#import shutil
import logging as log

from config import config

class Unistaller:
    """
    Core logic for uninstalling files and packages.
    """
    def __init__(self, manifest: list, args: argparse.Namespace):
        self.manifest = [Path(file) for file in manifest]
        self.args = args
