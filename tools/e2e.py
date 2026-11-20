"""Trusted CI harness. Never run code from the fixture in this token-bearing process."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import time

from loguru import logger
from tasknest import ToolContext, tool

GH = "gh"
GIT = "git"
CONFIG = "-c"
ID = "id"


def command(*args, cwd=None, env=None):
    """Run a bounded subprocess and capture its output."""
    return subprocess.check_output(args, cwd=cwd, env=env, text=True, timeout=90).strip()


def api(endpoint, *args):
    """Read a JSON response from the GitHub API."""
    return json.loads(command(GH, 'api', endpoint, *args))


def _hello_runs(repo, sha):
    runs = api(f'repos/{repo}/actions/runs?head_sha={sha}&event=push')['workflow_runs']
    return (run for run in runs
            if run['path'] == '.github/workflows/hello.yml' and run['head_branch'] == 'main')


def _collect_result(repo, run, report):
    jobs = api(f'repos/{repo}/actions/runs/{run[ID]}/jobs')['jobs']
    (report / 'jobs.json').write_text(json.dumps(jobs, indent=2))
    log = command(GH, 'run', 'view', str(run[ID]), '--repo', repo, '--log')
    (report / 'hello.log').write_text(log)
    hello_passed = any(j['name'] == 'hello' and j['conclusion'] == 'success' for j in jobs)
    if run['conclusion'] != 'success' or not hello_passed or 'hello world' not in log:
        raise RuntimeError('Fixture CI failed or the expected hello output was missing')


def observe(repo, sha, report):
    """Wait for the pushed workflow and collect its evidence."""
    deadline = time.monotonic() + 900
    while time.monotonic() < deadline:
        for run in _hello_runs(repo, sha):
            (report / 'run.json').write_text(json.dumps(run, indent=2))
            if run['status'] != 'completed':
                continue
            _collect_result(repo, run, report)
            return
        time.sleep(10)
    raise TimeoutError(f'No completed hello workflow for {repo}@{sha}')


def _render(root, tmp):
    src, dest = Path(tmp, 'src'), Path(tmp, 'hello')
    shutil.copytree(root / 'templates', src / 'templates')
    shutil.copy2(root / 'copier.yml', src)
    command('copier', 'copy', '--defaults', str(src), str(dest),
            env={k: v for k, v in os.environ.items() if k != 'GH_TOKEN'})
    return dest


def _commit(dest):
    command(GIT, 'init', '-b', 'main', cwd=dest)
    command(GIT, 'add', '.', cwd=dest)
    command(GIT, CONFIG, 'user.name=Fixture CI', CONFIG, 'user.email=fixture@example.invalid',
            'commit', '-m', 'Test generated hello starter', cwd=dest)
    return command(GIT, 'rev-parse', 'HEAD', cwd=dest)


def _create_fixture(owner, name):
    if api(f'users/{owner}')['type'] == 'Organization':
        create = f'orgs/{owner}/repos'
    else:
        if api('user')['login'].casefold() != owner.casefold():
            raise RuntimeError('Personal fixture owner must match the PAT owner')
        create = 'user/repos'
    return api(create, '-X', 'POST', '-f', f'name={name}', '-F', 'private=true')


def _delete_fixture(endpoint, fixture):
    if api(endpoint)[ID] != fixture[ID]:
        raise RuntimeError('Refusing cleanup: repository ID changed')
    command(GH, 'api', '-X', 'DELETE', endpoint)


def _progress(ctx, message):
    logger.opt(depth=1).info("[{}] {}", ctx.task_name, message)


def main(ctx: ToolContext):
    """Create, test, and remove a private hello fixture."""
    if not os.environ.get('GH_TOKEN'):
        raise SystemExit('Missing GH_TOKEN: configure tmpl environment secret TMPL_E2E_PAT')
    owner = os.environ['GITHUB_REPOSITORY_OWNER']
    name = f'tpl-e2e-hello-{int(os.environ["GITHUB_RUN_ID"])}-{int(os.environ["GITHUB_RUN_ATTEMPT"])}'
    repo = f'{owner}/{name}'
    endpoint = f'repos/{repo}'
    report = Path(os.environ['RUNNER_TEMP']) / 'hello-e2e-report'
    report.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        _progress(ctx, "Rendering hello starter")
        dest = _render(ctx.repo_root, tmp)
        sha = _commit(dest)
        _progress(ctx, f"Creating private fixture {repo}")
        fixture = _create_fixture(owner, name)
        try:
            (report / 'fixture.json').write_text(json.dumps({'repo': repo, 'id': fixture[ID], 'sha': sha}))
            if fixture['full_name'].casefold() != repo.casefold() or not fixture['private']:
                raise RuntimeError('Unexpected fixture identity or visibility')
            command(GIT, CONFIG, 'credential.helper=', CONFIG, 'credential.helper=!gh auth git-credential',
                    'push', f'https://github.com/{repo}.git', 'HEAD:refs/heads/main', cwd=dest)
            _progress(ctx, f"Waiting for hello.yml on {repo}@{sha}")
            observe(repo, sha, report)
            _progress(ctx, f"Hello CI passed; evidence in {report}")
        finally:
            _progress(ctx, f"Cleaning up {repo}")
            _delete_fixture(endpoint, fixture)


@tool(description="Run the live GitHub hello fixture test (CI only).")
def e2e(ctx: ToolContext) -> None:
    """Run the fixture test from the Tasknest workspace."""
    main(ctx)


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    main(ToolContext(repo_root=root, project_root=root, task_name="e2e"))
