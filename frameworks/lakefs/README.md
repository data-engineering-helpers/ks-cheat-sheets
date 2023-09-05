Cheat Sheet - LakeFS
====================

# Table of Content (ToC)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/lakefs/README.md)
explains how to install and to use LakeFS on premises, _e.g._, on a laptop
or on a virtual machine (VM).

> LakeFS is Data Version Control (Git for Data)
>
> lakeFS is an open-source tool that transforms object storage into a Git-like
> repository. It enables to manage your data lake the way code is managed.
>
> With lakeFS you can build repeatable, atomic, and versioned data lake
> operations - from complex ETL jobs to data science and analytics.
>
> lakeFS supports AWS S3, Azure Blob Storage, and Google Cloud Storage
> as its underlying storage service. It is API compatible with S3 and works
> seamlessly with all modern data frameworks such as Spark, Hive, AWS Athena,
> DuckDB, and Presto.

# References

## Minio
* [Minio](https://min.io/) is a dependency for on-premise deployment
* Install and deploy Minio on MacOS:
  https://min.io/docs/minio/macos/operations/installation.html
* Install and deploy containerized Minio:
  https://min.io/docs/minio/container/operations/installation.html

## LakeFS
* GitHub repository: https://github.com/treeverse/lakeFS
* End-to-end Write-Audit-Publish (WAP) pattern with LakeFS:
  https://lakefs.io/blog/write-audit-publish-with-lakefs/

### Installation
* On premises deployment: https://docs.lakefs.io/howto/deploy/onprem.html
* Deploy LakeFS on AWS: https://docs.lakefs.io/howto/deploy/aws.html

# Installation

## Minio

### MacOS
* Minio, with the Minio client, may be installed on MacOS with HomeBrew:
```bash
$ brew install minio/stable/minio
  brew install minio/stable/mc
```

* Create a default environment file:
```bash
% sudo mkdir -p /etc/default
  sudo chown $USER /etc/default
  cat > /etc/default/minio << _EOF
# MINIO_ROOT_USER and MINIO_ROOT_PASSWORD sets the root account for the MinIO server.
# This user has unrestricted permissions to perform S3 and administrative API operations on any resource in the deployment.
# Omit to use the default values 'minioadmin:minioadmin'.
# MinIO recommends setting non-default values as a best practice, regardless of environment

MINIO_ROOT_USER=myminioadmin
MINIO_ROOT_PASSWORD=minio-secret-key-change-me

# MINIO_VOLUMES sets the storage volume or path to use for the MinIO server.

MINIO_VOLUMES="/mnt/data"

# MINIO_SERVER_URL sets the hostname of the local machine for use with the MinIO Server
# MinIO assumes your network control plane can correctly resolve this hostname to the local machine

# Uncomment the following line and replace the value with the correct hostname for the local machine and port for the MinIO server (9000 by default).

#MINIO_SERVER_URL="http://minio.example.net:9000" 
_EOF
```

* Copy the MacOS service plist file to the place where Minio was installed:
```bash
$ BREW_PFX="$(brew --prefix)"
  MINIO_DIR="$(brew info minio|grep "^$BREW_PFX"|cut -d' ' -f1,1)"
  curl https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/lakefs/etc/homebrew.mxcl.minio.plist -o $BREW_DIR/homebrew.mxcl.minio.plist
```
