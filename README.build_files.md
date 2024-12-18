# NAME

**build.py** - A specification of, and terse instruction on tools
available for writing build files.

# DESCRIPTION

**build.py** files are the platform and user-preference dependent
backend scripts that specify how to build the software, and where to
install the software once it is built. These scripts are kept in
per-package directories underneath an appropriate category in the main
builds file tree. The name of these files must be:

    <pkg name>-<pkg version>.build.py

where \<pkg name\> and \<pkg version\> are the name and version strings
exactly as specified in the builds database.

# Build Script Overview

The build script contains all the package-specific instructions on how
to configure, build, and install the package. *builds* models this
process in seven discrete steps, of which 3 are automatic, and 4 must be
manually specified in the build file. These steps are:

**Fetch the package**

This step is automated. As long as the download URL in the db is
correct, bld will download the package into the ./builds/distfiles/
directory automatically. bld will also verify the sha256 hash of the
downloaded file. There are two scriptable hooks into this process, if
needed.

**Extract the package into a work directory**  

This step is automated. bld will extract package tarballs into a
directory called \'work\' under the package directory. Again, there are
hooks into this step if needed. For example, you may want to apply
patches to the source.

**Configure the package**  

This is an optional step that can be specified manually if necessary.
This is where you would perform the ./configure step in the typical
configure/make/make install process.

**Make the package**  

Optional. This is where you would run make if necessary.

**Make install the package**  

Optional. This is where you would run make install. Note that this step
should not be used to install files to the live filesystem, but rather,
into a segregated staging directory.

**Installing the package**  

This step is required to be defined in the build file. This is where the
package files get installed into the live filesystem. A set of helper
functions and path variables are provided to make this easy.

**Cleanup**  

This step is automated. If all previous steps ran successfully, this
step will remove the temporary \'work\' directory, write a manifest of
installed files, and record the package and version into a special
\'installed\' set file. This step also has two hooks into the process,
if necessary.

While knowledge of the internal workings of builds is not necessary to
write build scripts, it is very important to understand that build files
are not typical Python scripts. They do not get run or executed from
start to end. The build files will run any valid Python code but only
within the bounds of a small number of pre-defined functions which
provide a way to script the above seven steps. Internally, the functions
defined in a build file are \'injected\' into, and called from within
the main BuildPackage class defined in build_package.py. This means that
any code written outside of these predefined functions (including module
import statements) is undefined and may cause bad things to happen.

The namespace that these functions are injected into contains a few
Python Standard Library modules that are useful for building and
installing the packages. These modules are **os** , **glob** , and
**subprocess.** Any other modules needed while have to be imported from
within the predefined functions. There are also some builds-specific
functions defined which are available using the **cf** namespace. These
functions are specified in the following section.

# Functions available via the cf namespace

*bold() and print_bold()*  

    cf.bold(msg: str) -> None
    cf.print_bold(msg: str) -> None

These functions will print bold text to the console. They are intended
for informational output to the user. The \'bold\' variant includes a
newline character, while \'print_bold\' does not.

*green() and print_green()*

    cf.green(msg: str) -> None
    cf.print_green(msg: str) -> None

These functions will print green text to the console, unless the user
has disabled coloured output. They are intended for informational output
to the user. The \'green\' variant includes a newline character, while
\'print_green\' does not.

*yellow() and print_yellow()*

    cf.yellow(msg: str) -> None
    cf.print_yellow(msg: str) -> None

These functions will print yellow text to the console, unless the user
has disabled coloured output. They are intended for cautionary output to
the user. The \'yellow\' variant includes a newline character, while
\'print_yellow\' does not.

*red() and print_red()*

    cf.red(msg: str) -> None
    cf.print_red(msg: str) -> None

These functions will print red text to the console, unless the user has
disabled coloured output. They are intended to relay errors to the user.
The \'red\' variant includes a newline character, while \'print_red\'
does not.

*download()*

    cf.download(url: str, filename: str) -> None

This function will download the file at \'url\' as \'filename\' in the
current working directory. This is useful if supplementary packages or
patches are necessary to build a package. Note that it is good form to
download all files with the potential for reuse into the distfiles
directory. This function will check if the requested file already exists
in distfiles before downloading again.

