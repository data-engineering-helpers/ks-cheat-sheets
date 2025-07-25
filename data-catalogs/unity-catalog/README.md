Cheat Sheet - Unity Catalog
===========================

# Table of Content (ToC)
* [Overview](#overview)
* [References](#references)
  * [Data Engineering helpers](#data-engineering-helpers)
  * [Unity Catalog documentation](#unity-catalog-documentation)
  * [Iceberg REST API](#iceberg-rest-api)
* [Getting started](#getting-started)
  * [Browse the content of the catalog with the CLI](#browse-the-content-of-the-catalog-with-the-cli)
  * [Simple DuckDB](#simple-duckdb)
  * [DuckDB integrated with Unity Catalog](#duckdb-integrated-with-unity-catalog)
  * [Simple Spark](#simple-spark)
  * [Spark integrated with OSS Unity Catalog](#spark-integrated-with-oss-unity-catalog)
    * [Managed vs external tables](#managed-vs-external-tables)
    * [Create a table the SQL way](#create-a-table-the-sql-way)
    * [Create a table through the DataFrame API](#create-a-table-through-the-dataframe-api)
    * [Managed tables](#managed-tables)
  * [Spark integrated with Databricks Unity Catalog](#spark-integrated-with-databricks-unity-catalog)
  * [Daft integrated with Unity Catalog](#daft-integrated-with-unity-catalog)
  * [Interact with the UI](#interact-with-the-ui)
* [Installation](#installation)
  * [Clone the Unity Catalog Git repository](#clone-the-unity-catalog-git-repository)
  * [Launch the Unity Catalog server with Java 17](#launch-the-unity-catalog-server-with-java-17)
  * [Launch the Unity Catalog server with docker\-compose](#launch-the-unity-catalog-server-with-docker-compose)
  * [WSL](#wsl)
  * [(Optional) Local PostgreSQL database](#optional-local-postgresql-database)
    * [Setup the PostgreSQL connection in the Hibernate property file](#setup-the-postgresql-connection-in-the-hibernate-property-file)
    * [Create the content of the catalog](#create-the-content-of-the-catalog)
  * [Spark](#spark)
  * [DuckDB](#duckdb)
    * [MacOS](#macos)
    * [Linux](#linux)
  * [Daft](#daft)
  * [Launch the UI with JavaScript (JS)](#launch-the-ui-with-javascript-js)
    * [Prerequisites](#prerequisites)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/unity-catalog/README.md)
explains how to install and to use
[Unity Catalog](https://www.unitycatalog.io)
on premises, _e.g._, on a laptop or on a virtual machine (VM).

# References

## Data Engineering helpers
* [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md#unity-catalog-database-and-user)
* [Data Engineering Helpers - Knowledge Sharing - Hive Metastore](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/hive-metastore/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Egeria](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/egeria/README.md)
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box/blob/main/README.md)
* [Material for the Data platform - Data life cycle](https://github.com/data-engineering-helpers/data-life-cycle/blob/main/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Minio](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-storage/minio/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Trino](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/trino/README.md)
* [Data Engineering Helpers - Knowledge Sharing - DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Java world](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/java-world/README.md)
* [Data Engineering Helpers - Knowledge Sharing - JavaScipt (JS) world](https://github.com/data-engineering-helpers/ks-cheat-sheets/tree/main/programming/js-world)

## Unity Catalog documentation
* Home page: https://www.unitycatalog.io
* GitHub page: https://github.com/unitycatalog/unitycatalog
* [Unity Catalog docs](https://docs.unitycatalog.io/)
  * [Unity Catalog docs - Quickstart](https://docs.unitycatalog.io/quickstart/)
  * [Unity Catalog docs - Usage - CLI](https://docs.unitycatalog.io/usage/cli/)
  * [Unity Catalog docs - Deployment - PostgreSQL connection](https://docs.unitycatalog.io/deployment/#example-postgresql-connection)
  * [Unity Catalog docs - Integrations - Spark](https://docs.unitycatalog.io/integrations/unity-catalog-spark/)
  * [Unity Catalog docs - Integrations - DuckDB](https://docs.unitycatalog.io/integrations/unity-catalog-duckdb/)
  * [Unity Catalog docs - Integrations - XTable](https://docs.unitycatalog.io/integrations/unity-catalog-xtable/)
* [Unity Catalog blog post - Integrating Spark with Unity Catalog via Open APIs](https://www.unitycatalog.io/blogs/integrating-apache-spark-with-unity-catalog-assets-via-open-apis)

## Iceberg REST API
* Specification in GitHub: https://github.com/apache/iceberg/blob/main/open-api/rest-catalog-open-api.yaml
* Article on Substack by Alex Merced, Feb. 2025: https://amdatalakehouse.substack.com/p/iceberg-rest-catalog-overview-1-introduction

# Getting started
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

## Browse the content of the catalog with the CLI
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

## Simple DuckDB
* In this sub-section, DuckDB is simply used to create table pointing to
  the data files of the tables. Here, DuckDB does not integrate with the
  Unity Catalog, it accesses the content of the tables directly dealing
  with the content of the data files

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

## DuckDB integrated with Unity Catalog
* Relevant documentation: https://docs.unitycatalog.io/integrations/unity-catalog-duckdb/

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

## Simple Spark
* That section shows how to simply use Spark just to browse the `numbers` data
  files, as those have been created by the Kernel engine, and most of
  the tools (like the Parquet CLI on MacOS) are not able to read them

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

## Spark integrated with OSS Unity Catalog
* Relevant documentation: https://docs.unitycatalog.io/integrations/unity-catalog-spark/

* Launch PySpark (for the Unity Catalog Spark connector JAR package,
  see in the installation section how to generate it):
```bash
pyspark --name "local-uc-test" \
  --master "local[*]" \
  --packages "io.delta:delta-spark_2.12:3.2.1,io.unitycatalog:unitycatalog-spark_2.12:${UC_VERSION}" \
  --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
  --conf "spark.sql.catalog.spark_catalog=io.unitycatalog.spark.UCSingleCatalog" \
  --conf "spark.sql.catalog.unity=io.unitycatalog.spark.UCSingleCatalog" \
  --conf "spark.sql.catalog.unity.uri=http://localhost:8080" \
  --conf "spark.sql.catalog.unity.token=" \
  --conf "spark.sql.defaultCatalog=unity"
```

* Browse the catalogs:
```python
sql("show catalogs").show()
+-------------+
|      catalog|
+-------------+
|spark_catalog|
|        unity|
+-------------+
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

* Select a default schema:
```python
sql("use default;")
```

### Managed vs external tables
* With Unity Catalog:
  * When a location is specified for the storage, the table is said to be
  external.
  * It means that only the metadata of the tables is stored in the catalog,
  not the content of the table itself. It also implies that when the table
  is deleted (dropped) from the catalog, only the metadata is removed from
  the catalog, but the data itself is preserved.
  * When no location is specified, the table is said to be managed (by
  Unity Catalog).
  * It means that both the metadata and the actual data are managed
  by the catalog. As a consequence, when the table is dropped,
  so is the corresponding data.

* The location may be specified either:
  * In SQL, with the `location` parameter. For instance:
```python
sql("create table default.numbers (as_int int, as_double double) using delta location '/tmp/some/path/numbers';")
```
  * With the DataFrame API, with the `path` parameter. For instance:
```python
df.write.mode("overwrite").format("delta").option("path", "/tmp/some/path/numbers").saveAsTable("default.numbers")
```

* The location has to be expressed as an absolute path, either on the cloud
  or on the local file-system.
  * The rationale being that the location has to be understood without
  ambiguity by both the (Unity Catalog) server and the client tool (_e.g._,
  Spark, DuckDB, Daft), and both of them may run in different places.

### Create a table the SQL way
* Create an external table:
```python
sql("create table default.numbers2 (as_int int, as_double double) using delta location 'etc/data/external/tables/numbers2';")
```

* Show the table specification:
```python
sql("describe extended default.numbers2;").show()
```

* Insert some values into the `numbers` table:
```python
sql("insert into default.numbers2 values (1, 0.0);")
```

* Check the values in the `numbers2` table:
```python
sql("select * FROM default.numbers2;").show()
+------+---------+-----+
|as_int|as_double|marks|
+------+---------+-----+
|     1|      0.0|    1|
+------+---------+-----+
```

* Show the history of the table:
```python
sql("describe history default.numbers2;").show()
```

* Delete the `numbers2` table:
```python
sql("drop table default.numbers2;")
```

### Create a table through the DataFrame API
* Create a DataFrame and create an external table by dumping the content of
  the DataFrame in it:
```python
df = spark.createDataFrame([(1, "socks"), (2, "chips"), (3, "air conditioner"), (4, "tea"),], ["transaction_id", "item_name"])
df.write.mode("overwrite").format("delta").option("path", "/tmp/some/path/numbers3").saveAsTable("default.transactions")
```

* Show the table specification:
```python
sql("describe extended default.transactions;").show()
```

* Show the history of the table:
```python
sql("describe history default.transactions;").show()
```

* Delete the `transactions` table:
```python
sql("drop table default.transactions;")
```

### Managed tables
* As of end 2024 (version `0.3.0-SNAPSHOT`), it does not seem possible
  to create managed table with the open source version of Unity Catalog.
  * For instance, the DataFrame `saveAsTable()` method triggers an exception
  (`io.unitycatalog.client.ApiException: Unity Catalog does not support managed table`)
  * In SQL:
```python
df = spark.createDataFrame([(1, "socks"), (2, "chips"), (3, "air conditioner"), (4, "tea"),], ["transaction_id", "item_name"])
df.write.format("parquet").saveAsTable("default.transactions")
```
* With the DataFrame API:
```python
sql("create table default.transactions (transaction_id int, item_name string);")
```

* To leave the PySpark shell:
```python
quit()
```

## Spark integrated with Databricks Unity Catalog
* Relevant documentation:
  * Spark integration for Unity Catalog: https://docs.unitycatalog.io/integrations/unity-catalog-spark/
  * Integrating Apache Spark™ with Databricks Unity Catalog Assets via Open APIs:
  https://community.databricks.com/t5/technical-blog/integrating-apache-spark-with-databricks-unity-catalog-assets/ba-p/97533
  * How to use Databricks Unity Catalog as metastore for a local Spark session:
  https://community.databricks.com/t5/data-engineering/how-to-use-databricks-unity-catalog-as-metastore-for-a-local/td-p/101176
  * Allowing external access: https://learn.microsoft.com/en-us/azure/databricks/external-access/admin

* Launch PySpark (for the Unity Catalog Spark connector JAR package,
  see in the installation section how to generate it):
```bash
DBS_DOM="<<Databricks-domain-name>>"
DBS_PAT="<<Databricks-personal-access-token>>"
UC_CAT="<<Default-Unity-Catalog-catalog>>"
pyspark --name "s3-uc-test" \
  --packages "org.apache.hadoop:hadoop-aws:3.3.2,io.delta:delta-spark_2.12:3.2.1,io.unitycatalog:unitycatalog-spark_2.12:0.2.1" \
  --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
  --conf "spark.sql.catalog.spark_catalog=io.unitycatalog.spark.UCSingleCatalog" \
  --conf "spark.hadoop.fs.s3.impl=org.apache.hadoop.fs.s3a.S3AFileSystem" \
  --conf "spark.sql.catalog.$UC_CAT=io.unitycatalog.spark.UCSingleCatalog" \
  --conf "spark.sql.catalog.$UC_CAT.uri=https://$DBS_DOM.cloud.databricks.com/api/2.1/unity-catalog" \
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

## Daft integrated with Unity Catalog
* Relevant documentation: https://docs.unitycatalog.io/integrations/unity-catalog-daft/
 
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
['unity.default.numbers', 'unity.default.marksheet_uniform', 'unity.default.marksheet', 'unity.default.user_countries']
```

## Interact with the UI
* Visit http://localhost:3000
![Unity Catalog UI running locally](/images/data-catalogs/uc-ui.png)

# Installation
* The Unity Catalog service may either be started in containers thanks to
  Docker Compose, or directly with the Java 17 JVM. The following two sections
  show either of the methods
* The Unity Catalog UI relies on JavaScript (JS)/NodeJS

## Clone the Unity Catalog Git repository
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
alias unitycatalogstart='cd ~/dev/infra/unitycatalog; ./bin/start-uc-server'
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

## Launch the Unity Catalog server with Java 17
* See the
  [Java cheat sheet on this Git repository](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/java-world/README.md)
  for how to install/maintain a Java 17 stack on various platforms with
  [SDKMan](https://sdkman.io/), as well as tools like [SBT](https://www.scala-sbt.org/)

* Example of SDK commands to install/upgrade the Java stack (with the
  [Amazon Corretto Java distribution](https://aws.amazon.com/corretto/)):
```bash
sdk update
sdk install java 17.0.13-amzn
sdk default java 17.0.13-amzn
```

* Example of SDK commands to install, or upgrade, SBT:
```bash
sdk update
sdk install sbt
sdk upgrade sbt
```

* Build the JAR package with SBT:
```bash
sbt package
[info] welcome to sbt 1.9.9 (Amazon.com Inc. Java 17.0.13)
...
[info] Successfully generated code to $HOME/some/path/unitycatalog/target/clients/java
Generated classpath file '$HOME/some/path/unitycatalog/clients/python/target/classpath'
Generated classpath file '$HOME/some/path/unitycatalog/server/target/controlmodels/target/classpath'
Generated classpath file '$HOME/some/path/unitycatalog/target/classpath'
Generated classpath file '$HOME/some/path/unitycatalog/target/clients/java/target/classpath'
Generated classpath file '$HOME/some/path/unitycatalog/server/target/models/target/classpath'
Generated classpath file '$HOME/some/path/unitycatalog/target/control/java/target/classpath'
Generated classpath file '$HOME/some/path/unitycatalog/connectors/spark/target/scala-2.12/classpath'
Generated classpath file '$HOME/some/path/unitycatalog/server/target/classpath'
Generated classpath file '$HOME/some/path/unitycatalog/examples/cli/target/classpath'
[success] Total time: 9 s, completed Dec 17, 2024, 5:07:53 PM
```

* Publish the JAR packages locally (in the Ivy2/Maven local cache):
```bash
sbt publishLocal
[info] :: delivering :: io.unitycatalog#unitycatalog-spark_2.12;${UC_VERSION} :: ${UC_VERSION} :: integration :: Tue Dec 17 17:04:18 CET 2024
[info] 	delivering ivy file to $HOME/some/path/unitycatalog/connectors/spark/target/scala-2.12/ivy-${UC_VERSION}.xml
[info] 	published unitycatalog-spark_2.12 to $HOME/.ivy2/local/io.unitycatalog/unitycatalog-spark_2.12/${UC_VERSION}/poms/unitycatalog-spark_2.12.pom
[info] 	published unitycatalog-spark_2.12 to $HOME/.ivy2/local/io.unitycatalog/unitycatalog-spark_2.12/${UC_VERSION}/jars/unitycatalog-spark_2.12.jar
[info] 	published unitycatalog-spark_2.12 to $HOME/.ivy2/local/io.unitycatalog/unitycatalog-spark_2.12/${UC_VERSION}/srcs/unitycatalog-spark_2.12-sources.jar
[info] 	published unitycatalog-spark_2.12 to $HOME/.ivy2/local/io.unitycatalog/unitycatalog-spark_2.12/${UC_VERSION}/docs/unitycatalog-spark_2.12-javadoc.jar
[info] 	published ivy to $HOME/.ivy2/local/io.unitycatalog/unitycatalog-spark_2.12/${UC_VERSION}/ivys/ivy.xml
[success] Total time: 6 s, completed Dec 17, 2024, 5:04:18 PM
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

## Launch the Unity Catalog server with `docker-compose`
* See the
  [Docker cheat sheet on this Git repository](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/infrastructure/docker/README.md)
  for how to install a Docker-compliant desktop tool on various platforms,
  as well as a few plugins like Docker compose and Docker BuildKit

* Launch the Unity Catalog with Docker Compose:
```bash
docker compose up
```
## WSL
* On Windows, open CMD and type wsl.  
* Install Git:  
```
sudo apt-get install git 
``` 
* Navigate to the directory where you want to clone the repository.  
* Clone the repository by doing: 
```
git clone web_URL
```  
* Navigate into the project you just cloned using cd command and make sure the following versions are installed correctly:  
  * JDK 17 (check with java -version and javac -version.).  
  * sbt 1.9.9 (check both sbt version in this project and sbt script version → verify with sbt -version).  
  * Scala 2.13.15 (this may vary, but it must be compatible with JDK 17 and sbt 1.9.9 → verify with scala -version).  
* To start the UI correctly, you need also to install node.js and yarn.  
* From within the project you just cloned, we can now compile the project using:
```
build/sbt package
``` 
* Now start the UC server:
```
bin/start-uc-server 
```

* Open a new CMD, type wsl, and navigate to your project directory. 
From here, you should already be able to list Delta tables using the CLI: 
```
bin/uc table list --catalog unity --schema default  
```

* To start the UI at http://localhost:3000/, since we already started the server, just run:  
```
cd /ui  
yarn install  
yarn start
```  
At this point, a browser tab will automatically open.  

## (Optional) Local PostgreSQL database
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
$ psql -h $PG_SVR -U $PG_ADM_USR -d postgres -c "create user ucdba with encrypted password '<ucdba-pass>'; grant all privileges on database ucdb to ucdba;"
CREATE ROLE
GRANT
$ psql -h $PG_SVR -U $PG_ADM_USR -d ucdb -c "grant all on schema public to ucdba;"
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
echo "localhost:5432:ucdb:ucdba:<ucdba-pass-see-above>" >> ~/.pgpass
chmod 600 ~/.pgpass
```

### Setup the PostgreSQL connection in the Hibernate property file
* Specify the PostgreSQL database credentials as environment variables:
```bash
PG_UC_DB="ucdb"
PG_UC_USR="ucdba"
PG_UC_PWD="<ucdba-pass-see-above>"
```

* Replace, in the Hibernate property file, the H2 database by PostgreSQL details:
```bash
sed -i.bak1 -e 's/org.h2.Driver/org.postgresql.Driver/' etc/conf/hibernate.properties
sed -i.bak2 -e 's|jdbc:h2:file:./etc/db/h2db;DB_CLOSE_DELAY=-1|jdbc:postgresql://localhost:5432/ucdb|' etc/conf/hibernate.properties
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

### Create the content of the catalog
* With the default H2 database, the Git repository comes with a catalog
  pre-installed.
  * With PostgreSQL, the catalog has to be created and configured

* In the remainder of this sub-section, the content comes from the catalog
  when configured with the H2 database, exported into JSON. It is hence used
  here to recreate the content of the catalog when configured with the
  (initially empty) PostgreSQL database

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

* (In a distinct terminal tab,) use the UC client to create a `unity` catalog:
```bash
./bin/uc catalog create --name unity --comment "Main catalog"
```

* Create a `default` schema for the `unity` catalog:
```bash
./bin/uc schema create --catalog unity --name default --comment "Default schema"
```

* Create the `numbers` table:
```bash
bin/uc table create --full_name unity.default.numbers --columns "as_int int, as_double double" --storage_location "file://$HOME/some/path/unitycatalog/etc/data/external/unity/default/tables/numbers" --format DELTA --properties '{"key1": "value1", "key2": "value2"}'
```

* Create the `marksheet` table (as of end 2024, even though that table is
  supposed to be managed, the UC CLI does not seem to accept table creation
  commands without the `storage_location` parameter, that is,
  the UC CLI does not seem to accept to create managed tables:
  * The `storage_location` parameter is required for external tables,
  but should not be needed for managed tables; relevant documentation:
  https://docs.unitycatalog.io/usage/cli/#33-create-a-table):
```bash
bin/uc table create --full_name unity.default.marksheet --columns "id int, name string, marks int" --storage_location "file://$HOME/some/path/unitycatalog/etc/data/managed/unity/default/tables/marksheet" --format DELTA --properties '{"key1": "value1", "key2": "value2"}'
```

* Create the `marksheet_uniform` table:
```bash
bin/uc table create --full_name unity.default.marksheet_uniform --columns "id int, name string, marks int" --storage_location "file://$HOME/some/path/unitycatalog/etc/data/external/unity/default/tables/marksheet_uniform" --format DELTA --properties '{"key1": "value1", "key2": "value2"}'
```

* Create the `user_countries` table:
```bash
bin/uc table create --full_name unity.default.user_countries --columns "first_name string, age long, country string" --storage_location "file://$HOME/some/path/unitycatalog/etc/data/external/unity/default/tables/user_countries" --format DELTA --properties '{"key1": "value1", "key2": "value2"}'
```

* Create the `json_files` volume:
```bash
bin/uc volume create --full_name unity.default.json_files --storage_location file://$HOME/some/path/unitycatalog/etc/data/external/unity/default/volumes/json_files/ --comment "External volume"
```

* Create the `txt_files` volume:
```bash
bin/uc volume create --full_name unity.default.txt_files --storage_location file://$HOME/some/path/unitycatalog/etc/data/managed/unity/default/volumes/txt_files/ --comment "Managed volume"
```

## Spark
* Relevant documentation:
  https://docs.unitycatalog.io/integrations/unity-catalog-spark/

* For consistency reason, it is better, for the Unity Catalog connector,
  to use the JAR package generated by SBT (and published locally in the local
  Ivy2/Maven cache)
  * Check that the Unity Catalog Spark connector JAR package is
  in the local Ivy2/Maven cache:
```bash
ls -lFh ~/.ivy2/jars/io.unitycatalog*
```

* Launch PySpark:
```bash
pyspark --name "local-uc-test" \
  --master "local[*]" \
  --packages "io.delta:delta-spark_2.12:3.2.1,io.unitycatalog:unitycatalog-spark_2.12:${UC_VERSION}" \
  --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
  --conf "spark.sql.catalog.spark_catalog=io.unitycatalog.spark.UCSingleCatalog" \
  --conf "spark.sql.catalog.unity=io.unitycatalog.spark.UCSingleCatalog" \
  --conf "spark.sql.catalog.unity.uri=http://localhost:8080" \
  --conf "spark.sql.catalog.unity.token=" \
  --conf "spark.sql.defaultCatalog=unity"
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

## DuckDB
* Relevant documentation: https://docs.unitycatalog.io/integrations/unity-catalog-duckdb/

* See also the
  [DuckDB cheat sheet on this Git repository](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/README.md)

### MacOS
* On MacOS, DuckDB may be installed with HomeBrew:
```bash
brew install duckdb
```

### Linux
* See
  [DuckDB installation page for Linux](https://duckdb.org/docs/installation/?version=stable&environment=cli&platform=linux&download_method=direct&architecture=x86_64)

* It would give something like:
```bash
DDB_VER="$(curl -Ls https://api.github.com/repos/duckdb/duckdb/releases/latest | grep 'tag_name' | cut -d':' -f2,2 | cut -d'"' -f2,2)"
curl -L https://github.com/duckdb/duckdb/releases/download/$DDB_VER/duckdb_cli-linux-amd64.zip -o duckdb_cli-linux-amd64.zip
unzip -x duckdb_cli-linux-amd64.zip && rm -f duckdb_cli-linux-amd64.zip
mkdir -p ~/bin
mv duckdb ~/bin
chmod +x ~/bin/duckdb
export PATH="$HOME/bin:$PATH"
```

## Daft
* Install Daft, with its integration with Delta and Unity Catalog:
```bash
python -mpip install -U "getdaft[unity,deltalake]"
```

## Launch the UI with JavaScript (JS)

### Prerequisites
* NodeJS: https://nodejs.org/en/download/package-manager
* Yarn: https://classic.yarnpkg.com/lang/en/docs/install

* Start the UI through Yarn:
```bash
cd ui
yarn install
yarn start
```

