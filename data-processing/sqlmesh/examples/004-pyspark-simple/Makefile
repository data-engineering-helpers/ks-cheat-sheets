

clean: ## Clean potential previous states and logs
	rm -rf db.db db.db.wal logs .cache
	rm -rf derby.log metastore_db spark-warehouse

hint-change: ## Hint for the changes to be made
	@echo "Edit the full_model_python.py file and uncomment the country column"
	@echo "vi models/full_model_python.py"

plan-prod: ## Plan, backfill and apply changes
	sqlmesh plan

plan-dev: ## Plan, backfill and apply changes in dev
	sqlmesh plan dev --include-unmodified

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

