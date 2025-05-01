Mac world - HomeBrew
====================

# Getting started

## Write a HomeBrew file
* Curate a HomeBrew file, with the dependencies and some specific configuration, like:
```bash
cat > ~/.brewrc << _EOF

cask_args appdir: "~/Applications"

cask "bruno"

brew "git"
brew "gh"
brew "coreutils"
brew "gnu-sed"
brew "gawk"

_EOF
```
* Launch HomeBrew with that "bundle":
```bash
$ brew bundle --file ~/.brewrc
```
* The resulting applications (_e.g._, Bruno in the above example)
  are installed locally in the user folders, namely `~/Applications`

## A few packages from taps
* Companies/organizations may release their own packages, which are available
  on GitHub in specific `homebrew-tap` repositories in their respective
  GitHub public organizations, that is https://github.com/organization/homebrew-tap ,
  for instance https://github.com/databricks/homebrew-tap for DataBricks
  and https://github.com/hashicorp/homebrew-tap for HashiCorp.

* In order to install the "tap" from a specific company:
```bash
$ brew tap company/tap
```

* That usually clone the corresponding Git repository locally in a HomeBrew
  folder dedicated to taps, namely
  `$(brew --prefix)/Library/Taps/organization/homebrew-tap`
  (`$(brew --prefix)` usually expands to `/opt/homebrew`)

* And, then, to install a package from that tap:
```bash
$ brew install company/tap/package
```

### DataBricks
* References:
  * DataBricks helper page:
  https://docs.databricks.com/aws/en/dev-tools/cli/install

* Install the DataBricks tap:
```bash
$ brew tap databricks/tap
```

* Install the DataBricks CLI (command-line interface) utility:
```bash
$ brew install databricks/tap/databricks
```

### HashiCorp Vault
* References:
  * HashiCorp Vault helper page:
  https://developer.hashicorp.com/vault/install

* Install the HashiCorp tap:
```bash
$ brew tap hashicorp/tap
```

* Install the HashiCorp Vault CLI (command-line interface) utility:
```bash
$ brew install hashicorp/tap/vault
```

### MinIO
* References:
  * MinIO helper page to install it on MacOS:
  https://min.io/docs/minio/macos/index.html

* If any previous standard installation has been made, uninstall it:
```bash
$ brew uninstall minio
```

* Install the MinIO tap:
```bash
$ brew install minio/stable/minio
```

* Install MinIO:
```bash
$ brew install minio mc
```

## LakeFS
* References:
  * GitHub repository: https://github.com/treeverse/homebrew-lakefs

* Install the LakeFS tap:
```bash
$ brew tap treeverse/lakefs
```

* Install LakeFS:
```bash
$ brew install lakefs
```

