Cheat Sheet - Apache Spark Connect
==================================

# Table of Content (ToC)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/spark-connect/README.md)
explains how (potentially to install and) to use
[Spark Connect](https://github.com/delta-io/delta), _e.g._,
on a laptop or on a virtual machine (VM).

# References

## Data Engineering helpers
* [Data Engineering Helpers - Knowledge Sharing - Spark](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/)
* [Data Engineering Helpers - Knowledge Sharing - Delta Lake](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/delta/)
* [Data Engineering Helpers - Knowledge Sharing - Spark Declarative Pipelines (SDP)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/spd/)
* [Data Engineering Helpers - Knowledge Sharing - Unity Catalog (UC)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/unity-catalog/)
* [Data Engineering Helpers - Knowledge Sharing - Python](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/python/)
  * [Data Engineering Helpers - Knowledge Sharing - Jupyter, PySpark and DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/jupyter/jupyter-pyspark-duckdb/)
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box)

## Delta Lake
* [Data Engineering Helpers - Knowledge Sharing - Delta Lake](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/delta/)
* [Delta Lake doc - Delta Connect](https://docs.delta.io/delta-spark-connect/)

### Spark Connect
* [Apache Spark - Doc - Spark Connect - Overview](https://spark.apache.org/docs/latest/spark-connect-overview.html)
* [Apache Spark - Doc - Spark Connect - Quick start](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_connect.html)

## Java
* Java releases: https://www.java.com/releases/
* From Sep. 2025, the new LTS has been the 25 release
* The next LTS version should be the 27 release, expected to be available from
  Sep. 2027

## Spark 4.1
* As of beginning 2026, per
  [Delta Lake release compatibility matrix](https://docs.delta.io/releases/)
  and [Delta Lake releases](https://github.com/delta-io/delta/releases),
  there does not seem to be a version of Delta Lake compatible with
  the yet to be released Spark 4.1 versions
* For this cheat sheet, the following two alternatives have been tried, without
  success so far:
  * Installing and using the latest Delta Lake version out of the box, that is,
  [4.0.1](https://github.com/delta-io/delta/releases/tag/v4.0.1):
```bash
$ python -mpip install delta-spark==4.0.1
$ pyspark --packages io.delta:delta-spark_2.13:4.0.1 --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"
```
  * Building Delta Lake from the sources, as detailed in the sub-section below,
  installing and using it:
```bash
$ pyspark --packages io.delta:delta-spark_2.13:4.0.1-SNAPSHOT --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"
```
* When testing simple Delta examples, the following error appears:
```python
>>> data = spark.range(0, 5)
>>> data.write.format("delta").save("data-delta-test")
py4j.protocol.Py4JJavaError: An error occurred while calling o61.save.
: com.google.common.util.concurrent.ExecutionError: java.lang.NoSuchMethodError: 'void org.apache.spark.internal.LogKey.$init$(org.apache.spark.internal.LogKey)'
```

# Setup
* See the
  [setup section of the Spark cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/README.md#setup)
  (in this same Git repository) for installation instructions about Java and Spark

## Spark Connect
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
  (_e.g._, PySpark `4.0.x` is compatible with Delta Lake `4.0.x`)
    * Spark releases: https://spark.apache.org/releases/
	* Delta Lake releases: https://github.com/delta-io/delta/releases/

* Install PySpark, with the Spark Connect extension, from PyPi:
```bash
python -mpip install "pyspark[connect,sql,pandas_on_spark]==4.1.1"
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

## Shell environment and aliases
* Add the following Shell aliases to start and stop Spark, Spark Connect server
  and JupyterLab:
```bash
$ cat >> ~/.bash_aliases << _EOF

# Spark Connect
alias sparkconnectset='export SPARK_REMOTE="sc://localhost:15002"'
alias sparkconnectunset='unset SPARK_REMOTE'

## Spark Connect alone
alias sparkconnectstart='start-connect-server.sh'

## Spark Connect with Delta Lake
alias sparkconnectstartwdelta='sparkconnectunset; start-connect-server.sh --packages io.delta:delta-spark_2.13:\$DL_VERSION --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"'

## Spark Connect with Unity Catalog and Delta Lake
alias sparkconnectstartwucdelta='sparkconnectunset; start-connect-server.sh --packages io.delta:delta-spark_2.13:\$DL_VERSION,io.unitycatalog:unitycatalog-spark_2.13:\$UC_VERSION,org.postgresql:postgresql:9.4.1212 --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" --conf "spark.sql.catalog.spark_catalog=io.unitycatalog.spark.UCSingleCatalog" --conf "spark.sql.catalog.unity=io.unitycatalog.spark.UCSingleCatalog" --conf "spark.sql.catalog.unity.uri=http://localhost:8080" --conf "spark.sql.catalog.unity.token=" --conf "spark.sql.defaultCatalog=unity"'

## Stop Spark Connect
alias sparkconnectstop='stop-connect-server.sh'

# PySpark and/or PySpark kernel within JupyterLab
## PySpark with Delta Lake
alias pysparkdelta='pyspark io.delta:delta-spark_2.13:\$DL_VERSION --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"'

## PySpark with Unity Catalog and Delta Lake
alias pysparkucdelta='pyspark --packages org.apache.spark:spark-connect_2.13:\$SPARK_VERSION,io.delta:delta-spark_2.13:\$DL_VERSION,io.unitycatalog:unitycatalog-spark_2.13:\$UC_VERSION,org.postgresql:postgresql:9.4.1212 --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" --conf "spark.sql.catalog.spark_catalog=io.unitycatalog.spark.UCSingleCatalog" --conf "spark.sql.catalog.unity=io.unitycatalog.spark.UCSingleCatalog" --conf "spark.sql.catalog.unity.uri=http://localhost:8080" --conf "spark.sql.catalog.unity.token=" --conf "spark.sql.defaultCatalog=unity"'
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


