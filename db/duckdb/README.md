Cheat Sheets - DuckDB
=====================

# Table of Content (ToC)
* [Cheat Sheets \- DuckDB](#cheat-sheets---duckdb)
* [Overview](#overview)
* [Use cases](#use-cases)
* [Setup](#setup)
  * [DuckDB on the command\-line (CLI)](#duckdb-on-the-command-line-cli)
  * [DuckDB Python library](#duckdb-python-library)
  * [Geonames data files](#geonames-data-files)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/README.md)
explains how to install and to use DuckDB.

DuckDB allows to process and analyze rather big data files on local
computers or rather small virtual machines (VM).

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

## DuckDB on the command-line (CLI)
* On MacOS:
```bash
brew install duckdb
```

## DuckDB Python library
* Simply install with Pip:
```bash
python -mpip install -U pip duckdb
```

## Geonames data files
* Reference: http://download.geonames.org/export/dump/

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
