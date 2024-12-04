# For LFS/BLFS users

As stated, I wrote `builds` with a Linux from Scratch system specifically in mind, and while the front-end is for the 
most part portable across all Unix-like systems, the provided build script library is tailored specifically for a fresh
LFS/BLFS install.

I have tried to stay within the spirit of the LFS/BLFS books inasmuch as possible, but my buildscripts do deviate in 
some ways. Most notably: the build scripts do not install extra documentation, only man pages. This is a personal 
preferance of my own. I just don't see the value in installing HTML docs, Gnu info pages, and the like when I find 
myself pretty much always using online documentation. It especially annoys me when this extra documentation does nothing
but place a plain-text README file in /usr/share/docs/<packagename>.

The second notable difference is that my build files do not (yet) install i18n nls files. This is not because I do 
not feel they are usful, I absolutely understand their utility, I'm just honestly ignorant on exactly how it works. At 
some point I will write code that allows users to specify which locales/languages they want installed, and install only 
those, but I need to educate myself more on how this works first. 

Another difference is that `builds` will compress manpages by default, using bzip2. If you don't like this, you can edit
the build scripts and pass `compress=False` to all inst_manpage() calls.

## Installation

Presently, the only way to install `builds` is to use `git` and clone the working tree from GitHub. If you have not yet 
installed `git`, its installation is documented in the BLFS book. Once installed, simply cd to /var and run:

    # git clone https://github.com/DarrenKirby/builds.git

Once this is done, you need to initialize the `builds` database. Run:

    # cd builds/scripts
    # python initialize_builds_tree.py

Note that you MUST `cd` into 'scripts', as the initialization script uses the $PWD to determine file paths for the 
installation. This interactive script will prompt for configuration settings, for which you should accept the defaults
unless you know what you are doing. It will also create an unprivileged 'builds' user and group which the script uses 
for the majority of its functionality outside of installing files to the live filesystem.

Once installed, you can reinstall some of the LFS base packages to make `builds` aware of them. For the most part, all
files will be overwritten in place, with no issues. YMMV, but I installed `builds` in my own recently completed base 
LFS system and used builds to reinstall all available packages with no ill affect. The biggest issue, is that as 
`builds` compresses manpages, your man directories may contain duplicated uncompressed/compressed page pairs. You can 
use something like this to clean up the directories:

    find /path/to/manpages -type f -name '*.1' | while read -r uncompressed; do
      compressed="${uncompressed}.gz"
      bzipped="${uncompressed}.bz2"
      if [ -e "$compressed" ] || [ -e "$bzipped" ]; then
        echo "Deleting uncompressed manpage: $uncompressed"
        #rm "$uncompressed"
      fi
    done

Remove the pound sign from in front of `rm` if you are happy with what it's doing.

## Contributing

I would love some help with this! The documentation is not 100% there yet, as I'm focusing on implementing functionality 
and writing build scripts, but if you are saavy with LFS, building software from source, and have a bit of experience
with Python you should be able to figure it out. 

I have already written scripts for most of the LFS base packages, and added some BLFS packages to make a fresh install 
more useable, such as dhcpcd, iw, wpa_supplicant, links, lynx and some others. As far as build scripts, the focus should
be on writing scripts from the BLFS book.

Any contributions can be sent via pull requests on GitHub, or if you do not want to make a GitHub account you can just 
email me. Also feel free to email with comments/complaints/suggestions and requests for help writing build scripts.

Note that you should `git pull` from the main tree often, as `builds` is under heavy development, and changes daily.
If you have `sudo` installed on your system you can add:

    builds ALL=(ALL) NOPASSWD: /usr/bin/git

to /etc/sudoers then run:

    sudo -u builds git pull

If you do not have sudo, then you will have to git pull as root, then run:

    # chown -R builds:builds .

To change ownership of the files back to builds. I am working on a cleaner solution to this, and ultimately, will 
implement a command that performs the git pull from within builds itself.

Cheers!