There are several other functions available through the **cf** namespace
which are defined in the file common_functions.py, which you can look up
if you like. They will not be listed here because of their limited
utility in build files. It is also possible to access values from the
configuration file by referencing cf.config\[\<key\>\].

# Predefined variables and functions

Because the build script functions are injected into and run from the
BuildPackage() class, the build scripts have access to a number of
instance variables that are useful for building packages. These
predefined variables (and the functions which will be enumerated soon)
must be prefaced by the \'self\' instance representation. Using the
example of the package tar version 1.28, and assuming a builds_root of
/var/builds, they are:

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

There is also a dictionary defined which contains abbreviated keys for
brevity, and useful file paths as values. The directory is simply
defined as \'p\', and again, must be prefaced with self. The keys that
are prefaced with an underscore expand to locations within the
predefined \'seg_dir\' segregated directory into which the \'make
install\' step should install the built files. The non-underscore
versions expand to paths in the live filesystem where the built files
will ultimately be installed. This dictionary is defined as so:

    ir = config['install_root']
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

        '_b': self.seg_dir + "/bin",
        '_s': self.seg_dir + "/sbin",
        '_l': self.seg_dir + "/lib",
        '_e': self.seg_dir + "/etc",
        '_i': self.seg_dir + "/include",
        '_ub': self.seg_dir + "/usr/bin",
        '_ue': self.seg_dir + "/usr/etc",
        '_us': self.seg_dir + "/usr/sbin",
        '_ui': self.seg_dir + "/usr/include",
        '_ul': self.seg_dir + "/usr/lib",
        '_ule': self.seg_dir + "/usr/libexec",
        '_ulb': self.seg_dir + "/usr/local/bin",
        '_uls': self.seg_dir + "/usr/local/sbin",
        '_uli': self.seg_dir + "/usr/local/include",
        '_ull': self.seg_dir + "/usr/local/lib",
        '_ush': self.seg_dir + "/usr/share",
        '_man1': self.seg_dir + "/usr/share/man/man1",
        '_man2': self.seg_dir + "/usr/share/man/man2",
        '_man3': self.seg_dir + "/usr/share/man/man3",
        '_man4': self.seg_dir + "/usr/share/man/man4",
        '_man5': self.seg_dir + "/usr/share/man/man5",
        '_man6': self.seg_dir + "/usr/share/man/man6",
        '_man7': self.seg_dir + "/usr/share/man/man7",
        '_man8': self.seg_dir + "/usr/share/man/man8"

Before we have a look at the functions where the seven steps of the
build process must be defined, we should talk a bit about users and
privileges. If you have installed builds in the user configuration, most
of this discussion will not concern you. Your build_root and
install_root will be in a user-owned (or at least user-writable)
location, and all commands will be run as the user you use to run
builds. For system-wide installs, however, there is more nuance.

During a system-wide installation the initialization script will have
created a non-privileged user and group, both named \'builds\'. While
**bld** must be run as root, the program will drop root privileges as
much as possible and run the majority of commands and code as user
\'builds\' right up until the penultimate step where the built files are
installed into the live filesystem. So if you need to do some
housekeeping tasks as root in order to build and install your package,
these commands will have to be run during the install or cleanup steps.
All steps prior to this will be run as \'builds\', and therefore, you
will only have privilege enough to write/edit/delete to files and
directories in the build_root and below, which includes the working
directory where the package source is actually build and installed into
the segregated directory.

It is best practice to perform as much work as is possible in pure
Python, however, in the course of building and installing software,
there are many times you will need to run shell commands. Builds
provides two wrapper functions for this purpose, and their call
signatures are identical:

    self.do(cmd: str, shell: bool = False, env: [None | dict] = None) -> int
    self.sudo(cmd: str, shell: bool = False, env: [None | dict] = None) -> int

As the names may imply, \'do\' is for non-privileged commands, and
\'sudo\' is for commands that must be run as root. As per the privilege
dropping described in the previous section, this means that \'sudo\' may
only be called during the install and cleanup steps. All other steps
should use \'do\', or it will cause an error.

