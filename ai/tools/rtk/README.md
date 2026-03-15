# Rust Token Killer (RTK)

## Table of Content (ToC)

* [Rust Token Killer (RTK)](#rust-token-killer-rtk)
  * [Table of Content (ToC)](#table-of-content-toc)
  * [Overview](#overview)
  * [Refefences](#refefences)
    * [Articles](#articles)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

## Overview

* Your AI agent is drowning in CLI noise. Fix it.
* rtk compresses command outputs before they reach the context window.
* Better reasoning. Longer sessions. Lower costs.

## Refefences

* [RTK home page](https://www.rtk-ai.app/)
* [GitHub - RTK](https://github.com/rtk-ai/rtk)

### Articles

* [Post on LinkedIn](https://www.linkedin.com/posts/philipshurpik_claudecode-agenticcoding-devtools-share-7438005788448620544-qx9i/)
* Setup takes 30 seconds:
  * Install RTK on MacOS: `brew install rtk`
  * Initialize RTK: `rtk init -g --hook-only`
* One tip: skip the RTK.md file during init (use `--hook-only`).
  It adds ~400 tokens to every Claude.md read, which defeats the purpose.
  Run `rtk gain` anytime to see your savings.
