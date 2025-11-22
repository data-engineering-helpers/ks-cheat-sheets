Cheat Sheet - Databricks Apps
=============================

# Table of Content (ToC)

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
* [Databricks docs - Databricks Apps](https://docs.databricks.com/aws/en/dev-tools/databricks-apps/)
* [Databricks docs - Lakebase](https://www.databricks.com/product/lakebase)
  * [Databricks docs - Synchronized tables](https://docs.databricks.com/aws/en/oltp/instances/sync-data/sync-table)
* [Databricks docs - Databricks Asset Bundles (DABs)](https://docs.databricks.com/aws/en/dev-tools/bundles/)
* [GitHub - Databricks Solutions - Databricks DAB examples](https://github.com/databricks-solutions/databricks-dab-examples/tree/main/knowledge-base/app-react-lakebase)

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
* Interactive charts and data tables based on
  * [AG Grid](https://ag-grid.com/)
  * [AG Charts](https://charts.ag-grid.com/)
* Low-latency queries from a [Lakebase](https://www.databricks.com/product/lakebase) PostgreSQL table
* Managed data synchronization from Delta table to Lakebase using
  [synced tables](https://docs.databricks.com/aws/en/oltp/instances/sync-data/sync-table)
* [Databricks SDK](https://databricks-sdk-py.readthedocs.io/)
  for secure OAuth 2.0 based auth with Lakebase
* Seamless deployment using
  [Databricks Asset Bundles (DABs)](https://docs.databricks.com/en/dev-tools/bundles/index.html)

# Pre-requisites

## Unity Catalog
* A catalog and a schema need to be setup so that new tables may be created
  into them

* For this cheat sheet, it is assumed that the catalog is `poc` and the schema
  (aka database) is `default`

* It means that, thanks to the
  [Catalog Explorer UI](https://docs.databricks.com/aws/en/catalog-explorer/),
  it may usually be browsed on
  https://your-workspace.cloud.databricks.com/explore/data/poc/default/
	
* And all the Databricks workspaces have the NYC taxi dataset
  (`samples.nyctaxi.trips`) available for everyone:
  https://your-workspace.cloud.databricks.com/explore/data/samples/nyctaxi/trips

## Lakebase
* A Lakebase/Postgres compute instance needs to be setup. Lakebase instances
  are usually available in the Lakebase tab of the Compute menu, or directly
  with https://your-workspace.cloud.databricks.com/compute/database-instances
  
* For this cheat sheet, it is assumed that the Lakebase instance is called `lakebase-poc`.
  It should therefore be available through
  https://your-workspace.cloud.databricks.com/compute/database-instances/lakebase-poc

* Note that the credentials for the admin users are temporary. It is therefore advised
  to create specific users/roles dedicated to every use cases. For instance:
  * [Ontos database and user](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md#ontos-database-and-user)
  * [NYC taxi database and user](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md#nyc-taxi-database-and-user)

# NYC taxi application
* The example app displays recent taxi trips in both table and chart format
  and automatically polls for new trips
  * It reads data from a Lakebase synced table, which mirrors a Delta table
  in Unity Catalog
  * The first step is thus to setup that
  [synchronization pipeline](https://docs.databricks.com/aws/en/oltp/instances/sync-data/sync-table).
  That may fairly easily be done with the
  [Catalog Explorer UI](https://docs.databricks.com/aws/en/catalog-explorer/).
  Say that the details are as following:
    * Source table: `samples.nyctaxi.trips`, which may usually be browsed on
	https://your-workspace.cloud.databricks.com/explore/data/samples/nyctaxi/trips
	* Target catalog, schema and table: `poc.default.nyctaxis`, which may then be browsed on
	(once the synchronization pipeline has completed)
	https://your-workspace.cloud.databricks.com/explore/data/poc/default/nyctaxis
	* Target Lakebase instance and database
  * For this cheat sheet, it is assumed that the NYC taxi dataset has been replicated into


* The NYC taxi

# Ontos