Additionally, any dependencies must be listed in the build file first.
This is the only line of code that should exist outside of one of the 
supplied functions. Dependencies are listed in comma-delimited 
<category>/<package> strings like so:

    depend = "dev-lib/libunistring,dev-lib/libidn2"

# Step 1: Fetching

The fetching step is automated, however, there are two hooks you can
define if you need to customize this step:

    fetch_prehook()
    fetch_posthook()

As is implied, prehook runs before the package is fetched, and posthook
is run after the package is fetched. These functions can be used to
download other packages or patches if required. For example, git
distributes its manpages in a separate tarball, so git\'s build file
contains:

    def fetch_posthook(self):
       url = f"https://www.kernel.org/pub/software/scm/git/git-manpages-{self.version}.tar.xz"
       cf.bold(f"Fetching {url.split('/')[-1]}")
       cf.download(url, url.split('/')[-1])

When it comes to file paths, it is important to understand the directory
from which the predefined functions are called, and thus, the PWD in
relation to the function call. fetch_prehook() and fetch_posthook() are
both run from within the ./builds/distfiles/ directory, which is where
all packages should be downloaded to.

# Step 2: Extract the package into a work directory

    install_source_prehook()
    install_source_posthook()

These are two more pre/post hooks into the extract package step. This is
the appropriate place to script any changes that need to be applied to
the package source tree, such as edits to Makefiles and configure
scripts, or applying patches. The following snippet from the coreutils
build file illustrates how to apply a patch:

    def install_source_posthook(self):
        os.chdir(self.package_dir)
        patchname = "coreutils-9.5-i18n-2.patch"
        self.do(f"patch -Np1 -i {cf.config['builds_root']}/distfiles/{patchname}")
        os.chdir(self.work_dir)

Note that install_source_prehook() is run from inside distfiles/ (as the
package has not yet been extracted) and install_source_posthook() is run
from inside self.work_dir, so we os.chdir() into the source tree to
apply the patch.

Another use for these hooks is to correct a non-standard directory name.
Builds expects untarred package directory names to be in the form
\<packagename-version\>. While most packages follow this convention, you
may encounter some that do not, and they will have to be renamed
manually in order for builds to continue. Here is an example of
renameing the package directory for liburcu:

    def install_source_posthook(self):
        os.rename(f"userspace-rcu-{self.version}", f"liburcu-{self.version}")

# Step 3: Configure the package

    configure()

For all packages that require configuration, this is the place to do it.
Generally, this step requires only wrapping an appropriate configure
command into a call to self.do(), as shown in this example from the
OpenSSH build file:

    def configure(self):
        conf_d = '/etc/ssh' if cf.config['user'] == 'root' else '/usr/etc/ssh'
        return self.do("./configure --prefix=/usr "
                       f"--sysconfdir={conf_d} "
                       "--with-privsep-path=/var/lib/sshd "
                       "--with-default-path=/usr/bin "
                       "--with-superuser-path=/usr/sbin:/usr/bin "
                       "--with-pid-dir=/run")

Note that we have modified the \'\--sysconfdir\' variable depending on
which user is specified in the configuration file. Also note that I have
directly returned the exit status of the self.do() call here. The
callers of configure(), make() and make_install() all expect a return
value of 0, so they know the commands ran successfully, and that they
are free to continue. It doesn\'t matter how you do it, but if the code
and commands you script in these functions run normally, you must return
0, and if they do not, you must return a non-zero exit.

Another thing to note is the \--prefix=/usr. The Linux from scratch
system that I originally designed builds for, and the Gentoo system from
which I have done most of builds\'s development and testing on, both
make all of /bin, /sbin, and /lib as symlinks to their counterparts in
/usr, so I have gotten in the habit of installing to user. You can of
course use a prefix of / or /usr/local if it better suits your purposes.

It should go without saying that configure() is run from within
self.package_dir. It also bears repeating that defining this function is
optional. If you don\'t need to run configure, leave it undefined.

# Step 4: Make the package

    make()

