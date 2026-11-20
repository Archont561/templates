---
id: decision-3
title: Render repository documents from gh-templates
date: 2026-11-20
status: accepted
---

# Render repository documents from gh-templates

## Context

GitHub and agents read Markdown at the repository root; maintainers also need one canonical editable source for each document.

## Decision

Render `README.md` and `AGENTS.md` from `gh-templates/` using the Tasknest documents task. CI checks the rendered files without rewriting them.

## Consequences

Edit the Jinja sources and commit both source and output. The generated Hello project keeps its own independent README.
