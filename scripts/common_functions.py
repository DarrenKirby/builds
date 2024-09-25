#    /usr/builds/scripts/common_functions.py
#    Wed Sep 25 01:10:46 UTC 2024

#    Helper module for the builds source building tree
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
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


import hashlib
import sys
import subprocess as sp
import shlex

import requests
import tqdm

COLOR = COLOR or True
BUILDS_ROOT = BUILDS_ROOT or "/usr/builds"
DISTFILES = f"{BUILDS_ROOT}/distfiles"
CONF      = f"{BUILDS_ROOT}/builds.conf"
LOGFILE   = f"{BUILDS_ROOT}/builds.log"


class clr:
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    RED = '\033[1;31m'
    BOLD = '\033[1;37m'
    END = '\033[0;39m'


# These are a bunch of common paths to be used in
# tandem with the helper functions in the next section
# Install paths
paths = {}
paths['b']   = "/bin"
paths['s']   = "/sbin"
paths['l']   = "/lib"
paths['ub']  = "/usr/bin"
paths['us']  = "/usr/sbin"
paths['ui']  = "/usr/include"
paths['ul']  = "/usr/lib"
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

# These helper functions are intended to be used in the
# make_install() function in the package.build file.
# Install binary
def do_bin(frm: str, to: str) -> None:
    try:
        es = sp.call(shlex.split(f"install -v -o root -g root -m 755 -s {frm} {to}"))
    except OSError:
        red(f"Install of {frm} failed")

# install script
def do_scr(frm: str, to: str) -> None:
    es = sp.call(shlex.split(f"install -v -o root -g root -m 755 {frm} {to}"))


# install library
def do_lib(frm: str, to: str) -> None:
    es = sp.call(shlex.split(f"install -v -o root -g root -m 755 {frm} {to}"))


# install header
def do_hdr(frm: str, to: str) -> None:
    es = sp.call(shlex.split(f"install -v -o root -g root -m 644 {frm} {to}"))


# install manpage
def do_man(frm: str, to: str) -> None:
    es = sp.call(shlex.split(f"bzip2 {frm}"))
    es = sp.call(shlex.split(f"install -v -o root -g root -m 644 {frm}.bz2 {to}"))


# install symlink
def do_sym(target: str, name: str) -> None:
    es = sp.call(shlex.split(f"ln -svf {target} {name}"))


# Coloured output. For the following functions, the `print_x`
# version does not include a newline.
def bold(msg: str) -> None:
    print(f"{clr.BOLD if COLOR else clr.END}>>>  {msg}{clr.END}")


def print_bold(msg: str) -> None:
    print(f"{clr.BOLD}{msg}{clr.END}", end='')


def green(msg: str) -> None:
    print(f"{clr.GREEN}>>>  {msg}{clr.END}")


def print_green(msg: str) -> None:
    print(f"{clr.GREEN}{msg}{clr.END}", end='')


def yellow(msg: str) -> None:
    print(f"{clr.GREEN}***  {msg}{clr.END}")


def print_yellow(msg: str) -> None:
    print(f"{clr.YELLOW}{msg}{clr.END}", end='')


def red(msg: str) -> None:
    print(f"{clr.RED}!!!  {msg}{clr.END}")


def print_red(msg: str) -> None:
    print(f"{clr.RED}{msg}{clr.END}", end='')


# Print usage details and exit
def show_usage() -> None:
    print(f"""
Usage: {APPNAME} [options] command pkg_atom [pkg_atom...]
    General Options:
        '-h'   or '--help'                  show usage details
        '-f'   or '--fetch'                 download packages but do not install
        '-p'   or '--pretend'               only show which packages would be built
        '-a'   or '--ask'                   prompt before building packages

    Commands:
        'install'   pkg_atom [pkg_atom...]  install one or more packages and dependancies
        'uninstall' pkg_atom                uninstall package
        'search'    string                  search the package db for package names matching string
        'info'      pkg_atom                print info on package if installed
""")
    sys.exit(0)


def download(url: str, filename: str) -> None:
    """
    Download package with nice progress bar

    This requires requests and tqdm
    """
    with open(filename, 'wb') as f:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            total = int(r.headers.get('content-length', 0))

            # tqdm has many interesting parameters. Feel free to experiment!
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


def get_sha256sum(file_name: str) -> str:
    """Produce checksum of downloaded file"""
    with open(file_name, "rb") as f:
        digest = hashlib.file_digest(f, "sha256")
        return digest.hexdigest()

