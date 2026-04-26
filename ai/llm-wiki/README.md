# Knowledge Sharing (KS) - LLM Wiki

## Overview

[This cheat sheet](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/ai/llm-wiki/README.md)
is about the Andrey Karpathy's idea for AI agents and human beings
to capitalize knowkedge through a collection of wiki-typed pages, materialized as
MarkDown (md) files. Both AI agents and human beings benefit from that knowledge base,
which both of them contribute to as well.

The purpose is simple: manage markdown knowledge bases where AI agents and humans
work side by side.

From the day Andrey Karpathy published that idea, many initiatives have led to
implementations. This cheat sheet presents a few of them.

## References

### LLM Wiki

* Author: Andrej Karpathy
  ([Andrej Karpathy on LinkedIn](https://www.linkedin.com/in/andrej-karpathy-9a650716/),
  [Andrej Karpathy](https://github.com/karpathy))
* [GitHub Gist - LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
* Overview:

> **A pattern for building personal knowledge bases using LLMs**
> This is an idea file, it is designed to be copy pasted to your own LLM Agent (_e.g._
> OpenAI Codex, Claude Code, OpenCode / Pi, or etc.). Its goal is to communicate the
> high level idea, but your agent will build out the specifics in collaboration with you.

## Initiatives

### Tolaria

* [GitHub - Tolaria](https://github.com/refactoringhq/tolaria)
* Main contributor: Luca Rossi
  ([Luca Rossi on LinkedIn](https://www.linkedin.com/in/lucaronin/),
  [Luca Rossi on GitHub](https://github.com/LucaRonin))
* [LinkedIn post](https://www.linkedin.com/posts/eric-vyacheslav-156273169_karpathys-llm-wiki-idea-just-became-a-real-activity-7454061894610604032-XvI3/)
* Overview:

> Tolaria is a desktop app for Mac and Linux for managing markdown knowledge bases.
> People use it for a variety of use cases:
>
> * Operate second brains and personal knowledge
> * Organize company docs as context for AI
> * Store OpenClaw/assistants memory and procedures

* Principles:

> Principles
> * 📑 Files-first — Your notes are plain markdown files. They're portable, work with any editor,
> and require no export step. Your data belongs to you, not to any app.
> * 🔌 Git-first — Every vault is a git repository. You get full version history,
> the ability to use any git remote, and zero dependency on Tolaria servers.
> * 🛜 Offline-first, zero lock-in — No accounts, no subscriptions, no cloud dependencies.
> Your vault works completely offline and always will. If you stop using Tolaria, you lose nothing.
> * 🔬 Open source — Tolaria is free and open source. I built this for myself and for sharing it with others.
> * 📋 Standards-based — Notes are markdown files with YAML frontmatter. No proprietary formats,
> no locked-in data. Everything works with standard tools if you decide to move away from Tolaria.
> * 🔍 Types as lenses, not schemas — Types in Tolaria are navigation aids, not enforcement mechanisms.
> There's no required fields, no validation, just helpful categories for finding notes.
> * 🪄AI-first but not AI-only — A vault of files works very well with AI agents, but you are free
> to use whatever you want. We support Claude Code and Codex CLI (for now), but you can edit the vault
> with any AI you want. We provide an AGENTS file for your agents to figure out.
> * ⌨️ Keyboard-first — Tolaria is designed for power-users who want to use keyboard as much as possible.
> A lot of how we designed the Editor and the Command Palette is based on this.
> * 💪 Built from real use — Tolaria was created for manage my personal vault of 10,000+ notes,
> and I use it every day. Every feature exists because it solved a real problem.

### Wikibricks - Context and Memory for Agents on Databricks

* [GitHub - Wikibricks]()
* Main contributor: Dr. Philipp Tiefenbacher
  ([Dr. Philipp Tiefenbacher on LinkedIn](https://www.linkedin.com/in/philipptiefenbacher/),
  [Dr. Philipp Tiefenbacher on Medium](https://medium.com/@philipp.tiefenbacher_42173),
  [Dr. Philipp Tiefenbacher on GitHub](https://github.com/philtief/wikibricks))
* [LinkedIn post](https://www.linkedin.com/posts/philipptiefenbacher_github-philtiefwikibricks-a-wiki-for-activity-7453143479783702528-RXXg/)
* [Medium post - Context and Memory for Agents on Databricks](https://medium.com/@philipp.tiefenbacher_42173/context-and-memory-for-agents-on-databricks-f3c945cd8681)
* Date: Apr. 2026
* Overview:

> **A wiki for your AI agent, on Databricks**. Delta + Vector Search + Unity Catalog, exposed as native MCP tools.
> One databricks bundle deploy and your agent has a persistent, versioned, typed-link knowledge store
> that **grows from its own answer traces** via a nightly maintenance job.
>
> **Grounding ideas**
>
> Andrej Karpathy's [LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — instead
> of re-retrieving raw documents at every query, the agent incrementally compiles a structured,
> interlinked wiki it maintains itself. Knowledge compounds instead of getting re-derived.
> [Context and Memory for Agents on Databricks](https://medium.com/@philipp.tiefenbacher_42173/context-and-memory-for-agents-on-databricks-f3c945cd8681) — the
> reusable-memory-pattern argument:
> agent memory should be built from Databricks-native primitives (Delta, Unity Catalog,
> Vector Search, Model Serving, MCP) rather than a bespoke side-car,
> so every deployment inherits governance, lineage, and scale-to-zero for free.
> WikiBricks is the concrete intersection: Karpathy's compile-don't-retrieve pattern, implemented on the Databricks stack.


