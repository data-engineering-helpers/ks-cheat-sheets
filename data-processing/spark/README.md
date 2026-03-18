# Cheat Sheet - Apache Spark

## Table of Content (ToC)

* [Cheat Sheet \- Apache Spark](#cheat-sheet---apache-spark)
  * [Table of Content (ToC)](#table-of-content-toc)
  * [Overview](#overview)
  * [References](#references)
    * [Data Engineering helpers](#data-engineering-helpers)
    * [Apache Spark](#apache-spark)
      * [Spark Connect](#spark-connect)
      * [Delta Lake](#delta-lake)
      * [Spark Declarative Pipelines (SDP)](#spark-declarative-pipelines-sdp)
    * [Unity Catalog (UC)](#unity-catalog-uc)
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

## References

### Data Engineering helpers

* [Data Engineering Helpers - Knowledge Sharing - Python](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/python/)
  * [Data Engineering Helpers - Knowledge Sharing - Jupyter, PySpark and DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/jupyter/jupyter-pyspark-duckdb/)
* [Data Engineering Helpers - Knowledge Sharing - Delta Lake](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/delta/)
* [Data Engineering Helpers - Knowledge Sharing - Spark Connect](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/spark-connect/)
* [Data Engineering Helpers - Knowledge Sharing - Spark Declarative Pipelines](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/declarative-pipelines/)
* [Data Engineering Helpers - Knowledge Sharing - Unity Catalog (UC)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/unity-catalog/)
* [Data Engineering Helpers - Knowledge Sharing - SQLMesh](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/)
* [Data Engineering Helpers - Knowledge Sharing - DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/)
* [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/)
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box)

### Apache Spark

* [Apache Spark - Download Spark](https://spark.apache.org/docs/latest/api/python/getting_started/install.html)
  * The easiest way to install is through Pypi with something like
  `pip install pyspark`
* [Apache Spark - Doc - Getting started / Installation](https://spark.apache.org/docs/latest/api/python/getting_started/install.html)
* [GitHub - Palantir - PySpark style guide](https://github.com/palantir/pyspark-style-guide)

#### Spark Connect

* [Apache Spark - Doc - Spark Connect - Overview](https://spark.apache.org/docs/latest/spark-connect-overview.html)
* [Apache Spark - Doc - Spark Connect - Quick start](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_connect.html)

#### Delta Lake

* [Delta Lake documentation](https://docs.delta.io/)
  * [Delta Lake - Quick start guide](https://docs.delta.io/latest/quick-start.html)
* [Delta Lake - Compatibility matrix with Spark](https://docs.delta.io/releases/)
* [GitHub - Delta Lake - `delta` repository](https://github.com/delta-io/delta)
* [Maven central - Delta Spark: `io.delta/delta-spark`](https://mvnrepository.com/artifact/io.delta/delta-spark)

#### Spark Declarative Pipelines (SDP)

* A
  [specific cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/declarative-pipelines/)
  is dedicated to that feature

### Unity Catalog (UC)

* [Unity Catalog (UC) home page](https://www.unitycatalog.io)
* [GitHub - Unity Catalog repository](https://github.com/unitycatalog/unitycatalog)
* [Unity Catalog docs](https://docs.unitycatalog.io/)
  * [Unity Catalog docs - Quickstart](https://docs.unitycatalog.io/quickstart/)
  * [Unity Catalog docs - Usage - CLI](https://docs.unitycatalog.io/usage/cli/)
  * [Unity Catalog docs - Deployment - PostgreSQL connection](https://docs.unitycatalog.io/deployment/#example-postgresql-connection)
  * [Unity Catalog docs - Integrations - Spark](https://docs.unitycatalog.io/integrations/unity-catalog-spark/)
  * [Unity Catalog docs - Integrations - DataBricks](https://sqlmesh.readthedocs.io/en/stable/integrations/engines/databricks/)
  * [Unity Catalog docs - Integrations - DuckDB](https://docs.unitycatalog.io/integrations/unity-catalog-duckdb/)
  * [Unity Catalog docs - Integrations - XTable](https://docs.unitycatalog.io/integrations/unity-catalog-xtable/)
* [Unity Catalog blog post - Integrating Spark with Unity Catalog via Open APIs](https://www.unitycatalog.io/blogs/integrating-apache-spark-with-unity-catalog-assets-via-open-apis)

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
