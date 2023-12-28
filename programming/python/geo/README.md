Cheat Sheets - Python - Geography-related work
==============================================

# Table of Content (ToC)
* [Overview](#overview)
* [References](#references)
  * [Data Engineering helpers](#data-engineering-helpers)
  * [Blog articles](#blog-articles)
  * [Samples of data analysis](#samples-of-data-analysis)
    * [New\-York taxis](#new-york-taxis)
      * [Data preparation](#data-preparation)
    * [Analyzing changes in geospatial data](#analyzing-changes-in-geospatial-data)
* [References](#references-1)
  * [DataBricks notebooks](#databricks-notebooks)
    * [Constructing hexagon maps with H3 and Plotly](#constructing-hexagon-maps-with-h3-and-plotly)
      * [Data](#data)
  * [Use cases](#use-cases)
  * [Data sets](#data-sets)
    * [GeoJSON\-XYZ](#geojson-xyz)
  * [Tools/libraries](#toolslibraries)
    * [GeoJSON](#geojson)
    * [GeoPandas](#geopandas)
      * [Contextily](#contextily)
    * [Graviz](#graviz)
    * [Cartopy](#cartopy)
    * [Geospatial projections](#geospatial-projections)
    * [Choropleth map](#choropleth-map)
    * [H3](#h3)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/python/geo/README.md)
references material about data analysis related to geography with Python.

# References

## Data Engineering helpers
* [Data Engineering Helpers - Knowledge Sharing - DataBricks examples](https://github.com/data-engineering-helpers/databricks-examples)


## Blog articles
* [Medium - How to Create a Simple GIS Map with Plotly and Streamlit](https://towardsdatascience.com/how-to-create-a-simple-gis-map-with-plotly-and-streamlit-7732d67b84e2)
  + Date: Dec. 2023
  + Author: Alan Jones
  ([Alan Jones on Medium](https://medium.com/@alan-jones),
  [Alan Jones on LinkedIn](https://www.linkedin.com/in/alan-jones-032699100/))
  + Publisher: Medium TowardsDataScience
* Source: [Medium - 5 Visualizations with Python to Show Simultaneous Changes in Geospatial Data](https://towardsdatascience.com/5-visualizations-with-python-to-show-simultaneous-changes-in-geospatial-data-ddc2eaab9d78)
  + Date: Nov. 2023
  + Author: Boriharn K.
  ([Boriharn K. on Medium](https://medium.com/@borih.k)
* [Medium - 5 Visualizations with Python to Show Simultaneous Changes in Geospatial Data](https://towardsdatascience.com/5-visualizations-with-python-to-show-simultaneous-changes-in-geospatial-data-ddc2eaab9d78)
  + Date: Nov. 2023
  + Author: Boriharn K.
* [IBM - What is geospatial data?](https://www.ibm.com/topics/geospatial-data)

## Samples of data analysis

### New-York taxis
* [TLC - NYC taxi data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
* Data Dictionaries and MetaData
  + [Trip Record User Guide (PDF)](https://www.nyc.gov/assets/tlc/downloads/pdf/trip_record_user_guide.pdf)
  + [Yellow Trips Data Dictionary (PDF)](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf)
  + [Green Trips Data Dictionary (PDF)](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_green.pdf)
  + [FHV Trips Data Dictionary (PDF)](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_fhv.pdf)
  + [High Volume FHV Trips Data Dictionary (PDF)](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_hvfhs.pdf)
  + [Working With Parquet Format (PDF)](https://www.nyc.gov/assets/tlc/downloads/pdf/working_parquet_format.pdf)
* [GitHub - Data Engineering Helpers - DataBricks notebook - GeoPandas](https://github.com/data-engineering-helpers/databricks-examples/blob/main/ipython-notebooks/demos-geo-geopandas-nyc-taxi-trips.ipynb)

#### Data preparation
* [GitHub - NYC taxi data preparation](https://github.com/toddwschneider/nyc-taxi-data)
* Original notebook:
  https://www.databricks.com/notebooks/prep-nyc-taxi-geospatial-data.html
  + => [GitHub - Data Engineering Helpers - DataBricks notebook - prep-nyc-taxi-geospatial-data](https://github.com/data-engineering-helpers/databricks-examples/blob/main/ipython-notebooks/demos-geo-prep-nyc-taxi-geospatial-data.ipynb)
  (forked notebook to adapt with new format of data)

### Analyzing changes in geospatial data
# References
* Source: [Medium - 5 Visualizations with Python to Show Simultaneous Changes in Geospatial Data](https://towardsdatascience.com/5-visualizations-with-python-to-show-simultaneous-changes-in-geospatial-data-ddc2eaab9d78)
  + Date: Nov. 2023
  + Author: Boriharn K.
* [GitHub - Geojson-XYZ](https://github.com/geojson-xyz)
* [IBM - What is geospatial data?](https://www.ibm.com/topics/geospatial-data)
* [Wikipedia - List of U.S. states and territories by income](https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_income)
* [Wikipedia - Choropleth map](https://en.wikipedia.org/wiki/Choropleth_map)

## DataBricks notebooks
* [GitHub - Data Engineering Helpers - DataBricks notebook - Show Simultaneous Changes in Geospatial Data - Part 1](https://github.com/data-engineering-helpers/databricks-examples/blob/main/ipython-notebooks/demos-geo-show-simultaneous-changes-in-geospatial-data-1_2.ipynb)
* [GitHub - Data Engineering Helpers - DataBricks notebook - Show Simultaneous Changes in Geospatial Data - Part 2](https://github.com/data-engineering-helpers/databricks-examples/blob/main/ipython-notebooks/demos-geo-show-simultaneous-changes-in-geospatial-data-2_2.ipynb)
* [GitHub - Data Engineering Helpers - DataBricks notebook - Python Contextily package](https://github.com/data-engineering-helpers/databricks-examples/blob/main/ipython-notebooks/demos-geo-python-contextily-package.ipynb)
* [GitHub - Data Engineering Helpers - DataBricks notebook - Spatial projections](https://github.com/data-engineering-helpers/databricks-examples/blob/main/ipython-notebooks/demos-geo-spatial-projections.ipynb)

### Constructing hexagon maps with H3 and Plotly
* [GitHub - Data Engineering Helpers - DataBricks notebook - Constructing Hexagon Maps with H3 and Plotly: A Comprehensive Tutorial](https://github.com/data-engineering-helpers/databricks-examples/blob/main/ipython-notebooks/demos-geo-constructing-hexagon-maps-with-h3-and-plotly.ipynb)
* Original article:
  + [Medium - Constructing Hexagon Maps with H3 and Plotly: A Comprehensive Tutorial](https://towardsdatascience.com/constructing-hexagon-maps-with-h3-and-plotly-a-comprehensive-tutorial-8f37a91573bb)
  + Date: Nov. 2023
  + Author: Amanda Iglesias Moreno
    ([Amanda Iglesias Moreno on LinkedIn](https://www.linkedin.com/in/amanda-iglesias-moreno-55029417a/))

#### Data
* Home page:
  https://opendata-ajuntament.barcelona.cat/data/en/dataset/allotjaments-hotels
* [URL to download the CSV](https://opendata-ajuntament.barcelona.cat/data/dataset/88efe464-2bcd-4794-85b0-8b0bbfd9e4c0/resource/9bccce1b-0b9d-4cc6-94a7-459cb99450de/download)
* The resulting CSV is encoded with UTF-16
  + Convert it to UTF-8 with `dos2unix opendatabcn_allotjament_hotels-csv.csv`
  + Upload it somewhere on the DataBricks workspace

## Use cases


## Data sets
* [Wikipedia - List of U.S. states and territories by income](https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_income)

### GeoJSON-XYZ
* [GeoJSON-XYZ data sets](https://geojson.xyz/)
* [GitHub - Geojson-XYZ organization](https://github.com/geojson-xyz)
* Description: GeoJSON data sets

## Tools/libraries

### GeoJSON
* Home page: https://geojson.org/
* [The GeoJSON Specification (RFC 7946)](https://tools.ietf.org/html/rfc7946)
* Description: format for encoding a variety of geographic data structures

### GeoPandas
* GeoPandas home page: https://geopandas.org/en/stable/
* GitHub page: https://github.com/geopandas/geopandas
* Description: Python tools for geographic data

#### Contextily
* Contextily home page:
  https://contextily.readthedocs.io/en/latest/intro_guide.html
* [Introduction guide to contextily — contextily 1.1.0 documentation](https://contextily.readthedocs.io/en/latest/intro_guide.html)
* GitHub page: https://github.com/geopandas/contextily
* Description: context geo tiles in Python with GeoPandas

### Graviz
* Gravis documentation: https://robert-haas.github.io/gravis-docs/
* GitHub page: https://github.com/robert-haas/gravis
* Gravis on Pypi: https://pypi.org/project/gravis/
* Description: interactive graph visualizations with Python and HTML/CSS/JS

### Cartopy
* Cartopy documentation: https://scitools.org.uk/cartopy/docs/latest/
* GitHub page: https://github.com/SciTools/cartopy
* Description: Python package designed to make drawing maps for data analysis
  and visualisation easy

### Geospatial projections
* Cylindrical Equal Area (CEA)(projection preserving areas):
  https://proj.org/operations/projections/cea.html
* Very detailed answer on GIS Stack Exchange/Stack Overflow:
  https://gis.stackexchange.com/a/401815/23550

### Choropleth map
* [Wikipedia - Choropleth map](https://en.wikipedia.org/wiki/Choropleth_map)

### H3
* Home page: https://h3geo.org/
* H3 bindings for Python (`h3-py`): https://github.com/uber/h3-py
* [DataBricks doc - Native H3 support by DataBricks](https://docs.databricks.com/en/sql/language-manual/sql-ref-h3-geospatial-functions.html#language-python)

