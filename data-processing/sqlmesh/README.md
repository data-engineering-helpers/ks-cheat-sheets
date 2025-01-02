Cheat Sheet - SQLMesh
=====================

# Table of Content (ToC)
* [Overview](#overview)
* [References](#references)
  * [Data Engineering helpers](#data-engineering-helpers)
  * [SQLMesh](#sqlmesh)
    * [Documentation reference for SQLMesh](#documentation-reference-for-sqlmesh)
      * [Concepts](#concepts)
      * [Development](#development)
      * [Models](#models)
      * [Macros](#macros)
      * [Metrics](#metrics)
      * [Architecture](#architecture)
      * [Integrations](#integrations)
        * [Integration with tools](#integration-with-tools)
        * [Integration with execution engines](#integration-with-execution-engines)
    * [Git repository with SQLMesh examples](#git-repository-with-sqlmesh-examples)
      * [Sushi project](#sushi-project)
      * [Ibis project](#ibis-project)
  * [DuckDB](#duckdb)
  * [Unity Catalog (UC)](#unity-catalog-uc)
  * [Articles and Git knowledge sharing projects](#articles-and-git-knowledge-sharing-projects)
    * [Reddit thread](#reddit-thread)
    * [SQLMesh \- Migrate](#sqlmesh---migrate)
    * [SQLMesh as alternative to dbt](#sqlmesh-as-alternative-to-dbt)
    * [Arcane insight](#arcane-insight)
    * [Multi\-engine Stacks](#multi-engine-stacks)
    * [The rise of the analytics pretendgineer](#the-rise-of-the-analytics-pretendgineer)
    * [Unlocking data insights with Ibis and SQLMesh](#unlocking-data-insights-with-ibis-and-sqlmesh)
    * [SQL \+ DataOps = SQLMesh](#sql--dataops--sqlmesh)
    * [Time To Move From dbt to SQLMesh](#time-to-move-from-dbt-to-sqlmesh)
* [Introduction to the examples in this Git repository](#introduction-to-the-examples-in-this-git-repository)
* [Quickstart](#quickstart)
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
  * [Cleanup](#cleanup)
* [More advanced examples](#more-advanced-examples)
  * [Local PostgreSQL to store the state](#local-postgresql-to-store-the-state)
  * [Simple Python example](#simple-python-example)
    * [SQLMesh plan with Python models](#sqlmesh-plan-with-python-models)
    * [Check the content of the tables with Python models](#check-the-content-of-the-tables-with-python-models)
    * [Audit with Python models](#audit-with-python-models)
    * [Test with Python models](#test-with-python-models)
    * [Cleanup](#cleanup-1)
  * [Full example with Python models](#full-example-with-python-models)
    * [SQLMesh plan with Python models](#sqlmesh-plan-with-python-models-1)
    * [Check the created tables](#check-the-created-tables)
    * [Execution, tests and audits](#execution-tests-and-audits)
  * [Simple PySpark example](#simple-pyspark-example)
    * [SQLMesh plan](#sqlmesh-plan)
  * [Full end\-to\-end example](#full-end-to-end-example)
  * [Simple DataBricks example](#simple-databricks-example)
    * [Instantiate files depending on env vars](#instantiate-files-depending-on-env-vars)
    * [SQLMesh plan](#sqlmesh-plan-1)
  * [Simple Unity Catalog (UC) example](#simple-unity-catalog-uc-example)
    * [Spark Connect server](#spark-connect-server)
    * [SQLMesh plan](#sqlmesh-plan-2)
* [Installation](#installation)
  * [Clone this repository](#clone-this-repository)
  * [DuckDB](#duckdb-1)
    * [Public data sets on DuckDB](#public-data-sets-on-duckdb)
  * [Unity Catalog (UC)](#unity-catalog-uc-1)
  * [Spark Connect](#spark-connect)
  * [SQLMesh](#sqlmesh-1)
    * [SQLMesh UI](#sqlmesh-ui)
  * [Local PostgreSQL server](#local-postgresql-server)
    * [Setup of the configuration for the local PostgreSQL to store the state](#setup-of-the-configuration-for-the-local-postgresql-to-store-the-state)
    * [SQLMesh with PostgreSQL to store the state](#sqlmesh-with-postgresql-to-store-the-state)
    * [Cleanup when a local PostgreSQL database stores the state](#cleanup-when-a-local-postgresql-database-stores-the-state)
    * [Cleanup the changes when a local PostgreSQL database stores the state](#cleanup-the-changes-when-a-local-postgresql-database-stores-the-state)
  * [Local Airflow service](#local-airflow-service)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/README.md)
explains how to install and to use
[SQLMesh](https://sqlmesh.readthedocs.io/en/stable/), _e.g._,
on a laptop or on a virtual machine (VM).

> [SQLMesh](https://sqlmesh.readthedocs.io/en/stable/) is
> a next-generation data transformation framework designed to ship
> data quickly, efficiently, and without error. Data teams can efficiently
> run and deploy data transformations written in SQL or Python with
> visibility and control at any size. It is more than just a
> [dbt alternative](https://tobikodata.com/reduce_costs_with_cron_and_partitions.html).

SQLMesh requires some database to store its state.
[DuckDB](https://duckdb.org/) is the database by default,
as it is small and efficient enough to be available virtually everywhere:
> [DuckDB](https://duckdb.org/) is an embedded database, similar to SQLite,
> but designed for OLAP-style analytics. It is crazy fast and allows you
> to read and write data stored in CSV, JSON, and Parquet files directly,
> without requiring you to load them into the database first.

For production-ready deployments, other database backends, like PostgreSQL,
may be advised.

# References

## Data Engineering helpers
* [Data Engineering Helpers - Knowledge Sharing - DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/)
* [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/)
* [Data Engineering Helpers - Knowledge Sharing - Unity Catalog (UC)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/unity-catalog/)
* [Data Engineering Helpers - Knowledge Sharing - Spark](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/)
* [Data Engineering Helpers - Knowledge Sharing - dbt](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/dbt/)
* [Data Engineering Helpers - Knowledge Sharing - Airflow](https://github.com/data-engineering-helpers/ks-cheat-sheets/tree/main/orchestrators/airflow)
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
  * SQLGlot: https://github.com/tobymao/sqlglot (and
  [SQLGlot home page](https://sqlglot.com))
* Blog: https://tobikodata.com/blog

### Documentation reference for SQLMesh
* Quickstart guide: https://sqlmesh.readthedocs.io/en/stable/quick_start/
* Walkthrough example:
  https://sqlmesh.readthedocs.io/en/stable/examples/incremental_time_full_walkthrough/

#### Concepts
* Overview:
  https://sqlmesh.readthedocs.io/en/stable/concepts/overview/
* Glossary: https://sqlmesh.readthedocs.io/en/stable/concepts/glossary/

#### Development
* Plans:
  https://sqlmesh.readthedocs.io/en/stable/concepts/plans/
* Environments:
  https://sqlmesh.readthedocs.io/en/stable/concepts/environments/
* Testing:
  https://sqlmesh.readthedocs.io/en/stable/concepts/tests/
* Auditing:
  https://sqlmesh.readthedocs.io/en/stable/concepts/audits/

#### Models
* Overview:
  https://sqlmesh.readthedocs.io/en/stable/concepts/models/overview/
* Model kinds:
  https://sqlmesh.readthedocs.io/en/stable/concepts/models/model_kinds/
* SQL models:
  https://sqlmesh.readthedocs.io/en/stable/concepts/models/sql_models/
* Python models:
  https://sqlmesh.readthedocs.io/en/stable/concepts/models/python_models/
* Seed models:
  https://sqlmesh.readthedocs.io/en/stable/concepts/models/seed_models/
* External models:
  https://sqlmesh.readthedocs.io/en/stable/concepts/models/external_models/
* Managed models:
  https://sqlmesh.readthedocs.io/en/stable/concepts/models/managed_models/

#### Macros
* Overview:
  https://sqlmesh.readthedocs.io/en/stable/concepts/macros/overview/
* Macro variables:
  https://sqlmesh.readthedocs.io/en/stable/concepts/macros/macro_variables/
* SQLMesh variables:
  https://sqlmesh.readthedocs.io/en/stable/concepts/macros/sqlmesh_macros/
* Jinja macros:
  https://sqlmesh.readthedocs.io/en/stable/concepts/macros/jinja_macros/

#### Metrics
* Overview: https://sqlmesh.readthedocs.io/en/stable/concepts/metrics/overview/
* Definition:
  https://sqlmesh.readthedocs.io/en/stable/concepts/metrics/definition/

#### Architecture
* Snapshots:
  https://sqlmesh.readthedocs.io/en/stable/concepts/architecture/snapshots/
* Serialization:
  https://sqlmesh.readthedocs.io/en/stable/concepts/architecture/serialization/

#### Integrations
* Overview:
  https://sqlmesh.readthedocs.io/en/stable/integrations/overview/
  
##### Integration with tools
* Integration with Airflow:
  https://sqlmesh.readthedocs.io/en/stable/integrations/airflow/
* Integration with GitHub Actions CI/CD bot:
  https://sqlmesh.readthedocs.io/en/stable/integrations/github/
* Integration with dbt:
  https://sqlmesh.readthedocs.io/en/stable/integrations/dbt/
* Integration with dlt:
  https://sqlmesh.readthedocs.io/en/stable/integrations/dlt/

##### Integration with execution engines
* Integration with Spark:
  https://sqlmesh.readthedocs.io/en/stable/integrations/engines/spark/
  * PySpark models:
  https://sqlmesh.readthedocs.io/en/stable/concepts/models/python_models/#pyspark
* Integration with DataBricks:
  https://sqlmesh.readthedocs.io/en/stable/integrations/engines/databricks/
* Integration with Athena:
  https://sqlmesh.readthedocs.io/en/stable/integrations/engines/athena/
* Integration with DuckDB:
  https://sqlmesh.readthedocs.io/en/stable/integrations/engines/duckdb/
* Integration with PostgreSQL:
  https://sqlmesh.readthedocs.io/en/stable/integrations/engines/postgres/

### Git repository with SQLMesh examples
* Git repository: https://github.com/TobikoData/sqlmesh-examples

#### Sushi project
* Jupyter notebook about the Sushi project:
  https://github.com/TobikoData/sqlmesh-examples/blob/main/001_sushi/sushi-overview.ipynb
  * Simple part:
  https://github.com/TobikoData/sqlmesh-examples/tree/main/001_sushi/1_simple
  * Moderate part:
  https://github.com/TobikoData/sqlmesh-examples/tree/main/001_sushi/2_moderate

#### Ibis project
* Ibis SQLMesh project directory:
  https://github.com/TobikoData/sqlmesh-examples/tree/main/002_ibis
* The Ibis SQLMesh project features:
  * Python models:
  https://github.com/TobikoData/sqlmesh-examples/tree/main/002_ibis/models
  * The Ibis framework:
  https://github.com/ibis-project/ibis

## DuckDB
* Home page: https://duckdb.org/
  * [DuckDB doc - HTTPFS extension](https://duckdb.org/docs/extensions/httpfs.html)

## Unity Catalog (UC)
* Home page: https://www.unitycatalog.io
* GitHub page: https://github.com/unitycatalog/unitycatalog
* [Unity Catalog docs](https://docs.unitycatalog.io/)
  * [Unity Catalog docs - Quickstart](https://docs.unitycatalog.io/quickstart/)
  * [Unity Catalog docs - Usage - CLI](https://docs.unitycatalog.io/usage/cli/)
  * [Unity Catalog docs - Deployment - PostgreSQL connection](https://docs.unitycatalog.io/deployment/#example-postgresql-connection)
  * [Unity Catalog docs - Integrations - Spark](https://docs.unitycatalog.io/integrations/unity-catalog-spark/)
  * [Unity Catalog docs - Integrations - DataBricks](https://sqlmesh.readthedocs.io/en/stable/integrations/engines/databricks/)
  * [Unity Catalog docs - Integrations - DuckDB](https://docs.unitycatalog.io/integrations/unity-catalog-duckdb/)
  * [Unity Catalog docs - Integrations - XTable](https://docs.unitycatalog.io/integrations/unity-catalog-xtable/)
* [Unity Catalog blog post - Integrating Spark with Unity Catalog via Open APIs](https://www.unitycatalog.io/blogs/integrating-apache-spark-with-unity-catalog-assets-via-open-apis)


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

### Multi-engine Stacks
* Title: Multi-engine Stacks Deserve to be First Class
* Author: Julien Hurault
  ([Julien Hurault on LinkedIn](https://www.linkedin.com/in/julienhuraultanalytics/),
  [Julien Hurault on Substack](https://substack.com/@juhache))
* Date: July 2024
* Link to the article:
  https://juhache.substack.com/p/multi-engine-stacks-deserve-to-be
* Publisher: Substack

### The rise of the analytics pretendgineer
* Title: The rise of the analytics pretendgineer
* Date: May 2024
* Author: Benn Stancil
  ([Benn Stancil on LinkedIn](https://www.linkedin.com/in/benn-stancil/),
  [Benn Stancil on Substack](https://benn.substack.com/))
* Link to the article:
  https://benn.substack.com/p/the-rise-of-the-analytics-pretendgineer

### Unlocking data insights with Ibis and SQLMesh
* Title: Unlocking data insights with Ibis and SQLMesh
* Date: May 2024
* Authors:
  * Marisa Smith
  ([Marisa Smith on LinkedIn](https://www.linkedin.com/in/marisa-smith-datanerd/),
  [Marisa Smith on Tobiko blog](https://tobikodata.com/author/marisa-smith.html))
  * Andrew Shannon
  ([Andrew Shannon on LinkedIn](https://www.linkedin.com/in/ashannon01/),
  [Andrew Shannon on Tobiko blog](https://tobikodata.com/author/andrew-shannon.html))
* Link to the article:
  https://tobikodata.com/ibis-sqlmesh-unlocking-data-insights.html

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

# Introduction to the examples in this Git repository
* [Examples in this Git repository](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/examples/):
  * [`examples/001-simple` directory](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/examples/001-simple/) --
  Simple example, also named "quickstart".
    * DuckDB is used both for the executing engine and to store the state
  * [`examples/002-postgresql-state` directory](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/examples/002-postgresql-state/) --
  The same simple example as above (`examples/001-simple`), except that:
    * DuckDB is used for the executing engine and a local PostgreSQL database
	to store the state
  * [`examples/003-python-simple`](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/examples/003-python-simple/) --
  Example including a simple Python model
    * DuckDB is used both for the executing engine and to store the state
	* The Python model is also executed by DuckDB
  * [`examples/004-python-ibis` directory](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/examples/004-python-ibis/) --
  Example featuring the Python Ibis framework (translating Python dataframes
  from one executing engine to another, that is, like SQLGlot but for Python)
    * DuckDB is used both for the executing engine and to store the state
	* The Python models are also executed by DuckDB
  * [`examples/005-pyspark-simple` directory](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/examples/005-pyspark-simple/) --
  Simple example featuring a Python model and Spark as the executing engine
    * DuckDB is used to store the state
	* Note that Spark cannot store the state (as per the
	[official SQLMesh documentation about Spark](https://sqlmesh.readthedocs.io/en/stable/integrations/engines/spark/))
  * [`examples/006-e2e` directory](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/examples/006-e2e/) --
  End-to-end full example
    * Still needs to be documented
  * [`examples/007-unitycatalog-simple` directory](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/examples/007-unitycatalog-simple/) --
  Simple example featuring integration with UnityCatalog,
  thanks to Spark as the executing engine
    * DuckDB is used to store the state
	* Note that Spark cannot store the state (as per the
	[official SQLMesh documentation about Spark](https://sqlmesh.readthedocs.io/en/stable/integrations/engines/spark/))

* In most of the
  [example directories]((https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/examples/)),
  there is a `Makefile` with the most used commands as targets, for instance:
  * Clean the project from potential previous experiments: `make clean`
  * Create the prod environment: `make plan-prod`
  * List the tables in prod: `make list-tables-prod`
  * Browse the content of the main table in prod: `make check-data-prod`
  * Suggest what to do next in order to introduce a change: `make hint-change`
  * Create a dev environment: `make plan-dev`
  * List the tables in dev: `make list-tables-dev`
  * Browse the content of the main table in dev: `make check-data-dev`
  * List the differences for the main table between dev and prod: `make diff`

* A typical sequence is:
```bash
make clean
make plan-prod
make list-tables-prod
make check-data-prod
make hint-change
# Make a change on the model suggested above => vi models/some_model.{sql,py}
make plan-dev
make list-tables-dev
make check-data-dev
make diff
```

# Quickstart
* This sesction is a reproduction, step by step and with the full source code,
  of the
  [quickstart guide on the SQLMesh documentation](https://sqlmesh.readthedocs.io/en/stable/quickstart/cli/)

* It features a simple example with DuckDB, both as the execution engine
  and to store the SQLMesh state, in a local data file (namely `db.db`)
  ignored by Git (so that the example may be reproduced without interfering
  with this Git repository)

* Change to the
  [`examples/001-simple` directory](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/examples/001-simple/)
  within the SQLMesh dedicated directory:
```bash
cd ~/dev/knowledge-sharing/ks-cheat-sheets/data-processing/sqlmesh/examples/001-simple
```

* Clean/remove results of potential earlier tries (those files are ignored
  by Git):
```bash
make clean # equivalent of:
rm -rf .cache logs db.db
```

## Some information about the project
* The `info` command gives a high level overview of the project:
```bash
sqlmesh info
Models: 3
Macros: 0
Data warehouse connection succeeded
```

## Initial models
* The datasets are materialized as tables in a (to be created) prod environment

* The datasets are also called models. In the remainder of the documentation,
  datasets, tables and models may be interchanged

### Create a prod environment
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

### Check the new state brought by the plan
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

### Launch the tests
* Launch the tests:
```bash
sqlmesh test
.
----------------------------------------------------------------------
Ran 1 test in 0.021s

OK
```

## Introduce a change in the incremental model
* Reference:
  https://sqlmesh.readthedocs.io/en/stable/quickstart/cli/#3-update-a-model

### Create a dev environment
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

### Check the new state brought by the plan on dev
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

### Update the prod environment
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

### Check the upddates in the prod environment
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

## Cleanup
* For convenience, all the clean commands are featured in a single Makefile
  target:
```bash
make clean
```
  * For reference, the following cleaning operations are performed
  * As DuckDB stores both the state and the datasets, cleaning up is as
  straightforward as deleting the DuckDB data file, namely `db.db`:
```bash
rm -f db.db
```
  * Delete also the log and the cache directories:
```bash
make clean # equivalent of:
rm -rf .cache logs
```

* Comment the clause for the `z` column in the `incremental_model` model:
```bash
make hint-change
grep "z" models/incremental_model.sql
    --'z' AS new_column, -- Added column
```

* The project is now ready to start afresh, with no memory nor any change
  when compared to the Git repository

# More advanced examples

## Local PostgreSQL to store the state
* DuckDB is still the execution engine

* The state is stored within a local PostgreSQL database. See the
  [Local PostgreSQL server section](#local-postgresql-server) on how to install
  and setup such a local PostgreSQL database

* Change to the
  [`examples/002-postgresql-state` directory](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/examples/002-postgresql-state/)
  within the SQLMesh dedicated directory:
```bash
cd ~/dev/knowledge-sharing/ks-cheat-sheets/data-processing/sqlmesh/examples/002-postgresql-state
```

* Clean/remove results of potential earlier tries (those files are ignored
  by Git):
```bash
make clean # equivalent of:
rm -rf .cache logs db.db db.db.wal
```

* The other steps (_i.e._, SQLMesh plan, introduce a change, SQLMesh dev
  environment, check the updates, SQLMesh plan to merge the updates on prod,
  cleanup the project) are the same as in the quickstart example. The Makefile
  has been adapted to take PostgreSQL into account

## Simple Python example
* References:
  * Python models:
  https://sqlmesh.readthedocs.io/en/stable/concepts/models/python_models/

* Change to the
  [`examples/003-python-simple`](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/examples/003-python-simple/)
  directory within the SQLMesh dedicated directory:
```bash
cd ~/dev/knowledge-sharing/ks-cheat-sheets/data-processing/sqlmesh/examples/003-python-simple
```

* To create a project skeleton with Python models, simply use the
  `sqlmesh init` command, that is, using the default dialect (being DuckDB),
  like for SQL models. So, there are no difference, at that stage, between
  a project for SQL models and a project for Python models

* Note that the `sqlmesh init` command has already been performed and the
  resulting project skeleton is part of this Git repository

* Note that the `sqlmesh init` command accepts `python` as a dialect.
  * But if a project skeleton is created that way (_i.e._, with the
  `sqlmesh init python` command), the resulting project skeleton looks similar
  to a regular SQL-model project, with the important difference that the dialect
  in the `config.yaml` configuration file will be `python` rather than `duckdb`.
  * And then, when launching the SQLMesh plan (with the `sqlmesh plan` command),
  the underlying SQLGlot engine will fail with some cryptic error:
```bash
make plan-prod # equivalent of:
sqlmesh plan
Error: Required keyword: 'this' missing for <class 'sqlglot.expressions.Between'>. Line 1, Col: 239.
  odel WHERE BETWEEN(scope[None][event_date], DATESTRTODATE('1970-01-01'), DATESTRTODATE('1970-01-01'))
```

### SQLMesh plan with Python models
* Launch the SQLMesh plan:
```bash
sqlmesh plan
======================================================================
Successfully Ran 1 tests against duckdb
----------------------------------------------------------------------
`prod` environment will be initialized

Requirements:
+ pandas==2.2.3
Models:
└── Added:
    ├── sqlmesh_example.full_model
    ├── sqlmesh_example.incremental_model
    ├── sqlmesh_example.seed_model
    └── sqlmesh_example.full_model_python
Models needing backfill (missing dates):
├── sqlmesh_example.full_model: 2024-12-26 - 2024-12-26
├── sqlmesh_example.incremental_model: 2020-01-01 - 2024-12-26
├── sqlmesh_example.seed_model: 2024-12-26 - 2024-12-26
└── sqlmesh_example.full_model_python: 2024-12-26 - 2024-12-26
```

* Accept the suggestions at the prompt:
```text
Apply - Backfill Tables [y/n]: y
Creating physical tables ━━━━ ... ━━━━ 100.0% • 4/4 • 0:00:00

All model versions have been created successfully

[1/1] sqlmesh_example.seed_model evaluated in 0.03s
[1/1] sqlmesh_example.full_model_python evaluated in 0.01s
[1/1] sqlmesh_example.incremental_model evaluated in 0.01s
[1/1] sqlmesh_example.full_model evaluated in 0.01s
Evaluating models ━━━━ ... ━━━━ 100.0% • 4/4 • 0:00:00


All model batches have been executed successfully

Virtually Updating 'prod' ━━━━━ ... ━━━━━ 100.0% • 0:00:00

The target environment has been updated successfully
```

### Check the content of the tables with Python models
* Use the `fetchdf` command:
  * To list the tables:
```bash
make list-tables-prod # equivalent of
sqlmesh fetchdf "use sqlmesh_example; show tables"
                name
0         full_model
1  full_model_python
2  incremental_model
3         seed_model
```
  * To browse the content of the
  [Python model](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/examples/003-python-simple/full_model_python.py)
  table (that is, the `sqlmesh_example.full_model_python` table):
```bash
make check-data-prod # equivalent of:
sqlmesh fetchdf "use sqlmesh_example; select * from full_model_python"
   id   name
0   1  Laura
1   2   John
2   3  Lucie
```

### Audit with Python models
* Launch the `audit` command:
```bash
sqlmesh audit # equivalent of
Found 2 audit(s).
assert_positive_order_ids on model sqlmesh_example.full_model ✅ PASS.
not_null on model sqlmesh_example.full_model_python ✅ PASS.

Finished with 0 audit errors and 0 audits skipped.
Done.
```

### Test with Python models
* Launch the `test` command:
```bash
sqlmesh test # equivalent of
sqlmesh test
.
----------------------------------------------------------------------
Ran 1 test in 0.016s

OK
```

### Cleanup
* Clean/remove results of potential earlier tries (those files are ignored
  by Git):
```bash
make clean # equivalent of:
rm -rf .cache logs db.db
```

* Comment the clause for the `z` column in the `incremental_model` model:
```bash
make hint-change # equivalent of:
grep "z" models/incremental_model.sql
    --'z' AS new_column, -- Added column
```

## Full example with Python models
* References:
  * Article on Tobiko blog site:
  https://tobikodata.com/ibis-sqlmesh-unlocking-data-insights.html
  * Python models:
  https://sqlmesh.readthedocs.io/en/stable/concepts/models/python_models/
  * PySpark models:
  https://sqlmesh.readthedocs.io/en/stable/concepts/models/python_models/#pyspark
  * Ibis SQLMesh project:
  https://github.com/TobikoData/sqlmesh-examples/tree/main/002_ibis
  * The Ibis framework:
  https://github.com/ibis-project/ibis 

* Change to the
  [`examples/004-python-ibis` directory](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/examples/004-python-ibis/)
  within the SQLMesh dedicated directory:
```bash
cd ~/dev/knowledge-sharing/ks-cheat-sheets/data-processing/sqlmesh/examples/004-python-ibis
```

* This example has not been generated with the `sqlmesh init` command, but
  it has rather been fully imported from the
  [SQLMesh example Git repository](https://github.com/TobikoData/sqlmesh-examples/tree/main/002_ibis)
  (with `git clone git@github.com:TobikoData/sqlmesh-examples.git` into a
  temporary directory, and then `rsync -av` from that temporary directory unto
  [this current `python-ibis` directory](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/examples/004-python-ibis/))

* It features the [Ibis framework](https://github.com/ibis-project/ibis),
  a Python library to translate dataframes from one dialect to another
  (it is similar to SQLGlot, but for Python instead of for SQL)

### SQLMesh plan with Python models
* Launch the SQLMesh plan:
```bash
make plan-prod # equivalent of
sqlmesh plan
New environment `prod` will be created from `prod`
Summary of differences against `prod`:
Models:
└── Added:
    ├── ibis.full_model
    ├── ibis.ibis_full_model_python
    ├── ibis.ibis_full_model_sql
    ├── ibis.incremental_model
    └── ibis.seed_model
Models needing backfill (missing dates):
├── ibis.full_model: 2020-01-01 - 2024-12-26
├── ibis.ibis_full_model_python: 2020-01-01 - 2024-12-26
├── ibis.ibis_full_model_sql: 2020-01-01 - 2024-12-26
├── ibis.incremental_model: 2020-01-01 - 2024-12-26
└── ibis.seed_model: 2024-12-26 - 2024-12-26
```

* Answer yes to the prompt asking whether to apply and backfill the models:
```bash
Apply - Backfill Tables [y/n]: y
Creating physical table ━━━━ ... ━━━━ 100.0% • 5/5 • 0:00:00

All model versions have been created successfully

[1/1] ibis.seed_model evaluated in 0.00s
[1/1] ibis.incremental_model evaluated in 0.01s
[1/1] ibis.full_model evaluated in 0.01s
[1/1] ibis.ibis_full_model_python evaluated in 0.06s
[1/1] ibis.ibis_full_model_sql evaluated in 0.03s
Evaluating models ━━━ ... ━━━━ 100.0% • 5/5 • 0:00:00


All model batches have been executed successfully

Virtually Updating 'prod' ━━━ ... ━━━━ 100.0% • 0:00:00

The target environment has been updated successfully
```

### Check the created tables
* Note that the result of the `sqlmesh fetchdf "show all tables"` command
  may be truncated (_i.e._, the names of the tables do not appear).
  It is therefore advised to use a specific schema (_e.g._, `ibis` here):
```bash
make list-tables-prod # equivalent of
sqlmesh fetchdf "use ibis; show tables"
```
```text
                     name
0              full_model
1  ibis_full_model_python
2     ibis_full_model_sql
3       incremental_model
4              seed_model
```

* Browse the content of the incremental model/table:
```bash
make check-data-prod # equivalent of
sqlmesh fetchdf "select * from ibis.incremental_model"
```
```text
   id  item_id event_date
0   1        2 2020-01-01
1   2        1 2020-01-01
2   3        3 2020-01-03
3   4        1 2020-01-04
4   5        1 2020-01-05
5   6        1 2020-01-06
6   7        1 2020-01-07
```

* Anyway, DuckDB may also be used to explore the tables and the content.
  In the remainder of this sub-section, DuckDB will be used to explore the data

* Launch the DuckDB shell
  * Note that, as specified within the `config.yaml` configuration file,
  the DuckDB data file is `data/local.duckdb`
  * As may be seen in the
  [various models](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/examples/004-python-ibis/models),
  the schema is `ibis`
  * In order to quit the DuckDB shell, type Control-D or the `.quit` command
```bash
duckdb data/local.duckdb
```
```sql
D use ibis;
D show tables;
┌────────────────────────┐
│          name          │
│        varchar         │
├────────────────────────┤
│ full_model             │
│ ibis_full_model_python │
│ ibis_full_model_sql    │
│ incremental_model      │
│ seed_model             │
└────────────────────────┘
```

* Leave the DuckDB shell:
```sql
D .quit
```

### Execution, tests and audits
* Run the project (as there have been no change yet, running the project
  does not do anything):
```bash
sqlmesh run
Run finished for environment 'prod'
```
* Launch the tests:
```bash
sqlmesh test

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
```
* Launch the audit:
```bash
sqlmesh audit
Found 3 audit(s).
assert_positive_order_ids on model ibis.full_model ✅ PASS.
assert_positive_order_ids on model ibis.ibis_full_model_python ✅ PASS.
assert_positive_order_ids on model ibis.ibis_full_model_sql ✅ PASS.

Finished with 0 audit errors and 0 audits skipped.
Done.
```

## Simple PySpark example
* References:
  * Spark engine:
  https://sqlmesh.readthedocs.io/en/stable/integrations/engines/spark/
  * Python models:
  https://sqlmesh.readthedocs.io/en/stable/concepts/models/python_models/
    * PySpark models:
    https://sqlmesh.readthedocs.io/en/stable/concepts/models/python_models/#pyspark

* Change to the
  [`examples/005-pyspark-simple` directory](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/examples/005-pyspark-simple/)
  within the SQLMesh dedicated directory:
```bash
cd ~/dev/knowledge-sharing/ks-cheat-sheets/data-processing/sqlmesh/examples/005-pyspark-simple
```

* The project has been initialized with the `sqlmesh init spark` command

### SQLMesh plan
* Launch the SQLMesh plan:
```bash
make plan-prod # equivalent of:
sqlmesh plan
======================================================================
Successfully Ran 1 tests against duckdb
----------------------------------------------------------------------
`prod` environment will be initialized

Requirements:
+ pyspark==3.5.4
Models:
└── Added:
    ├── docs_example.pyspark
    ├── sqlmesh_example.full_model
    ├── sqlmesh_example.incremental_model
    └── sqlmesh_example.seed_model
Models needing backfill (missing dates):
└── docs_example.pyspark: 2024-12-26 - 2024-12-26
```

* Answer yes to the prompt:
```text
Apply - Backfill Tables [y/n]: y
Creating physical tables ━━━━ ... ━━━━━ 100.0% • 4/4 • 0:00:00

All model versions have been created successfully
```

## Full end-to-end example
* Example still to be created and documented

* Reference:
  https://sqlmesh.readthedocs.io/en/stable/examples/incremental_time_full_walkthrough/

* Change to the
  [`examples/006-e2e` directory](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/examples/006-e2e/)
  within the SQLMesh dedicated directory:
```bash
cd ~/dev/knowledge-sharing/ks-cheat-sheets/data-processing/sqlmesh/examples/006-e2e
```

## Simple DataBricks example
* References:
  * DataBricks engine:
  https://sqlmesh.readthedocs.io/en/stable/integrations/engines/databricks/
  * Spark engine:
  https://sqlmesh.readthedocs.io/en/stable/integrations/engines/spark/
  * Python models:
  https://sqlmesh.readthedocs.io/en/stable/concepts/models/python_models/
  * PySpark models:
  https://sqlmesh.readthedocs.io/en/stable/concepts/models/python_models/#pyspark

* Change to the
  [`examples/007-databricks-simple` directory](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/examples/007-databricks-simple/)
  within the SQLMesh dedicated directory:
```bash
cd ~/dev/knowledge-sharing/ks-cheat-sheets/data-processing/sqlmesh/examples/007-databricks-simple
```

* The project has been initialized with the `sqlmesh init spark` command

### Instantiate files depending on env vars
* First, specify the following environment variables (for instance, in the
  `~/.bashrc` or `~/.zshrc` Shell configuration file):
  * `DBS_SVR_HST` - DataBricks host, _e.g._,
  `<some-workspace>.cloud.databricks.com`
  * `DBS_HTTP_PATH` - DataBricks HTTP path, _e.g._,
  `sql/protocolv1/o/<wksp-id>/<cluster-id>`
  * `DBS_PAT` - DataBricks Personal Access Token (PAT)
  * `DBS_SCH` - DataBricks schema/database, on which the DataBricks cluster
  should have the right to write. That schema is the one used by the SQLMesh
  models

* Create the `.env` environment file, by substituting the environment
  variables in the `.env.sample` file:
```bash
envsubst < .env.sample > .env
```
  * That `.env` file is handled in a different way from all the `.in` files,
  as it is imported by the `Makefile`. That `Makefile` can therefore not
  alter the `.env` file itself, otherwise there will be a catch 22 situation

* Execute the `init-files` target in order to substitute the environment
  variables into the model files, the test files and the configuration file:
```bash
make init-files
```

### SQLMesh plan
* Launch the SQLMesh plan:
```bash
make plan-prod # equivalent of:
sqlmesh plan
======================================================================
Successfully Ran 1 tests against duckdb
----------------------------------------------------------------------
`prod` environment will be initialized

Requirements:
+ pyspark==3.5.4
Models:
└── Added:
    ├── docs_example.pyspark
    ├── sqlmesh_example.full_model
    ├── sqlmesh_example.incremental_model
    └── sqlmesh_example.seed_model
Models needing backfill (missing dates):
└── docs_example.pyspark: 2024-12-26 - 2024-12-26
```

* Answer yes to the prompt:
```text
Apply - Backfill Tables [y/n]: y
Creating physical tables ━━━━ ... ━━━━━ 100.0% • 4/4 • 0:00:00

All model versions have been created successfully
```

## Simple Unity Catalog (UC) example
* References:
  * [Data Engineering Helpers - Knowledge Sharing - Unity Catalog (UC)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/unity-catalog/)
  * DataBricks engine:
  https://sqlmesh.readthedocs.io/en/stable/integrations/engines/databricks/
  * Spark engine:
  https://sqlmesh.readthedocs.io/en/stable/integrations/engines/spark/
  * Python models:
  https://sqlmesh.readthedocs.io/en/stable/concepts/models/python_models/
  * PySpark models:
  https://sqlmesh.readthedocs.io/en/stable/concepts/models/python_models/#pyspark
  * [Unity Catalog docs](https://docs.unitycatalog.io/)
    * [Unity Catalog docs - Integrations - Spark](https://docs.unitycatalog.io/integrations/unity-catalog-spark/)
	* [Unity Catalog docs - Integrations - DataBricks](https://sqlmesh.readthedocs.io/en/stable/integrations/engines/databricks/)
    * [Unity Catalog blog post - Integrating Spark with Unity Catalog via Open APIs](https://www.unitycatalog.io/blogs/integrating-apache-spark-with-unity-catalog-assets-via-open-apis)

* Change to the
  [`examples/008-unitycatalog-simple` directory](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/examples/008-unitycatalog-simple/)
  within the SQLMesh dedicated directory:
```bash
cd ~/dev/knowledge-sharing/ks-cheat-sheets/data-processing/sqlmesh/examples/008-unitycatalog-simple
```

* The project has been initialized with the `sqlmesh init spark` command

### Spark Connect server
* See
  [Data Engineering Helpers - Knowledge Sharing - Spark](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/)
  on how to install and use the Spark Connect server and client

* (If not already done so,) Launch the Spark Connect server:
```bash
sparkconnectstart
```

* (At the end of the work session,) Shutdown the Spark Connect server:
```bash
sparkconnectstop
```

### SQLMesh plan
* Launch the SQLMesh plan:
```bash
make plan-prod # equivalent of:
sqlmesh plan
======================================================================
Successfully Ran 1 tests against duckdb
----------------------------------------------------------------------
`prod` environment will be initialized

Requirements:
+ pyspark==3.5.4
Models:
└── Added:
    ├── docs_example.pyspark
    ├── sqlmesh_example.full_model
    ├── sqlmesh_example.incremental_model
    └── sqlmesh_example.seed_model
Models needing backfill (missing dates):
└── docs_example.pyspark: 2024-12-26 - 2024-12-26
```

* Answer yes to the prompt:
```text
Apply - Backfill Tables [y/n]: y
Creating physical tables ━━━━ ... ━━━━━ 100.0% • 4/4 • 0:00:00

All model versions have been created successfully
```

# Installation

## Clone this repository
* Clone this
  [Git repository](https://github.com/data-engineering-helpers/ks-cheat-sheets)
  and move into its SQLMesh directory:
```bash
mkdir -p ~/dev/knowledge-sharing
git clone https://github.com/data-engineering-helpers/ks-cheat-sheets ~/dev/knowledge-sharing/ks-cheat-sheets
cd ~/dev/knowledge-sharing/ks-cheat-sheets/data-processing/sqlmesh
```

## DuckDB
* See also
  [Data Engineering Helpers - Knowledge Sharing - DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/)
  for more details on how to install DuckDB

* DuckDB may be installed through the native packaging utility, when available
  (for instance, on MacOS, `brew install duckdb`), through binary artifacts
  (on Linux) or through one of the programming stack utilities (for instance,
  for the Python stack, `pip install -U duckdb`)

### Public data sets on DuckDB
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

## Unity Catalog (UC)
* See
  [Data Engineering Helpers - Knowledge Sharing - Unity Catalog (UC)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/unity-catalog/)
 (in this same Git repository) for details on how to install and use
 Unity Catalog (UC)

* For just some trial of Unity Catalog, it is generally easier to use
  Docker compose (`docker compose up`)
  
* For the seasoned data engineer, it makes however more sense to know what
  is under the hood and to maintain Unity Catalog (UC) natively with a
  Java Virtual Machine (JVM) and with a local PostgreSQL database to store
  the catalog (it can be the same PostgreSQL service storing some SQLMesh
  states, but with different databse, schema and user).
  * Building the UC JARs and publishing them goes something like:
```bash
cd ~/dev/infra/unitycatalog
git pull
sbt package publishLocal
```

* In a dedicated tab of the terminal window, launch the Unity Catalog
  (Control-C to terminate the service)
  * With the default port (`8080`):
```bash
./bin/start-uc-server
```
  * With an alternative port (_e.g._, `9090`):
```bash
./bin/start-uc-server -p 9090
```

* (Optionally,) To start the UC UI, in another dedicated tab of
  the terminal window:
* Start the UI through Yarn (Control-C to terminate the service):
```bash
cd ui
yarn install
yarn start
```

* To interact with the UC
  * When the UC server has been started on the default port (entities: `schema`,
  `volume`, `model_version`, `metastore`, `auth`, `catalog`, `function`,
  `permission`, `registered_model`, `user`, `table`):
```bash
bin/uc <entity> <operation>
```
  * When the UC server has been started on an alternative port (say `9090`),
  specify the `--server` parameter before the entity:
```bash
bin/uc --server http://localhost:9090 <entity> <operation>
```
  * List the catalogs (the default one is usually called `unity`):
```bash
bin/uc catalog list
```
  * List the schemas (the default one is usually called `default`):
```bash
bin/uc schema list --catalog unity
```
  * List the tables:
```bash
bin/uc table list --catalog unity --schema default
```
  * Browse the records of a given table (`numbers` is a sample usually
  provided with UC at the installation):
```bash
bin/uc table read --full_name unity.default.numbers
```

## Spark Connect
* See
  [Data Engineering Helpers - Knowledge Sharing - Spark](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/)
  on how to install and use the Spark Connect server and client

* See also the relevant documentation when using Spark with Unity Catalog (UC):
  https://docs.unitycatalog.io/integrations/unity-catalog-spark/

* For consistency reason, it is better, for the Unity Catalog (UC) connector,
  to use the JAR package generated by SBT (and published locally in the local
  Ivy2/Maven cache)
  * Check that the Unity Catalog Spark connector JAR package is
  in the local Ivy2/Maven cache:
```bash
ls -lFh ~/.ivy2/jars/io.unitycatalog*
```

* (If not already done so,) Launch the Spark Connect server:
```bash
sparkconnectstart
```

* (At the end of the work session,) Shutdown the Spark Connect server:
```bash
sparkconnectstop
```

## SQLMesh
* SQLMesh comes as a Python package, and may therefore installed simply with
  the Python packager. For instance:
```bash
python -mpip install -U "sqlmesh[web,databricks]"
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
make clean # equivalent of:
rm -rf .cache logs db.db
```

* To create a new project from scratch, execute the `sqlmesh init` command,
  specifying which
  [SQL dialect](https://github.com/tobymao/sqlglot/blob/main/sqlglot/dialects/dialect.py)
  to use (among, for instance, DataBricks, Drill, DuckDB, Hive, MySQL,
  PostgreSQL, Presto, Redshift, Snowflake, Spark, SQLite, Tableau, Trino).
  * Note that `python` is also available as a dialect: `sqlmesh init python`
  will create a project skeleton populated for Python as a dialect
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

## Local PostgreSQL server
* See also:
  * [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md#sqlmesh-database-and-user)
  * [SQLMesh docs - Connections guide](https://sqlmesh.readthedocs.io/en/stable/guides/connections/)
  * [SQLMesh docs - Scheduling guide](https://sqlmesh.readthedocs.io/en/stable/guides/scheduling/)

* When SQLMesh is used with the built-in scheduler
  * DuckDB is used by default to store the state permanently (by default,
    in the `db.db` DuckDB database file)
  * Another database may be used to store the state, for instance PostgreSQL

* When SQLMesh is used with external schedulers (for instance, Airflow),
  the state is stored on the backend database of the external scheduler
  (in the case of Airflow, that is often a PostgreSQL database)

* In the
  [Data Engineering Helpers - Knowledge Sharing - PostgreSQL guide](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md#sqlmesh-database-and-user),
  there is a section detailing how to create a `sqlmesh` database, a `sqlmesh`
  schema and the `sqlmesh` user on a local PostgreSQL database
  
### Setup of the configuration for the local PostgreSQL to store the state
* See https://sqlmesh.readthedocs.io/en/stable/guides/configuration/#overrides
  on the relevant SQLMesh configuration options
  * In particular, the password of the PostgreSQL database user may be specified
  within an environment variable, for instance
  `SQLMESH__GATEWAYS__LOCAL__STATE_CONNECTION__PASSWORD`
  * However, within that documentation, another method (not to expose the
  password in the Git repository) has been chosen; see the next bullet point
  for that alternative method

* As the `config.yaml` configuration files contain credentials for the
  PostgreSQL database (even though those credentials are just some samples
  for local services, some security scanners may bump onto them in GitHub
  repositories and report them as false positives)
  * Git stores only a sample version of the `config.yaml` configuration file,
    namely `config.yaml.sample`
  * The `config.yaml` configuration file, that SQLMesh is expecting,
    has to be copied from the `config.yaml.sample` file and:
	* The password has to be adjusted in it
  * That `config.yaml` configuration file is ignored by Git (so that
    the credentials do not appear in clear in the Git repository)
  * The sequence is therefore as the following:
```bash
cp config.yaml.sample config.yaml
sed -i.bak -e 's/<sqlmesh-pass>/<REPLACE-HERE-BY-THE-POSTGRESQL-USER-PASSWORD>/' config.yaml && rm -f config.yaml.bak
```
  * Check that the content of the `config.yaml` configuration file
    seems correct
```bash
cat config.yaml | yq -r '.gateways.local.state_connection'
```
```yaml
type: postgres
host: localhost
port: 5432
database: sqlmesh
user: sqlmesh
password: <REPLACE-HERE-BY-THE-POSTGRESQL-USER-PASSWORD>
```

* SQLMesh is now ready to run with:
  * DuckDB as the execution engine
  * Local PostgreSQL database server to store the state
  * See
  [Local PostgreSQL to store the state](#local-postgresql-to-store-the-state)
  for the walkthrough
  * The next sub-sections detail a few specifities of having PostgreSQL
  to store the SQLMesh state

### SQLMesh with PostgreSQL to store the state
* Follow the
  [same steps as in the pure DuckDB example](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/README.md#initial-models)
  * The behaviour of SQLMesh should be exactly the same, except that the state
  is now stored in the local PostgreSQL database, as can be checked with
  the state-related tables in the PostgreSQL database. See the remainder of
  this sub-section for the details

* After `sqlmesh plan`
  * The datasets are in the DuckDB database, namely the `dbwost.db` file.
  The content may still be queried with the `sqlmesh fetchdf` command, _e.g._:
```bash
sqlmesh fetchdf "select * from sqlmesh_example.full_model"
```
  * The state is stored in the PostgreSQL database. For instance:
    * List the state-related tables (the `-t` option is to display tuples only,
	that is, turn off the header, footer and comments):
```bash
# psql -h localhost -U sqlmesh -d sqlmesh -t -c "\dt"
psql -h localhost -U sqlmesh -d sqlmesh -t -c "select table_name from information_schema.tables where table_schema = 'sqlmesh'"
```
```sql
 _snapshots
 _environments
 _auto_restatements
 _intervals
 _plan_dags
 _versions
```
    * List the (virtual data) environments:
```bash
psql -h localhost -U sqlmesh -d sqlmesh -t -c "select * from _environments;"
```
    * List the intervals:
```bash
psql -h localhost -U sqlmesh -d sqlmesh -t -c "select * from _intervals;"
```
```sql
 36c6a51271164c7687215c2d6927c252 | 1735489690863 | "db"."sqlmesh_example"."seed_model"        | 372700188  | 2185867172 | 1734998400000 | 1735430400000 | f      | f          | f            | f
 1aae0371a4664f51925bd0101984be12 | 1735489690871 | "db"."sqlmesh_example"."incremental_model" | 1463271556 | 1880815781 | 1577836800000 | 1735430400000 | f      | f          | f            | f
 15be8abdaf62493c8ebfab91f72a9099 | 1735489690881 | "db"."sqlmesh_example"."full_model"        | 3906121019 | 2278521865 | 1734998400000 | 1735430400000 | f      | f          | f            | f
```

### Cleanup when a local PostgreSQL database stores the state
* Delete the datasets in DuckDB, the logs and the cache directories:
```bash
make clean # equivalent of:
rm -rf db.db .cache logs
```

* In order to clean the SQLMesh state in the local PostgreSQL database,
  there is a
  [Bash script, namely `tools/clean-pg-state.sh` in this Git repository](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/tools/clean-pg-state.sh)
  * That Bash script features a few sanity checks (for instance, that the
  `psql` command exists and works)
  * If the PostgreSQL parameters are different from the default ones,
  they can be altered in
  [that `tools/clean-pg-state.sh` Bash script]((https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/tools/clean-pg-state.sh))
  at its top
  * The remainded of this sub-section still details on how to clean the SQLMesh
  state from the local PostgreSQL database manually 

* Specify the list of the state-related tables in a Shell array variable:
```bash
table_list=($(psql -h localhost -U sqlmesh -d sqlmesh -t -c "select table_name from information_schema.tables where table_schema = 'sqlmesh'"))
```

* Clean/drop the state-related tables in PostgreSQL:
```bash
for table in "${table_list[@]}"; do echo "Dropping ${table} table..."; psql -h localhost -U sqlmesh -d sqlmesh -c "drop table if exists ${table};"; echo "... ${table} table dropped"; done
```

### Cleanup the changes when a local PostgreSQL database stores the state
* If needed, comment the clause for the `z` column in the `incremental_model`
  model (_e.g._, in the
  [`examples/002-postgresql-state/models/incremental_model.sql` model file](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/examples/002-postgresql-state/models/incremental_model.sql))
  * It should read something like:
```bash
grep "z" models/incremental_model.sql
    --'z' AS new_column, -- Added column
```

* The project is now ready to start afresh, with no memory nor any change
  when compared to the Git repository

## Local Airflow service
* See also
  [Data Engineering Helpers - Knowledge Sharing - Airflow](https://github.com/data-engineering-helpers/ks-cheat-sheets/tree/main/orchestrators/airflow)
  
