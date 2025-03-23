Cheat Sheet - CMake
===================

# Table of Content (ToC)
* [Overview](#overview)
  * [Data Engineering helpers](#data-engineering-helpers)
  * [Documentation](#documentation)
* [Installation](#installation)
  * [Ubuntu](#ubuntu)
  * [Debian](#debian)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
* [This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/building/cmake/README.md)
  explains how to install and to use CMake.

## Data Engineering helpers
* [Data Engineering Helpers - Knowledge Sharing - Programming](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/)

## Documentation
* https://linuxcapable.com/how-to-install-cmake-on-debian-linux/
* [GitHub - CMake releases](https://github.com/Kitware/CMake/releases)
* [CMake download page](https://cmake.org/download/)
* [Kitware - apt repositories for Ubuntu](https://apt.kitware.com/)

# Installation

## Ubuntu
* Kitware maintains APT repositories for Ubuntu (LTS from 20.04):
  https://apt.kitware.com/

## Debian
* To have newer versions of CMake, they have to be built from sources.
  Helper documentation:
  https://linuxcapable.com/how-to-install-cmake-on-debian-linux/

* Remove any previous version of CMake (and potential no longer used packages):
```bash
sudo apt-get remove -y cmake && sudo apt-get autoremove -y
```

* Install a few system dependencies:
```bash
sudo apt install -y build-essential checkinstall zlib1g-dev libssl-dev
```

* Create a build directory:
```bash
sudo mkdir /opt/cmake && sudo chown ${USER} /opt/cmake
```

* Derive the version of the latest stable release for CMake:
```bash
CMAKE_VER=$(curl -Ls https://api.github.com/repos/Kitware/CMake/releases/latest | grep 'tag_name' | cut -d'v' -f2,2 | cut -d'"' -f1,1)
```

* Download the source tar-ball:
```bash
curl -Ls https://github.com/Kitware/CMake/archive/refs/tags/v${CMAKE_VER}.tar.gz -o /opt/cmake/cmake-${CMAKE_VER}.tar.gz
```

* Go into the build directory:
```bash
	pushd /opt/cmake
```

* Un-tar the source directory and delete the source tar-ball:
```bash
tar zxf cmake-${CMAKE_VER}.tar.gz && rm -f cmake-${CMAKE_VER}.tar.gz
```

* Go into the CMake directory:
```bash
pushd CMake-${CMAKE_VER}
```

* Boot-strap the build of CMake:
```bash
./bootstrap
```

* Launch the build of CMake:
```bash
gmake -j4
```

* Install CMake:
```bash
sudo make install
```

* Go back to the working directory:
```bash
popd && popd
```
