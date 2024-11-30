# Writing build scripts

## Database overview

*builds* keeps track of which packages are available to install using a [gdmb](https://www.gnu.org.ua/software/gdbm/)
database. Upon installation, *builds* will initialize a database which includes the package build scripts distributed
with the platform. This db is named 'builds-stable', and will be created in the script folder upon running the
`initialize_builds.py` script. The (semicolon-delimited) CSV file used to generate the db is also included in the
scripts directory.

To add your own packages, you can either edit the existing CSV file, or create your own from scratch. The format of this
file is:

    <pkg name>;<pkg category/name>;<pkg version>;<sha256 hash of pkg>;<download url>;<pkg homepage>;<pkg desription>

For example:

    gzip;app-arch/gzip;1.13;7454eb6935db17c6655576c2e1b0fabefd38b4d0936e0f87f48cd062ce91a057;https://ftpmirror.gnu.org/gzip/gzip-VVV.tar.xz;https://www.gnu.org/software/gzip/;Standard GNU compression utility

Note the 'VVV' slug in the download URL. This slug will be replaced 1:1 with the version string by `bld`. To regenerate
the db after editing a CSV file use the `initdb` command:

    # bld initdb ./scripts/builds-stable.csv

or:

    # bld initdb my_custom_packages.csv

which will create a new db named `my_custom_packages` in the scripts directory. You will then have to edit your
configuration file to use this custom db. While it is not currently possible, I will be adding the ability to use
multiple db files, ranked by preference, soon enough. Of course, it is not enough to just add the package to the db.
You will also have to write a build script for it.

The first thing to do is to decide on a relevant category for your package. You can use one of the existing categories,
or create a new one. The categories should be portage style: 'dev-tool', 'app-game' or similar. The hyphen is not
required, but it is recommended to visually distinguish categories from other directories under `builds/`.

After deciding on a category, create a directory under the category directory with just the name of the package, as
specified in the db. In this directory, create a file named `<pkg name>-<pkg version>.builds.py`. If you like there is
a well-commented template build file in `scripts/` that you can copy and edit.

For the purposes of this documentation, I will walk through the creation of a build script for
[OpenSSH](https://www.openssh.com/).

So first we have to add an entry to the CSV file. From the OpenSSH website, we can see that the latest version is
`openssh-9.9p1.tar.gz` available from the
URL `https://cdn.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-9.9p1.tar.gz`. Depending on the package, there may be
only one URL, or perhaps multiple mirrors. Choose the one that works best for you. We can now extract the version from
the download URL, and replace it with the 'VVV' slug.

Most software distributors allow for validating the download using a checksum or signature. Often, checksums or public
signatures will be located in the same directory as the source package. Sometimes they will be elsewhere on the website.
After downloading a package, it is important to verify its integrity. Use md5sum, or one of the sha<n>sum utilities to
compare the hashes. Many projects use only a PGP/GPG signature to verify. This is more involved, and beyond the scope
of this document to explain, but there
are [good references](https://www.tecmint.com/verify-pgp-signature-downloaded-software/)
online with instructions.

Regardless of how you verify the download, *builds* uses a sha256sum. If the distributor does not ptovide this you can
generate it your self using the previously verified download:

    # sha256sum openssh-9.9p1.tar.gz
    b343fbcdbff87f15b1986e6e15d6d4fc9a7d36066be6b7fb507087ba8f966c02  openssh-9.9p1.tar.gz

Copy and paste this hash into the CSV file in the 4th field. For the homepage, use the official site for the software
if there is one. Often this may just be a github page. Use your best judgement. The idea is to provide a link where
information and documentation for the software could be found. For the description, there can usually be a short
summary of what the software does on the homepage. Again, use your judgement here. The idea is to give a brief overview
of the software to be printed when running `bld search` or `bld info`.

So the complete line in the CSV file should look like this:

    # openssh;net-util/openssh;9.9p1;b343fbcdbff87f15b1986e6e15d6d4fc9a7d36066be6b7fb507087ba8f966c02;https://cdn.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-VVV.tar.gz;https://www.openssh.com/;OpenSSH is the premier connectivity tool for remote login with the SSH protocol

Now, re-initialize the database, and prepare to write the build script:

From './builds/':

    # bld initdb ./scripts/builds-stable.csv
    # mkdir -p net-util/openssh
    # cp ./scripts/template.build.py net-util/openssh/openssh-9.9p1.build.py

## build script overview

The build script contains all the package-specific instructions on how to configure, build, and install the package.
*builds* models this process in seven discrete steps, of which 3 are automatic, and 4 must be manually specified in the
build file. These steps are:

1. *Fetching the package*. This step is automated. As long as the download URL in the db is correct, `bld` will download
   the package into the `./builds/distfiles/` directory automatically. `bld` will also verify the sha256 hash of the
   downloaded file. There are two scriptable hooks into this process, if needed, but more on that later.
2. *Extracting the package into a working directory*. This step is automated. `bld` will extract package tarballs into
   a directory called 'work' under the package directory. In our example, this would result in the OpenSSH source tree
   in `./builds/net-util/openssh/work/openssh-9.9p1`. Again, there are hooks into this step if needed. For example, you
   may want to apply patches to the source.
3. *configuring the package*. This is an optional step that can be specified manually if necessary. This is where you
   would perform the `./configure` step in the typical configure/make/make install process.
4. *'make'ing the package*. Optional. This is where you would run `make` if necessary.
5. *'make install'ing the package*. Optional. This is where you would run `make install`. Note that this step should
   not be used to install files to the live filesystem, but rather, into a segregated staging directory. More on this
   later.
6. *Installing the package*. This step is required to be defined in the build file. This is where the package files
   get installed into the live filesystem. A set of helper functions and path variables are provided to make this easy.
7. *Clean up* This step is automated. If all previous steps ran successfully, this step will remove the temporary
   'work' directory, write a manifest of installed files, and record the package and version into a special 'installed'
   set file. This step also has two hooks into the process, if necessary.

While knowledge of the internal workings of *builds* is not necessary to write build scripts, it is very important to
understand that build files are not typical Python scripts. They do not get run or exec'ed from start to end. The build
files only accept a small number of pre-defined functions which provide a way to script the above seven steps.
Internally, the functions defined in a build file are 'injected' into, and called from within the main BuildPackage
class defined in `build_package.py`. The upshot of this is that any code written outside of these predefined functions
(including module import statements) will be silently ignored.

The namespace into which these functions are injected contains a few useful Python standard library modules, as well
as a suite of helpful functions provided by *builds*. They are:

1. [os](https://docs.python.org/3/whatsnew/3.13.html#os)
2. [glob](https://docs.python.org/3/whatsnew/3.13.html#glob)
3. [subprocess](https://docs.python.org/3/whatsnew/3.13.html#subprocess)
4. 'cf' - *builds*-specific functions defined in `common_functions.py`

While these modules generally provide all the necessary tools, if there is popular demand I may introduce more.
`shutils` and `pathlib` may be useful additions. If you really need the functionality from another standard library
module, or external package, you can import it from within the predefined functions.

The first thing to define in a build file is any dependencies. There is not yet a distinction between build-time and
run-time dependencies. There is not yet support for optional dependencies. So you will have to consider which
dependencies to list here in accordance with your own needs. It stands to reason, if there is not yet a build file
for a package listed as a dependency, you will have to write that too. Dependencies are specified using category/package
pairs seperated by commas like so:

      depend = "net-util/curl,app-editor/vim"

Since our example package OpenSSH does not have any explicit dependencies, we will omit his line.

## Predefined variables and functions

As the predefined variables and functions are defined within, and called from an enclosing class, variables must be
prefaced by `self`, and functions (more correctly: methods) must have `self` as the sole srgument. The `BuildPackage` 
class defines several instance variables available to the build scripts which may be useful. Here we are assuming 
that the builds_root specified in the configuration file is `/var/builds`:

         self.build       = 'app-arch/tar'
         self.name        = 'tar'
         self.version     = '1.28'
         self.sha256sum   = '9599b22ecd1d5787ad7d3b7bf0c59f312b3396d1e281175dd1f8a4014da621ff'
         self.src_url     = 'http://ftp.gnu.org/gnu/tar/tar-1.28.tar.xz'
         self.builds_root = '/var/builds'
         self.build_dir   = '/var/builds/app-arch/tar'
         self.build_file  = '/var/builds/app-arch/tar/tar-1.28.build.py'
         self.work_dir    = '/var/builds/app-arch/tar/work'
         self.seg_dir     - '/var/builds/app-arch/tar/work/seg'
         self.package     = 'tar-1.28.tar.xz'
         self.package_dir = 'tar-1.28'

# fetch_prehook() and fetch_posthook()

These two functions are hooks into the package download step. As is implied, prehook runs before the package is fetched,
and posthook is run after the package is fetched. These functions can be used to download other packages or patches if
required. For example, `git` distributes its manpages in a seperate tarball, so `git`'s build file contains:

      def fetch_posthook(self):
         url = f"https://www.kernel.org/pub/software/scm/git/git-manpages-{self.version}.tar.xz"
         cf.bold(f"Fetching {url.split('/')[-1]}")
         cf.download(url, url.split('/')[-1])

Here we can see two of the functions defined in `common_functions.py` being used. The first is `cf.bold()` which will
print any string argument to the console in bold text. `cf` also defines similar formatted output functions:
`cf.green()`, `cf.yellow()`, and `cf.red()`. All four of these functions have analogs that DO NOT include a newline
character. These functions have the same name but prefaced by `print_`, so, `cf.print_green()`, for example.

The second is `cf.download()`. This function takes two string arguments. The first is a web URL, and the second is 
a local filename. Apropos, when it comes to file paths, it is important to understand the directory from which the 
predefined functions are called, and thus, the PWD in relation to the function call. `fetch_prehook()` and
`fetch_posthook()` are both run from within the `./builds/distfiles/` directory, which is where all packages 
should be downloaded to.

Back to our example, OpenSSH does not require any special handline or downloads at this step, so we leave these
functions undefined.

## install_source_prehook() and install_source_posthook()

These are two more pre/post hooks into the extract package step. This is the appropriate place to script any changes
that need to be applied to the package source tree, such as edits to Makefiles and configure scripts, or applying
patches. The following snippet from the `coreutils` build file illustrates how to apply a patch:

      def install_source_posthook(self):
         os.chdir(self.package_dir)
         patchname = "coreutils-9.5-i18n-2.patch"
         os.system(f"patch -Np1 -i {cf.config['builds_root']}/distfiles/{patchname}")
         os.chdir(self.work_dir)

Note that `install_source_prehook()` is run from inside `distfiles/` (as the package has not yet been extracted) and
`install_source_posthook()` is run from inside `self.work_dir`, so we `os.chdir()` into the source tree to apply the
patch.

Again, OpenSSH requires no special patching or otherwise, so we will leave this undefined.

## configure()

For all packages that require configuration, this is the place to do it. Generally, the easiest way to do this is to
place the relevant command withing an `os.system()` call. It is considered better practice to use the newer 
`subprocess.run()` interface, and you are welcome to do so, but it is a bit more complicated, so I will use 
`os.system()` for our OpenSSH example:

      def configure(self:)
         return os.system("./configure --prefix=/usr "
                           "--sysconfdir=/etc/ssh "
                           "--with-privsep-path=/var/lib/sshd "
                           "--with-default-path=/usr/bin "
                           "--with-superuser-path=/usr/sbin:/usr/bin "
                           "--with-pid-dir=/run")

Note that I have directly returned the exit status of the `os.system` call here. The callers of `configure()`, `make()`
and `make_install()` all expect a return value of 0, so they know the commands ran successfully, and that they are 
free to continue. It doesn't matter how you do it, but if the code and commands you script in these functions run 
normally, you must return 0, and if they do not, you must return a non-zero exit.

Another thing to note is the `--prefix=/usr`. The [Linux from scratch](https://www.linuxfromscratch.org/) system that
I originally designed *builds* for, and the Gentoo system from which I have done most of *builds*'s development
and testing on, both make all of `/bin`, `/sbin`, and `/lib` as symlinks to their counterparts in `/usr`, so I have
gotten in the habit of installing to user. You can of course use a prefix of `/` or `/usr/local` if it better suits
your purposes. 

It should go without saying that `configure()` is run from within `self.package_dir`. It also bears repeating that
defining this function is optional. If you don't need to run configure, leave it undefined.

## make()

As the name would imply, this is where you would run `make` if necessary. It is generally quite simple:

      def make(self):
         return os.system(f"make {cf.config['makeopts']}")

Again we directly return the exit status of `os.system()` to the caller. `cf.config` is a dictionary
of key -> value pairs loaded from the configuration file when you run `bld`. In this case, we are using 'makeopts' to
pass `-j4` to the make command, to speed up compilation. You can define this in your configuration file. If it is not 
defined it will default to `-j1`.

`make()` is called from `self.package_dir`, and is an optional function.

## make_install()

This is the function from which to run your `make install` command. Again, I will re-itterate that this is NOT from
where files are installed to the live filesystem. This function should command `make` to install the files into 
a segregated directory, which is the predefined instance variable `self.seg_dir`, and will appear in the filesystem as
`./builds/net-util/openssh/work/seg`. It is not manditory to do this, but it is certainly a best practice. If your 
package is simple enough (or a binary package), it may be easier to just pluck the files you want to install from
within the package source tree (in the next step), and leave this function undefined.

For any non-trivial package, however, it is far preferable to install to the staging directory, as all the files you 
need to install will be nicely seperated into their appropriate directories under `seg/`.

      def make_install(self):
         return os.system(f"make DESTDIR={self.seg_dir} install")

Note the inclusion of `DESTDIR` here. This tells the install script to install files relative to `seg/`. After this
command runs, binaries will be installed in `work/seg/usr/bin`, libraries in `work/seg/usr/lib`, headers in
`work/seg/usr/include`, manpages in `work/seg/usr/share/man/man1` and so on.

It should be noted that not all packages honour `DESTDIR`. It is very important to read your package's README and
INSTALL files, and test before running a command that could bork your system. Most, if not all packages will have a
similar way to install the files to a segregated directory. Read the docs, and adjust this step as needed!

Now: This is generally a good place to stop and test your script, and make sure the package is building as expected.
`bld install` has a few options that make testing easier for us. The `-d` or `--dontclean` option will skip the cleaning
step, which preserves the work directory for inspection. The `-t` or `--test` option will make `bld` run right up until 
this step, then it will exit. This allows you to test a build without affecting the greater system. Try it now by
running:

      # bld -v install -dt openssh

If this runs without error, go and inspect the files installed under `./seg/`. This will give you an idea what files
you need to install, and where they should be installed for the next step.

## install()

This is the penultimate step which installs the build files into your live filesystem. This is the only function that
is required to be defined in a build file. The class `FileInstaller`, defined in `build_package.py` creates a dictionary
of useful file paths, and defines nine functions which install files and directories. It is very import to use these
functions, as they keep track of which files they have installed, and where they have put them. These paths are 
then written to a manifest file which will be located at `builds/net-util/openssh/openssh-9.9p1.manifest` for our
example. While it is certainly possible to define any valid Python code to put any file wherever you want, within 
this function, if the files are not wrangled through these functions they will not be placed in the manifest, and `bld`
will not know they are installed if you later decide to uninstall or update the package. This may result in orphaned
files, or other hard to track down breakages. If you decide to do this, you are on your own. Fair warning...

### Defined file paths

As mentioned, there is a dictionary instance variable available to this (and other) functions that make dealing with
paths easier:

      self.p = {

            'b': f"{ir}/bin",
            's': f"{ir}/sbin",
            'l': f"{ir}/lib",
            'e': f"{ir}/etc",
            'i': f"{ir}/include",
            'ub': f"{ir}/usr/bin",
            'ue': f"{ir}/usr/etc",
            'us': f"{ir}/usr/sbin",
            'ui': f"{ir}/usr/include",
            'ul': f"{ir}/usr/lib",
            'ule': f"{ir}/usr/libexec",
            'ulb': f"{ir}/usr/local/bin",
            'uls': f"{ir}/usr/local/sbin",
            'uli': f"{ir}/usr/local/include",
            'ull': f"{ir}/usr/local/lib",
            'ush': f"{ir}/usr/share",
            'man1': f"{ir}/usr/share/man/man1",
            'man2': f"{ir}/usr/share/man/man2",
            'man3': f"{ir}/usr/share/man/man3",
            'man4': f"{ir}/usr/share/man/man4",
            'man5': f"{ir}/usr/share/man/man5",
            'man6': f"{ir}/usr/share/man/man6",
            'man7': f"{ir}/usr/share/man/man7",
            'man8': f"{ir}/usr/share/man/man8",

            '_b': self.seg + "/bin",
            '_s': self.seg + "/sbin",
            '_l': self.seg + "/lib",
            '_e': self.seg + "/etc",
            '_i': self.seg + "/include",
            '_ub': self.seg + "/usr/bin",
            '_ue': self.seg + "/usr/etc",
            '_us': self.seg + "/usr/sbin",
            '_ui': self.seg + "/usr/include",
            '_ul': self.seg + "/usr/lib",
            '_ule': self.seg + "/usr/libexec",
            '_ulb': self.seg + "/usr/local/bin",
            '_uls': self.seg + "/usr/local/sbin",
            '_uli': self.seg + "/usr/local/include",
            '_ull': self.seg + "/usr/local/lib",
            '_ush': self.seg + "/usr/share",
            '_man1': self.seg + "/usr/share/man/man1",
            '_man2': self.seg + "/usr/share/man/man2",
            '_man3': self.seg + "/usr/share/man/man3",
            '_man4': self.seg + "/usr/share/man/man4",
            '_man5': self.seg + "/usr/share/man/man5",
            '_man6': self.seg + "/usr/share/man/man6",
            '_man7': self.seg + "/usr/share/man/man7",
            '_man8': self.seg + "/usr/share/man/man8"
        }

The first group are paths in the live filesystem, in which to install files. `{ir}` is defined as the `install_root`
read from the configuration file, which is set up during the installation of builds. For a system-wide install it is
simply an empty string, which means the paths resolve from the `/` (root) directory. For a default user install, this
will be the user's home directory, thus, assuming a --prefix of /usr in the configure step, files will be installed
under `/home/<user>/usr/`. 

The second group of paths, which are identical but for the underscore, are paths which lead to files installed under
the segregated directory. These paths may, but don't have to be, used as path arguments to the nine installation 
functions, which are enumerated now:

`self.inst_binary(frm: str, to: str)` - for installing binaries
`self.inst_script(frm: str, to: str)` - for installing scripts and other executable text files
`self.inst_library(frm: str, to: str)` - for installing library files
`self.inst_header(frm: str, to: str)` - for installing header files
`self.inst_manpage(frm: str, to: str, compress: bool = True)`- for installing manpages
`self.inst_symlink(target: str, name: str)` - for creating symlinks
`self.inst_config(frm: str, to: str` - for installing configuration files
`self.inst_directory(frm: str, to: str)` - for recursively installing entire directories
`self.inst_file(frm: str, to: str, mode: int = 644)` - for installing any file, with optional mode argument

All of these functions, except for `inst_directory()`, use the `install` shell command under the hood. This ensures all 
files are placed in the filesystem with proper ownership and permissions, and allows us to overwrite existing files
for an upgrade. The general signiture is to call them with the 'from' location as the first arg, and the 'to' location
as the second arg. *builds* compresses manpages using `bzip2` by default, but this can be disabled by passing an
optional `compress=False` third arg to `inst_manpage()`

So with that explanation, let's get back to our example and start by installing the binaries.

Taking a peak in `./seg/usr/bin` we can see that there are several binaries here. It is important to ascertain that
the binaries you install are actually binaries. `inst_binary()` strips them, and will raise an error if you try to
strip a script. `inst_script()` is functionally equivelant, but for the stripping, so use that for scripts, or if you
don't want your binaries stripped. It is a good idea to run `file` on 
these directories, as regular `ls -l` output will not distinguish between binaries and scripts:

      # for f in `ls`; do file ${f}; done
      scp: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, stripped
      sftp: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, stripped
      ssh: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, stripped
      ssh-add: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, stripped
      ssh-agent: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, stripped
      ssh-keygen: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, stripped
      ssh-keyscan: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, stripped

So we can see they are all in fact binaries, but they are already stripped. Not all packages do this, so it is good to 
check. Since they are stripped, we will use `inst_script`:

      def install(self):
         # Get all files in work/seg/usr/bin/, and install to /usr/bin/
         for file in os.listdir(self.p['_ub']):
            self.inst_script(f"{self.p['_ub']}/{file}", self.p['ub'])

Note that we only have to specify the destination directory for the second argument. 

OpenSSH has placed the stripped `sshd` binary in sbin/:

      # install sshd
      self.inst_script(f"{self.p['_us']}/sshd", self.p['ub'])

There are several helper binaries in `usr/libexec/`. They are all stripped:

      # install helper programs
      for file in os.listdir(self.p['_ule']):
         self_inst_script(f"{self.p['_ule']}/{file}", self.p['ule'])

There are only manpages left. They are seperated into man1, man5, and man8 directories:

      # install manpages
      for file in os.listdir(self.p['_man1']):
         self.inst_manpage(f"{self.p['_man1']}/{file}", self.p['man1'])
        
      for file in os.listdir(self.p['_man5']):
         self.inst_manpage(f"{self.p['_man5']}/{file}", self.p['man5'])

      # We can use glob if finer-grained control is wanted.
      # Note that glob returns full paths, rather than the 
      # relative paths from os.listdir(), so we have to adapt:
      for file in glob.glob(f"{self.p['_man8']}/s*.8"):
         self.inst_manpage(file, self.p['man8'])

There are three configuration files installed into `./seg/etc/ssh/`. Let's use `inst_directory()` to grab them:

      # install configuration files
         self.inst_directory(self.p['_e'] + '/ssh/', self.p['e'] + '/ssh/')

Note that you will want to include the trailing directory slash to BOTH path with `inst_directory`!

We are almost done. On to our final step...

## cleanup_prehook() and cleanup_posthook()

The cleanup step is automated, but we have our two hooks if needed. prehook is run from `self.package_dir` before the
work directory and source tree are deleted, and posthook is run from `self.build_dir` after the work directory is
deleted. This is a good place to script any needed post-installation tasks. For example, for OpenSSH, we may want to
create a 'sshd' user and group to run the daemon under. We can do that here:

      def cleanup_posthook(self):
         try:
            os.system("groupadd -g 50 sshd")
            os.system("useradd -c 'sshd PrivSep' -d /var/lib/sshd -g sshd -s /bin/false -u 50 sshd")
         except OSError as e:
            cf.yellow(f"Adding user/group 'sshd' failed: {e}")

