Cheat Sheets - JavaScript (JS)
==============================

# Table of Content (ToC)
* [Overview](#overview)
* [Quick start](#quick-start)
  * [NVM \- Parallel installable NodeJS](#nvm---parallel-installable-nodejs)
  * [NodeJS](#nodejs)
  * [Node modules](#node-modules)
    * [npx](#npx)
    * [Yarn](#yarn)
    * [TypeScript (TS)](#typescript-ts)
* [Update / upgrade](#update--upgrade)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/js-world/README.md)
explains how to install and to maintain a few tools pertaining to
programming with JavaScript.

# Quick start

## NVM - Parallel installable NodeJS
* Reference: https://github.com/nvm-sh/nvm#install--update-script

* Releases: https://github.com/nvm-sh/nvm/releases
  + Tags: https://github.com/nvm-sh/nvm/tags

### MacOS
* Install [NVM with HomeBrew](https://formulae.brew.sh/formula/nvm):
```bash
brew install nvm
```

### Generic
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

### Post-installation
* Reset the terminal:
```bash
$ exec bash
```
  * Check the version of NVM:
```bash
$ nvm --version
0.40.3
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
$ nvm install 25.1.0
Downloading and installing node v25.1.0...
...
Now using node v25.1.0 (npm v11.6.2)
```

* Have a specific NodeJS version as global default:
```bash
$ nvm use 25.1.0
Now using node v25.1.0 (npm v11.6.2)
```

* Uninstall some older version of NodeJS:
```bash
$ nvm uninstall v22.19.0
Uninstalled node v22.19.0
```

* Set default Node version on the Shell:
```bash
$ nvm alias default 25.1.0
default -> 25.1.0 (-> v25.1.0)
```

## Node modules
* npm (node package manager) is the dependency/package manager that
  we get out of the box when we install Node.js (see above).
  It provides a way for developers to install packages both globally
  and locally
  * First and foremost, it is an online repository for the publishing
  of open-source Node.js projects
  * Second, it is a CLI tool that aids you install those packages
  and manage their versions and dependencies. There are hundreds of thousands
  of Node.js libraries and applications on npm and many more are added
  every day

* npm by itself does not run any packages. If we want to run a package
  using npm, we must specify that package in the `package.json` file.

* When executables are installed via npm packages, npm creates links to them:
  * local installs have links created at the `./node_modules/.bin/` directory
  * global installs have links created from the global `bin/` directory
  (for example, `/usr/local/bin` on Linux or at `%AppData%/npm` on MS Windows)

* To execute a package with npm we either have to type the local path,
  like this:
```bash
$ ./node_modules/.bin/your-package
```

* Or we can run a locally installed package by adding it into
  the `package.json` file in the scripts section, like this:
```json
{
  "name": "your-application",
  "version": "1.0.0",
  "scripts": {
    "your-package": "your-package"
  }
}
```

* Then the script may be run using `npm run`:
```bash
npm run your-package
```

* We can see that running a package with plain npm requires quite a bit
  of ceremony. Fortunately, this is where npx comes in handy:
  * Sometimes we might want to take a look at a specific package
  and try out some commands. But we cannot do that without installing
  the dependencies in our local `node_modules` folder

### npx
* References:
  * npx command in the command-line (CLI):
  https://docs.npmjs.com/cli/v8/commands/npx
  * npx package, now part of npm: https://www.npmjs.com/package/npx

* The `npx` command allows to run an arbitrary command from an npm package
  (either one installed locally, or fetched remotely), in a similar context
  as running it via `npm run`.

### Yarn
* Reference: https://classic.yarnpkg.com/en/docs/install#mac-stable

* Install Yarn:
```bash
$ npm install -g yarn
added 1 package in 883ms
```

* Check the version of Yarn:
```bash
$ yarn --version
1.22.22
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


