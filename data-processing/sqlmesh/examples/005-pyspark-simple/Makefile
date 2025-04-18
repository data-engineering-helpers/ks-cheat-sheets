#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/examples/005-pyspark-simple/Makefile
#

clean-cache: ## Clean the SQLMesh cache directory
	rm -rf .cache

clean-logs: ## Clean the SQLMesh logs
	rm -rf logs

clean-state: ## Clean the SQLMesh state (DuckDB)
	rm -f db.db db.db.wal

clean-spark: ## Clean the warehouse (Spark metastore and warehouse)
	rm -rf derby.log metastore_db spark-warehouse

clean: clean-cache clean-logs clean-state clean-spark ## Clean potential previous states and logs

hint-change: ## Hint for the changes to be made
	@echo "Edit the full_model_python.py file and uncomment the country column"
	@echo "vi models/full_model_python.py"

plan-prod: ## Plan, backfill and apply changes
	sqlmesh plan

plan-dev: ## Plan, backfill and apply changes in dev
	sqlmesh plan dev --include-unmodified

audit: ## Audit
	sqlmesh audit

test: ## Tests
	sqlmesh test

list-tables-prod: ## List the tables in prod
	sqlmesh fetchdf "show tables in spark_catalog.sqlmesh_example"

list-tables-dev: ## List the tables in dev
	sqlmesh fetchdf "show tables in spark_catalog.sqlmesh_example__dev"

check-data-prod: ## Check the data in prod
	sqlmesh fetchdf "select * from spark_catalog.sqlmesh_example.full_model_python"

check-data-dev: ## Check the data in dev
	sqlmesh fetchdf "select * from sqlmesh_example__dev.full_model_python"

diff: ## Differences between dev and prod
	sqlmesh table_diff prod:dev sqlmesh_example.full_model_python

ui: ## Launch the UI
	sqlmesh ui --port 10000


