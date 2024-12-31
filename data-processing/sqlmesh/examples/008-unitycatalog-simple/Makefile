#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/examples/005-pyspark-simple/Makefile
#

# DBS_ environment variables
include .env

clean-cache: ## Clean the SQLMesh cache directory
	rm -rf .cache

clean-logs: ## Clean the SQLMesh logs
	rm -rf logs

clean-state: ## Clean the SQLMesh state (DuckDB)
	rm -f db.db db.db.wal

clean-spark: ## Clean the warehouse (Spark metastore and warehouse)
	rm -rf derby.log metastore_db spark-warehouse

clean: clean-cache clean-logs clean-state clean-spark ## Clean potential previous states and logs

init-python: ## Install Python libraries
	python -mpip install -U "sqlmesh[web,databricks,spark]"

init-files: ## Create files with instantiated env vars
	@../../tools/init-dbs-w-env.sh

init: init-python init-files ## Initialization

info: ## Info about the project
	sqlmesh info

hint-change: ## Hint for the changes to be made
	@echo "Edit the incremental_model.sql file and uncomment the z column"
	@echo "vi models/incremental_model.sql"

plan-prod: ## Plan, backfill and apply changes
	sqlmesh plan

plan-dev: ## Plan, backfill and apply changes in dev
	sqlmesh plan dev --include-unmodified

audit: ## Audit
	sqlmesh audit

test: ## Tests
	sqlmesh test

list-tables-prod: ## List the tables in prod
	sqlmesh fetchdf "show tables in $(DBS_SCH) like '*seed_model*|*incremental_model*|*full_model*'"

list-tables-dev: ## List the tables in dev
	sqlmesh fetchdf "show tables in $(DBS_SCH) like '*seed_model__dev*|*incremental_model__dev*|*full_model__dev*'"

check-data-prod: ## Check the data in prod
	sqlmesh fetchdf "select * from $(DBS_SCH).incremental_model"

check-data-dev: ## Check the data in dev
	sqlmesh fetchdf "select * from $(DBS_SCH).incremental_model__dev"

diff: ## Differences between dev and prod
	sqlmesh table_diff --temp-schema $(DBS_SCH) prod:dev $(DBS_SCH).incremental_model

