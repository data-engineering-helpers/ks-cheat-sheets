# Cheat Sheet - Proxmox Virtual Environment (VE)

## Table of Content (ToC)

* [Cheat Sheet \- Proxmox Virtual Environment (VE)](#cheat-sheet---proxmox-virtual-environment-ve)
  * [Table of Content (ToC)](#table-of-content-toc)
  * [Overview](#overview)
  * [References](#references)
    * [Knowledge Sharing](#knowledge-sharing)
    * [Proxmox](#proxmox)
    * [AI Agent skills and MCP servers](#ai-agent-skills-and-mcp-servers)
  * [Setup of AI Agent harness and skills](#setup-of-ai-agent-harness-and-skills)
    * [Getting started with Copilot on a Proxmox host](#getting-started-with-copilot-on-a-proxmox-host)
      * [Getting started with the proxmox\-admin skill](#getting-started-with-the-proxmox-admin-skill)
      * [Getting started with the nginx\-configuration skill](#getting-started-with-the-nginx-configuration-skill)
      * [Getting started with the systemd skill](#getting-started-with-the-systemd-skill)
    * [Setup of Copilot on a Proxmox host](#setup-of-copilot-on-a-proxmox-host)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

## Overview

[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/infrastructure/proxmox/)
collects a few reference material about the
[Proxmox Virtual Environment (VE) framework](https://proxmox.com/en/products/proxmox-virtual-environment/overview).

> Proxmox Virtual Environment is a complete, open-source server management
> platform for enterprise virtualization. It tightly integrates the KVM
> hypervisor and Linux Containers (LXC), software-defined storage and networking
> functionality, on a single platform. With the integrated web-based user
> interface you can manage VMs and containers, high availability for clusters,
> or the integrated disaster recovery tools with ease.

The setup of Proxmox itself is well described in a
[dedicated GitHub repository](https://github.com/cloud-helpers/kubernetes-hard-way-bare-metal/blob/master/proxmox/)
and is therefore out of scope of this cheat sheet. Rather, this cheat sheet
showcases a few tools on top of the Proxmox VE platform, such as how to run
Copilot in order to troubleshoot the Proxmox host and/or its containers.

## References

### Knowledge Sharing

* [Cloud Helpers - Knowledge Sharing - Setup of a Proxmox host](https://github.com/cloud-helpers/kubernetes-hard-way-bare-metal/blob/master/proxmox/)
* [Cloud Helpers - Knowledge Sharing - Setup of Linux containers (LXC)](https://github.com/cloud-helpers/kubernetes-hard-way-bare-metal/blob/master/lxc/)
* [AI Helpers - Knowledge Sharing - AI skills curated](https://github.com/ai-helpers/ai-skills-curated)
* [Data Engineering Helpers - Knowledge Sharing - AI skills and rules](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/ai/rules-skills/)

### Proxmox

* [Proxmox home page](https://proxmox.com/en/)
* [Proxmox - Proxmox VE overview](https://proxmox.com/en/products/proxmox-virtual-environment/overview)
* [Proxmox VE wiki](https://pve.proxmox.com/wiki/Main_Page)

### AI Agent skills and MCP servers

* proxmox-admin:
  * [Skills.sh - proxomox-admin](https://www.skills.sh/bastos/skills/proxmox-admin)
  * [GitHub - proxomox-admin Agent Skill](https://github.com/bastos/skills/tree/main/proxmox-admin)
* [GitHub - proxmox-ops OpenClaw skill](https://github.com/eddygk/proxmox-ops)
* systemd-services:
  * [Skills.sh - systemd-services](https://www.skills.sh/bagelhole/devops-security-agent-skills/systemd-services)
  * [GitHub - systemd-services Agent Skill](https://github.com/BagelHole/DevOps-Security-Agent-Skills/tree/main/infrastructure/servers/systemd-services)
* Nginx-configuration:
  * [Skills.sh - nginx-configuration Agent Skill](https://www.skills.sh/aj-geddes/useful-ai-prompts/nginx-configuration)
  * [GitHub - nginx-configuration Agent Skill](https://github.com/aj-geddes/useful-ai-prompts/tree/main/skills/nginx-configuration)

## Setup of AI Agent harness and skills

### Getting started with Copilot on a Proxmox host

* Launch Copilot and login:

```bash
copilot
```

```agent
/login
```

#### Getting started with the proxmox-admin skill

* (In the Copilot CLI, invoke the `proxmox-admin` skill) to list the containers:

```agent
/proxmox-admin list containers
```

* (In the Copilot CLI, invoke the `proxmox-admin` skill) to upgrade the (Linux)
  distribution of a given container:

```agent
/proxmox-admin upgrade distribution of container #CTID
```

#### Getting started with the nginx-configuration skill

* (In the Copilot CLI, invoke the `nginx-configuration` skill) to check the
  Nginx configuration and fix the issues discovered by the agent (here, the
  agent suggested to change the error level from `error` to `warn`):

```agent
/nginx-configuration check configuration
...
yes, set the error_level to warn
```

* Request the agent to check the Nginx configuration and suggest potential fixes
  related to a Debian change log
  * Reference:
  [Debian - apt-listchanges](https://manpages.debian.org/testing/apt-listchanges/apt-listchanges.1.en.html)

```agent
/nginx-configuration Based on the following Debian change log, check
  the configuration and suggest potential fixes:
nginx (1.26.3-3+deb13u4) UNRELEASED; urgency=medium

  * d/conf/*_params: use "$host" instead of "$http_host"
    * "$http_host" forwards the Host header exactly as supplied by the client
      and may not match the effective request target (e.g. absolute-form
      requests with a conflicting Host header)
      this can expose inconsistent or attacker-controlled host values to
      backend applications (uwsgi, fastcgi, scgi, proxy)
    * switch to "$host" as a safer, normalized alternative
    * note: this changes behaviour, as "$host" does not preserve the
      client-supplied port; deployments relying on "$http_host" including
      a port number may be affected
    * it is workaround for Debian bug #1126960 for stable/oldstable release
```

#### Getting started with the systemd skill

* (In the Copilot CLI, invoke the `systemd-services` skill) to check the SystemD
  configuration and fix the issues discovered by the agent (here, analyze SSH
  service logs and proceed with the installation of `fail2ban`):

```agent
/systemd-services analyze the sshd logs and make suggestions
...
yes, install, configure and start fail2ban
```

### Setup of Copilot on a Proxmox host

* Reference:
 [GitHub Copilot docs - How-to install Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli)

* Prerequisites:
  * Copilot subcription - [Copilot plans](https://github.com/features/copilot/plans?ref_product=copilot&ref_type=engagement&ref_style=text)
  * JavaScript/Node -
  [Data Engineering Helpers - Knowledge Sharing - JavaScript (JS) world](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/js-world/)

* On the Proxmox host, install the Copilot CLI:

```bash
curl -fsSL https://gh.io/copilot-install | bash
```

* Configure Copilot by launching it a first time:

```bash
copilot
```

* If on a trusted device, the state may be saved permanently.
  Even so, login will be required every so often:

```agent
/login
```

* Quit Copilot:

```agent
/quit
```

* Install the `proxmox-admin` skill globally:

```bash
npx skills add https://github.com/bastos/skills --skill proxmox-admin -g
```

* Install the `nginx-configuration` skill globally:

```bash
npx skills add https://github.com/aj-geddes/useful-ai-prompts \
  --skill nginx-configuration -g
```
