<!-- Generated from gh-templates/AGENTS.md.j2; edit the template instead. -->

# Working on the templates catalog

- `templates/` contains downstream payloads. `gh-templates/` contains the catalog’s own document sources. Keep maintainer credentials, automation, and backlog items out of generated starters.
- Edit the `.md.j2` sources, not the generated root documents. Run `pixi run --locked tools run documents` after edits.
- Use the locked Pixi environment. Before submitting changes, run `pixi run --locked tools run lint` and `pixi run --locked tools run smoke`.
- For handbook changes, build from the repository root with `pixi run --locked docs-install` and `NEXT_PUBLIC_BASE_PATH=/templates pixi run --locked docs-build`.
- Use the protected `tmpl` environment for real GitHub fixture tests. Never print its PAT or pass it to the generated project.
- See [the backlog](backlog/README.md) for task conventions and acceptance criteria.
