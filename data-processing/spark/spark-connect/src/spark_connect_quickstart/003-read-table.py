#!/usr/bin/env python
#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/spark-connect/src/spark_connect_quickstart/003-read-table.py
#

from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import pyspark.sql.types as T

#
k_table = "dim_customer"

def getSparkSession() -> SparkSession:
    # Retrieve (or create) the Spark session
    spark = SparkSession.builder.appName("spark-connect-quickstart-app").enableHiveSupport().getOrCreate()

    # Hive and Delta Lake version
    #spark = (
    #    SparkSession.builder.appName("spark-connect-quickstart-app")
    #    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    #    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    #    .enableHiveSupport()
    #    .getOrCreate()
    #)

    return spark

def main() -> None:
    # Retrieve the Spark session
    spark = getSparkSession()

    # Read the table
    df = spark.read.table(k_table)

    # Reporting
    nb_rows = df.count()
    print(f"Number of rows in the {k_table} table: {nb_rows}")
    df_10recs_str = str(df.take(10))
    print(f"10 first rows: {df_10recs_str}")

if __name__ == "__main__":
    main()

