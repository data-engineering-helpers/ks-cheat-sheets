# Cheat Sheet - Spark Declarative Pipelines (SDP)

## Table of Content (ToC)

* [Cheat Sheet \- Spark Declarative Pipelines (SDP)](#cheat-sheet---spark-declarative-pipelines-sdp)
  * [Table of Content (ToC)](#table-of-content-toc)
  * [Overview](#overview)
  * [References](#references)
    * [Data Engineering helpers](#data-engineering-helpers)
    * [Java](#java)
    * [Spark Declarative Pipelines (SDP)](#spark-declarative-pipelines-sdp)
    * [Delta Lake](#delta-lake)
  * [Articles](#articles)
    * [Spark Declarative Pipelines 101](#spark-declarative-pipelines-101)
    * [SDP Quick Start](#sdp-quick-start)
  * [Setup](#setup)
    * [Setup of Apache Spark](#setup-of-apache-spark)
    * [Setup of Delta Lake](#setup-of-delta-lake)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

## Overview

[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/declarative-pipelines/README.md)
explains how to install and to use
[Spark Declarative Pipelines](https://spark.apache.org/docs/4.1.0-preview4/declarative-pipelines-programming-guide.html),
_e.g._, on a laptop or on a virtual machine (VM).

The
[Delta Lake v4.1.0 release](https://github.com/delta-io/delta/releases/tag/v4.1.0)
now brings support for Apache Spark 4.1, which is the first release of Spark
featuring the Spark Declarative Pipelines (SDP) framework.
See also
[Data Engineering Helpers - Knowledge Sharing - Delta Lake](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/delta/)
for more details about Delta Lake and its compatibility with Apache Spark.

## References

### Data Engineering helpers

* [Data Engineering Helpers - Knowledge Sharing - Java](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/java-world/)
* [Data Engineering Helpers - Knowledge Sharing - Python](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/python/)
* [Data Engineering Helpers - Knowledge Sharing - Spark](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/)
* [Data Engineering Helpers - Knowledge Sharing - Spark Connect](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/spark-connect/)
* [Data Engineering Helpers - Knowledge Sharing - Delta Lake](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/delta/)
* [Data Engineering Helpers - Knowledge Sharing - Unity Catalog (UC)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/unity-catalog/)
* [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/)
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box)

### Java

* [Java releases](https://www.java.com/releases/)
* From Sep. 2025, the new LTS has been the 25 release
* The next LTS version should be the 27 release, expected to be available from
  Sep. 2027

### Spark Declarative Pipelines (SDP)

* Spark Declarative Pipelines has been developed as part of
  [SPARK-51727](https://issues.apache.org/jira/browse/SPARK-51727) by:
  Aakash Japi, Anish Mahto, Calili dos Santos Silva, Dongjoon Hyun,
  Jacek Laskowski, Jacky Wang, Jon Mio, Jungtaek Lim, Peter Toth, Sandy Ryza,
  Sanford Ryza, Wenchen Fan, Yang Jie, Yuheng Chang
* [Apache Spark doc - Spark Declarative Pipelines Programming Guide](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
* Databricks Lakeflow:
  * [Databricks doc - AWS - Lakeflow Spark Declarative Pipelines (LDP)](https://docs.databricks.com/aws/en/ldp/)
  * [Microsoft doc - Lakeflow Spark Declarative Pipelines (LDP)](https://learn.microsoft.com/en-us/azure/databricks/ldp/)
* [GitHub - End-to-end quick start guide for Spark Declarative Pipelines](https://github.com/Idowuilekura/sdp-quick-start)
* [YouTube - Spark Declarative Pipelines (SDP) explained in under 20 minutes](https://www.youtube.com/watch?v=WNPYEZ7SMSM),
  by [Sandy Ryza](https://www.linkedin.com/in/sandyryza/), Feb. 2026

### Delta Lake

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
* [GitHub - PySpark example code supporting the blog post about SDP](https://github.com/bartosz25/spark-playground/tree/master/structured-streaming-declarative-pipelines/pyspark)

### SDP Quick Start

* Date: March 2026
* Author: Idowu Oselumhe Ilekura
  ([Idowu Oselumhe Ilekura on LinkedIn](https://www.linkedin.com/in/ilekuraidowu/),
  [Idowu Oselumhe Ilekura on GitHub](https://github.com/Idowuilekura))
* [LinkedIn post showcasing the SDP Quick Start Git repository](https://www.linkedin.com/posts/ilekuraidowu_want-to-experiment-with-spark-declarative-activity-7435610338764410880-BsID)
* [GitHub - SDP Quick Start](https://github.com/Idowuilekura/sdp-quick-start)

## Setup

### Setup of Apache Spark

* Reference:
  [Data Engineering Helpers - Knowledge Sharing - Spark](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/)

### Setup of Delta Lake

* Reference:
  [Data Engineering Helpers - Knowledge Sharing - Delta Lake](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/delta/)
