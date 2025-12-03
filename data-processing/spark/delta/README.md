Cheat Sheet - Delta Lake
========================

# Table of Content (ToC)
* [Overview](#overview)
* [References](#references)
  * [Data Engineering helpers](#data-engineering-helpers)
  * [Delta Lake](#delta-lake)
  * [Spark 4\.1 preview](#spark-41-preview)
* [Setup](#setup)
  * [Java](#java)
  * [Delta Lake](#delta-lake-1)
  * [Build from the sources](#build-from-the-sources)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/delta/README.md)
explains how (potentially to install and) to use
[Delta Lake](https://github.com/delta-io/delta), _e.g._,
on a laptop or on a virtual machine (VM).

Note that Delta Lake needs to come with a version compatible to Spark, as per the
[Delta Lake release compatibility matrix](https://docs.delta.io/releases/).

Since Spark 4.1 is available only as a preview (as of end 2025), Delta Lake is not
easily available in a compatible version.
The [Delta Lake 4.1.0 milestone](https://github.com/delta-io/delta/milestone/31)
states that it is due for end of January 2026.

In some very specific cases (_e.g._, trying new features not yet available in the
public releases), it may be interesting to build Delta Lake from the sources. This
cheat sheet also gives details on how to do it.

# References

## Data Engineering helpers
* [Data Engineering Helpers - Knowledge Sharing - Python](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/python/)
  * [Data Engineering Helpers - Knowledge Sharing - Jupyter, PySpark and DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/jupyter/jupyter-pyspark-duckdb/)
* [Data Engineering Helpers - Knowledge Sharing - Spark](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/)
* [Data Engineering Helpers - Knowledge Sharing - Unity Catalog (UC)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/unity-catalog/)
* [Data Engineering Helpers - Knowledge Sharing - SQLMesh](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/)
* [Data Engineering Helpers - Knowledge Sharing - DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/)
* [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/)
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box)

## Delta Lake
* [Delta Lake release compatibility matrix](https://docs.delta.io/releases/)
* [Delta Lake releases](https://github.com/delta-io/delta/releases)
* [Delta Lake documentation](https://docs.delta.io/)
  * [Delta Lake - Quick start guide](https://docs.delta.io/latest/quick-start.html)
* [Delta Lake - Compatibility matrix with Spark](https://docs.delta.io/releases/)
* [GitHub - Delta Lake - `delta` repository](https://github.com/delta-io/delta)
* [Maven central - Delta Spark: `io.delta/delta-spark`](https://mvnrepository.com/artifact/io.delta/delta-spark)

## Spark 4.1 preview
* As of end 2025, per
  [Delta Lake release compatibility matrix](https://docs.delta.io/releases/)
  and [Delta Lake releases](https://github.com/delta-io/delta/releases),
  there does not seem to be a version of Delta Lake compatible with
  the yet to be released Spark 4.1 version
* For this cheat sheet, the following two alternatives have been tried, without
  success so far:
  * Installing and using the latest Delta Lake version out of the box, that is,
  [4.0.0 ](https://github.com/delta-io/delta/releases/tag/v4.0.0):
```bash
$ python -mpip install delta-spark==4.0.0
$ pyspark --packages io.delta:delta-spark_2.13:4.0.0 --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"
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
## Java
* If not already done so, install Java 21
  * [Spark 4.1.0 appears to be compatible with Java versions from 17 up to 21 included](https://spark.apache.org/docs/4.1.0-preview4/#downloading)
  * SDKMan is recommended to manage the versions of Java-based
    tools. For instance, with the Corretto JDKs:
```bash
$ sdk install java 21.0.9-amzn
$ sdk default java 21.0.9-amzn
```
* Check the version of Java:
```bash
$ java -version
openjdk version "21.0.9" 2025-10-21 LTS
OpenJDK Runtime Environment Corretto-21.0.9.10.1 (build 21.0.9+10-LTS)
OpenJDK 64-Bit Server VM Corretto-21.0.9.10.1 (build 21.0.9+10-LTS, mixed mode, sharing)
```

## Delta Lake
* The simplest way to install Delta Lake is through Pypi. First check the
  [Delta Lake release compatibility matrix](https://docs.delta.io/releases/),
  and then both PySpark and Delta Lake may be installed together.
  A few possible combinations:
  * Spark 4.0 and Delta Lake 4.0:
```bash
$ python -mpip install pyspark==4.0.0 delta-spark==4.0.0
```
  * Spark 3.5 and Delta Lake 3.3:
```bash
$ python -mpip install pyspark==3.5.4 delta-spark==3.3.2
```
  * Spark 3.4 and Delta Lake 3.2:
```bash
$ python -mpip install pyspark==3.4.4 delta-spark==3.2.1
```

## Build from the sources

