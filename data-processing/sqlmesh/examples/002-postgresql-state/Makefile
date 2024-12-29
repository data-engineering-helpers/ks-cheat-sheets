#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/examples/002-postgresql-state/Makefile
#

clean-cache: ## Clean the SQLMesh cache directory
	rm -rf .cache

clean-logs: ## Clean the SQLMesh logs
	rm -rf logs

clean-wh: ## Clean the SQLMesh warehouse (DuckDB)
	rm -f db.db

clean-pg: ## Clean the SQLMesh state in the local PostgreSQL database
	@../../tools/clean-pg-state.sh

clean: clean-cache clean-logs clean-wh clean-pg ## Clean potential previous states and logs

init: ## Initialize the project with PostgreSQL to store the state
	cp -f config.yaml.sample config.yaml
	sed -i.bak -e 's/<sqlmesh-pass>/sqlmesh/' config.yaml && rm -f config.yaml.bak

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
	sqlmesh fetchdf "use sqlmesh_example; show tables"

list-tables-dev: ## List the tables in dev
	sqlmesh fetchdf "use sqlmesh_example__dev; show tables"

check-data-prod: ## Check the data in prod
	sqlmesh fetchdf "select * from sqlmesh_example.incremental_model"

check-data-dev: ## Check the data in dev
	sqlmesh fetchdf "select * from sqlmesh_example__dev.incremental_model"

diff: ## Differences between dev and prod
	sqlmesh table_diff prod:dev sqlmesh_example.incremental_model

