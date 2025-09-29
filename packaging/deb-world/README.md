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

## Package Management
* Add a multimedia-oriented repository
  * In `/etc/apt/sources.list`, add:
```bash
$ deb http://www.debian-multimedia.org/ stable main
```

* Display the list of installed packages:
```bash
$ dpkg --list | grep expat
```

* Display the files of a given package:
```bash
$ dpkg -L libexpat1
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


