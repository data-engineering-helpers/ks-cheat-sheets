Cheat Sheet - Python
====================

# Table of Content (ToC)
* [Overview](#overview)
  * [Data Engineering helpers](#data-engineering-helpers)
  * [Machine Learning helpers](#machine-learning-helpers)
  * [Python](#python)
    * [PyEnv](#pyenv)
  * [uv](#uv)
  * [Ruff](#ruff)
  * [Poetry](#poetry)
* [Getting started](#getting-started)
  * [Specify a specific Python version](#specify-a-specific-python-version)
  * [Execute somme Python commands](#execute-somme-python-commands)
  * [Install a new Python version](#install-a-new-python-version)
  * [Remove a specific Python version](#remove-a-specific-python-version)
  * [uv \- Getting started](#uv---getting-started)
    * [uv \- Projects](#uv---projects)
    * [uv \- Scripts](#uv---scripts)
    * [uv \- Tools](#uv---tools)
    * [uv \- Python versions](#uv---python-versions)
    * [uv \- pip interface](#uv---pip-interface)
  * [Ruff \- Getting started](#ruff---getting-started)
* [Installation](#installation)
  * [PyEnv \- Installation](#pyenv---installation)
    * [PyEnv on Linux](#pyenv-on-linux)
    * [PyEnv on MacOS](#pyenv-on-macos)
    * [PyEnv on MS Windows](#pyenv-on-ms-windows)
  * [PyEnv configuration](#pyenv-configuration)
    * [PyEnv Bash configuration](#pyenv-bash-configuration)
  * [uv \- Installation](#uv---installation)
    * [uv \- MacOS](#uv---macos)
    * [uv \- Linux](#uv---linux)
    * [uv \- MS Windows](#uv---ms-windows)
  * [Ruff \- Installation](#ruff---installation)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
* [This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/python/README.md)
  explains how to install and to use Python, and associated tools and utilities.
  Python is a cornerstone of the so-called Modern Data Stack (MDS) in a box.
  Python powers other data-related tools, such as PySpark, Jupyter Lab,
  DuckDB, SQLMesh/SQLGlot, Polars, Daft, FastAPI/Flask.

* There are several ways to install and use Python and the ecosystem built
  upon Python.
  * [PyEnv](https://github.com/pyenv/pyenv) has been available
  for a while and is now mature enough to be widely used by the majority of
  users. PyEnv is the solution be default used in
  [these cheat sheets](https://github.com/data-engineering-helpers/ks-cheat-sheets)
  * [uv](https://github.com/astral-sh/uv) is the new, shiny, kid on the block,
  and may appeal to those seeking to be on the edge of technological trends.
  There is at least a very specific use case where uv proves useful, it is
  to power standalone Python scripts: it is enough to add the magic
  `#!/usr/bin/env -S uv` command as the first line of any Python script,
  and that latter becomes standalone, self-served on any platform, any where,
  whithout requiring the users to install anything like dependencies (apart
  uv itself, obviously)

## Data Engineering helpers
* [Data Engineering Helpers - Knowledge Sharing - Jupyter, PySpark and DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/programming/jupyter/jupyter-pyspark-duckdb/)
* [Data Engineering Helpers - Knowledge Sharing - Spark](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/spark/)
* [Data Engineering Helpers - Knowledge Sharing - SQLMesh](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/data-processing/sqlmesh/)
* [Data Engineering Helpers - Knowledge Sharing - DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/)
* [Material for the Data platform - Modern Data Stack (MDS) in a box](https://github.com/data-engineering-helpers/mds-in-a-box)

## Machine Learning helpers
* (old, but somewhat still relevant)
  [Machine Learning Helpers - Knowledge Sharing - Python virtual environments](https://github.com/machine-learning-helpers/induction-python/tree/master/installation/virtual-env)

## Python
* Home page: https://python.org

### PyEnv
* GitHub repository: https://github.com/pyenv/pyenv

## uv
* GitHub repository: https://github.com/astral-sh/uv
* Documentation: https://docs.astral.sh/uv/guides/projects/
* Publishing guide: https://docs.astral.sh/uv/guides/publish/
* Motto: A single tool to replace `pip`, `pip-tools`, `pipx`, `poetry`,
  `pyenv`, `twine`, `virtualenv`, and more

## Ruff
* GitHub project: https://github.com/astral-sh/ruff
* Documentation page: https://docs.astral.sh/ruff
* Motto: an extremely fast Python linter and code formatter, written in Rust

## Poetry

# Getting started

## Specify a specific Python version
* Specify a version of Python, either globally or locally for the current
  project at hand
  * Globally:
```bash
pyenv global 3.11.11
```
  * Locally, for the current project at hand:
```bash
pyenv local 3.11.11
```

* Check the current version
  * With PyEnv:
```bash
pyenv versions
  system
* 3.11.11 (set by ~/.pyenv/version)
  3.13.2
```
  * With Python directly:
```bash
python -V
3.11.11
```

## Execute somme Python commands
* To execute some simple commands, inline, pass the Python code after the
  `-c` (command) parameter of the `python` utility:
```bash
python -c "import sys; print(sys.version)"
3.11.11 (main, Dec  6 2024, 12:21:43) [Clang 16.0.0 (clang-1600.0.26.4)]
```

## Install a new Python version
* Retrieve the latest list of Python versions, filtering for some specific
  minor version, say `3.11`:
```bash
pyenv install --list|grep "3\.11\." | grep -v "conda" | grep -v "forge"
  3.11.0
  ...
  3.11.11
```

* Install a specific version of Python, say `3.11.11`:
```bash
pyenv install 3.11.11
```

## Remove a specific Python version
* To uninstall a specific version of Python, say the `3.11.10`,
  just execute the `uninstall` command:
```bash
pyenv uninstall 3.11.10
```

## uv - Getting started
* uv manages project dependencies and environments, with support for lockfiles,
  workspaces, and more, similar to `rye` or `poetry`

### uv - Projects
* Reference: https://github.com/astral-sh/uv?tab=readme-ov-file#projects

* Create a sample project, say `example`, and move into it:
```bash
$ uv init example
Initialized project `example` at `$PWD/example`
$ pushd example
```

* Add Ruff to the project dependencies:
```bash
$ uv add ruff
Creating virtual environment at: .venv
Resolved 2 packages in 170ms
   Built example @ file://$PWD/example
Prepared 2 packages in 627ms
Installed 2 packages in 1ms
 + example==0.1.0 (from file://$PWD/example)
 + ruff==0.5.0
```

* Audit the code with Ruff:
```bash
$ uv run ruff check
All checks passed!
```

* Update the `uv.lock` file (ignored by Git, here):
```bash
$ uv lock
Resolved 2 packages in 0.33ms
```

* Synchronize the dependencies:
```bash
$ uv sync
Resolved 2 packages in 0.70ms
Audited 1 package in 0.02ms
```

* Leave the project directory:
```bash
popd
```

### uv - Scripts
* Reference: https://github.com/astral-sh/uv?tab=readme-ov-file#scripts

uv manages dependencies and environments for single-file scripts.

* Create a new script:
```bash
$ echo 'import requests; print(requests.get("https://astral.sh"))' > example.py
```

* Add inline metadata declaring its dependencies:
```bash
$ uv add --script example.py requests
Updated `example.py`
```

* Then, run the script in an isolated virtual environment:
```bash
$ uv run example.py
Reading inline script metadata from: example.py
Installed 5 packages in 12ms
<Response [200]>
```

* See the [uv scripts documentation](https://docs.astral.sh/uv/guides/scripts/)
to get started.

### uv - Tools
* Reference: https://github.com/astral-sh/uv?tab=readme-ov-file#tools

### uv - Python versions
* Reference: https://github.com/astral-sh/uv?tab=readme-ov-file#python-versions

### uv - pip interface
* Reference: https://github.com/astral-sh/uv?tab=readme-ov-file#the-pip-interface


## Ruff - Getting started
* This section partially reproduces, for convenience, the
  [tutorial section of the Ruff documentation](https://docs.astral.sh/ruff/tutorial/).
  See the [Ruff documentation](https://docs.astral.sh/ruff/) for more details
  or advanced use cases

* Initialize a Python module/library project, say `numbers`:
```bash
uv init --lib numbers
```

* This command creates a Python project with the following structure:
```txt
numbers
  ├── README.md
  ├── pyproject.toml
  └── src
      └── numbers
          ├── __init__.py
          └── py.typed
```

* We will then replace the contents of `src/numbers/__init__.py` with the
  following code:
```python
from typing import Iterable

import os

def sum_even_numbers(numbers: Iterable[int]) -> int:
    """Given an iterable of integers, return the sum of all even numbers in the iterable."""
    return sum(
        num for num in numbers
        if num % 2 == 0
    )
```

* Next, we'll add Ruff to our project:
```bash
uv add --dev ruff
Using CPython 3.13.1
Creating virtual environment at: .venv
Resolved 2 packages in 445ms
      Built numbers @ file://$HOME/dev/ks-cheat-sheets/programming/python/numbers
Prepared 2 packages in 7.66s
Installed 2 packages in 7ms
 + numbers==0.1.0 (from file://$HOME/dev/ks-cheat-sheets/programming/python/numbers)
 + ruff==0.9.6
```

* We can then run the Ruff linter over our project via uv run ruff check:
```bash
uv run ruff check
```

!**Note**: As an alternative to `uv run`, you can also run Ruff by activating
the project's virtual environment (`source .venv/bin/active` on Linux and
macOS, or `.venv\Scripts\activate` on MS Windows) and running ruff check
directly.

* Ruff identified an unused import, which is a common error in Python code.
  Ruff considers this a "fixable" error, so we can resolve the issue
  automatically by running `ruff check --fix`:
```bash
uv run ruff check --fix
```

* Running git diff shows the following:
```diff
--- a/src/numbers/__init__.py
+++ b/src/numbers/__init__.py
@@ -1,7 +1,5 @@
 from typing import Iterable

-import os
-

def sum_even_numbers(numbers: Iterable[int]) -> int:
    """Given an iterable of integers, return the sum of all even numbers in the iterable."""
    return sum(
        num for num in numbers
        if num % 2 == 0
    )
```

* Note Ruff runs in the current directory by default, but you can pass specific
  paths to check:
```bash
uv run ruff check src/numbers/__init__.py
```

* Now that our project is passing ruff check, we can run the Ruff formatter
  via ruff format:
```bash
uv run ruff format
```

* Running `git diff` shows that the sum call was reformatted to fit within
  the default 88-character line length limit:
```diff
--- a/numbers.py
+++ b/numbers.py
@@ -3,7 +3,4 @@ from typing import Iterable

 def sum_even_numbers(numbers: Iterable[int]) -> int:
     """Given an iterable of integers, return the sum of all even numbers in the iterable."""
-    return sum(
-        num for num in numbers
-        if num % 2 == 0
-    )
+    return sum(num for num in numbers if num % 2 == 0)
```

* Thus far, we have been using Ruff's default configuration. Let us take
  a look at how we can customize Ruff's behavior:
  https://docs.astral.sh/ruff/tutorial/#configuration

# Installation

## PyEnv - Installation
* This section partially reproduces, for convenience, the content of the
  [PyEnv GitHub project](https://github.com/pyenv/pyenv). For more details
  and advance usage, directly visit it

### PyEnv on Linux
The Homebrew option from the [MacOS section below](#pyenv-on-macos)
would also work if you have Homebrew installed.

1. Automatic installer (Recommended):
```bash
curl -fsSL https://pyenv.run | bash
```

* For more details visit our other project:
  https://github.com/pyenv/pyenv-installer

2. Basic GitHub Checkout
This will get you going with the latest version of Pyenv and make it easy
to fork and contribute any changes back upstream.

* Check out Pyenv where you want it installed. A good place to choose is
`$HOME/.pyenv` (but you can install it somewhere else):
```bash
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

* Optionally, try to compile a dynamic Bash extension to speed up Pyenv.
  Don't worry if it fails; Pyenv will still work normally:
```bash
cd ~/.pyenv && src/configure && make -C src
```

### PyEnv on MacOS
The options from the
[Linux section above](#pyenv-on-linux) also work but Homebrew is recommended
for basic usage.

[Homebrew](https://brew.sh/) in macOS
1. Update homebrew and install pyenv:
```bash
brew update
brew install pyenv
```

* If you want to install (and update to) the latest development head of Pyenv rather than the latest release, instead run:
```bash
brew install pyenv --head
```

2. Then follow the rest of the post-installation steps, starting with
  [Set up your shell environment for Pyenv](#pyenv-configuration)

3. OPTIONAL. To fix `brew doctor`'s warning
  `""config" scripts exist outside your system or Homebrew directories"`

* If you are going to build Homebrew formulae from source that link against
  Python like Tkinter or NumPy (This is only generally the case if you are
  a developer of such a formula, or if you have an EOL version of MacOS
  for which prebuilt bottles are no longer provided and you are using
  such a formula).

* To avoid them accidentally linking against a Pyenv-provided Python,
  add the following line into your interactive shell's configuration:

  * Bash/Zsh:
```bash
alias brew='env PATH="${PATH//$(pyenv root)\/shims:/}" brew'
```
  * Fish:
```bash
alias brew="env PATH=(string replace (pyenv root)/shims '' \"\$PATH\") brew"
```

### PyEnv on MS Windows
Pyenv does not officially support MS Windows and does not work in Windows
outside the Windows Subsystem for Linux (WSL). Moreover, even there,
the Pythons it installs are not native Windows versions but rather Linux
versions running in a virtual machine -- so you will not get Windows-specific
functionality.

If you are in Windows, we recommend using
[@kirankotari's](https://github.com/kirankotari)
[pyenv-win](https://github.com/pyenv-win/pyenv-win) fork -- which does install
native Windows Python versions.

## PyEnv configuration

### PyEnv Bash configuration
* The below setup should work for the vast majority of users for common
  use cases. For details and more configuration options, visit directly the
  [PyEnv GitHub project](https://github.com/pyenv/pyenv) and, in particular,
  [Advanced configuration](https://github.com/pyenv/pyenv#advanced-configuration)
  for details and more configuration options.

* Stock Bash startup files vary widely between distributions in which of them
  source which, under what circumstances, in what order and what additional
  configuration they perform. As such, the most reliable way to get Pyenv
  in all environments is to append Pyenv configuration commands to both
  `.bashrc` (for interactive shells) and the profile file that Bash would use
  (for login shells).

1. First, add the commands to `~/.bashrc` by running the following in your
  terminal:
```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init - bash)"' >> ~/.bashrc
```

2. Then, if you have `~/.profile`, `~/.bash_profile` or `~/.bash_login`,
  add the commands there as well. If you have none of these, create a
  `~/.profile` and add the commands there.

  * To add to `~/.profile`:
```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
echo 'eval "$(pyenv init - bash)"' >> ~/.profile
```
  * To add to `~/.bash_profile`:
```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init - bash)"' >> ~/.bash_profile
```

**Bash warning**: There are some systems where the `BASH_ENV` variable is
configured to point to `.bashrc`. On such systems, you should almost certainly
put the `eval "$(pyenv init - bash)"` line into `.bash_profile`, and not into
`.bashrc`. Otherwise, you may observe strange behaviour, such as pyenv getting
into an infinite loop. See
[PyEnv issue #264](https://github.com/pyenv/pyenv/issues/264) for details.

## uv - Installation
* This section partially reproduces, for convenience, the content of the
  [uv installation documentation](https://github.com/astral-sh/uv).
  For more details and advance usage, directly visit it

### uv - MacOS
* Install uv on MacOS with Homebrew:
```bash
brew install uv
```

### uv - Linux
* Install uv on Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### uv - MS Windows
* Install uv on MS Windows:
```bash
# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Ruff - Installation
* This section partially reproduces, for convenience, the content of the
  [Ruff installation documentation](https://docs.astral.sh/ruff/installation/).
  For more details and advance usage, directly visit it

