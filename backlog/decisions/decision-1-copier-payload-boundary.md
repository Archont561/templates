---
id: decision-1
title: Separate starter payloads from the catalog
date: 2026-11-20
status: accepted
---

# Separate starter payloads from the catalog

## Context

The catalog needs maintainer tools, a handbook, and release workflows that don't belong in a generated project.

## Decision

Keep one root `copier.yml`. Select the downstream payload with `_subdirectory`; today that’s `templates/hello`. Keep the catalog’s `tools/`, `docs/`, and `backlog/` outside it.

## Consequences

Cloning and rendering are different operations. A second starter needs explicit selection and render coverage; adding a directory alone doesn't publish it.
