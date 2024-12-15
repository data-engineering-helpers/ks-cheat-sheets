Cheat Sheet - Unity Catalog
===========================

# Table of Content (ToC)
* [Overview](#overview)
* [References](#references)
  * [Data Engineering helpers](#data-engineering-helpers)
  * [Unity Catalog documentation](#unity-catalog-documentation)
* [Getting started](#getting-started)
  * [Browse the content of the catalog with the CLI](#browse-the-content-of-the-catalog-with-the-cli)
  * [Operate on the tables with DuckDB](#operate-on-the-tables-with-duckdb)
  * [Interact with the UI](#interact-with-the-ui)
* [Installation](#installation)
  * [Clone the Unity Catalog Git repository](#clone-the-unity-catalog-git-repository)
  * [Launch the Unity Catalog server with Java 17](#launch-the-unity-catalog-server-with-java-17)
  * [Launch the Unity Catalog server with docker\-compose](#launch-the-unity-catalog-server-with-docker-compose)
  * [(Optional) Local PostgreSQL database](#optional-local-postgresql-database)
    * [Setup the PostgreSQL connection in the Hibernate property file](#setup-the-postgresql-connection-in-the-hibernate-property-file)
    * [Create the content of the catalog](#create-the-content-of-the-catalog)
  * [DuckDB](#duckdb)
    * [MacOS](#macos)
    * [Linux](#linux)
  * [Launch the UI with JavaScript (JS)](#launch-the-ui-with-javascript-js)
    * [Prerequisites](#prerequisites)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/unity-catalog/README.md)
explains how to install and to use
[Unity Catalog](https://www.unitycatalog.io)
on premises, _e.g._, on a laptop or on a virtual machine (VM).

# References

## Data Engineering helpers
* [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md#unity-catalog-database-and-user)
* [Data Engineering Helpers - Knowledge Sharing - Hive Metastore](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/hive-metastore/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Egeria](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/egeria/README.md)
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box/blob/main/README.md)
* [Material for the Data platform - Data life cycle](https://github.com/data-engineering-helpers/data-life-cycle/blob/main/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Minio](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-storage/minio/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Trino](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/trino/README.md)
* [Data Engineering Helpers - Knowledge Sharing - DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Java world](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/java-world/README.md)
* [Data Engineering Helpers - Knowledge Sharing - JavaScipt (JS) world](https://github.com/data-engineering-helpers/ks-cheat-sheets/tree/main/programming/js-world)

## Unity Catalog documentation
* Home page: https://www.unitycatalog.io
* GitHub page: https://github.com/unitycatalog/unitycatalog
* [Unity Catalog docs](https://docs.unitycatalog.io/)
  * [Unity Catalog docs - Quickstart](https://docs.unitycatalog.io/quickstart/)
  * [Unity Catalog docs - Usage - CLI](https://docs.unitycatalog.io/usage/cli/)
  * [Unity Catalog docs - Deployment - PostgreSQL connection](https://docs.unitycatalog.io/deployment/#example-postgresql-connection)
  * [Unity Catalog docs - Integrations - Spark](https://docs.unitycatalog.io/integrations/unity-catalog-spark/)
  * [Unity Catalog docs - Integrations - DuckDB](https://docs.unitycatalog.io/integrations/unity-catalog-duckdb/)
  * [Unity Catalog docs - Integrations - XTable](https://docs.unitycatalog.io/integrations/unity-catalog-xtable/)

# Getting started

## Browse the content of the catalog with the CLI
* List the catalogs:
```bash
bin/uc catalog list --output json
```
```json
[{"name":"unity","comment":"Main catalog","properties":{},"owner":null,"created_at":1721230405334,"created_by":null,"updated_at":null,"updated_by":null,"id":"f029b870-9468-4f10-badd-630b41e5690d"}]
```

* Get the details of the `unity` catalog:
```bash
bin/uc catalog get --name unity --output json
```
```json
{"name":"unity","comment":"Main catalog","properties":{},"owner":null,"created_at":1721234005334,"created_by":null,"updated_at":1734289209110,"updated_by":null,"id":"f029b870-9468-4f10-badd-630b41e5690d"}
```

* List the schemas:
```bash
bin/uc schema list --catalog unity --output json
```
```json
[{"name":"default","catalog_name":"unity","comment":"Default schema","properties":{},"full_name":"unity.default","owner":null,"created_at":1721234405571,"created_by":null,"updated_at":null,"updated_by":null,"schema_id":"b08dfd57-a939-46cf-b102-9b906b884fae"}]
```

* List the tables:
```bash
bin/uc table list --catalog unity --schema default --output jsonPretty
```
```json
[ {
  "name" : "marksheet",
  "catalog_name" : "unity",
  "schema_name" : "default",
  "table_type" : "MANAGED",
  "data_source_format" : "DELTA",
  "columns" : [ {
    "name" : "id",
    "type_text" : "int",
  ...
  } ],
  "storage_location" : "file://$HOME/some/path/unitycatalog/etc/data/external/unity/default/tables/user_countries/",
  "comment" : "Partitioned table",
  "properties" : { },
  "owner" : null,
  "table_id" : "26ed93b5-9a18-4726-8ae7-c89dfcfea069"
} ]
```

* It should show a few tables. Some details are truncated because of the nested nature of the data.
  To see all the content, you can add `--output jsonPretty` to any command.

* Browse the metadata of one of those tables:
```bash
bin/uc table get --full_name unity.default.numbers --output jsonPretty
```
```json
{
  "name" : "numbers",
  "catalog_name" : "unity",
  "schema_name" : "default",
  "table_type" : "EXTERNAL",
  "data_source_format" : "DELTA",
  "columns" : [ {
    "name" : "as_int",
    "type_text" : "int",
    ...
  } ],
  "storage_location" : "file://$HOME/some/path/unitycatalog/etc/data/external/unity/default/tables/numbers/",
  "comment" : "External table",
  "properties" : {
    "key1" : "value1",
    "key2" : "value2"
  },
  ...
  "table_id" : "32025924-be53-4d67-ac39-501a86046c01"
}
```

* You can see that it is a Delta table. Now, specifically for Delta tables,
  this CLI can print a snippet of the content of a Delta table (powered by
  the [Delta Kernel Java project](https://delta.io/blog/delta-kernel/)).

* List the content of the `numbers` table:
```bash
bin/uc table read --full_name unity.default.numbers --output jsonPretty
```

* List the volumes:
```bash
bin/uc volume list --catalog unity --schema default --output jsonPretty
```
```json
[ {
  "catalog_name" : "unity",
  "schema_name" : "default",
  "name" : "json_files",
  ...
  "volume_type" : "EXTERNAL",
  "storage_location" : "file://$HOME/some/path/unitycatalog/etc/data/external/unity/default/volumes/json_files/",
  "full_name" : "unity.default.json_files"
}, {
  "catalog_name" : "unity",
  "schema_name" : "default",
  "name" : "txt_files",
  ...
  "volume_type" : "MANAGED",
  "storage_location" : "file://$HOME/some/path/unitycatalog/etc/data/managed/unity/default/volumes/txt_files/",
  "full_name" : "unity.default.txt_files"
} ]
```

* Get the details of the (external) `json_files` volume:
```bash
bin/uc volume get --full_name unity.default.json_files --output jsonPretty
```json
```
{
  "catalog_name" : "unity",
  "schema_name" : "default",
  "name" : "json_files",
  ...
  "volume_type" : "EXTERNAL",
  "storage_location" : "file://$HOME/some/path/unitycatalog/etc/data/external/unity/default/volumes/json_files/",
  "full_name" : "unity.default.json_files"
}
```

* Browse the files on the `json_files` volume:
```bash
bin/uc volume read --full_name unity.default.json_files
```txt
```
d.json [file]
c.json [file]
dir1 [directory]
```

* Browse the files on the `txt_files` volume:
```bash
bin/uc volume read --full_name unity.default.txt_files
```txt
```
b.txt [file]
a.txt [file]
```

* Get the details of the (managed) `txt_files` volume:
```bash
bin/uc volume get --full_name unity.default.txt_files --output jsonPretty
```json
```
{
  "catalog_name" : "unity",
  "schema_name" : "default",
  "name" : "txt_files",
  ...
  "volume_type" : "MANAGED",
  "storage_location" : "file://$HOME/some/pathinfra/unitycatalog/etc/data/managed/unity/default/volumes/txt_files/",
  "full_name" : "unity.default.txt_files"
}
```

## Operate on the tables with DuckDB
For operating on tables with DuckDB, [it has to be installed](https://duckdb.org/docs/installation/).
Let's start DuckDB and install a couple of extensions.

* To start DuckDB, run the command `duckdb` command in the terminal.

* Then, in the DuckDB shell, run the following commands:
```bash
install uc_catalog from core_nightly;
load uc_catalog;
install delta;
load delta;
```

* If you have installed these extensions before, you may have to run update extensions
  and restart DuckDB for the following steps to work.

* Now that we have DuckDB all set up, let's try connecting to UC by specifying a secret.
```sql
CREATE SECRET (
      TYPE UC,
      TOKEN 'not-used',
      ENDPOINT 'http://127.0.0.1:8080',
      AWS_REGION 'us-east-2'
 );
```
 
* You should see it print a short table saying `Success = true`.

* Then we attach the unity catalog to DuckDB.
```sql
ATTACH 'unity' AS unity (TYPE UC_CATALOG);
```

* Now we are ready to query. Try the following:
```sql
SHOW ALL TABLES;
SELECT * from unity.default.numbers;
```

* You should see the tables listed and the contents of the numbers table printed.

* To quit DuckDB, press Controll-D (if your platform supports it),
  press Control-C, or use the `.exit` command in the DuckDB shell

## Interact with the UI
* Visit http://localhost:3000
![Unity Catalog UI running locally](/images/data-catalogs/uc-ui.png)

# Installation
* The Unity Catalog service may either be started in containers thanks to Docker Compose,
  or directly with the Java 17 JVM. The following two sections show either of the methods
* The Unity Catalog UI relies on JavaScript (JS)/NodeJS

## Clone the Unity Catalog Git repository
* If not already done so, clone the Git repository of Unity Catalog, and move to the corresponding directory:
```bash
mkdir -p dev/infra
git clone git@github.com:unitycatalog/unitycatalog.git ~/dev/infra/unitycatalog
cd ~/dev/infra/unitycatalog
```

* For convenience, a Shell alias may be specified like
  * For the Java-based installation:
```bash
alias unitycatalogstart='cd ~/dev/infra/unitycatalog; ./bin/start-uc-server'
```
  * For the container-based installation:
```bash
alias unitycatalogstart='cd ~/dev/infra/unitycatalog; docker-compose up'
```

* The Unity Catalog will then be started simply with the `unitycatalogstart` alias in
  a dedicated tab of the Shell terminal, and terminated with the Control-C key

## Launch the Unity Catalog server with Java 17
* See the
  [Java cheat sheet on this Git repository](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/java-world/README.md)
  for how to install/maintain a Java 17 stack on various platforms with
  [SDKMan](https://sdkman.io/), as well as tools like [SBT](https://www.scala-sbt.org/)

* Example of SDK commands to install/upgrade the Java stack (with the
  [Amazon Corretto Java distribution](https://aws.amazon.com/corretto/)):
```bash
sdk update
sdk install java 17.0.13-amzn
sdk default java 17.0.13-amzn
```

* Example of SDK commands to install, or upgrade, SBT:
```bash
sdk update
sdk install sbt
sdk upgrade sbt
```

* Build the JAR package with SBT:
```bash
sbt package
```

* Launch the Unity Catalog (Control-C to quit terminate the service):
```bash
./bin/start-uc-server
```

## Launch the Unity Catalog server with `docker-compose`
* See the
  [Docker cheat sheet on this Git repository](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/infrastructure/docker/README.md)
  for how to install a Docker-compliant desktop tool on various platforms,
  as well as a few plugins like Docker compose and Docker BuildKit

* Launch the Unity Catalog with Docker Compose:
```bash
docker-compose up
```

## (Optional) Local PostgreSQL database
* See also
  [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md#unity-catalog-database-and-user)
  on how to install a PostgreSQL database server locally and how to create the `ucdb` database and the `ucdba` database user.
  * For convenience, the commands to create the `ucdb` database and `ucdba` user are reproduced in the remainder of this sub-section

 * Create on PostgreSQL a `ucdb` database and a `ucdba` user:
```bash
$ psql -h $PG_SVR -U $PG_ADM_USR -d postgres -c "create database ucdb;"
CREATE DATABASE
$ psql -h $PG_SVR -U $PG_ADM_USR -d postgres -c "create user ucdba with encrypted password '<ucdba-pass>'; grant all privileges on database ucdb to ucdba;"
CREATE ROLE
GRANT
$ psql -h $PG_SVR -U $PG_ADM_USR -d ucdb -c "grant all on schema public to ucdba;"
GRANT
```

* Check that the access to the PostgreSQL database works:
```bash
$ psql -h $PG_SVR -U ucdba -d ucdb -c "select 42 as nb;"
 nb 
----
 42
(1 row)
```

* Add the `ucdba` credentials to the local PostgreSQL configuration file:
```bash
echo "localhost:5432:ucdb:ucdba:<ucdba-pass-see-above>" >> ~/.pgpass
chmod 600 ~/.pgpass
```

### Setup the PostgreSQL connection in the Hibernate property file
* Specify the PostgreSQL database credentials as environment variables:
```bash
PG_UC_DB="ucdb"
PG_UC_USR="ucdba"
PG_UC_PWD="<ucdba-pass-see-above>"
```

* Replace, in the Hibernate property file, the H2 database by PostgreSQL details:
```bash
sed -i.bak1 -e 's/org.h2.Driver/org.postgresql.Driver/' etc/conf/hibernate.properties
sed -i.bak2 -e 's|jdbc:h2:file:./etc/db/h2db;DB_CLOSE_DELAY=-1|jdbc:postgresql://localhost:5432/ucdb|' etc/conf/hibernate.properties
cat >> etc/conf/hibernate.properties < _EOF
hibernate.connection.user=ucdba
hibernate.connection.password=ucdba1234
_EOF
```

* Check the resulting Hibernate property file and compare it with
  [the sample on Unity Catalog documentation](https://docs.unitycatalog.io/deployment/#example-postgresql-connection):
```bash
cat etc/conf/hibernate.properties
```

* If everything seems correct, delete the `.bak` files created by the SED commands:
```bash
rm -f etc/conf/hibernate.properties.bak?
```

### Create the content of the catalog
* With the default H2 database, the Git repository comes with a catalog pre-installed.
  With PostgreSQL, the catalog has to be created and configured

* In the remainder of this sub-section, the content comes from the catalog when configured
  with the H2 database, exported into JSON. It is hence used here to recreate the content of
  the catalog when configured with the (initially empty) PostgreSQL database

* Launch the Unity Catalog (UC) server in a dedicated terminal tab (reminder: type Control-C to stop the server):
```bash
./bin/start-uc-server
```

* (In a distinct terminal tab,) use the UC client to create a `unity` catalog:
```bash
./bin/uc catalog create --name unity --comment "Main catalog"
```

* Create a `default` schema for the `unity` catalog:
```bash
./bin/uc schema create --catalog unity --name default --comment "Default schema"
```

* Create the `marksheet` table:
```bash
bin/uc table create --full_name unity.default.marksheet --columns "id int, name string, marks int" --storage_location file://$HOME/some/path/unitycatalog/etc/data/managed/unity/default/tables/marksheet/ --format DELTA --comment "Managed table" --properties "{\"key1\": \"value1\", \"key2\": \"value2\"}"
```

* Create the `marksheet_uniform` table:
```bash
bin/uc table create --full_name unity.default.marksheet_uniform --columns "id int, name string, marks int" --storage_location file:///tmp/marksheet_uniform --format DELTA --comment "Uniform table" --properties "{\"key1\": \"value1\", \"key2\": \"value2\"}"
```

* Create the `numbers` table:
```bash
bin/uc table create --full_name unity.default.numbers --columns "as_int int, as_double double, marks int" --storage_location file://$HOME/some/path/unitycatalog/etc/data/external/unity/default/tables/numbers/ --format DELTA --comment "External table" --properties "{\"key1\": \"value1\", \"key2\": \"value2\"}"
```

* Create the `user_countries` table:
```bash
bin/uc table create --full_name unity.default.user_countries --columns "first_name string, age long, country string" --storage_location file://$HOME/dev/infra/unitycatalog/etc/data/external/unity/default/tables/user_countries/ --format DELTA --comment "Partitioned table" --properties "{\"key1\": \"value1\", \"key2\": \"value2\"}"
```

* Create the `json_files` volume:
```bash
bin/uc volume create --full_name unity.default.json_files --storage_location file://$HOME/some/path/unitycatalog/etc/data/external/unity/default/volumes/json_files/ --comment "External volume"
```

* Create the `txt_files` volume:
```bash
bin/uc volume create --full_name unity.default.txt_files --storage_location file://$HOME/some/path/unitycatalog/etc/data/managed/unity/default/volumes/txt_files/ --comment "Managed volume"
```

## DuckDB
* See also the
  [DuckDB cheat sheet on this Git repository](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/README.md)

### MacOS
* On MacOS, DuckDB may be installed with HomeBrew:
```bash
brew install duckdb
```

### Linux
* See
  [DuckDB installation page for Linux](https://duckdb.org/docs/installation/?version=stable&environment=cli&platform=linux&download_method=direct&architecture=x86_64)

* It would give something like:
```bash
DDB_VER="$(curl -Ls https://api.github.com/repos/duckdb/duckdb/releases/latest | grep 'tag_name' | cut -d':' -f2,2 | cut -d'"' -f2,2)"
curl -L https://github.com/duckdb/duckdb/releases/download/$DDB_VER/duckdb_cli-linux-amd64.zip -o duckdb_cli-linux-amd64.zip
unzip -x duckdb_cli-linux-amd64.zip && rm -f duckdb_cli-linux-amd64.zip
mkdir -p ~/bin
mv duckdb ~/bin
chmod +x ~/bin/duckdb
export PATH="$HOME/bin:$PATH"
```

## Launch the UI with JavaScript (JS)

### Prerequisites
* NodeJS: https://nodejs.org/en/download/package-manager
* Yarn: https://classic.yarnpkg.com/lang/en/docs/install

* Start the UI through Yarn:
```bash
cd ui
yarn install
yarn start
```

