#!/usr/bin/env python
#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/000_data_setup/src/000_data_setup/generate_customer_datasets.py
#

from faker import Faker
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import pyspark.sql.types as T

#
cust_init_dataset = "../data/dim_customer/init"
cust_inc_dataset = "../data/dim_customer/inc1"

def main() -> None:
    # Retrieve (or create) the Spark session
    spark = SparkSession.builder.appName("scd2-app").getOrCreate()

    faker = Faker()
    Faker.seed(4321)

    # Generate randomly, with Faker, a few customer profiles. That yields the
    # initial customer dataset
    # Faker doc:
    #  https://faker.readthedocs.io/en/master/providers/faker.providers.profile.html
    cust_profiles = [faker.profile() | {"uuid": faker.uuid4()} for i in range(0, 100)]

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

    # Reorder the fields
    df_customer_init = df_customer_init.select(
        "uuid", "address", "birthdate", "blood_group", "company", "job", "mail",
        "name", "residence", "sex", "ssn", "username", "website",
        "current_location_lat", "current_location_lon"
    )
    
    # Write the Spark DataFrame to a local Parquet file in the specified
    # directory
    df_customer_init.coalesce(1).write.mode("overwrite").save(cust_init_dataset)

    # DEBUG
    nb_rows = df_customer_init.count()
    print(f"Nb of rows: {nb_rows} - First 5 records of df_customer_init:")
    df_customer_init.show(5)
    
    # Derive a sample from the initial dataset: take roughly 50% of the initial
    # dataset (that is, around 50 records out of 100) and then limit to 42, so that
    # this number be deterministic
    df_customer_inc1 = df_customer_init.sample(fraction=0.5).limit(42)

    # Update the job field (with randomly generated new strings thanks to Faker)
    udf_job = F.udf(lambda _: faker.job(), T.StringType())
    df_customer_inc1 = df_customer_inc1.withColumn("job", udf_job(df_customer_inc1.job))

    # Update the company field (with randomly generated new strings thanks to
    # Faker)
    udf_company = F.udf(lambda _: faker.company(), T.StringType())
    df_customer_inc1 = df_customer_inc1.withColumn("company", udf_company(df_customer_inc1.company))

    # Reorder the fields
    df_customer_inc1 = df_customer_inc1.select(
        "uuid", "address", "birthdate", "blood_group", "company", "job", "mail",
        "name", "residence", "sex", "ssn", "username", "website",
        "current_location_lat", "current_location_lon"
    )
    
    # DEBUG
    nb_rows = df_customer_inc1.count()
    print(f"Nb of rows: {nb_rows} - First 5 records of df_customer_inc1:")
    df_customer_inc1.show(5)

    # Extract the list of uuid keys for the increment data sets
    df_customer_inc1_uuid_list = df_customer_inc1.select("uuid")

    # DEBUG
    print(f"List of uuid of updated records: {df_customer_inc1_uuid_list}")

    # Derive the data set of records which have not changed
    df_customer_init_not_changed = df_customer_init.where(~df_customer_init.uuid.isin(df_customer_inc1_uuid_list))

    # Reorder the fields
    df_customer_init_not_changed = df_customer_init_not_changed.select(
        "uuid", "address", "birthdate", "blood_group", "company", "job", "mail",
        "name", "residence", "sex", "ssn", "username", "website",
        "current_location_lat", "current_location_lon"
    )
    
    # DEBUG
    nb_rows = df_customer_init_not_changed.count()
    print(f"Nb of rows: {nb_rows} - First 5 records of df_customer_init_not_changed:")
    df_customer_init_not_changed.show(5)

    # Derive the full data set with the records which have changed and with the records
    # that have changed. That is, compared to the initial data set, the records
    # that have changed are not present, as they are replaced by the records which
    # have changed
    df_customer_all = df_customer_init_not_changed.union(df_customer_inc1)
    
    # Write the Spark DataFrame to a local Parquet file in the specified
    # directory
    df_customer_all.coalesce(1).write.mode("overwrite").save(cust_inc_dataset)

    # DEBUG
    nb_rows = df_customer_all.count()
    print(f"Nb of rows: {nb_rows} - First 5 records of df_customer_all:")
    df_customer_all.show(5)
    
if __name__ == "__main__":
    main()

