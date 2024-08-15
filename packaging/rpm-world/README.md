Knowledge Sharing (KS) - Cheat Sheets - RPM world
=================================================

# Table of Content (ToC)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/packaging/rpm-world/README.md)
gives a few hints about housekeeping with RPM-based Linux distributions.

# References

## Data Engineering helpers
* [Data Engineering Helpers - Knowledge Sharing - Packaging - RPM world (this repository)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/packaging/rpm-world/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Packaging - Debian world](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/packaging/deb-world/README.md)

## Fedora
* [Fedora forum - Preferred Fedora Housecleaning/Package Cleanup?](https://forums.fedoraforum.org/showthread.php?330282-Preferred-Fedora-Housecleaning-Package-Cleanup)
* [Fedora docs - Packaging guidelines](https://docs.fedoraproject.org/en-US/packaging-guidelines/)

# Use cases

## Identify leaves
* Identify leaves with:
```bash
$ dnf leaves
```

## Identify orphans
* Identify orphans with:
```bash
$ rpmorphan
```


