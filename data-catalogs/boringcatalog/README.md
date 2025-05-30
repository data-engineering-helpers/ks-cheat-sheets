Cheat Sheet - Boring Catalog
============================

# Table of Content (ToC)
* [Overview](#overview)
* [References](#references)
  * [Data Engineering helpers](#data-engineering-helpers)
  * [BoringData documentation](#boringdata-documentation)
* [Setup](#setup)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/boringcatalog/README.md)
explains how to install and to use
[Boring Catalog](https://github.com/boringdata/boring-catalog)
on premises, _e.g._, on a laptop or on a virtual machine (VM).

# References

## Data Engineering helpers
* [Data Engineering Helpers - Knowledge Sharing - Minio](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-storage/minio/README.md)
* [Data Engineering Helpers - Knowledge Sharing - DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/README.md)

## BoringData documentation
* GitHub page: https://github.com/boringdata/boring-catalog
* Article on Substack by Julien Hurault (the author of Boring Catalog):
  https://juhache.substack.com/p/boring-iceberg-catalog
* Showcase video by Daniel Beach, May 2025, Substack:
  https://substack.com/home/post/p-164251337
  * Companion article: https://substack.com/home/post/p-163944714

# Setup
* Optionally (but recommended), install `uv`
  * On MacOS:
```bash
brew intall uv
```

* Optionally (but recommended), install a virtual environment with `uv`
```bash
uv venv
```

* Install the Boring-Catalog Python module (as well as a few other utilities)
  * With a standard Python environment:
```bash
pip install -U pyiceberg duckdb polars boringcatalog
```
  * With `uv`:
```bash
uv pip install -U pyiceberg duckdb polars boringcatalog
```

* With a standard Python environment, the Shell needs to be reloaded
  (`uv` already manages virtual environment, no additional step is needed with
  it)
  * With Bash
```bash
exec bash
```
  * With Zsh
```bash
exec zsh
```

* From this point on, it will not be repeated every time how to use `uv`.
  With `uv`, just prefix every command by `uv run`. For instance:
  * Simple Python command: `uv run python -V`
  * BoringCatalog command (`ice`): `uv run ice`
  * And so on

* Init the catalog with a storage location on S3:
```bash
ice init -p warehouse=s3://mybucket/ice-warehouse
```

* Download the NYC taxi Parquet file (45 MB) from Kaggle:
```bash
curl https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet -o /tmp/yellow_tripdata_2023-01.parquet
```

* Create a table with the Parquet file:
```bash
ice commit my_table --source /tmp/yellow_tripdata_2023-01.parquet
```

* Launch DuckDB prompt, pre-set with the BoringCatalog extension:
```bash
ice duck
```

* From the DuckDB prompt
  * Dump everything as DDL:
```sql
.schema
```
  * Set the Boring-Catalog as the default schema:
```sql
use ice_default;
```
  * Display the tables:
```sql
show tables;
```
  * Display a few rows of the just created table (prefixing the table name
  is optional, as a default schema has been specified; the prefix is kept here
  so that the line can still be copied/pasted even without specifying a default
  schema):
```sql
select * from ice_default.my_table limit 10;
```
  * Describe the schema:
```sql
desc ice_default.my_table;
```
  * Count the number of rows:
```sql
select count(*) as nb_rows from ice_default.my_table;
┌────────────────┐
│    nb_rows     │
│     int64      │
├────────────────┤
│    3066766     │
│ (3.07 million) │
└────────────────┘
```
  * Quit the DuckDB Shell:
```sql
.quit
```
