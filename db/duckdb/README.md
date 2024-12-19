Cheat Sheet - DuckDB
====================

# Table of Content (ToC)
* [Overview](#overview)
  * [References](#references)
    * [DuckDB in Jupyter](#duckdb-in-jupyter)
* [Use cases](#use-cases)
* [Setup](#setup)
  * [DuckDB on the command\-line (CLI)](#duckdb-on-the-command-line-cli)
  * [DuckDB Python library](#duckdb-python-library)
  * [Integration with S3](#integration-with-s3)
  * [Geonames data files](#geonames-data-files)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/README.md)
explains how to install and to use DuckDB.

DuckDB allows to process and analyze rather big data files on local
computers or rather small virtual machines (VM).

The following is an excerpt from https://duckdb.org/why_duckdb .
> There are many database management systems (DBMS) out there. But there is
> [no one-size-fits all database system](http://cs.brown.edu/research/db/publications/fits_all.pdf).
> All take different trade-offs to better adjust to specific use cases.
> DuckDB is no different. Here, we try to explain what goals DuckDB
> has and why and how we try to achieve those goals through technical means.
> To start with, DuckDB is a [relational (table-oriented) DBMS](https://en.wikipedia.org/wiki/Relational_database)
> that supports the [Structured Query Language (SQL)](https://en.wikipedia.org/wiki/SQL).

## References
* DuckDB home page: https://duckdb.org/
   + Why DuckDB: https://duckdb.org/why_duckdb
* DuckDB project on GitHub: https://github.com/duckdb/duckdb
* DuckDQ - Embeddable Data Quality (DQ) validation:
  https://github.com/tdoehmen/duckdq
* [DuckDB - Modern Data Stack (MDS) in a box](https://duckdb.org/2022/10/12/modern-data-stack-in-a-box.html)
* Connectivity with Arrow: https://duckdb.org/2023/08/04/adbc.html

### DuckDB in Jupyter
* [GitHub - Data Engineering Helpers - Cheat Sheet - Jupyter with PySpark and DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/jupyter/jupyter-pyspark-duckdb/)
* [DuckDB docs - DuckDB in Jupyter](https://duckdb.org/docs/guides/python/jupyter.html)

### Orchestrating DuckDB with dbt
* [GitHub - dbt-duckdb](https://github.com/jwills/dbt-duckdb)

# Use cases
* Denormalize Geonames tables
  (reference:
  [GitHub - DuckDB - `array_agg()` fucntion](https://github.com/duckdb/duckdb/issues/2607))
  + Retrieve all the records corresponding to a specific IATA code:
```sql
D select distinct ac.geonameid,
         string_agg(an.isoLanguage || '|' || an.alternateName, '=') altname_section
  from allcountries ac
  join altnames an
    on ac.geonameid=an.geonameid
  where an.isoLanguage='iata'
    and an.alternateName='NCE'
  group by ac.geonameid;
┌───────────┬─────────────────┐
│ geonameid │ altname_section │
│   int64   │     varchar     │
├───────────┼─────────────────┤
│   2990440 │ iata|NCE        │
│   6299418 │ iata|NCE        │
└───────────┴─────────────────┘
```

  + Retrieve the corresponding alternate names:
```sql
D select distinct ac.geonameid,
         any_value(ac) geoname_core,
         string_agg(an.isoLanguage || '|' || an.alternateName, '=') altname_section
  from allcountries ac
  join altnames an
    on ac.geonameid=an.geonameid
  where ac.geonameid in (2990440, 6299418)
  group by ac.geonameid;
┌───────────┬──────────────────────┬───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ geonameid │     geoname_core     │                                                                                                    altname_section                                                                            │
│   int64   │ struct(geonameid b…  │                                                                                                        varchar                                                                                │
├───────────┼──────────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│   6299418 │ {'geonameid': 6299…  │ icao|LFMN=iata|NCE=en|Nice Côte d'Azur International Airport=es|Niza Aeropuerto=link|https://en.wikipedia.org/wiki/Nice_C%C3%B4te_d%27Azur_Airport=fr|Aéroport de Nice Côte d'Azur=en|Nice …  │
│   2990440 │ {'geonameid': 2990…  │ en|Nice=es|Niza=ar|نيس==ca|Niça=da|Nice=eo|Nico=et|Nice=fi|Nizza=fr|Nice=he|ניס=id|Nice=it|Nizza=ja|ニース=la|Nicaea=lad|Nisa=lb|Nice=lt|Nica=nb|Nice=nl|Nice=no|Nice=oc|Niça=pl|Nicea=pt|N…  │
└───────────┴──────────────────────┴───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

# Setup
* If not already done so, clone
  [this Git repository](https://github.com/data-engineering-helpers/ks-cheat-sheets):
```bash
mkdir -p ~/dev/ks && \
  git clone https://github.com/data-engineering-helpers/ks-cheat-sheets.git ~/dev/ks/ks-cheat-sheets && \
  cd ~/dev/ks/ks-cheat-sheets
```

## DuckDB on the command-line (CLI)
* On MacOS:
```bash
brew install duckdb
```

## DuckDB Python library
* DuckDB, as a Python library, perfectly works with Jupyter. For the details
  on how to install JupyterLab so that it works with DuckDB, refer to the
  [installation section of the Jupyter with PySpark and DuckDB cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/tree/main/programming/jupyter/jupyter-pyspark-duckdb#initial-setup)
  + The
    [`ipython-notebooks/simple-duckdb.ipynb` Jupyter notebook](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/jupyter/jupyter-pyspark-duckdb/ipython-notebooks/simple-spark-pandas.ipynb)
    features a simple example of DuckDB reading a Parquet file as a standard
	table with SQL. It is as simple as executing the following SQL query:
	`select * from 'data/parquet/user-details.parquet';`

* Simply install with Pip:
```bash
python -mpip install -U pip duckdb
```

* Check that DuckDB works well:
```bash
duckdb programming/jupyter/jupyter-pyspark-duckdb/db.duckdb
```
```sql
D select * from 'programming/jupyter/jupyter-pyspark-duckdb/data/parquet/user-details.parquet';
┌─────────┬──────────┬─────────┬─────────┐
│ User ID │ Username │ Browser │   OS    │
│  int32  │ varchar  │ varchar │ varchar │
├─────────┼──────────┼─────────┼─────────┤
│    1580 │ Barry    │ FireFox │ Windows │
│    5820 │ Sam      │ MS Edge │ Linux   │
│    2340 │ Harry    │ Vivaldi │ Windows │
│    7860 │ Albert   │ Chrome  │ Windows │
│    1123 │ May      │ Safari  │ macOS   │
└─────────┴──────────┴─────────┴─────────┘
D .exit
```

## Integration with S3
* In the DuckDB shell, create a secret with the AWS credential chain (typically works
  with the `awsume` command/tool):
```sql
install https;
load https;
CREATE SECRET secret2 (
    TYPE S3,
    PROVIDER CREDENTIAL_CHAIN
);
```

## Geonames data files
* Reference: http://download.geonames.org/export/dump/

* The goal of this section (Geonames data) is to test DuckDB with bigger
  tables (with smaller tables, other tools such as SQLites would perfectly
  do as well)

* Download the Zip-compressed versions of the main CSV data file,
  named `allCountries.txt` (sized around 360 MB), and the CSV data file
  with alternate names, named `alternateNames.txt` (size of around 160 MB):
```bash
wget http://download.geonames.org/export/dump/allCountries.zip
wget http://download.geonames.org/export/dump/alternateNames.zip
```

* Uncompress the Zip files and remove them:
```bash
unzip allCountries.zip && \rm -f allCountries.zip
unzip alternateNames.zip && \rm -f alternateNames.zip iso-languagecodes.txt
mv al*.txt data/
```

* Check that the CSV input data files have been downloaded
  (the size, uncompressed, is around 2.2 GB):
```bash
ls -lFh data/al*.txt
-rw-r--r-- 1 user group 1.5G Jul 15 15:49 data/allCountries.txt
-rw-r--r-- 1 user group 617M Jul 15 04:19 data/alternateNames.txt
```

* Parse the CSV, transform into Parquet files and create views
  (the size is around 900 MB, which is a gain of 2.5 times)
```bash
./elt-geonames.py 
Number of rows: [(12.400482,), (15.893027,), (15.893027,)]
List of records featuring NCE as the IATA code:
(2990440, 'Nice', 'Nice', 'NCE,...,尼斯', 43.70313, 7.26608, 'P', 'PPLA2', 'FR', None, '93', '06', '062', '06088', 342669, 25, 18, 'Europe/Paris', datetime.date(2023, 2, 13), 'data/csv/allCountries.txt', 6634025, 2990440, 'iata', 'NCE', None, None, None, None, 'data/csv/alternateNames.txt')
(6299418, "Nice Côte d'Azur International Airport", "Nice Cote d'Azur International Airport", "Aéroport de Nice Côte d'Azur,...,니스 코트다쥐르 공항", 43.66272, 7.20787, 'S', 'AIRP', 'FR', None, '93', '06', '062', '06088', 0, 3, 5, 'Europe/Paris', datetime.date(2018, 12, 5), 'data/csv/allCountries.txt', 1888981, 6299418, 'iata', 'NCE', None, None, None, None, 'data/csv/alternateNames.txt')
```

* Check the result on the file-system:
```bash
ls -lFh data/parquet/
-rw-r--r--  1 user  group   648M Jul 16 12:33 allCountries.parquet
-rw-r--r--  1 user  group   245M Jul 16 12:34 alternateNames.parquet
-rw-r--r--  1 user  group   764M Jul 16 12:34 geonames.parquet
```

* Note that the DuckDB itself is not big, as the storage is relying on the
  Parquet files:
```bash
ls -lFh db.duckdb
-rw-r--r--  1 user  group   268K Jul 16 12:34 db.duckdb
```

* Check that everything goes well, by launching DuckDB:
```bash
$ duckdb db.duckdb
```
```sql
```sql
D select count(*)/1e6 as nb from allcountries
union all
select count(*)/1e6 as nb from altnames
union all
select count(*)/1e6 as nb from geonames;
┌───────────┐
│    nb     │
│  double   │
├───────────┤
│ 12.400482 │
│ 15.893027 │
│ 15.893027 │
└───────────┘
D .quit
```
