Cheat Sheet - Data Product Management - Ontos
=============================================

# Table of Content (ToC)
* [Overview](#overview)
* [References](#references)
  * [Data Engineering helpers](#data-engineering-helpers)
* [Getting started](#getting-started)
  * [Backend (Python and FastAPI)](#backend-python-and-fastapi)
  * [Frontend (React and TypeScript)](#frontend-react-and-typescript)
* [Setup](#setup)
  * [Shell](#shell)
  * [Python](#python)
    * [Hatch Python project manager](#hatch-python-project-manager)
  * [JavaScript (JS)](#javascript-js)
  * [PostgreSQL](#postgresql)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

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

* Build the static part (there is a dependency on JavaScript tools, and in particular
  Yarn and Vite)
```bash
yarn build
```

* Launch the backend, for instance with [Uvicorn](https://uvicorn.dev/):
```bash
$ uvicorn src.app:app --reload --host 0.0.0.0 --port 8060
```

## Frontend (React and TypeScript)
* Change directory to `src/frontend`:
```bash
$ cd src/frontend
```

* Setup the port of the backend:
```bash
$ sed -i.bak -e 's/8000/8060/g' vite.config.ts
$ rm -f vite.config.ts.bak
```

* Launch the frontend:
```bash
$ yarn dev:frontend
```

# Setup

## Shell
* Reference: https://github.com/larsgeorge/ontos?tab=readme-ov-file#environment-configuration
* Setup a few environment variables. Shell aliases are used here in order to switch
  to various environemtns (_e.g._, local, production)

* Add the following lines into `~/.bashrc` (for the Bash) or `~/.zshrc` (for Zsh):
```bash
alias pgsetontosdbx='export DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"; export DATABRICKS_WAREHOUSE_ID="1234567890abcdef"; export DATABRICKS_CATALOG="main"; export DATABRICKS_SCHEMA="default"; export DATABRICKS_VOLUME="app_volume"; export APP_AUDIT_LOG_DIR="audit_logs"; export DATABRICKS_TOKEN="dapi1234567890abcdef"'
alias pgsetontoslocal='pgsetontosdbx; export DATABASE_TYPE="postgres"; export POSTGRES_HOST="localhost"; export POSTGRES_PORT="5432"; export POSTGRES_USER="ontos"; export POSTGRES_DB="ontos"'
alias setontosprod='pgsetontosdbx; export DATABASE_TYPE="postgres"; export POSTGRES_HOST="instance-01234567-89ab-cdef-0000-0123456789abcdef.database.cloud.databricks.com"; export POSTGRES_PORT="5432"; export POSTGRES_USER="ontos"; export POSTGRES_DB="ontos"'
alias dbontosprod='pgsetontossandbox; psql -h ${POSTGRES_HOST} -p ${POSTGRES_PORT} --set=sslmode=require -d ${POSTGRES_DB} -U ${POSTGRES_USER}'
```

## Python
* [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/)
  features how to install [Python](https://python.org)

### Hatch Python project manager
* If not already done so, install [Hatch](https://hatch.pypa.io/latest/):
```bash
$ brew install hatch
$ hatch --version
Hatch, version 1.15.1
```

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
  * If needed, install [Hatch]()
  (_e.g._, with `npm`)
```bash
$ npm install -g hatch
```
  * If needed, install [Vite](https://vite.dev/)
  (_e.g._, with `npm`)
```bash
$ npm install -g vite
$ vite --version
vite/7.2.2 darwin-arm64 node-v25.1.0
```

## PostgreSQL
* [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/)
  has detailed step-by-step instructions on:
  * If needed, how to install a PostgreSQL database server
  * How to create the Ontos user, schema and database

* Create on PostgreSQL a `ontos` database and a `ontos` user:
```bash
$ psql -h $POSTGRES_HOST -U $PG_ADM_USR -d postgres -c "create database ontos;"
CREATE DATABASE
$ psql -h $POSTGRES_HOST -U $PG_ADM_USR -d postgres -c "create user ontos with encrypted password '<ontos-pass>'; grant all privileges on database ontos to ontos;"
CREATE ROLE
GRANT
$ psql -h $POSTGRES_HOST -U $PG_ADM_USR -d ontos -c "grant all on schema public to ontos;"
GRANT
```

* Check that the access to the PostgreSQL database works:
```bash
$ psql -h $POSTGRES_HOST -U ontos -d ontos -c "select 42 as nb;"
 nb 
----
 42
(1 row)
```
