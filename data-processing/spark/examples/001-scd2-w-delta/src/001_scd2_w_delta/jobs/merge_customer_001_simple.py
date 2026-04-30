#!/usr/bin/env python
#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/001-scd2-w-delta/src/001_scd2_w_delta/jobs/merge_customer_001_simple.py
#

import pyspark.sql
import pyspark.sql.functions as F
import delta.tables as dt

#
k_spark_version = "4.1"
k_scala_version = "2.13"
k_dl_version = "4.2.0"
k_dl_jar_package = f"io.delta:delta-spark_{k_spark_version}_{k_scala_version}:{k_dl_version}"

#
schema_name = "bronze"
table_name = "dim_customer"
delta_table_name = f"{schema_name}.{table_name}"
cust_init_dataset = f"../data/{table_name}/init"
cust_inc_dataset1 = f"../data/{table_name}/inc1"

def getSparkSession() -> pyspark.sql.SparkSession:
    spark = (
        pyspark.sql.SparkSession.builder.appName("scd2-app")
        .config("spark.jars.packages", k_dl_jar_package)
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config("spark.sql.catalog.spark_catalog",
                "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        .enableHiveSupport()
        .getOrCreate()
    )
    return spark

def subtract_one_week(df: pyspark.sql.DataFrame) -> pyspark.sql.DataFrame:
    """
    Substract one week (7 days)
    """
    df_out = df.withColumn(
        "start_date",
        F.date_sub(F.current_date().cast("date"), days=7)
    )

    return df_out

def displayCustTableHdr(spark: pyspark.sql.SparkSession):
    df_table = spark.sql(f"select * from {delta_table_name}")
    nb_rows = df_table.count()
    df_table_hdr = df_table.limit(5).toPandas()
    print(f"Nb of rows: {nb_rows} - First 5 records of {delta_table_name}:")
    print(df_table_hdr)

def processCustomerInit(spark: pyspark.sql.SparkSession):
    source_df = spark.read.parquet(cust_init_dataset)

    # DEBUG
    nb_rows_init = source_df.count()
    print(f"Nb of rows in {cust_init_dataset}: {nb_rows_init}")

    # Add metadata fields
    source_df = subtract_one_week(df=source_df)
    source_df = source_df.withColumn("end_date",
                                     F.lit("9999-12-31").cast("date"))
    source_df = source_df.withColumn("is_current", F.lit(True))

    # Retrieve the Delta table if existing, otherwise fill it
    if dt.DeltaTable.isDeltaTable(spark, delta_table_name):
        delta_table = dt.DeltaTable.forName(spark, delta_table_name)
        print(f"{delta_table_name} Delta table exists. All is fine")

        # DEBUG
        displayCustTableHdr(spark=spark)

    else:
        print(f"{delta_table_name} Delta table did not exist. Creating initial snapshot...")
        source_df.write.format("delta").mode("overwrite").saveAsTable(delta_table_name)

        # DEBUG
        displayCustTableHdr(spark=spark)

def processCustomerInc1(spark: pyspark.sql.SparkSession):
    inc_df = spark.read.parquet(cust_inc_dataset1)

    # DEBUG
    nb_rows_inc = inc_df.count()
    print(f"Nb of rows in {cust_inc_dataset1}: {nb_rows_inc}")

    # Add metadata fields
    # inc_df = inc_df.withColumn("start_date", F.current_date().cast("date"))
    # inc_df = inc_df.withColumn("end_date", F.lit("9999-12-31").cast("date"))
    # inc_df = inc_df.withColumn("is_current", F.lit(True))

    # Sanity check
    #if not dt.DeltaTable.isDeltaTable(spark, delta_table_name):
    #    print(f"{delta_table_name} is apparently not a Delta table")
    #    return 1
    
    # Retrieve the Delta table
    delta_table = dt.DeltaTable.forName(spark, delta_table_name)
    df_dt = delta_table.toDF()
    nb_rows_dt = df_dt.count()
    print(f"Nb of rows in {delta_table_name}: {nb_rows_dt}")

    # Merge the incremental dataset into the Delta table
    # See https://docs.delta.io/delta-update/#slowly-changing-data-scd-type-2-operation-into-delta-tables
    print(f"Merging the incremental dataset ({cust_inc_dataset1}) into {delta_table_name} Delta table...")

    # Rows to INSERT new details (company, job) of existing customers. As the
    # join method is the default one, it is an INNER one, that is, the
    # intersection of both data sets, joined on the primary key (uuid)
    newDetailsToInsert = (
        inc_df.alias("src")
        .join(df_dt.alias("tgt"), on="uuid", how="inner")
        .where("tgt.is_current = true AND (src.company != tgt.company or src.job != tgt.job)")
        .select("src.*")
    )

    # Stage the update by unioning two sets of rows
    # 1. Rows that will be inserted in the whenNotMatched clause
    # 2. Rows that will either update the current details (company, job) of existing
    #    customers or insert the new details of new customers

    # Rows for 1
    newDetailsToInsertWMergeKey = newDetailsToInsert.alias("rone").selectExpr("NULL as mergeKey", "*")

    # DEBUG
    nb_rows = newDetailsToInsertWMergeKey.count()
    print(f"Nb of rows: {nb_rows} - First 5 records of newDetailsToInsertWMergeKey:")
    newDetailsToInsertWMergeKey.show(5)

    # Rows for 2
    incDFWMergeKey = inc_df.alias("rtwo").selectExpr("uuid as mergeKey", "*")

    # DEBUG
    nb_rows = incDFWMergeKey.count()
    print(f"Nb of rows: {nb_rows} - First 5 records of incDFWMergeKey:")
    incDFWMergeKey.show(5)

    # Union of both types of rows
    stagedUpdates = (
        newDetailsToInsertWMergeKey
        .union(
            incDFWMergeKey
        )
    )

    # DEBUG
    nb_rows = stagedUpdates.count()
    print(f"Nb of rows: {nb_rows} - First 5 records of stagedUpdates:")
    stagedUpdates.show(5)
    
    # Apply SCD Type 2 operation using merge
    delta_table.alias("tgt").merge(
        stagedUpdates.alias("stgupd"),
        "tgt.uuid = stgupd.mergeKey"

    ).whenMatchedUpdate(
        # By design, when there is a match on the primary key (mergeKey==uuid),
        # the corresponding records of the stgupd data set are exactly the ones
        # of the incremental data set, that is, both records with a change and
        # records without. Hence, an additional condition has to be added so as
        # to filter on only the changed records
        condition = "tgt.is_current = true AND (tgt.company != stgupd.company or tgt.job != stgupd.job)",

        # Set is_current to false and end_date to today's date. The validity of the
        # old record/row ends today: it is now superceded by the new record to be
        # inserted in the whenNotMatchedInsert() clause below
        set={
            "is_current": F.lit(False),
            "end_date": F.current_date()
        }

    ).whenNotMatchedInsert(
        # By design, when there is no match on the primary key (mergeKey==NULL),
        # the corresponding records of the stgupd data set are the ones with a
        # change. The target dataset (the data set stored as a table) is therefore
        # updated with the records of the stgupd data set

        # Set is_current to true and the end_date, along with the other potential
        # changes

        # For the full list of field names and types, see
        # https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/001-scd2-w-delta/src/001_scd2_w_delta/ddl.py
        values = {
            "name": F.col("stgupd.name"),
            "username": F.col("stgupd.username"),
            "mail": F.col("stgupd.mail"),
            "ssn": F.col("stgupd.ssn"),
            "company": F.col("stgupd.company"),
            "job": F.col("stgupd.job"),
            "address": F.col("stgupd.address"),
            "residence": F.col("stgupd.residence"),
            "birthdate": F.col("stgupd.birthdate"),
            "sex": F.col("stgupd.sex"),
            "blood_group": F.col("stgupd.blood_group"),
            "website": F.col("stgupd.website"),
            "current_location_lat": F.col("stgupd.current_location_lat"),
            "current_location_lon": F.col("stgupd.current_location_lon"),
            # Added fields for SCD2
            "start_date": F.current_date().cast("date"),
            "end_date": F.lit("9999-12-31").cast("date"),
            "is_current": F.lit(True),
        }

    ).execute()

def main() -> None:
    # Retrieve the Spark session
    spark = getSparkSession()

    # Read the initial customer dataset and save it in the Detla table
    processCustomerInit(spark=spark)

    # Read the incremental customer dataset and merge it in the Detla table
    processCustomerInc1(spark=spark)

if __name__ == "__main__":
    main()

