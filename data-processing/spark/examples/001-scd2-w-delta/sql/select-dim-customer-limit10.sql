--
-- File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/sql/select-dim-customer-limit10.sql
--

desc dim_customer;

select count(*) as nb_rows from dim_customer;

select * from dim_customer limit 10;
