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

## Data Engineering helpers
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box/blob/main/README.md)
* [Material for the Data platform - Data life cycle](https://github.com/data-engineering-helpers/data-life-cycle/blob/main/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Minio](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/minio/README.md)
* [Data Engineering Helpers - Knowledge Sharing - LakeFS](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/lakefs/README.md)

## Minio
* [Minio](https://min.io/) is a dependency for on-premise deployment
* See [Data Engineering Helpers - Knowledge Sharing - Minio](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/minio/README.md)
  for more details on how to install the Minio service

## LakeFS
* GitHub repository: https://github.com/treeverse/lakeFS
* End-to-end Write-Audit-Publish (WAP) pattern with LakeFS:
  https://lakefs.io/blog/write-audit-publish-with-lakefs/

### Installation of LakeFS
* On premises deployment: https://docs.lakefs.io/howto/deploy/onprem.html
* Deploy LakeFS on AWS: https://docs.lakefs.io/howto/deploy/aws.html
* LakeFS command-line (CLI) tool: https://docs.lakefs.io/reference/cli.html

# Installation

## Dependencies

### PostgreSQL

#### MacOS
* PostgreSQL, with the PostgreSQL client, may be installed on MacOS
  with HomeBrew:
```bash
$ brew install postgresql@15
```

### Minio
See [Data Engineering Helpers - Knowledge Sharing - Minio](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/minio/README.md)
for more details on how to install the Minio service

## LakeFS server

### Linux
TBC

### MacOS
* Install the LakeFS HomeBrew tap:
```bash
$ brew tap treeverse/lakefs
```

* Install LakeFS:
```bash
$ brew install lakefs
```

### General
* Setup the LakeFS server configuration file
  + Download the sample into the LakeFS configuration directory:
```bash
$ mkdir -p ~/.lakefs
  curl https://raw.githubusercontent.com/data-engineering-helpers/ks-cheat-sheets/main/frameworks/lakefs/etc/config.yaml -o ~/.lakefs/config.yaml
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
