#!/usr/bin/env python
#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/001-scd2-w-delta/src/001_scd2_w_delta/test_002_delta_uc_only.py
#

from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import delta.tables as dt

from jobs import merge_customer_002_uc_only

#
k_spark_version = "4.1"
k_scala_version = "2.13"
k_dl_version = "4.2.0"
k_uc_version = "0.5.0-SNAPSHOT"

#
k_dl_jar_package = f"io.delta:delta-spark_{k_spark_version}_{k_scala_version}:{k_dl_version}"
k_uc_jar_package = f"io.unitycatalog:unitycatalog-spark_{k_scala_version}:{k_uc_version}"
k_all_jars = f"{k_dl_jar_package},{k_uc_jar_package}"

#
k_uc_url = "http://localhost:8080"
catalog_name = "unityxt"
schema_name = "bronze"
table_name = "dim_customer"
delta_table_name = f"{catalog_name}.{schema_name}.{table_name}"
cust_init_dataset = f"../data/{table_name}/init"
cust_inc_dataset1 = f"../data/{table_name}/inc1"

def getSparkSession() -> SparkSession:
    spark = (
        SparkSession.builder.appName("test-scd2-002-app")
        .config("spark.jars.packages", k_all_jars)
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config("spark.sql.catalog.spark_catalog",
                "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        .config(f"spark.sql.catalog.{catalog_name}",
                "io.unitycatalog.spark.UCSingleCatalog")
        .config(f"spark.sql.catalog.{catalog_name}.uri", k_uc_url)
        .config(f"spark.sql.catalog.{catalog_name}.token", "")
        .config(f"spark.sql.defaultCatalog", catalog_name)
        .getOrCreate()
    )
    return spark

def test_merge_customer_002_uc_only():
    """
    Test that the job ingesting initial and incremental data sets
    """
    # Execute the ingestion job
    merge_customer_002_uc_only.main()
    
    # Retrieve the Spark session
    spark = getSparkSession()

    # Retrieve the Delta table
    delta_table = dt.DeltaTable.forName(spark, delta_table_name)
    df_dt = delta_table.toDF()

    #
    nb_rows_dt = df_dt.count()
    assert nb_rows_dt == 100

    # Derive only the rows which have been updated (they are no longer current)
    df_updated = df_dt.filter(df_dt.is_current == False)
    nb_rows_updated = df_updated.count()
    assert nb_rows_updated == 42

if __name__ == "__main__":
    test_merge_customer_002_uc_only()
