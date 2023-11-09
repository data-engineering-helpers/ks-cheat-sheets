Cheat Sheet - Kubernetes (K8S)
==============================

# Table of Content (ToC)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/k8s/README.md)
explains how to use Kubernetes services, that is, installing Kubernetes client utilities such as `kubectl`
and interacting with remote Kubernetes services (_e.g._, pods, services, jobs).

# References

## Data Engineering helpers
* [Architecture principles for data engineering pipelines on the Modern Data Stack (MDS)](https://github.com/data-engineering-helpers/architecture-principles)
* [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md)

# Installation

## On laptops and desktops
* Container-related utilities, such as Docker and Kubernetes command-line interfaces (_resp._ `docker` and
  `kubectl`) may be installed from all-in-one desktop applications like
  [Rancher Desktop](https://rancherdesktop.io/), [Podman desktop](https://podman-desktop.io/) and
  [Docker Desktop](https://www.docker.com/products/docker-desktop/) (be aware that the license of that latter
  usually does not allow to use it in a corporate environment without the company signing a global agreement
  with Docker first)

## Linux
* Docker and Kubernetes client command-line interfaces (_resp._ `docker` and `kubectl`) are usually available
  as native packages on most of the Linux distributions. Installing them is as easy as launching the corresponding
  commands
  + On RPM-based distributions (_e.g._, RedHat, CentOS, Rocky, Alma, Fedora):
    `dnf -y install docker-ce-cli kubectl`
  + On Debian-derived distributions (_e.g._, Debian, Ubuntu):
    `apt-get update && apt-get install -y docker kubectl`
  

