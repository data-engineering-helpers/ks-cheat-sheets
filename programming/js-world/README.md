Cheat Sheets - JavaScript (JS)
==============================

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/js-world/README.md)
explains how to install and to maintain a few tools pertaining to
programming with JavaScript.

# Quick start

## NVM - Parallel installable NodeJS
* Reference: https://github.com/nvm-sh/nvm#install--update-script

* Releases: https://github.com/nvm-sh/nvm/releases
  + Tags: https://github.com/nvm-sh/nvm/tags

* Install, or update, NVM (for parallel installation of Node) into `~/.nvm`:
```bash
$ NVM_VER=$(curl -Ls https://api.github.com/repos/nvm-sh/nvm/releases/latest | grep 'tag_name' | cut -d'v' -f2 | cut -d'"' -f1)
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v${NVM_VER}/install.sh | bash
```
  * To upgrade NVM, just go into the NVM folder (`~/.nvm`) and pull the latest
    changes:
```bash
$ pushd ~/.nvm && git pull && popd
```
  * Reset the terminal:
```bash
$ exec bash
```
  * Check the version of NVM:
```bash
$ nvm --version
0.39.7
```

## NodeJS
* Reference: https://nodejs.org/en/blog/release

* List the installed versions of NodeJS:
```bash
$ nvm ls
```

* List the available versions of NodeJS, which may be installed locally:
```bash
$ nvm ls-remote
```

* If there are no specific need, it is better to install the latest
  Long Term Support (LTS) release

* Install some specific version of NodeJS:
```bash
$ nvm install 20.15.1
Downloading and installing node v20.15.1...
...
Now using node v20.15.1 (npm v10.7.0)
```

* Have a specific NodeJS version as global default:
```bash
$ nvm use 20.15.1
Now using node v20.15.1 (npm v10.7.0)
```

* Uninstall some older version of NodeJS:
```bash
$ nvm uninstall 20.14.0
Uninstalled node v20.14.0
```

* Set default Node version on the Shell:
```bash
$ nvm alias default 20.15.1
default -> 20.15.1 (-> v20.15.1)
```

## Node modules

### Yarn
* Reference: https://classic.yarnpkg.com/en/docs/install#mac-stable

* Install Yarn:
```bash
$ npm install -g yarn
```

### TypeScript (TS)
* Reference: https://www.npmjs.com/package/ts-node

* Install TypeScript and `ts-node`:
```bash
$ npm install -g typescript
  npm install -g ts-node
```

# Update / upgrade
* In a given project
  * Download the latest information about packages:
```bash
$ npm update
```
  * Upgrade the packages of the project (as seen in the `package-lock.json`
    file):
```bash
$ npm upgrade
```


