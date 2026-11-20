"""Render the starter and run the same entrypoint as downstream CI."""

import shutil
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

from copier import run_copy
from tasknest import ToolContext, tool


@tool(description="Render the working tree and check the generated hello project.")
def smoke(ctx: ToolContext) -> None:
    """Render a fresh project and verify its greeting."""
    with TemporaryDirectory() as tmp:
        # Stage only authoring inputs: exercise uncommitted edits, not the last tag.
        source = Path(tmp, "source")
        shutil.copytree(ctx.repo_root / "templates", source / "templates")
        shutil.copy2(ctx.repo_root / "copier.yml", source)
        dest = Path(tmp, "generated")
        run_copy(str(source), dest, data={"project_name": "Smoke Test"}, defaults=True)
        workflows = list((dest / ".github/workflows").iterdir())
        if [p.name for p in workflows] != ["hello.yml"]:
            raise ValueError(f"Unexpected workflows: {workflows}")
        if not (dest / "README.md").read_text().startswith("# Smoke Test\n"):
            raise ValueError("Copier did not render the project name")
        output = subprocess.check_output([sys.executable, "tools/hello.py"], cwd=dest, text=True)
        if output != "hello world\n":
            raise ValueError(f"Unexpected greeting: {output!r}")
        print(output, end="")
