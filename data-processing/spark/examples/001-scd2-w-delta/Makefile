#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/001-scd2-w-delta/Makefile
#

#SHELL := /bin/bash

PYTHON_VERSION := 3.12
SCALA_VERSION := 2.13
SPARK_VERSION := 4.1.1 # 3.5.2
DL_VERSION := 4.1.0 # 3.2.0
DL_JAR := $(strip delta-spark_$(SCALA_VERSION):$(DL_VERSION))
DL_SC_SVR_JAR := $(strip delta-connect-server_$(SCALA_VERSION):$(DL_VERSION))
DL_SC_CLT_JAR := $(strip delta-connect-client_$(SCALA_VERSION):$(DL_VERSION))
DL_SQL_DOM := org.apache.spark.sql.delta.catalog
PB_DOM := com.google.protobuf
PB_VERSION := 3.25.1
PB_JAR := $(strip protobuf-java:$(PB_VERSION))
UC_VERSION := 0.5.0-SNAPSHOT
UC_DOM := io.unitycatalog
UC_JAR := unitycatalog-spark_$(SCALA_VERSION):$(UC_VERSION)
UC_DIR := $(HOME)/dev/infra/unitycatalog
SC_DOM := org.apache.spark
SC_JAR := $(strip spark-connect_$(SCALA_VERSION):$(SPARK_VERSION))
SC_URL = sc://localhost:15002
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

clean-uc-table: ## Clean the table in Unity Catalog (UC)
	@$(eval TBL_NAME=$(shell $(UC_DIR)/bin/uc table list --catalog unityxt --schema bronze --output json | jq -r '.[]|select(.name|contains("dim_customer"))|.name'))
	@if [ "$(TBL_NAME)" == "dim_customer" ]; then \
		$(UC_DIR)/bin/uc table delete --full_name unityxt.bronze.dim_customer ; \
	else \
		echo "Table dim_customer has not been created on UC in unityxt.bronze yet"; \
		echo "No need to delete it" ; \
	fi

clean-uc-schema: ## Clean the schema in Unity Catalog (UC)
	@$(UC_DIR)/bin/uc schema delete --full_name unityxt.bronze --force true

clean-uc-catalog: ## Clean the catalog in Unity Catalog (UC)
	@$(UC_DIR)/bin/uc catalog delete --name unityxt --force true

clean-uc-all: clean-uc-catalog ## Clean all about the unityxt catalog

clean-sc-table: ## Clean the Spark Connect (SC) table if needed
	@rm -rf spark-warehouse/bronze.db/dim_customer

# Initializers
init-uv-python: ## Install Python $(PYTHON_VERSION) if necessary
	uv python install $(PYTHON_VERSION)

init-log-dir: ## Create the logs directory if need
	@mkdir -p logs

init-pyspark: ## Install PySpark and Delta Lake in the current Python environment (not the uv virtual one)
	python -mpip install --force-reinstall \
		pyspark==$(SPARK_VERSION) delta-spark==$(DL_VERSION) \
		pyspark-client==$(SPARK_VERSION)

init-database: ## Initialize the Delta tables
	spark-sql \
		--packages io.delta:delta-spark_$(SCALA_VERSION):$(DL_VERSION) \
	  	--conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
	  	--conf "spark.sql.catalog.spark_catalog=$(DL_SQL_DOM).DeltaCatalog" \
	  < sql/ddl.sql
	@$(MAKE) check-database

init-database-purepython: ## Initialize the Delta tables
	spark-submit \
		--packages io.delta:delta-spark_$(SCALA_VERSION):$(DL_VERSION) \
	  	--conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
	  	--conf "spark.sql.catalog.spark_catalog=$(DL_SQL_DOM).DeltaCatalog" \
		src/001_scd2_w_delta/ddl.py
	@$(MAKE) check-database

init-database-sc: clean-sc-table init-log-dir ## Initialize the Delta tables on SC
	@echo "Creating the table on SC server. Check logs/init_database_sc.log"
	@pyspark --remote $(SC_URL) \
		--packages "io.delta:$(DL_SC_CLT_JAR),$(PB_DOM):$(PB_JAR)" \
		< src/001_scd2_w_delta/sc-ddl.py \
		> logs/init_database_sc.log 2>&1

init-uc-catalog: ## Initialize the unityxt catalog in Unity Catalog (UC)
	@$(UC_DIR)/bin/uc catalog create --name unityxt \
		--storage_root /tmp/unitycatalog/storage --comment "Extended catalog"

init-uc-schema: ## Initialize the unityxt.bronze catalog in Unity Catalog (UC)
	@$(UC_DIR)/bin/uc schema create --catalog unityxt --name bronze \
		--storage_root /tmp/unitycatalog/storage --comment "Bronze schema"

