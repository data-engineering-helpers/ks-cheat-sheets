Cheat Sheet - Docker
====================

# Table of Content (ToC)
* [Overview](#overview)
* [References](#references)
  * [Data Engineering helpers](#data-engineering-helpers)
  * [Docker utilties and alternatives](#docker-utilties-and-alternatives)
    * [Docker Desktop](#docker-desktop)
    * [Rancher Desktop](#rancher-desktop)
    * [Podman Desktop](#podman-desktop)
  * [Docker plugins](#docker-plugins)
    * [Docker compose](#docker-compose)
    * [SBOM](#sbom)
* [Typical workflow](#typical-workflow)
* [Build images for multiple platforms](#build-images-for-multiple-platforms)
* [Installation](#installation)
  * [Docker repository for Linux distributions](#docker-repository-for-linux-distributions)
    * [CentOS](#centos)
    * [Ubuntu](#ubuntu)
    * [Debian](#debian)
  * [Docker BuildKit plugin](#docker-buildkit-plugin)
    * [MacOS](#macos)
    * [Linux](#linux)
  * [Docker compose plugin](#docker-compose-plugin)
    * [MacOS](#macos-1)
      * [(Optional) MacOS \- Install the Docker compose plugin with HomeBrew](#optional-macos---install-the-docker-compose-plugin-with-homebrew)
    * [Linux](#linux-1)
  * [SBOM plugin](#sbom-plugin)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/infrastructure/docker/README.md)
references material and lists a few usual commands to manage containers
compliant with the
[Open Container Initiative (OCI)](https://opencontainers.org/), including Docker
containers and images.

# References

## Data Engineering helpers
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box/blob/main/README.md)
* [Data Engineering Helpers - Knowledge Sharing - Cheat Sheets (this Git repository)](https://github.com/data-engineering-helpers/ks-cheat-sheets)

## Docker utilties and alternatives

### Docker Desktop
* [Docker docs - Install Docker Desktop on MacOS](https://docs.docker.com/desktop/setup/install/mac-install/)
* [Docker docs - Install Docker Desktop on Linux](https://docs.docker.com/compose/install/linux/)
* [Docker docs - Install Docker Desktop on MS Windows](https://docs.docker.com/desktop/setup/install/windows-install/)

### Rancher Desktop
* [Rancher Desktop](https://rancherdesktop.io)

### Podman Desktop
* [Podman Desktop](https://podmani-desktop.io)

## Docker plugins

### Docker compose
* [Docker docs - Docker compose](https://docs.docker.com/compose/install/)

### SBOM
* [SPDX - Homepage](https://spdx.dev/)
  * [SPDX - Overview for users](https://spdx.dev/use/overview/)
* [Earthly docs - Docker SBOM](https://earthly.dev/blog/docker-sbom/)
* [GitHub - Docker SBOM plugin](https://github.com/docker/sbom-cli-plugin)
  for Docker-compatible CLI tools (like Rancher or Podman) not shipping
  with integrated SBOM
* SPDX tools
  * [GitHub - SPDX tools - Quickstart guides](https://github.com/spdx/outreach/tree/main/quickstart)
  * [GitHub - SPDX spec examples](https://github.com/spdx/spdx-spec/tree/development/v2.3.1/examples)

# Typical workflow
* Build an image:
```bash
$ docker build -t project-name:version \
    --build-arg some-var=some-value \
	./project-name/Dockerfile
```

* Tag the image:
```bash
$ docker tag project-name:version project-name:latest
```

* Publish the image:
```bash
$ docker push project-name:version
  docker push project-name:latest
```

* Create the SBOM for the image:
```bash
$ docker sbom project-name:version -o sbom.txt
```

# Build images for multiple platforms
* Source: [StackOverflow - Multiple-platform-feature](https://unix.stackexchange.com/a/748634/115196)

* Create a builder profile for multiple platforms (`X86_64` and `ARM64` here;
  if the `--platform` parameter is omitted, all the platforms are supported):
```bash
$ docker buildx create --use --platform=linux/arm64,linux/amd64 --name multi-platform-builder
```

* Check the builder profile:
```bash
$ docker buildx inspect --bootstrap
```

* Build an image for multiple platforms:
```bash
$ docker buildx build --platform=linux/arm64,linux/amd64 --push --tag project-name:latest -f ./project-name/Dockerfile .
```

* Build an image for multiple platforms, adding support for SBOM and provenance:
```bash
$ docker buildx build --platform=linux/arm64,linux/amd64 --provenance true --sbom true --push --tag project-name:latest -f ./project-name/Dockerfile .
```

# Installation
* On MacOS, most of the Docker tools may be installed thanks to [HomeBrew](https://brew.sh/).
  [Rancher Desktop](https://rancherdesktop.io) also features both the Docker BuildKit (`buildx`)
  and Docker Compose plugins

* On Linux, the easiest is to install the official Docker repository, featuring native packages
  for most of the Linux distributions (_e.g._, Debian, Ubuntu, CentOS, RHEL, Fedora)
  The official package repository also features a few Docker plugins like Compose and BuildKit

## Docker repository for Linux distributions
* If not already done so, install the Docker repository

### CentOS
* On CentOS:
```bash
sudo dnf -y install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```

### Ubuntu
* On Ubuntu:
```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

### Debian
* On Debian:
```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

## Docker BuildKit plugin

### MacOS
* Rancher Desktop features the Docker BuildKit plugin

### Linux
* Once the Docker repository has been added (see above section),
  install the `docker-buildx-plugin` package with the native package manager
  of the Linux distribution (_i.e._, `dnf install` for RPM-based distributions
  or `apt-get install` for Debian-based distributions)

## Docker compose plugin

### MacOS
* Rancher Desktop features the Docker compose plugin.

* The plugin is linked in the Docker plugin repository, _i.e._,
  `~/.docker/cli-plugins/`

#### (Optional) MacOS - Install the Docker compose plugin with HomeBrew
* If not already done so, and if not using Rancher Desktop (or Docker Desktop),
  install the Docker compose plugin with HomeBrew:
```bash
brew install docker-compose
```
* The plugin is installed in `$(brew --prefix)/lib/docker/cli-plugins/docker-compose`
  and the following lines have to be added to the `~/.docker/config.json` file
  (change `/opt/homebrew` by your own installation directory of HomeBrew):
```json
  "cliPluginsExtraDirs": [
      "/opt/homebrew/lib/docker/cli-plugins"
  ]
```

### Linux
* Install the Docker compose plugin
  * On RPM-based distributions:
```bash
sudo dnf update
sudo dnf -y install docker-compose-plugin
```
  * On Debian-based distributions:
```bash
sudo apt-get update
sudo apt-get -y install docker-compose-plugin
```

## SBOM plugin
* Install the [Docker SBOM plugin](https://github.com/docker/sbom-cli-plugin):
```bash
$ curl -sSfL https://raw.githubusercontent.com/docker/sbom-cli-plugin/main/install.sh | sh -s --
```
* The Docker SBOM may then be used on a specific image as follows:
```bash
$ docker sbom image-name:version --format spdx-json -o sbom.json
```

