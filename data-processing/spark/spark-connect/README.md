# Cheat Sheet - Apache Spark Connect

## Table of Content (ToC)

* [Cheat Sheet \- Apache Spark Connect](#cheat-sheet---apache-spark-connect)
  * [Table of Content (ToC)](#table-of-content-toc)
  * [Overview](#overview)
  * [References](#references)
    * [Data Engineering helpers](#data-engineering-helpers)
    * [Unity Catalog (UC)](#unity-catalog-uc)
    * [Delta Lake](#delta-lake)
    * [Spark Connect](#spark-connect)
  * [Getting started](#getting-started)
    * [Spark as a client to Spark Connect](#spark-as-a-client-to-spark-connect)
  * [Setup](#setup)
    * [Setup of Spark Connect](#setup-of-spark-connect)
    * [Manual install of Apache Spark](#manual-install-of-apache-spark)
    * [Shell environment and aliases](#shell-environment-and-aliases)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

## Overview

[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/spark-connect/README.md)
explains how (potentially to install and) to use
[Spark Connect](https://github.com/delta-io/delta), _e.g._,
on a laptop or on a virtual machine (VM).

## References

### Data Engineering helpers

* [Data Engineering Helpers - Knowledge Sharing - Java](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/java-world/)
* [Data Engineering Helpers - Knowledge Sharing - Python](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/python/)
* [Data Engineering Helpers - Knowledge Sharing - Spark](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/)
* [Data Engineering Helpers - Knowledge Sharing - Delta Lake](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/delta/)
* [Data Engineering Helpers - Knowledge Sharing - Spark Declarative Pipelines (SDP)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/spd/)
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box)

### Unity Catalog (UC)

* [Data Engineering Helpers - Knowledge Sharing - Unity Catalog (UC)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/unity-catalog/)

* Note that, as of March 2026
  * The OSS version of Unity Catalog does not allow to create managed tables on
  the sample catalog and schema (the ones provided by default, coming with the
  OSS version of Unity Catalog), as those latter have not specified any default
  storage location
    * Trying to create a manage table on those catalog and schema typically
    triggers an error stating that a storage location has not been specified
  * That is why, in
  [Data Engineering Helpers - Knowledge Sharing - Unity Catalog (UC)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/unity-catalog/),
  it is documented how to create another catalog, namely `unityxt` (`xt` standing
  for extended), and associated default schema, this time with a proper default
  storage location specified

### Delta Lake

* [Data Engineering Helpers - Knowledge Sharing - Delta Lake](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/delta/)
* [Delta Lake doc - Delta Connect](https://docs.delta.io/delta-spark-connect/)

### Spark Connect

* [Apache Spark - Doc - Spark Connect - Overview](https://spark.apache.org/docs/latest/spark-connect-overview.html)
* [Apache Spark - Doc - Spark Connect - Quick start](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_connect.html)

## Getting started

### Spark as a client to Spark Connect

* See also
  [Spark doc - Quickstart: Spark Connect](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_connect.html)

* The good thing is that there is no need for any dependency (_e.g._, Unity Catalog,
  Delta Lake), as the Spark driver is running in the server part of Spark Connect
  
* The only (small) issues are:
  * Spark Connect yields a lot of logs, making it hard to spot the client part
  * The Spark session object (`SparkSession`) is no longer instantiated by default.
  It has to be started explicitly, for instance with something like:

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.remote("sc://localhost:15002").getOrCreate()
```

* Typical sequence for PySpark on the client side
  * Launch PySpark:

```bash
pyspark
```

* In PySpark, retrieve the Spark session:

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.remote("sc://localhost:15002").getOrCreate()
```

* Specify the catalog and schema (from Unity Catalog) to use:

```python
spark.sql("use unity.default;")
```

* List the tables for the default (Unity) schema:

```python
spark.sql("show tables in unity.default;").show()
```

* Browse the content of a table:

```python
spark.sql("select * from default.numbers;").show()
```

* Create a DataFrame and create a temporary view out of it (allowing to get
  access to that temporary view from within a SQL query):

```python
df = spark.createDataFrame(
  [(1, "socks"), (2, "chips"), (3, "air conditioner"), (4, "tea"),],
  ["transaction_id", "item_name"]
)
df.createTempView("tiny_df")
```

* Note that this example expects a `transactions` table to have been created
  in Unity Catalog
  * See the
  [_Create managed tables with Spark_ section of Data Engineering Helpers - Unity Catalog (UC)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/unity-catalog/README.md#create-managed-tables-with-spark)

* Insert the content of the DataFrame into the corresponding table:

```python
spark.sql("insert overwrite default.transactions select * from tiny_df;")
```

* Check that the table has been filled correctly:

```python
spark.sql("select * from default.transactions;").show()
```

* On the Unity Catalog server side, the table may be browsed thanks to something
  like:

```bash
bin/uc table get --full_name unityxt.default.transactions
bin/uc table read --full_name unityxt.default.transactions
```

## Setup

* See the
  [setup section of the Spark cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/README.md#setup)
  (in this same Git repository) for installation instructions about Java and Spark

### Setup of Spark Connect

* As per the official
  [Apache Spark documentation](https://spark.apache.org/docs/latest/api/python/getting_started/install.html),
  PyPi-installed PySpark (`pip install pyspark[connect]`) comes with
  Spark Connect from Spark version 3.4 or later

* However, as of Spark version at least up to 4.1.1, the PySpark installation
  lacks the two administration scripts allowing to start and to stop
  the Spark Connect server
  * For convenience, these two scripts have therefore been copied into this
  Git repository, in the Spark cheat sheet top directory, that is, in the
  [`data-processing/spark/tools/` directory](https://github.com/data-engineering-helpers/ks-cheat-sheets/tree/main/data-processing/spark/tools/)
  They may then be simply copied in the PySpark `sbin` directory,
  once PySpark has been installed with `pip`
  * The Delta Lake version has to be compatible with Spark. See
  [Delta Lake releases](https://docs.delta.io/latest/releases.html)
  for the compatibility table
  (_e.g._, PySpark `4.1.x` is compatible with Delta Lake `4.1.x`)
    * [Spark releases](https://spark.apache.org/releases/)
    * [Delta Lake releases](https://github.com/delta-io/delta/releases/)

* Install PySpark, with the Spark Connect extension, from PyPi:

```bash
python -mpip install "pyspark[connect,sql,pandas_on_spark]==4.1.1"
```

* Copy the two Spark connect administrative scripts into the PySpark
  installation:

```bash
cp tools/st*-connect*.sh $SPARK_HOME/sbin/
```

* Check that the scripts are installed correctly:

```bash
ls -lFh $SPARK_HOME/sbin/*connect*.sh
-rwxr-xr-x  1 user staff 1.5K Jun 28 16:54 $PY_LIBDIR/pyspark/sbin/start-connect-server.sh*
-rwxr-xr-x  1 user staff 1.0K Jun 28 16:54 $PY_LIBDIR/pyspark/sbin/stop-connect-server.sh*
```

### Manual install of Apache Spark

* Download and install the Connect-enabled Spark tar-ball (the
  [Spark 4.1.1 download page will list the best mirror sites for you](https://www.apache.org/dyn/closer.lua/spark/spark-4.1.1/spark-4.1.1-bin-hadoop3-connect.tgz)

```bash
SPARK_VERSION=4.1.1
MIRROR_URL=https://dlcdn.apache.org/spark
curl -k \
  $MIRROR_URL/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop3-connect.tgz \
  -o spark-$SPARK_VERSION-bin-hadoop3-connect.tgz
```

### Shell environment and aliases

* Add the following Shell aliases to start and stop Spark, Spark Connect server
  and JupyterLab
  * Note that the Shell aliases are compatible with having an additional `unityxt`
  (`xt` standing for extended) catalog, but do not require it. In other words, even
  if such a catlog does not exist, the alias will still work

```bash
cat >> ~/.bash_aliases << _EOF

# Spark Connect
alias sparkconnectset='export SPARK_REMOTE="sc://localhost:15002"'
alias sparkconnectunset='unset SPARK_REMOTE'

## Spark Connect alone
alias sparkconnectstart='start-connect-server.sh'

## Spark Connect with Delta Lake
alias sparkconnectstartwdelta='sparkconnectunset; start-connect-server.sh \
  --packages io.delta:delta-spark_2.13:\$DL_VERSION \
  --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
  --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"'

## Spark Connect with Unity Catalog and Delta Lake
alias sparkconnectstartwucdelta='sparkconnectunset; start-connect-server.sh \
  --packages io.delta:delta-spark_2.13:\$DL_VERSION,io.unitycatalog:unitycatalog-spark_2.13:\$UC_VERSION,org.postgresql:postgresql:9.4.1212 \
  --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
  --conf "spark.sql.catalog.spark_catalog=io.unitycatalog.spark.UCSingleCatalog" \
  --conf "spark.sql.catalog.unity=io.unitycatalog.spark.UCSingleCatalog" \
  --conf "spark.sql.catalog.unity.uri=http://localhost:8080" \
  --conf "spark.sql.catalog.unity.token=" \
  --conf "spark.sql.defaultCatalog=unity" \
  --conf "spark.sql.catalog.unityxt=io.unitycatalog.spark.UCSingleCatalog" \
  --conf "spark.sql.catalog.unityxt.uri=http://localhost:8080" \
  --conf "spark.sql.catalog.unityxt.token=" \
  --conf "spark.sql.defaultCatalog=unityxt"'

## Stop Spark Connect
alias sparkconnectstop='stop-connect-server.sh'

# PySpark and/or PySpark kernel within JupyterLab
## PySpark with Delta Lake
alias pysparkdelta='pyspark io.delta:delta-spark_2.13:\$DL_VERSION \
  --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
  --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"'

## PySpark with Unity Catalog and Delta Lake
alias pysparkucdelta='pyspark --packages org.apache.spark:spark-connect_2.13:\$SPARK_VERSION,io.delta:delta-spark_2.13:\$DL_VERSION,io.unitycatalog:unitycatalog-spark_2.13:\$UC_VERSION,org.postgresql:postgresql:9.4.1212 \
  --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
  --conf "spark.sql.catalog.spark_catalog=io.unitycatalog.spark.UCSingleCatalog" \
  --conf "spark.sql.catalog.unity=io.unitycatalog.spark.UCSingleCatalog" \
  --conf "spark.sql.catalog.unity.uri=http://localhost:8080" \
  --conf "spark.sql.catalog.unity.token=" \
  --conf "spark.sql.defaultCatalog=unity" \
  --conf "spark.sql.catalog.unityxt=io.unitycatalog.spark.UCSingleCatalog" \
  --conf "spark.sql.catalog.unityxt.uri=http://localhost:8080" \
  --conf "spark.sql.catalog.unityxt.token=" \
  --conf "spark.sql.defaultCatalog=unityxt"'
alias pysparkdeltawconnect='sparkconnectset; pysparkdelta'
alias pysparkdeltawoconnect='sparkconnectunset; pysparkdelta'

_EOF
```

* Re-read the Shell aliases:

```bash
. ~/.bash_aliases
```

* Launch the Spark Connect server from a dedicated terminal window/tab
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
