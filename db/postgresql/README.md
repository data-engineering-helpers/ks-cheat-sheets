Cheat Sheet - PostgreSQL
========================

# Table of Content (ToC)
* [Overview](#overview)
* [References](#references)
  * [PostgreSQL](#postgresql)
  * [Linux](#linux)
* [Use cases](#use-cases)
  * [Quick setup for the use cases](#quick-setup-for-the-use-cases)
  * [Create a database and associated user](#create-a-database-and-associated-user)
    * [Guest database and user](#guest-database-and-user)
    * [Unity Catalog database and user](#unity-catalog-database-and-user)
    * [Hive Metastore database and user](#hive-metastore-database-and-user)
    * [MinIO database and user](#minio-database-and-user)
    * [LakeFS database and user](#lakefs-database-and-user)
    * [Airflow database and user](#airflow-database-and-user)
    * [AWS RDS proxy and PostgreSQL database](#aws-rds-proxy-and-postgresql-database)
  * [Import files, create and browse tables](#import-files-create-and-browse-tables)
* [Installation](#installation)
  * [Python](#python)
  * [PySpark](#pyspark)
  * [PostgreSQL clients](#postgresql-clients)
    * [MacOS](#macos)
    * [Linux](#linux-1)
      * [Recent RedHat\-based Linux](#recent-redhat-based-linux)
    * [General](#general)
  * [PostgreSQL server](#postgresql-server)
    * [MacOS](#macos-1)
    * [Linux](#linux-2)
      * [Recent RedHat\-based Linux](#recent-redhat-based-linux-1)
    * [Nginx](#nginx)
  * [PostgreSQL as a managed service with AWS RDS](#postgresql-as-a-managed-service-with-aws-rds)
    * [AWS RDS PostgreSQL database](#aws-rds-postgresql-database)
    * [AWS RDS proxy](#aws-rds-proxy)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md)
explains how to install and to use PostgreSQL server.

# References

## PostgreSQL
* PostgreSQL home page: https://www.postgresql.org

## Linux
* Examples of recent RedHat-based distributions:
  [Amazon Linux 2023](https://aws.amazon.com/linux/amazon-linux-2023/),
  [RedHat Enterprise Linux (RHEL) 9](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9),
  [CentOS Stream 9](https://centos.org/stream9/),
  [Alma Linux 9](https://almalinux.org/),
  [Rocky Linux 9](https://rockylinux.org/)

# Use cases

## Quick setup for the use cases
* Specify a few environment variables
  + For local PostgreSQL server on MacOS:
```bash
$ PG_SVR="localhost"; PG_ADM_USR="$USER"
```
  + For local PostgreSQL server on Linux:
```bash
$ PG_SVR="localhost"; PG_ADM_USR="postgres"
```
  + For AWS RDS PostgreSQL service (set the proxy endpoint to
    the AWS RDS proxy one):
```bash
$ PG_SVR="project-proxy.proxy-someid.us-east-1.rds.amazonaws.com"; PG_ADM_USR="postgres"
```

## Create a database and associated user

### Guest database and user
* Create on PostgreSQL a `guest` database and a `guest` user:
```bash
$ psql -h $PG_SVR -U $PG_ADM_USR -d postgres -c "create database guest;"
CREATE DATABASE
$ psql -h $PG_SVR -U $PG_ADM_USR -d postgres -c "create user guest with encrypted password '<guest-pass>'; grant all privileges on database guest to guest;"
CREATE ROLE
GRANT
$ psql -h $PG_SVR -U $PG_ADM_USR -d guest -c "grant all on schema public to guest;"
GRANT
```

* Check that the access to the PostgreSQL database works:
```bash
$ psql -h $PG_SVR -U guest -c "select 42 as nb;"
 nb 
----
 42
(1 row)
```

### Unity Catalog database and user
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

### Hive Metastore database and user
* Create on PostgreSQL a `metastore` database and a `metastore` user:
```bash
$ psql -h $PG_SVR -U $PG_ADM_USR -d postgres -c "create database metastore;"
CREATE DATABASE
$ psql -h $PG_SVR -U $PG_ADM_USR -d postgres -c "create user metastore with encrypted password '<metastore-pass>'; grant all privileges on database metastore to metastore;"
CREATE ROLE
GRANT
$ psql -h $PG_SVR -U $PG_ADM_USR -d metastore -c "grant all on schema public to metastore;"
GRANT
```

* Check that the access to the PostgreSQL database works:
```bash
$ psql -h $PG_SVR -U metastore -d metastore -c "select 42 as nb;"
 nb 
----
 42
(1 row)
```

### MinIO database and user
* Create on PostgreSQL a `minio` database and a `minio` user:
```bash
$ psql -h $PG_SVR -U $PG_ADM_USR -d postgres -c "create database minio;"
CREATE DATABASE
$ psql -h $PG_SVR -U $PG_ADM_USR -d postgres -c "create user minio with encrypted password '<minio-pass>'; grant all privileges on database minio to minio;"
CREATE ROLE
GRANT
$ psql -h $PG_SVR -U $PG_ADM_USR -d minio -c "grant all on schema public to minio;"
GRANT
```

* Check that the access to the PostgreSQL database works:
```bash
$ psql -h $PG_SVR -U minio -d minio -c "select 42 as nb;"
 nb 
----
 42
(1 row)
```

### LakeFS database and user
* Create on PostgreSQL a `lakefs` database and a `lakefs` user:
```bash
$ psql -h $PG_SVR -U $PG_ADM_USR -d postgres -c "create database lakefs;"
CREATE DATABASE
$ psql -h $PG_SVR -U $PG_ADM_USR -d postgres -c "create user lakefs with encrypted password '<lakefs-pass>'; grant all privileges on database lakefs to lakefs;"
CREATE ROLE
GRANT
$ psql -h $PG_SVR -U $PG_ADM_USR -d lakefs -c "grant all on schema public to lakefs;"
GRANT
```

* Check that the access to the PostgreSQL database works:
```bash
$ psql -h $PG_SVR -U lakefs -d lakefs -c "select 42 as nb;"
 nb 
----
 42
(1 row)
```

### Airflow database and user
* Create on PostgreSQL a `airflow` database and a `airflow` user:
```bash
$ psql -h $PG_SVR -U $PG_ADM_USR -d postgres -c "create database airflow;"
CREATE DATABASE
$ psql -h $PG_SVR -U $PG_ADM_USR -d postgres -c "create user airflow with encrypted password '<airflow-pass>'; grant all privileges on database airflow to airflow;"
CREATE ROLE
GRANT
$ psql -h $PG_SVR -U $PG_ADM_USR -d airflow -c "grant all on schema public to airflow;"
GRANT
```

* Check that the access to the PostgreSQL database works:
```bash
$ psql -h $PG_SVR -U airflow -d airflow -c "select 42 as nb;"
 nb 
----
 42
(1 row)
```

### AWS RDS proxy and PostgreSQL database
* In the AWS console, with the
  [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/),
  create an AWS secret, named like `<project>/db/guest`
* Modify the
  [`project-proxy` RDS proxy](https://us-east-1.console.aws.amazon.com/rds/home?region=us-east-1#proxy:id=project-proxy)
  so as to add the new secret, and save the changes
  + Check on the
    [`project-proxy` RDS proxy page](https://us-east-1.console.aws.amazon.com/rds/home?region=us-east-1#proxy:id=project-proxy)
    the full name of the secret, for instance
    `arn:aws:secretsmanager:us-east-1:1234567890:secret:project/db/guest-BZo8GD`
    for the `guest` user
  + Edit the IAM policy in JSON mode and add that secret full name to the list
    of resources in the IAM policy corresponding to the RDS proxy role
	(see just below)
  + Modify (again) the RDS proxy, even though nothing changes this time.
    That is fine, modifying the RDS proxy triggers a restart and re-reading
	of the secrets
* [AWS console - Policies](https://us-east-1.console.aws.amazon.com/iamv2/home)
    (associated to the IAM role of the proxy)

## Import files, create and browse tables
* List the tables:
```bash
$ psql -h $PG_SVR -U guest -c "\dt"
```

* Describe a given table:
```bash
$ psql -h $PG_SVR -U guest -c "\d mytable"
```

* Execute a specific SQL script:
```bash
$ psql -h $PG_SVR -U guest -f db/postgresql/sql/create-geonames-tables.sql
```

* Load CSV data into a table
  + Download the country information CSV data file from
    [Geonames](https://download.geonames.org/export/dump/):
```bash
$ curl https://download.geonames.org/export/dump/countryInfo.txt -o db/duckdb/data/csv/countryInfo.txt
```
  + Remove the header comments:
```bash
$ tail -n +51 db/duckdb/data/csv/countryInfo.txt > db/duckdb/data/csv/countryInfo.csv
```
  + Parse and load the data into PostgreSQL
    (`<CTRL-V-TAB>` means: on the terminal, press successively the Control-V
	  and the TAB keys):
```bash
$ psql -h $PG_SVR -U guest -c "\copy country_info(iso_alpha2, iso_alpha3, iso_numeric, fips_code, name, capital, areainsqkm, population, continent, tld, currency_code, currency_name, phone, postal_code_format, postal_code_regex, languages, geonameId, neighbours, equivalent_fips_code) from 'db/duckdb/data/csv/countryInfo.csv' delimiter '<CTRL-V-TAB>' csv header;"
```
  
* Display the content of a table:
```bash
$ psql -h $PG_SVR -U guest -c "select iso_alpha2, iso_alpha3, name, capital, continent, currency_code, languages from country_info;"
```

# Installation

## Python
* The Python notebooks and/or scripts make use of some libraries,
  which therefore need to be installed:
```bash
$ python -mpip install -U pip sqlalchemy psycopg2 cloudpathlib[s3] pandas jupyterlab jupysql
```

## PySpark
* Install PySpark:
```bash
$ python -mpip install -U pip sqlalchemy psycopg2 cloudpathlib[s3] pandas jupyterlab jupysql pyspark
```

* In the Shell initialization scripts (_e.g._, `~/.bashrc`), add the following
  setup for Spark-related environment variables:
```bash
$ cat >> ~/.bashrc << _EOF

# Spark
## The following lines are for Spark coming simply from pip install pyspark[connect,sql,pandas_on_spark]
PY_LIBDIR="\$(python -mpip show pyspark|grep "^Location:"|cut -d' ' -f2,2)"
export SPARK_VERSION="\$(python -mpip show pyspark|grep "^Version:"|cut -d' ' -f2,2)"
export SPARK_HOME="\$PY_LIBDIR/pyspark"
export PATH="\$SPARK_HOME/sbin:\$PATH"
export PYSPARK_PYTHON="\$(which python3)"
export PYSPARK_DRIVER_PYTHON="\$(which python3)"

_EOF
 exec bash
```

* Download Spark-related JAR artifacts, required by PySpark:
```bash
$ curl https://repo1.maven.org/maven2/org/postgresql/postgresql/42.6.0/postgresql-42.6.0.jar -o db/postgresql/jars/postgresql-42.6.0.jar
  curl https://repo1.maven.org/maven2/io/delta/delta-core_2.12/2.4.0/delta-core_2.12-2.4.0.jar -o db/postgresql/jars/delta-core_2.12-2.4.0.jar
```

* Setup the PySpark Jupyter kernel
  + Create the directory for the Jupyter kernel:
```bash
$ mkdir -p ~/.local/share/jupyter/kernels/pyspark
```

* Copy the kernel configuration file:
```bash
$ envsubst > ~/.local/share/jupyter/kernels/spark-local/kernel.json < db/postgresql/jupyter/pyspark-kernel.json
```

* Check that the kernel has been added:
```bash
$ jupyter kernelspec list
Available kernels:
  spark-local  ~/.local/share/jupyter/kernels/spark-local
  python3      ~/.pyenv/versions/3.11.4/share/jupyter/kernels/python3
```

## PostgreSQL clients

### MacOS
* On MacOS, the HomeBrew PostgreSQL recipe installs both the server
  and the client tools:
```bash
$ brew install postgresql@15
  psql --version
psql (PostgreSQL) 15.4 (Homebrew)
```

### Linux

#### Recent RedHat-based Linux
* Install PostgreSQL client tool and development packages:
```bash
$ sudo dnf -y install postgresql15 libpq-devel python3-psycopg2
  psql --version
psql (PostgreSQL) 15.0
```

### General
* Specify a few environment variables
  + For local PostgreSQL server on MacOS:
```bash
$ PG_SVR="localhost"; PG_ADM_USR="$USER"
```
  + For local PostgreSQL server on Linux:
```bash
$ PG_SVR="localhost"; PG_ADM_USR="postgres"
```
  + For AWS RDS PostgreSQL service (set the proxy endpoint to
    the AWS RDS proxy one):
```bash
$ PG_SVR="project-proxy.proxy-someid.us-east-1.rds.amazonaws.com"; PG_ADM_USR="postgres"
```

* Add the PostgreSQL credentials to the home configuration:
```bash
$ cat >> ~/.pgpass << _EOF
$PG_SVR:5432:*:$PG_ADM_USR:<admin-passwd-see-below>
$PG_SVR:5432:guest:guest:<guest-passwd-see-above>
_EOF
  chmod 600 ~/.pgpass
```

## PostgreSQL server

### MacOS
* On MacOS, the HomeBrew PostgreSQL recipe installs both the server
  and the client tools:
```bash
$ brew install postgresql@15
  psql --version
psql (PostgreSQL) 15.4 (Homebrew)
```

### Linux

#### Recent RedHat-based Linux
* Install the PostgreSQL server package:
```bash
$ sudo dnf -y install postgresql-server || sudo dnf -y install postgresql15-server
```

>**Note**
The PostgreSQL installation comes with a documentation specific to
RedHat-based Linux OSes. Once the `postgresql-server` is installed with DNF,
the documentation may be browsed on the command-line:
```bash
$ less /usr/share/doc/postgresql*/README.rpm-dist
```

* Initialize the PostgreSQL server:
```bash
$ sudo /usr/bin/postgresql-setup --initdb
```

* Start PostgreSQL as a (SystemD) service:
```bash
$ sudo systemctl start postgresql.service
```

* Check the PostgreSQL (SystemD) service:
```bash
$ sudo systemctl status -l postgresql
```

>**Note**
For more robust installations, the data storage for the PostgreSQL database
may be moved to another disk/partition than the root one. Indeed, it happens
that the root disk/partition gets corrupted, or simply becomes no longer
relevant. An easy way out is to re-install the base image on the root
disk/partition. If all the user accounts and data are on an idependent
disk/partition, then it is fairly straightforward to remount that
disk/partition on the freshly installed OS, and the whole system is back
online in no time.

* Specify the target location of the PostgreSQL database data storage
  (and potentially create the corresponding directory structure):
```bash
$ PG_DATA_DIR="/home/postgres/db"
  sudo mkdir -p $PG_DATA_DIR
```

* Move the storage for the PostgreSQL database
  + Stop the PostgreSQL (SystemD) service:
```bash
$ sudo systemctl stop postgresql
```
  + Alter the PostgreSQL configuration so as to allow access
    from other machines:
```bash
$ sudo sed -i -e "s/^#port = 5432/port = 6543/g" /var/lib/pgsql/data/postgresql.conf
  sudo sed -i -e "s/^#listen_addresses = 'localhost'/listen_addresses = '*'/g" /var/lib/pgsql/data/postgresql.conf
  sudo sed -i -e "s|127.0.0.1/32            ident|0.0.0.0/0            md5|g" /var/lib/pgsql/data/pg_hba.conf
```
  + Deep copy the PostgreSQL storage directory structure onto the new location:
```bash
$ sudo rsync -av --quiet /var/lib/pgsql/ ${PG_DATA_DIR}/
  sudo chown -R postgres.postgres ${PG_DATA_DIR}
  sudo semanage fcontext --add --equal /var/lib/pgsql ${PG_DATA_DIR}
  sudo restorecon -rv ${PG_DATA_DIR}
```
  + Update the SystemD configuration for the PostgreSQL service:
```bash
$ sudo sed -i -e "s|Environment=PGDATA=\(.*\)|Environment=PGDATA=${PG_DATA_DIR}/data|g" /usr/lib/systemd/system/postgresql.service
```
  + Check that the location of the PostgreSQL storage has been correctly set:
```bash
$ systemd_datadir="$(grep "^Environment=PGDATA=" /usr/lib/systemd/system/postgresql.service|cut -d'=' -f3,3)"
  echo "Expected location: $PG_DATA_DIR"
  echo "Actual location: $systemd_datadir"
```
  + Reload the SystemD service configuration:
```bash
$ sudo systemctl daemon-reload
```
  + Start the PostgreSQL (SystemD) service:
```bash
$ sudo systemctl start postgresql
```

* Check that the PostgreSQL (SystemD) service is running correctly:
```bash
$ sudo systemctl status -l postgresql
```

* Log in as the `postgres` Unix user:
```bash
$ sudo su - postgres
```

* Specify a password for the PostgreSQL admin user, also named `postgres`:
```bash
postgres@vm$ psql -c "ALTER USER postgres WITH PASSWORD '<admin-passwd>';"
```

* Log out of the `postgres` Unix user:
```bash
postgres@vm$ exit
logout
```

### Nginx
>**Note**
That step is not strictly necessary. It adds some robustness
and security in the deployment of PostgreSQL (and other services)

>**Note**
If the PostgreSQL database is setup without Nginx, then the server port
may have to be adapted (from 6543 as specified in the above section,
to the default port for PostgreSQL, which is 5432); indeed, when Nginx
is installed, Nginx is the service listening on the PostgreSQL default port
(that is, 5432), where the PostgreSQL service itself listens to the 6543 port
(if installed as specified in the above section)

* If not already done so, install Nginx:
```bash
$ sudo dnf -y install nginx nginx-mod-stream
```

* Install the Nginx reverse-proxy:
```bash
$ sudo mkdir -p /etc/nginx/conf.d
  sudo cp db/postgresql/nginx/conf.d/*.conf /etc/nginx/conf.d/
```

* In the Nginx configuration file (`sudo vi /etc/nginx/nginx.conf`)
  + Add a stream section
    - Spot the `http` block
	- Add, just before it, the following stream section:
```conf

stream {
    # Load modular configuration files from the /etc/nginx/conf.d directory.
    # See http://nginx.org/en/docs/ngx_core_module.html#include
    # for more information.
    include /etc/nginx/conf.d/stream.*.conf;
}

```
  + Add the possible length of fully qualified server names
    - Spot the `types_hash_max_size 2048;` line, in the `http` block
    - Add, just after that latter line, the following line:
```conf
    server_names_hash_bucket_size 100;
```

* Set the SE Linux web server (`httpd_can_network_connect`) boolean:
```bash
$ sudo setsebool -P httpd_can_network_connect 1
```

* Check that the Nginx configuration is good:
```bash
$ sudo nginx -t
$ # sudo nginx -s reload
```

* Enable and start the Nginx as a SystemD service:
```bash
$ sudo systemctl daemon-reload
$ sudo systemctl enable nginx --now
```

* Check that the (SystemD) Nginx service works correctly:
```bash
$ sudo systemctl status -l nginx
```

* Potentially debug with the system journal:
```bash
$ sudo journalctl -xeu nginx.service
```

## PostgreSQL as a managed service with AWS RDS
* That solution is an alternative to the PostgreSQL server

* The password of the admin user, namely `postgres`, is specified when
  installing/creating the AWS RDS PostgreSQL service

### AWS RDS PostgreSQL database
* [AWS console - `project-db` RDS PostgreSQL](https://eu-west-1.console.aws.amazon.com/rds/home?region=eu-west-1#database:id=project-db;is-cluster=false)
* Endpoint: `project-db.someid.us-east-1.rds.amazonaws.com`
* Port: 5342

### AWS RDS proxy
* Documentation:
  + [AWS docs - Using RDS proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)
  + [AWS docs - Managing RDS proxy - Adding a new database user](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-managing.html#rds-proxy-new-db-user)
* [AWS console - `projecy-proxy` proxy to RDS](https://us-east-1.console.aws.amazon.com/rds/home?region=us-east-1#proxy:id=project-proxy)
* Endpoint: [AWS console - `project-proxy` proxy endpoint](https://us-east-1.console.aws.amazon.com/rds/home?region=us-east-1#proxy-endpoint:id=default;proxy=project-proxy)
  + Endpoint address:
    project-proxy.proxy-someid.us-east-1.rds.amazonaws.com
* IAM role:
  `arn:aws:iam::1234567890:role/service-role/rds-proxy-role-1234567890`

