# Cheat Sheet - AI - Rules and Skills

## Table of Content (ToC)

* [Cheat Sheet \- AI \- Rules and Skills](#cheat-sheet---ai---rules-and-skills)
  * [Table of Content (ToC)](#table-of-content-toc)
  * [Overview](#overview)
  * [References](#references)
    * [AI helpers](#ai-helpers)
    * [Data Engineering helpers](#data-engineering-helpers)
    * [AI rules and skills](#ai-rules-and-skills)
  * [Getting started](#getting-started)
    * [List the skills already installed](#list-the-skills-already-installed)
    * [Install a skill locally](#install-a-skill-locally)
    * [Remove a skill](#remove-a-skill)
    * [Update skills](#update-skills)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

## Overview

[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/ai/rules-skills/README.md)
explains how to install and to use [AI skills](https://skills.sh), _e.g._,
on a laptop or on a virtual machine (VM).

## References

### AI helpers

* [AI Helpers - Knowledge Sharing - AI skills curated](https://github.com/ai-helpers/ai-skills-curated)

### Data Engineering helpers

* [Data Engineering Helpers - Knowledge Sharing - Declarative Data Pipelines](https://github.com/data-engineering-helpers/declarative-data-pipelines/)
* [Data Engineering Helpers - Knowledge Sharing - Databricks AI Dev Kit](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/ai/databricks-ai-dev-kit/)
* [Data Engineering Helpers - Knowledge Sharing - AI skills and rules](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/ai/rules-skills/)
* [Data Engineering Helpers - Knowledge Sharing - JavaScript (JS) world](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/js-world/)
* [Data Engineering Helpers - Knowledge Sharing - Python](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/python/)

### AI rules and skills

* [Vercel labs - Skills homepage](https://skills.sh)
* [GitHub - Vercel labs - Skills](https://github.com/vercel-labs/skills)

#### Rules and skills - Articles

##### Copilot agents Dojo
* [GitHub - Copilot Agents Dojo](https://github.com/andreaswasita/copilot-agents-dojo)
* Author: Andreas Wasita Pradipta
  ([Andreas Wasita Pradipta on LinkedIn](https://www.linkedin.com/in/andreaswasita/),
  [Andreas Wasita Pradipta on GitHub](https://github.com/andreaswasita))
* Date: March 2026
* [LinkedIn - Copilot Agents Dojo](https://www.linkedin.com/posts/andreaswasita_agenticai-githubcopilot-microsoft-activity-7438219647650283520-eKIT)

### AI Spec-Driven Development (SDD)

#### SDD - Articles

##### Stop chatting start specifying build

* Author: Fabrice Monnier
  ([Fabrice Monnier on LinkedIn](https://www.linkedin.com/in/fabrice-monnier-cloud-data-devops/),
  [Fabrice Monnier on Substack](https://substack.com/@fabricemonnier))
* Date: March 2026
* [Substack - Stop chatting start specifying build](https://open.substack.com/pub/fabricemonnier/p/stop-chatting-start-specifying-build)

## Getting started

### List the skills already installed

* List the skills brought by the current project:

```bash
npx skills list
```

* List the skills installed globally (in the user directory, that is,
  in the `$HOME/.agents/skills/` directory):

```bash
npx skills list -g
```

### Install a skill locally

* The available skill sets may be browsed online: all the skill sets are in the
  [`agents/skills/` directory](https://github.com/ai-helpers/ai-skills-curated/blob/main/agents/skills/)

* In order to install a skill set for generic agents (the `--global` parameter
  will have the skill set installed in the `$HOME/.agents/skills/` global user
  directory):

```bash
npx skills add ai-helpers/ai-skills-curated <sill-set> --global
```

* For instance, for the
  [`managing-python-projects-with-uv`](https://github.com/ai-helpers/ai-skills-curated/tree/main/agents/skills/managing-python-projects-with-uv/)
  skill set:

```bash
npx skills add ai-helpers/ai-skills-curated managing-python-projects-with-uv --global
```

### Remove a skill

* In order to remove an installed skill set, use `npx skills remove <skill>`.
  For instance, to remove the `managing-python-projects-with-uv` skill set:

```bash
npx skills remove managing-python-projects-with-uv -g
```

### Update skills

* Upgrade the skills (it fetches potential new releases of the installed skills
  and installs those latest versions):

```bash
npx skills update
```