As the name would imply, this is where you would run make if necessary.
It is generally quite simple:

    def make(self):
        return self.do(f"make {cf.config['makeopts']}")

Again we directly return the exit status of self.do() to the caller.
cf.config is a dictionary of key -\> value pairs loaded from the
configuration file when you run bld. In this case, we are using
\'makeopts\' to pass -j4 to the make command, to speed up compilation.
You can define this in your configuration file. If it is not defined it
will default to -j1. make() is called from self.package_dir, and is an
optional function.

# Step 5: Make install the package

    make_install()

This is the function from which to run your make install command. Again,
I will re-iterate that this is NOT from where files are installed to the
live filesystem. This function should command make to install the files
into a segregated directory, which is the predefined instance variable
self.seg_dir, and will appear in the filesystem as
./builds/\<category\>/\<pkgname\>/work/seg. It is not mandatory to do
this, but it is certainly a best practice. If your package is simple
enough (or a binary package), it may be easier to just pluck the files
you want to install from within the package source tree (in the next
step), and leave this function undefined.

For any non-trivial package, however, it is far preferable to install to
the staging directory, as all the files you need to install will be
nicely separated into their appropriate directories under seg/:

    def make_install(self):
        return self.do(f"make DESTDIR={self.seg_dir} install")

Note the inclusion of DESTDIR here. This tells the install script to
install files relative to seg/. After this command runs, binaries will
be installed in work/seg/usr/bin, libraries in work/seg/usr/lib, headers
in work/seg/usr/include, manpages in work/seg/usr/share/man/man1 and so
on.

Most, if not all build systems have some sort of mechanism analogous to
DESTDIR. You may have to read some documentation to discover it for your
package\'s build system. Some, like ninja, use DESTDIR, but want the
environmental variable specified first in the command line, rather than
in the middle, as in the above example. This causes problems, as
subprocess.run(), which is the command that self.do() directly calls,
expects the first argument to be a command, and it will throw an error
(FileNotFoundError) when you try to pass an env var first. There is a
workaround. libpsl uses ninja, and so during make_install we will put
the DESTDIR env var in a dictionary, and pass it as an optional arg to
self.do():

    def make_install(self):
        env = {'DESTDIR': self.seg_dir}
        return self.do(f"ninja install", env=env)

# Step 6: Install the package to the live filesystem

    install()

