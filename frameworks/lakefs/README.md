Cheat Sheet - LakeFS
====================

# Table of Content (ToC)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/lakefs/README.md)
explains how to install and to use LakeFS on premises, _e.g._, on a laptop
or on a virtual machine (VM).

> LakeFS is Data Version Control (Git for Data)
>
> lakeFS is an open-source tool that transforms object storage into a Git-like
> repository. It enables to manage your data lake the way code is managed.
>
> With lakeFS you can build repeatable, atomic, and versioned data lake
> operations - from complex ETL jobs to data science and analytics.
>
> lakeFS supports AWS S3, Azure Blob Storage, and Google Cloud Storage
> as its underlying storage service. It is API compatible with S3 and works
> seamlessly with all modern data frameworks such as Spark, Hive, AWS Athena,
> DuckDB, and Presto.

# References

## Minio
* [Minio](https://min.io/) is a dependency for on-premise deployment
* Install and deploy Minio on MacOS:
  https://min.io/docs/minio/macos/operations/installation.html
* Install and deploy containerized Minio:
  https://min.io/docs/minio/container/operations/installation.html

## LakeFS
* GitHub repository: https://github.com/treeverse/lakeFS
* End-to-end Write-Audit-Publish (WAP) pattern with LakeFS:
  https://lakefs.io/blog/write-audit-publish-with-lakefs/

### Installation
* On premises deployment: https://docs.lakefs.io/howto/deploy/onprem.html
* Deploy LakeFS on AWS: https://docs.lakefs.io/howto/deploy/aws.html

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
$ vrew services start minio
```

* The Minio data lake is now accessible through http://localhost:9090/

* Specify an alias for the Minio service for the Minio client:
```bash
$ . /etc/default/minio
  mc alias set myminio http://localhost:9000 $MINIO_ROOT_USER $MINIO_ROOT_PASSWORD
```

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
