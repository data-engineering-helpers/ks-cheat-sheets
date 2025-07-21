#!/usr/bin/env python
#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/spark-merge-customer.py
#

from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import delta.tables as dt

spark = (
  SparkSession.builder.appName("scd2-app")
  .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
  .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
  .getOrCreate()
)

parquet_source_path = "dim_customer/"
delta_table_name = "dim_customer"

source_df = spark.read.parquet(parquet_source_path)

source_df = source_df.withColumn("start_date", F.current_date())
source_df = source_df.withColumn("end_date", F.lit("9999-12-31"))
source_df = source_df.withColumn("is_current", F.lit(True))

if dt.DeltaTable.isDeltaTable(spark, delta_table_name):
    delta_table = dt.DeltaTable.forName(spark, delta_table)
    print(f"{delta_table_name} Delta table exists. All is fine")
else:
    source_df.write.format("delta").mode("overwrite").saveAsTable(delta_table_name)
    print(f"{delta_table_name} Delta table did not exist. Created initial snapshot")
