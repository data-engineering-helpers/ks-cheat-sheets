Cheat Sheet - Spark
===================

# Table of Content (ToC)
* [Overview](#overview)
* [References](#references)
  * [Data Engineering helpers](#data-engineering-helpers)
  * [Spark](#spark)
    * [Spark Connect](#spark-connect)
  * [Unity Catalog (UC)](#unity-catalog-uc)
* [Installation](#installation)
  * [Clone this repository](#clone-this-repository)
  * [Unity Catalog (UC)](#unity-catalog-uc-1)
  * [Spark](#spark-1)

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
* [Data Engineering Helpers - Knowledge Sharing - Jupyter, PySpark and DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/jupyter/jupyter-pyspark-duckdb/)
* [Data Engineering Helpers - Knowledge Sharing - Unity Catalog (UC)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/unity-catalog/)
* [Data Engineering Helpers - Knowledge Sharing - SQLMesh](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/)
* [Data Engineering Helpers - Knowledge Sharing - DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/)
* [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/)
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box)

## Spark
* [Apache Spark - Download Spark manually](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#manually-downloading)
* [Apache Spark - Doc - Getting started / Installation](https://spark.apache.org/docs/latest/api/python/getting_started/install.html)

### Spark Connect
* [Apache Spark - Doc - Spark Connect - Overview](https://spark.apache.org/docs/latest/spark-connect-overview.html)
* [Apache Spark - Doc - Spark Connect - Quick start](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_connect.html)


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

# Installation

## Clone this repository
* Clone this
  [Git repository](https://github.com/data-engineering-helpers/ks-cheat-sheets)
  and move into its Spark-related directory:
```bash
mkdir -p ~/dev/knowledge-sharing
git clone https://github.com/data-engineering-helpers/ks-cheat-sheets ~/dev/knowledge-sharing/ks-cheat-sheets
cd ~/dev/knowledge-sharing/ks-cheat-sheets/data-processing/spark
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

## Spark
* Relevant documentation when using Spark with Unity Catalog (UC):
  https://docs.unitycatalog.io/integrations/unity-catalog-spark/

* For consistency reason, it is better, for the Unity Catalog (UC) connector,
  to use the JAR package generated by SBT (and published locally in the local
  Ivy2/Maven cache)
  * Check that the Unity Catalog Spark connector JAR package is
  in the local Ivy2/Maven cache:
```bash
ls -lFh ~/.ivy2/jars/io.unitycatalog*
```

* Launch PySpark
  * With support for local Unity Catalog (UC) service:
```bash
UC_VERSION=0.3.0-SNAPSHOT
pyspark --name "local-uc" --master "local[*]" \
  --packages "io.delta:delta-spark_2.12:3.2.1,io.unitycatalog:unitycatalog-spark_2.12:${UC_VERSION}" \
  --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
  --conf "spark.sql.catalog.spark_catalog=io.unitycatalog.spark.UCSingleCatalog" \
  --conf "spark.sql.catalog.unity=io.unitycatalog.spark.UCSingleCatalog" \
  --conf "spark.sql.catalog.unity.uri=http://localhost:8080" \
  --conf "spark.sql.catalog.unity.token=" \
  --conf "spark.sql.defaultCatalog=unity"
```
  * Only with support for Delta:
```bash
pyspark --name "local" --master "local[*]" \
  --packages "io.delta:delta-spark_2.12:3.2.1" \
  --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
```

* Insert some values into the `numbers` table:
```python
sql("insert into default.numbers values (1, 0.0);")
```

* Check the values in the `numbers` table:
```python
sql("SELECT * FROM default.numbers;").show()
+------+---------+
|as_int|as_double|
+------+---------+
|     1|      0.0|
+------+---------+
```

