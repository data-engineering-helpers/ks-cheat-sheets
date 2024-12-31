Cheat Sheet - Jupyter with PySpark and DuckDB
=============================================

# Table of Content (ToC)
* [Overview](#overview)
* [References](#references)
  * [Jupyter](#jupyter)
  * [Spark](#spark)
    * [Spark Connect](#spark-connect)
  * [DuckDB](#duckdb)
* [Quick start](#quick-start)
  * [Start JupyterLab with a PySpark\-Delta kernel](#start-jupyterlab-with-a-pyspark-delta-kernel)
  * [Simple PySpark notebook](#simple-pyspark-notebook)
  * [Spark](#spark-1)
* [Use cases](#use-cases)
* [Initial setup](#initial-setup)
  * [Python libraries](#python-libraries)
  * [DuckDB on the command\-line (CLI)](#duckdb-on-the-command-line-cli)
  * [DuckDB Python library](#duckdb-python-library)
  * [JupyterLab](#jupyterlab)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/jupyter/jupyter-pyspark-duckdb/README.md)
explains how to install and to use JupyterLab with a PySpark kernel
and a DuckDB database.
Together, these open source tools offer kind of a so-called
Modern Data Stack (MDS) in a box, _i.e._, one can analyze and
process data all in local from Jupyter notebooks.

See also the:
* [Dedicated cheat sheet for DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/)
* [Dedicated cheat sheet for Spark](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/)

# References

## Jupyter
* [BMC - Integrate PySpark with Jupyter](https://www.bmc.com/blogs/jupyter-notebooks-apache-spark/)

## Spark
* [GitHub - Data Engineering Helpers - Cheat sheet for Spark](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/)
  * [Apache Spark - Download Spark manually](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#manually-downloading)
  * [Apache Spark - Doc - Getting started / Installation](https://spark.apache.org/docs/latest/api/python/getting_started/install.html)

### Spark Connect
* [Apache Spark - Doc - Spark Connect - Overview](https://spark.apache.org/docs/latest/spark-connect-overview.html)
* [Apache Spark - Doc - Spark Connect - Quick start](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_connect.html)

## DuckDB
* [GitHub - Data Engineering Helpers - Cheat sheet for DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/)

# Quick start
* Go into the directory dedicated to that cheat sheet (see the
  [Initial setup](#initial-setup)
  on how to clone this Git repository):
```bash
cd ~/dev/ks/ks-cheat-sheets
```

## Start JupyterLab with a PySpark-Delta kernel
> **Note**
* For the sake of reference, there are two options described
  in this cheat sheet:
  * An independent Spark cluster may be started, and the PySpark kernel
  may use that cluster with Spark Connect
  * The PySpark kernel may be autonomous (it does not need to connect to any
  independent cluster)
* The option with independent Spark cluster (and using Spark Connect)
  makes sense for at least the following use cases:
  * Several programming stacks are used (_e_g_, Python, Scala, R or SQL).
    * When only PySpark (Python) is used, an independent Spark server.
    * Note that SQL may be used in PySpark too (the queries are then
    regular Python strings); it is not ideal for seasonal SQL users, but
    it works well.
  * Several users, or teams, need to use Spark on the same machine,
  for instance on a remote virtual machine (VM).
  * The Spark cluster requires some extra packages, like for instance
  [Delta](https://delta.io) or [Unity Catalog](https://unitycatalog.io),
  and the client process (_e.g._, Airflow, SQLMesh) may not be designed
  to pass those extra packages
	 

* If using an independent Spark cluster, from a dedicated terminal window/tab,
  launch Spark Connect server in the background.
  Note that the `SPARK_REMOTE` environment variable should not be set at this
  stage, otherwise the Spark Connect server will try to connect to the
  corresponding Spark Connect server and will therefore not start.
  * The
  [Shell aliases given in the Spark-dedicated cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/README.md#shell-environment-and-aliases)
  first unset that environment variable before launching the Spark Connect
  server (if you use those aliases, all is good)
```bash
$ sparkconnectstart
```
* [GitHub - Data Engineering Helpers - Cheat sheet for Spark](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/)

* Note that JupyterLab will be available locally from a web browser on
  a port, which may be configured thanks to the `PYSPARK_DRIVER_PYTHON_OPTS`
  environment variable (see the
  [Shell aliases given in the Spark-dedicated cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/README.md#shell-environment-and-aliases)
  for further details). By default, that port is specified to be `8889`
  in this cheat sheet; the local web browser URL is therefore
  http://localhost:8889/lab

* If not using an independent Spark cluster, simply launch PySpark
  from the command-line, which in turn launches Jupyter Lab
  + Follow the details given by PySpark to open Jupyter in a web browser
  commands from any terminal/tab:
```bash
$ pysparkdeltawoconnect
```

* If using an independent Spark cluster, from any terminal window/tab,
  different from the window/tab having launched the Spark Connect server,
  launch PySpark from the command-line, which in turn launches Jupyter Lab
  + Follow the details given by PySpark/Jupyter to open Jupyter
    in a web browser
```bash
$ pysparkdeltawconnect
```

* In both cases, the output of the PySpark command (triggering JupyterLab)
  should be something like the following (filtered out here):
```txt
...
[C 2023-06-27 21:54:04.720 ServerApp] 
    
    To access the server, open this file in a browser:
        file://$HOME/Library/Jupyter/runtime/jpserver-21219-open.html
    Or copy and paste one of these URLs:
        http://localhost:8889/lab?token=dd69151c26a3b91fabda4b2b7e9724d13b49561f2c00908d
        http://127.0.0.1:8889/lab?token=dd69151c26a3b91fabda4b2b7e9724d13b49561f2c00908d
...
```

* Open Jupyter in a web browser. For instance, on MacOS:
```bash
$ open ~/Library/Jupyter/runtime/jpserver-*-open.html
```

* Open a notebook, for instance
  [`ipython-notebooks/simple-connect.ipynb`](https://github.com/data-engineering-helpers/databricks-examples/blob/main/ipython-notebooks/simple-connect.ipynb)
  * Run the cells. The third cell should give a result like:
```txt
+-------+--------+-------+-------+
|User ID|Username|Browser|     OS|
+-------+--------+-------+-------+
|   1580|   Barry|FireFox|Windows|
|   5820|     Sam|MS Edge|  Linux|
|   2340|   Harry|Vivaldi|Windows|
|   7860|  Albert| Chrome|Windows|
|   1123|     May| Safari|  macOS|
+-------+--------+-------+-------+
```

## Simple PySpark notebook
* Source:
  * [Local web browser - `simple-spark-pandas.ipynb` notebook](http://localhost:8889/lab/tree/ipython-notebooks/simple-spark-pandas.ipynb)
  * [Local file-system - `simple-spark-pandas.ipynb` notebook](ipython-notebooks/simple-spark-pandas.ipynb)
  * [On GitHub - `simple-spark-pandas.ipynb` notebook](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/jupyter/jupyter-pyspark-duckdb/ipython-notebooks/simple-spark-pandas.ipynb)

## Spark
* See
  [GitHub - Data Engineering Helpers - Cheat sheet for Spark](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/)
  * For the details on how to launch a Spark Connect cluster and/or
  a standalone Spark engine
  * For the
  [Shell aliases given in the Spark-dedicated cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/README.md#shell-environment-and-aliases)
  used in this cheat sheet

# Use cases

# Initial setup
* If not already done so, clone
  [this Git repository](https://github.com/data-engineering-helpers/ks-cheat-sheets):
```bash
mkdir -p ~/dev/ks && \
  git clone https://github.com/data-engineering-helpers/ks-cheat-sheets.git ~/dev/ks/ks-cheat-sheets && \
  cd ~/dev/ks/ks-cheat-sheets
```

## Python libraries
* Install a few Python libraries from PyPi:
```bash
$ python -mpip install -U pip plotly folium cloudpathlib pyvis matplotlib seaborn
```

## DuckDB on the command-line (CLI)
* On MacOS:
```bash
brew install duckdb
```

## DuckDB Python library
* Simply install with Pip:
```bash
$ python -mpip install -U duckdb
```

## JupyterLab
* Install JupyterLab from PyPi:
```bash
$ python -mpip install -U jupyterlab
```

