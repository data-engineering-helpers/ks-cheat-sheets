

clean: ## Clean potential previous states and logs
	rm -rf db.db data/local.duckdb logs .cache

hint-change: ## Hint for the changes to be made
	@echo "Edit the incremental_model.sql file and uncomment the country column"
	@echo "vi models/incremental_model.sql"

plan-prod: ## Plan, backfill and apply changes
	sqlmesh plan

plan-dev: ## Plan, backfill and apply changes in dev
	sqlmesh plan dev --include-unmodified

list-tables-prod: ## List the tables in prod
	sqlmesh fetchdf "use ibis; show tables"

list-tables-dev: ## List the tables in dev
	sqlmesh fetchdf "use ibis__dev; show tables"

check-data-prod: ## Check the data in prod
	sqlmesh fetchdf "select * from ibis.incremental_model"

check-data-dev: ## Check the data in dev
	sqlmesh fetchdf "select * from ibis__dev.incremental_model"

diff: ## Differences between dev and prod
	sqlmesh table_diff prod:dev ibis.incremental_model

