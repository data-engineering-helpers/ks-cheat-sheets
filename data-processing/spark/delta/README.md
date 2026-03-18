# Cheat Sheet - Delta Lake

## Table of Content (ToC)

* [Cheat Sheet \- Delta Lake](#cheat-sheet---delta-lake)
  * [Table of Content (ToC)](#table-of-content-toc)
  * [Overview](#overview)
    * [A note about Delta keeping up with Spark upgrades](#a-note-about-delta-keeping-up-with-spark-upgrades)
  * [References](#references)
    * [Data Engineering helpers](#data-engineering-helpers)
    * [Delta Lake](#delta-lake)
    * [Java](#java)
    * [Spark 4\.1](#spark-41)
  * [Setup](#setup)
    * [Setup of Delta Lake](#setup-of-delta-lake)
    * [Build from the sources](#build-from-the-sources)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

## Overview

[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/delta/README.md)
explains how (potentially to install and) to use
[Delta Lake](https://github.com/delta-io/delta), _e.g._,
on a laptop or on a virtual machine (VM).

### A note about Delta keeping up with Spark upgrades

At some point, whenever Spark is upgraded, the corresponding version of
Delta Lake may not be immediately released to work together with the new Spark version.
Indeed, Delta Lake needs to come with a version compatible to Spark, as per the
[Delta Lake release compatibility matrix](https://docs.delta.io/releases/).

That situation happened for instance at the end of 2025, when:

* Spark 4.1 was available only as a preview
* Delta Lake was not easily available in a compatible version
  * The
   [Delta Lake 4.1.0 milestone](https://github.com/delta-io/delta/milestone/31)
   stated that the new version was due for end of January 2026, which more or less
   happened (it was released in February 2026).

In some very specific cases (_e.g._, trying new features not yet available in the
public releases), it may be interesting to build Delta Lake from the sources. This
cheat sheet also gives details on how to do it.

## References

### Data Engineering helpers

* [Data Engineering Helpers - Knowledge Sharing - Java](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/java-world/)
* [Data Engineering Helpers - Knowledge Sharing - Python](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/python/)
* [Data Engineering Helpers - Knowledge Sharing - Spark](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/)
* [Data Engineering Helpers - Knowledge Sharing - Spark Connect](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/spark-connect/)
* [Data Engineering Helpers - Knowledge Sharing - Spark Declarative Pipelines (SDP)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/spd/)
* [Data Engineering Helpers - Knowledge Sharing - Unity Catalog (UC)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/unity-catalog/)
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box)

### Java

* [Java releases](https://www.java.com/releases/)
* From Sep. 2025, the new LTS has been the 25 release
* The next LTS version should be the 27 release, expected to be available from
  Sep. 2027

### Delta Lake

* [Delta Lake release compatibility matrix](https://docs.delta.io/releases/)
* [Delta Lake releases](https://github.com/delta-io/delta/releases)
* [Delta Lake documentation](https://docs.delta.io/)
  * [Delta Lake - Quick start guide](https://docs.delta.io/latest/quick-start.html)
* [GitHub - Delta Lake - `delta` repository](https://github.com/delta-io/delta)
* [Maven central - Delta Spark: `io.delta/delta-spark`](https://mvnrepository.com/artifact/io.delta/delta-spark)
* [Delta Lake doc - Delta Connect](https://docs.delta.io/delta-spark-connect/)

### Spark 4.1

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
python -mpip install delta-spark==4.0.1
pyspark --packages io.delta:delta-spark_2.13:4.0.1 \
  --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
  --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"
```

* Building Delta Lake from the sources, as detailed in the sub-section below,
  installing and using it:

```bash
pyspark --packages io.delta:delta-spark_2.13:4.0.1-SNAPSHOT \
  --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
  --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"
```

* When testing simple Delta examples, the following error appears:

```python
>>> data = spark.range(0, 5)
>>> data.write.format("delta").save("data-delta-test")
py4j.protocol.Py4JJavaError: An error occurred while calling o61.save.
: com.google.common.util.concurrent.ExecutionError: java.lang.NoSuchMethodError:
 'void org.apache.spark.internal.LogKey.$init$(org.apache.spark.internal.LogKey)'
```

## Setup

* See the
  [setup section of the Spark cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/README.md#setup)
  (in this same Git repository) for installation instructions about Java and Spark

### Setup of Delta Lake

* The simplest way to install Delta Lake is through Pypi. First check the
  [Delta Lake release compatibility matrix](https://docs.delta.io/releases/),
  and then both PySpark and Delta Lake may be installed together.
  A few possible combinations:
  * Spark 4.1 and Delta Lake 4.0.1 (as of Feb. 2026, no combination was found
    which could make Delta Lake work):

```bash
python -mpip install pyspark==4.1.1 delta-spark==4.0.1
```

* Spark 4.0 and Delta Lake 4.0:

```bash
python -mpip install pyspark==4.0.0 delta-spark==4.0.0
```

* Spark 3.5 and Delta Lake 3.3:

```bash
python -mpip install pyspark==3.5.4 delta-spark==3.3.2
```

* Spark 3.4 and Delta Lake 3.2:

```bash
python -mpip install pyspark==3.4.4 delta-spark==3.2.1
```

### Build from the sources

TBD - Ipsem lorum
