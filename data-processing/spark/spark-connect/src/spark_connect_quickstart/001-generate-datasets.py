#!/usr/bin/env python
#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/spark-connect/src/spark_connect_quickstart/001-generate-datasets.py
#

from faker import Faker
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import pyspark.sql.types as T

#
k_table = "dim_customer"
k_data_base_dir = f"data/{k_table}"
cust_init_dataset = f"{k_data_base_dir}/init"
cust_inc_dataset = f"{k_data_base_dir}/inc1"

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

    #
    faker = Faker()
    Faker.seed(4321)

    # Generate randomly, with Faker, a few customer profiles. That yields the
    # initial customer dataset
    # Faker doc:
    #  https://faker.readthedocs.io/en/master/providers/faker.providers.profile.html
    cust_profiles = [faker.profile() for i in range(0, 100)]

    # Create a Spark DataFrame from the list of randomly generated customer
    # profiles
    df_customer_init = spark.createDataFrame(cust_profiles)

    # Transform the geo-location from a structure into two regular fields
    df_customer_init = df_customer_init.withColumn("current_location_lat",
                                                   F.col("current_location._1").cast("double"))
    df_customer_init = df_customer_init.withColumn("current_location_lon",
                                                   F.col("current_location._2").cast("double"))
    df_customer_init = df_customer_init.drop("current_location")

    # Transform the website array into a mere field
    udf_website = F.udf(lambda x: x[0], T.StringType())
    df_customer_init = df_customer_init.withColumn("website",
                                                   udf_website(df_customer_init.website))

    # Write the Spark DataFrame to a local Parquet file in the specified
    # directory
    df_customer_init.coalesce(1).write.mode("overwrite").save(cust_init_dataset)

    # Derive a sample from the initial dataset: take roughly 40% of the initial
    # dataset (that is, around 40 records out of 100)
    df_customer_inc1 = df_customer_init.sample(0.4)

    # Update the job field (with randomly generated new strings thanks to Faker)
    udf_job = F.udf(lambda _: faker.job(), T.StringType())
    df_customer_inc1 = df_customer_inc1.withColumn("job", udf_job(df_customer_inc1.job))

    # Update the company field (with randomly generated new strings thanks to
    # Faker)
    udf_company = F.udf(lambda _: faker.company(), T.StringType())
    df_customer_inc1 = df_customer_inc1.withColumn("company", udf_company(df_customer_inc1.company))

    # Write the Spark DataFrame to a local Parquet file in the specified
    # directory
    df_customer_inc1.coalesce(1).write.mode("overwrite").save(cust_inc_dataset)
    
if __name__ == "__main__":
    main()

