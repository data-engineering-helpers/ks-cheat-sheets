# Knowledge Sharing (KS) - Spark - Tutorials / examples

## Table of Content (ToC)

* [Knowledge Sharing (KS) \- Spark \- Tutorials / examples](#knowledge-sharing-ks---spark---tutorials--examples)
  * [Table of Content (ToC)](#table-of-content-toc)
  * [Overview](#overview)
  * [References](#references)
    * [Data Engineering helpers](#data-engineering-helpers)
  * [Spark\-related tutorials](#spark-related-tutorials)
  * [Different ingestion types](#different-ingestion-types)
    * [Full refresh vs increment pipelines](#full-refresh-vs-increment-pipelines)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

## Overview

This
[documentation](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/README.md).
showcases a few end-to-end Spark pipelines, for instance
[SCD2 ingestion with Delta Lake](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/001-scd2-w-delta/README.md),
[Getting started with Spark Declarative Pipelines (SDP)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/004-sdp-quick-start/README.md).

Some of the Spark-related tutorials require sample datasets, which may be
generated/managed thanks to a [dedicated directory](000-data-setup/).

The
[_Spark and related components_ sub-section of the Spark cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/README.md#spark-and-related-components)
details the various components in the Spark ecosystem. The Spark-related
tutorials feature some of those components wherever possible. For instance,
the
[SCD2 ingestion with Delta Lake tutorial](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/001-scd2-w-delta/)
features a few variations:

* Pure Delta Lake tables
* Integration with Unity Catalog (UC)
* Integration with Spark Connect only
* Integration with Spark Connect, itself using Unity Catalog (UC)

## References

### Data Engineering helpers

* [Data Engineering Helpers - Knowledge Sharing - Java](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/java-world/)
* [Data Engineering Helpers - Knowledge Sharing - Python](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/python/)
* [Data Engineering Helpers - Knowledge Sharing - Spark](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/)
* [Data Engineering Helpers - Knowledge Sharing - Delta Lake](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/delta/)
* [Data Engineering Helpers - Knowledge Sharing - Spark Connect (SC)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/spark-connect/)
* [Data Engineering Helpers - Knowledge Sharing - Spark Declarative Pipelines (SDP)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/declarative-pipelines/)
* [Data Engineering Helpers - Knowledge Sharing - Unity Catalog (UC)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/unity-catalog/)

## Spark-related tutorials

* [000 - Setup of datasets for the Spark-related tutorials](000-data-setup/README.md)
* [001 - SCD2 with Delta Lake](001-scd2-w-delta/README.md)
* (WIP) [002 - Incremental vs full ingestion](002-incremental-vs-full//README.md)
* (TBD) [003 - Row-level lineage](003-row-level-lineage/README.md)
* (WIP) [004 - Getting started with Spark Declarative Pipelines (SDP)](004-sdp-quick-start/README.md)

## Different ingestion types

### Full refresh vs increment pipelines

* [Substack - Seattle Data Guy - Full refresh vs increment pipelines](https://seattledataguy.substack.com/p/full-refresh-vs-incremental-pipelines)
  * Author: [Seattle Data Guy](https://substack.com/@seattledataguy)
  * Date: March 2026
* [LinkedIn post - Full refresh vs increment pipelines](https://www.linkedin.com/posts/jimmy-pang-hk603_full-refresh-vs-incremental-pipelines-share-7441154171598381056-WNIv/)
  * Author: [Jimmy Pang](https://www.linkedin.com/in/jimmy-pang-hk603)
  * Date: May 2026
