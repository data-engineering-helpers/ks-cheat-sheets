Cheat Sheet - DuckDB
====================

# Table of Content (ToC)
* [Overview](#overview)
  * [References](#references)
    * [DuckDB in Jupyter](#duckdb-in-jupyter)
  * [A few DuckDB extra features](#a-few-duckdb-extra-features)
    * [Windowing with DuckDB](#windowing-with-duckdb)

* [Use cases](#use-cases)
* [Public catalogs](#public-catalogs)
  * [Boring panda](#boring-panda)
  * [Buz Hive](#buz-hive)
    * [BlueSky data](#blueSky-data)
    * [Foursquare data](#foursquare-data)
    * [GeoIP](#geoip)
    * [NYC taxis](#nyc-taxis)
* [Setup](#setup)
  * [Clone this Git repository](#clone-this-git-repository)
  * [DuckDB on the command\-line (CLI)](#duckdb-on-the-command-line-cli)
    * [MacOS](#macos)
    * [Linux](#linux)
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

### A few DuckDB extra features

#### Windowing with DuckDB
* Gettaing started with Windowing: https://duckdb.org/2021/10/13/windowing.html
* Reference documentation: https://duckdb.org/docs/sql/functions/window_functions.html
* Catching up with Windowing (in Feb. 2025): https://duckdb.org/2025/02/10/window-catchup.html
* Fast moving holistic aggregates: https://duckdb.org/2021/11/12/moving-holistic.html

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

# Public catalogs

## Boring panda
* Home page: https://catalog.boringdata.io/dashboard/
* Article:
  * Link to the article: https://juhache.substack.com/p/0-data-distribution
  * Date: Dec. 2024
  * Author: Julien Hurault
* [Getting started](https://catalog.boringdata.io/dashboard/get_started/duckdb/)
  * In the DuckDB shell:
```sql
.shell curl https://catalog.boringdata.io/start
```
  * Follow the instructions given as a result (the secret/credentials step
  is not reproduced here):
```sql
load iceberg;
attach 'https://catalog.boringdata.io/catalog' as boringdata;
```
  * Start exploring data:
```sql
select * from boringdata.metadata.catalog;
show all tables;
```

## Buz Hive
* Overview: Buz Hive is a collection of DuckDB-compatible data catalogs
  with public data sets, stored in public R2 buckets on CloudFare
* Home page: https://catalog.buz.dev/
* Author?: Jake Thomas
  ([Jake Thomas on LinkedIn](https://www.linkedin.com/in/jake-thomas/),
  [Jake Thomas on BlueSky](https://bsky.app/profile/jakthom.bsky.social),
  [Jake Thomas on GitHub](https://github.com/jakthom))

### BlueSky data
* Home page: https://catalog.buz.dev/datasets/bluesky/jetstream
* Overview: The Bluesky dataset consists of the last 1M records
  from Bluesky's Jetstream
* Getting started:
  * In the DuckDB shell, bind to the BlueSky data catalog (there is no need
  for credentials here):
```sql
attach 'https://hive.buz.dev/bluesky/catalog' as bluesky;
```
  * Start exploring data:
```sql
show all tables;
select count(*)/1e6 as nb_rows from bluesky.jetstream;
select * from bluesky.jetstream limit 10;
```

* David Jayatillake
  ([David Jayatillake on LinkedIn](https://www.linkedin.com/in/david-jayatillake/),
  [David Jayatillake on Substack](https://substack.com/@davidsj)),
  as part of
  [his exploration of SQLMesh as an alternative to dbt](https://davidsj.substack.com/p/sqlmesh-migrate),
  has setup a Git repository to expose BlueSky data
  * Article by David Jayatillake:
    https://davidsj.substack.com/p/sqlmesh-init-duckdb
  * See also
    [GitHub - Data Engineering Helpers - KS - SQLMesh - Migrate](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/README.md#sqlmesh---migrate)
  * Clone the Git repository and move into it:
```bash
mkdir -p ~/dev/infra
git clone https://github.com/djayatillake/bluesky-data ~/dev/infra/bluesky-data
cd ~/dev/infra/bluesky-data
```

### Foursquare data
* Home page: https://catalog.buz.dev/datasets/foursquare/places
* Overview: OSS Foursquare Places database
  * 100 millions of rows for the `places` table
* Getting started:
  * In the DuckDB shell, bind to the Foursquare data catalog (there is no need
  for credentials here):
```sql
attach 'https://hive.buz.dev/foursquare' as foursquare;
```
  * Start exploring data:
```sql
show all tables;
select count(*)/1e6 as nb_rows from foursquare.places;
select * from foursquare.categories limit 10;
select * from foursquare.places limit 10;
```

### GeoIP
* Home page: https://catalog.buz.dev/datasets/ipinfo/geoip
* Overview: Geoip database from ipinfo.io
  * 2 millions of rows for the `country` table
* Getting started:
  * In the DuckDB shell, bind to the GeoIP data catalog (there is no need for credentials here):
```sql
attach 'https://hive.buz.dev/ipinfo' as geoip;
```
  * Start exploring data:
```sql
show all tables;
select count(*)/1e6 as nb_rows from geoip.country;
select * from bluesky.jetstream limit 10;
```

### NYC taxis
* Home page: https://catalog.buz.dev/datasets/nyc.gov/taxi
* Overview: The NYC taxi rides dataset consists of all taxi rides for the month of October 2024
  * 30 millions of rows for the `yellow_trips` table
* Getting started:
  * In the DuckDB shell, bind to the GeoIP data catalog (there is no need for credentials here):
```sql
attach 'https://hive.buz.dev/nyc_taxi' as taxi;
```
  * Start exploring data:
```sql
show all tables;
select count(*)/1e6 as nb_rows from taxi.yellow_trips;
select * from taxi.yellow_trips limit 10;
```

# Setup
* See also https://duckdb.org/docs/installation

* DuckDB may be installed through the native packaging utility (for instance,
  on MacOS, HomeBrew) or through one of the programming stack utilities
  (for instance, Pip for the Python stack)
  * Most of these methods produce a all-in-one binary artifact,
    named `duckdb`, which may be used directly and which does not rely
	on any other dependency (that is, they are all-in-one)
  * All those binary artifacts are independent from one another
    and have to be updated independently

## Clone this Git repository
* (Optionally,) If not already done so, clone
  [this Git repository](https://github.com/data-engineering-helpers/ks-cheat-sheets):
```bash
mkdir -p ~/dev/ks && \
  git clone https://github.com/data-engineering-helpers/ks-cheat-sheets.git ~/dev/ks/ks-cheat-sheets && \
  cd ~/dev/ks/ks-cheat-sheets
```

## DuckDB on the command-line (CLI)

### MacOS
* Use HomeBrew to install DuckDB:
```bash
brew install duckdb
```

### Linux
* Install the executable corresponding to the CPU architecture directly:
```bash
mkdir -p ~/bin
architecture="$(uname -m|sed 's/arm/aarch/')"
DUCK_VER="$(curl -Ls https://api.github.com/repos/duckdb/duckdb/releases/latest | grep 'tag_name' | cut -d'v' -f2,2 | cut -d'"' -f1,1)"
curl -L https://github.com/duckdb/duckdb/releases/download/v$DUCK_VER/duckdb_cli-linux-$architecture.zip -o duckdb_cli.zip && \
  unzip duckdb_cli.zip && rm -f unzip duckdb_cli.zip && \
  chmod +x duckdb && mv duckdb ~/bin/
```

* If the local binary directory is not in the `PATH` environment variable,
  just add something like the following lines in your Shell setup script
  (_e.g._, `~/.bashrc` or `~/.zshrc`):
```bash
# DuckDB - See also https://duckdb.org/docs/installation
PATH="$HOME/bin:$PATH"; export PATH
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
