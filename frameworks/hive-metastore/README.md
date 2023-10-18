Cheat Sheet - LakeFS
====================

# Table of Content (ToC)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/hive-metastore/README.md)
explains how to install and to use
[Hive Metastore](https://cwiki.apache.org/confluence/display/Hive/AdminManual+Metastore+3.0+Administration)
on premises, _e.g._, on a laptop or on a virtual machine (VM).

> Part of the larger Apache Hive data warehouse platform, the Hive metastore is a repository for details relating to Hive databases and their objects. It is adopted by Spark as the solution for storage of metadata regarding tables, databases and their related properties.  An essential element of Spark, it is worth getting to know this better so that it can be safeguarded and leveraged for development appropriately.

# References

## Data Engineering helpers
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box/blob/main/README.md)
* [Material for the Data platform - Data life cycle](https://github.com/data-engineering-helpers/data-life-cycle/blob/main/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Minio](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/minio/README.md)
* [Data Engineering Helpers - Knowledge Sharing - DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/README.md)

## Hive Metastore
* Hive home page: https://cwiki.apache.org/confluence/display/Hive/Home
  + [Hive doc - Admin manual for Metastore 3.0](https://cwiki.apache.org/confluence/display/Hive/AdminManual+Metastore+3.0+Administration)
  + Git repository: https://github.com/apache/hive/tree/master/metastore
    - [Git - PostgreSQL DDL script](https://github.com/apache/hive/blob/master/metastore/scripts/upgrade/postgres/hive-schema-2.3.0.postgres.sql)
	  ([copy of the PostgreSQL DDL script in this Git repository](sql/hive-schema-2.3.0.postgres.sql))
* [AWS blog post - How do I use a PostgreSQL database as the external metastore for Hive on Amazon EMR?](https://repost.aws/knowledge-center/postgresql-hive-metastore-emr)
* [Pivotal BI blog - The Hive Metastore and local development](https://pivotalbi.com/the-hive-metastore-and-local-development/),
  by Nigel Meakins, Dec. 2021
* JDBC driver for PostgreSQL: https://jdbc.postgresql.org/download/

# Installation

## Quick setup for the use cases
* Specify a few environment variables
  + For local PostgreSQL server on MacOS:
```bash
$ PG_SVR="localhost"; PG_ADM_USR="$USER"
```
  + For local PostgreSQL server on Linux:
```bash
$ PG_SVR="localhost"; PG_ADM_USR="postgres"
```
  + For AWS RDS PostgreSQL service (set the proxy endpoint to
    the AWS RDS proxy one):
```bash
$ PG_SVR="project-proxy.proxy-someid.us-east-1.rds.amazonaws.com"; PG_ADM_USR="postgres"
```

## PySpark
* If not already done so, install PySpark:
```bash
$ python -mpip install pyspark==3.4.1 delta-spark==2.4.0
```

## PostgreSQL database
* Install and/or set up a PostgreSQL database service, as detailed in the
 [Data Engineering Helpers - Cheat sheet for PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md)
* Sets up a `metastore` user and a `metastore` database, as detailed in the
  ["Hive Metastore database and user" section](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md#hive-metastore-database-and-user)
  of [that cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md)

* Launch the DDL script:
```bash
$ psql -h $PG_SVR -U metastore -f sql/hive-schema-2.3.0.postgres.sql
 nb 
----
 42
(1 row)
```

* Download the
  [JDBC driver for PostgreSQL](https://jdbc.postgresql.org/download/) and
  place it in the `$SPARK_HOME/jars/` directory:
```bash
$ curl https://jdbc.postgresql.org/download/postgresql-42.6.0.jar -o $SPARK_HOME/jars/postgresql-42.6.0.jar
```
