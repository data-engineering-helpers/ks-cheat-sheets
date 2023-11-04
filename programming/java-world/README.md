Cheat Sheets - Java and Scala
=============================

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/java-world/README.md)
explains how to install and to maintain a few tools pertaining to
programming with Java and Scala, in particular for Spark-powered data processing.

# SDKMan
* If Java needs to be installed (_e.g._, on systems not packaging it natively),
  it is advised to install and use [SDKMan](https://sdkman.io/)
  + Once SDKMan has been installed, installing in parallel a specific version of Java becomes as easy as
    `sdk install 11.0.21-amzn` (here, for the Amazon-supported Corretto OpenJDK 11)
  + On MacOS, Java may simply be installed with HomeBrew: `brew install openjdk`

# JAR packages on Maven Central
* The packages may be searched for on [Maven Central](https://mvnrepository.com/)

# Specific JAR packages

## Hadoop
* Hadoop download page (as of end 2023, the [latest version is 3.3.6](https://archive.apache.org/dist/hadoop/common/hadoop-3.3.6/)
  and dates back to June 2023): https://archive.apache.org/dist/hadoop/common/current/

## Hive Metastore
* Hive Metastore standalone download page (as of end 2023, the latest version is 3.0.0 and dates back to 2018):
  https://downloads.apache.org/hive/hive-standalone-metastore-3.0.0/

## PostgreSQL JDBC drivers
* The [PostgreSQL drivers are available only for JDK up to version 8](https://jdbc.postgresql.org/download)

## Spark
* Download page for Apache Spark: https://spark.apache.org/downloads.html

# Examples

## Delta
* Delta Spark:
  + [`io.delta:delta-spark_2.12:3.0.0` package page](https://mvnrepository.com/artifact/io.delta/delta-spark_2.12/3.0.0)
  + Download the JAR package:
```bash
$ wget https://repo1.maven.org/maven2/io/delta/delta-spark_2.12/3.0.0/delta-spark_2.12-3.0.0.jar
```
* Delta standalone:
  + [`io.delta:delta-standalone_2.12:3.0.0` package page](https://mvnrepository.com/artifact/io.delta/delta-standalone_2.12/3.0.0)
  + Download the JAR package:
```bash
$ wget https://repo1.maven.org/maven2/io/delta/delta-standalone_2.12/3.0.0/delta-standalone_2.12-3.0.0.jar
```

## PostgreSQL JDBC drivers
* PostgreSQL JDBC driver:
  + [`org.postgresql:postgresql:42.6.0` package page](https://mvnrepository.com/artifact/org.postgresql/postgresql/42.6.0)
```bash
$ wget https://repo1.maven.org/maven2/org/postgresql/postgresql/42.6.0/postgresql-42.6.0.jar
```

