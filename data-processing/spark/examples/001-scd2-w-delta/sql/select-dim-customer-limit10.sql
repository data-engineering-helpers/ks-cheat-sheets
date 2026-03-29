--
-- File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/sql/001-scd2-w-delta/select-dim-customer-limit10.sql
--

-- Provide more details for the Delta table
desc extended bronze.dim_customer;

-- History of the Delta table
desc history bronze.dim_customer;

-- Number of rows
select count(*) as nb_rows from bronze.dim_customer;

-- First 10 rows
select * from bronze.dim_customer limit 10;

