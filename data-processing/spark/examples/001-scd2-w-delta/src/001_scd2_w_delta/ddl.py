#!/usr/bin/env python
#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/001-scd2-w-delta/src/001_scd2_w_delta/ddl.py
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
k_spark_version = "4.1"
k_scala_version = "2.13"
k_dl_version = "4.2.0"
k_dl_jar_package = f"io.delta:delta-spark_{k_spark_version}_{k_scala_version}:{k_dl_version}"

#
schema_name = "bronze"
delta_table_name = f"{schema_name}.dim_customer"

#
ddl_create_schema = f"create schema if not exists {schema_name};"

ddl_drop_table = f"drop table if exists {delta_table_name};"

ddl_create_table = f"""
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
        .config("spark.jars.packages", k_dl_jar_package)
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config("spark.sql.catalog.spark_catalog",
                "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        .enableHiveSupport()
        .getOrCreate()
    )

    # DEBUG
    # spark_conf_str = spark.sparkContext.getConf().getAll()
    # print(f"Spark conf: {spark_conf_str}")

    return spark

def ddl(spark: SparkSession):
    # Create schema if not existing
    spark.sql(ddl_create_schema)

    # Drop table if existing
    spark.sql(ddl_drop_table)

    # Create table
    spark.sql(ddl_create_table)

def main() -> None:
    # Retrieve the Spark session
    spark = getSparkSession()

    # Process the DDL statements
    ddl(spark=spark)

if __name__ == "__main__":
    main()
