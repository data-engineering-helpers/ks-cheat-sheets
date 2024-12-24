Cheat Sheet - dbt
=================

# Table of Content (ToC)
* [Overview](#overview)
* [References](#references)
  * [Data Engineering helpers](#data-engineering-helpers)
  * [DuckDB](#duckdb)
  * [dbt](#dbt)
  * [dbt\-duckdb](#dbt-duckdb)
* [Quickstart](#quickstart)
* [Installation](#installation)
  * [Dependencies](#dependencies)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/dbt/README.md)
explains how to install and to use [dbt](https://getdbt.com/) with
[DuckDB](https://duckdb.org/) on premises, _e.g._, on a laptop or
on a virtual machine (VM).

> [DuckDB](https://duckdb.org/) is an embedded database, similar to SQLite,
> but designed for OLAP-style analytics. It is crazy fast and allows you
> to read and write data stored in CSV, JSON, and Parquet files directly,
> without requiring you to load them into the database first.

> [dbt](https://getdbt.com/) is the best way to manage a collection of data
> transformations written in SQL or Python for analytics and data science.
> [`dbt-duckdb`](https://github.com/duckdb/dbt-duckdb) is the project that ties
> DuckDB and dbt together, allowing you to create a
> [Modern Data Stack In A Box](https://duckdb.org/2022/10/12/modern-data-stack-in-a-box.html)
> or a simple and powerful data lakehouse with Python.

# References

## Data Engineering helpers
* [Data Engineering Helpers - Knowledge Sharing - SQLMesh](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/dbt/README.md)
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box/blob/main/README.md)
* [Material for the Data platform - Data life cycle](https://github.com/data-engineering-helpers/data-life-cycle/blob/main/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Minio](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-storage/minio/README.md)
* [Data Engineering Helpers - Knowledge Sharing - DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/README.md)

## DuckDB
* Home page: https://duckdb.org/
  * [DuckDB doc - HTTPFS extension](https://duckdb.org/docs/extensions/httpfs.html)

## dbt
* Home page: https://gitdbt.com

## `dbt-duckdb`
* Git repository: https://github.com/duckdb/dbt-duckdb

# Quickstart

# Installation
* Install `dbt-duckdb` as a Python module:
```bash
$ python -mpip install -U pip dbt-duckdb
```

* To enable persistency of the DuckDB-created tables in the
  [AWS Glue service](https://aws.amazon.com/glue/),
  install the Glue dependency:
```bash
$ python -mpip install -U "dbt-duckdb[glue]"
```

## Dependencies

