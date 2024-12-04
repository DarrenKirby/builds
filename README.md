## *builds*

*builds* is a lightweight and simple package management tool for installing, managing, and updating software, typically
from source code. It is superficially similar to *ports* from FreeBSD, and *portage* from Gentoo.
Similarly to both, *builds* uses backend scripts which specify how to build and install packages. Unlike both,
there is no central 'official' repository of
scripts or packages. While I have created a modest library of scripts which are distributed with the platform, *builds*
should be thought of as a kitchen, in which you create and test your own recipes. If a particular
build script does not yet exist, it is relatively easy for anyone to create their own, even with a minimum of Python
knowledge.

I originally created *builds* to take care of updating and installing software in a
new [Linux From Scratch](https://www.linuxfromscratch.org/) system installation of my own, and the provided build files 
are tailered specifically for a fresh LFS install. That said, I have designed
*builds* to be portable, and the front-end should work just fine on any unixish system that supports Python 3.6 or
better. It is only the per-package build scripts that would need to be customized for each system, and for personal
preferences. The provided build files _should_ work as-is with most Linux systems, and with minimal changes for 
macOS and other Unix systems

*builds* is pure-Python, and uses only two non-standard library
modules: [requests](https://pypi.org/project/requests/)
to download packages, and [tqdm](https://pypi.org/project/tqdm/) for a nice download progress bar.

Although it is theoretically possible, I have not designed *builds* to take the place of a proper, operating
system-wide package management system, outside an LFS/BLFS system. Rather than managing all software for a
particular system, *builds* is best suited to managing a specific subset of
packages, collected for a specific purpose. For example, collectively managing all the packages required for a Python
data-science ecosystem. Or perhaps for managing a development/testing environment for some custom software and its
dependencies. Or for keeping a collection of bleeding-edge versions of some favourite packages separate from the stable
base packages offered by your operating system.

There are two different methods for installing *builds*:

The first is a system-wide install, which will install all software to the usual locations in the live file system. This
type of install will therefore require root, or otherwise privileged access to the system.

The second method is a segregated user install. This method will install the software and associated files to a
directory of the user's choosing, presumably, somewhere within their home directory. This does not require privileged
access.

While it should be possible to have a single system-wide and multiple user installations of *builds* on the same
system, I have not yet tested this.

The foremost feature of *builds* is customization ability. While I have tried to stay close to best practices (POSIX,
LSB, FHS etc..) in the build scripts provided, it is up to the user to modify and create their own scripts to build the
software how they want, and install it where they want. I have tried as much as I can to not have *builds* force
unnecessary constraints on, well, anything really.

## How it works

All available software is centrally managed in a DBM database file, which is created from a CSV file. This db
collects the package names, versions, categories, websites, download sites, and a short description of the package. The
frontend is a collection of Python scripts, functions, and classes which use this db to determine which software, and
which version(s) of said software are available to install.

The backend scripts are kept in per-package directories underneath an appropriate category in the main builds file tree.
These scripts specify how to build the software, and where to install the software once it is built.

It is as simple as:

	# bld install vim

to install a package. Of course, multiple packages can be specified at one time:

	# bld install vim nano git

*builds* allows you to collect multiple packages together in a set, to act on at one time. Given a file named `myset` in
the `sets` directory like so:

	# This is a set of compression utilities

	app-arch/bzip2
	app-arch/lz4
	app-arch/xz

you can install all of them using set notation like this:

	# bld install @myset

You can search the available package database using `search`, and it will match against package names and descriptions:

	# bld search shell
	
	bld version 0.4.0 (By far the best software available for turtle stacking)

	Category/Name >>> app-shell/dash
	      Version >>> 0.5.12
	  Description >>> The Debian Almquist shell
	     Homepage >>> http://gondor.apana.org.au/~herbert/dash/

	Category/Name >>> app-shell/zsh
	      Version >>> 5.9
	  Description >>> zsh is an interactive shell and powerful scripting language
	     Homepage >>> https://zsh.sourceforge.io/

	Category/Name >>> app-shell/bash
	      Version >>> 5.2.37
	  Description >>> bash is the GNU Bourne again shell
	     Homepage >>> https://www.gnu.org/software/bash/

	Category/Name >>> dev-tool/autoconf
	      Version >>> 2.72
	  Description >>> Autoconf is an extensible package of M4 macros that produce shell scripts to automatically configure software source code
	     Homepage >>> https://www.gnu.org/software/autoconf/

	Category/Name >>> app-shell/tcsh
	      Version >>> 6.24.13
	  Description >>> C shell with file name completion and command line editing
	     Homepage >>> https://www.tcsh.org/

You can use `info` to get information about installed packages:

    # bld info coreutils
    bld version 0.4.0 (By far the best software available for turtle stacking)
    
    Current installed version of app-util/coreutils is 9.5
    
    Current database information:
    Category/Name >>> app-util/coreutils
          Version >>> 9.5
      Description >>> These are the core utilities which are expected to exist on every operating system
         Homepage >>> https://www.gnu.org/software/coreutils/
    
    Local builds information:
    Build of coreutils 9.5 started on Mon, Nov 18, 2024 at 11:45AM
    Build of coreutils 9.5 complete in 3 minutes, 6 seconds.
    
    Build of coreutils 9.5 started on Sun, Nov 17, 2024 at 05:45PM
    Build of coreutils 9.5 complete in 3 minutes, 8 seconds.

## Installation

The simplest method to install *builds* is to just `git clone` the builds tree into the location you want it to live in.
For a system-wide install it is recommended (but not necessary) to use `/var/builds/`. For a user
install, `/home/<user>/builds/` is appropriate. If `git` is not available on the target system, then you extract a
tarball of the builds tree into the appropriate location, then use builds to install `git` to keep updated.

To install...

    # git clone https://github.com/DarrenKirby/builds.git

To update (run from the top-level "builds" directory:

    # git pull

Once the tree is installed, you can `cd` into the `scripts` directory and run `initialize_builds_tree.py` like so:

	# python initialize_builds_tree.py

If you run this script as root, it will assume a system-wide installation. If you run it as a non-privileged user, it
will assume a user install. The script will write a configuration file (`/etc/builds.conf` for system-wide,
`~/.config/builds/builds.conf` for user) and initialize the database. It is important to run this script from inside
`builds/scripts/`, as the script uses the $PWD to determine paths to write to the config file.

For system-wide installations the initialization script will create a non-privileged system user and group named
"builds", and `chown` the entire builds tree to this user. While `bld` will still have to be run as root, the program
will drop privileges and execute as the 'builds' user except for the step where it installs the files to the live
filesystem.

## Note on stability

Currently, *builds* is under heavy development and changes almost daily. While I certainly try my best to not introduce
backwards-incompatible changes without good reason, breakage may occur at any time, at least until it gets to a proper
1.0.0 version, at which time *builds* will assume [semantic versioning](https://semver.org/).