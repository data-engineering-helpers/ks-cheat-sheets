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
* [Typical workflow](#typical-workflow)
* [Build images for multiple platforms](#build-images-for-multiple-platforms)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/docker/README.md)
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

### Rancher Desktop

### Podman Desktop

## SBOM
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

## SBOM plugin
* Install the [Docker SBOM plugin](https://github.com/docker/sbom-cli-plugin):
```bash
$ curl -sSfL https://raw.githubusercontent.com/docker/sbom-cli-plugin/main/install.sh | sh -s --
```
* The Docker SBOM may then be used on a specific image as follows:
```bash
$ docker sbom image-name:version --format spdx-json -o sbom.json
```
