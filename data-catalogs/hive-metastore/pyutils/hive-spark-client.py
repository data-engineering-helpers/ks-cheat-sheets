#!/usr/bin/env python
#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/hive-metastore/pyutils/hive-spark-client.py
#
#
import ntpath
import posixpath
from os import path
from SparkSessionUtil import SparkSessionUtil

data_root = 'data'
db_name = 'test_metastore_persist'
table_name = 'test_table'
db_path = f"'{path.join(data_root, db_name)}'".replace(ntpath.sep, posixpath.sep)
spark = SparkSessionUtil.get_configured_spark_session()
spark.sql(f"""create database if not exists {db_name} location {db_path}""")
spark.sql(f"""create table if not exists {db_name}.{table_name}(Id int not null)""")

# reset our spark session
spark = None

spark = SparkSessionUtil.get_configured_spark_session()
# confirm the database and table created above are available in the metastore
spark.sql(f"show tables in {db_name}").show(truncate=False)
