Cheat Sheet - Databricks Apps
=============================

# Table of Content (ToC)
* [Overview](#overview)
* [References](#references)
  * [Data Engineering helpers](#data-engineering-helpers)
  * [Databricks](#databricks)
  * [NYC taxis](#nyc-taxis)
  * [Ontos](#ontos)
  * [Involved technologies](#involved-technologies)
* [Pre\-requisites](#pre-requisites)
  * [Databricks CLI](#databricks-cli)
  * [Unity Catalog](#unity-catalog)
  * [Lakebase](#lakebase)
  * [Databricks Asset Bundle (DAB)](#databricks-asset-bundle-dab)
* [NYC taxi application](#nyc-taxi-application)
* [Ontos](#ontos-1)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/infrastructure/databricks-apps/README.md)
explains how to build, deploy and run full-stack applications thanks to
[Databricks Apps](https://docs.databricks.com/aws/en/dev-tools/databricks-apps/).

It demonstrates how to deploy
[Databricks Apps](https://docs.databricks.com/aws/en/dev-tools/databricks-apps/),
[Lakebase](https://www.databricks.com/product/lakebase) OLTP database, and
[synced tables](https://docs.databricks.com/aws/en/oltp/instances/sync-data/sync-table)
in
[Databricks Asset Bundles (DABs)](https://docs.databricks.com/aws/en/dev-tools/bundles/).

![Databricks Apps - Architecture - How it works](https://www.databricks.com/sites/default/files/inline-images/Screenshot-2025-11-19-at-5.20.16-PM.png)

At a high level:
* [Databricks Apps](https://docs.databricks.com/aws/en/dev-tools/databricks-apps/)
  serves as the front end where users explore and visualize data,
* [Lakebase](https://www.databricks.com/product/lakebase) provides the Postgres
  database that the app queries, keeping it close to live data from:
* [Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/)
  with synced tables,
* [Databricks Asset Bundles (DABs)](https://docs.databricks.com/aws/en/dev-tools/bundles/)
  tie everything together by defining and deploying all resources—app, database,
  and data synchronization—as one version-controlled unit

Two specific applications are detailed in this cheat sheet:
* An application visualizing the iconic
  [NYC taxi durations](https://www.kaggle.com/c/nyc-taxi-trip-duration),
  featured in the
  [introductory Databricks blog about Databricks Apps](https://www.databricks.com/blog/how-build-production-ready-data-and-ai-apps-databricks-apps-and-lakebase)
* [Ontos](https://github.com/databrickslabs/ontos),
  for which there is also a
  [dedicated cheat sheet on Data Engineering Helpers - Knowledge Sharing](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-product-management/ontos/README.md)

# References

## Data Engineering helpers
* [Data Engineering Helpers - Knowledge Sharing - Ontos](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-product-management/ontos/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Unity Catalog](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/unity-catalog/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Lakebase](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/lakebase/README.md)
* [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Kubernetes (k8s)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/infrastructure/k8s/README.md)
* [Data Engineering Helpers - Knowledge Sharing - JavaScipt (JS) world](https://github.com/data-engineering-helpers/ks-cheat-sheets/tree/main/programming/js-world)
* [Data Engineering Helpers - Knowledge Sharing - Python](https://github.com/data-engineering-helpers/ks-cheat-sheets/tree/main/programming/python)
* [Architecture principles for data engineering pipelines on the Modern Data Stack (MDS)](https://github.com/data-engineering-helpers/architecture-principles)

## Databricks
* [Databricks blog - How to Build Production-Ready Data and AI Apps with Databricks Apps and Lakebase](https://www.databricks.com/blog/how-build-production-ready-data-and-ai-apps-databricks-apps-and-lakebase)
  * [Companion Git repository - Databricks Solutions - Databricks DAB examples](https://github.com/databricks-solutions/databricks-dab-examples/tree/main/knowledge-base/app-react-lakebase)
* [Databricks docs - Lakebase](https://www.databricks.com/product/lakebase)
  * [Databricks docs - Synchronized tables](https://docs.databricks.com/aws/en/oltp/instances/sync-data/sync-table)
* [Databricks docs - Databricks Apps](https://docs.databricks.com/aws/en/dev-tools/databricks-apps/)
  * [Databricks docs - Databricks Apps - Lakebase as a resource](https://docs.databricks.com/aws/en/dev-tools/databricks-apps/lakebase)
  * [Companion Git repository - Databricks - Bundle examples](https://github.com/databricks/bundle-examples)
    * [GitHub - DAB examples - App with database](https://github.com/databricks/bundle-examples/tree/main/knowledge_base/app_with_database)
    * [GitHub - DAB examples - NYC taxi dashboard](https://github.com/databricks/bundle-examples/tree/main/knowledge_base/dashboard_nyc_taxi)
    * [GitHub - DAB examples - Database with catalog](https://github.com/databricks/bundle-examples/tree/main/knowledge_base/database_with_catalog)
	* [GitHub - DAB examples - Databricks App](https://github.com/databricks/bundle-examples/tree/main/knowledge_base/databricks_app)
* [Databricks docs - Service Principals](https://docs.databricks.com/aws/en/admin/users-groups/service-principals)
* [Databricks docs - Databricks Asset Bundles (DABs)](https://docs.databricks.com/aws/en/dev-tools/bundles/)
  * [Databricks docs - DAB - Variables](https://docs.databricks.com/aws/en/dev-tools/bundles/variables)
* [Databricks docs - Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli)

## NYC taxis
* [Databricks docs - Unity Catalog datasets - NYC taxis](https://docs.databricks.com/aws/en/discover/databricks-datasets#unity-catalog-datasets)
* [Kaggle - NYC taxi trip durations](https://www.kaggle.com/c/nyc-taxi-trip-duration)
* [Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/)
  provides access to a number of sample datasets in the `samples` catalog.
  These datasets may be reviewed in the [Catalog Explorer UI](https://docs.databricks.com/aws/en/catalog-explorer/)
  and referenced directly in a [notebook](https://docs.databricks.com/aws/en/notebooks/)
  or in [the SQL editor](https://docs.databricks.com/aws/en/sql/user/sql-editor/)
  by using the `<catalog-name>.<schema-name>.<table-name>` pattern.
* The `nyctaxi` schema (also known as a database) contains the `trips` table, which has details
  about taxi rides in New York City (NYC)
* The following statement returns the first 10 records in this table:
```sql
select * from samples.nyctaxi.trips limit 10;
```

## Ontos
* [GitHub - Databricks Labs - Ontos](https://github.com/databrickslabs/ontos)

## Involved technologies
* App frontend based on
  * [React](https://react.dev/)
  * [Vite](https://vite.dev/)
  * [TypeScript](https://www.typescriptlang.org/)
  * [TailwindCSS](https://tailwindcss.com/) for styling
* App backend based on
  * [FastAPI](https://fastapi.tiangolo.com/)
  * [uvicorn](https://www.uvicorn.org/)
  * [psycopg](https://psycopg.org/)
* Interactive charts and data tables based on
  * [AG Grid](https://ag-grid.com/)
  * [AG Charts](https://charts.ag-grid.com/)
* Low-latency queries from a
  [Lakebase](https://www.databricks.com/product/lakebase) PostgreSQL table
* Managed data synchronization from Delta table to Lakebase using
  [synced tables](https://docs.databricks.com/aws/en/oltp/instances/sync-data/sync-table)
* [Databricks SDK](https://databricks-sdk-py.readthedocs.io/)
  for secure OAuth 2.0 based auth with Lakebase
* Seamless deployment using
  [Databricks Asset Bundles (DABs)](https://docs.databricks.com/en/dev-tools/bundles/index.html)

# Pre-requisites

## Databricks CLI
* The [Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli)
  may be [installed](https://docs.databricks.com/aws/en/dev-tools/cli/install)
  with the native packager. For instance, on MacOS:
```bash
$ brew tap databricks/tap
$ brew install databricks
```

* The Databricks CLI configuration is usually stored in `~/.databrickscfg`.
  It contains profiles for every workspace the user has access to. Such
  profiles are usually like the following, that is, they specify the workspace
  URL and the
  [private access token (PAT)](https://docs.databricks.com/aws/en/dev-tools/auth/pat):
```txt
[dkt-sdbx]
host = https://company-dev.cloud.databricks.com
token = dapi00aa00aaxxxxx00
```

## Unity Catalog
* A catalog and a schema need to be setup so that new tables may be created
  into them

* For this cheat sheet, it is assumed that the catalog is `poc` and the schema
  (aka database) is `apps`

* It means that, thanks to the
  [Catalog Explorer UI](https://docs.databricks.com/aws/en/catalog-explorer/),
  it may usually be browsed on
  https://company-dev.cloud.databricks.com/explore/data/poc/apps/
	
* And all the Databricks workspaces have the NYC taxi dataset
  (`samples.nyctaxi.trips`) available for everyone:
  https://company-dev.cloud.databricks.com/explore/data/samples/nyctaxi/trips

## Lakebase
* A Lakebase/Postgres compute instance needs to be setup. Lakebase instances
  are usually available in the Lakebase tab of the Compute menu, or directly
  with https://company-dev.cloud.databricks.com/compute/database-instances
  
* For this cheat sheet, it is assumed that the Lakebase instance is called `lakebase-poc`.
  It should therefore be available through
  https://company-dev.cloud.databricks.com/compute/database-instances/lakebase-poc

* Note that the credentials for the admin users are generated dynamically and
  temporary. It is therefore advised to create specific users/roles dedicated
  to every use cases. For instance:
  * [NYC taxi database and user](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md#nyc-taxi-database-and-user)
  * [Ontos database and user](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md#ontos-database-and-user)

* For that cheat sheet, it is assumed that the following databases, users/roles
  and schemas have been created:
  * For the NYC taxi application:
    * Database: `nyctaxi`
    * User/role: `nyctaxi`
    * Schemas: `public` and `apps`
  * For Ontos:
    * Database: `ontos`
    * User/role: `ontos`
    * Schema: `public`

* Note that when Databricks synchronizes a table from the Unity Catalog towards
  a Lakebase table, it creates that table in a Postgres schema named according
  to the target schema in Unity Catalog
  * For this cheat sheet, the target Unity Catalog schema is assumed to be `apps`
  (in the `poc` catalog):
  https://company-dev.cloud.databricks.com/explore/data/poc/apps/
  * The Postgres user then needs to be granted access rights on that schema.
  It may be granted with the following command (already detailed in the
  [Postgres cheat sheet referenced above](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md#nyc-taxi-database-and-user)):
```bash
$ psql -h $PG_SVR -U $PG_ADM_USR -d nyctaxi -c "grant all on schema apps to nyctaxi;"
GRANT
```

## Databricks Asset Bundle (DAB)
* YAML files and resources:
  https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/infrastructure/databricks-apps/
  * Original files:
  https://github.com/databricks-solutions/databricks-dab-examples/tree/main/knowledge-base/app-react-lakebase/

# NYC taxi application
* The example app displays recent taxi trips in both table and chart format
  and automatically polls for new trips
  * It reads data from a Lakebase synced table, which mirrors a Delta table
  in Unity Catalog
  * The first step is to create a copy of the original NYC taxi duration table,
  adding an `id` field, which will serve later for the synchronization to
  Lakebase:
```sql
CREATE TABLE poc.apps.trips AS
  SELECT ROW_NUMBER() OVER (ORDER BY tpep_pickup_datetime) AS id, *
  FROM samples.nyctaxi.trips
;
```
  * The second step is to setup the
  [synchronization pipeline](https://docs.databricks.com/aws/en/oltp/instances/sync-data/sync-table).
  That may fairly easily be done with the
  [Catalog Explorer UI](https://docs.databricks.com/aws/en/catalog-explorer/).
  Say that the details are as following:
    * Source table: `samples.nyctaxi.trips`, which may usually be browsed on
	https://company-dev.cloud.databricks.com/explore/data/samples/nyctaxi/trips
	* Target catalog, schema and table: `poc.apps.nyctaxis`, which may then be browsed on
	(once the synchronization pipeline has completed)
	https://company-dev.cloud.databricks.com/explore/data/poc/apps/nyctaxis
	* Target Lakebase instance and database
  * For this cheat sheet, it is assumed that the NYC taxi dataset has been
  replicated into Lakebase with the following details:
    * Database: `nyctaxi`
	* Schema: `apps`
	* Table: `nyctaxis`
  * The synchronized table may therefore be browsed thanks to the following
  command:
```bash
$ psql -h $PG_SVR -U nyctaxi -d nyctaxi -c "select * from apps.nyctaxis limit 10;"
$ psql -h $PG_SVR -U nyctaxi -d nyctaxi -c "\copy (select * from apps.nyctaxis limit 10) to 'nyctaxi-sample.csv' delimiter ',' csv header;"
```

# Ontos
