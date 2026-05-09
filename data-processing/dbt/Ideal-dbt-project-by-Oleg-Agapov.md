# Knowledge Sharing (KS) - Cheat sheets - dbt - The ideal dbt project

## Overview

This cheat sheet is part of the
[Data Engineering Helpers - dbt cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/tree/main/data-processing/dbt).

## References

* [LinkedIn post - The ideal dbt project](https://www.linkedin.com/feed/update/urn:li:activity:7458485893666902017/)
  * Author: [Oleg Agapov](https://www.linkedin.com/in/oleg-agapov/)
  * Date: May 2026

## Ideal dbt project structure

The ideal dbt project structure, according to Oleg Agapov:
* `/analyses` — ad-hoc SQL queries that compile but don't materialize. Great for one-off investigations you want version-controlled.

* `/macros` — reusable Jinja functions. Custom tests, generate statements, repeated logic.

* `/models` — the core of your project, split into three layers:
  * `/staging` — mirrors your sources. One subfolder per connection (postgres, stripe). Light renaming, casting, deduplication only.
  * `/intermediate` — business logic by domain. Joins, filters, calculations. Organized by business area, not by source.
  * `/marts` — final models your BI tool queries. Each model has a .sql and .yml file side by side.

* `/seeds` — small static CSV files loaded into the warehouse. Country codes, category mappings, manual overrides.

* `/snapshots` — slowly changing dimension tracking. Captures how source data changes over time.

* `/tests` — custom data tests that don't belong to a specific model. Cross-model validation, business rule assertions.

* `.pre-commit-config.yaml` — SQLFluff + yamllint to catch issues before they hit your PR.

* `dbt_project.yml` — project-level config. Name, version, materialization defaults, folder paths.

* `packages.yml` — external dbt packages (dbt-utils, dbt-expectations, audit-helper).

* `profiles.yml` — connection details for your warehouse. Dev, staging, prod targets.
