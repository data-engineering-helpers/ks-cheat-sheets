#!/usr/bin/env python
#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/001-scd2-w-delta/src/001_scd2_w_delta/jobs/merge_customer_002_uc_only.py
#

from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import delta.tables as dt

#
cust_init_dataset = "../data/dim_customer/init"
cust_inc_dataset1 = "../data/dim_customer/inc1"
delta_table_name = "unityxt.bronze.dim_customer"

def getSparkSession() -> SparkSession:
    # .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    # .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    # .enableHiveSupport()
    spark = (
        SparkSession.builder.appName("scd2-app-uc-only")
        .getOrCreate()
    )
    return spark

def displayCustTableHdr(spark: SparkSession):
    df_table = spark.sql(f"select * from {delta_table_name}")
    nb_rows = df_table.count()
    df_table_hdr = df_table.limit(5).toPandas()
    print(f"Nb of rows: {nb_rows} - First 5 records of {delta_table_name}:")
    print(df_table_hdr)

def processCustomerInit(spark: SparkSession):
    source_df = spark.read.parquet(cust_init_dataset)

    # DEBUG
    nb_rows_init = source_df.count()
    print(f"Nb of rows in {cust_init_dataset}: {nb_rows_init}")

    # Add metadata fields
    source_df = source_df.withColumn("start_date",
                                     F.current_date().cast("date"))
    source_df = source_df.withColumn("end_date",
                                     F.lit("9999-12-31").cast("date"))
    source_df = source_df.withColumn("is_current", F.lit(True))

    # Retrieve the Delta table if existing, otherwise fill it
    # if dt.DeltaTable.isDeltaTable(spark, delta_table_name):
    try:
        delta_table = dt.DeltaTable.forName(spark, delta_table_name)
        print(f"{delta_table_name} Delta table exists. All is fine")
        print(
            f"Replacing the {delta_table_name} Delta table by the content of the "
            f"initial dataset ({cust_init_dataset})"
        )

        # The following works well, but it is in SQL, not in pure Python. Neverthless,
        # the alternatives do not fully work:
        # * The "append" mode is not idempotent (as everytime the records are appended)
        # * The overwrite mode triggers an exception by the Spark engine. That holds
        #   true for both direct access to Unity Catalog (UC) and for indirect access
        #   through Spark Connect (SC), itself connected to United Catalog (UC),
        #   eventhough the exception may not be the same.
        # Hence, apparently, we cannot have a pure Python overwrite clause: it is
        # either SQL (and idempotent) or not idempotent (append)
        source_df.createTempView("source_df")
        spark.sql(f"insert overwrite {delta_table_name} select * from source_df;")

        print(f"{delta_table_name} Delta table has been successfully rewritten")

        # The following does not work when Spark directly invokes Unity Catalog (UC),
        # and does not work either when Spark connects to Spark Connect (SC), itself
        # connected to Unity Catalog. See also merge_customer_004_sc_and_uc.py
        # source_df.write.format("delta").mode("overwrite").saveAsTable(delta_table_name)

        # The following is kept for reference only. Indeed, that operation is not
        # idempotent (as the initial dataset is added every time the Python script is
        # called). Yet, for that simple tutorial, it would be fine, as the whole
        # purpose is to showcase the merge feature of the Delta table in the
        # processCustomerInc1() method (see below)
        # source_df.write.format("delta").mode("append").saveAsTable(delta_table_name)
        
        # DEBUG
        displayCustTableHdr(spark=spark)

    except:
        import sys
        e = sys.exc_info()[0]
        print(f"Error: {e}")
        
        print(
            f"There was an issue with the {delta_table_name} Delta table. "
            "Potentially execute make init-uc-table"
        )

def processCustomerInc1(spark: SparkSession):
    inc_df = spark.read.parquet(cust_inc_dataset1)

    # DEBUG
    nb_rows_inc = inc_df.count()
    print(f"Nb of rows in {cust_inc_dataset1}: {nb_rows_inc}")

    # Add metadata fields
    inc_df = inc_df.withColumn("start_date", F.current_date().cast("date"))
    inc_df = inc_df.withColumn("end_date", F.lit("9999-12-31").cast("date"))
    inc_df = inc_df.withColumn("is_current", F.lit(True))

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
    print("Merging the incremental dataset ({cust_inc_dataset1}) into {delta_table_name} Delta table...")

    delta_table.alias("tgt").merge(
        inc_df.alias("src"),
        "tgt.name = src.name and tgt.is_current = true"

    ).whenMatchedUpdate(
        condition="tgt.company != src.company or tgt.job != src.job",
        set={
            "is_current": F.lit(False),
            "end_date": F.current_date()
        }

    ).whenNotMatchedInsert(
        values = {
            "name": F.col("src.name"),
            "company": F.col("src.company"),
            "job": F.col("src.job"),
            "address": F.col("src.address"),
            "birthdate": F.col("src.birthdate"),
            "start_date": F.col("src.start_date"),
            "end_date": F.col("src.end_date"),
            "is_current": F.col("src.is_current"),
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

