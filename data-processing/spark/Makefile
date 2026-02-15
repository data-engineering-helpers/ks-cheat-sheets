UV ?= uv

.PHONY: deps run test build clean

init: ## uv - Creates/updates the uv.lock file
	@uv lock
	@uv export --format requirements.txt > requirements.txt

update: ## uv - Upgrades the uv.lock file
	@uv sync
	@uv export --format requirements.txt > requirements.txt

build: ## Build the software artifact (wheel)
	@uv build
