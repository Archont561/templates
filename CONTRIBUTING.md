# Contributing to the templates catalog

Thanks for helping improve the catalog. This guide covers the workflow for
changing starters, tooling, and the handbook.

## Ground rules

- `templates/` holds downstream payloads. `gh-templates/` holds the catalog’s
  own document sources. Keep maintainer credentials, automation, and backlog
  items out of generated starters.
- Edit the `.md.j2` sources, not the generated root documents. Run
  `pixi run --locked tools run documents` after edits.
- Never commit secrets. Fixture credentials live in the protected `tmpl`
  environment only.

## Set up the toolchain

Install [Pixi](https://pixi.sh/), then from the repository root:

```sh
pixi install --locked
```

The locked environment provides Python, Copier, Vale, rumdl, alint, and Bun.

## Before you open a pull request

```sh
pixi run --locked tools run lint
pixi run --locked tools run smoke
```

Lint covers Python, GitHub Actions, and prose. Smoke renders the Hello
starter and runs its entrypoint. CI runs both on every pull request.

## Work on the handbook

```sh
pixi run --locked docs-install
NEXT_PUBLIC_BASE_PATH=/templates pixi run --locked docs-build
```

The handbook source lives in `docs/`. Deployments publish from `main` only.

## Track work in the backlog

- Use `TMPL` IDs and keep acceptance criteria observable.
- Move tasks through **To Do → In Progress → Done**.
- Tasks and status changes travel in the same pull requests as the work.

## Commits and pull requests

- Use [Conventional Commits](https://www.conventionalcommits.org/), for
  example `feat: add a starter` or `docs: clarify the handbook`.
- The repository rebases pull requests onto `main`; merge commits aren’t
  allowed, so keep the branch history clean.
- Keep pull requests small and scoped so review stays quick.

## License

By contributing, you agree that your contributions are licensed under the
[MIT license](LICENSE).
