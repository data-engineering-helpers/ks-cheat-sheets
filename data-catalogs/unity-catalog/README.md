Cheat Sheet - Unity Catalog
===========================

# Table of Content (ToC)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/unity-catalog/README.md)
explains how to install and to use
[Unity Catalog](https://www.unitycatalog.io)
on premises, _e.g._, on a laptop or on a virtual machine (VM).

# References

## Data Engineering helpers
* [Data Engineering Helpers - Knowledge Sharing - Hive Metastore](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/hive-metastore/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Egeria](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/egeria/README.md)
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box/blob/main/README.md)
* [Material for the Data platform - Data life cycle](https://github.com/data-engineering-helpers/data-life-cycle/blob/main/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Minio](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-storage/minio/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Trino](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/trino/README.md)
* [Data Engineering Helpers - Knowledge Sharing - DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Java world](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/java-world/README.md)

## Unity Catalog documentation
* Home page: https://www.unitycatalog.io
* GitHub page: https://github.com/unitycatalog/unitycatalog

# Getting started

## Operate on Delta tables with the CLI
* List the tables:
```bash
bin/uc table list --catalog unity --schema default
```

It should show a few tables. Some details are truncated because of the nested nature of the data.
To see all the content, you can add `--output jsonPretty` to any command.

* Next, let's get the metadata of one of those tables:
```bash
bin/uc table get --full_name unity.default.numbers
```

You can see that it is a Delta table. Now, specifically for Delta tables,
this CLI can print a snippet of the contents of a Delta table (powered by
the [Delta Kernel Java project](https://delta.io/blog/delta-kernel/)).
Let's try that:
```bash
bin/uc table read --full_name unity.default.numbers
```

## Operate on Delta tables with DuckDB
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

# Installation
* The Unity Catalog service may either be started in containers thanks to Docker Compose,
  or directly with the Java 17 JVM. The following two sections show either of the methods

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

## Java 17
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

## DuckDB

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

