#!/usr/bin/env python
#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/001-scd2-w-delta/src/001_scd2_w_delta/sc-ddl.py
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
schema_name = "bronze"
delta_table_name = f"{schema_name}.dim_customer"
sc_url = "sc://localhost:15002"

schema_create = f"create schema if not exists {schema_name};"

ddl_drop = f"drop table if exists {delta_table_name};"

ddl_create = f"""
create table {delta_table_name} (
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
        SparkSession.builder.appName("scd2-app-sc-only")
        .remote(sc_url)
        .getOrCreate()
    )
    return spark

def ddl(spark: SparkSession):
    # Create schema if not existing
    spark.sql(schema_create)

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

