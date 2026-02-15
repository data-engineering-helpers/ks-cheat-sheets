#!/usr/bin/env python
#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/sql/select-dim-customer-limit10.sql
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

def getSparkSession() -> SparkSession:
    spark = (
        SparkSession.builder.appName("scd2-app")
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        .enableHiveSupport()
        .getOrCreate()
    )
    return spark

def displayCustTableHdr(spark: SparkSession):
    df_table = spark.sql(f"select * from {delta_table_name} limit 5")
    nb_rows = df_table.count()
    df_table_hdr = df_table.limit(5).show()
    print(f"Nb of rows: {nb_rows} - First 5 records of {delta_table_name}:")
    print(df_table_hdr)

def main() -> None:
    # Retrieve the Spark session
    spark = getSparkSession()

    # Execute checking queries
    displayCustTableHdr(spark=spark)

if __name__ == "__main__":
    main()

