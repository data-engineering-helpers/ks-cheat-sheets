# Cheat Sheet - Google Agent Platform and tools

## Table of Content (ToC)

* [Cheat Sheet \- Google Agent Platform and tools](#cheat-sheet---google-agent-platform-and-tools)
  * [Table of Content (ToC)](#table-of-content-toc)
  * [Overview](#overview)
  * [References](#references)
    * [Data Engineering and AI helpers](#data-engineering-and-ai-helpers)
    * [References \- Google Agentic platform and tools](#references---google-agentic-platform-and-tools)
  * [Setup](#setup)
    * [Google Agents CLI](#google-agents-cli)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

## Overview

[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/ai/databricks-ai-dev-kit/README.md)
explains how to install and to use
[GitHub - Databricks Solutions - AI Dev Kit](https://github.com/databricks-solutions/ai-dev-kit),
_e.g._, on a laptop or on a virtual machine (VM).

## References

### Data Engineering and AI helpers

* [AI Helpers - Knowledge Sharing - Cheat Sheets](https://github.com/ai-helpers/ks-cheat-sheets/)
* [AI Helpers - Knowledge Sharing - Curated AI agent skills](https://github.com/ai-helpers/ai-skills-curated/)
* [Data Engineering Helpers - Knowledge Sharing - AI skills and rules](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/ai/rules-skills/)
* [Data Engineering Helpers - Knowledge Sharing - JavaScript (JS) world](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/js-world/)
* [Data Engineering Helpers - Knowledge Sharing - Python](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/python/)

### References - Google Agentic platform and tools

* [GCP docs - Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [GCP docs - Gemini Enterprise Agent Platform - Create an agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/create-an-agent)
* [GitHub - Google Agents CLI](https://github.com/google/agents-cli)
  * [GitHub pages - Google Agents CLI](https://google.github.io/agents-cli/)
  * [GitHub pages - Google Agents CLI - Getting started](https://google.github.io/agents-cli/guide/getting-started/)

## Setup

### Google Agents CLI

* See
  [Data Engineering Helpers - Knowledge Sharing - Python](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/python/)
  for the installation of the Python-related tools, including `uv` and `uvx`

* Simply install both the Google Agents CLI and the agent skill through `uvx`:

```bash
uvx google-agents-cli setup
```

* Note the `google/agents-cli` skill alone may be also installed via
  the classical `npx skills` command:

```bash
npx skills add google/agents-cli -g
```
