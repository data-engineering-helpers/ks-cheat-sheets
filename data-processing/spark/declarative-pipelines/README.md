Cheat Sheet - Spark Declarative Pipelines (SDP)
===============================================

# Table of Content (ToC)
* [Overview](#overview)
* [References](#references)
  * [Data Engineering helpers](#data-engineering-helpers)
  * [Spark Declarative Pipelines (SDP)](#spark-declarative-pipelines-sdp)
  * [Delta Lake](#delta-lake)
  * [Articles](#articles)
    * [Spark Declarative Pipelines 101](#spark-declarative-pipelines-101)
* [Setup](#setup)
  * [Java](#java)
  * [Delta Lake](#delta-lake-1)
  * [Spark 4\.1\.0 preview](#spark-410-preview)
  * [Delta Lake](#delta-lake-2)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/declarative-pipelines/README.md)
explains how to install and to use
[Spark Declarative Pipelines](https://spark.apache.org/docs/4.1.0-preview4/declarative-pipelines-programming-guide.html),
_e.g._, on a laptop or on a virtual machine (VM).

Since Delta Lake has not released a version explicitly compatible with Spark 4.1.x
yet, Delta Lake may not fully work with Spark versions featuring Spark Declarative
Pipelines (SDP), that is, Spark 4.1+.
[Delta Lake 4.1.0 milestone](https://github.com/delta-io/delta/milestone/31)
states that it was due for end of January 2026, but the completion rate is still
0% for that miestone, even at the end of Feb. 2026.
And there is no sign in
[Delta Lake releases](https://github.com/delta-io/delta/releases),
nor in the
[Delta Lake release compatibility matrix](https://docs.delta.io/releases/),
of a version explicitly compatible with Spark 4.1.x.

# References

## Data Engineering helpers
* [Data Engineering Helpers - Knowledge Sharing - Spark](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/)
* [Data Engineering Helpers - Knowledge Sharing - Delta Lake](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/delta/)
* [Data Engineering Helpers - Knowledge Sharing - Python](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/python/)
  * [Data Engineering Helpers - Knowledge Sharing - Jupyter, PySpark and DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/jupyter/jupyter-pyspark-duckdb/)
* [Data Engineering Helpers - Knowledge Sharing - Unity Catalog (UC)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/unity-catalog/)
* [Data Engineering Helpers - Knowledge Sharing - SQLMesh](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/)
* [Data Engineering Helpers - Knowledge Sharing - DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/)
* [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/)
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box)

## Spark Declarative Pipelines (SDP)
* [Apache Spark doc - Spark Declarative Pipelines Programming Guide](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
* Databricks Lakeflow:
  * [Databricks doc - AWS - Lakeflow Spark Declarative Pipelines (LDP)](https://docs.databricks.com/aws/en/ldp/)
  * [Microsoft doc - Lakeflow Spark Declarative Pipelines (LDP)](https://learn.microsoft.com/en-us/azure/databricks/ldp/)
* [GitHub - End-to-end quick start guide for Spark Declarative Pipelines](https://github.com/Idowuilekura/sdp-quick-start)

## Delta Lake
* [Delta Lake release compatibility matrix](https://docs.delta.io/releases/)
* [Delta Lake releases](https://github.com/delta-io/delta/releases)
* [Delta Lake documentation](https://docs.delta.io/)
  * [Delta Lake - Quick start guide](https://docs.delta.io/latest/quick-start.html)
* [Delta Lake - Compatibility matrix with Spark](https://docs.delta.io/releases/)
* [GitHub - Delta Lake - `delta` repository](https://github.com/delta-io/delta)
* [Maven central - Delta Spark: `io.delta/delta-spark`](https://mvnrepository.com/artifact/io.delta/delta-spark)

## Articles

### Spark Declarative Pipelines 101

* Date: March 2026
* Author: Bartosz Konieczny
  ([Bartosz Konieczny on LinkedIn](https://www.linkedin.com/in/bartosz-konieczny-waitingforcode/),
  [Bartosz Konieczny on Waiting for code blog, that is, his blog](https://www.waitingforcode.com/static/about))
* [Waiting for code blog - Spark Declarative Pipelines (SDP) 101](https://www.waitingforcode.com/apache-spark-structured-streaming/spark-declarative-pipelines-101/read)

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
* Reference:
  [Data Engineering Helpers - Knowledge Sharing - Delta Lake](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/delta/)

## Spark 4.1.0 preview
* Specify the Spark version:
```bash
$ SPARK_VERSION="4.1.0.dev4"
```

* Download PySpark:
```bash
$ mkdir -p $HOME/opt/spark/archives
$ curl -kL https://dist.apache.org/repos/dist/release/spark/spark-4.1.0-preview4/pyspark-${SPARK_VERSION}.tar.gz -o $HOME/opt/spark/pyspark-${SPARK_VERSION}.tar.gz
```
* Build and install PySpark:
``` bash
$ pushd $HOME/opt/spark
$ tar zxf pyspark-${SPARK_VERSION}.tar.gz && mv pyspark-${SPARK_VERSION}.tar.gz archives
$ pushd pyspark-${SPARK_VERSION}
$ python -mbuild .
$ python -mpip install dist/pyspark-${SPARK_VERSION}-*.whl
$ popd && popd
```
* Check that PySpark has been installed correctly:
```bash
$ python -mpip show pyspark
```
* Check the version of PySpark:
```bash
$ pyspark --version
WARNING: Using incubator modules: jdk.incubator.vector
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 4.1.0-preview4
      /_/

Using Scala version 2.13.17, OpenJDK 64-Bit Server VM, 21.0.9
Branch HEAD
Compiled by user ubuntu on 2025-11-16T18:45:58Z
Revision c125aea395b37ec1fa3b4e8b5a3e9bee270203c2
Url https://github.com/apache/spark
```

## Delta Lake
* [Delta Lake release compatibility matrix](https://docs.delta.io/releases/)
* [Delta Lake releases](https://github.com/delta-io/delta/releases)
* As of end 2025, the latest Delta Lake release is 4.0.0
* There does not seem to be any release, or even
  [branch](https://github.com/delta-io/delta/branches), for Spark 4.1
* The
  [default version of Delta Lake is 3.4.0-SNAPSHOT](https://github.com/delta-io/delta/blob/master/version.sbt)
* The latest branch seems to be [branch 4.0](https://github.com/delta-io/delta/tree/branch-4.0)
