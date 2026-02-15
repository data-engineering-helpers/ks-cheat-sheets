#!/usr/bin/env python
#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/spark-merge-customer.py
#
# The schema corresponds to Faker profiles:
# https://faker.readthedocs.io/en/master/providers/faker.providers.profile.html
# The structure and array have been removed for simplification purpose,
# so as to ease the Delta merging
#
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import delta.tables as dt

ddl_drop = "drop table if exists dim_customer;"

ddl_create = """
create table dim_customer (
  address string,
  birthdate date,
  blood_group string,
  company string,
  current_location_lat double,
  current_location_lon double,
  job string,
  mail string,
  name string,
  residence string,
  sex string,
  ssn string,
  username string,
  website string,
  start_date date,
  end_date date,
  is_current boolean
)
using delta
location 'dim_customer';
"""

def getSparkSession() -> SparkSession:
    spark = (
        SparkSession.builder.appName("scd2-app")
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

