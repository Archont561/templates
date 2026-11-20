<!-- Generated from gh-templates/README.md.j2; edit the template instead. -->

# Archont561 / Templates

**A curated collection of project scaffolds maintained by [Archont561](https://github.com/Archont561).** Generate a project with Copier and take only the starter files you need. The catalog’s own tooling stays here.

[![Open the handbook](https://img.shields.io/badge/Handbook-Template_Fieldnotes-226c55)](https://archont561.github.io/templates/)
[![Browse starters](https://img.shields.io/badge/Catalog-Browse_starters-175c75)](https://archont561.github.io/templates/guide/)
[![Generator: Copier](https://img.shields.io/badge/Generator-Copier-594582)](https://copier.readthedocs.io/)
[![Maintainer: Archont561](https://img.shields.io/badge/Maintainer-Archont561-30363d?logo=github)](https://github.com/Archont561)

[![Template CI](https://github.com/Archont561/templates/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Archont561/templates/actions/workflows/ci.yml)
[![Hello fixture E2E](https://github.com/Archont561/templates/actions/workflows/e2e.yml/badge.svg?branch=main)](https://github.com/Archont561/templates/actions/workflows/e2e.yml)
[![Handbook deployment](https://github.com/Archont561/templates/actions/workflows/pages.yml/badge.svg?branch=main)](https://github.com/Archont561/templates/actions/workflows/pages.yml)

## Start with Hello

[**Hello**](https://archont561.github.io/templates/guide/hello/) is a minimal Python starter: one script, a README, and a GitHub Actions workflow that runs the script on pushes to `main`. With Copier and Git installed:

```bash
copier copy --vcs-ref main --defaults https://github.com/Archont561/templates.git my-hello
cd my-hello
python tools/hello.py
```

Expected output: `hello world`.

**[Browse the handbook](https://archont561.github.io/templates/)** · [How quality is checked](https://archont561.github.io/templates/guide/quality/) · [How to add a starter](https://archont561.github.io/templates/guide/authoring/)
