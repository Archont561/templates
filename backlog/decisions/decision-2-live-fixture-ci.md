---
id: decision-2
title: Verify downstream CI in an ephemeral repository
date: 2026-11-20
status: accepted
---

# Verify downstream CI in an ephemeral repository

## Context

A local render can verify files and output, but can't establish that GitHub triggers the shipped workflow on a push to `main`.

## Decision

Run the fast checks on PRs. Run the protected live fixture weekly or by manual dispatch: push the generated starter, wait for its exact SHA, collect evidence, then attempt ID-checked cleanup.

## Consequences

The harness needs a privileged credential and a cleanup procedure for interrupted runs. The credential stays in the publisher. This decision defines the test, not evidence that a live run has passed.
