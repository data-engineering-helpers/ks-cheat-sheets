Knowledge Sharing (KS) - Spark - SCD2 with Delta
================================================

# Overview
This [documentation](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/001-scd2-w-delta/README.md).
aims at showcasing how to perform a "merge into" operation, from some Parquet
source data set into a Delta-enabled data set.

# References
* [LinkedIn post - SCD Type 2 Implementation Simplified with Spark and Delta Lake](https://www.linkedin.com/posts/mathew-midhun_lets-simplify-scd2-implementation-ugcPost-7352104443984666624-rjPs/),
  July 2025, [Mathew Midhun](https://www.linkedin.com/in/mathew-midhun/)

# Getting started

* Clean any previous work (including local Spark warehouse/database,
  Python virtual environment):
```bash
make cleaners
```

* If needed, install Python dependencies (once it has been done once, it is
  no longer necessary):
```bash
make init-python
```

* Create the Delta tables in the local Spark warehouse/database:
```bash
make init-database
```

* Generate the initial and incremental data-sets:
```bash
make init-datasets
```

* Ingest the initial and incremental data-sets, filling the Delta table:
```bash
make ingest-datasets
```
