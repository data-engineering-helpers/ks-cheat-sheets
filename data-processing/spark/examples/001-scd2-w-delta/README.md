# Knowledge Sharing (KS) - Spark - SCD2 with Delta

## Table of Content (ToC)

* [Knowledge Sharing (KS) \- Spark \- SCD2 with Delta](#knowledge-sharing-ks---spark---scd2-with-delta)
  * [Table of Content (ToC)](#table-of-content-toc)
  * [Overview](#overview)
   * [Delta Lake tables](#delta-lake-tables)
  * [References](#references)
  * [Getting started](#getting-started)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

## Overview

This
[documentation](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/001-scd2-w-delta/README.md)
aims at showcasing how to perform a "merge into" operation, from some Parquet
source data set into a Delta-enabled data set.

It is part of
[Spark-related tutorials/examples](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/README.md),
themselves part of the
[Spark-related cheat sheets](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/README.md).

This tutorial requires sample datasets, which may be setup thanks to the
[directory dedicated to managing sample datasets](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/000-data-setup/).

### Delta Lake tables

* See
  [Delta Lake - Table batch reads and writes](https://docs.delta.io/delta-batch/)
  for the various ways to create Delta Lake tables

* Delta Lake tables have to be created either by specifying a location (on the
  file-system or on a cloud storage), or by specifying a schema and table names:
  * SQL:

```sql
-- Create or replace table with location/path
CREATE OR REPLACE TABLE delta.`/tmp/delta/people10m` (
...
)

-- Create or replace table with schema and table names (without location)
CREATE OR REPLACE TABLE default.people10m (
)
```

* Python:

```python
# Create or replace table with location/path using DataFrame's schema and
# write/overwrite data to it
df.write.format("delta").mode("overwrite").save("/tmp/delta/people10m")

# Create table in the metastore using DataFrame's schema and write data to it
df.write.format("delta").saveAsTable("default.people10m")
```

* Use the `make init-database` target in order to create the (`dim_customer`)
  Delta Lake table if needed

* Use the `make check-database` target to check the content of the directory
  storing the Parquet data files of the Delta Lake table

* The main point is that discussion is to NOT use BOTH the location/path and
  the schema and table names
  * In the tutorial, the latter (using schema and
  table names) is featured
  * Typically, Spark/Delta stores the (Parquet/Delta) data files in the
  `spark-warehouse/<schema>.db/<table_name>/` directory, that is, for the
  `dim_customer` table in the `bronze` schema:
  `spark-warehouse/bronze.db/dim_customer/`

## References

* [Medium - Slowly Changing Dimensions Aren’t Slow — They’re About Respecting Time in Data](https://medium.com/@think-data/slowly-changing-dimensions-arent-slow-they-re-about-respecting-time-in-data-e3c64d088fd5)
  , Feb. 2026, [Think Data](https://medium.com/@think-data)
* [LinkedIn post - SCD Type 2 Implementation Simplified with Spark and Delta Lake](https://www.linkedin.com/posts/mathew-midhun_lets-simplify-scd2-implementation-ugcPost-7352104443984666624-rjPs/),
  July 2025, [Mathew Midhun](https://www.linkedin.com/in/mathew-midhun/)
* [LinkedIn post - A cheat sheet for building fail-safe/idempotent DataBricks jobs](https://www.linkedin.com/posts/jrlasak_databricks-dataengineering-etl-activity-7358425287455363072-x2yw/),
  August 2025, [Jakub Lasak](https://www.linkedin.com/in/jrlasak/)
* [GitHub - Datanomy](https://github.com/raulcd/datanomy)

### Delta Lake

* [Delta Lake documentation](https://docs.delta.io/)
  * [Delta Lake - Quick start guide](https://docs.delta.io/latest/quick-start.html)
  * [Delta Lake - Table batch reads and writes](https://docs.delta.io/delta-batch/)
  * [Delta Lake - Catalog-managed tables](https://docs.delta.io/delta-catalog-managed-tables/)

## Getting started

* Clean any previous work (including local Spark warehouse/database,
  Python virtual environment):

```bash
make cleaners
```

* Initialize the uv virtual environment (_e.g._, uv installs the Python dependencies
  in that dedicated virtual environment):

```bash
make init update
```

* Create the Delta tables in the local Spark warehouse/database:

```bash
make init-database
```

* Generate the initial and incremental data-sets (it crates an stores Parquet
  files for the initial and the incremental data-sets):

```bash
make init-datasets
```

* Analyze the generate data-sets with Datanomy:

```bash
make check-dataset-init
make check-dataset-incremental
```

* Ingest the initial and incremental data-sets, filling the Delta table:

```bash
make ingest-datasets
```

* Check the content of the database (Delta table) storage location on
  the file-system:

```bash
make check-database
```

* Browse the content of the database (Delta table):

```bash
make browse-database
```
