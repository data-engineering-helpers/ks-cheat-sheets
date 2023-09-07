--
-- File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/sql/create-geonames-tables.sql
--
-- Tables for Geonames data
--

--
-- Table structure for table admin1_codes_ascii
--

DROP TABLE IF EXISTS admin1_codes_ascii;
CREATE TABLE admin1_codes_ascii (
  ccode char(2) NOT NULL,
  code varchar(7) NOT NULL,
  name text NOT NULL,
  nameAscii text default NULL,
  geonameid integer NOT NULL
);


--
-- Table structure for table admin2_codes
--

DROP TABLE IF EXISTS admin2_codes;
CREATE TABLE admin2_codes (
  ccode char(2) NOT NULL,
  code1 varchar(7) default NULL,
  code2 varchar(100) NOT NULL,
  name_local text default NULL,
  name text NOT NULL,
  geonameid integer NOT NULL
);


--
-- Table structure for table airports_pageranked
--

DROP TABLE IF EXISTS airport_pageranked;
CREATE TABLE airport_pageranked (
 iata_code char(3) NOT NULL,
 location_type varchar(4) default NULL,
 page_rank decimal(15,12) NOT NULL
);


--
-- Table structure for table alternate_name
--

DROP TABLE IF EXISTS alternate_name;
CREATE TABLE alternate_name (
  alternatenameId integer NOT NULL,
  geonameid integer default NULL,
  isoLanguage varchar(7) default NULL,
  alternateName varchar(200) default NULL,
  isPreferredName boolean default NULL,
  isShortName boolean default NULL,
  isColloquial boolean default NULL,
  isHistoric boolean default NULL
);


--
-- Table structure for table continent_codes
--

DROP TABLE IF EXISTS continent_codes;
CREATE TABLE continent_codes (
  code char(2) NOT NULL,
  name varchar(20) default NULL,
  geonameid integer default NULL
);


--
-- Table structure for table country_info
--

DROP TABLE IF EXISTS country_info;
CREATE TABLE country_info (
  iso_alpha2 char(2) default NULL,
  iso_alpha3 char(3) default NULL,
  iso_numeric integer default NULL,
  fips_code varchar(3) default NULL,
  name varchar(200) default NULL,
  capital varchar(200) default NULL,
  areainsqkm float default NULL,
  population integer default NULL,
  continent char(2) default NULL,
  tld varchar(4) default NULL,
  currency_code char(3) default NULL,
  currency_name varchar(32) default NULL,
  phone varchar(16) default NULL,
  postal_code_format varchar(64) default NULL,
  postal_code_regex varchar(256) default NULL,
  languages varchar(200) default NULL,
  geonameId integer default NULL,
  neighbours varchar(64) default NULL,
  equivalent_fips_code varchar(3) default NULL
);


--
-- Table structure for table feature_classes
--

DROP TABLE IF EXISTS feature_classes;
CREATE TABLE feature_classes (
  class char(1) NOT NULL,
  names varchar(200) default NULL
);


--
-- Table structure for table feature_codes
--

DROP TABLE IF EXISTS feature_codes;
CREATE TABLE feature_codes (
  class char(1) NOT NULL,
  code varchar(5) NOT NULL,
  name_en varchar(200) default NULL,
  description_en text default NULL,
  name_ru varchar(200) default NULL,
  description_ru text default NULL
);


--
-- Table structure for table geoname
--

DROP TABLE IF EXISTS geoname;
CREATE TABLE geoname (
  geonameid integer NOT NULL,
  name varchar(200) default NULL,
  asciiname varchar(200) default NULL,
  alternatenames varchar(4000) default NULL,
  latitude decimal(10,7) default NULL,
  longitude decimal(10,7) default NULL,
  fclass char(1) default NULL,
  fcode varchar(10) default NULL,
  country varchar(2) default NULL,
  cc2 varchar(60) default NULL,
  admin1 varchar(20) default NULL,
  admin2 varchar(80) default NULL,
  admin3 varchar(20) default NULL,
  admin4 varchar(20) default NULL,
  population integer default NULL,
  elevation integer default NULL,
  gtopo30 integer default NULL,
  timezone varchar(40) default NULL,
  moddate date default NULL
);


--
-- Table structure for table hierarchy
--

DROP TABLE IF EXISTS hierarchy;
CREATE TABLE hierarchy (
  parentId integer NOT NULL,
  childId integer NOT NULL,
  relationType varchar(20) NOT NULL
);


--
-- Table structure for table iso_language_codes
--

DROP TABLE IF EXISTS iso_language_codes;
CREATE TABLE iso_language_codes (
  iso_639_3 char(4) default NULL,
  iso_639_2 varchar(50) default NULL,
  iso_639_1 varchar(50) default NULL,
  language_name varchar(200) default NULL
);


--
-- Table structure for table time_zones
--

DROP TABLE IF EXISTS time_zones;
CREATE TABLE time_zones (
  country varchar(2) default NULL,
  timeZoneId varchar(200) default NULL,
  GMT_offset decimal(3,1) default NULL,
  DST_offset decimal(3,1) default NULL,
  raw_offset decimal(3,1) default NULL
);


--
-- Table structure for table zip_codes
--

DROP TABLE IF EXISTS zip_codes;
CREATE TABLE zip_codes (
  iso_alpha2 char(2) default NULL,
  postal_code varchar(10) default NULL,
  place_name varchar(200) default NULL,
  admin_name1 varchar(100) default NULL,
  admin_code1 varchar(20) default NULL,
  admin_name2 varchar(100) default NULL,
  admin_code2 varchar(20) default NULL,
  admin_name3 varchar(100) default NULL,
  latitude decimal(10,7) default NULL,
  longitude decimal(10,7) default NULL,
  accuracy integer default NULL
);

