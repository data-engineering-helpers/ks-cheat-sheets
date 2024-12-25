Cheat Sheet - SQLMesh
=====================

# Table of Content (ToC)
* [Overview](#overview)
* [References](#references)
  * [Data Engineering helpers](#data-engineering-helpers)
  * [DuckDB](#duckdb)
  * [Articles and Git knowledge sharing projects](#articles-and-git-knowledge-sharing-projects)
    * [SQLMesh \- Migrate](#sqlmesh---migrate)
    * [SQLMesh as alternative to dbt](#sqlmesh-as-alternative-to-dbt)
* [Quickstart](#quickstart)
  * [Simple example with DuckDB](#simple-example-with-duckdb)
  * [Full end\-to\-end example](#full-end-to-end-example)
* [Installation](#installation)
  * [BlueSky data](#bluesky-data)
  * [Clone this repository](#clone-this-repository)
  * [SQLMesh](#sqlmesh)

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

## Articles and Git knowledge sharing projects

### SQLMesh - Migrate
* Overview: series of articles to explore SQLMesh and how it compares
  to dbt
* Author: David Jayatillake
([David Jayatillake on LinkedIn](https://www.linkedin.com/in/david-jayatillake/),
  [David Jayatillake on Substack](https://substack.com/@davidsj))
* Date: Dec. 2024
* Publisher: Substack
* Link to the articles:
  * Migrate (the conclusion): https://substack.com/home/post/p-153375690
  * Init with dbt: https://davidsj.substack.com/p/sqlmesh-init-t-dbt
  * Init with DuckDB: https://davidsj.substack.com/p/sqlmesh-init-duckdb
  * Models kind 1: https://davidsj.substack.com/p/sqlmesh-model-kinds-1
  * Models kind 2: https://davidsj.substack.com/p/sqlmesh-model-kinds-2
  * Plan: https://davidsj.substack.com/p/sqlmesh-plan
  * Breaking and non-breaking changes:
  https://davidsj.substack.com/p/breaking-and-non-breaking-changes
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

### SQLMesh as alternative to dbt
* Title: Why SQLMesh Might be The Best dbt Alternative
* Author: Yuki Kakegawa
  ([Yuki Kakegawa on LinkedIn](https://www.linkedin.com/in/yukikakegawa/),
  [Yuki Kakegawa on Substack](https://substack.com/@yuki1))
* Date: Dec. 2024
* Link to the article:
  https://thedatatoolbox.substack.com/p/why-sqlmesh-might-be-the-best-dbt
* Publisher: Substack


###
* GitHub repository: https://github.com/mattiasthalen/arcane-insight/tree/main
* Title: Arcane insight
* Overview: Arcane Insight is a data analytics project designed to harness
  the power of SQLMesh and DuckDB to collect, transform, and analyze data from
  [Blizzard's Hearthstone API](https://develop.battle.net/documentation/hearthstone).
* Author: Mattias Thalén
 ([Mattias Thalén on LinkedIn](https://www.linkedin.com/in/mattias-thal%C3%A9n/),
  [Mattias Thalén on GitHub](https://github.com/mattiasthalen))
* Date: End of 2024

# Quickstart

## Simple example with DuckDB
* Reference:
  https://sqlmesh.readthedocs.io/en/stable/quickstart/cli/#3-update-a-model

* Change to the `simple-example` directory within the SQLMesh dedicated
  directory:
```bash
cd ~/dev/knowledge-sharing/ks-cheat-sheets/data-processing/sqlmesh/simple-example
```

* Clean/remove results of potential earlier tries (those files are ignored
  by Git):
```bash
rm -rf .cache logs db.db
```

* Launch the SQLMesh plan:
```bash
sqlmesh plan
======================================================================
Successfully Ran 1 tests against duckdb
----------------------------------------------------------------------
`prod` environment will be initialized

Models:
└── Added:
    ├── sqlmesh_example.full_model
    ├── sqlmesh_example.incremental_model
    └── sqlmesh_example.seed_model
Models needing backfill (missing dates):
├── sqlmesh_example.full_model: 2024-12-24 - 2024-12-24
├── sqlmesh_example.incremental_model: 2020-01-01 - 2024-12-24
└── sqlmesh_example.seed_model: 2024-12-24 - 2024-12-24
Apply - Backfill Tables [y/n]:
```

* Answer yes (`y`) to the prompted question ("backfill tables?"):
```bash
Creating physical tables ━━━━ ... ━━━━━ 100.0% • 3/3 • 0:00:00

All model versions have been created successfully

[1/1] sqlmesh_example.seed_model evaluated in 0.03s
[1/1] sqlmesh_example.incremental_model evaluated in 0.01s
[1/1] sqlmesh_example.full_model evaluated in 0.01s
Evaluating models ━━━━━━ ... ━━━━━━━ 100.0% • 3/3 • 0:00:00


All model batches have been executed successfully

Virtually Updating 'prod' ━━━━━━━ ... ━━━━━━━━ 100.0% • 0:00:00

The target environment has been updated successfully
```

* It will update the DuckDB database (`db.db`), which is ignored by Git

* Logs are available in the `logs/` sub-directory (also ignored by Git)
  and cache files are to be found in the `.cache/` sub-directory (also
  ignored by Git)

* If the SQLMesh plan is run again, this time, there will be no change
  (the SQLMesh commands are idempotent):
```bash
sqlmesh plan
======================================================================
Successfully Ran 1 tests against duckdb
----------------------------------------------------------------------
No changes to plan: project files match the `prod` environment
```

## Full end-to-end example
* Reference:
  https://sqlmesh.readthedocs.io/en/stable/examples/incremental_time_full_walkthrough/

* Change to the `e2e-example` directory within the SQLMesh dedicated
  directory:
```bash
cd ~/dev/knowledge-sharing/ks-cheat-sheets/data-processing/sqlmesh/e2e-example
```


# Installation

## BlueSky data
* That sub-section is the basis/data part of the
  [article by David Jayatillake](https://davidsj.substack.com/p/sqlmesh-init-duckdb).
  It will however not be used for now. Hence, its installation/cloning is
  purely optional

* Clone the Git repository and move into it:
```bash
mkdir -p ~/dev/infra
git clone https://github.com/djayatillake/bluesky-data ~/dev/infra/bluesky-data
cd ~/dev/infra/bluesky-data
```

* Launch the DuckDb shell:
```bash
$ duckdb
```

* (In DuckDB,) attach to the BlueSky data catalog:
```sql
D attach 'https://hive.buz.dev/bluesky/catalog' as bluesky;
```

* Check that the BlueSky data is available:
```sql
D select count(*)/1e6 as nb_rows from bluesky.jetstream;
┌─────────┐
│ nb_rows │
│ double  │
├─────────┤
│     1.0 │
└─────────┘
D select * from bluesky.jetstream limit 10;
```

* To leave the DuckDB shell, either type Control-D or the `.quit` command:
```sql
D .quit
```

## Clone this repository
* Clone this
  [Git repository](https://github.com/data-engineering-helpers/ks-cheat-sheets)
  and move into its SQLMesh directory:
```bash
mkdir -p ~/dev/knowledge-sharing
git clone https://github.com/data-engineering-helpers/ks-cheat-sheets ~/dev/knowledge-sharing/ks-cheat-sheets
cd ~/dev/knowledge-sharing/ks-cheat-sheets/data-processing/sqlmesh
```

## SQLMesh
* SQLMesh comes as a Python package, and may therefore installed simply with
  the Python packager. For instance:
```bash
python -mpip install -U sqlmesh
```

* The SQLMesh package installs two executable scripts, namely `sqlmesh` and
  `sqlmesh_cicd`, which are usually stored along side the other Python packages.
  For instance, with PyEnv, it will end up as wrappers in `~/.pyenv/shims/`.

* Usually, for the Shell (_e.g._, Bash or Zsh) to become aware of those newly
  installed executables scripts, it has to be refreshed (with the `exec`
  command)
  * For the Bash Shell:
```bash
exec bash
```
  * For the Zsh Shell:
```bash
exec zsh
```

* Check the version of the just installed SQLMesh package:
```bash
sqlmesh --version
0.141.1
```

* Note that most of the projetcs, to be found in Git repositories,
  have already been initialized; they no longer need initializing.

* Clean/remove results of potential earlier tries (those files are ignored
  by Git):
```bash
rm -rf .cache logs db.db
```

* To create a new project from scratch, execute the `sqlmesh init` command,
  specifying which
  [SQL dialect](https://github.com/tobymao/sqlglot/blob/main/sqlglot/dialects/dialect.py)
  to use (among, for instance, DataBricks, Drill, DuckDB, Hive, MySQL,
  PostgreSQL, Presto, Redshift, Snowflake, Spark, SQLite, Tableau, Trino)
  * The simple example, described in the
  [SQLMesh getting started page](https://sqlmesh.readthedocs.io/en/stable/quickstart/cli/#1-create-the-sqlmesh-project),
  has been created in the
  [`simple-example` directory of this Git repository](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/simple-example),
  with the `sqlmesh init duckdb` command. The resulting file structure
  has been added and committed to the Git repository:
  * [Configuration](https://sqlmesh.readthedocs.io/en/stable/guides/configuration/):
  [`config.yaml` file](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/simple-example/config.yaml)
  * [Models](https://sqlmesh.readthedocs.io/en/stable/concepts/models/overview/):
  [`models/` directory](https://github.com/data-engineering-helpers/ks-cheat-sheets/tree/main/data-processing/sqlmesh/simple-example/models)
  * [Seed files](https://sqlmesh.readthedocs.io/en/stable/concepts/models/seed_models/):
  [`seeds/` directory](https://github.com/data-engineering-helpers/ks-cheat-sheets/tree/main/data-processing/sqlmesh/simple-example/seeds)
  * Which contain a seed/example data set, namely
  [`seed_data.csv`](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/simple-example/seeds/seed_data.csv)
  * [Shared audit files](https://sqlmesh.readthedocs.io/en/stable/concepts/audits/):
  [`audits/` directory](https://github.com/data-engineering-helpers/ks-cheat-sheets/tree/main/data-processing/sqlmesh/simple-example/audits)
  * [Unit test files](https://sqlmesh.readthedocs.io/en/stable/concepts/tests/):
  [`tests/` directory](https://github.com/data-engineering-helpers/ks-cheat-sheets/tree/main/data-processing/sqlmesh/simple-example/tests)
  * [Macro files](https://sqlmesh.readthedocs.io/en/stable/concepts/macros/overview/):
  [`macros/` directory](https://github.com/data-engineering-helpers/ks-cheat-sheets/tree/main/data-processing/sqlmesh/simple-example/macros)

