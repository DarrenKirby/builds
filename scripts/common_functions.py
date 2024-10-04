"""
    /usr/builds/scripts/common_functions.py
    Wed Sep 25 23:30:16 UTC 2024

    Helper module for the builds source building tree

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

import hashlib
import sys
import subprocess as sp
import shlex
import os
import csv
import dbm
import logging as log

import requests
import tqdm


# These are a bunch of common paths to be used in
# tandem with the helper functions in the next section
# Install paths
paths = {}
paths['b'] = "/bin"
paths['s'] = "/sbin"
paths['l'] = "/lib"
paths['ub'] = "/usr/bin"
paths['us'] = "/usr/sbin"
paths['ui'] = "/usr/include"
paths['ul'] = "/usr/lib"
paths['ulb'] = "/usr/local/bin"
paths['uls'] = "/usr/local/sbin"
paths['uli'] = "/usr/local/include"
paths['ull'] = "/usr/local/lib"

# Man paths
paths['man1'] = "/usr/share/man/man1"
paths['man2'] = "/usr/share/man/man2"
paths['man3'] = "/usr/share/man/man3"
paths['man4'] = "/usr/share/man/man4"
paths['man5'] = "/usr/share/man/man5"
paths['man6'] = "/usr/share/man/man6"
paths['man7'] = "/usr/share/man/man7"
paths['man8'] = "/usr/share/man/man8"


clr = {
    'green': '\033[1;32m',
    'yellow': '\033[1;33m',
    'red': '\033[1;31m',
    'bold': '\033[1;37m',
    'end': '\033[0;39m'
}


# Coloured output. For the following functions, the `print_x`
# version does not include a newline.
def bold(msg: str) -> None:
    """Print bold text """
    print(f"{clr['bold'] if config['color'] else ''}>>>  {msg}{clr['end']}")


def print_bold(msg: str) -> None:
    """Print bold text with no newline """
    print(f"{clr['bold']}{msg}{clr['end']}", end='')


def green(msg: str) -> None:
    """Print green text """
    print(f"{clr['green']}>>>  {msg}{clr['end']}")


def print_green(msg: str) -> None:
    """Print green text with no newline """
    print(f"{clr['green']}{msg}{clr['end']}", end='')


def yellow(msg: str) -> None:
    """Print yellow text """
    print(f"{clr['yellow']}***  {msg}{clr['end']}")


def print_yellow(msg: str) -> None:
    """Print yellow text with no newline """
    print(f"{clr['yellow']}{msg}{clr['end']}", end='')


def red(msg: str) -> None:
    """Print red text """
    print(f"{clr['red']}!!!  {msg}{clr['end']}")


def print_red(msg: str) -> None:
    """Print red text with no newline """
    print(f"{clr['red']}{msg}{clr['end']}", end='')


def get_config():
    """Read the configuration file """
    if not os.path.exists("/Users/darrenkirby/code/builds/scripts/builds.conf"):
        red("Cannot find builds.conf")
        sys.exit(-1)

    _config = {}
    with open("/Users/darrenkirby/code/builds/scripts/builds.conf", "r", encoding='UTF8') as f:
        for line in f.readlines():
            if line.startswith("#"):
                pass
            elif line in ('\n', ''):
                pass
            else:
                c = line.split("=")
                _config[c[0].strip()] = c[1].strip()
    return _config


config = get_config()

# Initialize logger
#   call: logging.warning("File: '%s' does not exist", filename)
# output: 2024-07-22 09:55 - WARNING - File 'foo.txt' does not exist
log.basicConfig(
        filename=config['logfile'],
        encoding="utf-8",
        filemode="a",
        format="%(asctime)s - %(levelname)s - %(message)s",
        #format="{asctime} - {levelname} - {message}",
        style="%",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=log.INFO
)

# These helper functions are intended to be used in the
# install() function in the package.build file.
def do_bin(frm: str, to: str) -> None:
    """
    Install a binary to the live filesystem
    """
    try:
        sp.run(shlex.split(f"install -S -v -o root -g root -m 755 -s {frm} {to}"), check=True)
    except sp.CalledProcessError as e:
        red(f"Install of {frm} failed:")
        print(e)
        log_fail(config['logfile'], f"install of {frm} failed.")
        sys.exit(-1)


def do_scr(frm: str, to: str) -> None:
    """
    Install a script to the live filesystem
    """
    try:
        sp.run(shlex.split(f"install -S -v -o root -g root -m 755 {frm} {to}"), check=True)
    except sp.CalledProcessError as e:
        red(f"Install of {frm} failed:")
        print(e)
        log_fail(config['logfile'], f"install of {frm} failed.")
        sys.exit(-1)


def do_lib(frm: str, to: str) -> None:
    """
    Install a library to the live filesystem
    """
    try:
        sp.run(shlex.split(f"install -S -v -o root -g root -m 755 {frm} {to}"), check=True)
    except sp.CalledProcessError as e:
        red(f"Install of {frm} failed:")
        print(e)
        log_fail(config['logfile'], f"install of {frm} failed.")
        sys.exit(-1)


def do_hdr(frm: str, to: str) -> None:
    """
    Install a header file to the live filesystem
    """
    try:
        sp.run(shlex.split(f"install -S -v -o root -g root -m 644 {frm} {to}"), check=True)
    except sp.CalledProcessError as e:
        red(f"Install of {frm} failed:")
        print(e)
        log_fail(config['logfile'], f"install of {frm} failed: {e}")
        sys.exit(-1)


def do_man(frm: str, to: str) -> None:
    """
    Compress and install a manpage to the live filesystem
    """
    try:
        sp.run(shlex.split(f"bzip2 {frm}"), check=True)
        sp.run(shlex.split(f"install -S -v -o root -g root -m 644 {frm}.bz2 {to}"), check=True)
    except sp.CalledProcessError as e:
        red(f"Install of {frm} failed:")
        print(e)
        log_fail(config['logfile'], f"install of {frm} failed: {e}")
        sys.exit(-1)


def do_sym(target: str, name: str) -> None:
    """
    Make a symbolic link in the live filesystem
    """
    try:
        sp.run(shlex.split(f"ln -svf {target} {name}"), check=True)
    except sp.CalledProcessError as e:
        red(f"Install of {name} failed:")
        print(e)
        log_fail(config['logfile'], f"install of {name} failed: {e}")
        sys.exit(-1)


def download(url: str, filename: str) -> None:
    """
    Download package with nice progress bar

    This requires requests and tqdm
    """
    with open(filename, 'wb') as f:
        try:
            with requests.get(url, stream=True, timeout=10) as r:
                r.raise_for_status()
                total = int(r.headers.get('content-length', 0))

                tqdm_params = {
                    'desc': url,
                    'total': total,
                    'miniters': 1,
                    'unit': 'B',
                    'unit_scale': True,
                    'unit_divisor': 1024,
                }
                with tqdm.tqdm(**tqdm_params) as pb:
                    for chunk in r.iter_content(chunk_size=8192):
                        pb.update(len(chunk))
                        f.write(chunk)

        except requests.exceptions.Timeout:
            yellow("Download timed out")
            print("Perhaps try a mirror?")
            #log_fail(config['logfile'], f"Download of {filename} timed out")


def get_sha256sum(file_name: str) -> str:
    """
    Produce checksum of downloaded file
    """
    with open(file_name, "rb") as f:
        digest = hashlib.file_digest(f, "sha256")
        return digest.hexdigest()


def do_initdb(args: list, config: dict) -> None:
    """
    Initialize a db file from a csv file
    """
    for csv_file in args:
        with dbm.open(f'{BUILDS_ROOT}/scripts/{csv_file[:-4]}', 'c') as db:
            with open(csv_file, newline='', encoding='UTF8') as f:
                reader = csv.reader(f)
                for row in reader:
                    db[row[0]] = ','.join(row[1:])
