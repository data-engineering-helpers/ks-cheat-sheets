Cheat Sheet - Cloud - Amazon Web Services (AWS)
===============================================

# Table of Content (ToC)
* [Overview](#overview)
* [References](#references)
  * [Data Engineering helpers](#data-engineering-helpers)
* [Installation](#installation)
  * [AWS account](#aws-account)
  * [AWS Command\-Line Interface (CLI)](#aws-command-line-interface-cli)
    * [MacOS](#macos)
    * [Linux](#linux)
    * [Configuration for the AWS CLI](#configuration-for-the-aws-cli)
  * [AWSume commad\-line utility](#awsume-commad-line-utility)
  * [SAML\-to\-AWS (saml2aws) command\-line utility](#saml-to-aws-saml2aws-command-line-utility)
    * [MacOS](#macos-1)
    * [Linux](#linux-1)
    * [Configure SAML\-to\-AWS](#configure-saml-to-aws)
    * [Typical end\-to\-end example](#typical-end-to-end-example)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/clouds/aws/README.md)
explains how to use and interact with Amazon Web Services (AWS), that is,
installing AWS command-line utilities such as `aws`, `saml2aws` and `awsume`
and interacting with remote AWS services (_e.g._,
[Identity and Access Management (IAM)](https://aws.amazon.com/iam/),
[S3](https://aws.amazon.com/s3/), [Glue](https://aws.amazon.com/glue/),
[EC2](https://aws.amazon.com/ec2/),
[Athena](https://aws.amazon.com/athena/), [RDS](https://aws.amazon.com/rds/),
[Redshift](https://aws.amazon.com/redshift/),
[CodeArtifact](https://aws.amazon.com/codeartifact/),
[Elastic Container Registry (ECR)](https://aws.amazon.com/ecr/),
[Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/),
[Lambda](https://aws.amazon.com/lambda/),
[Elastic Map Reduce (EMR)](https://aws.amazon.com/emr/),
[Managed Workflows for Apache Airflow (MWAA)](https://aws.amazon.com/managed-workflows-for-apache-airflow/),
[Managed Streaming for Apache Kafka (MSK)](https://aws.amazon.com/msk/)).

# References

## Data Engineering helpers
* [Architecture principles for data engineering pipelines on the Modern Data Stack (MDS)](https://github.com/data-engineering-helpers/architecture-principles)
* [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Kubernetes (k8s)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/k8s/README.md)

# Installation

## AWS account
* If not already done so, create an account on the
  [AWS web console](https://console.aws.amazon.com). For the sake of
  illustration, the following fake account ID will be used
  in the remainder of the documentation:
  + Account ID: `012345678901`
	
* If not already done so, create an access key
  + Visit the [AWS web console](https://console.aws.amazon.com/), click on your
    name on the top-right corner, and select the
    [Security credentials section](https://us-east-1.console.aws.amazon.com/iamv2/home#/security_credentials)
  + Click on the "Create access key" button
  + Write down a copy of both the access key ID (`aws_access_key_id`)
    and the corresponding secret access key (`aws_secret_access_key`).
	That latter is hown just once, and is then no more accessible: it is
	therefore important to write it down in a safe place at the creation time
	of the access key
* For the sake of illustration, the following fake access key will be used
  in the remainder of the documentation:
  + AWS Access Key ID: `AKSomeKey05`
  + AWS Secret Access Key: `xyGL09SomeSecretKkz89m`

## AWS Command-Line Interface (CLI)

### MacOS
* Install the AWS CLI with HomeBrew:
```bash
$ brew install awscli
```

### Linux
* Install the AWS Command-Line Interface (CLI) with ready-to-use AWS tar-ball:
```bash
$ mkdir -p ~/tmp/awscliv2 && \
  curl -Ls https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip \
       -o ~/tmp/awscliv2/awscliv2.zip && \
  pushd ~/tmp/awscliv2 && \
  unzip -qq awscliv2.zip && \
  rm -f awscliv2.zip
$ sudo ./aws/install # --update
$ popd && \
  rm -rf ~/tmp/awscliv2
$ aws --version
aws-cli/2.13.33 Python/3.11.6 Linux/4.18.0-521.el8.x86_64 exe/x86_64.centos.8 prompt/off
```

### Configuration for the AWS CLI
* Retrieve the access key details and create the configuration and credential
  files, thanks to the `aws configure` one-time command:
```bash
$ aws configure
AWS Access Key ID [None]: AKSomeKey05
AWS Secret Access Key [None]: xyGL09SomeSecretKkz89m
Default region name [None]: eu-west-1
Default output format [None]: json
```
* Check that the AWS CLI now works correctly
  + Check the caller ID (it should correspond to the access key
    and AWS account):
```bash
$ aws sts get-caller-identity
{
    "UserId":  "012345678901",
    "Account": "012345678901",
    "Arn": "arn:aws:iam::440510661531:root"
}
```
  + List the content of some S3 public buckets:
```bash
$ aws s3 ls --human --summarize s3://nyc-tlc/
                           PRE csv_backup/
                           PRE misc/
                           PRE opendata_repo/
                           PRE trip data/
$ aws s3 ls --human --summarize --recursive s3://optd/latest/
2023-09-27 18:42:25    0 Bytes latest/
2023-09-27 18:42:44    1.3 MiB latest/optd_airline_por.csv

Total Objects: 2
   Total Size: 1.3 MiB
```
* The configuration has created two configuration files in the `~/.aws/`
  local directory, namely `config` and `credentials`:
```bash
$ ls -lFh ~/.aws/
total 8.0K
-rw------- 1 user group  44 Nov  9 15:39 config
-rw------- 1 user group 116 Nov  9 15:39 credentials
```
* The `credentials` file has a `[default]` section, named profile,
  with the access key ID and the secret access key
* Other access keys may simply be added with associated specific profiles,
  for instance the following command will create a `demo` profile:
```bash
$ cat >> ~/.aws/credentials << _EOF

[demo]
aws_access_key_id = AKSomeKey05
aws_secret_access_key = xyGL09SomeSecretKkz89m
_EOF
```

## AWSume commad-line utility
* AWSume is a Python-based utility. Simply install it with Python:
```bash
$ python -mpip install -U awsume
```
* Reset the Shell:
```bash
$ exec bash # zsh
```
* Configure AWSume:
```bash
$ awsume-configure
===== Setting up bash =====
Wrote alias to ~/.bash_profile
Wrote autocomplete script to ~/.bash_profile
===== Setting up zsh =====
Wrote alias to /home/build/.zshenv
Wrote autocomplete script to ~/.zshenv
Wrote zsh function to ~/.awsume/zsh-autocomplete/_awsume
===== Finished setting up =====
```
* Reset the Shell:
```bash
$ exec bash # zsh
```
* Check the version:
```bash
$ awsume --version
4.5.3
```
* Assume a role/profile referenced in the `~/.aws/credentials` file and
  use the AWS services (_e.g._, S3 here)
  + Default role/profile:
```bash
$ awsume default
$ aws sts get-caller-identity
{
    "UserId":  "012345678901",
    "Account": "012345678901",
    "Arn": "arn:aws:iam::440510661531:root"
}
```
  + "Demo" role/profile:
```bash
$ awsume demo
$ aws sts get-caller-identity
{
    "UserId":  "012345678901",
    "Account": "012345678901",
    "Arn": "arn:aws:iam::440510661531:root"
}
```

## SAML-to-AWS (`saml2aws`) command-line utility
* Some corporations use
  [Security Assertion Markup Language](https://en.wikipedia.org/wiki/Security_Assertion_Markup_Language)
  as the way to login to/authenticate with the AWS services
* Usually, the user has access to a selection of roles, at the login time
  on the AWS services. The SAML protocol allows the user to select one of
  those roles at login time. If the role needs to be changed, a new login
  must be performed
* Natively, the SAML protocol is triggered via a URL similar to
  https://idp.example.com/idp/startSSO.ping?PartnerSpId=urn:amazon:webservices
  where the first part of the URL corresponds to the
  [Identity Provider (IdP)](https://en.wikipedia.org/wiki/Identity_provider_(SAML))
  and the second part corresponds to the
  [service provider](https://en.wikipedia.org/wiki/Service_provider_(SAML)),
  AWS here
* The open source `saml2aws` command-line utility allows to go through
  that SAML-powered login process from the command-line, that is, without
  having to open a web browser
* Once the login has been performed and a role has been selected, the user
  has to assume the `saml` role (see below) with the `awsume` command
  (see above)

### MacOS
* Install the AWS CLI with HomeBrew:
```bash
$ brew install saml2aws
```

### Linux
* Install the `saml2aws` command-line interface (CLI) with ready-to-use
  tar-ball:
```bash
$ SAML2AWS_VER=$(curl -Ls https://api.github.com/repos/Versent/saml2aws/releases/latest | grep 'tag_name' | cut -d'v' -f2 | cut -d'"' -f1) && \
  curl -Ls \
       https://github.com/Versent/saml2aws/releases/download/v${SAML2AWS_VER}/saml2aws_${SAML2AWS_VER}_linux_amd64.tar.gz -o saml2aws.tar.gz && \
       tar zxf saml2aws.tar.gz && rm -f saml2aws.tar.gz README.md LICENSE.md
  sudo mv -f saml2aws /usr/local/bin/ && sudo chmod 775 /usr/local/bin/saml2aws
```

### Configure SAML-to-AWS
* If not already done so, create the configuration file for SAML-to-AWS:
```bash
$ saml2aws configure
? Please choose a provider: Ping # choose your own relevant provider
? AWS Profile saml # any name may be picked it
? URL https://idp.example.com
? Username USERID
```
* It should have created the `~/.saml2aws` file

### Typical end-to-end example
* Login with AWS and select a role:
```bash
$ saml2aws login # --force
```
* Assume the `saml` role:
```bash
$ awsume saml
```
* Check the AWS role:
```bash
$ aws sts get-caller-identity
```
* Make use of AWS services:
```bash
$ aws s3 ls --human s3://nyc-tlc/
```

