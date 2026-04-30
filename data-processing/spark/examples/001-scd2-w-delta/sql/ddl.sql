--
-- File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/001-scd2-w-delta/sql/ddl.sql
--
-- The schema corresponds to Faker profiles:
-- https://faker.readthedocs.io/en/master/providers/faker.providers.profile.html
-- The structure and array have been removed for simplification purpose,
-- so as to ease the Delta merging
--

--
-- Schema: Bronze in local; it may differ in remote environments
--
create schema if not exists bronze;

--
-- Drop the table
--
drop table if exists bronze.dim_customer;

--
-- Create the table
--
create table bronze.dim_customer (
  uuid string,
  address string,
  birthdate date,
  blood_group string,
  company string,
  current_location_lat double,
  current_location_lon double,
  job string,
  mail string,
  name string,
  residence string,
  sex string,
  ssn string,
  username string,
  website string,
  start_date date,
  end_date date,
  is_current boolean
)
using delta
--location 'dim_customer'
;

