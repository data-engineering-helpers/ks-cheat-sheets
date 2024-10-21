Cheat Sheet - HashiCorp Vault
=============================

# Table of Content (ToC)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/secret-management/hashicorp-vault/README.md)
explains how to install and to use 
[HasiCorp Vault](https://developer.hashicorp.com/vault/tutorials/getting-started/getting-started-install)
on premises, _e.g._, on a laptop or on a virtual machine (VM).

# References
* [HashiCorp - Developer docs - Getting started - Installation](https://developer.hashicorp.com/vault/tutorials/getting-started/getting-started-install)
  * [HashiCorp - Developer docs - Install Vault](https://developer.hashicorp.com/vault/install)

# Setup

## MacOS
* Install HashiCorp Vault with HomeBrew:
```bash
brew tap hashicorp/tap
brew install hashicorp/tap/vault
```

* In the Shell init script (_e.g._, `~/.bashrc`), specifiy the `VAULT_ADDR` environment variable:
```bash
export VAULT_ADDR="https://some.vaultdomain.my.cloud"
```

## Interact with the HashiCorp Vault
* Once in a while, login to the Vault
  * Sign in with the domain SSO (single sign on) on a web browser
```bash
vault login -method=oidc
```
  * That opens a tab in the current web browser window and checks
    that the SSO is still valid, and then setups the Vault token
    in the `~/.vault-token` file

* Display the various key-value pairs and paths available for the project:
```bash
vault kv list -namespace=mynm -mount="secret-mydom" "some/specific/path"
Keys
----
path1
path2
somedir/
```

* Display the Vault key-value pairs for a specific path:
```bash
vault kv get -namespace=mynm -mount="secret-mydom" "some/specific/path"
============= Data =============
Key                         Value
---                         -----
...
some_key1                   some_value1
some_key2                   some_value2
```

