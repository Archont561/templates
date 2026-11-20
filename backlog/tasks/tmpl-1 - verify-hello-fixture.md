---
id: TMPL-1
title: Verify Hello against a live GitHub fixture
status: Done
assignee: []
created_date: '2026-11-20'
labels: [ci]
dependencies: []
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Exercise the publisher after the protected environment and its secret are configured.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 A manual main-branch run records the fixture commit, successful hello job, and expected greeting in the parent artifact.
- [x] #2 The fixture repository is removed after evidence collection.
<!-- AC:END -->

## Evidence

<!-- SECTION:EVIDENCE:BEGIN -->
Manual dispatch on `main` in the protected `tmpl` environment: run [44817345766](https://github.com/Archont561/templates/actions/runs/44817345766) (2026-11-20, success, 47s), artifact `hello-e2e-44817345766-1`.

- **AC #1** — `fixture.json` records fixture commit `cd918e70b0c3829b9a295b8f473513556d98f2b1` on `Archont561/tpl-e2e-hello-44817345766-1`; `run.json` shows the push-triggered Hello run at the same SHA with conclusion `success`; `jobs.json` shows the `hello` job succeeded; `hello.log` line 120 prints `hello world`.
- **AC #2** — `repos/Archont561/tpl-e2e-hello-44817345766-1` returns 404 after the run; the ID-checked cleanup removed the fixture (id 1465902970).
<!-- SECTION:EVIDENCE:END -->
