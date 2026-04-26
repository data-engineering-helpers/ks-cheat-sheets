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
k_spark_version = "4.1"
k_scala_version = "2.13"
k_dl_version = "4.2.0"
k_pb_version = "3.25.1"

#
k_dl_jar_package = f"io.delta:delta-connect-client_{k_spark_version}_{k_scala_version}:{k_dl_version}"
k_pb_jar_package = f"com.google.protobuf:protobuf-java:{k_pb_version}"
k_all_jars = f"{k_dl_jar_package},{k_pb_jar_package}"

#
schema_name = "bronze"
table_name = "dim_customer"
delta_table_name = f"{schema_name}.{table_name}"
cust_init_dataset = f"../data/{table_name}/init"
cust_inc_dataset1 = f"../data/{table_name}/inc1"
sc_url = "sc://localhost:15002"

#
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
        .config("spark.jars.packages", k_all_jars)
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

