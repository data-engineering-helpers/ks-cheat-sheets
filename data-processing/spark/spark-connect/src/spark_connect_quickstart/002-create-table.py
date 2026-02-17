#!/usr/bin/env python
#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/spark-connect/src/spark_connect_quickstart/002-create-table.py
#

from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import pyspark.sql.types as T

#
k_table = "dim_customer"
k_data_base_dir = f"data/{k_table}"
k_data_dir = f"{k_data_base_dir}/init/"

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

    # Read the data-set
    df = spark.read.load(k_data_dir)

    # Reporting
    nb_rows = df.count()
    print(f"Number of rows in {k_data_dir}: {nb_rows}")

    # Write the data set as a table
    # Without the "path" option, Spark will complain that the location directory is not empty.
    # See also https://stackoverflow.com/a/65605842/798053
    df.write.option("path", k_table).mode("overwrite").saveAsTable(k_table)
    print(f"Wrote the data-set as a table, namely {k_table}")


if __name__ == "__main__":
    main()

