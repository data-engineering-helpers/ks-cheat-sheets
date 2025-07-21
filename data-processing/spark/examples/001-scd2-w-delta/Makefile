#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/001-scd2-w-delta/Makefile
#

PYTHON_VERSION := 3.12
SPARK_VERSION := 3.5.2
DELTA_VERSION := 3.2.0

# Cleaners
clean-db: ## Clean database
	rm -rf derby.log metastore_db spark-warehouse

clean-python: ## Clean Python-related objects
	rm -rf .venv

cleaners: clean-db clean-python ## Clean everything

# Initializers
init-uv-python: ## Install Python 3.12 if necessary
	uv python install $(PYTHON_VERSION)

init-uv: ## Initialize the uv-managed Python environment
	uv venv --clear --python $(PYTHON_VERSION)
	uv run pip install pyspark==$(SPARK_VERSION) delta-spark==$(DELTA_VERSION)

init-python: ## Initialize Python environment
	python -mpip install -U pip
	python -mpip install pyspark==$(SPARK_VERSION) delta-spark==$(DELTA_VERSION)
	python -mpip install -U faker

init-data-source: ## Generate Parquet source data file
	pyspark < spark-generate-customer-increment.py
	echo "Customer data source generated in dim_customer/"
	ls -lFh dim_customer/

