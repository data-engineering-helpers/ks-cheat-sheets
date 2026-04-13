# Cheat Sheet - Apache Spark

## Table of Content (ToC)

* [Cheat Sheet \- Apache Spark](#cheat-sheet---apache-spark)
  * [Table of Content (ToC)](#table-of-content-toc)
  * [Overview](#overview)
    * [Spark and related components](#spark-and-related-components)
    * [Sub\-directories for this Spark cheat sheet](#sub-directories-for-this-spark-cheat-sheet)
    * [Spark ecosystem architectural shift towards native engines](#spark-ecosystem-architectural-shift-towards-native-engines)
  * [References](#references)
    * [Data Engineering helpers](#data-engineering-helpers)
    * [Unity Catalog (UC)](#unity-catalog-uc)
    * [Apache Spark](#apache-spark)
      * [Spark Connect](#spark-connect)
      * [Delta Lake](#delta-lake)
      * [Spark Declarative Pipelines (SDP)](#spark-declarative-pipelines-sdp)
  * [Setup](#setup)
    * [Setup of Java](#setup-of-java)
    * [Clone this repository](#clone-this-repository)
    * [Setup of Delta Lake](#setup-of-delta-lake)
    * [Setup of Spark Connect](#setup-of-spark-connect)
    * [Setup of Spark Declarative Pipelines (SDP)](#setup-of-spark-declarative-pipelines-sdp)
    * [Setup of Unity Catalog (UC)](#setup-of-unity-catalog-uc)
    * [Setup of Spark](#setup-of-spark)
      * [PostgreSQL JDBC connector](#postgresql-jdbc-connector)
    * [Shell environment and aliases](#shell-environment-and-aliases)
  * [Install native Spark manually](#install-native-spark-manually)
    * [All\-in\-one Spark engine](#all-in-one-spark-engine)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

## Overview

[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/README.md)
explains how to install and to use
[Apache Spark](https://spark.apache.org), _e.g._,
on a laptop or on a virtual machine (VM).

Apache Spark is a multi-language engine for executing data engineering, data
science, and machine learning (ML) on single-node machines or clusters.

### Spark and related components

* The Spark ecosystem is rich. The following cheat sheets are detailing specific
  Spark-related features/components

* [Unity Catalog (UC)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/unity-catalog/)
  * UC is a governance platform and data catalog allowing any data-related
  tools to access datasets through the names the corresponding schema and
  table
  * UC has no dependency on Spark (it does not need Spark to run), but
  it integrates well, by design, with Spark and all its components
  * The
  [Unity Catalog blog post](https://www.unitycatalog.io/blogs/unity-catalog-spark-delta-lake)
  details how Unity Catalog (UC) works with Apache Spark ad Delta Lake
  * UC also integrates with a wide range of
  [data-related tools/engines](https://github.com/unitycatalog/unitycatalog?tab=readme-ov-file#vibrant-ecosystem)
  (_e.g._, [DuckDB](https://duckdb.org/docs/stable/core_extensions/delta))

* [Spark Connect (SC)](spark-connect/)
  * Spark Connect introduced a decoupled client-server architecture for Spark
  that allows remote connectivity to Spark clusters using the
  [DataFrame API](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.html?highlight=dataframe#pyspark.sql.DataFrame)
  * The separation between client and server allows Spark and its open
  ecosystem to be leveraged from everywhere. It can be embedded in modern data
  applications, in IDEs, notebooks and programming languages

* [Delta Lake](delta/)
  * Delta Lake is a storage framework that enables building a
  [Lakehouse architecture](https://www.databricks.com/blog/2020/01/30/what-is-a-data-lakehouse.html)
  with compute engines including Spark, DuckDB, PrestoDB, Flink, Trino, and
  Hive and APIs for Scala, Java, Rust, Ruby, and Python
  * [Delta Connect, the Delta Lake version of Spark Connect](https://docs.delta.io/delta-spark-connect/)

* [Spark Declarative Pipelines (SDP)](declarative-pipelines/)
  * Spark Declarative Pipelines (SDP) is a declarative framework for building
  reliable, maintainable, and testable data pipelines on Spark. SDP simplifies
  ETL development by allowing you to focus on the transformations you want
  to apply to your data, rather than the mechanics of pipeline execution
  * The key advantage of SDP is its declarative approach - you define what
  tables should exist and what their contents should be, and SDP handles the
  orchestration, compute management, and error handling automatically

* Even though some of these components fully work without Spark (_e.g._, Unity
  Catalog and Delta Lake may be interacted with DuckDB only, among others),
  they are, by design, fully compatible with Spark

### Sub-directories for this Spark cheat sheet

* In addition to the above-mentionned Spark-related components:
  * [Spark Connect (SC)](spark-connect/)
  * [Delta Lake](delta/)
  * [Spark Declarative Pipelines (SDP)](declarative-pipelines/)

* A few end-to-end Spark-related tutorials, with full code source,
  are featured in the
  [examples/ directory](examples/)

### Spark ecosystem architectural shift towards native engines

* [LinkedIn post - Spark ecosystem architectural shift](https://www.linkedin.com/posts/lakehouse_the-spark-ecosystem-is-quietly-undergoing-activity-7444376892960399360-_IEn/)
  * Date: Apr. 2026
  * Author: [Kyle Weller](https://www.linkedin.com/in/lakehouse/)

> The Spark ecosystem is quietly undergoing a deep architectural shift from
> JVM-bound execution toward heterogeneous, vectorized, native backends.
> What used to be a monolithic execution engine is now a pluggable compute
> substrate.
>
> At a high level, Spark is evolving into a query planner plus orchestration
> layer, delegating execution to specialized engines:
>
> * Photon (Databricks) → tightly integrated C++ vectorized engine optimized for
>   whole-stage codegen replacement
> * Quanton (Onehouse) → native execution layer pushing Hudi and Iceberg native
>   and lakehouse optimizations closer to storage
> * RAPIDS (NVIDIA) → GPU-accelerated columnar execution via cuDF, translating
>   Spark plans into GPU kernels
> * Gluten (Intel + ecosystem) → Velox backend bridge, decoupling Spark from
>   JVM execution
> * Velox (Meta) → reusable vectorized execution engine underpinning multiple
>   systems (Presto, Spark via Gluten)
> * DataFusion Comet (InfluxData) → Rust-native execution aligned with Arrow
>   memory model
> * Plus many more

## References

### Data Engineering helpers

* [Data Engineering Helpers - Knowledge Sharing - Python](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/python/)
  * [Data Engineering Helpers - Knowledge Sharing - Jupyter, PySpark and DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/jupyter/jupyter-pyspark-duckdb/)
* [Data Engineering Helpers - Knowledge Sharing - SQLMesh](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/)
* [Data Engineering Helpers - Knowledge Sharing - DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/)
* [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/)
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box)

### Unity Catalog (UC)

* [Data Engineering Helpers - Knowledge Sharing - Unity Catalog](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/unity-catalog/)

### Apache Spark

* [Apache Spark - Download Spark](https://spark.apache.org/docs/latest/api/python/getting_started/install.html)
  * The easiest way to install is through Pypi with something like
  `pip install pyspark`
* [Apache Spark - Doc - Getting started / Installation](https://spark.apache.org/docs/latest/api/python/getting_started/install.html)
* [GitHub - Palantir - PySpark style guide](https://github.com/palantir/pyspark-style-guide)

#### Spark Connect

* [Data Engineering Helpers - Knowledge Sharing - Spark Connect](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/spark-connect/)

#### Delta Lake

* [Data Engineering Helpers - Knowledge Sharing - Delta Lake](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/delta/)

#### Spark Declarative Pipelines (SDP)

* [Data Engineering Helpers - Knowledge Sharing - Spark Declarative Pipelines (SDP)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/declarative-pipelines/)

## Setup

### Setup of Java

* If not already done so, install Java 21
  * [Spark 4.1.0 appears to be compatible with Java versions from 17 up to 21 included](https://spark.apache.org/docs/4.1.0-preview4/#downloading)
  * SDKMan is recommended to manage the versions of Java-based
    tools. For instance, with the Corretto JDKs:

```bash
sdk install java 21.0.9-amzn
sdk default java 21.0.9-amzn
```

* Check the version of Java:

```bash
java -version
openjdk version "21.0.9" 2025-10-21 LTS
OpenJDK Runtime Environment Corretto-21.0.9.10.1 (build 21.0.9+10-LTS)
OpenJDK 64-Bit Server VM Corretto-21.0.9.10.1 (build 21.0.9+10-LTS, mixed mode,
 sharing)
```

### Clone this repository

* Clone this
  [Git repository](https://github.com/data-engineering-helpers/ks-cheat-sheets)
  and move into its Spark-related directory:

```bash
mkdir -p ~/dev/knowledge-sharing
git clone https://github.com/data-engineering-helpers/ks-cheat-sheets ~/dev/knowledge-sharing/ks-cheat-sheets
cd ~/dev/knowledge-sharing/ks-cheat-sheets/data-processing/spark
```

### Setup of Delta Lake

* See the
  [setup section of the Delta Lake cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/delta/README.md#setup)
  (in this same Git repository) for installation instructions about Delta Lake

### Setup of Spark Connect

* See the
  [setup section of the Spark Connect cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/spark-connect/README.md#setup)
  (in this same Git repository) for installation instructions about Spark Connect

### Setup of Spark Declarative Pipelines (SDP)

* See the
  [setup section of the Spark Declarative Pipelines (SDP) cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/declarative-pipelines/README.md#setup)
  (in this same Git repository) for installation instructions about Spark Declarative
  Pipelines (SDP)

### Setup of Unity Catalog (UC)

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

### Setup of Spark

#### PostgreSQL JDBC connector

* See
  [Data Engineering Helpers - Knowledge Sharing - PostgreSQL - JDBC connector sub-section](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md#postgresql-jdbc-connector)

* Example on how to launch a Spark REPL
  * Spark Shell (in Scala):

```bash
spark-shell \
  --driver-class-path postgresql-42.7.8.jar --jars postgresql-42.7.8.jar
```

```scala
scala> :quit
```

* PySpark (in Python):

```bash
pyspark \
  --driver-class-path postgresql-42.7.8.jar --jars postgresql-42.7.8.jar
```

```python
>>> quit()
```

### Shell environment and aliases

* Add the following in the Bash/Zsh init script:

```bash
$ cat >> ~/.bashrc << _EOF

# Spark
PY_LIBDIR="$(python -mpip show pyspark|grep "^Location:"|cut -d' ' -f2,2)"
export SPARK_VERSION="\$(python -mpip show pyspark|grep "^Version:"|cut -d' ' -f2,2)"
export SPARK_HOME="\$PY_LIBDIR/pyspark"
export PATH="\$SPARK_HOME/sbin:\$PATH"
export PYSPARK_PYTHON="\$(which python3)"
export PYSPARK_DRIVER_PYTHON="\$(which python3)"

# Delta Lake
DL_VERSION="\$(python -mpip show delta-spark | grep "^Version" | cut -d" " -f2,2)"

# Unity Catalog
UC_JAR="\$(ls ~/.ivy2/cache/io.unitycatalog/unitycatalog-spark_2.12/jars/*.jar \
 | xargs basename | sort -r | head -1)"
UC_VERSION="\$(basename "\$(echo ${UC_JAR} | cut -d"-" -f3-)" .jar)"

_EOF
```

* Re-read the Shell init scripts
  * Bash:

```bash
exec bash
```

* Zsh:

```bash
exec zsh
```

## Install native Spark manually

* That section is kept for reference only. It is normally not needed

* Install Spark/PySpark manually, _e.g._ with Spark 4.1.1:

```bash
export SPARK_VERSION="4.1.1"
  wget https://dlcdn.apache.org/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop3.tgz
  tar zxf spark-$SPARK_VERSION-bin-hadoop3.tgz && \
  mv spark-$SPARK_VERSION-bin-hadoop3 ~/ && \
  rm -f spark-$SPARK_VERSION-bin-hadoop3.tgz
```

* Add the following in the Bash/Zsh init script:

```bash
$ cat >> ~/.bashrc << _EOF

# Spark
export SPARK_VERSION="${SPARK_VERSION}"
export SPARK_HOME="\$HOME/spark-\$SPARK_VERSION-bin-hadoop3"
export PATH="\$SPARK_HOME/bin:\$SPARK_HOME/sbin:\${PATH}"
export PYTHONPATH=\$(ZIPS=("\$SPARK_HOME"/python/lib/*.zip); IFS=:; echo "\${ZIPS[*]}"):\$PYTHONPATH
export PYSPARK_PYTHON="\$(which python3)"
export PYSPARK_DRIVER_PYTHON="$(which python3)"

_EOF
exec bash
```

* See the
  ['Shell environment and aliases' section of the Spark Connect cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/spark-connect/README.md#shell-environment-and-aliases)
  (in this same Git repository) for additional Shell aliases related to
  Spark Connect

### All-in-one Spark engine

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
SCALA_MINOR=2.13
DL_VERSION=4.0.1
DL_JAR=delta-spark_$SCALA_MINOR
UC_VERSION=0.3.0-SNAPSHOT
UC_DOM=io.unitycatalog
UC_JAR=unitycatalog-spark_$SCALA_MINOR
pyspark --name "local-uc" --master "local[*]" \
  --packages \
  "io.delta:$DL_JAR:$DL_VERSION,$UC_DOM:$UC_JAR:$UC_VERSION" \
  --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
  --conf "spark.sql.catalog.spark_catalog=$UC_DOM.spark.UCSingleCatalog" \
  --conf "spark.sql.catalog.unity=$UC_DOM.spark.UCSingleCatalog" \
  --conf "spark.sql.catalog.unity.uri=http://localhost:8080" \
  --conf "spark.sql.catalog.unity.token=" \
  --conf "spark.sql.defaultCatalog=unity"
```

* Only with support for Delta:

```bash
pyspark --name "local" --master "local[*]" \
  --packages "io.delta:delta-spark_2.13:${DL_VERSION}" \
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
