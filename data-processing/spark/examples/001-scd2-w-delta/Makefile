#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/001-scd2-w-delta/Makefile
#

PYTHON_VERSION := 3.12
SCALA_VERSION := 2.13
SPARK_VERSION := 4.1.1 # 3.5.2
DELTA_VERSION := 4.1.0 # 3.2.0
DELTA_JAR := $(strip delta-spark_$(SCALA_VERSION):$(DELTA_VERSION))
DELTA_SC_SVR_JAR := $(strip delta-connect-server_$(SCALA_VERSION):$(DELTA_VERSION))
DELTA_SC_CLT_JAR := $(strip delta-connect-client_$(SCALA_VERSION):$(DELTA_VERSION))
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
	@$(UC_DIR)/bin/uc table delete --full_name unityxt.bronze.dim_customer

clean-uc-schema: ## Clean the schema in Unity Catalog (UC)
	@$(UC_DIR)/bin/uc schema delete --full_name unityxt.bronze --force true

clean-uc-catalog: ## Clean the catalog in Unity Catalog (UC)
	@$(UC_DIR)/bin/uc catalog delete --name unityxt --force true

clean-uc-all: clean-uc-catalog ## Clean all about the unityxt catalog

# Initializers
init-uv-python: ## Install Python $(PYTHON_VERSION) if necessary
	uv python install $(PYTHON_VERSION)

init-pyspark: ## Install PySpark and Delta Lake in the current Python environment (not the uv virtual one)
	python -mpip install --force-reinstall \
		pyspark==$(SPARK_VERSION) delta-spark==$(DELTA_VERSION) \
		pyspark-client==$(SPARK_VERSION)

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

init-database-sc: ## Initialize the Delta tables on SC
	pyspark --remote $(SC_URL) \
		--packages "io.delta:$(DELTA_SC_CLT_JAR),$(PB_DOM):$(PB_JAR)" \
		< src/001_scd2_w_delta/sc-ddl.py
	@$(MAKE) check-database-sc

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
		--packages "io.delta:$(DELTA_SC_SVR_JAR),$(PB_DOM):$(PB_JAR)" \
		--conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
		--conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog" \
		--conf "spark.connect.extensions.relation.classes=org.apache.spark.sql.connect.delta.DeltaRelationPlugin" \
		--conf "spark.connect.extensions.command.classes=org.apache.spark.sql.connect.delta.DeltaCommandPlugin"
	@echo "In order to stop the Spark Connect (SC) server: make stop-sc"

start-sc-and-uc: ## Start Spark Connect (SC), itself connected to UC
	@echo "Starting Spark Connect (SC), itself connected to Unity Catalog (UC)"
	@$(MAKE) check-uc
	@unset SPARK_REMOTE; start-connect-server.sh \
		--packages "$(SC_DOM):$(SC_JAR),io.delta:$(DELTA_JAR),$(UC_DOM):$(UC_JAR)" \
	  	--conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
        --conf "spark.sql.catalog.spark_catalog=$(UC_DOM).spark.UCSingleCatalog" \
        --conf "spark.sql.catalog.unityxt=$(UC_DOM).spark.UCSingleCatalog" \
        --conf "spark.sql.catalog.unityxt.uri=http://localhost:8080" \
        --conf "spark.sql.catalog.unityxt.token=" \
        --conf "spark.sql.defaultCatalog=unityxt"
	@echo "In order to stop the Spark Connect (SC) server: make stop-sc"

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
	@$(UC_DIR)/bin/uc table get --full_name unityxt.bronze.dim_customer

check-database-sc: ## Check the table on Spark Connect (SC)
	pyspark --remote $(SC_URL) \
		--packages "io.delta:$(DELTA_SC_CLT_JAR),$(PB_DOM):$(PB_JAR)" \
	  < src/001_scd2_w_delta/sc-select-dim-customer-limit10.py

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

browse-uc: ## Browse the content of Unity Catalog (UC)
	@$(UC_DIR)/bin/uc table read --full_name unityxt.bronze.dim_customer

#
ingest-datasets-simple: ## Ingest the customer-related datasets (initial and incremental) - Simple version
	@$(MAKE) check-database
	@echo "Check logs/merge_customer_001_simple.log"
	@mkdir -p logs
	time spark-submit \
		--packages io.delta:delta-spark_$(SCALA_VERSION):$(DELTA_VERSION) \
	  	--conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
	  	--conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog" \
	  src/001_scd2_w_delta/jobs/merge_customer_001_simple.py > logs/merge_customer_001_simple.log 2>&1
	@$(MAKE) check-database

ingest-datasets-uc-only: ## Ingest the customer-related datasets (initial and incremental) - Version for UC only
	@$(MAKE) check-uc
	@echo "Check logs/merge_customer_002_uc_only.log"
	@mkdir -p logs
	time spark-submit \
		--packages "io.delta:$(DELTA_JAR),$(UC_DOM):$(UC_JAR)" \
	  	--conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
        --conf "spark.sql.catalog.spark_catalog=$(UC_DOM).spark.UCSingleCatalog" \
        --conf "spark.sql.catalog.unityxt=$(UC_DOM).spark.UCSingleCatalog" \
        --conf "spark.sql.catalog.unityxt.uri=http://localhost:8080" \
        --conf "spark.sql.catalog.unityxt.token=" \
        --conf "spark.sql.defaultCatalog=unityxt" \
	  src/001_scd2_w_delta/jobs/merge_customer_002_uc_only.py > logs/merge_customer_002_uc_only.log 2>&1
	@$(MAKE) check-uc
	@echo "Hint for next step: make browse-uc"

ingest-datasets-sc-only: ## Ingest the customer-related datasets (initial and incremental) - Version for SC only
	@$(MAKE) check-database
	@echo "Check logs/merge_customer_003_sc_only.log"
	@mkdir -p logs
	time pyspark --remote $(SC_URL) \
		< src/001_scd2_w_delta/jobs/merge_customer_003_sc_only.py \
		> logs/merge_customer_003_sc_only.log 2>&1
	@$(MAKE) check-database-sc

ingest-datasets-uc-and-sc: ## Ingest the customer-related datasets (initial and incremental) - Version for SC and UC
	@$(MAKE) check-uc
	@echo "Check logs/merge_customer_004_sc_and_uc.log"
	@mkdir -p logs
	time spark-submit \
		--packages "io.delta:$(DELTA_JAR),$(UC_DOM):$(UC_JAR)" \
	  	--conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
        --conf "spark.sql.catalog.spark_catalog=$(UC_DOM).spark.UCSingleCatalog" \
        --conf "spark.sql.catalog.unityxt=$(UC_DOM).spark.UCSingleCatalog" \
        --conf "spark.sql.catalog.unityxt.uri=http://localhost:8080" \
        --conf "spark.sql.catalog.unityxt.token=" \
        --conf "spark.sql.defaultCatalog=unityxt" \
	  src/001_scd2_w_delta/jobs/merge_customer_004_sc_and_uc.py > logs/merge_customer_004_sc_and_uc.log 2>&1
	@$(MAKE) check-uc
	@echo "Hint for next step: make browse-uc"

