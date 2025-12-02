Cheat Sheet - Spark Declarative Pipelines
=========================================

# Table of Content (ToC)


# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/declarative-pipelines/README.md)
explains how to install and to use
[Spark Declarative Pipelines](https://spark.apache.org/docs/4.1.0-preview4/declarative-pipelines-programming-guide.html), _e.g._,
on a laptop or on a virtual machine (VM).

Note that, since the Declarative Pipelines feature is available in Apache Spark only
from the yet to be released 4.1 version, as of end 2025 it has to be tested on preview
releases, _e.g._,
[Apache Spark 4.1.0 preview](https://spark.apache.org/docs/4.1.0-preview4/)

Since Spark 4.1 is available only as a preview (as of end 2025), Delta Lake is not
easily available in a compatible version.
The [Delta Lake 4.1.0 milestone](https://github.com/delta-io/delta/milestone/31)
states that it is due for end of January 2026.

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

## Spark Declarative Pipelines
* [Apache Spark - Doc - Declarative Pipelines programming guide](https://spark.apache.org/docs/4.1.0-preview4/declarative-pipelines-programming-guide.html)
* [Apache Spark - Doc - Spark 4.1.0 preview](https://spark.apache.org/docs/4.1.0-preview4/)

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
