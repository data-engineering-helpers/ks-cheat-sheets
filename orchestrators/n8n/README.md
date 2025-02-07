Cheat Sheet - n8n
=================

# Table of Content (ToC)
* [Overview](#overview)
* [References](#references)
  * [Data Engineering helpers](#data-engineering-helpers)
  * [n8n](#n8n)
    * [Key Capabilities](#key-capabilities)
* [Getting started](#getting-started)
* [Installation](#installation)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/orchestrators/n8n/README.md)
explains how to install and to use n8n on premises, _e.g._, on a laptop
or on a virtual machine (VM).

# References

## Data Engineering helpers
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box/blob/main/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Airflow](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/orchestrators/airflow/README.md)

## n8n
* Home page: https://n8n.io
* GitHub page: https://github.com/n8n-io/n8n
* A LinkedIn post showcasing how to use n8n on DataBricks:
  https://www.linkedin.com/posts/hellomikelo_databricks-apps-started-out-as-a-framework-activity-7293304974766194689-wPhg/
* Motto: Secure Workflow Automation for Technical Teams
> n8n is a workflow automation platform that gives technical teams
> the flexibility of code with the speed of no-code. With 400+ integrations,
> native AI capabilities, and a fair-code license, n8n lets you build powerful
> automations while maintaining full control over your data and deployments.

### Key Capabilities
* Code When You Need It: Write JavaScript/Python, add npm packages,
  or use the visual interface
* AI-Native Platform: Build AI agent workflows based on LangChain
  with your own data and models
* Full Control: Self-host with our fair-code license or use our
  [cloud offering](https://app.n8n.cloud/login)
* Enterprise-Ready: Advanced permissions, SSO, and air-gapped deployments
* Active Community: 400+ integrations and 900+ ready-to-use
  [templates](https://n8n.io/workflows)


# Getting started
* Try n8n instantly with [npx](https://docs.n8n.io/hosting/installation/npm/)
  (requires [Node.js](https://nodejs.org/en/)):
```bash
npx n8n
```

* Or deploy with [Docker](https://docs.n8n.io/hosting/installation/docker/):
```bash
docker volume create n8n_data
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

# Installation

