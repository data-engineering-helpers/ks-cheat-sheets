Cheat Sheet - dbt
=================

# Table of Content (ToC)
* [Overview](#overview)
* [References](#references)
  * [Data Engineering helpers](#data-engineering-helpers)
  * [ArkFlow](#arkflow)
* [Quickstart](#quickstart)
* [Installation](#installation)
  * [Rust](#rust)
  * [Build from the sources](#build-from-the-sources)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/arkflow/README.md)
explains how to install and to use [ArkFlow](https://ark-flow.github.io/arkflow/)
on premises, _e.g._, on a laptop or on a virtual machine (VM).

# References

## Data Engineering helpers
* [Data Engineering Helpers - Knowledge Sharing - SQLMesh](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/dbt/README.md)
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box/blob/main/README.md)
* [Material for the Data platform - Data life cycle](https://github.com/data-engineering-helpers/data-life-cycle/blob/main/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Minio](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-storage/minio/README.md)
* [Data Engineering Helpers - Knowledge Sharing - DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/README.md)

## ArkFlow
* GitHub repository: https://github.com/ark-flow/arkflow

# Quickstart
* Create a configuration file `config.yaml`:
```yaml
logging:
  level: info
streams:
  - input:
      type: "generate"
      context: '{ "timestamp": 1625000000000, "value": 10, "sensor": "temp_1" }'
      interval: 1s
      batch_size: 10

    pipeline:
      thread_num: 4
      processors:
        - type: "json_to_arrow"
        - type: "sql"
          query: "SELECT * FROM flow WHERE value >= 10"

    output:
      type: "stdout"
```

* Run ArkFlow:
```bash
./target/release/arkflow --config config.yaml
```

# Installation

## Rust
Rust tools need to be installed

* On MacOS:
```bash
brew install rust
```

## Build from the sources
* Clone the Git repository:
```bash
mkdir -p ~/dev/infra
git clone https://github.com/ark-flow/arkflow.git ~/dev/infra/arkflow
cd ~/dev/infra/arkflow
```

* Build project
```bash
cargo build --release
```

* Run tests:
```bash
cargo test
```