init-uc-table: ## Initialize the dim_customer table in Unity Catalog (UC)
	@$(UC_DIR)/bin/uc table create \
		--full_name unityxt.bronze.dim_customer \
		--columns "address string, birthdate date, blood_group string, \
		company string, job string, mail string, name string, residence string, \
		sex string, ssn string, username string, website string, \
		current_location_lat double, current_location_lon double, \
		start_date date, end_date date, is_current boolean" \
		--table_type MANAGED --format DELTA \
		--properties '{"key1": "value1", "key2": "value2"}'

init-uc-all: init-uc-catalog init-uc-schema init-uc-table ## Init everything in Unity Catalog (UC)

init-datasets: ## Generate sample datasets
	@$(MAKE) -C $(DSTSTP_DIR) init-datasets


## Spark Connect (SC)
start-sc-only: ## Start Spark Connect (SC) only
	@echo "Starting Spark Connect (SC) only"
	@unset SPARK_REMOTE; start-connect-server.sh \
		--packages "io.delta:$(DL_SC_SVR_JAR),$(PB_DOM):$(PB_JAR)" \
		--conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
		--conf "spark.connect.extensions.relation.classes=org.apache.spark.sql.connect.delta.DeltaRelationPlugin" \
		--conf "spark.connect.extensions.command.classes=org.apache.spark.sql.connect.delta.DeltaCommandPlugin" \
		--conf "spark.sql.catalog.spark_catalog=$(DL_SQL_DOM).DeltaCatalog"
	@echo "In order to stop the Spark Connect (SC) server: make stop-sc"

start-sc-and-uc: ## Start Spark Connect (SC), itself connected to UC
	@$(MAKE) check-uc
	@echo "Starting Spark Connect (SC), itself connected to Unity Catalog (UC)"
	@unset SPARK_REMOTE; start-connect-server.sh \
		--packages "io.delta:$(DL_SC_SVR_JAR),$(PB_DOM):$(PB_JAR),$(UC_DOM):$(UC_JAR)"\
	  	--conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
		--conf "spark.connect.extensions.relation.classes=org.apache.spark.sql.connect.delta.DeltaRelationPlugin" \
		--conf "spark.connect.extensions.command.classes=org.apache.spark.sql.connect.delta.DeltaCommandPlugin" \
        --conf "spark.sql.catalog.spark_catalog=$(UC_DOM).spark.UCSingleCatalog" \
        --conf "spark.sql.catalog.unityxt=$(UC_DOM).spark.UCSingleCatalog" \
        --conf "spark.sql.catalog.unityxt.uri=http://localhost:8080" \
        --conf "spark.sql.catalog.unityxt.token=" \
        --conf "spark.sql.defaultCatalog=unityxt"
	@echo "In order to stop the Spark Connect (SC) server: make stop-sc"

check-sc: ## Check whether Spark Connect (SC) runs
	@$(eval IS_SC_RUNNING=$(shell ps -ax|grep "class org.apache.spark.sql.connect.service.SparkConnectServer" | grep -o "Spark Connect"))
	@if [ "$(IS_SC_RUNNING)" == "Spark Connect Spark Connect" ]; then \
		echo "Spark Connect (SC) seems to be running"; \
	else \
		echo "Spark Connect (SC) does not seem to be running"; \
	fi

stop-sc: ## Stop Spark Connect (SC)
	@echo "Stopping Spark Connect (SC)"
	@stop-connect-server.sh

## Checkers

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

check-uc: ## Check the content of Unity Catalog (UC)
	@echo "Checking for the dim_customer table in the table list on Unity Catalog (UC)"
	@$(eval TBL_NAME=$(shell $(UC_DIR)/bin/uc table list --catalog unityxt --schema bronze --output json | jq -r '.[]|select(.name|contains("dim_customer"))|.name'))
	@if [ "$(TBL_NAME)" == "dim_customer" ]; then \
		$(UC_DIR)/bin/uc table get --full_name unityxt.bronze.dim_customer ; \
	else \
		echo "Table dim_customer has not been created on UC in unityxt.bronze yet"; \
		echo "Hint: make init-uc-table"; \
	fi

check-uc-hard: ## Check the content of Unity Catalog (UC). Exit if not found
	@echo "Checking for the dim_customer table in the table list on Unity Catalog (UC)"
	@$(eval TBL_NAME=$(shell $(UC_DIR)/bin/uc table list --catalog unityxt --schema bronze --output json | jq -r '.[]|select(.name|contains("dim_customer"))|.name'))
	@if [ "$(TBL_NAME)" == "dim_customer" ]; then \
		$(UC_DIR)/bin/uc table get --full_name unityxt.bronze.dim_customer ; \
	else \
		echo "Table dim_customer has not been created on UC in unityxt.bronze yet"; \
		echo "Hint: make init-uc-table"; \
		exit 1; \
	fi

check-database-sc: init-log-dir ## Check the table on Spark Connect (SC)
	@echo "Check the logs/check_database_sc.log log file for details"
	@pyspark --remote $(SC_URL) \
		--packages "io.delta:$(DL_SC_CLT_JAR),$(PB_DOM):$(PB_JAR)" \
		< src/001_scd2_w_delta/sc-select-dim-customer-limit10.py \
		> logs/check_database_sc.log 2>&1
	@grep -v "^I00" logs/check_database_sc.log

