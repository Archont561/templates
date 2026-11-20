# Template catalog backlog

Maintainer work lives here, outside the Copier payload. Tasks and status changes travel in the same PRs as the work. The public handbook lives in `docs/`, not here.

From the repository root, with the Backlog.md CLI installed:

```sh
backlog task list
backlog board
backlog task create "Describe the next outcome"
```

No CLI is required to read the Markdown tasks. Use `TMPL` IDs, keep acceptance criteria observable, and move tasks through **To Do → In Progress → Done**. Remote operations and automatic commits are disabled in `config.yml`.

## Architecture decisions

Tasks track unfinished work; decisions record why the repository works this way.

- [Decision 1: Separate starter payloads from the catalog](decisions/decision-1-copier-payload-boundary.md)
- [Decision 2: Verify downstream CI in an ephemeral repository](decisions/decision-2-live-fixture-ci.md)
- [Decision 3: Render repository documents from gh-templates](decisions/decision-3-generated-root-documents.md)

For new decisions, use the next `decision-N` ID and record the context, decision, consequences, and status. If a decision changes, add a successor and link it from the superseded record.
