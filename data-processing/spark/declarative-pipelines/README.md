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
    * [Lakeflow Declarative Pipelines](#lakeflow-declarative-pipelines)
    * [Spark Declarative Pipelines 101](#spark-declarative-pipelines-101)
    * [SDP Quick Start](#sdp-quick-start)
  * [Getting started](#getting-started)
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

* [Data Engineering Helpers - Knowledge Sharing - Delta Lake](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/delta/README.md#delta-lake)

## Articles

## Declarative Pipelining in Apache Spark

* Title: Declarative Pipelining in Apache Spark Part 1: Focus on Your Data, Not Your DAGs
* Date: March 2026
* Author: [Lisa N. Cao](https://www.linkedin.com/in/lisancao)
* [Medium - Declarative Pipelining in Apache Spark Part 1](https://medium.com/apache-spark/declarative-pipelining-in-apache-spark-part-1-focus-on-your-data-not-your-dags-553a1056d178)

### Lakeflow Declarative Pipelines

* Date: March 2026
* Author: Hitesh Kaushik
  ([Hitesh Kaushik on LinkedIn](https://www.linkedin.com/in/h-kaushik/),
  [Hitesh Kaushik on Medium](https://medium.com/@hiteshkhk0105))
* Series of LinkedIn posts:
  * [LinkedIn post - Lakeflow Declarative - Introduction](https://www.linkedin.com/posts/h-kaushik_lake-flow-spark-declarative-pipelines-activity-7432802777547862016-OUE8/)
  * [LinkedIn post - Lakeflow Declarative - Part 1](https://www.linkedin.com/posts/h-kaushik_dataengineering-databricks-lakeflow-activity-7439669655293755392-R-15/)
  * [LinkedIn post - Lakeflow Declarative - Part 2](https://www.linkedin.com/posts/h-kaushik_phase-2-of-the-lakeflow-series-we-build-share-7442202922941267969-YHzl/)
    * [Medium - Lakeflow Declarative pipelines - Actual end-to-end example with code](https://medium.com/@hiteshkhk0105/build-a-real-etl-pipeline-from-scratch-with-lakeflow-declarative-pipelines-ae3aaabf7274)

### Spark Declarative Pipelines 101

* Date: March 2026
* Author: Bartosz Konieczny
  ([Bartosz Konieczny on LinkedIn](https://www.linkedin.com/in/bartosz-konieczny-waitingforcode/),
  [Bartosz Konieczny on Waiting for code blog, that is, his blog](https://www.waitingforcode.com/static/about))
* Part 1: [Waiting for code blog - Spark Declarative Pipelines (SDP) 101](https://www.waitingforcode.com/apache-spark-structured-streaming/spark-declarative-pipelines-101/read)
* Part 2: [Waiting for code blog - Spark Declarative Pipelines (SDP), going further](https://www.waitingforcode.com/apache-spark-structured-streaming/spark-declarative-pipelines-going-further/read)
* [GitHub - PySpark example code supporting the blog post about SDP](https://github.com/bartosz25/spark-playground/tree/master/structured-streaming-declarative-pipelines/pyspark)

### SDP Quick Start

* Date: March 2026
* Author: Idowu Oselumhe Ilekura
  ([Idowu Oselumhe Ilekura on LinkedIn](https://www.linkedin.com/in/ilekuraidowu/),
  [Idowu Oselumhe Ilekura on GitHub](https://github.com/Idowuilekura))
* [LinkedIn post showcasing the SDP Quick Start Git repository](https://www.linkedin.com/posts/ilekuraidowu_want-to-experiment-with-spark-declarative-activity-7435610338764410880-BsID)
* [GitHub - SDP Quick Start](https://github.com/Idowuilekura/sdp-quick-start)

## Getting started

### Create a new project

* Specify a project name, for instance `sdp-poc` (PoC standing for
  Proof-of-Concept):
  
```bash
MY_PROJ=sdp-poc
```

* Initialize the project and go into the newly created directory:

```bash
spark-pipelines init --name $MY_PROJ
cd $MY_PROJ
```

* Execute the SDP pipeline:

```bash
spark-pipelines run
```

## Setup

### Setup of Apache Spark

* Reference:
  [Data Engineering Helpers - Knowledge Sharing - Spark](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/)

### Setup of Delta Lake

* Reference:
  [Data Engineering Helpers - Knowledge Sharing - Delta Lake](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/delta/)

### Setup of SDP

* See
  [Apache Spark doc - SDP Programming Guide - Quick install](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html#quick-install)
  for the details

* SDP comes as an optional module of PySpark and can therefore be installed from
  [Pypi](https://pypi.org/project/pyspark/):

```bash
python -mpip install "pyspark[pipelines]"
```

* Note that SDP has a dependency on
  [Spark Connect](https://spark.apache.org/docs/latest/spark-connect-overview.html).
  The installation of the SDP option will therefore pull in a few Python
  dependencies related to Spark Connect, such as gRPC (_e.g._,
  [grpcio](https://pypi.org/project/grpcio/)
  and [Protocol Buffers (aka Protobuf)](https://pypi.org/project/protobuf/)).
  The following alternate installation option should pull in the same
  dependencies:

```bash
python -mpip install "pyspark[connect,sql,pandas_on_spark]"
```

* Moreover, in order to install with a compatible version of Delta Lake:

```bash
python -mpip install "pyspark[pipelines] delta-spark"
```

* As an alternative, it can of course be installed from a manual install of
  [Apache Spark](https://spark.apache.org/downloads.html)
