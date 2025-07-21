--
-- File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/sql/ddl.sql 
--
-- The schema corresponds to Faker profiles:
-- https://faker.readthedocs.io/en/master/providers/faker.providers.profile.html
--

drop table if exists dim_customer;

create table dim_customer (
  address string,
  birthdate date,
  blood_group string,
  company string,
  current_location struct <_1 double, _2 double>,
  job string,
  mail string,
  name string,
  residence string,
  sex string,
  ssn string,
  username string,
  website array <string>,
  start_date date,
  end_date date,
  is_current boolean
)
using delta
location 'metastore/dim_customer';

