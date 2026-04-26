#!/usr/bin/env python
#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/001-scd2-w-delta/src/001_scd2_w_delta/jobs/merge_customer_002_uc_only.py
#

from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import delta.tables as dt

#
k_spark_version = "4.1"
k_scala_version = "2.13"
k_dl_version = "4.2.0"
k_uc_version = "0.5.0-SNAPSHOT"

#
k_dl_jar_package = f"io.delta:delta-spark_{k_spark_version}_{k_scala_version}:{k_dl_version}"
k_uc_jar_package = f"io.unitycatalog:unitycatalog-spark_{k_scala_version}:{k_uc_version}"
k_all_jars = f"{k_dl_jar_package},{k_uc_jar_package}"

#
k_uc_url = "http://localhost:8080"
catalog_name = "unityxt"
schema_name = "bronze"
table_name = "dim_customer"
delta_table_name = f"{catalog_name}.{schema_name}.{table_name}"
cust_init_dataset = f"../data/{table_name}/init"
cust_inc_dataset1 = f"../data/{table_name}/inc1"

def getSparkSession() -> SparkSession:
    spark = (
        SparkSession.builder.appName("scd2-app-uc-only")
        .config("spark.jars.packages", k_all_jars)
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config("spark.sql.catalog.spark_catalog",
                "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        .config(f"spark.sql.catalog.{catalog_name}",
                "io.unitycatalog.spark.UCSingleCatalog")
        .config(f"spark.sql.catalog.{catalog_name}.uri", k_uc_url)
        .config(f"spark.sql.catalog.{catalog_name}.token", "")
        .config(f"spark.sql.defaultCatalog", catalog_name)
        .getOrCreate()
    )

    # DEBUG
    # spark_conf_str = spark.sparkContext.getConf().getAll()
    # print(f"Spark conf: {spark_conf_str}")

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

