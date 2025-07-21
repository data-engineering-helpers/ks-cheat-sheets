--
-- File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/sql/ddl.sql
--
-- The schema corresponds to Faker profiles:
-- https://faker.readthedocs.io/en/master/providers/faker.providers.profile.html
-- The structure and array have been removed for simplification purpose,
-- so as to ease the Delta merging
--

drop table if exists dim_customer;

create table dim_customer (
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
location 'dim_customer';

