Cheat Sheet - Minio
===================

# Table of Content (ToC)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/minio/README.md)
explains how to install and to use Minio service on premises, _e.g._,
on a laptop or on a virtual machine (VM).

> MinIO is a high-performance, S3 compatible object store.
> It is built for large scale AI/ML, data lake and database workloads.
> It is software-defined and runs on any cloud or on-premises infrastructure.

# References

## Data Engineering helpers
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box/blob/main/README.md)
* [Material for the Data platform - Data life cycle](https://github.com/data-engineering-helpers/data-life-cycle/blob/main/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Minio](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/minio/README.md)
* [Data Engineering Helpers - Knowledge Sharing - LakeFS](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/lakefs/README.md)

## Minio
* Minio home page: https://min.io/
* Minio GitHub repository: https://github.com/minio/minio/

### Installation of Minio
* [Minio doc - Install and deploy Minio on MacOS](https://min.io/docs/minio/macos/operations/installation.html)
* [Minio doc - Install and deploy Minio on Linux](https://min.io/docs/minio/linux/operations/installation.html)
* [Minio doc - Install and deploy containerized Minio](https://min.io/docs/minio/container/operations/installation.html)
* [Minio doc - Configure Nginx proxy for MinIO Server](https://min.io/docs/minio/linux/integrations/setup-nginx-proxy-with-minio.html)

### Use Minio with standard client tools
* [Minio doc - AWS CLI with MinIO Server](https://min.io/docs/minio/linux/integrations/aws-cli-with-minio.html)

## Client tools
* Cloudpathlib: https://cloudpathlib.drivendata.org

# Installation

## MacOS
* Minio, with the Minio client, may be installed on MacOS with HomeBrew:
```bash
$ brew install minio/stable/minio
  brew install minio/stable/mc
```

* Create a default configuration file:
```bash
% sudo mkdir -p /etc/default
  sudo chown $USER /etc/default
  curl https://raw.githubusercontent.com/data-engineering-helpers/ks-cheat-sheets/main/frameworks/minio/etc/minio -o /etc/default/minio
```

* In that new Minio configuration file, adjust the `MINIO_VOLUMES`,
  administrative user and password values:
```bash
$ vi /etc/default/minio
```

* If, for some reason, HomeBrew does not install the Minio service (specified
  with a Plist file), copy the
  [MacOS service plist file](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/minio/etc/homebrew.mxcl.minio.plist)
  to the place where Minio was installed (that solution was documented
  as a
  [GitHub issue on Minio repository](https://github.com/minio/minio/issues/16382)):
```bash
$ export BREW_PFX="$(brew --prefix)"
  export MINIO_DIR="$(brew info minio|grep "^$BREW_PFX"|cut -d' ' -f1,1)"
  export MINIO_VOLUMES="$(grep "^MINIO_VOLUMES=" /etc/default/minio | cut -d'=' -f2,2 | sed -e 's/"//g')"
  curl https://raw.githubusercontent.com/data-engineering-helpers/ks-cheat-sheets/main/frameworks/minio/etc/homebrew.mxcl.minio.plist -o homebrew.mxcl.minio.plist.in
  envsubst < homebrew.mxcl.minio.plist.in > $MINIO_DIR/homebrew.mxcl.minio.plist
```

* Start the Minio service:
```bash
$ brew services start minio
```

* The Minio data lake is now accessible through http://localhost:9090/

* Specify an alias for the Minio service for the Minio client:
```bash
$ . /etc/default/minio
  mc alias set myminio http://localhost:9000 $MINIO_ROOT_USER $MINIO_ROOT_PASSWORD
```

## Linux
TBC

## General
* Create access key pair on http://localhost:9000/access-keys
  and take note of it. That key pair will be required for client tools
  of the Minio service, such as the AWS CLI (see the
  [AWS CLI section below](#aws-cli)) or LakeFS (see for instance the
  [Knowledge Sharing - LakeFS cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/lakefs/README.md)).

* Create some content
  + Create some buckets and folders:
```bash
$ mc mb myminio/bronze/geonames
  mc mb myminio/silver/geonames
  mc mb myminio/gold/geonames
```
  + Copy some Parquet data files (_e.g._, copy the Parquet files resulting from
    launching the
	[EL script](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/elt-geonames.py)
	in the [DuckDB cheat sheet folder](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/)):
```bash
$ mc cp db/duckdb/data/parquet/al*.parquet myminio/bronze/geonames
```

* Browse the content:
```bash
$ mc ls -r --summarize myminio/bronze
```

## Minio client tools

### AWS CLI
* Create a profile for Minio:
```bash
$ aws configure --profile minio
AWS Access Key ID [None]: <minio-access-key-id>
AWS Secret Access Key [None]: <minio-secret-access-key>
Default region name [None]: us-east-1
Default output format [None]: json
```

* Specify the S3 protocol version in the AWS CLI Minio profile:
```bash
$ aws configure --profile minio set s3.signature_version s3v4
```

* Specify the endpoint as part of the AWS CLI Minio profile:
```bash
$ aws configure --profile minio set endpoint_url http://localhost:9000
```

* List the buckets within the Minio service:
```bash
$ aws --profile minio --endpoint-url http://localhost:9000 s3 ls
2023-09-05 19:30:02 bronze
2023-09-05 19:30:08 gold
2023-09-05 21:39:50 silver
```

* Browse the content of a given bucket within the Minio service:
```bash
$ aws --profile minio s3 ls --summarize --human --recursive s3://bronze
2023-09-05 21:40:08    0 Bytes geonames/
2023-09-05 21:43:22  648.0 MiB geonames/allCountries.parquet
2023-09-05 21:43:20  244.7 MiB geonames/alternateNames.parquet

Total Objects: 3
   Total Size: 892.7 MiB
```

* In order to avoid having to repeat the AWS CLI profile every time, `awsume`
  may be used
  + If not already done so, install `awsume` (technically, it is a Python
    module) and configure it:
```bash
$ python -mpip install -U pip awsume
  awsume-configure
```
  + Add an alias for `awsume` in the Shell initialization script, and source
    the Shell aliases:
```bash
$ cat >> ~/.bash_aliases << _EOF

# AWSume
alias awsume="source \\\$(pyenv which awsume)"
alias awsumeminio="awsume minio; export AWS_ENDPOINT_URL=\"http://localhost:9000\""

_EOF
 . ~/.bash_aliases
```
  + Switch to the `minio` profile:
```bash
$ awsume minio
```
  + From then, AWS CLI may be used without specifying the profile:
```bash
$ aws s3 ls --summarize --human --recursive s3://bronze
2023-09-05 21:40:08    0 Bytes geonames/
2023-09-05 21:43:22  648.0 MiB geonames/allCountries.parquet
2023-09-05 21:43:20  244.7 MiB geonames/alternateNames.parquet

Total Objects: 3
   Total Size: 892.7 MiB
```

### Python SDK

#### Cloudpathlib
* If not already done so, install the
  [Cloudpathlib module](https://cloudpathlib.drivendata.org):
```bash
$ python -mpip install -U pip cloudpathlib[s3]
```

#### Sample code
* A simple Jupyter notebook showcases how to browse data files from the
  Minio Bronze bucket. Just open
  http://localhost:8889/lab/tree/ipython-notebooks/lakefs-browse.ipynb
  after starting Jupyter Lab locally:
```bash
$ jupyter lab frameworks/minio --port 8889 --allow-root --no-browser --ip 0.0.0.0 --IdendityProvider.token=
```

* A
  [simple Python script](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/minio/python/minio-browse.py)
  allows to browse the same Minio Bronze bucket:
```bash
$ ./frameworks/minio/python/minio-browse.py
s3://bronze/geonames/allCountries.parquet
s3://bronze/geonames/alternateNames.parquet
```

* The corresponding Python code is:
```python
import os
from cloudpathlib import CloudPath

geo_dir = CloudPath("s3://bronze/geonames")
for f in geo_dir.glob("**/*.parquet"):
    print(f)
```

