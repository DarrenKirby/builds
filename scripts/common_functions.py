"""
    /var/builds/scripts/common_functions.py
    Wed Oct 30 22:26:43 UTC 2024

    Helper module for the builds source building tree

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
import hashlib
import sys
import subprocess as sp
import shlex
import os
import csv
import dbm
import logging as log
import urllib.request as request
from urllib.error import URLError

import requests
import tqdm

from config import config

# These are a bunch of common paths to be used in
# tandem with the helper functions in the next section
# Install paths
paths = {
    'b': "/bin",
    's': "/sbin",
    'l': "/lib",
    'e': "/etc",
    'ub': "/usr/bin",
    'us': "/usr/sbin",
    'ui': "/usr/include",
    'ul': "/usr/lib",
    'ule': "/usr/libexec",
    'ulb': "/usr/local/bin",
    'uls': "/usr/local/sbin",
    'uli': "/usr/local/include",
    'ull': "/usr/local/lib",
    'ush': "/usr/share",

    # Man paths
    'man1': "/usr/share/man/man1",
    'man2': "/usr/share/man/man2",
    'man3': "/usr/share/man/man3",
    'man4': "/usr/share/man/man4",
    'man5': "/usr/share/man/man5",
    'man6': "/usr/share/man/man6",
    'man7': "/usr/share/man/man7",
    'man8': "/usr/share/man/man8"
}

clr = {
    'green': '\033[1;32m',
    'yellow': '\033[1;33m',
    'red': '\033[1;31m',
    'bold': '\033[1;37m',
    'end': '\033[0;39m'
}


# Coloured output. For the following functions, the `print_x`
# version does not include a newline.

def colorize(color: str, msg: str) -> str:
    s = ""
    s += clr[color] if config['color'] else ''
    s += msg
    s += clr['end'] if config['color'] else ''
    return s


def bold(msg: str) -> None:
    """Print bold text """
    msg = colorize("bold", msg)
    print(f">>> {msg}")


def print_bold(msg: str) -> None:
    """Print bold text with no newline """
    msg = colorize("bold", msg)
    print(msg, end='')


def green(msg: str) -> None:
    """Print green text """
    msg = colorize("green", msg)
    print(f">>> {msg}")


def print_green(msg: str) -> None:
    """Print green text with no newline """
    msg = colorize("green", msg)
    print(msg, end='')


def yellow(msg: str) -> None:
    """Print yellow text """
    msg = colorize("yellow", msg)
    print(f"*** {msg}")


def print_yellow(msg: str) -> None:
    """Print yellow text with no newline """
    msg = colorize("yellow", msg)
    print(msg, end='')


def red(msg: str) -> None:
    """Print red text """
    msg = colorize("red", msg)
    print(f"!!! {msg}")


def print_red(msg: str) -> None:
    """Print red text with no newline """
    msg = colorize("red", msg)
    print(msg, end='')


# These helper functions are intended to be used in the
# 'install()' function in the package.build file.
def do_bin(frm: str, to: str) -> None:
    """
    Install a binary to the live filesystem
    """
    try:
        sp.run(shlex.split(f"install -S -v -o root -g root -m 755 -s {frm} {to}"), check=True)
    except sp.CalledProcessError as e:
        red(f"Install of {frm} failed: ")
        print(e)
        log.error("install of %s failed.", frm)
        sys.exit(-1)


def do_scr(frm: str, to: str) -> None:
    """
    Install a script to the live filesystem
    """
    try:
        sp.run(shlex.split(f"install -S -v -o root -g root -m 755 {frm} {to}"), check=True)
    except sp.CalledProcessError as e:
        red(f"Install of {frm} failed: ")
        print(e)
        log.error("install of %s failed.", frm)
        sys.exit(-1)


def do_lib(frm: str, to: str) -> None:
    """
    Install a library to the live filesystem
    """
    try:
        sp.run(shlex.split(f"install -S -v -o root -g root -m 755 {frm} {to}"), check=True)
    except sp.CalledProcessError as e:
        red(f"Install of {frm} failed: ")
        print(e)
        log.error("install of %s failed.", frm)
        sys.exit(-1)


def do_hdr(frm: str, to: str) -> None:
    """
    Install a header file to the live filesystem
    """
    try:
        sp.run(shlex.split(f"install -S -v -o root -g root -m 644 {frm} {to}"), check=True)
    except sp.CalledProcessError as e:
        red(f"Install of {frm} failed: ")
        print(e)
        log.error("install of %s failed.", frm)
        sys.exit(-1)


def do_man(frm: str, to: str) -> None:
    """
    Compress and install a manpage to the live filesystem
    """
    try:
        sp.run(shlex.split(f"bzip2 {frm}"), check=True)
        sp.run(shlex.split(f"install -S -v -o root -g root -m 644 {frm}.bz2 {to}"), check=True)
    except sp.CalledProcessError as e:
        red(f"Install of {frm} failed: ")
        print(e)
        log.error("install of %s failed: %s.", frm, e)
        sys.exit(-1)


def do_sym(target: str, name: str) -> None:
    """
    Make a symbolic link in the live filesystem
    """
    try:
        sp.run(shlex.split(f"ln -svf {target} {name}"), check=True)
    except sp.CalledProcessError as e:
        red(f"Install of {name} failed: ")
        print(e)
        log.error("symbolic link of %s failed: %s.", name, e)
        sys.exit(-1)


def do_dir(src: str, dst: str) -> None:
    """
    Recursively install a directory of files

    This is intended to be used with packages that create
    deep nested directories of library files
    """
    try:
        os.rename(src, dst)
    except OSError as e:
        red("Call to do_dir failed: ")
        print(e)
        log.error("call to do_dir failed. Aborting install")
        sys.exit(-1)


def do_con(frm: str, to: str) -> None:
    """
    Install a configuration file to the live filesystem.
    """
    try:
        sp.run(shlex.split(f"install -b -v -o root -g root -m 644 {frm} {to}"), check=True)
    except sp.CalledProcessError as e:
        red(f"Install of {frm} failed: ")
        print(e)
        log.error("install of %s failed.", frm)
        sys.exit(-1)


def download(url: str, filename: str) -> None:
    """
    Download package with nice progress bar

    This requires requests and tqdm
    """

    # requests doesn't do FTP
    if url[0:4] == "ftp:":
        download_ftp(url, filename)
        return

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
            log.error("Download of %s timed out", filename)
            sys.exit(12)
        except requests.exceptions.ConnectionError:
            red("Name resolution error!")
            print("Are you sure you're connected to the Internet?")
            log.error("Download of %s failed", filename)
            # requests leaves a zero-length stub file
            # which we need to clean up if the download fails
            os.remove(filename)
            sys.exit(12)


class DownloadProgressBar(tqdm.tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


def download_ftp(url: str, filename: str) -> None:
    """
    Download using ftp protocol
    """
    try:
        with DownloadProgressBar(unit='B',
                                 unit_scale=True,
                                 miniters=1,
                                 desc=url.split('/')[-1]) as t:
            request.urlretrieve(url, filename=filename, reporthook=t.update_to)
    # try:
    #     with closing(request.urlopen(url)) as r:
    #         with open(filename, 'wb') as f:
    #             shutil.copyfileobj(r, f)
    except URLError as e:
        if e.reason.find('No such file or directory') >= 0:
            red(f"File: {filename.split('/')[-1]} not found on server")
            sys.exit(23)
        else:
            raise Exception(f'Something else happened. "{e.reason}"')


def get_sha256sum(file_name: str) -> str:
    """
    Produce checksum of downloaded file
    """
    # with open(file_name, "rb") as f:
    #    digest = hashlib.file_digest(f, "sha256")
    #    return digest.hexdigest()
    # file_digest only available on Python 3.11+
    #
    sha256_hash = hashlib.sha256()
    with open(file_name, "rb") as f:
        # Read the file in chunks to avoid memory issues with large files
        for chunk in iter(lambda: f.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()


def do_initdb(args: argparse.Namespace) -> None:
    """
    Initialize a db file from a csv file
    """
    for csv_file in args.db_file:
        try:
            db_file_name = csv_file.split('/')[-1]
            with dbm.open(f'{config["builds_root"]}/scripts/{db_file_name[:-4]}', 'c') as db:
                with open(csv_file, newline='', encoding='UTF8') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        db[row[0]] = ','.join(row[1:])

        except FileNotFoundError:
            red(f"The file {csv_file} was not found.")
            log.error("%s was not found", csv_file)
            sys.exit(6)
        except PermissionError:
            red(f"You don't have permission to read {csv_file}.")
            log.error("No permission to read %s", csv_file)
            sys.exit(7)
        except csv.Error as e:
            red(f"Error while reading {csv_file}: {e}")
            sys.exit(8)
        green(f"Initialized {csv_file[:-4]}")


def get_manifest(build_file: str) -> list:
    """
    Open the build file and retrieve file manifest
    """
    manifest = []
    in_manifest = False
    with open(build_file, 'r', encoding='utf-8') as f:
        for line in f:

            if '"""' in line and not in_manifest:
                in_manifest = True
                continue
            if '"""' in line and in_manifest:
                break

            if in_manifest:
                manifest.append(line.strip())

    return manifest


def get_db_info(package: str) -> list:
    """
    Retrieve the database info for a given package
    """
    if package.find('/') != -1:
        package = package.split('/')[0]

    with dbm.open(config['db_file']) as db:
        string = db[package].decode()

    lst = string.split(',')
    lst.insert(0, package)
    return lst


def get_installed_version(package: str) -> list:
    """
    Retrieve the installed version from 'installed' file
    """
    if package.find('/') == -1:
        package = get_db_info(package)[1]

    with open(f"{config['builds_root']}/sets/installed", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith(package):
                line = line.strip('\n')
                return line.split(',')

    # yellow(f"{package} does not appear to be installed")
    return [None]


def add_to_install_file(name: str, version: str) -> int:
    """
    Add a newly installed package to the 'installed' file
    """
    try:
        with open(f"{config['builds_root']}/sets/installed", "a", encoding="utf-8") as f:
            f.write(f"{name},{version}\n")
            return 0
    except IOError:
        return 1
