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
* [Use cases](#use-cases)
* [Initial setup](#initial-setup)
  * [Python libraries](#python-libraries)
  * [DuckDB on the command\-line (CLI)](#duckdb-on-the-command-line-cli)
  * [DuckDB Python library](#duckdb-python-library)
  * [PySpark and Spark Connect](#pyspark-and-spark-connect)
  * [JupyterLab](#jupyterlab)
  * [Shell environment and aliases](#shell-environment-and-aliases)
  * [Install native Spark manually](#install-native-spark-manually)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/jupyter/jupyter-pyspark-duckdb/README.md)
explains how to install and to use JupyterLab with a PySpark kernel
and a DuckDB database.
Together, these open source tools offer kind of a so-called
Modern Data Stack (MDS) in a box, _i.e._, one can analyze and
process data all in local from Jupyter notebooks.

See also the
[dedicated cheat sheet for DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/README.md).

## References

### Jupyter
* [BMC - Integrate PySpark with Jupyter](https://www.bmc.com/blogs/jupyter-notebooks-apache-spark/)

### Spark
* [Apache Spark - Download Spark manually](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#manually-downloading)
* [Apache Spark - Doc - Getting started / Installation](https://spark.apache.org/docs/latest/api/python/getting_started/install.html)

#### Spark Connect
* [Apache Spark - Doc - Spark Connect - Overview](https://spark.apache.org/docs/latest/spark-connect-overview.html)
* [Apache Spark - Doc - Spark Connect - Quick start](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_connect.html)

### DuckDB
* [GitHub - Data Engineering Helpers - Cheat sheet for DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/README.md)

# Quick start
* Go into the directory dedicated to that cheat sheet (see the
  [Initial setup](#initial-setup)
  on how to clone this Git repository):
```bash
cd ~/dev/ks/ks-cheat-sheets
```

## Start JupyterLab with a PySpark-Delta kernel
> **Note**
For the sake of reference, there are two options described
in this cheat sheet:
* An independent Spark cluster may be started, and the PySpark kernel
   may use that cluster with Spark Connect
* The PySpark kernel may be autonomous (it does not need to connect to any
   independent cluster)
The option with independent Spark cluster (and using Spark Connect)
makes sense for at least the following use cases:
* Several programming stacks are used (_e_g_, Python, Scala, R or SQL).
  When only PySpark (Python) is used, an independent Spark server.
  Note that SQL may be used in PySpark too (the queries are then
  regular Python strings); it is not ideal for seasonal SQL users, but
  it works well.
* Several users, or teams, need to use Spark on the same machine,
  for instance on a remote virtual machine (VM).
	 

* If using an independent Spark cluster, from a dedicated terminal window/tab,
  launch Spark Connect server in the background.
  Note that the `SPARK_REMOTE` environment variable should not be set at this
  stage, otherwise the Spark Connect server will try to connect to the
  corresponding Spark Connect server and will therefore not start.
  The [Shell aliases given in this cheat sheet](#shell-environment-and-aliases)
  first unset that environment variable before launching the Spark Connect
  server (if you use those aliases, all is good)
```bash
$ sparkconnectstart
```

* Note that JupyterLab will be available locally from a web browser on
  a port, which may be configured thanks to the `PYSPARK_DRIVER_PYTHON_OPTS`
  environment variable (see the
  [Shell environment and aliases section](#shell-environment-and-aliases)
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
  + Run the cells. The third cell should give a result like:
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
  + [Local web browser - `simple-spark-pandas.ipynb` notebook](http://localhost:8889/lab/tree/ipython-notebooks/simple-spark-pandas.ipynb)
  + [Local file-system - `simple-spark-pandas.ipynb` notebook](ipython-notebooks/simple-spark-pandas.ipynb)
  + [On GitHub - `simple-spark-pandas.ipynb` notebook](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/jupyter/jupyter-pyspark-duckdb/ipython-notebooks/simple-spark-pandas.ipynb)

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
$ pip install -U pip plotly folium cloudpathlib pyvis matplotlib seaborn
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

## PySpark and Spark Connect
* As per the official
  [Apache Spark documentation](https://spark.apache.org/docs/latest/api/python/getting_started/install.html),
  PyPi-installed PySpark (`pip install pyspark[connect]`) comes with
  Spark Connect from Spark version 3.4 or later.
  + However, as of Spark version up to 3.4.1, the PySpark installation
    lacks the two new administration scripts allowing to start and
	to stop the Spark Connect server.
  + For convenience, these two scripts have therefore been copied into this
    Git repository, in the
    [`tools/` directory](https://github.com/data-engineering-helpers/ks-cheat-sheets/tree/main/tools). They may then be simply copied in the PySpark
	`sbin` directory, once PySpark has been installed with `pip`

* Install PySpark, with the Spark Connect extension, from PyPi:
```bash
$ pip install -U pyspark[connect,sql,pandas_on_spark]
```

## JupyterLab
* Install JupyterLab from PyPi:
```bash
$ pip install -U jupyterlab
```

## Shell environment and aliases
* Add the following in the Bash/Zsh init script:
```bash
$ cat >> ~/.bashrc << _EOF

# Spark
PY_LIBDIR="$(python -mpip show pyspark|grep "^Location:"|cut -d' ' -f2,2)"
export SPARK_VERSION="\$(python -mpip show pyspark|grep "^Version:"|cut -d' ' -f2,2)"
export SPARK_HOME="\$PY_LIBDIR/pyspark"
export PATH="\$SPARK_HOME/sbin:\$PATH"
export PYSPARK_PYTHON="\$(which python3)"
export PYSPARK_DRIVER_PYTHON='jupyter'
export PYSPARK_DRIVER_PYTHON_OPTS='lab --no-browser --port=8889'

_EOF
```

* Re-read the Shell init scripts:
```
$ exec bash
```

* Copy the two Spark connect administrative scripts into the PySpark
  installation:
```bash
$ cp tools/st*-connect*.sh $SPARK_HOME/sbin/
```

* Check that the scripts are installed correctly:
```bash
$ ls -lFh $SPARK_HOME/sbin/*connect*.sh
-rwxr-xr-x  1 user  staff   1.5K Jun 28 16:54 $PY_LIBDIR/pyspark/sbin/start-connect-server.sh*
-rwxr-xr-x  1 user  staff   1.0K Jun 28 16:54 $PY_LIBDIR/pyspark/sbin/stop-connect-server.sh*
```

* Add the following Shell aliases to start and stop Spark, Spark Connect server
  and JupyterLab:
```bash
$ cat >> ~/.bash_aliases << _EOF

# Spark Connect
alias sparkconnectset='export SPARK_REMOTE="sc://localhost:15002"'
alias sparkconnectunset='unset SPARK_REMOTE'
alias sparkconnectstart='sparkconnectunset; start-connect-server.sh --packages org.apache.spark:spark-connect_2.12:\$SPARK_VERSION,io.delta:delta-core_2.12:2.4.0 --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"'
alias sparkconnectstop='stop-connect-server.sh'

# PySpark and/or PySpark kernel within JupyterLab
alias pysparkdeltawconnect='sparkconnectset; pysparkdelta'
alias pysparkdeltawoconnect='sparkconnectunset; pysparkdelta'

_EOF
```

* Re-read the Shell aliases:
```bash
. ~/.bash_aliases
```

## Install native Spark manually
* That section is kept for reference only. It is normally not needed

* Install Spark/PySpark manually, _e.g._ with Spark 3.4.1:
```bash
$ export SPARK_VERSION="3.4.1"
  wget https://dlcdn.apache.org/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop3.tgz
  tar zxf spark-$SPARK_VERSION-bin-hadoop3.tgz && \
  mv spark-$SPARK_VERSION-bin-hadoop3 ~/ && \
  rm -f spark-$SPARK_VERSION-bin-hadoop3.tgz
```

* Add the following in the Bash/Zsh init script:
```bash
$ cat >> ~/.bashrc << _EOF

# Spark
export SPARK_VERSION="${SPARK_VERSION}"
export SPARK_HOME="\$HOME/spark-\$SPARK_VERSION-bin-hadoop3"
export PATH="\$SPARK_HOME/bin:\$SPARK_HOME/sbin:\${PATH}"
export PYTHONPATH=\$(ZIPS=("\$SPARK_HOME"/python/lib/*.zip); IFS=:; echo "\${ZIPS[*]}"):\$PYTHONPATH
export PYSPARK_PYTHON="\$(which python3)"
export PYSPARK_DRIVER_PYTHON='jupyter'
export PYSPARK_DRIVER_PYTHON_OPTS='lab --no-browser --port=8889'

_EOF
exec bash
```

* Add the following Shell aliases to start and stop Spark Connect server:
```bash
$ cat >> ~/.bash_aliases << _EOF

# Spark Connect
alias sparkconnectstart='start-connect-server.sh --packages org.apache.spark:spark-connect_2.12:${SPARK_VERSION}'
alias sparkconnectstop='stop-connect-server.sh'

_EOF
. ~/.bash_aliases
```

