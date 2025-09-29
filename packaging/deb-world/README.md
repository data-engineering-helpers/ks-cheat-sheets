Knowledge Sharing (KS) - Cheat Sheets - Debian world
====================================================

# Table of Content (ToC)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/packaging/deb-world/README.md)
gives a few hints about housekeeping with Debian-based Linux distributions.

# References

## Data Engineering helpers
* [Data Engineering Helpers - Knowledge Sharing - Packaging - RPM world](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/packaging/rpm-world/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Packaging - Debian world (this repository)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/packaging/deb-world/README.md)

# Use cases

## Package management
* Display the list of installed packages:
```bash
$ dpkg --list | grep expat
ii  libexpat1:amd64             2.7.1-2                              amd64        XML parsing C library - runtime library
```

* Display the files of a given package:
```bash
$ dpkg -L libexpat1
...
/usr/lib/x86_64-linux-gnu/libexpat.so.1.10.2
/usr/lib/x86_64-linux-gnu/libexpatw.so.1.10.2
/usr/lib/x86_64-linux-gnu/libexpat.so.1
```

* Display the dependencies of a given package:
```bash
$ apt-cache depends libexpat1
libexpat1
  PreDepends: libc6
```

* Display which packages depend on a given package:
```bash
$ apt-cache rdepends libexpat1
libexpat1
Reverse Depends:
  libpython3.13
```

## Distribution maintenance
* Add a multimedia-oriented repository:
```bash
$ echo "deb http://www.debian-multimedia.org/ stable main" > /etc/apt/sources.list.d/multimedia.list
```

* Build an up-to-date package list
```bash
$ apt-get update
```

* Update the packages
```bash
$ apt-get upgrade
```

* Search for a package
```bash
$ apt-cache search mediawiki
```

* Install a package
```bash
$ apt-get install mediawiki
```

* Un-install a package, keeping the configuration files
```bash
$ apt-get remove mediawiki
```

* Un-install a package, with all the configuration files (do a back-up before!)
```bash
$ apt-get purge mediawiki
```

## Identify leaves
* Identify leaves with:
```bash
$ 
```

## Identify orphans
* Identify orphans with:
```bash
$ 
```


