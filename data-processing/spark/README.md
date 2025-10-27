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
    * [PostgreSQL JDBC connector](#postgresql-jdbc-connector)
    * [Spark Connect](#spark-connect-1)
  * [Shell environment and aliases](#shell-environment-and-aliases)
  * [Install native Spark manually](#install-native-spark-manually)
    * [All\-in\-one Spark engine](#all-in-one-spark-engine)

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
* [Data Engineering Helpers - Knowledge Sharing - Python](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/python/)
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

* As per the official
  [Apache Spark documentation](https://spark.apache.org/docs/latest/api/python/getting_started/install.html),
  PyPi-installed PySpark (`pip install pyspark[connect]`) comes with
  Spark Connect from Spark version 3.4 or later.
  * However, as of Spark version up to 3.4.1, the PySpark installation
  lacks the two new administration scripts allowing to start and
  to stop the Spark Connect server.
  * For convenience, these two scripts have therefore been copied into this
  Git repository, in the
  [`tools/` directory](https://github.com/data-engineering-helpers/ks-cheat-sheets/tree/main/tools).
  They may then be simply copied in the PySpark `sbin` directory,
  once PySpark has been installed with `pip`
  * The Delta Lake version has to be compatible with Spark. See
  https://docs.delta.io/latest/releases.html for the compatibility table
  (_e.g._, PySpark `3.5.x` is compatible with Delta Lake `3.3.x`)
    * Spark releases: https://spark.apache.org/releases/
	* Delta Lake releases: https://github.com/delta-io/delta/releases/

* Install PySpark, with the Spark Connect extension, from PyPi:
```bash
python -mpip install "pyspark[connect,sql,pandas_on_spark]==3.5.4"
```

* Install Delta Lake:
```bash
python -mpip install delta-lake==3.3.0
```

### PostgreSQL JDBC connector
* See
  [Data Engineering Helpers - Knowledge Sharing - PostgreSQL - JDBC connector sub-section](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md#postgresql-jdbc-connector)

* Note that, as of end 2025, at least on MacOS, Java still needs to be in version 8
  * For instance, install the Corretto JDK8 with SDKMan:
```bash
$ sdk install java 8.0.472-amzn
$ sdk default java 8.0.472-amzn
$ java -version
openjdk version "1.8.0_472"
OpenJDK Runtime Environment Corretto-8.472.08.1 (build 1.8.0_472-b08)
OpenJDK 64-Bit Server VM Corretto-8.472.08.1 (build 25.472-b08, mixed mode)
```

* Example on how to launch a Spark REPL
  * Spark Shell (in Scala):
```bash
$ spark-shell --driver-class-path postgresql-42.7.8.jar --jars postgresql-42.7.8.jar
```
```scala
scala> :quit
```
  * PySpark (in Python):
```bash
$ pyspark --driver-class-path postgresql-42.7.8.jar --jars postgresql-42.7.8.jar
```
```python
>>> quit()
```

### Spark Connect
* Launch the Spark Connect cluster from a dedicated terminal window/tab
  (Control-C to terminate it)
* Note that the `SPARK_REMOTE` environment variable should not be set at this
  stage, otherwise the Spark Connect server will try to connect to itself
  (catch 22) and will therefore not start
  * The
  [Shell aliases given in this cheat sheet](#shell-environment-and-aliases)
  first unset that environment variable before launching the Spark Connect
  server (if you use those aliases, all is good)
```bash
sparkconnectstart
```

## Shell environment and aliases
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
UC_JAR="\$(ls ~/.ivy2/cache/io.unitycatalog/unitycatalog-spark_2.12/jars/*.jar | xargs basename | sort -r | head -1)"
UC_VERSION="\$(basename "\$(echo ${UC_JAR} | cut -d"-" -f3-)" .jar)"

_EOF
```

* Re-read the Shell init scripts
  * Bash:
```
$ exec bash
```
  * Zsh:
```
$ exec zsh
```

* Copy the two Spark connect administrative scripts into the PySpark
  installation:
```bash
$ cp tools/st*-connect*.sh $SPARK_HOME/sbin/
```

* Check that the scripts are installed correctly:
```bash
$ ls -lFh $SPARK_HOME/sbin/*connect*.sh
-rwxr-xr-x  1 user staff 1.5K Jun 28 16:54 $PY_LIBDIR/pyspark/sbin/start-connect-server.sh*
-rwxr-xr-x  1 user staff 1.0K Jun 28 16:54 $PY_LIBDIR/pyspark/sbin/stop-connect-server.sh*
```

* Add the following Shell aliases to start and stop Spark, Spark Connect server
  and JupyterLab:
```bash
$ cat >> ~/.bash_aliases << _EOF

# Spark Connect
alias sparkconnectset='export SPARK_REMOTE="sc://localhost:15002"'
alias sparkconnectunset='unset SPARK_REMOTE'
alias sparkconnectstart='sparkconnectunset; start-connect-server.sh --packages org.apache.spark:spark-connect_2.12:\$SPARK_VERSION,io.delta:delta-spark_2.12:\$DL_VERSION,io.unitycatalog:unitycatalog-spark_2.12:\$UC_VERSION,org.postgresql:postgresql:9.4.1212 --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" --conf "spark.sql.catalog.spark_catalog=io.unitycatalog.spark.UCSingleCatalog" --conf "spark.sql.catalog.unity=io.unitycatalog.spark.UCSingleCatalog" --conf "spark.sql.catalog.unity.uri=http://localhost:8080" --conf "spark.sql.catalog.unity.token=" --conf "spark.sql.defaultCatalog=unity"'
alias sparkconnectstop='stop-connect-server.sh'

# PySpark and/or PySpark kernel within JupyterLab
alias pysparkdelta='pyspark --packages org.apache.spark:spark-connect_2.12:\$SPARK_VERSION,io.delta:delta-spark_2.12:\$DL_VERSION,io.unitycatalog:unitycatalog-spark_2.12:\$UC_VERSION,org.postgresql:postgresql:9.4.1212 --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" --conf "spark.sql.catalog.spark_catalog=io.unitycatalog.spark.UCSingleCatalog" --conf "spark.sql.catalog.unity=io.unitycatalog.spark.UCSingleCatalog" --conf "spark.sql.catalog.unity.uri=http://localhost:8080" --conf "spark.sql.catalog.unity.token=" --conf "spark.sql.defaultCatalog=unity"'
alias pysparkdeltawconnect='sparkconnectset; pysparkdelta'
alias pysparkdeltawoconnect='sparkconnectunset; pysparkdelta'

_EOF
```

* Re-read the Shell aliases:
```bash
. ~/.bash_aliases
```

## Install native Spark manually
* That section is kept for reference only. It is normally not needed

* Install Spark/PySpark manually, _e.g._ with Spark 3.5.4:
```bash
$ export SPARK_VERSION="3.5.4"
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

* Add the following Shell aliases to start and stop Spark Connect server:
```bash
$ cat >> ~/.bash_aliases << _EOF

# Spark Connect
alias sparkconnectstart='start-connect-server.sh --packages org.apache.spark:spark-connect_2.12:${SPARK_VERSION}'
alias sparkconnectstop='stop-connect-server.sh'

_EOF
. ~/.bash_aliases
```

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
DL_VERSION=3.3.0
UC_VERSION=0.3.0-SNAPSHOT
pyspark --name "local-uc" --master "local[*]" \
  --packages "io.delta:delta-spark_2.12:${DL_VERSION},io.unitycatalog:unitycatalog-spark_2.12:${UC_VERSION}" \
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
  --packages "io.delta:delta-spark_2.12:${DL_VERSION}" \
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

