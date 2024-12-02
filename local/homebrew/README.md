HomeBrew
========

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

