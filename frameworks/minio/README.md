Cheat Sheet - Minio
===================

# Table of Content (ToC)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/minio/README.md)
explains how to install and to use Minio service on premises, _e.g._,
on a laptop or on a virtual machine (VM).

> MinIO is a high-performance, S3 compatible object store.
> It is built for large scale AI/ML, data lake and database workloads.
> It is software-defined and runs on any cloud or on-premises infrastructure.

# References

## Data Engineering helpers
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box/blob/main/README.md)
* [Material for the Data platform - Data life cycle](https://github.com/data-engineering-helpers/data-life-cycle/blob/main/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Minio](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/minio/README.md)
* [Data Engineering Helpers - Knowledge Sharing - LakeFS](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/lakefs/README.md)

## Minio
* Minio home page: https://min.io/
* Minio GitHub repository: https://github.com/minio/minio/

### Installation of Minio
* Install and deploy Minio on MacOS:
  https://min.io/docs/minio/macos/operations/installation.html
* Install and deploy Minio on Linux:
  https://min.io/docs/minio/linux/operations/installation.html
* Install and deploy containerized Minio:
  https://min.io/docs/minio/container/operations/installation.html

# Installation

## Minio

### MacOS
* Minio, with the Minio client, may be installed on MacOS with HomeBrew:
```bash
$ brew install minio/stable/minio
  brew install minio/stable/mc
```

* Create a default configuration file:
```bash
% sudo mkdir -p /etc/default
  sudo chown $USER /etc/default
  curl https://raw.githubusercontent.com/data-engineering-helpers/ks-cheat-sheets/main/frameworks/lakefs/etc/minio -o /etc/default/minio
```

* In that new Minio configuration file, adjust the `MINIO_VOLUMES`,
  administrative user and password values:
```bash
$ vi /etc/default/minio
```

* If, for some reason, HomeBrew does not install the Minio service (specified
  with a Plist file), copy the
  [MacOS service plist file](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/lakefs/etc/homebrew.mxcl.minio.plist)
  to the place where Minio was installed (that solution was documented
  as a
  [GitHub issue on Minio repository](https://github.com/minio/minio/issues/16382)):
```bash
$ export BREW_PFX="$(brew --prefix)"
  export MINIO_DIR="$(brew info minio|grep "^$BREW_PFX"|cut -d' ' -f1,1)"
  export MINIO_VOLUMES="$(grep "^MINIO_VOLUMES=" /etc/default/minio | cut -d'=' -f2,2 | sed -e 's/"//g')"
  curl https://raw.githubusercontent.com/data-engineering-helpers/ks-cheat-sheets/main/frameworks/lakefs/etc/homebrew.mxcl.minio.plist -o homebrew.mxcl.minio.plist.in
  envsubst < homebrew.mxcl.minio.plist.in > $MINIO_DIR/homebrew.mxcl.minio.plist
```

* Start the Minio service:
```bash
$ brew services start minio
```

* The Minio data lake is now accessible through http://localhost:9090/

* Specify an alias for the Minio service for the Minio client:
```bash
$ . /etc/default/minio
  mc alias set myminio http://localhost:9000 $MINIO_ROOT_USER $MINIO_ROOT_PASSWORD
```

### Linux
TBC

### General
* Create access key pair on http://localhost:9000/access-keys
  and take note of it. That key pair will be fed in the LakeFS service
  configuration file (`/.lakefs/config.yaml`, see below)

* Create some content
  + Create some buckets and folders:
```bash
$ mc mb myminio/bronze/geonames
  mc mb myminio/silver/geonames
  mc mb myminio/gold/geonames
```
  + Copy some Parquet data files (_e.g._, copy the Parquet files resulting from
    launching the
	[EL script](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/elt-geonames.py)
	in the [DuckDB cheat sheet folder](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/)):
```bash
$ mc cp db/duckdb/data/parquet/al*.parquet myminio/bronze/geonames
```

* Browse the content:
```bash
$ mc ls -r --summarize myminio/bronze
```

