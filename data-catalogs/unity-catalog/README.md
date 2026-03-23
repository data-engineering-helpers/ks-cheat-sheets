# Cheat Sheet - Unity Catalog

## Table of Content (ToC)

* [Cheat Sheet \- Unity Catalog](#cheat-sheet---unity-catalog)
  * [Table of Content (ToC)](#table-of-content-toc)
  * [Overview](#overview)
  * [References](#references)
    * [Data Engineering helpers](#data-engineering-helpers)
    * [Unity Catalog documentation](#unity-catalog-documentation)
    * [Iceberg REST API](#iceberg-rest-api)
  * [Getting started](#getting-started)
    * [General](#general)
    * [Unity Catalog with Docker](#unity-catalog-with-docker)
    * [Interact with the UI](#interact-with-the-ui)
    * [Interact with the Unity Catalog CLI](#interact-with-the-unity-catalog-cli)
    * [Simple Spark](#simple-spark)
    * [Spark integrated with OSS Unity Catalog](#spark-integrated-with-oss-unity-catalog)
      * [Create external tables with Spark](#create-external-tables-with-spark)
      * [Create managed tables with Spark](#create-managed-tables-with-spark)
      * [Show the details of tables with Spark](#show-the-details-of-tables-with-spark)
      * [Life\-cycle of tables with Spark](#life-cycle-of-tables-with-spark)
      * [Managed tables](#managed-tables)
    * [Spark integrated with Databricks Unity Catalog](#spark-integrated-with-databricks-unity-catalog)
    * [Daft integrated with Unity Catalog](#daft-integrated-with-unity-catalog)
    * [Simple DuckDB](#simple-duckdb)
    * [DuckDB integrated with Unity Catalog](#duckdb-integrated-with-unity-catalog)
    * [Unity Catalog without Docker](#unity-catalog-without-docker)
      * [Check the content of the catalog when the db is PostgreSQL](#check-the-content-of-the-catalog-when-the-db-is-postgresql)
      * [Create the content of the catalog](#create-the-content-of-the-catalog)
      * [Browse the content of the catalog with the CLI](#browse-the-content-of-the-catalog-with-the-cli)
  * [Setup](#setup)
    * [Clone the Unity Catalog Git repository](#clone-the-unity-catalog-git-repository)
    * [Launch the Unity Catalog server with Java 21](#launch-the-unity-catalog-server-with-java-21)
    * [Launch the Unity Catalog server with docker\-compose](#launch-the-unity-catalog-server-with-docker-compose)
    * [WSL](#wsl)
    * [(Optional) Local PostgreSQL database](#optional-local-postgresql-database)
      * [Setup the PostgreSQL connection in the Hibernate property file](#setup-the-postgresql-connection-in-the-hibernate-property-file)
    * [Setup of DuckDB](#setup-of-duckdb)
      * [MacOS](#macos)
      * [Linux](#linux)
    * [Setup of Daft](#setup-of-daft)
    * [Launch the UI with JavaScript (JS)](#launch-the-ui-with-javascript-js)
      * [Prerequisites](#prerequisites)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

## Overview

[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/unity-catalog/README.md)
explains how to install and to use
[Unity Catalog](https://www.unitycatalog.io)
on premises, _e.g._, on a laptop or on a virtual machine (VM).

## References

### Data Engineering helpers

* [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md#unity-catalog-database-and-user)
* [Data Engineering Helpers - Knowledge Sharing - Lakebase](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/lakebase/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Databricks Apps](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/infrastructure/databricks-apps/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Hive Metastore](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/hive-metastore/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Egeria](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/egeria/README.md)
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box/blob/main/README.md)
* [Material for the Data platform - Data life cycle](https://github.com/data-engineering-helpers/data-life-cycle/blob/main/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Minio](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-storage/minio/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Trino](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/trino/README.md)
* [Data Engineering Helpers - Knowledge Sharing - DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Java world](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/java-world/README.md)
* [Data Engineering Helpers - Knowledge Sharing - JavaScipt (JS) world](https://github.com/data-engineering-helpers/ks-cheat-sheets/tree/main/programming/js-world)

### Unity Catalog documentation

* [Unity Catalog home page](https://www.unitycatalog.io)
* [GitHub - Unity Catalog page](https://github.com/unitycatalog/unitycatalog)
* [Unity Catalog docs](https://docs.unitycatalog.io/)
  * [Unity Catalog docs - Quickstart](https://docs.unitycatalog.io/quickstart/)
  * [Unity Catalog docs - Usage - CLI](https://docs.unitycatalog.io/usage/cli/)
  * [Unity Catalog docs - Deployment - PostgreSQL connection](https://docs.unitycatalog.io/deployment/#example-postgresql-connection)
  * [Unity Catalog docs - Integrations - Spark](https://docs.unitycatalog.io/integrations/unity-catalog-spark/)
  * [Unity Catalog docs - Integrations - DuckDB](https://docs.unitycatalog.io/integrations/unity-catalog-duckdb/)
  * [Unity Catalog docs - Integrations - XTable](https://docs.unitycatalog.io/integrations/unity-catalog-xtable/)
* [Unity Catalog blog post - Integrating Spark with Unity Catalog via Open APIs](https://www.unitycatalog.io/blogs/integrating-apache-spark-with-unity-catalog-assets-via-open-apis)

### Iceberg REST API

* [GitHub - Iceberg REST API Specification](https://github.com/apache/iceberg/blob/main/open-api/rest-catalog-open-api.yaml)
* [Article on Substack by Alex Merced](https://amdatalakehouse.substack.com/p/iceberg-rest-catalog-overview-1-introduction),
  Feb. 2025

## Getting started

### General

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

### Unity Catalog with Docker

* Unity Catalog publishes an
  [image on Docker Hub](https://hub.docker.com/r/unitycatalog/unitycatalog/tags)
  which, for some reason, may not correspond to the latest snapshot version
  * If that is the case (that the Docker Hub image does not correspond to the
  latest version), it can easily be built locally, with the tag that
  Docker compose will use:

```bash
docker build . -t unitycatalog/unitycatalog:latest
```

* Start the Unity Catalog server and its UI (type Control-C twice in order
  to stop both):

```bash
docker-compose up
```

### Interact with the UI

* Visit [Unity Catalog local page](http://localhost:3000)
![Unity Catalog UI running locally](/images/data-catalogs/uc-ui.png)

### Interact with the Unity Catalog CLI

* In a distinct terminal tab, use the UC CLI to create the `unityxt` (`xt`
  standing for extended, as that version of the catalog uses default storage
  location in order to support catalog-controlled tables, _i.e._, managed
  tables) catalog with a default storage location (for managed tables and
  managed volumes):

```bash
bin/uc catalog create --name unityxt \
  --storage_root /home/unitycatalog/etc/data --comment "Extended catalog"
```

* Create a `default` schema for the `unityxt` (extended) catalog:

```bash
bin/uc schema create --catalog unityxt --name default \
  --storage_root /home/unitycatalog/etc/data --comment "Default schema"
```

* Create the `unityxt.default.numbers` table, as a managed table:

```bash
bin/uc table create \
  --full_name unityxt.default.numbers \
  --columns "as_int int, as_double double" \
  --table_type MANAGED \
  --format DELTA \
  --properties '{"key1": "value1", "key2": "value2"}'
```

* Create the `unityxt.default.transactions` table, as a managed table:

```bash
bin/uc table create \
  --full_name unityxt.default.transactions \
  --columns "transaction_id int, item_name string" \
  --table_type MANAGED \
  --format DELTA \
  --properties '{"key1": "value1", "key2": "value2"}'
```

### Simple Spark

* That section shows how to simply use Spark just to browse the `numbers` data
  files directly on the file-system (not through Unity Catalog), as those have
  been created by the Kernel engine, and most of the tools (like the Parquet CLI
  on MacOS) are not able to read them

* Check the Parquet/Delta data files of the `numbers` table:

```bash
ls -laFh etc/data/external/unity/default/tables/numbers/
total 8
drwxr-xr-x@ 4 $USER  staff   128B Dec  2 14:52 _delta_log/
-rw-r--r--@ 1 $USER  staff   804B Dec  2 14:52 d1df15d1-33d8-45ab-ad77-465476e2d5cd-000.parquet
```

* Launch PySpark:

```bash
pyspark
```

* Within PySpark, create a DataFrame with the Parquet/Delta data files of
  the `numbers` table:

```python
df = spark.read.format("delta").parquet("etc/data/external/unity/default/tables/numbers/")
df.count()
15
df.show()
+------+------------------+
|as_int|         as_double|
+------+------------------+
|   564|188.75535598441473|
  ...
|   958| 509.3712727285101|
+------+------------------+
```

* To leave the PySpark shell:

```python
quit()
```

### Spark integrated with OSS Unity Catalog

* [Relevant documentation](https://docs.unitycatalog.io/integrations/unity-catalog-spark/)

* For consistency reason, it is better, for the Unity Catalog connector,
  to use the JAR package generated by SBT (and published locally in the local
  Ivy2/Maven cache)
  * Check that the Unity Catalog Spark connector JAR package is
  in the local Ivy2/Maven cache:

```bash
ls -lFh ~/.ivy2*/jars/io.unitycatalog*
```

* Launch PySpark (the configuration is here for both the main and the extended
  catalogs, namely `unity` and `unityxt`):

```bash
SC_VERSION=2.13
DL_VERSION=4.1.0
DL_JAR=delta-spark_$SC_VERSION:$DL_VERSION
UC_DOM=io.unitycatalog
UC_JAR=unitycatalog-spark_$SC_VERSION
pyspark --name "local-uc-test" \
  --packages "io.delta:$DL_JAR,$UC_DOM:$UC_JAR:$UC_VERSION" \
  --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
  --conf "spark.sql.catalog.spark_catalog=$UC_DOM.spark.UCSingleCatalog" \
  --conf "spark.sql.catalog.unity=$UC_DOM.spark.UCSingleCatalog" \
  --conf "spark.sql.catalog.unity.uri=http://localhost:8080" \
  --conf "spark.sql.catalog.unity.token=" \
  --conf "spark.sql.catalog.unityxt=$UC_DOM.spark.UCSingleCatalog" \
  --conf "spark.sql.catalog.unityxt.uri=http://localhost:8080" \
  --conf "spark.sql.catalog.unityxt.token=" \
  --conf "spark.sql.defaultCatalog=unity"
```

* Browse the catalogs:

```python
sql("show catalogs").show()
+---------------+
|        catalog|
+---------------+
|  spark_catalog|
|          unity|
|        unityxt|
+---------------+
```

* Select/switch to `unity` catalog:

```python
sql("use unity;")
```

* Select/switch to `unityxt` catalog:

```python
sql("use unityxt;")
```

* Browse the schemas:

```python
sql("show schemas").show()
+---------+
|namespace|
+---------+
|  default|
+---------+
```

* List the tables:

```python
sql("show tables in default;").show()
+---------+-----------------+-----------+
|namespace|        tableName|isTemporary|
+---------+-----------------+-----------+
|  default|        marksheet|      false|
|  default|marksheet_uniform|      false|
|  default|          numbers|      false|
|  default|   user_countries|      false|
+---------+-----------------+-----------+
```

#### Create external tables with Spark

* When a location is specified for the storage, the table is said to be
  external (to Unity Catalog)

* It means that only the metadata of the tables is stored in the catalog,
  not the content of the table itself. It also implies that when the table
  is deleted (dropped) from the catalog, only the metadata is removed from
  the catalog, but the data itself is preserved

* The location may be specified either:
  * In SQL, with the `location` parameter. For instance:

```python
sql("create table default.numbers (transaction_id int, item_name string) \
    using delta location '/tmp/some/path/transactions';")
```

* With the DataFrame API, with the `path` parameter. For instance:

```python
df = spark.createDataFrame(
  [(1, "socks"), (2, "chips"), (3, "air conditioner"), (4, "tea"),],
  ["transaction_id", "item_name"]
)
(
  df.write
    .mode("overwrite")
    .format("delta")
    .option("path", "/tmp/some/path/transactions")
    .saveAsTable("default.transactions")
)
```

* The location has to be expressed as an absolute path, either on the cloud
  or on the local file-system.
  * The rationale being that the location has to be understood without
  ambiguity by both the (Unity Catalog) server and the client tool (_e.g._,
  Spark, DuckDB, Daft), and both of them may run in different places.

#### Create managed tables with Spark

* When no location is specified, the table is said to be managed (by
  Unity Catalog)

* It means that both the metadata and the actual data are managed
  by the catalog. As a consequence, when the table is dropped,
  so is the corresponding data

* For catalog-managed tables, the `delta.feature.catalogManaged` property
  has to be set within the `tblproperties`, which may be specified
  thanks to the SQL API:

```python
sql("create table default.transactions (transaction_id int, item_name string) \
    using delta tblproperties('delta.feature.catalogManaged'='supported');")
```

* Create a Spark DataFrame, and then a temporary view from it (this allows
  to get access to the content of the table from the SQL API):

```python
df = spark.createDataFrame(
  [(1, "socks"), (2, "chips"), (3, "air conditioner"), (4, "tea"),],
  ["transaction_id", "item_name"]
)
df.createTempView("tiny_df")
```

* Create the catalog-managed Delta table from the content of the DataFrame
  with the SQL API (see also
  [Databricks doc - SQL Reference - Create a table](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-create-table-using)):

```python
sql("create table default.transactions2 (transaction_id int, item_name string) \
     using delta tblproperties('delta.feature.catalogManaged'='supported');")
```

* As a reminder, when a table is created that way, the columns do not appear
  in the Unity Catalog UI and/or CLI

* Inserting the content of the DataFrame into the Delta table may then be
  performed through the SQL API:

```python
sql("insert overwrite default.transactions select * from tiny_df;")
```

* As of March 2026, with the way (_e.g._, configuration) Spark is launched
  as seen above, the DataFrame API does not work, as the table paths are
  interpreted by Spark as local Hive Metastore paths (_i.e._, in the
  `spark-warehouse/` sub-directory, created by Spark dynamically), not as
  Unity Catalog paths

* The following two DataFrame API do not work with Unity Catalog; they are kept
  here for reference, so as to avoid wasting one's time trying them:

```python
(
  df.write
    .mode("overwrite")
    .format("delta")
    .saveAsTable("default.transactions")
)
(
  df.writeTo("unityxt.default.transactions2")
    .using("delta")
    .tableProperty('delta.feature.catalogManaged', 'supported')
    .createOrReplace()
)
```

#### Show the details of tables with Spark

* Show the table specification:

```python
sql("describe extended default.transactions;").show()
```

* Show the history of the table:

```python
sql("describe history default.transactions;").show()
```

#### Life-cycle of tables with Spark

* Show the table specification:

```python
sql("describe extended default.transactions;").show()
```

* Insert some values into the `transactions` table:

```python
sql("insert into default.transactions values (5, socks);")
```

* Check the values in the `transactions` table:

```python
sql("select * FROM default.transactions;").show()
+------+---------+-----+
|as_int|as_double|marks|
+------+---------+-----+
|     1|      0.0|    1|
+------+---------+-----+
```

* Show the history of the table:

```python
sql("describe history default.numbers;").show()
```

* Delete the `transactions` table:

```python
sql("drop table default.transactions;")
```

#### Managed tables

* The DataFrame `saveAsTable()` method works well:

```python
df = (
  spark
  .createDataFrame(
    [(1, "socks"), (2, "chips"), (3, "air conditioner"), (4, "tea"),],
    ["transaction_id", "item_name"])
)
df.write.format("delta").saveAsTable("default.transactions")
```

* With the DataFrame API:

```python
sql("create table default.transactions (transaction_id int, item_name string) \
     using delta tblproperties('delta.feature.catalogManaged'='supported');")
```

* To leave the PySpark shell:

```python
quit()
```

### Spark integrated with Databricks Unity Catalog

* Relevant documentation:
  * [Spark integration for Unity Catalog](https://docs.unitycatalog.io/integrations/unity-catalog-spark/)
  * [Databricks Community - Integrating Apache Spark with Databricks Unity Catalog Assets via Open APIs](https://community.databricks.com/t5/technical-blog/integrating-apache-spark-with-databricks-unity-catalog-assets/ba-p/97533)
  * [Databricks Community - How to use Databricks Unity Catalog as metastore for a local Spark session](https://community.databricks.com/t5/data-engineering/how-to-use-databricks-unity-catalog-as-metastore-for-a-local/td-p/101176)
  * [Allowing external access](https://learn.microsoft.com/en-us/azure/databricks/external-access/admin)

* Launch PySpark (for the Unity Catalog Spark connector JAR package,
  see in the installation section how to generate it):

```bash
SC_VERSION=2.13
DL_VERSION=4.1.0
DL_JAR=delta-spark_$SC_VERSION:$DL_VERSION
UC_DOM=io.unitycatalog
UC_JAR=unitycatalog-spark_$SC_VERSION
UC_CAT="<<Default-Unity-Catalog-catalog>>"
HDP_DOM=org.apache.hadoop
HDP_JAR=hadoop-aws:3.3.2
DBS_DOM="<<Databricks-domain-name>>"
DBS_PAT="<<Databricks-personal-access-token>>"
DBS_UC_URL=https://$DBS_DOM.cloud.databricks.com/api/2.1/unity-catalog
pyspark --name "s3-uc-test" \
  --packages "$HDP_DOM:$HDP_JAR,io.delta:$DL_JAR,$UC_DOM:$UC_JAR:$UC_VERSION" \
  --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
  --conf "spark.sql.catalog.spark_catalog=io.unitycatalog.spark.UCSingleCatalog"\
  --conf "spark.hadoop.fs.s3.impl=org.apache.hadoop.fs.s3a.S3AFileSystem" \
  --conf "spark.sql.catalog.$UC_CAT=$UC_DOM.spark.UCSingleCatalog" \
  --conf "spark.sql.catalog.$UC_CAT.uri=$DBS_UC_URL" \
  --conf "spark.sql.catalog.$UC_CAT.token=$DBS_PAT" \
  --conf "spark.sql.defaultCatalog=$UC_CAT"
```

* Browse the catalogs:

```python
sql("show catalogs").show()
+-------------+
|      catalog|
+-------------+
|spark_catalog|
|      samples|
+-------------+
```

* Browse the schemas:

```python
>>> sql("show schemas").show()
+------------------+
|         namespace|
+------------------+
|information_schema|
|           nyctaxi|
+------------------+
```

* List the tables:

```python
sql("show tables in nyctaxi;").show()
+---------+---------+-----------+
|namespace|tableName|isTemporary|
+---------+---------+-----------+
|  nyctaxi|    trips|      false|
+---------+---------+-----------+
```

* Select a default schema:

```python
sql("use nyctaxi;")
```

* Browse a few records of a specific table:

```python
>>> sql("select * from samples.nyctaxi.trips;").show()
```

* Quit PySpark:

```python
>>> quit()
```

### Daft integrated with Unity Catalog

* [Relevant documentation](https://docs.unitycatalog.io/integrations/unity-catalog-daft/)

* As of end 2024, with the release of the
  [new UC Python client](https://pypi.org/project/unitycatalog-client/) in the
  [v0.2.1 release](https://github.com/unitycatalog/unitycatalog/releases/tag/v0.2.1),
  Daft does not work anymore

* Launch a Python interpreter, for instance iPython:

```bash
python -mpip install -U ipython
ipython
```

* In the Python shell:

```python
import daft
from daft.unity_catalog import UnityCatalog

unity = UnityCatalog(
    endpoint="http://127.0.0.1:8080",
    token="not-used",
)
```

* List the catalogs:

```python
print(unity.list_catalogs())
['unity']
```

* List the schemas:

```python
print(unity.list_schemas("unity"))
['unity.default']
```

* List the tables:

```python
print(unity.list_tables("unity.default"))
['unity.default.numbers', 'unity.default.marksheet_uniform', \
 'unity.default.marksheet', 'unity.default.user_countries']
```

### Simple DuckDB

* In this sub-section, DuckDB is simply used to create table pointing to
  the data files of the tables (without using Unity Catalog). Here, DuckDB
  does not integrate with the Unity Catalog, it accesses the content of the
  tables directly dealing with the content of the data files

* Launch DuckDB:

```bash
duckdb
```

* (if not already done so,) Install the Delta extension, and load it:

```sql
install delta;
load delta;
```

* Create the `numbers` table in DuckDB, directly accessing the data files:

```sql
create table numbers as (select * from 'etc/data/external/unity/default/tables/numbers/*.parquet');
select * from numbers;
┌────────┬────────────────────┐
│ as_int │     as_double      │
│ int32  │       double       │
├────────┼────────────────────┤
│    564 │ 188.75535598441473 │
   ...
│    958 │  509.3712727285101 │
├────────┴────────────────────┤
│ 15 rows           2 columns │
└─────────────────────────────┘
```

* To leave the DuckDB shell:

```sql
.quit
```

### DuckDB integrated with Unity Catalog

* [DuckDB - Relevant documentation](https://docs.unitycatalog.io/integrations/unity-catalog-duckdb/)

* Launch DuckDB:

```bash
duckdb
```

* Then, in the DuckDB shell, run the following commands:

```sql
install uc_catalog from core_nightly;
load uc_catalog;
install delta;
load delta;
```

* If you have installed these extensions before, you may have to run
  update extensions and restart DuckDB for the following steps to work

* Now that we have DuckDB all set up, let's try connecting to UC
  by specifying a secret.

```sql
CREATE SECRET (
      TYPE UC,
      TOKEN 'not-used',
      ENDPOINT 'http://127.0.0.1:8080',
      AWS_REGION 'us-east-2'
 );
```

* You should see it print a short table saying `Success = true`.

* Then we attach the unity catalog to DuckDB.

```sql
ATTACH 'unity' AS unity (TYPE UC_CATALOG);
```

* Now we are ready to query. Try the following:

```sql
SHOW ALL TABLES;
SELECT * from unity.default.numbers;
```

* You should see the tables listed and the contents of the `numbers` table
  printed

* To quit DuckDB, press Controll-D (if your platform supports it),
  press Control-C, or use the `.exit` command in the DuckDB shell

* To leave the DuckDB shell:

```sql
.quit
```

### Unity Catalog without Docker

* Docker is very good to showcase Unity Catalog and getting started quickly,
  in a way easy to reproduce and document (as explained above)
  
* In order to gain a deeper knowledge of how Unity Catalog works,
  and to tweak its configuration, and in order to be more efficient
  (as running Docker consumes quite some resources in terms of both disk space
  and memory), it is interesting to see how Unity Catalog may be setup and
  run without involving Docker at all
  
* And since we are it, the following sub-section shows how to store the state
  of the Unity Catalog server within a PostgreSQL database, rather than in the native
  H2 embedded database
  
* In this section, everything runs locally. PostgreSQL, however, may run either
  locally or remotely, it does not make much difference (except that, if it runs
  remotely, an internet connection is needed)

#### Check the content of the catalog when the db is PostgreSQL

* Browse the list of tables related to Unity Catalog
  * With the `\dt` command:

```bash
psql -h localhost -U ucdba -d ucdb -c "\dt"
```

* With the `information_schema` schema:

```bash
psql -h localhost -U ucdba -d ucdb -c "select * from information_schema.tables \
  where table_schema='ucdba'"
```

#### Create the content of the catalog

* With the default H2 database, the Git repository comes with a catalog
  pre-installed.
  * With PostgreSQL, the catalog has to be created and configured

* In the remainder of this sub-section, the content comes from the catalog
  when configured with the H2 database, exported into JSON. It is hence used
  here to recreate the content of the catalog when configured with the
  (initially empty) PostgreSQL database

* For the catalog-managed tables, the catalog and schema have to be setup
  with a default storage location. In the remainder of this sub-section
  * A so-called extended catalog, named `unityxt` (xt standing for extended),
    will be created with a default storage location pointing to the temporary
    file-system (_i.e._, in `/tmp/unitycatalog/storage`)
  * A default schema, also setup with the same default storage location,
    will be created for that extended catalog

* Typically, for the catalog-managed tables, Unity Catlog stores
  * Catalog metadata in the `__unitystorage/catalogs/` sub-directory
    of the default storage location on the file-system
  * Schema metadata in the `__unitystorage/schemas/` sub-directory
    of the default storage location on the file-system

* As of March 2026, when using Spark to create tables, rather than using
  the Unity Catalog command-line (`uc table create` command), even though
  it does not seem to make any difference from the Spark point of view,
  the Unity Catalog UI does not show the column specifications (the schema of
  the table)

* Launch the Unity Catalog (UC) server in a dedicated terminal tab
  (reminder: type Control-C to stop the server)
  * With the default port (`8080`):

```bash
./bin/start-uc-server
```

* With an alternative port (_e.g._, `9090`):

```bash
./bin/start-uc-server -p 9090
```

* In a distinct terminal tab, if the `unity` catalog does not already exist
  (_e.g._, when the underlying database is PostgreSQL), use the UC client
  to create a `unity` catalog with a default storage location (for managed
  tables and managed volumes):

```bash
bin/uc catalog create --name unity --comment "Main catalog"
```

* Use the UC client to create the `unityxt` (`xt` standing for extended, as that
  version of the catalog uses default storage location in order to support
  catalog-controlled tables, _i.e._, managed tables) catalog with a default
  storage location (for managed tables and managed volumes):

```bash
mkdir -p /tmp/unitycatalog/storage
bin/uc catalog create --name unityxt \
  --storage_root /tmp/unitycatalog/storage --comment "Extended catalog"
```

* If the `default` schema for the `unity` catalog does not already exist
  (_e.g._, when using a PostgreSQL database), create it for the `unity` catalog:

```bash
bin/uc schema create --catalog unity --name default --comment "Default schema"
```

* Create a `default` schema for the `unityxt` (extended) catalog:

```bash
bin/uc schema create --catalog unityxt --name default \
  --storage_root /tmp/unitycatalog/storage --comment "Default schema"
```

* If not already existing, create the `unity.default.numbers` table,
  as an external table
  * The `storage_location` parameter is required for external tables,
    but is not needed for managed tables (as the storage location is that
    of the catalog and schema)
  * See also [relevant documentation](https://docs.unitycatalog.io/usage/cli/#33-create-a-table)

```bash
STR_FP=$HOME/some-uc-path/etc/data/external/unity/default/tables/numbers
bin/uc table create \
  --full_name unity.default.numbers \
  --columns "as_int int, as_double double" \
  --table_type EXTERNAL \
  --format DELTA \
  --properties '{"key1": "value1", "key2": "value2"}' \
  --storage_location "file://$STR_FP"
```

* Create the `unityxt.default.numbers` table, as a managed table:

```bash
bin/uc table create \
  --full_name unityxt.default.numbers \
  --columns "as_int int, as_double double" \
  --table_type MANAGED \
  --format DELTA \
  --properties '{"key1": "value1", "key2": "value2"}'
```

* Create the `unityxt.default.transactions` table, as a managed table:

```bash
bin/uc table create \
  --full_name unityxt.default.transactions \
  --columns "transaction_id int, item_name string" \
  --table_type MANAGED \
  --format DELTA \
  --properties '{"key1": "value1", "key2": "value2"}'
```

* If not already existing, create the `unity.default.marksheet` table,
  as an external table:

```bash
STR_FP=$HOME/some-uc-path/etc/data/external/unity/default/tables/marksheet
bin/uc table create \
  --full_name unity.default.marksheet \
  --columns "id int, name string, marks int" \
  --table_type EXTERNAL \
  --format DELTA \
  --properties '{"key1": "value1", "key2": "value2"}' \
  --storage_location "file://$STR_FP"
```

* Create the `unityxt.default.marksheet` table, as a managed table:

```bash
bin/uc table create \
  --full_name unityxt.default.marksheet \
  --columns "id int, name string, marks int" \
  --table_type MANAGED \
  --format DELTA \
  --properties '{"key1": "value1", "key2": "value2"}'
```

* If not already existing, create the `unity.default.marksheet_uniform` table,
  as an external table:

```bash
STR_FP=$HOME/some-uc-path/etc/data/external/unity/default/tables/marksheet_uniform
bin/uc table create \
  --full_name unity.default.marksheet_uniform \
  --columns "id int, name string, marks int" \
  --table_type EXTERNAL \
  --format DELTA \
  --properties '{"key1": "value1", "key2": "value2"}' \
  --storage_location "file://$STR_FP"
```

* Create the `unityxt.default.marksheet_uniform` table, as a managed table:

```bash
bin/uc table create \
  --full_name unityxt.default.marksheet_uniform \
  --columns "id int, name string, marks int" \
  --table_type MANAGED \
  --format DELTA \
  --properties '{"key1": "value1", "key2": "value2"}'
```

* Create the `user_countries` table:

```bash
STR_FP=$HOME/some-uc-path/etc/data/managed/unity/default/tables/user_countries
bin/uc table create \
  --full_name unity.default.user_countries \
  --columns "first_name string, age long, country string" \
  --table_type MANAGED \
  --format DELTA \
  --properties '{"key1": "value1", "key2": "value2"}'
  # --storage_location "file://$STR_FP"
```

* If not already existing, create the `json_files` volume
  * In the main catalog:

```bash
STR_FP=$HOME/some-uc-path/etc/data/managed/unity/default/volumes/json_files/
bin/uc volume create \
  --full_name unity.default.json_files \
  --volume_type EXTERNAL \
  --storage_location file://$STR_FP \
  --comment "External volume"
```

* In the extended catalog:

```bash
bin/uc volume create \
  --full_name unityxt.default.json_files \
  --volume_type MANAGED \
  --comment "External volume"
```

* Create the `txt_files` volume
  * In the main catalog:

```bash
STR_FP=$HOME/some-uc-path/etc/data/managed/unity/default/volumes/txt_files/
bin/uc volume create \
  --full_name unity.default.txt_files \
  --volume_type EXTERNAL \
  --storage_location file://$STR_FP \
  --comment "Managed volume"
```

* In the extended catalog:

```bash
bin/uc volume create \
  --full_name unityxt.default.txt_files \
  --volume_type MANAGED \
  --comment "Managed volume"
```

#### Browse the content of the catalog with the CLI

* List the catalogs:

```bash
bin/uc catalog list --output json
```

```json
[{"name":"unity","comment":"Main catalog","properties":{},"owner":null,"created_at":1721230405334,"created_by":null,"updated_at":null,"updated_by":null,"id":"f029b870-9468-4f10-badd-630b41e5690d"}]
```

* Get the details of the `unity` catalog:

```bash
bin/uc catalog get --name unity --output json
```

```json
{"name":"unity","comment":"Main catalog","properties":{},"owner":null,"created_at":1721234005334,"created_by":null,"updated_at":1734289209110,"updated_by":null,"id":"f029b870-9468-4f10-badd-630b41e5690d"}
```

* List the schemas:

```bash
bin/uc schema list --catalog unity --output json
```

```json
[{"name":"default","catalog_name":"unity","comment":"Default schema","properties":{},"full_name":"unity.default","owner":null,"created_at":1721234405571,"created_by":null,"updated_at":null,"updated_by":null,"schema_id":"b08dfd57-a939-46cf-b102-9b906b884fae"}]
```

* List the tables:

```bash
bin/uc table list --catalog unity --schema default --output jsonPretty
```

```json
[ {
  "name" : "marksheet",
  "catalog_name" : "unity",
  "schema_name" : "default",
  "table_type" : "MANAGED",
  "data_source_format" : "DELTA",
  "columns" : [ {
    "name" : "id",
    "type_text" : "int",
  ...
  } ],
  "storage_location" : "file://$HOME/some/path/unitycatalog/etc/data/external/unity/default/tables/user_countries/",
  "comment" : "Partitioned table",
  "properties" : { },
  "owner" : null,
  "table_id" : "26ed93b5-9a18-4726-8ae7-c89dfcfea069"
} ]
```

* It should show a few tables. Some details are truncated because of
  the nested nature of the data.
  * To see all the content, you can add `--output jsonPretty` to any command.

* Browse the metadata of one of those tables:

```bash
bin/uc table get --full_name unity.default.numbers --output jsonPretty
```

```json
{
  "name" : "numbers",
  "catalog_name" : "unity",
  "schema_name" : "default",
  "table_type" : "EXTERNAL",
  "data_source_format" : "DELTA",
  "columns" : [ {
    "name" : "as_int",
    "type_text" : "int",
    ...
  } ],
  "storage_location" : "file://$HOME/some/path/unitycatalog/etc/data/external/unity/default/tables/numbers/",
  "comment" : "External table",
  "properties" : {
    "key1" : "value1",
    "key2" : "value2"
  },
  ...
  "table_id" : "32025924-be53-4d67-ac39-501a86046c01"
}
```

* You can see that it is a Delta table. Now, specifically for Delta tables,
  this CLI can print a snippet of the content of a Delta table (powered by
  the [Delta Kernel Java project](https://delta.io/blog/delta-kernel/)).

* List the content of the `numbers` table:

```bash
bin/uc table read --full_name unity.default.numbers --output jsonPretty
```

* List the volumes:

```bash
bin/uc volume list --catalog unity --schema default --output jsonPretty
```

```json
[ {
  "catalog_name" : "unity",
  "schema_name" : "default",
  "name" : "json_files",
  ...
  "volume_type" : "EXTERNAL",
  "storage_location" : "file://$HOME/some/path/unitycatalog/etc/data/external/unity/default/volumes/json_files/",
  "full_name" : "unity.default.json_files"
}, {
  "catalog_name" : "unity",
  "schema_name" : "default",
  "name" : "txt_files",
  ...
  "volume_type" : "MANAGED",
  "storage_location" : "file://$HOME/some/path/unitycatalog/etc/data/managed/unity/default/volumes/txt_files/",
  "full_name" : "unity.default.txt_files"
} ]
```

* Get the details of the (external) `json_files` volume:

```bash
bin/uc volume get --full_name unity.default.json_files --output jsonPretty
```

```json
{
  "catalog_name" : "unity",
  "schema_name" : "default",
  "name" : "json_files",
  ...
  "volume_type" : "EXTERNAL",
  "storage_location" : "file://$HOME/some/path/unitycatalog/etc/data/external/unity/default/volumes/json_files/",
  "full_name" : "unity.default.json_files"
}
```

* Browse the files on the `json_files` volume:

```bash
bin/uc volume read --full_name unity.default.json_files
```

```text
d.json [file]
c.json [file]
dir1 [directory]
```

* Browse the files on the `txt_files` volume:

```bash
bin/uc volume read --full_name unity.default.txt_files
```

```text
b.txt [file]
a.txt [file]
```

* Get the details of the (managed) `txt_files` volume:

```bash
bin/uc volume get --full_name unity.default.txt_files --output jsonPretty
```

```json
{
  "catalog_name" : "unity",
  "schema_name" : "default",
  "name" : "txt_files",
  ...
  "volume_type" : "MANAGED",
  "storage_location" : "file://$HOME/some/pathinfra/unitycatalog/etc/data/managed/unity/default/volumes/txt_files/",
  "full_name" : "unity.default.txt_files"
}
```

## Setup

* See the
  [setup section of the Spark cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/README.md#setup)
  (in this same Git repository) for installation instructions about Java and Spark
* [Relevant documentation when using Spark with Unity Catalog (UC)](https://docs.unitycatalog.io/integrations/unity-catalog-spark/)
* The Unity Catalog service may either be started in containers thanks to
  Docker Compose, or directly with the Java 21 JVM. The following two sections
  show either of the methods
* The Unity Catalog UI relies on JavaScript (JS)/NodeJS

### Clone the Unity Catalog Git repository

* If not already done so, clone the Git repository of Unity Catalog,
  and move to the corresponding directory:

```bash
mkdir -p dev/infra
git clone git@github.com:unitycatalog/unitycatalog.git ~/dev/infra/unitycatalog
cd ~/dev/infra/unitycatalog
```

* For convenience, a Shell alias may be specified like
  * For the Java-based installation:

```bash
alias unitycatalogstart='cd ~/dev/infra/unitycatalog; bin/start-uc-server'
```

* For the container-based installation:

```bash
alias unitycatalogstart='cd ~/dev/infra/unitycatalog; docker-compose up'
```

* For convenience of documentation, the version (of Unity Catalog) is captured
  in an environment variable, which will be re-used everywhere in place of
  explicitly referring to the version:

```bash
UC_VERSION="$(cut -d\" -f2,2 version.sbt)"
```

* The Unity Catalog will then be started simply with the `unitycatalogstart`
  alias in a dedicated tab of the Shell terminal, and terminated with the
  Control-C key

### Launch the Unity Catalog server with Java 21

* See the
  [Java cheat sheet on this Git repository](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/java-world/README.md)
  for how to install/maintain a Java 17 stack on various platforms with
  [SDKMan](https://sdkman.io/),
  as well as tools like [SBT](https://www.scala-sbt.org/)

* Example of SDK commands to install/upgrade the Java stack (with the
  [Amazon Corretto Java distribution](https://aws.amazon.com/corretto/)):

```bash
sdk update
sdk install java 21.0.10-amzn
sdk default java 21.0.10-amzn
```

* Example of SDK commands to install, or upgrade, SBT:

```bash
sdk update
sdk install sbt
sdk upgrade sbt
```

* Build the JAR package with SBT:

```bash
sbt +compile +package
[info] welcome to sbt 1.9.9 (Amazon.com Inc. Java 21.0.10)
...
[info] Successfully generated code to $HOME/some/path/unitycatalog/target/clients/java
...
[success] Total time: 9 s, completed Dec 17, 2024, 5:07:53 PM
```

* Publish the JAR artifacts locally (in the Ivy2 and Maven local caches):

```bash
sbt +publishLocal +publishM2
[info] :: delivering :: io.unitycatalog#unitycatalog-spark_...
[info] delivering ivy file to $HOME/some/path/unitycatalog/connectors...
[info] published ivy to $HOME/.ivy2/local/io.unitycatalog/...
[success] Total time: 6 s, completed Dec 17, 2024, 5:04:18 PM
```

* A new feature of Spark 4.1, Delta 4.1 and associated Unity Catalog (0.5)
  is for Delta Lake to delegate the management of tables to the catalog.
  See the
  [documentation catalog-managed Delta tables](https://docs.delta.io/delta-catalog-managed-tables/)
  for more details
  * Set the managed-table property feature to true (it is set to false by default)

```bash
sed -i.bak1 \
  -e 's/server.managed-table.enabled=false/server.managed-table.enabled=true/' \
  etc/conf/server.properties
```

* Launch the Unity Catalog (Control-C to terminate the service)
  * With the default port (`8080`):

```bash
./bin/start-uc-server
```

* With an alternative port (_e.g._, `9090`):

```bash
./bin/start-uc-server -p 9090
```

### Launch the Unity Catalog server with `docker-compose`

* See the
  [Docker cheat sheet on this Git repository](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/infrastructure/docker/README.md)
  for how to install a Docker-compliant desktop tool on various platforms,
  as well as a few plugins like Docker compose and Docker BuildKit

* Launch the Unity Catalog with Docker Compose:

```bash
docker compose up
```

### WSL

* On Windows, open CMD and type wsl
* Install Git:

```bash
sudo apt-get install git 
```

* Navigate to the directory where you want to clone the repository.
* Clone the repository by doing:

```bash
git clone web_URL
```

* Navigate into the project you just cloned using cd command and make sure
  the following versions are installed correctly:
  * JDK 21 (check with `java -version` and `javac -version`)
  * sbt 1.9.9 (check both sbt version in this project and sbt script version
  → verify with `sbt -version`)
  * Scala 2.13.17 (this may vary, but it must be compatible with JDK 21
  and sbt 1.9.9 → verify with `scala -version`)
* To start the UI correctly, you need also to install NodeJS and Yarn
* From within the just cloned repository, the project can now be compiled
  and the JAR artifacts may be built:

```bash
build/sbt +compile +package
```

* Publish the JAR in the Ivy2 and Maven local caches/repositories:

```bash
build/sbt +publishLocal +publishM2
```

* Now start the UC server:

```bash
bin/start-uc-server 
```

* Open a new CMD, type wsl, and navigate to your project directory.
  From here, you should already be able to list Delta tables using the CLI:

```bash
bin/uc table list --catalog unity --schema default
```

* To [start the local UI](http://localhost:3000/), since we already started
  the server, just run:

```bash
cd /ui
yarn install
yarn start
```

At this point, a browser tab will automatically open.

### (Optional) Local PostgreSQL database

* See also
  [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md#unity-catalog-database-and-user)
  on how to install a PostgreSQL database server locally and how to create
  the `ucdb` database and the `ucdba` database user.
  * For convenience, the commands to create the `ucdb` database and
  `ucdba` user are reproduced in the remainder of this sub-section

* Create on PostgreSQL a `ucdb` database and a `ucdba` user:

```bash
$ psql -h $PG_SVR -U $PG_ADM_USR -d postgres -c "create database ucdb;"
CREATE DATABASE
$ psql -h $PG_SVR -U $PG_ADM_USR -d postgres \
  -c "create user ucdba with encrypted password '<ucdba-pass>'; \
      grant all privileges on database ucdb to ucdba;"
CREATE ROLE
GRANT
$ psql -h $PG_SVR -U $PG_ADM_USR -d ucdb \
  -c "grant all on schema public to ucdba;"
GRANT
```

* Check that the access to the PostgreSQL database works:

```bash
$ psql -h $PG_SVR -U ucdba -d ucdb -c "select 42 as nb;"
 nb 
----
 42
(1 row)
```

* Add the `ucdba` credentials to the local PostgreSQL configuration file:

```bash
echo "localhost:5432:*:ucdba:<ucdba-pass-see-above>" >> ~/.pgpass
chmod 600 ~/.pgpass
```

#### Setup the PostgreSQL connection in the Hibernate property file

* Specify the PostgreSQL database credentials as environment variables:

```bash
PG_UC_DB="ucdb"
PG_UC_USR="ucdba"
PG_UC_PWD="<ucdba-pass-see-above>"
```

* Replace, in the Hibernate property file, the H2 database by PostgreSQL details:

```bash
sed -i.bak1 \
  -e 's/org.h2.Driver/org.postgresql.Driver/' etc/conf/hibernate.properties
sed -i.bak2 \
  -e 's|jdbc:h2:file:./etc/db/h2db;DB_CLOSE_DELAY=-1|jdbc:postgresql://localhost:5432/ucdb|' \
  etc/conf/hibernate.properties
cat >> etc/conf/hibernate.properties < _EOF
hibernate.connection.user=ucdba
hibernate.connection.password=ucdba1234
_EOF
```

* Check the resulting Hibernate property file and compare it with
  [the sample on Unity Catalog documentation](https://docs.unitycatalog.io/deployment/#example-postgresql-connection):

```bash
cat etc/conf/hibernate.properties
```

* If everything seems correct, delete the `.bak` files created by
  the SED commands:

```bash
rm -f etc/conf/hibernate.properties.bak?
```

### Setup of DuckDB

* [Relevant documentation](https://docs.unitycatalog.io/integrations/unity-catalog-duckdb/)

* See also the
  [DuckDB cheat sheet on this Git repository](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/README.md)

#### MacOS

* On MacOS, DuckDB may be installed with HomeBrew:

```bash
brew install duckdb
```

#### Linux

* See
  [DuckDB installation page for Linux](https://duckdb.org/docs/installation/?version=stable&environment=cli&platform=linux&download_method=direct&architecture=x86_64)

* It would give something like:

```bash
DDB_ZIP=duckdb_cli-linux-amd64.zip
DDB_VER="$(curl -Ls https://api.github.com/repos/duckdb/duckdb/releases/latest \
           | grep 'tag_name' | cut -d':' -f2,2 | cut -d'"' -f2,2)"
curl -L https://github.com/duckdb/duckdb/releases/download/$DDB_VER/$DDB_ZIP \
  -o $DDB_ZIP
unzip -x duckdb_cli-linux-amd64.zip && rm -f duckdb_cli-linux-amd64.zip
mkdir -p ~/bin
mv duckdb ~/bin
chmod +x ~/bin/duckdb
export PATH="$HOME/bin:$PATH"
```

### Setup of Daft

* Install Daft, with its integration with Delta and Unity Catalog:

```bash
python -mpip install -U "getdaft[unity,deltalake]"
```

### Launch the UI with JavaScript (JS)

#### Prerequisites

* [NodeJS](https://nodejs.org/en/download/package-manager)
* [Yarn](https://classic.yarnpkg.com/lang/en/docs/install)

* If needed, install Yarn
  * For instance, with NPM:

```bash
npm -g install yarn
```

* Start the UI through Yarn:

```bash
cd ui
yarn install
yarn start
```
