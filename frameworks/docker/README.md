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
