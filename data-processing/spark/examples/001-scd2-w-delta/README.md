Knowledge Sharing (KS) - Spark - SCD2 with Delta
================================================

# Overview
This [documentation](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/001-scd2-w-delta/README.md).
aims at showcasing how to perform a "merge into" operation, from some Parquet
source data set into a Delta-enabled data set.

# References
* [LinkedIn post - SCD Type 2 Implementation Simplified with Spark and Delta Lake](https://www.linkedin.com/posts/mathew-midhun_lets-simplify-scd2-implementation-ugcPost-7352104443984666624-rjPs/),
  July 2025, [Mathew Midhun](https://www.linkedin.com/in/mathew-midhun/)
* [LinkedIn post - A cheat sheet for building fail-safe/idempotent DataBricks jobs](https://www.linkedin.com/posts/jrlasak_databricks-dataengineering-etl-activity-7358425287455363072-x2yw/),
  August 2025, [Jakub Lasak](https://www.linkedin.com/in/jrlasak/)
* [GitHub - Datanomy](https://github.com/raulcd/datanomy)

# Getting started

* Clean any previous work (including local Spark warehouse/database,
  Python virtual environment):
```bash
make cleaners
```

* Initialize the uv virtual environment (_e.g._, uv installs the Python dependencies
  in that dedicated virtual environment):
```bash
make init update
```

* Create the Delta tables in the local Spark warehouse/database:
```bash
make init-database
```

* Generate the initial and incremental data-sets (it crates an stores Parquet
  files for the initial and the incremental data-sets):
```bash
make init-datasets
```

* Analyze the generate data-sets with Datanomy:
```bash
make check-dataset-init
make check-dataset-incremental
```

* Ingest the initial and incremental data-sets, filling the Delta table:
```bash
make ingest-datasets
```

* Check the content of the database (Delta table):
```bash
make check-database
```

