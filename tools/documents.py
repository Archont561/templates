"""Render or verify the catalog's checked-in root documents."""

from jinja2 import Environment, FileSystemLoader, StrictUndefined
from tasknest import ToolContext, tool


@tool(description="Render root Markdown from gh-templates, or check for drift.")
def documents(ctx: ToolContext, check: bool = False) -> None:
    """Compare UTF-8 output byte-for-byte; check mode never writes files."""
    env = Environment(
        loader=FileSystemLoader(ctx.repo_root / "gh-templates"),
        undefined=StrictUndefined, keep_trailing_newline=True,
    )
    stale = []
    for name in ("README.md", "AGENTS.md"):
        template = name + ".j2"
        data = env.get_template(template).render(
            notice=f"<!-- Generated from gh-templates/{template}; edit the template instead. -->",
            render_command="pixi run --locked tools run documents",
        ).encode("utf-8")
        target = ctx.repo_root / name
        if not target.exists() or target.read_bytes() != data:
            stale.append(name)
            if not check:
                target.write_bytes(data)
    if check and stale:
        raise ValueError("Stale documents: " + ", ".join(stale) + "; run the documents task")
