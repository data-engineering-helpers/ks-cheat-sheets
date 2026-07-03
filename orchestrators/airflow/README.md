---
title: Cheat Sheet - Airflow
intro: Cheat sheet about Airflow, be it OSS, Astro or AWS MWAA
---

## Table of Content (ToC)

* [title: Cheat Sheet \- Airflowintro: Cheat sheet about Airflow, be it OSS, Astro or AWS MWAA](#title-cheat-sheet---airflowintro-cheat-sheet-about-airflow-be-it-oss-astro-or-aws-mwaa)
* [Table of Content (ToC)](#table-of-content-toc)
* [Overview](#overview)
* [References](#references)
  * [Data Engineering and AI helpers](#data-engineering-and-ai-helpers)
  * [Astronomer documentation](#astronomer-documentation)
  * [PostgreSQL documentation](#postgresql-documentation)
  * [Airflow documentation](#airflow-documentation)
* [Quick start](#quick-start)
  * [Specific DAG](#specific-dag)
  * [Tutorials](#tutorials)
* [Installation](#installation)
  * [Installation from PyPI](#installation-from-pypi)
  * [Python](#python)
  * [Setup of Astro agentic tooling](#setup-of-astro-agentic-tooling)
    * [Setup of Astro Airflow MCP server](#setup-of-astro-airflow-mcp-server)
  * [Setup of PostgreSQL](#setup-of-postgresql)
  * [Database](#database)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

## Overview

[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/orchestrators/airflow/README.md)
explains how to install and to use Airflow on premises, _e.g._, on a laptop
or on a virtual machine (VM).

## References

### Data Engineering and AI helpers

* [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/)
* [Data Engineering Helpers - Knowledge Sharing - Python](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/python/)
* [Data Engineering Helpers - Knowledge Sharing - JavaScript (JS) world](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/js-world/)
* [Data Engineering Helpers - Knowledge Sharing - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box/)
* [Data Engineering Helpers - Knowledge Sharing - AI skills and rules](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/ai/rules-skills/)
* [AI Helpers - Knowledge Sharing - Cheat Sheets](https://github.com/ai-helpers/ks-cheat-sheets/)
* [AI Helpers - Knowledge Sharing - Curated AI agent skills](https://github.com/ai-helpers/ai-skills-curated/)

### Astronomer documentation

* [GitHub - Astronomer - Agentic tooling](https://github.com/astronomer/agents)
  * [GitHub - Astronomer - Astro Airflow MCP](https://github.com/astronomer/agents/tree/main/astro-airflow-mcp)

### PostgreSQL documentation

* [PostgreSQL](https://www.postgresql.org) is a good option to power the
  metadata of Airflow when the installation of that latter is somewhat
  persistent
* See [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md)
  for more details on how to install some PostgreSQL server/service
* This cheat sheet (about Airflow) details how to install Airflow both with
  SQLite (the standard and easy way) and with PostgreSQL

### Airflow documentation

* [Airflow overview](https://airflow.apache.org/docs/apache-airflow/stable/index.html)
* [Airflow quick start](https://airflow.apache.org/docs/apache-airflow/stable/start.html)
* [Airflow releases](https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html)
* [Installation of Airflow](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html)
  * [Installation of Airflow from PyPI](https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html)

## Quick start

* Upgrade to the latest versions:

```bash
make init update
```

* Launch Airflow in either
  * Stand-alone mode:

```bash
make airflow-start-standalone
```

* After a few seconds, among the last few lines, the credentials of
  the Airflow admin user (something like `admin` for the user name and
  the password is generated randomly at the first execution of the  Airflow
  standalone service) are given for the web application

* Mode of distinct components, launched in the background
  * Launch the Airflow web console application (and wait a few seconds):

```bash
uv run airflow webserver --port 8080 &
```

* Launch the Airflow scheduler:

```bash
uv run airflow scheduler &
```

* The web console is available [locally on port `8080`](http://localhost:8080)

* To stop the Airflow components (as they have been started in the background):

```bash
$ jobs
  kill %2
  kill %1
```

### Specific DAG

* Let us pick the Bash operator example (`example_bash_operator`)

* In the [Airflow web console](http://localhost:8080/dags/example_bash_operator/graph)

* Alternatively, from the command-line:

```bash
pipenv run airflow dags details example_bash_operator
```

* Run the DAG from the command-line:

```bash
TODAY_DATE="$(date +'%Y-%m-%d')"
pipenv run airflow tasks test example_bash_operator runme_0 $TODAY_DATE
```

### Tutorials

* See [Airflow tutorial](https://airflow.apache.org/docs/apache-airflow/2.6.3/tutorial/index.html)

## Installation

* If not already odne so, clone
  [this Git repository](https://github.com/data-engineering-helpers/ks-cheat-sheets)

```bash
mkdir -p ~/dev/knowledge-sharing
git clone https://github.com/data-engineering-helpers/ks-cheat-sheets \
  ~/dev/knowledge-sharing/ks-cheat-sheets
cd ~/dev/knowledge-sharing/ks-cheat-sheets/orchestrators/airflow
```

### Python

* See the details in
  [Data Engineering Helpers - Knowledge Sharing - Python](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/python/)

* If not already done so, install uv. For instance, on MacOS:

```bash
brew install uv
```

* Upgrade to the latest versions:

```bash
make init update
```

* Show the versions of Airflow and of all its components:

```bash
make airflow-info
```

### Setup of Astro agentic tooling

* Install all the Astro agentic tools with a single command:

```bash
npx skills add astronomer/agents --skill '*' -g
```

#### Setup of Astro Airflow MCP server

* Integrate the following Astro Airflow MCP server setting in the agent
  configuration:

```json
{
  "mcpServers": {
    "airflow": {
      "command": "uvx",
      "args": ["astro-airflow-mcp", "--transport", "stdio"]
    }
  }
}
```

### Setup of PostgreSQL

* It is assumed in this cheat sheet that PostgreSQL has been installed locally
  anc may be simply administered through the command-line

* The PostgreSQL `~/.pgpass` may have to be setup (see
  [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md)
  for details)

* Check that the PostgreSQL command-line works:

```bash
$ psql -d postgres -c "select 42 as THGTTG;"
 thgttg 
--------
     42
(1 row)
```

* If needed, the Airflow database and user may be deleted (so as
  to be re-created from scratch):

```bash
psql -d postgres -c "drop database airflow;"
psql -d postgres -c "drop user airflow;"
```

* If not already done so, create a database and admin user for the
  Airflow database:

```bash
psql -d postgres -c "create database airflow;"
psql -d postgres -c "create user airflow with encrypted password '<airflow-pass>'; grant all privileges on database airflow to airflow;"
psql -d airflow -c "grant all on schema public to airflow;"
```

* Add the Airflow credentials to the `~/.pgpass`  file:

```bash
cat >> ~/.pgpass << _EOF
localhost:5432:airflow:airflow:>airflow-passwd>
_EOF
chmod 600 ~/.pgpass
```

* Check that the new Airflow database and user work:

```bash
$ psql -d airflow -U airflow -c "select 42 as test;"
 test 
------
   42
(1 row)
```

* To use a PostgreSQL database, instead of SQLite, replace, within
  the Airflow configuration file, the database connection strings.
  * See [Airflow doc](http://airflow.apache.org/docs/apache-airflow/stable/howto/set-up-database.html#database-uri)
  * Spot the line beginning with `sql_alchemy_conn`, and replace the line
    like `sql_alchemy_conn = sqlite:///$HOME/airflow/airflow.db`
    by something like `sql_alchemy_conn = postgresql://airflow:<airflow-passwd>@localhost/airflow`

```bash
vi ~/airflow/airflow.cfg
```

### Database

* The database (either SQLite or PostgreSQL) is specified in the Airflow
  configuration script (see above)

* Create the Airflow database

```bash
uv run airflow db upgrade
```

* The output with SQLite:

```txt
DB: sqlite:$HOME/airflow/airflow.db
Performing upgrade with database sqlite:$HOME/airflow/airflow.db
...
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running stamp_revision  -> c804e5c76e3e
Upgrades done
```

* The output with PostgreSQL:

```txt
DB: postgresql://airflow:***@localhost/airflow
erforming upgrade with database postgresql://airflow:***@localhost/airflow
...
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running stamp_revision  -> c804e5c76e3e
Upgrades done
```

* To check the content of the SQLite database:

```bash
sqlite3 ~/airflow/airflow.db ".schema dag;"
```

```sql
CREATE TABLE dag (
    dag_id VARCHAR(250) NOT NULL, 
    ...
    CONSTRAINT dag_pkey PRIMARY KEY (dag_id)
);
```

* To check the content of the PostgreSQL database (type the `q` key to quit
  the browsing mode):

```bash
psql -d airflow -U airflow -c "\d dag;"
```

```sql
                              Table "public.dag"
  Column                  | Type                     | Nullable | Default
--------------------------+-          ---------------+----------+---------
 dag_id                   | character varying(250)   | not null | 
  ...
 next_dagrun_create_after | timestamp with time zone |          | 
```

* Create an admin user for the web console:

```bash
uv run airflow users create --username admin --firstname John --lastname Doe --role Admin --email john@doe.com --password <airflow-passwd>
```
