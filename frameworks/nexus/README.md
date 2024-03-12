Cheat Sheet - Nexus Repository Manager
======================================

# Table of Content (ToC)
* [Overview](#overview)
* [References](#references)
  * [Data Engineering helpers](#data-engineering-helpers)
  * [Nexus](#nexus)
* [Installation](#installation)
  * [Clone this Git repository](#clone-this-git-repository)
  * [Java (OpenJDK)](#java-openjdk)
  * [nexus Unix user](#nexus-unix-user)
  * [Nexus software](#nexus-software)
  * [Nexus as a SystemD service](#nexus-as-a-systemd-service)
  * [Setup the credentials for the administrator](#setup-the-credentials-for-the-administrator)
  * [Check the Nexus version](#check-the-nexus-version)
  * [Do some cleaning](#do-some-cleaning)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/nexus/README.md)
explains how to setup the open source version of the Nexus Repository Manager
service, so as to store and manage software artifacts (_e.g._, Python wheels,
Java-world JARs, R packages, Linux RPM and Debian packages, static internet
pages).

# References

## Data Engineering helpers
* [Architecture principles for data engineering pipelines on the Modern Data Stack (MDS)](https://github.com/data-engineering-helpers/architecture-principles)
* [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md)

## Nexus
* How to install Nexus 3 on an EC2 instance:
  https://devopscube.com/how-to-install-latest-sonatype-nexus-3-on-linux/
* How to install Nexus on Kubernetes:
  https://devopscube.com/setup-nexus-kubernetes/
* Upgrading a standalone instance:
  https://help.sonatype.com/repomanager3/installation-and-upgrades/upgrading-a-standalone-instance
* Latest releases:
  + https://help.sonatype.com/repomanager3/product-information/release-notes
  + https://help.sonatype.com/repomanager3/download 

# Installation
The procedure has been tested on RPM-based Linux distributions (_e.g._,
CentOS, Fedora, RedHat, Rocky, Alma), and could probably be easily adapted
for Debian-based Linux distributions or even MacOS.

## Clone this Git repository
* Prepare the local file-system:
```bash
$ mkdir -p ~/dev/knowledge-sharing
```

* Clone this Git repository:
```bash
$ git clone git@github.com:data-engineering-helpers/ks-cheat-sheets.git \
	~/dev/knowledge-sharing/ks-cheat-sheets
```

* Go into the local clone of this Git repository:
```bash
$ cd ~/dev/knowledge-sharing/ks-cheat-sheets
```

## Java (OpenJDK)
* Install OpenJDK 1.8.0:
```bash
$ sudo dnf -y install java-1.8.0-openjdk java-1.8.0-openjdk-headless
```

* Check that the OpenJDK 1.8 has been installed:
```bash
$ rpm -qa|grep "openjdk-1.8.0"
java-1.8.0-openjdk-1.8.0.322.b06-11.el8.x86_64
```

* Optionally, install the OpenJDK 11 and OpenJDK 17 (as of beginning 2024,
  it is the long term support (LTS) version of Java):
```bash
$ sudo dnf -y install java-11-openjdk java-11-openjdk-headless
  sudo dnf -y install java-17-openjdk java-17-openjdk-headless
```

## `nexus` Unix user
* Create a `nexus` Unix user:
```bash
$ sudo adduser nexus
```

## Nexus software
* This procedure works for an initial installation as well as for an upgrade

* Most of the commands have to be executed as the `nexus` user. For instance,
  to switch to the `nexus` user from a user having admin rights:
```bash
user@mynexussvr$ sudo su - nexus
```
  + An alternative is to connect with SSH directly as the nexus user:
```bash
user@laptop$ ssh mynexussvr -l nexus
```

* The admin commands have to be executed from a user having the `sudo` rights
  on the remote machine. The simplest way is to directly connect with SSH
  as such an admin user:
```bash
user@laptop$ ssh mynexussvr -l admin
```

* As an admin, create the `/opt/nexus` directory:
```bash
admin@mynexussvr$ sudo mkdir -p /opt/nexus
  sudo chown -R nexus.nexus /opt/nexus
```

* Spot the latest version on
  https://help.sonatype.com/repomanager3/product-information/download and
  set the `NEXUS_VERSION` environment variable to the corresponding value:
```bash
nexus@mynexussvr$ NEXUS_VERSION="3.66.0-02"
```

* Donwload the latest Nexus tar-ball from
  https://help.sonatype.com/repomanager3/product-information/download :
```bash
nexus@mynexussvr$ mkdir -p /opt/nexus/archives && \
  curl -kL https://download.sonatype.com/nexus/3/nexus-${NEXUS_VERSION}-unix.tar.gz \
       -o /opt/nexus/archives/nexus-${NEXUS_VERSION}-unix.tar.gz
```

* Note that the Nexus tar-ball may also be obtained from the commercial
  Sonatype pages (if, for some reason, the above page is no longer available),
  _i.e._, https://www.sonatype.com/products/repository-oss-download .
  However, note that as of October 2022, Sonatype imposes to enter business
  contact details in order to download the Nexus tar-ball.
  In that case, the tar-ball has to be downloaded on the laptop,
  and transferred to the remote machine:
```bash
user@laptop$ rsync -av ~/Downloads/nexus-${NEXUS_VERSION}-unix.tar.gz nexus@mynexussvr:~/archives/
```

* As an admin user, if the Nexus SystemD service is already running, stop it:
```bash
admin@mynexussvr$ sudo systemctl stop nexus.service
```

* Un-tar the archive (tar-ball):
```bash
nexus@mynexussvr$ tar zxf archives/nexus-${NEXUS_VERSION}-unix.tar.gz
```

* Create a `nexus-latest` symbolic link to the latest version folder of Nexus:
```bash
nexus@mynexussvr$ rm -f nexus-latest && ln -s nexus-${NEXUS_VERSION} nexus-latest
```

* Configure Nexus to be run with the `nexus` Unix user:
```bash
nexus@mynexussvr$ sed -i -e 's/#run_as_user=""/run_as_user="nexus"/' /opt/nexus/nexus-latest/bin/nexus.rc
```

* As an admin user, adapt the SE Linux context for the `nexus` binary:
```bash
admin@mynexussvr$ sudo chcon -R -t bin_t /opt/nexus/nexus-latest/bin
                 sudo restorecon -R -v /opt/nexus
```
  + Check the SE Linux context of Python executables:
```bash
admin@mynexussvr$ sudo ls -Z /opt/nexus/nexus-latest/bin/nexus
unconfined_u:object_r:bin_t:s0 /opt/nexus/nexus-latest/bin/nexus
```
  + Restart the Nexus SystemD service:
```bash
admin@mynexussvr$ sudo systemctl start nexus.service
```

* Check that the SystemD service has successfully started:
```bash
nexus@mynexussvr$ systemctl status -l nexus.service
```

## Nexus as a SystemD service
* If the Nexus SystemD service is already running, stop it:
```bash
admin@mynexussvr$ sudo systemctl stop nexus.service
```

* If not already done so, setup Nexus as a SystemD service:
```bash
admin@mynexussvr$ sudo cp ~/dev/knowledge-sharing/ks-cheat-sheets/main/tree/frameworks/nexus/systemd/nexus.service /usr/lib/systemd/system/
admin@mynexussvr$ sudo systemctl daemon-reload
admin@mynexussvr$ sudo systemctl enable nexus.service
```

* Start the Nexus SystemD service:
```bash
admin@mynexussvr$ sudo systemctl start nexus.service
```

* Check that the SystemD service has successfully started:
```bash
admin@mynexussvr$ systemctl status -l nexus.service
```

* If the service failed to start, it may help to look through the logs:
```bash
admin@mynexussvr$ sudo journalctl -xeu nexus.service
```

* The Nexus repository manager should have started on port `8081`:
```bash
admin@mynexussvr$ curl http://localhost:8081
```

## Setup the credentials for the administrator
* The password for the `admin` account is available from the
  `/home/nexus/sonatype-work/nexus3/admin.password` temporary local file
  (once the password will have been setup through the web interface,
  that local file will be deleted):
```bash
nexus@mynexussvr$ cat /home/nexus/sonatype-work/nexus3/admin.password
```

## Check the Nexus version
* From the Nexus remote server instance:
```bash
nexus@mynexussvr$ curl -is http://localhost:8081/ | grep Server
Server: Nexus/${NEXUS_VERSION} (OSS)
```

* From the broader network:
```bash
$ curl -is http://mynexussvr.example.org/ | grep Server
Server: Nexus/${NEXUS_VERSION} (OSS)
```

## Do some cleaning
* When everything works well, as the `nexus` user, remove older versions:
```bash
nexus@mynexussvr$ rm -rf nexus-${NEXUS_VERSION}
```

