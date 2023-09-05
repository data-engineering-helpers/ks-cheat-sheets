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
* LakeFS command-line (CLI) tool: https://docs.lakefs.io/reference/cli.html

# Installation

## PostgreSQL

### MacOS
* PostgreSQL, with the PostgreSQL client, may be installed on MacOS
  with HomeBrew:
```bash
$ brew install postgresql@15
```

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

## LakeFS server

### MacOS
* Install the LakeFS HomeBrew tap:
```bash
$ brew tap treeverse/lakefs
```

* Install LakeFS:
```bash
$ brew install lakefs
```

* Setup the LakeFS server configuration file
  + Download the sample into the LakeFS configuration directory:
```bash
$ mkdir -p ~/.lakefs
  https://raw.githubusercontent.com/data-engineering-helpers/ks-cheat-sheets/main/frameworks/lakefs/etc/config.yaml -o ~/.lakefs/config.yaml
```
  + Edit the LakeFS server configuration file, and specify the PostgreSQL
    connection string as well as the Minio access key (as setup in the above
	section):
```bash
$ vi ~/.lakefs/config.yaml
```

* Run the LakeFS server:
```bash
$ lakefs --config ~/.lakefs/config.yaml run &
```

* Perform the server setup by visiting http://localhost:8000/setup
  + Leave the admin username as suggested (`admin`)
  + Click on the "Setup" button
  + Access keys are then created. Make a note of them, as they will be needed
    in the section below to set up the LakeFS CLI

* Create a `silver` repository by visiting http://localhost:8000/repositories
  and clicking on the "Create repository" button. The details are as following:
  + Repository ID: `silver`
  + Default branch name: leave it as `main`
  + Storage namespace: `s3://silver/`. Here, `silver` corresponds to the
    Minio bucket setup in the above section
  + Click on the "Create" button

* The content of the newly created `silver` repository is available by
  visiting http://localhost:8000/repositories/silver/objects?ref=main
  
* The newly created content on LakeFS may also be browsed on Minio. However,
  like with Git, the object files are named according to IDs, which makes it
  very hard for a human being to recognize anything without the overlay of
  LakeFS
```bash
$ mc ls -r --summarize myminio/silver/data
```

## LakeFS CLI
* Generate the LakeFS configuration file for the CLI (to be stored as
  `/.lakectl.yaml`):
```bash
$ lakectl config
```

* Edit the LakeFS CLI configuration
  + Set up the access key as created in the above section (LakeFS server setup)
  + Specify the server endpoint to http://localhost:8000

* List the repositories:
```bash
$ lakectl repo list
+------------+--------------------------------+------------------+-------------------+
| REPOSITORY | CREATION DATE                  | DEFAULT REF NAME | STORAGE NAMESPACE |
+------------+--------------------------------+------------------+-------------------+
| silver     | 2023-09-05 22:50:11 +0200 CEST | main             | s3://silver/      |
+------------+--------------------------------+------------------+-------------------+
```

* List the content of the `silver` repository:
```bash
$ lakectl fs ls --recursive lakefs://silver/main/lakes.parquet
```
