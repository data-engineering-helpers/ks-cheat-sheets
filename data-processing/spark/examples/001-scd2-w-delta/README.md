# Knowledge Sharing (KS) - Spark - SCD2 with Delta

## Table of Content (ToC)

* [Knowledge Sharing (KS) \- Spark \- SCD2 with Delta](#knowledge-sharing-ks---spark---scd2-with-delta)
  * [Table of Content (ToC)](#table-of-content-toc)
  * [Overview](#overview)
    * [Delta Lake tables](#delta-lake-tables)
  * [References](#references)
    * [Data Engineering helpers](#data-engineering-helpers)
    * [SCD2 type ingestion](#scd2-type-ingestion)
    * [Delta Lake](#delta-lake)
  * [Getting started](#getting-started)
    * [Pure Delta Lake tables](#pure-delta-lake-tables)
    * [Integration with Unity Catalog (UC) only](#integration-with-unity-catalog-uc-only)
    * [Integration with Spark Connect (SC) only](#integration-with-spark-connect-sc-only)
    * [Integration with Spark Connect (SC) and Unity Catalog (UC)](#integration-with-spark-connect-sc-and-unity-catalog-uc)
    * [Use of Spark Declarative Pipelines (SDP) with SC and UC](#use-of-spark-declarative-pipelines-sdp-with-sc-and-uc)

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

The
[_Spark and related components_ sub-section of the Spark cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/README.md#spark-and-related-components)
details the various components in the Spark ecosystem. This Spark-related
tutorial features those components through a few variations:

* Pure Delta Lake tables
  * PySpark script:
  [`merge_customer_001_simple.py` script](src/001_scd2_w_delta/jobs/merge_customer_001_simple.py)
* Integration with Unity Catalog (UC) only
  * PySpark script:
  [`merge_customer_002_uc_only.py` script](src/001_scd2_w_delta/jobs/merge_customer_002_uc_only.py)
* Integration with Spark Connect (SC) only
  * PySpark script:
  [`merge_customer_003_sc_only.py` script](src/001_scd2_w_delta/jobs/merge_customer_003_sc_only.py)
* Integration with Spark Connect, itself using Unity Catalog (UC)
  * PySpark script:
  [`merge_customer_004_sc_and_uc.py` script](src/001_scd2_w_delta/jobs/merge_customer_004_sc_and_uc.py)

Each variation is detailed in the [_Getting started_ section](#getting-started)
below.

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

### Data Engineering helpers

* [Data Engineering Helpers - Knowledge Sharing - Java](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/java-world/)
* [Data Engineering Helpers - Knowledge Sharing - Python](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/python/)
* [Data Engineering Helpers - Knowledge Sharing - Spark](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/)
* [Data Engineering Helpers - Knowledge Sharing - Delta Lake](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/delta/)
* [Data Engineering Helpers - Knowledge Sharing - Spark Connect (SC)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/spark-connect/)
* [Data Engineering Helpers - Knowledge Sharing - Spark Declarative Pipelines (SDP)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/declarative-pipelines/)
* [Data Engineering Helpers - Knowledge Sharing - Unity Catalog (UC)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/unity-catalog/)

### SCD2 type ingestion

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

* Check the content of the database (Delta table) storage location on
  the file-system:

```bash
make check-database
```

* Generate the initial and incremental data-sets (it creates an stores Parquet
  files for the initial and the incremental data-sets):

```bash
make init-datasets
```

* Analyze the generate data-sets with Datanomy:

```bash
make check-dataset-init
make check-dataset-incremental
```

* The remaining of the tasks depends on the variations, featured each in its
  own sub-section below

### Pure Delta Lake tables

* PySpark script:
  [`merge_customer_001_simple.py` script](src/001_scd2_w_delta/jobs/merge_customer_001_simple.py)

* Ingest the initial and incremental data-sets, filling the Delta table:

```bash
make ingest-datasets-simple
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

### Integration with Unity Catalog (UC) only

* See
  [Data Engineering Helpers - Knowledge Sharing - Unity Catalog (UC)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/unity-catalog/)
  for the details on how to start the UC server and interact with UC client CLI

* PySpark script:
  [`merge_customer_002_uc_only.py` script](src/001_scd2_w_delta/jobs/merge_customer_002_uc_only.py)

* If not already done so, in a dedicated Shell tab, start the UC server (knowing
  that `~/dev/infra/unitycatalog` is the directory where the
  [Unity Catalog Git repository](https://github.com/unitycatalog/unitycatalog)
  has been cloned and UC has been built and packaged with
  `sbt +clean +compile +package +publishLocal +publishM2`):

```bash
pushd ~/dev/infra/unitycatalog
bin/start-uc-server # Control-C to stop the server
popd
```

* If not already done so, initialize the Unity Catalog with:
  * A `unityxt` (`xt` standing for extended, as that version of the catalog uses
  default storage location in order to support catalog-controlled tables,
  _i.e._, managed tables) catalog with a default storage location (for managed
  tables and managed volumes)
  * A `bronze` schema for the `unityxt` (extended) catalog
  * A `unityxt.bronze.dim_customer` table, as a managed table

```bash
make init-uc-all
```

* Ingest the initial and incremental data-sets, filling the Delta table:

```bash
make ingest-datasets-uc-only
```

* Browse the content of the `dim_customer` table:

```bash
make browse-uc
```

* When the session is done, delete everything in Unity Catalog (that is,
  the table, the schema and the catalog):

```bash
make clean-uc-all
```

### Integration with Spark Connect (SC) only

* [Data Engineering Helpers - Knowledge Sharing - Spark Connect (SC)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/spark-connect/)

* PySpark script:
  [`merge_customer_003_sc_only.py` script](src/001_scd2_w_delta/jobs/merge_customer_003_sc_only.py)

* Note that, as the Spark Connect (SC) server runs on the same machine (typically,
  the laptop)
  * The database, which is a Hive/Spark local database, is the same as for
  the use case without any Spark Connect (SC) setup, that is, in the
  `spark-warehouse/bronze.db/dim_customer/` directory
  * It would be cleaner to start the Spark Connect (SC) server elsewhere
  (_e.g._, in a temporary directory like `/tmp/sparkconnect/workspace`). But,
  then, the `make init-datasets` target would need to be adapted, as the
  Spark Connect (SC) server will search for those datasets where it has been
  started

* Potentially stop the Spark Connect (SC) server (to then start from a cleaner
  state):

```bash
make stop-sc
```

* Clean potential previous database on the Spark Connect (SC) server, whcih is
  on the same node/computer for that use case/example:

```bash
make clean-database
```

* If not already done so, generate the initial and incremental data-sets
  (it creates an stores Parquet files for the initial and the incremental
  data-sets):

```bash
make init-datasets
```

* If not already done so, start the Spark Connect (SC) server:

```bash
make start-sc-only
```

* Check that the Spark Connect (SC) server is running:

```bash
make check-sc
```

* Create the Delta tables on Spark Connect (SC) server:

```bash
make init-database-sc
```

* Check the content of the database (Delta table) on the Spark Connect (SC):

```bash
make check-database-sc
```

* Ingest the initial and incremental data-sets, filling the Delta table:

```bash
make ingest-datasets-sc-only
```

* Check the content of the database (Delta table) on the Spark Connect (SC):

```bash
make check-database-sc
```

* Potentially stop the Spark Connect (SC) server:

```bash
make stop-sc
```

* Clean the database on the Spark Connect (SC) server:

```bash
make clean-database
```

### Integration with Spark Connect (SC) and Unity Catalog (UC)

* PySpark script:
  [`merge_customer_004_sc_and_uc.py` script](src/001_scd2_w_delta/jobs/merge_customer_004_sc_and_uc.py)

* If not already done so, in a dedicated Shell tab, start the UC server (knowing
  that `~/dev/infra/unitycatalog` is the directory where the
  [Unity Catalog Git repository](https://github.com/unitycatalog/unitycatalog)
  has been cloned and UC has been built and packaged with
  `sbt +clean +compile +package +publishLocal +publishM2`):

```bash
pushd ~/dev/infra/unitycatalog
bin/start-uc-server # Control-C to stop the server
popd
```

* If not already done so, initialize the Unity Catalog with:
  * A `unityxt` (`xt` standing for extended, as that version of the catalog uses
  default storage location in order to support catalog-controlled tables,
  _i.e._, managed tables) catalog with a default storage location (for managed
  tables and managed volumes)
  * A `bronze` schema for the `unityxt` (extended) catalog
  * A `unityxt.bronze.dim_customer` table, as a managed table

```bash
make init-uc-all
```

* Potentially stop the Spark Connect (SC) server (to then start from a cleaner
  state):

```bash
make stop-sc
```

* If not already done so, start the Spark Connect (SC) server, itself connected
  to Unity Catalog (UC):

```bash
make start-sc-w-uc
```

* Check that the Spark Connect (SC) server is running:

```bash
make check-sc
```

* Ingest the initial and incremental data-sets, filling the Delta table:

```bash
make ingest-datasets-sc-w-uc
```

* Check the content of the database (Delta table) on the Spark Connect (SC):

```bash
make check-database-sc-w-uc
```

* Browse the content of the `dim_customer` table:

```bash
make browse-uc
```

* When the session is done, stop the Spark Connect (SC) server:

```bash
make stop-sc
```

* When the session is done, delete everything in Unity Catalog (that is,
  the table, the schema and the catalog):

```bash
make clean-uc-all
```

### Use of Spark Declarative Pipelines (SDP) with SC and UC

* [Data Engineering Helpers - Knowledge Sharing - Spark Declarative Pipelines (SDP)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/declarative-pipelines/)

* Just for reference, SDP was installed with the following command, as part of
  the Spark ecosystem:

```bash
python -mpip install "pyspark[connect,sql,pipelines,pandas_on_spark]" delta-spark
```

* Still just for reference, the directory with the SDP pipeline, namely
  [`sdp-005-sc-w-uc`](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/001-scd2-w-delta/sdp-005-sc-w-uc/),
  has been created with the following command:
  `spark-pipelines init --name sdp-005-sc-w-uc`

* If needed, copy the
  [`sdp-005-sc-w-uc/spark-pipeline.yml.sample` specification file](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/001-scd2-w-delta/sdp-005-sc-w-uc/)
  into the Git-ignored `sdp-005-sc-w-uc/spark-pipeline.yml` file and change
  the `storage` value to reflect your setup

* If not already done so, in a dedicated Shell tab, start the UC server (knowing
  that `~/dev/infra/unitycatalog` is the directory where the
  [Unity Catalog Git repository](https://github.com/unitycatalog/unitycatalog)
  has been cloned and UC has been built and packaged with
  `sbt +clean +compile +package +publishLocal +publishM2`):

```bash
pushd ~/dev/infra/unitycatalog
bin/start-uc-server # Control-C to stop the server
popd
```

* If not already done so, initialize the Unity Catalog with:
  * A `unityxt` (`xt` standing for extended, as that version of the catalog uses
  default storage location in order to support catalog-controlled tables,
  _i.e._, managed tables) catalog with a default storage location (for managed
  tables and managed volumes)
  * A `bronze` schema for the `unityxt` (extended) catalog
  * A `unityxt.bronze.dim_customer` table, as a managed table

```bash
make init-uc-all
```

* Potentially stop the Spark Connect (SC) server (to then start from a cleaner
  state):

```bash
make stop-sc
```

* If not already done so, start the Spark Connect (SC) server, itself connected
  to Unity Catalog (UC):

```bash
make start-sc-w-uc
```

* Check that the Spark Connect (SC) server is running:

```bash
make check-sc
```
