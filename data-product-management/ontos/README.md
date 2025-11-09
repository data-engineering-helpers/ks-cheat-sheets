Cheat Sheet - Data Product Management - Ontos
=============================================

# Table of Content (ToC)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-product-management/ontos/README.md)
explains how to install and to use
[Ontos](https://github.com/larsgeorge/ontos).

* The Ontos frontend (based on React and TypeScript) and backend (based on FastAPI)
  applications may run locally, on a laptop, or on a virtual machine (VM)
* However, those applications connect and interact with
  [Unity Catalog on a DataBricks](https://www.databricks.com/product/unity-catalog)
  workspace (it is not sure, at this stage, that it can integrate with
  the open source version of [Unity Catalog](https://www.unitycatalog.io/))
* Ontos requires a
  [PostgreSQL database](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/)
  to store its state. For production-ready deployments,
  [Lakebase](https://www.databricks.com/product/lakebase) is to be used

# References

## Data Engineering helpers
* [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/)
* [Data Engineering Helpers - Knowledge Sharing - Unity Catalog (UC)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-catalogs/unity-catalog/)
* [Data Engineering Helpers - Knowledge Sharing - JS world](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/js-world/)
* [Data Engineering Helpers - Knowledge Sharing - Python](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/python/)
* [Material for the Data platform - Data life cycle](https://github.com/data-engineering-helpers/data-life-cycle)
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box)

# Getting started

## Backend (Python and FastAPI)
* Change directory to `src/backend`:
```bash
$ cd src/backend
```

* Create a Python virtual environment, _e.g._, with Python 3.12,
  and activate it
```bash
$ virtualenv .venv --python 3.12
$ source .venv/bin/activate
```

* Install the Python dependencies:
```bash
$ python -mpip install -U pip
$ python -mpip install -r requirements.txt
```

* Launch the backend, for instance with [Uvicorn](https://uvicorn.dev/):
```bash
$ uvicorn src.app:app --reload --host 0.0.0.0 --port 8060
```

# Setup

## Shell
* Reference: https://github.com/larsgeorge/ontos?tab=readme-ov-file#environment-configuration
* Setup a few environment variables. Shell aliases are used here in order to switch
  to various environemtns (_e.g._, local, production)

* Add the following lines into `~/.bashrc` (for the Bash) or `~/.zshrc` (for Zsh):
```bash
alias setontosdbx='export DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"; export DATABRICKS_WAREHOUSE_ID="1234567890abcdef"; export DATABRICKS_CATALOG="main"; export DATABRICKS_SCHEMA="default"; export DATABRICKS_VOLUME="app_volume"; export APP_AUDIT_LOG_DIR="audit_logs"; export DATABRICKS_TOKEN="dapi1234567890abcdef"'
alias setonposlocal='export DATABASE_TYPE="postgres"; export POSTGRES_HOST="localhost"'
```

## Python
* [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/)
  features how to install [Python](https://python.org)

## JavaScript (JS)
* [Data Engineering Helpers - Knowledge Sharing - JS world](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/js-world/)
  features instructions on:
  * If needed, how to install
  [NVM (NodeJS Version Manager)](https://github.com/nvm-sh/nvm):
```bash
$ brew install nvm
$ nvm --version
0.40.3
```
  * If needed, how to install [NodeJS](https://nodejs.org/) (_e.g._, with NVM)
```bash
$ nvm ls-remote
$ nvm install 25.1.0
$ npm --version
11.6.2
```
  * If needed, how to install the [Yarn package manager](https://yarnpkg.com/)
  (_e.g._, with `npm`)
```bash
$ npm install -g yarn
$ yarn --version
1.22.22
```

## PostgreSQL
* [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/)
  has detailed step-by-step instructions on:
  * If needed, how to install a PostgreSQL database server
  * How to create the Ontos user, schema and database
