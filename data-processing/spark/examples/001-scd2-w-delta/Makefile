#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/001-scd2-w-delta/Makefile
#

PYTHON_VERSION := 3.12
SPARK_VERSION := 3.5.2
DELTA_VERSION := 3.2.0

# Cleaners
clean-db: ## Clean database
	rm -rf derby.log metastore_db spark-warehouse

clean-logs: ## Clean log files
	rm -rf logs

clean-python: ## Clean Python-related objects
	rm -rf .venv

clean-datasets: ## Clean generated datasets
	rm -rf data/dim_customer/init data/dim_customer/inc1

cleaners: clean-db clean-logs clean-python clean-datasets ## Clean everything

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

init-database: ## Initialize the Delta tables
	spark-sql --packages io.delta:delta-spark_2.12:${DELTA_VERSION} \
	  --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
	  --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog" \
	  < sql/ddl.sql
	echo "Delta table generated in spark-warehouse/dim_customer/"
	ls -lFh spark-warehouse/dim_customer/

init-datasets: ## Generate Parquet source data file
	pyspark < spark-generate-customer-increment.py
	echo "Customer data source generated in data/dim_customer/"
	tree data/dim_customer/

check-database: ## Check the Delta tables
	spark-sql --packages io.delta:delta-spark_2.12:${DELTA_VERSION} \
	  --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
	  --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog" \
	  < sql/select-dim-customer-limit10.sql
	echo "Delta table generated in spark-warehouse/dim_customer/"
	ls -lFh spark-warehouse/dim_customer/

ingest-datasets: ## Ingest the customer-related datasets (initial and incremental)
	@echo "Check logs/ingest-datasets.log"
	mkdir -p logs
	time spark-submit --packages io.delta:delta-spark_2.12:${DELTA_VERSION} \
	  --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
	  --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog" \
	  spark-merge-customer.py > logs/ingest-datasets.log 2>&1
	echo "Delta table updated in spark-warehouse/dim_customer/"
	ls -lFh spark-warehouse/dim_customer/

