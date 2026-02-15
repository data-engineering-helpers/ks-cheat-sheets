#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/examples/004-sdp-quick-start/Makefile
#

PYTHON_VERSION := 3.13
SCALA_VERSION := 2.13
SPARK_VERSION := 4.1.1
DELTA_VERSION := 4.0.1

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

cleaners: clean-db clean-logs clean-python clean-package clean-install ## Clean everything

# Initializers
init-uv-python: ## Install Python $(PYTHON_VERSION) if necessary
	uv python install $(PYTHON_VERSION)

init-pyspark: ## Install PySpark and Delta Lake in the current Python environment (not the uv virtual one)
	python -mpip install pyspark==$(SPARK_VERSION) delta-spark==$(DELTA_VERSION)

#
init: ## Setup Python virtual environment
	@uv lock
	@uv export --format requirements.txt > requirements.txt

update: ## Update the dependencies
	@uv sync
	@uv export --format requirements.txt > requirements.txt

build: ## Build the software artifact (wheel)
	@uv build

