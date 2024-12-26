Cheat Sheet - SQLMesh
=====================

# Table of Content (ToC)
* [Overview](#overview)
* [References](#references)
  * [Data Engineering helpers](#data-engineering-helpers)
  * [SQLMesh](#sqlmesh)
  * [DuckDB](#duckdb)
  * [Articles and Git knowledge sharing projects](#articles-and-git-knowledge-sharing-projects)
    * [Reddit thread](#reddit-thread)
    * [SQLMesh \- Migrate](#sqlmesh---migrate)
    * [SQLMesh as alternative to dbt](#sqlmesh-as-alternative-to-dbt)
    * [Arcane insight](#arcane-insight)
    * [SQL \+ DataOps = SQLMesh](#sql--dataops--sqlmesh)
    * [Time To Move From dbt to SQLMesh](#time-to-move-from-dbt-to-sqlmesh)
* [Quickstart](#quickstart)
  * [Simple example with DuckDB](#simple-example-with-duckdb)
    * [Some information about the project](#some-information-about-the-project)
    * [Initial models](#initial-models)
      * [Create a prod environment](#create-a-prod-environment)
      * [Check the new state brought by the plan](#check-the-new-state-brought-by-the-plan)
      * [Launch the tests](#launch-the-tests)
    * [Introduce a change in the incremental model](#introduce-a-change-in-the-incremental-model)
      * [Create a dev environment](#create-a-dev-environment)
      * [Check the new state brought by the plan on dev](#check-the-new-state-brought-by-the-plan-on-dev)
      * [Update the prod environment](#update-the-prod-environment)
      * [Check the upddates in the prod environment](#check-the-upddates-in-the-prod-environment)
  * [Full end\-to\-end example](#full-end-to-end-example)
* [Installation](#installation)
  * [Public data sets on DuckDB](#public-data-sets-on-duckdb)
  * [Clone this repository](#clone-this-repository)
  * [SQLMesh](#sqlmesh-1)
    * [SQLMesh UI](#sqlmesh-ui)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/README.md)
explains how to install and to use [SQLMesh](https://sqlmesh.readthedocs.io/en/stable/),
_e.g._, on a laptop or on a virtual machine (VM).

> [SQLMesh](https://sqlmesh.readthedocs.io/en/stable/) is
> a next-generation data transformation framework designed to ship
> data quickly, efficiently, and without error. Data teams can efficiently
> run and deploy data transformations written in SQL or Python with
> visibility and control at any size.
> It is more than just a [dbt alternative](https://tobikodata.com/reduce_costs_with_cron_and_partitions.html).

SQLMesh requires some database to store its state. [DuckDB](https://duckdb.org/) is the database by default,
as it is small and efficient enough to be available virtually everywhere:
> [DuckDB](https://duckdb.org/) is an embedded database, similar to SQLite,
> but designed for OLAP-style analytics. It is crazy fast and allows you
> to read and write data stored in CSV, JSON, and Parquet files directly,
> without requiring you to load them into the database first.

For production-ready deployments, other database backends, like PostgreSQL, may be advised.

# References

## Data Engineering helpers
* [Data Engineering Helpers - Knowledge Sharing - DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/)
* [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/)
* [Data Engineering Helpers - Knowledge Sharing - dbt](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/dbt/)
* [Material for the Data platform - Data life cycle](https://github.com/data-engineering-helpers/data-life-cycle)
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box)

## SQLMesh
* GitHub page: https://github.com/TobikoData/sqlmesh
* Home page: https://sqlmesh.com/
* Company behind it: [Tobiko Data](https://www.linkedin.com/company/tobikodata)
* Some significant contributors:
  * CEO of Tobyko: Tobias Mao, aka Toby
  ([Toby Mao on LinkedIn](https://www.linkedin.com/in/toby-mao/),
  [Toby Mao on GitHub](https://github.com/tobymao),
  [Toby Mao on Tobiko blog site](https://tobikodata.com/author/toby-mao.html),
  [Toby Mao home page](https://tobymao.com/))
  * Co-founder of Tobiko: Iaroslav Zeigerman
  ([Iaroslav Zeigerman on LinkedIn](https://www.linkedin.com/in/izeigerman/),
  [Iaroslav Zeigerman on GitHub](https://github.com/izeigerman),
  [Iaroslav Zeigerman on the Tobiko blog site](https://tobikodata.com/author/iaroslav-zeigerman.html))
  * Founding engineer: Ryan Eakman
  ([Ryan Eakman on LinkedIn](https://www.linkedin.com/in/ryan-eakman-65469988/),
  [Ryan Eakman on GitHub](https://github.com/eakmanrq),
  [Ryan Eakman on Tobiko blog site](https://tobikodata.com/author/ryan-eakman.html))
* Related project:
  * SQLGlot: https://github.com/tobymao/sqlglot (and [SQLGlot home page](https://sqlglot.com))
* Blog: https://tobikodata.com/blog

## DuckDB
* Home page: https://duckdb.org/
  * [DuckDB doc - HTTPFS extension](https://duckdb.org/docs/extensions/httpfs.html)

## Articles and Git knowledge sharing projects

### Reddit thread
* Triggered by Tobias Mao, aka Toby:
  https://www.reddit.com/r/dataengineering/comments/124tspm/sqlmesh_the_future_of_dataops/

### SQLMesh - Migrate
* Overview: series of articles to explore SQLMesh and how it compares
  to dbt
* Author: David Jayatillake
([David Jayatillake on LinkedIn](https://www.linkedin.com/in/david-jayatillake/),
  [David Jayatillake on Substack](https://substack.com/@davidsj))
* Date: Dec. 2024
* Publisher: Substack
* Link to the articles:
  * Migrate (the conclusion): https://davidsj.substack.com/p/sqlmesh-migrate
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

### Arcane insight
* GitHub repository: https://github.com/mattiasthalen/arcane-insight/tree/main
* Title: Arcane insight
* Overview: Arcane Insight is a data analytics project designed to harness
  the power of SQLMesh and DuckDB to collect, transform, and analyze data from
  [Blizzard's Hearthstone API](https://develop.battle.net/documentation/hearthstone).
* Author: Mattias Thalén
 ([Mattias Thalén on LinkedIn](https://www.linkedin.com/in/mattias-thal%C3%A9n/),
  [Mattias Thalén on GitHub](https://github.com/mattiasthalen))
* Date: End of 2024

### SQL + DataOps = SQLMesh
* Title: SQL + DataOps = SQLMesh?
* Date: March 2024
* Author: Marti Sec
  ([Marti Sec on blog page](https://8vi.cat/author/marti/))
* Link to the article:
  https://8vi.cat/sqlmesh-quick-overview/
* Publisher: [63 orders of magnitude blog site](https://8vi.cat/)

### Time To Move From dbt to SQLMesh
* Title: Is It Time To Move From dbt to SQLMesh?
* Date: Feb. 2024
* Author: Benoit Pimpaud
  ([Benoit Pimpaud on LinkedIn](https://www.linkedin.com/in/pimpaudben/))
* Link to the article: https://kestra.io/blogs/2024-02-28-dbt-or-sqlmesh
* Publisher: Kestra blog

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

### Some information about the project
* The `info` command gives a high level overview of the project:
```bash
sqlmesh info
Models: 3
Macros: 0
Data warehouse connection succeeded
```

### Initial models
* The datasets are materialized as tables in a (to be created) prod environment

* The datasets are also called models. In the remainder of the documentation,
  datasets, tables and models may be interchanged

#### Create a prod environment
* Reference:
  https://sqlmesh.readthedocs.io/en/stable/quickstart/cli/#2-create-a-prod-environment

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

#### Check the new state brought by the plan
* The `sqlmesh fetchdf` command is a proxy to the backend database, DuckDB in
  this example. The content of the backend database may therefore be queries
  either through the `sqlmesh fetchdf` command or directly with the backend
  database.
  
* In the remaining of this sub-section, DuckDB is used directly.
  All the SQL queries could also be executed thanks to
  the `sqlmesh fetchdf` command, for instance:
```bash
sqlmesh fetchdf "select * from sqlmesh_example.incremental_model"
   id  item_id event_date
0   1        2 2020-01-01
 ...
6   7        1 2020-01-07
```

* Check the models with DuckDB
  * Launch DuckDB on the just created/updated database (namely `db.db`)
  (as a reminder, to quit the Duck shell, either type Control-D or
  the `.quit` command):
```bash
duckdb db.db
```
  * List all the tables:
```sql
D show all tables;
```
  * List the items of the `seed_model` table:
```sql
D select * from sqlmesh_example.seed_model;
┌───────┬─────────┬────────────┐
│  id   │ item_id │ event_date │
│ int32 │  int32  │    date    │
├───────┼─────────┼────────────┤
│     1 │       2 │ 2020-01-01 │
 ...
│     7 │       1 │ 2020-01-07 │
└───────┴─────────┴────────────┘
```
  * List the items of the `incremental_model` table:
```sql
D select * from sqlmesh_example.incremental_model;
┌───────┬─────────┬────────────┐
│  id   │ item_id │ event_date │
│ int32 │  int32  │    date    │
├───────┼─────────┼────────────┤
│     1 │       2 │ 2020-01-01 │
 ...
│     7 │       1 │ 2020-01-07 │
└───────┴─────────┴────────────┘
```
  * List the items of the `full_model` table:
```sql
D select * from sqlmesh_example.full_model;
┌─────────┬────────────┐
│ item_id │ num_orders │
│  int32  │   int64    │
├─────────┼────────────┤
│       2 │          1 │
│       1 │          5 │
│       3 │          1 │
└─────────┴────────────┘
```
  * Quit DuckDB:
```sql
D .quit
```

#### Launch the tests
* Launch the tests:
```bash
sqlmesh test
.
----------------------------------------------------------------------
Ran 1 test in 0.021s

OK
```

### Introduce a change in the incremental model
* Reference:
  https://sqlmesh.readthedocs.io/en/stable/quickstart/cli/#3-update-a-model

#### Create a dev environment
* Reference:
  https://sqlmesh.readthedocs.io/en/stable/quickstart/cli/#4-work-with-a-development-environment
  
* Launch the plan command, specifying the dev environment (which does not exist
  yet):
```bash
sqlmesh plan dev
======================================================================
Successfully Ran 1 tests against duckdb
----------------------------------------------------------------------
New environment `dev` will be created from `prod`

Differences from the `prod` environment:

Models:
├── Directly Modified:
│   └── sqlmesh_example__dev.incremental_model
└── Indirectly Modified:
    └── sqlmesh_example__dev.full_model
...
Directly Modified: sqlmesh_example__dev.incremental_model (Non-breaking)
└── Indirectly Modified Children:
    └── sqlmesh_example__dev.full_model (Indirect Non-breaking)
Models needing backfill (missing dates):
└── sqlmesh_example__dev.incremental_model: 2020-01-01 - 2024-12-24
Enter the backfill start date (eg. '1 year', '2020-01-01') or blank to backfill from the beginning of history:
Enter the backfill end date (eg. '1 month ago', '2020-01-01') or blank to backfill up until '2024-12-25 00:00:00':
Apply - Backfill Tables [y/n]:
```
  * Answer yes when prompted about applying the change:
```bash
Apply - Backfill Tables [y/n]: y
Creating physical tables ━━━━━ ... ━━━━━ 100.0% • 3/3 • 0:00:00

All model versions have been created successfully

[1/1] sqlmesh_example__dev.incremental_model evaluated in 0.04s
Evaluating models ━━━━━ ... ━━━━━━ 100.0% • 1/1 • 0:00:00


All model batches have been executed successfully

Virtually Updating 'dev' ━━━━━ ... ━━━━━ 100.0% • 0:00:00

The target environment has been updated successfully
```

#### Check the new state brought by the plan on dev
* Check the content of the updated table in the dev environment:
```bash
sqlmesh fetchdf "select * from sqlmesh_example__dev.incremental_model"
   id  item_id new_column event_date
0   1        2          z 2020-01-01
 ...
6   7        1          z 2020-01-07
```

* Even though there is a new `full_model` table in the dev environment,
  its content is the same as the same table on the prod environment
  (as this table does not use the new column yet):
```bash
sqlmesh fetchdf "select * from sqlmesh_example__dev.full_model"
   item_id  num_orders
0        2           1
1        1           5
2        3           1
```

* There is a command, namely `table_diff`, to display the differences
  between two environment for a given table:
```bash
sqlmesh table_diff prod:dev sqlmesh_example.incremental_model

Schema Diff Between 'PROD' and 'DEV' environments for model 'sqlmesh_example.incremental_model':
└── Added Columns:
    └── new_column (TEXT)

Row Counts:
└──  FULL MATCH: 7 rows (100.0%)

COMMON ROWS column comparison stats:
         pct_match
item_id      100.0
```

#### Update the prod environment
* Reference:
  https://sqlmesh.readthedocs.io/en/stable/quickstart/cli/#51-apply-updates-to-prod
  
* Launch the plan command, and when not specifying any environment, the prod
  environment is assumed:

```bash
sqlmesh plan # prod
======================================================================
Successfully Ran 1 tests against duckdb
----------------------------------------------------------------------
Differences from the `prod` environment:

Models:
├── Directly Modified:
│   └── sqlmesh_example.incremental_model
└── Indirectly Modified:
    └── sqlmesh_example.full_model
...
Directly Modified: sqlmesh_example.incremental_model (Non-breaking)
└── Indirectly Modified Children:
    └── sqlmesh_example.full_model (Indirect Non-breaking)
Apply - Virtual Update [y/n]:
```

  * Answer yes when prompted about applying the change:
```bash
Apply - Backfill Tables [y/n]: y
Creating physical tables ━━━━ ... ━━━━━ 100.0% • 3/3 • 0:00:00

All model versions have been created successfully

Virtually Updating 'prod' ━━━━ ... ━━━━━ 100.0% • 0:00:00

The target environment has been updated successfully


Virtual Update executed successfully
```

#### Check the upddates in the prod environment
* Reference:
  https://sqlmesh.readthedocs.io/en/stable/quickstart/cli/#5.2-validate-updates-in-prod

* Check that the prod table has been updated with the new column:
```bash
sqlmesh fetchdf "select * from sqlmesh_example.incremental_model"
   id  item_id new_column event_date
0   1        2          z 2020-01-01
 ...
6   7        1          z 2020-01-07
```

* The `table_diff` command now reports that the tables are the same in both the
  dev and prod environments:
```bash
sqlmesh table_diff prod:dev sqlmesh_example.incremental_model

Schema Diff Between 'PROD' and 'DEV' environments for model 'sqlmesh_example.incremental_model':
└── Schemas match


Row Counts:
└──  FULL MATCH: 7 rows (100.0%)

COMMON ROWS column comparison stats:
            pct_match
item_id         100.0
new_column      100.0
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

## Public data sets on DuckDB
* This sub-section is just for reference. It is not used for most of
  the examples explored in the
  [Quickstart section](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/README.md#quickstart)

* See also
  [GitHub - Data Engineering Helpers - KS - DuckDB - Public catalogs](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/README.md#public-catalogs)

* Launch the DuckDB shell:
```bash
$ duckdb
```

* (In DuckDB,) attach to a public catalog, for instance the BlueSky catalog:
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
python -mpip install -U "sqlmesh[web]"
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

### SQLMesh UI
* In a separate terminal tab, as the default local port (`8000`) may already
  be taken by other processes (_e.g._,
  [LakeFS](https://github.com/treeverse/lakeFS) is running on the `8000` port
  by default), launch the SQLMesh UI by specifying a port not already in use:
```bash
sqlmesh ui --port 9090
INFO:     Started server process [7586]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:9090 (Press CTRL+C to quit)
```

* With a web browser, open http://localhost:9090

