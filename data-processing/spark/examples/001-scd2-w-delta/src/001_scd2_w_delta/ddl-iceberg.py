#!/usr/bin/env python
#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/001-scd2-w-delta/src/001_scd2_w_delta/ddl-iceberg.py
#
# The schema corresponds to Faker profiles:
# https://faker.readthedocs.io/en/master/providers/faker.providers.profile.html
# The structure and array have been removed for simplification purpose,
# so as to ease the Delta merging
#
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import delta.tables as dt

#
delta_table_name = "bronze.dim_customer"

ddl_drop = f"drop table if exists {delta_table_name};"

ddl_create = f"""
create table {delta_table_name} (
  uuid string,
  address string,
  birthdate date,
  blood_group string,
  company string,
  job string,
  mail string,
  name string,
  residence string,
  sex string,
  ssn string,
  username string,
  website string,
  current_location_lat double,
  current_location_lon double,
  start_date date,
  end_date date,
  is_current boolean
)
using delta
--location '{delta_table_name}'
;
"""

def getSparkSession() -> SparkSession:
    spark = (
        SparkSession.builder.appName("scd2-app")
        .config("spark.jars.packages", "org.apache.iceberg:iceberg-spark-runtime-3.2_2.12:1.1.0,mysql:mysql-connector-java:8.0.32")
        .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")
        .config("spark.sql.catalog.spark_catalog", "org.apache.iceberg.spark.SparkSessionCatalog")
        .config('spark.sql.catalog.spark_catalog.type', 'hive')
        .config('spark.sql.catalog.local', 'org.apache.iceberg.spark.SparkCatalog')
        .config('spark.sql.catalog.local.type','hadoop')
        .config('spark.sql.catalog.local.warehouse','warehouse')
        .config('spark.sql.defaultCatalog','local')
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        .enableHiveSupport()
        .getOrCreate()
    )
    return spark

def ddl(spark: SparkSession):
    # Drop if existing
    spark.sql(ddl_drop)

    # Create
    spark.sql(ddl_create)

def main() -> None:
    # Retrieve the Spark session
    spark = getSparkSession()

    # Process the DDL statements
    ddl(spark=spark)

if __name__ == "__main__":
    main()

