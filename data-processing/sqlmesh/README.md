Cheat Sheet - SQLMesh
=====================

# Table of Content (ToC)
* [Overview](#overview)
* [References](#references)
  * [Data Engineering helpers](#data-engineering-helpers)
  * [DuckDB](#duckdb)
  * [Articles](#articles)
    * [SQLMesh \- Migrate](#sqlmesh---migrate)
* [Quickstart](#quickstart)
* [Installation](#installation)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/README.md)
explains how to install and to use
[SQLMesh](https://sqlmesh.readthedocs.io/en/stable/) with
[DuckDB](https://duckdb.org/) on premises, _e.g._, on a laptop or
on a virtual machine (VM).

> [DuckDB](https://duckdb.org/) is an embedded database, similar to SQLite,
> but designed for OLAP-style analytics. It is crazy fast and allows you
> to read and write data stored in CSV, JSON, and Parquet files directly,
> without requiring you to load them into the database first.

> [SQLMesh](https://sqlmesh.readthedocs.io/en/stable/) SQLMesh is
> a next-generation data transformation framework designed to ship
> data quickly, efficiently, and without error. Data teams can efficiently
> run and deploy data transformations written in SQL or Python with
> visibility and control at any size.
> It is more than just a dbt alternative.

# References

## Data Engineering helpers
* [Data Engineering Helpers - Knowledge Sharing - dbt](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/dbt/README.md)
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box/blob/main/README.md)
* [Material for the Data platform - Data life cycle](https://github.com/data-engineering-helpers/data-life-cycle/blob/main/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Minio](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-storage/minio/README.md)
* [Data Engineering Helpers - Knowledge Sharing - DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/README.md)

## DuckDB
* Home page: https://duckdb.org/
  * [DuckDB doc - HTTPFS extension](https://duckdb.org/docs/extensions/httpfs.html)

## Articles

### SQLMesh - Migrate
* Overview: series of articles to explore SQLMesh and how it compares
  to dbt
* Author: David Jayatillake
* Date: Dec. 2024
* Link to the articles:
  * Migrate (the conclusion): https://substack.com/home/post/p-153375690
  * Init with dbt: https://davidsj.substack.com/p/sqlmesh-init-t-dbt
  * Init with DuckDB: https://davidsj.substack.com/p/sqlmesh-init-duckdb
  * Models kind 1: https://davidsj.substack.com/p/sqlmesh-model-kinds-1
  * Models kind 2: https://davidsj.substack.com/p/sqlmesh-model-kinds-2
  * Plan: https://davidsj.substack.com/p/sqlmesh-plan
  * Breaking and non-breaking changes: https://davidsj.substack.com/p/breaking-and-non-breaking-changes
  * Test: https://davidsj.substack.com/p/sqlmesh-test
  * Janitor: https://davidsj.substack.com/p/sqlmesh-janitor
  
* Excerpts from the conclusion:
> In short, if you use dbt-core and run it yourself in Airflow or
> in a container on cron etc, there is no reason not to switch to SQLMesh,
> and there are many reasons to do so.

> The fact that it’s backwards compatible with dbt means it can’t be ignored.
> I know that learning a new framework is a big deal for most data folks.
> You are under pressure to deliver instead of trying new tools,
> but you can even run an existing dbt project using sqlmesh and
> continue to keep building dbt models if you don’t want to learn
> the SQLMesh way. You get the benefits of virtual data environments
> and the sqlmesh plan/apply workflow, which are substantial for very little
> lift.

> Then, when you have time, you can try the SQLMesh model kinds and
> see that they are not so difficult or different to use.

# Quickstart

# Installation
