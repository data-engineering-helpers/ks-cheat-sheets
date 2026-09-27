# chezmoi

## Overview

chezmoi manages one's personal configuration files (dotfiles, like ~/.gitconfig)
across multiple machines, securely.

chezmoi provides many features beyond symlinking or using a bare Git repo including:
* templates (to handle small differences between machines)
* password manager support (to store your secrets securely)
* importing files from archives (great for shell and editor plugins)
* full file encryption (using age, gpg, git-crypt, or transcrypt)
* running scripts (to handle everything else)

### References

* [dotfiles - Home page](https://dotfiles.github.io/)
* [chezmoi docs - Quick start](https://www.chezmoi.io/quick-start/)
* [chezmoi docs - User guide](https://www.chezmoi.io/user-guide/setup/)
* [GitHub - chezmoi repository](https://github.com/twpayne/chezmoi)

## Quick start

* Updating one's dotfiles on any machine is a single command:

```bash
chezmoi update
```

* Copy/migrate a configuration file into chezmoi-managed dotfiles repository
  (this copies `~/.bashrc` to `~/.local/share/chezmoi/dot_bashrc`):

```bash
chezmoi add ~/.bashrc
```

* Edit the chezmoi-managed configuration file

  * With chezmoi wrapper (this opens `~/.local/share/chezmoi/dot_bashrc`
  with `$EDITOR`):

```bash
chezmoi edit ~/.bashrc
```

* With any text editor:

```bash
vi ~/.local/share/chezmoi/dot_bashrc
```

* See what changes chezmoi would make:

```bash
chezmoi diff
# alternative
pushd ~/.local/share/chezmoi/ ; git diff ; popd
```

* Apply the changes:

```bash
chezmoi -v apply
```

* All chezmoi commands accept the `-v` (verbose) flag to print out exactly
  what changes they will make to the file system, and the `-n` (dry run) flag
  to not make any actual changes. The combination `-n -v` is very useful
  if you want to see exactly what changes would be made

* Merge local changes into a chezmoi-managed configuration file:

```bash
chezmoi merge ~/.bashrc
```

* Commit the changes:

```
chezmoi cd
git add .
git commit -m "Updated .bashrc"
```

## Setup

* [chezmoi docs - Install](https://www.chezmoi.io/install/)

* As chezmoi is based on Go, the chezmoi binary is standalone (_e.g._,
  does not need shared libraries), and can easily be installed on any platform
  simply by downloading the Go binary and placing it in a directory included
  in `PATH`

* Universal installation (that downloads the `chezmoi` binary and stores it in `~/bin/`;
  be sure to have `$HOME/bin` in `PATH`):

```bash
sh -c "$(curl -fsLS https://get.chezmoi.io)"
```

* Clone a private `dotfiles` Git repository (it also works with public ones,
  but that form is more general), the Git clone being stored in
  `~/.local/share/chezmoi/`:

```bash
chezmoi init git@github.com:$GITHUB_USERNAME/dotfiles.git
```
