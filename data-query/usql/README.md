Cheat Sheet - usql - Universal command-line interface for SQL databases
=======================================================================

# Table of Content (ToC)
* [Overview](#overview)
* [References](#references)
  * [Data Engineering helpers](#data-engineering-helpers)
  * [usql](#usql)
  * [Specific databases](#specific-databases)
* [Quickstart](#quickstart)
* [Installation](#installation)
  * [MacOS](#macos)
  * [Specific databases](#specific-databases-1)
    * [Databricks](#databricks)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-query/usql/README.md)
explains how to install and to use [usql](https://github.com/xo/usql), _e.g._,
on a laptop or on a virtual machine (VM).

# References
## Data Engineering helpers
* [Data Engineering Helpers - Knowledge Sharing - Python](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/python/)
* [Data Engineering Helpers - Knowledge Sharing - DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/)
* [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/)
* [Data Engineering Helpers - Knowledge Sharing - Unity Catalog (UC)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/unity-catalog/)
* [Data Engineering Helpers - Knowledge Sharing - Spark](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/)
* [Data Engineering Helpers - Knowledge Sharing - SQLMesh](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/)
* [Data Engineering Helpers - Knowledge Sharing - dbt](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/dbt/)
* [Data Engineering Helpers - Knowledge Sharing - Airflow](https://github.com/data-engineering-helpers/ks-cheat-sheets/tree/main/orchestrators/airflow)
* [Material for the Data platform - Data life cycle](https://github.com/data-engineering-helpers/data-life-cycle)
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box)

## usql
* GitHub page: https://github.com/xo/usql
* [Support for ODBC databases](https://github.com/xo/usql#database-support)

## Specific databases
* See [usql - Supported Database Schemes and Aliases](https://github.com/xo/usql/blob/master/README.md#supported-database-schemes-and-aliases)
  for the complete list of support databases

# Quickstart
```bash
TODAY_DATE=$(date +'%Y-%m-%d')
usql mydb -C -c "select * from mytable limit 10;"
```

# Installation

## MacOS
* With HomeBrew:
```bash
brew tap xo/xo
brew install usql
# brew install --with-odbc usql
```

## Specific databases
* The [YAML configuration](https://github.com/xo/usql?tab=readme-ov-file#configuration)
  has to be located where usql will fint it. For instance, on MacOS:
```bash
cat $HOME/Library/Application\ Support/usql/config.yaml
```

* Most of the drivers are written in Go.

### Databricks
* The Databricks connection uses the
  [Go driver of Databricks SQL](https://github.com/databricks/databricks-sql-go).

* The [connection string (DSN) is documented on Databricks web site](https://docs.databricks.com/aws/en/dev-tools/go-sql-driver#connect-with-a-dsn-connection-string)

* Example of configuration for Databricks SQL Warehouse from MacOS:
```bash
cat $HOME/Library/Application\ Support/usql/config.yaml
connections:
  dbsql: ["databricks", "token:dapi1XXXXXX@XXXXX.cloud.databricks.com:443/sql/1.0/warehouses/XXXXXX"]
```

* Then, to connect to the remote Databricks SQL Warehouse:
```bash
usql dbsql -c "select 42;"
 42
----
 42
(1 row)
```

