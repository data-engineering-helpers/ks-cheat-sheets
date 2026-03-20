# Cheat Sheet - Databricks AI Dev Kit

## Table of Content (ToC)

* [Cheat Sheet \- Databricks AI Dev Kit](#cheat-sheet---databricks-ai-dev-kit)
  * [Table of Content (ToC)](#table-of-content-toc)
  * [Overview](#overview)
  * [References](#references)
    * [Data Engineering helpers](#data-engineering-helpers)
    * [Databricks declarative development](#databricks-declarative-development)
    * [Spec\-driven development (SDD)](#spec-driven-development-sdd)
    * [Lakehouse Plumber](#lakehouse-plumber)
    * [Metadata\-Driven Lakehouse Ingestion](#metadata-driven-lakehouse-ingestion)
    * [Articles about Databricks AI Dev Kit](#articles-about-databricks-ai-dev-kit)
      * [Hitchhikers guide to the Databricks AI Dev Kit](#hitchhikers-guide-to-the-databricks-ai-dev-kit)
  * [Getting started](#getting-started)
    * [Use with VS Code Copilot](#use-with-vs-code-copilot)
  * [Setup](#setup)
    * [Prerequisites](#prerequisites)
    * [Setup \- References](#setup---references)
    * [Authentication for the Databricks CLI](#authentication-for-the-databricks-cli)
    * [MCP mode \- Install globally](#mcp-mode---install-globally)
    * [MCP mode \- Install in existing project](#mcp-mode---install-in-existing-project)
    * [Direct CLI mode installation](#direct-cli-mode-installation)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

## Overview

[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/ai/databricks-ai-dev-kit/README.md)
explains how to install and to use
[GitHub - Databricks Solutions - AI Dev Kit](https://github.com/databricks-solutions/ai-dev-kit),
_e.g._, on a laptop or on a virtual machine (VM).

## References

### Data Engineering helpers

* [Data Engineering Helpers - Knowledge Sharing - Declarative Data Pipelines](https://github.com/data-engineering-helpers/declarative-data-pipelines/)
* [Data Engineering Helpers - Knowledge Sharing - AI skills and rules](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/ai/rules-skills/)
* [Data Engineering Helpers - Knowledge Sharing - JavaScript (JS) world](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/js-world/)
* [Data Engineering Helpers - Knowledge Sharing - python](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/python/)

### Databricks declarative development

* [GitHub - Databricks Solutions - AI Dev Kit](https://github.com/databricks-solutions/ai-dev-kit)
* [Spark Declarative Pipelines (SDP)](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [Databricks Lakeflow Declarative Pipelines (LDP)](https://docs.databricks.com/aws/en/ldp/)
* [Databricks Asset Bundles (DAB)](https://docs.databricks.com/aws/en/dev-tools/bundles/)

### Spec-driven development (SDD)

* [GitHub - Spec-kit](https://github.com/github/spec-kit)
  * [GitHub - Spec-kit - Spec-driven development (SDD)](https://github.com/github/spec-kit/blob/main/spec-driven.md)
* [Martin Fowler's blog](https://martinfowler.com/)
  [Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html),
  by [Birgitta Böckeler](https://birgitta.info/), Oct. 2025

### Lakehouse Plumber

* Overview:

> The Metadata Driven framework for Databricks Lakeflow Declarative Pipelines
> (LDP) (formerly Delta Live Tables (DLT)). Metadata framework that generates
> production ready Pyspark code for Lakeflow Declarative Pipelines

* Authors/main contributors:
  * Mehdi Modarressi
  ([Mehdi Modarressi on LinkedIn](https://www.linkedin.com/in/modarressi/),
  [Mehdi Modarressi on GitHub](https://github.com/Mmodarre))
  * David O'Keefe
  ([David O'Keefe on LinkedIn](https://www.linkedin.com/in/dgokeeffe/),
  [David O'Keefe on GitHub](https://github.com/dgokeeffe),
  [David O'Keefe on Medium](https://medium.com/@davidok7))
* [GitHub - Lakehouse Plumber](https://github.com/Mmodarre/Lakehouse_Plumber)

### Metadata-Driven Lakehouse Ingestion

* Author/main contributor: Yasar Kocyigit
* LinkedIn posts:
  * [Linkedin post - Main features of Metadata-Driven Lakehouse Ingestion](https://www.linkedin.com/posts/yasarkocyigit_databricks-aidevkit-dataengineering-share-7433025769511047168-RoD2/),
  Feb. 2026
  * [LinkedIn post - Introduction to Metadata-Driven Lakehouse Ingestion](https://www.linkedin.com/posts/yasarkocyigit_databricks-lakehouse-dataengineering-activity-7432386473104080897-S-nA/),
  Feb. 2026
* [GitHub - Metadata-Driven Lakehouse Ingestion](https://github.com/yasarkocyigit/daq-databricks-dab)
* Overview:

> In my initial experiments to democratize onboarding in metadata-driven
> development (MDD) architectures, the process has been much easier with
> Databricks AI Dev Kit.
>
> I first built the infra foundation with DAB + MDD, then integrated AI Dev Kit
> and tested it at Databricks app level.
>
> Technically, what we added:
>
> * Chat-based onboarding entrypoint
> * AI Agent runtime for intent-driven orchestration
> * MCP layer for Databricks tool execution
> * Lakebase for conversation and project-state persistence
> * Git-based metadata flow (YAML + DAB)
> * CI/CD gates for validation and controlled deployment
>
> Impact so far:
>
> * Faster source/table onboarding
> * More consistent metadata-driven pipelines
> * Clear path from request -> config -> validation -> deployment
>
> Also, development can be managed via CLI + Claude
> I tested Codex and Gemini Pro 3.1 as well; for this workflow Claude 4.6
> performed best in my experience.

### Articles about Databricks AI Dev Kit

#### Hitchhikers guide to the Databricks AI Dev Kit
* Title: Hitchhikers guide to the Databricks AI Dev Kit
* Author: Jaco van Gelder
  ([Jaco van Gelder on LinkedIn](https://www.linkedin.com/in/jwvangelder/)),
  Co-Founder of [Dtyped](https://www.linkedin.com/company/dtyped)
* [Dtyped blog - Hitchhikers guide to the Databricks AI Dev Kit](https://dtyped.com/hitchhikers-guide-to-the-databricks-ai-dev-kit/)
<img width="182" height="202" alt="image" src="https://github.com/user-attachments/assets/27992092-55a4-4f9f-9e2c-f35035c2f369" />

## Getting started

### Use with VS Code Copilot

* In the [VS Code Copilot chat](https://github.com/features/copilot/ai-code-editor)
  ([Open Copilot in VS Code](vscode://github.copilot-chat)), open the tools
  (bottom-right tool icon) window and enable Databricks if not already done so
* Start with simple Databricks commands like `list_warehouses`.
  And, of course, Copilot also understand plain English like
  `list SQL Warehouses`, and it will then proposes subsequent actions
* Display details about a table: `table <database>.<schema>.<table>`

## Setup

### Prerequisites

* [uv](https://github.com/astral-sh/uv) - Python package manager
  * See also
  [Data Engineering Helpers - Knowledge Sharing - python](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/python/)
  which gives details on how to install and to use uv
* [Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli/) -
  Command line interface for Databricks
  * See also
  [Databricks doc - Authentication for the Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli/authentication)
* AI coding environment; either of:
  * [Copilot in VS Code](https://github.com/features/copilot/ai-code-editor)
  * [Claude Code](https://claude.ai/code)
  * [Cursor](https://cursor.com/)
* For the direct CLI mode (rather than through MCP):
  * [Vercel labs - Skills homepage](https://skills.sh)
  * [GitHub - Vercel labs - Skills](https://github.com/vercel-labs/skills)
  * See also
  [Data Engineering Helpers - Knowledge Sharing - AI skills and rules](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/ai/rules-skills/)

### Setup - References

* [GitHub - Databricks AI Dev Kit - Install in existing project](https://github.com/databricks-solutions/ai-dev-kit?tab=readme-ov-file#install-in-existing-project)
* [GitHub - Data Engineering Helpers - KS - Databricks AI Dev Kit - VSCode Databricks MCP JSON config file (`mcp.json`)](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/ai/databricks-ai-dev-kit/vscode/mcp.json)

### Authentication for the Databricks CLI

* References:
  * [Databricks doc - Authorize access to Databricks resources](https://docs.databricks.com/aws/en/dev-tools/auth/)
    * [Databricks doc - Authenticate access to Databricks using OAuth token federation](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-federation)
  * [Databricks doc - Authentication for the Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli/authentication)

* The recommended authentication way from the command-line (CLI) for interactive
  sessions is
  [Authenticate access to Databricks using OAuth token federation](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-federation)

> Databricks OAuth token federation enables you to securely access Databricks
> APIs using tokens from your trusted identity providers (IdPs). OAuth token
> federation eliminates the need to manage and rotate Databricks secrets such as
> personal access tokens and Databricks OAuth client secrets.
>
> Using Databricks OAuth token federation, users and service principals exchange
> JWT (JSON Web Tokens) tokens from your identity provider for Databricks OAuth
> tokens, which can then be used to access Databricks APIs.

* Basically, once the Databricks CLI has been installed, the Databricks CLI
  configuration file (`~/.databrickscfg`) should look like the following:

```cfg
[DEFAULT]
host      = https://<your-workspace>.cloud.databricks.com
auth_type = databricks-cli
jobs-api-version = 2.1

[dbx-fav]
host      = https://<your-workspace>.cloud.databricks.com
auth_type = databricks-cli
```

* For reference, the deprecated way of authentication was through the use of
  so-called Personal Access Token (PAT). It is not documented here in order
  to avoid confusion

* In order to authenticate for a given profile, just use the
  `databricks auth login` command.
  * This will normally open the web browser on the login page of Databricks,
  usually offering to use the SSO when there is one

* To login with the default workspace/environment/profile:

```bash
databricks auth login
```

* To login with a given workspace/environment/profile, just specify it with the
  `--profile` parameter, like for any other Databricks CLI command:

```bash
databricks auth login --profile dbx-fav
```

### MCP mode - Install globally

* The MCP installation mode seems to be the default (documented) one
  * However, as discussed in a mid-Feb. 2026 Medium article, namely
  [Why CLIs Beat MCP for AI Agents](https://medium.com/@rentierdigital/why-clis-beat-mcp-for-ai-agents-and-how-to-build-your-own-cli-army-6c27b0aec969),
  the MCP installation bloats the context window
  * And, in the case of DataBricks AI Dev Kit, all the Skills nevertheless
  already use the DataBricks CLI
  * Most probably, it was documented that way (MCP first) to allow for easy
  discovery, for instance through the VSCode tooling window
  * Now that VSCode has a Copilot Skill menu, exposing DataBricks Skills
  through MCP is becoming less important
* Moreover, for some reason, as of March 2026, the global installation does not
  seem to install anything that VSCode Copilot recognizes
  * If you exclusively use Copilot, it may be easier to also install AI Dev Kit
  locally, as seen in the subsection below
  * Nevertheless, the global installation allows to have the DataBricks MCP server
  installed at the user space level, that is, in the `~/.ai-dev-kit` directory
  * Any further local installation (in project workspaces/directories) will then
  use/reference that global installation, and avoir duplication of the
  AI Dev Kit installation
* Excute the following
  [install Shell script](https://github.com/databricks-solutions/ai-dev-kit/blob/main/install.sh)
  with the `--global` and `--force` options (it will force the reinstallation if
  needed):

```bash
ADK_URL="https://raw.githubusercontent.com/databricks-solutions/ai-dev-kit/main/install.sh"
bash <(curl -sL $ADK_URL) --global --force
```

### MCP mode - Install in existing project

* By default this will install at a project level rather than a user level.
  This is often a good fit, but requires you to run your client from the exact
  directory that was used for the install.
  * **Note**: Project configuration files can be re-used in other projects.
  You find these configs under `.vscode`, `.claude` or `.cursor`
* Excute the following
  [install Shell script](https://github.com/databricks-solutions/ai-dev-kit/blob/main/install.sh):

```bash
ADK_URL="https://raw.githubusercontent.com/databricks-solutions/ai-dev-kit/main/install.sh"
bash <(curl -sL $ADK_URL)
```

* As a matter of fact, once AI Dev Kit has already been installed globally,
  the local installation will only reference/point to the global installation,
  and consists mainly of a `mcp.json` configuration file (see just below),
  pointing to/referencing the global AI Dev Kit installation

* If, for some reason, the Databricks MCP configuration file has not been
  installed (typically, in `.vscode/mcp.json`), you can copy
  [the sample `mcp.json` file from this repository](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/ai/databricks-ai-dev-kit/vscode/mcp.json)
  into the local `.vscode/` directory and adapt it for your environment,
  that is, mainly the home directory and the Databricks
  profile/workspace/environment, which is to be found in the Databricks CLI
  configuration file (`~/.databrickscfg`)

* From [VS Code, open the chat](vscode://github.copilot-chat), and click on
  the tool icon at the bottom-right of the chat window:
<img width="1674" height="327" alt="image"
     src="https://github.com/user-attachments/assets/43aaa285-a134-4ef7-a71d-0c6dcf010245"
/>
<img width="153" height="33" alt="image"
     src="https://github.com/user-attachments/assets/64e55688-9454-4117-b8af-dda103793c2f"
/>

* In the tool pop-up window of that chat, click on `databricks` to enable it,
  and then click on the OK button:
<img width="597" height="136" alt="image"
     src="https://github.com/user-attachments/assets/4ba57905-f394-4c84-b08d-16b505680a5f"
/>

### Direct CLI mode installation

* [Browse the DataBricks AI Dev Kit Skills](https://skills.sh/?q=databricks-solutions/ai-dev-kit)

* Install the DataBricks DataBricks development guide:

```bash
npx skills add https://github.com/databricks-solutions/ai-dev-kit \
    --skill databricks-python-sdk -g
```

* Install the DataBricks Python development rules:

```bash
npx skills add https://github.com/databricks-solutions/ai-dev-kit 
    --skill python-dev -g
```

* As of March 2026, for some reason, the remaining of the Skills cannot be
  installed through the `npx skills` CLI interface. The details to install
  them are left below for reference only (but Skills.sh report that those
  Skills cannot be found)

* Install the DataBricks Skill testing framework:

```bash
npx skills add https://github.com/databricks-solutions/ai-dev-kit \
    --skill skill-test -g
```

* Install the DataBricks Skill testing framework:

```bash
npx skills add https://github.com/databricks-solutions/ai-dev-kit \
    --skill databricks-unity-catalog -g
```
