#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/000-data-setup/Makefile
#

PYTHON_VERSION := 3.12
SCALA_VERSION := 2.13
SPARK_VERSION := 4.1.1 # 3.5.2
DELTA_VERSION := 4.1.0 # 3.2.0
DATA_DIR := ../data
DATA_CUST_DIR := $(DATA_DIR)/dim_customer

UV ?= uv

# Cleaners
clean-db: ## Clean database
	rm -rf derby.log metastore_db spark-warehouse

clean-logs: ## Clean log files
	rm -rf logs

clean-python: ## Clean Python-related objects
	find . -type f -name '*.py[co]' -delete
	find . -type d -name __pycache__ -delete
	rm -f requirements.txt

clean-package: ## Clean the project package.
	rm -rf dist/

clean-install: ## Clean the project installation.
	rm -rf .venv/

clean-datasets: ## Clean generated datasets
	rm -rf $(DATA_CUST_DIR)/init $(DATA_CUST_DIR)/inc1

cleaners: clean-db clean-logs clean-python clean-package clean-install clean-datasets ## Clean everything

# Initializers
init-uv-python: ## Install Python $(PYTHON_VERSION) if necessary
	uv python install $(PYTHON_VERSION)

init-pyspark: ## Install PySpark and Delta Lake in the current Python environment (not the uv virtual one)
	python -mpip install --force-reinstall \
		pyspark==$(SPARK_VERSION) delta-spark==$(DELTA_VERSION)

init-database: ## Initialize the Delta tables
	spark-sql \
		--packages io.delta:delta-spark_$(SCALA_VERSION):$(DELTA_VERSION) \
	  	--conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
	  	--conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog" \
	  < sql/ddl.sql
	echo "Delta table generated in spark-warehouse/dim_customer/"
	ls -lFh spark-warehouse/dim_customer/

init-database-purepython: ## Initialize the Delta tables
	uv run spark-submit \
		--packages io.delta:delta-spark_$(SCALA_VERSION):$(DELTA_VERSION) \
	  	--conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
	  	--conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog" \
		src/001_scd2_w_delta/ddl.py
	echo "Delta table generated in spark-warehouse/dim_customer/"
	ls -lFh spark-warehouse/dim_customer/

init-datasets: ## Generate sample datasets
	@pyspark < src/000_data_setup/generate_customer_datasets.py
	@echo "Customer data source generated in $(DATA_CUST_DIR)/"
	@command -v tree > /dev/null && tree $(DATA_CUST_DIR)/ || echo "The tree command does not seem to be installed. Please install it to analyze the content of the local file-system"

check-dataset-init: ## Analyze the initial data-set
	uv run datanomy $(DATA_CUST_DIR)/init/part*.parquet

check-dataset-incremental: ## Analyze the incremental data-set
	uv run datanomy $(DATA_CUST_DIR)/inc1/part*.parquet

#
init: ## Setup Python virtual environment
	@uv lock
	@uv export --format requirements.txt > requirements.txt

update: ## Update the dependencies
	@uv sync
	@uv export --format requirements.txt > requirements.txt

build: ## Build the software artifact (wheel)
	@uv build

#
check-database: ## Check the Delta tables
	uv run spark-sql \
		--packages io.delta:delta-spark_$(SCALA_VERSION):$(DELTA_VERSION) \
	  	--conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
	  	--conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog" \
	  < sql/select-dim-customer-limit10.sql
	echo "Delta table generated in spark-warehouse/dim_customer/"
	ls -lFh spark-warehouse/dim_customer/

check-database-purepython: ## Check the Delta tables
	uv run spark-submit \
		--packages io.delta:delta-spark_$(SCALA_VERSION):$(DELTA_VERSION) \
	  	--conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
	  	--conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog" \
	  src/001_scd2_w_delta/select-dim-customer-limit10.py
	echo "Delta table generated in spark-warehouse/dim_customer/"
	ls -lFh spark-warehouse/dim_customer/

#
ingest-datasets: ## Ingest the customer-related datasets (initial and incremental)
	@echo "Check logs/ingest-datasets.log"
	mkdir -p logs
	time uv run spark-submit \
		--packages io.delta:delta-spark_$(SCALA_VERSION):$(DELTA_VERSION) \
	  	--conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
	  	--conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog" \
	  src/001_scd2_w_delta/spark-merge-customer.py > logs/ingest-datasets.log 2>&1
	echo "Delta table updated in spark-warehouse/dim_customer/"
	ls -lFh spark-warehouse/dim_customer/

