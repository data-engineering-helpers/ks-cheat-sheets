#!/usr/bin/env python
#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/spark-merge-customer.py
#

from faker import Faker
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

spark = SparkSession.builder.appName("scd2-app").getOrCreate()

parquet_source_path = "customer_increment.parquet"
delta_table_name = "dim_customer"

faker = Faker()
Faker.seed(4321)

profiles = [faker.profile() for i in range(0, 100)]
df_customer = spark.createDataFrame(profiles)

df_customer = df_customer.withColumn("start_date", F.current_date())
df_customer = df_customer.withColumn("end_date", F.lit("9999-12-31"))
df_customer = df_customer.withColumn("is_current", F.lit(True))


df_customer.coalesce(1).write.mode("overwrite").save(delta_table_name)
