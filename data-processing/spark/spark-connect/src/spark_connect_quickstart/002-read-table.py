#!/usr/bin/env python
#
#
#

#
k_table = "dim_customer"

# Read the table
df = spark.read.table(k_table)

# Reporting
nb_rows = df.count()
print(f"Number of rows in the {k_table} table: {nb_rows}")

