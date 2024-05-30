Cheat Sheet - Frameworks - Egeria
=================================

# Table of Content (ToC)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/egeria/README.md)
explains how to install and to use
[Egeria](https://github.com/odpi/egeria/)
on premises, _e.g._, on a laptop or on a virtual machine (VM).

# References

## Data Engineering helpers
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box/blob/main/README.md)
* [Material for the Data platform - Data life cycle](https://github.com/data-engineering-helpers/data-life-cycle/blob/main/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Minio](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/minio/README.md)
* [Data Engineering Helpers - Knowledge Sharing - DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/README.md)
* [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Hive Metastore](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/hive-metastore/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Trino](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/trino/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Dremio](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/dremio/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Java world](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/java-world/README.md)

## Egeria
* Egeria home page: https://egeria-project.org/
* GitHub project: https://github.com/odpi/egeria

## Articles
* [Medium - ](),
  by [Xxx](),
  May 2024

# Installation

## Egeria Git repository
* If not already done so, clone the Git repository of Egeria (beware that it takes up
  half a GB of storage on disk, and a good internet connection is therefore mandatory):
```bash
$ mkdir -p ~/dev/metadata && cd ~/dev/metadata
  git clone git@github.com:odpi/egeria.git
```

* Go into the Egeria project directory:
```bash
$ cd ~/dev/metadata/egeria
```

## Egeria as a standalone server without Docker
* Go into the standalone server directory:
```bash
$ cd open-metadata-distribution/omag-server-platform/build/unpacked/egeria*gz/assembly/platform
```

* Start the OMAG (Open Metadata and Governance) server:
```bash
$ java -Dloader.path=lib,extra -jar omag-server-platform*.jar
```

* To shutdown the server, just type Control-C in the terminal where Egeria was started

* In order to ease the launching of the Egeria server in the background,
  two Shell scripts are provided in this Git repository:
  * [GitHub - KS Egeria - `bin/egeria-start.sh`](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/egeria/bin/egeria-start.sh)
  * [GitHub - KS Egeria - `bin/egeria-screen.sh`](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/egeria/bin/egeria-screen.sh)
* If not already done so, install `screen`, _e.g._, on MacOS, `brew install screen`
* Copy those 2 scripts in the local `~/bin/` directory, so that the Egeria server may be launched and audited as following:
  * Installation:
```bash
$ mkdir -p ~/bin
  curl https://raw.githubusercontent.com/data-engineering-helpers/ks-cheat-sheets/main/frameworks/egeria/bin/egeria-start.sh -o ~/bin/egeria-start.sh
  curl https://raw.githubusercontent.com/data-engineering-helpers/ks-cheat-sheets/main/frameworks/egeria/bin/egeria-screen.sh -o ~/bin/egeria-screen.sh
  chmod +x ~/bin/egeria-*.sh
```
  * Start the Egeria server in a dedicated screen:
```bash
$ ~/bin/egeria-screen.sh
```
  * Go into the screen where the Egeria server has started:
```bash
$ screen -r egeria
```
  * When finished, stop the Egeria server by typing Control-C in the screen where the Egeria server runs
