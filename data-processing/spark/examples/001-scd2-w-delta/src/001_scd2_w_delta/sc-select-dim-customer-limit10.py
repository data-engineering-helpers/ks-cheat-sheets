#!/usr/bin/env python
#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/001-scd2-w-delta/src/001_scd2_w_delta/sc-select-dim-customer-limit10.py
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

def getSparkSession() -> SparkSession:
    spark = (
        SparkSession.builder.appName("scd2-app-sc-only")
        .config("spark.jars.packages", k_all_jars)
        .remote(sc_url)
        .getOrCreate()
    )
    return spark

def displayCustTableHdr(spark: SparkSession):
    df_table = spark.sql(f"select * from {delta_table_name}")
    nb_rows = df_table.count()
    df_table_hdr = df_table.limit(5).toPandas()
    print(f"Nb of rows: {nb_rows} - First 5 records of {delta_table_name}:")
    print(df_table_hdr)

def main() -> None:
    # Retrieve the Spark session
    spark = getSparkSession()

    # Execute checking queries
    displayCustTableHdr(spark=spark)

if __name__ == "__main__":
    main()

