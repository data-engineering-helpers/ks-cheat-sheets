#!/usr/bin/env python
#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/001-scd2-w-delta/src/001_scd2_w_delta/test_001_delta_simple.py
#

from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import delta.tables as dt

from jobs import merge_customer_001_simple

#
k_spark_version = "4.1"
k_scala_version = "2.13"
k_dl_version = "4.2.0"
k_dl_jar_package = f"io.delta:delta-spark_{k_spark_version}_{k_scala_version}:{k_dl_version}"

#
schema_name = "bronze"
table_name = "dim_customer"
delta_table_name = f"{schema_name}.{table_name}"
cust_init_dataset = f"../data/{table_name}/init"
cust_inc_dataset1 = f"../data/{table_name}/inc1"

def getSparkSession() -> SparkSession:
    spark = (
        SparkSession.builder.appName("test-scd2-001-app")
        .config("spark.jars.packages", k_dl_jar_package)
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config("spark.sql.catalog.spark_catalog",
                "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        .enableHiveSupport()
        .getOrCreate()
    )
    return spark

def test_merge_customer_001_simple():
    """
    Test that the job ingesting initial and incremental data sets
    """
    # Execute the ingestion job
    merge_customer_001_simple.main()
    
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
    test_merge_customer_001_simple()
