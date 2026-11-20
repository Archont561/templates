"""Lint the catalog's Python automation."""

from tasknest import ToolContext, tool


CHECK = "check"
DOCS = ("README.md", "AGENTS.md", "backlog", "docs/content/docs")


@tool(description="Check Python, repository structure, and documentation.")
def lint(ctx: ToolContext) -> None:
    """Run the offline checks used by template CI."""
    ctx.run(["rude", CHECK, "--max-line-length", "110", "tools"], cwd=ctx.repo_root)
    ctx.run(["alint", CHECK], cwd=ctx.repo_root)
    ctx.run(["rumdl", CHECK, *DOCS], cwd=ctx.repo_root)
    ctx.run(["vale", *DOCS], cwd=ctx.repo_root)