check-database-uc: init-log-dir ## Check the table on Unity Catalog (UC)
	@echo "Check the logs/check_database_uc.log log file for details"
	@pyspark --remote $(SC_URL) \
		--packages "io.delta:$(DL_SC_CLT_JAR),$(PB_DOM):$(PB_JAR)" \
		< src/001_scd2_w_delta/uc-select-dim-customer-limit10.py \
		> logs/check_database_uc.log 2>&1
	@grep -v "^I00" logs/check_database_uc.log

check-database-sc-and-uc: init-log-dir ## Check the table on Spark Connect (SC), itself connected to UC
	@echo "Check the logs/check_database_sc_and_uc.log log file for details"
	@pyspark --remote $(SC_URL) \
		--packages "io.delta:$(DL_SC_CLT_JAR),$(PB_DOM):$(PB_JAR)" \
		< src/001_scd2_w_delta/sc-and-uc-select-dim-customer-limit10.py \
		> logs/check_database_sc_and_uc.log 2>&1
	@grep -v "^I00" logs/check_database_sc_and_uc.log

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
		--packages io.delta:delta-spark_$(SCALA_VERSION):$(DL_VERSION) \
	  	--conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
	  	--conf "spark.sql.catalog.spark_catalog=$(DL_SQL_DOM).DeltaCatalog" \
	  < sql/select-dim-customer-limit10.sql

browse-database-purepython: ## Check the Delta tables
	@$(MAKE) check-database
	spark-submit \
		--packages io.delta:delta-spark_$(SCALA_VERSION):$(DL_VERSION) \
	  	--conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
	  	--conf "spark.sql.catalog.spark_catalog=$(DL_SQL_DOM).DeltaCatalog" \
	  src/001_scd2_w_delta/select-dim-customer-limit10.py

browse-uc: ## Browse the content of Unity Catalog (UC)
	@$(UC_DIR)/bin/uc table read --full_name unityxt.bronze.dim_customer

#
ingest-datasets-simple: ## Ingest the customer-related datasets (initial and incremental) - Simple version
	@$(MAKE) check-database
	@echo "Merging datasets into the table. Check logs/merge_customer_001_simple.log"
	@mkdir -p logs
	time pyspark \
		--packages io.delta:delta-spark_$(SCALA_VERSION):$(DL_VERSION) \
	  	--conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
	  	--conf "spark.sql.catalog.spark_catalog=$(DL_SQL_DOM).DeltaCatalog" \
		< src/001_scd2_w_delta/jobs/merge_customer_001_simple.py \
		> logs/merge_customer_001_simple.log 2>&1
	@$(MAKE) check-database

ingest-datasets-uc-only: ## Ingest the customer-related datasets (initial and incremental) - Version for UC only
	@$(MAKE) check-uc-hard
	@echo "Merging datasets into the table. Check logs/merge_customer_002_uc_only.log"
	@mkdir -p logs
	time pyspark \
		--packages "io.delta:$(DL_JAR),$(UC_DOM):$(UC_JAR)" \
	  	--conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
        --conf "spark.sql.catalog.spark_catalog=$(DL_SQL_DOM).DeltaCatalog" \
        --conf "spark.sql.catalog.unityxt=$(UC_DOM).spark.UCSingleCatalog" \
        --conf "spark.sql.catalog.unityxt.uri=http://localhost:8080" \
        --conf "spark.sql.catalog.unityxt.token=" \
        --conf "spark.sql.defaultCatalog=unityxt" \
		< src/001_scd2_w_delta/jobs/merge_customer_002_uc_only.py \
		> logs/merge_customer_002_uc_only.log 2>&1
	@$(MAKE) check-uc
	@echo "Hint for next step: make browse-uc"

ingest-datasets-sc-only: init-log-dir ## Ingest the customer-related datasets (initial and incremental) - Version for SC only
	@echo "Merging datasets into the table on SC. Check logs/merge_customer_003_sc_only.log"
	time pyspark --remote $(SC_URL) \
		--packages "io.delta:$(DL_SC_CLT_JAR),$(PB_DOM):$(PB_JAR)" \
		< src/001_scd2_w_delta/jobs/merge_customer_003_sc_only.py \
		> logs/merge_customer_003_sc_only.log 2>&1

ingest-datasets-sc-and-uc: ## Ingest the customer-related datasets (initial and incremental) - Version for SC and UC
	@$(MAKE) check-uc-hard
	@echo "Check logs/merge_customer_004_sc_and_uc.log"
	@mkdir -p logs
	time pyspark --remote $(SC_URL) \
		--packages "io.delta:$(DL_SC_CLT_JAR),$(PB_DOM):$(PB_JAR)" \
		< src/001_scd2_w_delta/jobs/merge_customer_004_sc_and_uc.py \
		> logs/merge_customer_004_sc_and_uc.log 2>&1
	@$(MAKE) check-uc
	@echo "Hint for next step: make browse-uc"

