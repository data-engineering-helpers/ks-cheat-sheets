Cheat Sheet - Databases - Trino
===============================

# Table of Content (ToC)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/trino/README.md)
explains how to install and to use
[Trino (formerly Presto)](https://trino.io/)
on premises, _e.g._, on a laptop or on a virtual machine (VM).

> Part of the larger Apache Hive data warehouse platform, the Hive metastore is a repository for details relating to Hive databases and their objects. It is adopted by Spark as the solution for storage of metadata regarding tables, databases and their related properties.  An essential element of Spark, it is worth getting to know this better so that it can be safeguarded and leveraged for development appropriately.

# References

## Data Engineering helpers
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box/blob/main/README.md)
* [Material for the Data platform - Data life cycle](https://github.com/data-engineering-helpers/data-life-cycle/blob/main/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Minio](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/minio/README.md)
* [Data Engineering Helpers - Knowledge Sharing - DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/README.md)
* [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Hive Metastore](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/hive-metastore/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Java world](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/java-world/README.md)

## Trino
* Trino home page: https://trino.io/
  + Presto home page (still existing, as of end 2023): https://prestodb.io/
* GitHub project: https://github.com/trinodb/trino
* [Trino doc - Hive connector](https://trino.io/docs/current/connector/hive.html)

## Articles
* [Medium - Visualize parquet files with Apache Superset using Trino or PrestoSQL](https://sairamkrish.medium.com/visualize-parquet-files-with-apache-superset-using-trino-or-prestosql-511f18a37e3b),
  by [Sairam Krish](https://www.linkedin.com/in/sairamkrish/),
  Dec. 2021
  + [GitHub - Containerized Hive Metastore service](https://github.com/bitsondatadev/hive-metastore)
    - [GitHub - Containerized Hive Metastore service - `Dockerfile`](https://github.com/bitsondatadev/hive-metastore/blob/master/Dockerfile)
    - [GitHub - Containerized Hive Metastore service - `entrypoint.sh` service launch script](https://github.com/bitsondatadev/hive-metastore/blob/master/scripts/entrypoint.sh)
  + [GitHub - Trino demo - `metastore-site.xml` Hive Metastore client configuration](https://github.com/sairamkrish/trino-superset-demo/blob/main/hive/conf/metastore-site.xml)

# Installation

## Hive Metastore
* See the dedicated cheat sheet in this Git repository:
  [Data Engineering Helpers - Knowledge Sharing - Hive Metastore](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/hive-metastore/README.md)

## Trino
* On MacOS, install Trino with HomeBrew:
```bash
$ brew install trino
```

* Setup the Hive Metastore client
  (inspired by [GitHub - Trino demo - `metastore-site.xml` Hive Metastore client configuration](https://github.com/sairamkrish/trino-superset-demo/blob/main/hive/conf/metastore-site.xml))

* Launch the Trino service:
```bash
$ trino-server start
```

* Open the Trino administrative UI in a browser: http://192.168.1.99:8080/ui/

* On the command-line, get the status of the cluster:
```bash
$ trino
```
```sql
trino> SELECT * FROM system.runtime.nodes;
               node_id                |         http_uri         | node_version | coordinator | state  
--------------------------------------+--------------------------+--------------+-------------+--------
 9243b2b6-9a64-4e29-98e8-c2de6b698553 | http://192.168.1.99:8080 | 412          | true        | active 
(1 row)

Query 20231104_100933_00003_v65it, FINISHED, 1 node
Splits: 1 total, 1 done (100.00%)
0.64 [1 rows, 70B] [1 rows/s, 110B/s]
```
