#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/000-data-setup/Makefile
#

PYTHON_VERSION := 3.12
SCALA_VERSION := 2.13
SPARK_VERSION := 4.1.1
DELTA_VERSION := 4.2.0
DATA_DIR := ../data
DATA_CUST_DIR := $(DATA_DIR)/dim_customer

UV ?= uv

# Cleaners
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

cleaners: clean-logs clean-python clean-package clean-install clean-datasets ## Clean everything

# Initializers
init-uv-python: ## Install Python $(PYTHON_VERSION) if necessary
	uv python install $(PYTHON_VERSION)

init-pyspark: ## Install PySpark and Delta Lake in the current Python environment (not the uv virtual one)
	python -mpip install --force-reinstall \
		pyspark==$(SPARK_VERSION) delta-spark==$(DELTA_VERSION)

init-datasets: ## Generate sample datasets
	@uv run python src/000_data_setup/generate_customer_datasets.py
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
