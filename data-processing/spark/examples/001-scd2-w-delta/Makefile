#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/001-scd2-w-delta/Makefile
#

PYTHON_VERSION := 3.12
SCALA_VERSION := 2.13
SPARK_VERSION := 4.1.1 # 3.5.2
DELTA_VERSION := 4.1.0 # 3.2.0
# Dataset (dst) setup (stp) directory
DSTSTP_DIR := ../000-data-setup
# Customer (cst) dataset (dst)
CSTDST_DIR := dim_customer

UV ?= uv

# Cleaners
clean-database: ## Clean database
	rm -rf derby.log metastore_db spark-warehouse $(CSTDST_DIR)

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
	@$(MAKE) -C $(DSTSTP_DIR) clean-datasets

cleaners: clean-database clean-logs clean-python clean-package clean-install clean-datasets ## Clean everything

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
	@$(MAKE) check-database

init-database-purepython: ## Initialize the Delta tables
	spark-submit \
		--packages io.delta:delta-spark_$(SCALA_VERSION):$(DELTA_VERSION) \
	  	--conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
	  	--conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog" \
		src/001_scd2_w_delta/ddl.py
	@$(MAKE) check-database

init-datasets: ## Generate sample datasets
	@$(MAKE) -C $(DSTSTP_DIR) init-datasets

check-dataset-init: ## Analyze the initial data-set
	@$(MAKE) -C $(DSTSTP_DIR) check-dataset-init

check-dataset-incremental: ## Analyze the incremental data-set
	@$(MAKE) -C $(DSTSTP_DIR) check-dataset-incremental

check-database: ## Check the content of the Spark database, if existing
	@echo "Checking whether the the $(CSTDST_DIR)/ directory has been created..."
	@$(eval DB_CUST_DIR=$(shell find . -type d -name '$(CSTDST_DIR)' | head -1))
	@echo "Resulting DB_CUST_DIR: $(DB_CUST_DIR)"
	@if [ -d "$(DB_CUST_DIR)" ]; then \
		echo "Delta table generated in $(DB_CUST_DIR)/ . Content of that directory:"; \
		ls -lFh $(DB_CUST_DIR); \
	else \
		echo "The $(CSTDST_DIR)/ directory cannot be found. Be sure to execute 'make init-database'"; \
	fi

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
browse-database: ## Browse the Delta tables
	@$(MAKE) check-database
	spark-sql \
		--packages io.delta:delta-spark_$(SCALA_VERSION):$(DELTA_VERSION) \
	  	--conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
	  	--conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog" \
	  < sql/select-dim-customer-limit10.sql

browse-database-purepython: ## Check the Delta tables
	@$(MAKE) check-database
	spark-submit \
		--packages io.delta:delta-spark_$(SCALA_VERSION):$(DELTA_VERSION) \
	  	--conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
	  	--conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog" \
	  src/001_scd2_w_delta/select-dim-customer-limit10.py

#
ingest-datasets: ## Ingest the customer-related datasets (initial and incremental)
	@$(MAKE) check-database
	@echo "Check logs/ingest-datasets.log"
	mkdir -p logs
	time spark-submit \
		--packages io.delta:delta-spark_$(SCALA_VERSION):$(DELTA_VERSION) \
	  	--conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
	  	--conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog" \
	  src/001_scd2_w_delta/spark-merge-customer.py > logs/ingest-datasets.log 2>&1
	@$(MAKE) check-database

