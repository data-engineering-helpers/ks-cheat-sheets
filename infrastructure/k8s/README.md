Cheat Sheet - Kubernetes (K8S)
==============================

# Table of Content (ToC)
* [Overview](#overview)
* [References](#references)
  * [Data Engineering helpers](#data-engineering-helpers)
* [Installation](#installation)
  * [On laptops and desktops](#on-laptops-and-desktops)
  * [Linux](#linux)
* [Installation](#installation-1)
  * [Shell variables and aliases](#shell-variables-and-aliases)
* [Trouble\-shooting \- Getting started with Kubernetes](#trouble-shooting---getting-started-with-kubernetes)
  * [Switch to a specific cluster and namespace](#switch-to-a-specific-cluster-and-namespace)
  * [Launch an elementary interactive Shell](#launch-an-elementary-interactive-shell)
  * [Launch a simple PostgreSQL database service](#launch-a-simple-postgresql-database-service)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/infrastructure/k8s/README.md)
explains how to use Kubernetes services, that is, installing Kubernetes client
utilities such as `kubectl` and interacting with remote Kubernetes services
(_e.g._, pods, services, jobs).

# References

## Data Engineering helpers
* [Architecture principles for data engineering pipelines on the Modern Data Stack (MDS)](https://github.com/data-engineering-helpers/architecture-principles)
* [Data Engineering Helpers - Knowledge Sharing - AWS](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/clouds/aws/)
* [Data Engineering Helpers - Knowledge Sharing - PostgreSQL](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/README.md)
* [Cloud helpers - Kubernetes The Hard Way - Bare Metal with VM and Containers](https://github.com/cloud-helpers/kubernetes-hard-way-bare-metal)

# Installation

## On laptops and desktops
* Container-related utilities, such as Docker and Kubernetes command-line
  interfaces (_resp._ `docker` and `kubectl`) may be installed from all-in-one
  desktop applications like
  [Rancher Desktop](https://rancherdesktop.io/), [Podman desktop](https://podman-desktop.io/) and
  [Docker Desktop](https://www.docker.com/products/docker-desktop/) (be aware
  that the license of that latter usually does not allow to use it in
  a corporate environment without the company signing a global agreement
  with Docker first)

## Linux
* Docker and Kubernetes client command-line interfaces (_resp._ `docker`
  and `kubectl`) are usually available as native packages on most of the
  Linux distributions. Installing them is as easy as launching
  the corresponding commands
  + On RPM-based distributions (_e.g._, RedHat, CentOS, Rocky, Alma, Fedora):
    `dnf -y install docker-ce-cli kubectl`
  + On Debian-derived distributions (_e.g._, Debian, Ubuntu):
    `apt-get update && apt-get install -y docker kubectl` 

# Installation

## Shell variables and aliases
* Add a few Shell aliases:
```bash
$ cat >> ~/.bash_aliases << _EOF

# K8S

## Login on AWS with SAML
alias awsumesaml='awsume saml'
alias awslogin='saml2aws login --force; awsume saml'

## Utility
alias kc='kubectl'
alias kcpod='kubectl get pod'
alias kcpodall='kubectl get pod --all-namespaces'
alias kcing='kubectl get ingress'
alias kcingall='kubectl get ingress --all-namespaces'
alias kcall='kubectl get all'
alias kcallall='kubectl get all --all-namespaces'

## Rancher desktop cluster
alias kubectxsetrancher='kubectx rancher-desktop'
alias kubenssetrancher='kubens default'

## AWS EKS cluster and namespace
alias kubectxsetekscluster='awsumesaml ; aws eks --region eu-west-1 update-kubeconfig --name my-eks-cluster'
alias kubensseteksnamespace='kubectxsetekscluster ; kubectl config set-context --current --namespace=my-eks-namespace'

_EOF
$ . ~/.bash_aliases
```

# Trouble-shooting - Getting started with Kubernetes

## Switch to a specific cluster and namespace
* If necessary for your environment, login with SAML on AWS (and, once logged,
  select the right role, typically the IDP in pre-production, _e.g._,
  `Account: my-corporate-account (012345678901) / USERID`):
```bash
$ awslogin
```

* Switch to a specific cluster (context) and namespace
  + For the local k8s cluster powered by Rancher Desktop:
```bash
$ kubenssetrancher
Context "rancher-desktop" modified.
Active namespace is "default".
```
  + For a specific AWS EKS cluster and namespace:
```bash
$ kubensseteksnamespace
Updated context arn:aws:eks:eu-west-1:012345678901:cluster/my-eks-cluster in ~/.kube/config
Context "arn:aws:eks:eu-west-1:012345678901:cluster/my-eks-cluster" modified.
```

* List all the pods on the cluster:
```bash
$ kc get pods --all-namespaces
...
```

* List all the services on the cluster:
```bash
$ kc get all --all-namespaces
...
```

## Launch an elementary interactive Shell
* Deploy a service-oriented pod:
```bash
$ kubectl apply -f demos/simple-shell.yaml
pod/shell-demo created
```

* Check that the Kubenertes pod is running:
```bash
$ kubectl get pods
NAME         READY   STATUS    RESTARTS   AGE
shell-demo   1/1     Running   0          82s
```

* Launch an interactive Shell and execute a few Shell commands:
```bash
$ kubectl exec -it shell-demo -- bash
I have no name!@shell-demo:/$ id
uid=1000 gid=0(root) groups=0(root)
I have no name!@shell-demo:/$ df -h .
Filesystem      Size  Used Avail Use% Mounted on
overlay          99G   23G   76G  23% /
I have no name!@shell-demo:/$ cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
NAME="Debian GNU/Linux"
...
I have no name!@shell-demo:/$ uname -a
Linux shell-demo 5.15.134 #1 SMP Wed Oct 25 06:51:24 UTC 2023 x86_64 GNU/Linux
I have no name!@shell-demo:/$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
I have no name!@shell-demo:/$ exit
exit
```

* Shutdown the Kubernetes service:
```bash
$ kubectl delete -f demos/simple-shell.yaml
pod "shell-demo" deleted
```

## Launch a simple PostgreSQL database service
* Deploy the PostgreSQL service:
```bash
$ kubectl apply -f demos/simple-postgresql.yaml
statefulset.apps/db created
```

* Check that the PostgreSQL Kubenertes service is running
  + Check all the k8s services:
```bash
$ kubectl get all
NAME       READY   STATUS    RESTARTS   AGE
pod/db-0   1/1     Running   0          58s

NAME                  READY   AGE
statefulset.apps/db   1/1     58s
```
  + Check only the k8s pods:
```bash
$ kubectl get pods
NAME   READY   STATUS    RESTARTS   AGE
db-0   1/1     Running   0          112s
```
  + Wait for the k8s pods to start (type Control-C to leave the waiting mode
    when the pods are ready):
```bash
$ kubectl get pods -w
NAME   READY   STATUS    RESTARTS   AGE
db-0   1/1     Running   0          112s
```

* Show the logs of the pod:
```bash
$ kubectl logs db-0
The files belonging to this database system will be owned by user "postgres".
This user must also own the server process.

  ...

PostgreSQL init process complete; ready for start up.

Some-Date [1] LOG:  starting PostgreSQL xx.x (Debian xx.x-x.pgdg120+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian xx.x.x-xx) xx.x.x, 64-bit
Some-Date [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
Some-Date [1] LOG:  listening on IPv6 address "::", port 5432
Some-Date [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
Some-Date [49] LOG:  database system was shut down at Some-Date
Some-Date [1] LOG:  database system is ready to accept connections
```

* Check that the database executes SQL queries correctly:
```bash
$ kubectl exec -it db-0 -- psql -c "select 42 as test;"
 test 
------
   42
(1 row)
```

* Launch an interactive Shell session
  + Launch the Shell session:
```bash
$ kubectl exec -it db-0 -- bash
postgres@db-0:/$ psql -c "select 42 as test;"
 test 
------
   42
(1 row)
```
  + From the Shell session, launch the interactive PostgreSQL client:
```bash
postgres@db-0:/$ psql
psql (16.0 (Debian 16.0-1.pgdg120+1))
Type "help" for help.

postgres=# 
```
  + Execute SQL queries:
```sql
postgres=# select 42 as test;
test 
------
   42
(1 row)
postgres=# 
```
  + Exit the PostgreSQL interactive client:
```sql
postgres=# \q
```
```bash
postgres@db-0:/$
```
  + Visit the file-system in the PostgreSQL data directory:
```bash
postgres@db-0:/$ cd
postgres@db-0:~/$ pwd
/var/lib/postgresql
postgres@db-0:~$ id
uid=999(postgres) gid=999(postgres) groups=999(postgres),101(ssl-cert)
postgres@db-0:~/$ mount | grep postgresql
/dev/nvme1n1p1 on /var/lib/postgresql/data type ext4 (rw,nosuid,nodev,noatime,seclabel)
postgres@db-0:~/$ cd data/pgdata
postgres@db-0:~/data/pgdata$ df -h .
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme1n1p1   99G   23G   76G  24% /var/lib/postgresql/data
```
  + Exit the interactive Shell session:
```bash
postgres@db-0:~/$ exit
exit
```

* Shutdown the Kubernetes PostgreSQL service:
```bash
$ kubectl delete -f demos/simple-postgresql.yaml
statefulset.apps "db" deleted
```

