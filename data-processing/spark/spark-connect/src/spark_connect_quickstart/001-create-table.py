#!/usr/bin/env python
#
#
#

#
k_table = "dim_customer"
k_data_dir = f"data/{k_table}/init/"

# Read the data-set
df = spark.read.load(k_data_dir)

# Reporting
nb_rows = df.count()
print(f"Number of rows in {k_data_dir}: {nb_rows}")

# Write the data set as a table
df.write.mode("overwrite").saveAsTable(k_table)
print(f"Wrote the data-set as a table, namely {k_table}")

