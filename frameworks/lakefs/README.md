Cheat Sheet - LakeFS
====================

# Table of Content (ToC)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/lakefs/README.md)
explains how to install and to use [LakeFS](https://lakefs.io/) on premises,
_e.g._, on a laptop or on a virtual machine (VM).

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
* [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md)

## PostgreSQL
* [PostgreSQL](https://www.postgresql.org) is a dependency of LakeFS
* See [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md)
  for more details on how to install some PostgreSQL server/service

## Minio
* [Minio](https://min.io/) is a dependency for on-premise deployment
* See [Data Engineering Helpers - Knowledge Sharing - Minio](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/minio/README.md)
  for more details on how to install the Minio service

## DuckDB
* [DuckDB](https://duckdb.org/) is fully integrated with the LakeFS web console.
  That is, LakeFS relies on an embedded DuckDB engine to browse and alter data
  on LakeFS repositories
* From the command-line, or from a Python editor (_e.g._, iPython, Jupyter),
  DuckDB has to be configured to interact with LakeFS
  + [LakeFS doc - Using lakeFS with DuckDB](https://docs.lakefs.io/integrations/duckdb.html)
  + [DuckDB doc - HTTPFS extension](https://duckdb.org/docs/extensions/httpfs.html)

## LakeFS
* GitHub repository: https://github.com/treeverse/lakeFS
* End-to-end Write-Audit-Publish (WAP) pattern with LakeFS:
  https://lakefs.io/blog/write-audit-publish-with-lakefs/

### Installation of LakeFS
* On premises deployment: https://docs.lakefs.io/howto/deploy/onprem.html
* Deploy LakeFS on AWS: https://docs.lakefs.io/howto/deploy/aws.html
* LakeFS command-line (CLI) tool: https://docs.lakefs.io/reference/cli.html

# Quickstart

## Launch the LakeFS service
* If not already done so, launch the LakeFS service from a terminal tab
  dedicated to LakeFS (so that the logs produced by the service may be seen
  while the service is operating):
```bash
$ lakefs --config ~/.lakefs/config.yaml run
```

## Browse the data from the web console
* Browse some specific data objects on a given repository (_e.g._, `silver`
  repository and `lakes.parquet` data file here):
  http://localhost:8000/repositories/silver/object?ref=main&path=lakes.parquet

* Query the data with DuckDB-powered SQL (_e.g._, top five of the lakes
  by countries):
```sql
SELECT   country, COUNT(*) as nb_lakes
FROM     READ_PARQUET('lakefs://silver/main/lakes.parquet')
GROUP BY country
ORDER BY nb_lakes
DESC LIMIT 5;
```

## Browse the data from DuckDB on the CLI
* Basically, once configured properly, the only difference between using the
  LakeFS web UI embedded version of DuckDB and DuckDB on the command-line
  is the prefix/scheme used in the paths. The path is:
  + `lakefs://` for the LakeFS embedded DuckDB engine
  + `s3://` for DuckDB on the command-line (CLI)

* If not already done so, clone
  [this Git repository](https://github.com:data-engineering-helpers/ks-cheat-sheets)
  and go into it:
```bash
$ mkdir -p ~/dev/knowledge-sharing && \
  git clone git@github.com:data-engineering-helpers/ks-cheat-sheets.git ~/dev/knowledge-sharing/ks-cheat-sheets
  cd ~/dev/knowledge-sharing/ks-cheat-sheets/frameworks/lakefs
```

* From the command-line (CLI), from within this project LakeFS directory,
  launch DuckDB:
```bash
$ duckdb db.duckdb
```

* Setup DuckDB to access LakeFS (the access key credentials may be seen in the
  `~/.lakectl.yaml` file):
```sql
D INSTALL httpfs;
  LOAD httpfs;
  SET global s3_region='eu-west-1';
  SET global s3_endpoint='localhost:8000';
  SET global s3_access_key_id='AKIAIOSFODNN7EXAMPLE';
  SET global s3_secret_access_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY';
  SET global s3_url_style='path';
  SET global s3_use_ssl=false;
```

* Query the data from LakeFS (_e.g._, the `lakes.parquet` file on the silver
  repository here):
```sql
$ SELECT country, COUNT(*) as nb_lakes FROM READ_PARQUET('s3://silver/main/lakes.parquet') GROUP BY country ORDER BY nb_lakes DESC LIMIT 5;
┌──────────────────────────┬──────────┐
│         Country          │ nb_lakes │
│         varchar          │  int64   │
├──────────────────────────┼──────────┤
│ Canada                   │    83819 │
│ United States of America │     6175 │
│ Russia                   │     2524 │
│ Denmark                  │     1677 │
│ China                    │      966 │
└──────────────────────────┴──────────┘
```

* Create a DuckDB table with the content of the Parquet file:
```sql
D CREATE OR REPLACE TABLE lakes AS SELECT * FROM READ_PARQUET('s3://silver/main/lakes.parquet');
```

* Check that the DuckDB table has been created correctly:
```sql
D SELECT country, COUNT(*) as nb_lakes FROM lakes GROUP BY country ORDER BY nb_lakes DESC LIMIT 5;
```

## Create a publication branch
* Create a branch from the command-line (CLI):
```bash
$ lakectl branch create \
  lakefs://silver/denmark-lakes \
  --source lakefs://silver/main
Source ref: lakefs://silver/main
created branch 'denmark-lakes' 908dbxxxa7787
```

* Alter the data on the newly created branch
  + Visit
    http://localhost:8000/repositories/silver/object?ref=denmark-lakes&path=lakes.parquet
  + Replace the SQL query by the following, which will create a DuckDB table
    with the content of the Parquet file:
```sql
CREATE OR REPLACE TABLE lakes AS 
    SELECT * FROM READ_PARQUET('lakefs://silver/denmark-lakes/lakes.parquet');
```
  + Check that the DuckDB table has been created correctly:
```sql
SELECT   country, COUNT(*) as nb_lakes
FROM     lakes
GROUP BY country
ORDER BY nb_lakes
DESC LIMIT 5;
```
  + Alter the data, _e.g._, remove any lake record not located in Denmark:
```sql
DELETE FROM lakes WHERE Country != 'Denmark';
```
  + Check that the DuckDB table has been altered correctly:
```sql
SELECT   country, COUNT(*) as nb_lakes
FROM     lakes
GROUP BY country
ORDER BY nb_lakes
DESC LIMIT 5;
```

* Write the data back to LakeFS in the publication branch:
```sql
COPY lakes TO 'lakefs://silver/denmark-lakes/lakes.parquet';
```

* Check that the data has changed on the publication branch:
```sql
DROP TABLE lakes;

SELECT   country, COUNT(*) as nb_lakes
FROM     READ_PARQUET('lakefs://silver/denmark-lakes/lakes.parquet')
GROUP BY country
ORDER BY nb_lakes
DESC LIMIT 5;
```

* Commit the changes of the publication branch:
```bash
$ lakectl commit lakefs://silver/denmark-lakes \
  -m "Create a dataset of just the lakes in Denmark"
Branch: lakefs://silver/denmark-lakes
Commit for branch "denmark-lakes" completed.

ID: 25fed72dxxx7aa92
Message: Create a dataset of just the lakes in Denmark
Timestamp: 2023-09-20 12:06:18 +0200 CEST
Parents: 908db9xxx7787
```

## Merge the publication branch
* Merge the publication branch onto the main branch:
```bash
$ lakectl merge \
  lakefs://silver/denmark-lakes \
  lakefs://silver/main
Source: lakefs://silver/denmark-lakes
Destination: lakefs://silver/main
Merged "denmark-lakes" into "main" to get "110dxxxd141".
```

## Revert changes
* Roll-back the changes:
```bash
$ lakectl branch revert \
  lakefs://silver/main \
  main --parent-number 1 --yes
Branch: lakefs://silver/main
commit main successfully reverted
```

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
