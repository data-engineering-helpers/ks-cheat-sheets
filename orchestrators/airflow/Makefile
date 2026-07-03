

clean: ## Delete temporary files
	@rm -rf .venv
	@rm -rf *.egg-info
	@rm -f requirements.txt

init: ## Initialize dependencies lock and exported requirements.
	@uv lock
	@uv export --format requirements.txt --only-group runtime --no-emit-project --no-hashes --no-header > requirements.txt

update: ## Update dependencies lock and exported requirements.
	@uv sync --upgrade --all-extras --all-groups
	@uv export --format requirements.txt --only-group runtime --no-emit-project --no-hashes --no-header > requirements.txt

airflow-info: ## Display information (eg, version) of Airflow components
	@uv run airflow info

airflow-start-standalone: ## Start Airflow in standalone mode
	@uv run airflow standalone
