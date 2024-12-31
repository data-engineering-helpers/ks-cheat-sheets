#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/examples/003-python-simple/Makefile
#

clean-cache: ## Clean the SQLMesh cache directory
	rm -rf .cache

clean-logs: ## Clean the SQLMesh logs
	rm -rf logs

clean-wh: ## Clean the SQLMesh warehouse (DuckDB)
	rm -f db.db

clean: clean-cache clean-logs clean-wh ## Clean potential previous states and logs

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
	sqlmesh fetchdf "use sqlmesh_example; show tables"

list-tables-dev: ## List the tables in dev
	sqlmesh fetchdf "use sqlmesh_example__dev; show tables"

check-data-prod: ## Check the data in prod
	sqlmesh fetchdf "select * from sqlmesh_example.full_model_python"

check-data-dev: ## Check the data in dev
	sqlmesh fetchdf "select * from sqlmesh_example__dev.full_model_python"

diff: ## Differences between dev and prod
	sqlmesh table_diff prod:dev sqlmesh_example.full_model_python

ui: ## Launch the UI
	sqlmesh ui --port 10000