This is the penultimate step which installs the build files into your
live filesystem. This is the only function that is required to be
defined in a build file. Along with the self.p path dictionary explained
above, there are nine predefined functions which should be used to
install the files. They are:

    self.inst_binary(frm: str, to: str) - for installing binaries
    self.inst_script(frm: str, to: str) - for installing scripts and other executable text files
    self.inst_library(frm: str, to: str) - for installing library files
    self.inst_header(frm: str, to: str) - for installing header files
    self.inst_manpage(frm: str, to: str, compress: bool = True)- for installing manpages
    self.inst_symlink(target: str, name: str) - for creating symlinks
    self.inst_config(frm: str, to: str - for installing configuration files
    self.inst_directory(frm: str, to: str) - for recursively installing entire directories
    self.inst_file(frm: str, to: str, mode: int = 644) - for installing any file, with optional mode argument

All of these functions, except for inst_directory(), use the install
shell command under the hood. This ensures all files are placed in the
filesystem with proper ownership and permissions, and allows us to
overwrite existing files for an upgrade. The general signature is to
call them with the \'from\' location as the first arg, and the \'to\'
location as the second arg. builds compresses manpages using bzip2 by
default, but this can be disabled by passing an optional compress=False
third arg to inst_manpage(). The inst_file() function accepts an
optional \'mode\' argument if you need something other than the default
644 permissions.

It is very important to only use these provided functions to install
files, as when wrangled through these functions all files and
directories are tracked and written to the manifest file. If you
manually install files outside of these functions builds will not know
about them, and you may have orphaned files on your system if you try to
uninstall or upgrade the package later!

Here is the install() function for the OpenSSSh package, which
demonstrates the use of most of them:

    def install(self):
        # Get all files in work/seg/usr/bin/, and install to /usr/bin/
        for file in os.listdir(self.p['_ub']):
            self.inst_script(f"{self.p['_ub']}/{file}", self.p['ub'])

        # install sshd
        self.inst_script(f"{self.p['_us']}/sshd", self.p['us'])

        # install helper programs to /usr/libexec
        for file in os.listdir(self.p['_ule']):
            self.inst_script(f"{self.p['_ule']}/{file}", self.p['ule'])

        # install manpages
        for file in os.listdir(self.p['_man1']):
            self.inst_manpage(f"{self.p['_man1']}/{file}", self.p['man1'])

        for file in os.listdir(self.p['_man5']):
            self.inst_manpage(f"{self.p['_man5']}/{file}", self.p['man5'])

        for file in os.listdir(self.p['_man8']):
            self.inst_manpage(f"{self.p['_man8']}/{file}", self.p['man8'])

        # install configuration files
        conf_d = 'e' if cf.config['user'] == 'root' else 'ue'
        self.inst_directory(self.p['_' + conf_d] + '/ssh/', self.p[conf_d] + '/ssh/')

        # Install ssh-copy-id and manpage
        self.inst_script(f"{self.work_dir}/{self.package_dir}/contrib/ssh-copy-id", self.p['ub'])
        self.inst_manpage(f"{self.work_dir}/{self.package_dir}/contrib/ssh-copy-id.1", self.p['man1'])

This example from libyaml shows how to install header files, and install
library files and their symlinks:

    def install(self):
        self.inst_header(self.p['_ui'] + "/yaml.h", self.p['ui'])

        self.inst_library(self.p['_ul'] + "/libyaml-0.so.2.0.9", self.p['ul'])
        self.inst_symlink(self.p['ul'] + "/libyaml-0.so.2.0.9", self.p['ul'] + "/libyaml-0.so.2")
        self.inst_symlink(self.p['ul'] + "/libyaml-0.so.2.0.9", self.p['ul'] + "/libyaml-0.so")

        self.inst_file(self.p['_ul'] + "/pkgconfig/yaml-0.1.pc", self.p['ul'] + "/pkgconfig/")

# Step 7: Cleanup

    cleanup_prehook()
    cleanup_posthook()

The cleanup step is automated, but we have our two hooks if needed.
prehook is run from self.package_dir before the work directory and
source tree are deleted, and posthook is run from self.build_dir after
the work directory is deleted. This is a good place to script any needed
post-installation tasks. For example, for OpenSSH, we may want to create
a \'sshd\' user and group to run the daemon under. We can do that here:

    # This will only work on a system install.
    def cleanup_posthook(self):
        if cf.config['user'] != 'root':
            return
        # Check if sshd user already exists...
        import pwd
        try:
            pwd.getpwnam("sshd")
            return
        except KeyError:
            pass
        try:
            # UID/GID 50 to match LFS/BLFS
            cf.bold("Creating user/group 'sshd'")
            self.sudo("install -v -g sys -m700 -d /var/lib/sshd")
            self.sudo("groupadd -g 50 sshd")
            self.sudo("useradd -c 'sshd PrivSep' -d /var/lib/sshd -g sshd -s /bin/false -u 50 sshd")
        except OSError as e:
            cf.yellow(f"Adding user/group 'sshd' failed: {e}")

Note the use of self.sudo() rather than self.do() for these commands
that must be run as root.

# Conclusion

So that\'s how to write a build file in a nutshell. Every package can be
different, and you will have to go through a manual process of
determining how they want to be built, and how they can be scripted in a
build file. Thankfully, most packages do not stray far from the typical
\'configure, make, make install\' three-step process.

If you\'ve actually read all the way to the end of this document you may
be thinking to yourself that writing build files is hopelessly
complicated. It really is not. Most are quite simple and
straightforward. I strongly suggest reading a few of them using this
documentation for context on what they are doing.

# SEE ALSO

**bld(1)**

# BUGS

The author strongly prefers you report bugs by opening an issue at the
**builds** github page:
**https://github.com/DarrenKirby/builds/issues.** If you do not have a
github account, please send an email to \<bulliver@gmail.com\>

# AUTHOR

Darren Kirby \<bulliver@gmail.com\>
