Cheat Sheets - JavaScript (JS)
==============================

# Quick start

## NVM - Parallel installable NodeJS
* Reference: https://github.com/nvm-sh/nvm#install--update-script

* Install NVM (for parallel installation of Node):
```bash
$ curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
```

* Reset the terminal:
```bash
$ exec bash
```

## NodeJS
* Reference: https://nodejs.org/en/blog/release

* If there are no specific need, it is better to install the latest
  Long Term Support (LTS) release

* Install some specific version of NodeJS:
```bash
$ nvm install 18.16.0
```

* Have a specific NodeJS version as global default:
```bash
$ nvm use 18.16.0
```

## Node modules

### Yarn
* Reference: https://classic.yarnpkg.com/en/docs/install#mac-stable

* Install Yarn:
```bash
$ npm install --global yarn
```

# Update / upgrade
* In a given project
  + Download the latest information about packages:
```bash
$ npm update
```
  + Upgrade the packages of the project (as seen in the `package-lock.json`
    file)):
```bash
$ npm upgrade
```


