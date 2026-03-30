---
id: T01
parent: S01
milestone: M003
provides:
  - Complete kotti_file package scaffold at /Users/disko/Projects/ipn/kotti_file/
  - Passing pytest smoke test (1 passed)
  - Passing ruff check + ruff format --check
  - git repo initialised on master branch with initial commit
  - uv.lock with 121 resolved packages
key_files:
  - /Users/disko/Projects/ipn/kotti_file/pyproject.toml
  - /Users/disko/Projects/ipn/kotti_file/src/kotti_file/__init__.py
  - /Users/disko/Projects/ipn/kotti_file/tests/test_smoke.py
  - /Users/disko/Projects/ipn/kotti_file/.github/workflows/ci.yml
  - /Users/disko/Projects/ipn/kotti_file/uv.lock
  - /Users/disko/Projects/ipn/kotti_file/.gitignore
key_decisions:
  - Added `tool.hatch.metadata.allow-direct-references = true` — hatchling 1.x rejects git URL deps without this flag
  - Pinned `setuptools<80` in test dependency group — setuptools 80+ dropped the standalone `pkg_resources` module from site-packages; pyramid 1.x still imports it at the top level
  - Removed unused `# noqa: ANN001` from includeme — ANN001 is not in the ruff rule set so RUF100 fires
patterns_established:
  - kotti add-on packages must pin `setuptools<80` in their test group due to pyramid 1.x pkg_resources usage
  - hatchling requires `tool.hatch.metadata.allow-direct-references = true` for any git-URL dependency
observability_surfaces:
  - pytest --cov=kotti_file reports per-file coverage on every test run
duration: ~8 min
verification_result: passed
completed_at: 2026-03-28
blocker_discovered: false
---

# T01: Write all scaffold files and verify locally

**Wrote all 13 scaffold files for kotti_file, resolved two environment issues (hatchling git-ref flag, setuptools pkg_resources regression), and confirmed pytest + ruff checks all pass on the local git master branch.**

## What Happened

Created `/Users/disko/Projects/ipn/kotti_file/` from scratch and wrote every required file mirroring Kotti's toolchain conventions. Two non-obvious issues surfaced during `uv run pytest`:

1. **Hatchling rejects git-URL dependencies by default.** Added `[tool.hatch.metadata] allow-direct-references = true` to pyproject.toml.

2. **setuptools 82 dropped `pkg_resources` as a standalone import.** The uv-managed Python 3.12 environment installed setuptools 82.0.1, but `pyramid/path.py` does `import pkg_resources` at module load. This is a known breakage in the Pyramid 1.x / modern setuptools combination. Fix: pin `setuptools<80` in the test dependency group, which downgrades to 79.0.1 where `pkg_resources` is still present as a top-level module.

3. **Unused `# noqa: ANN001` in `__init__.py`.** `ANN001` is not in the ruff `select` list, so ruff's `RUF100` rule fires on the directive. Removed it.

After those fixes, `uv sync --group test && uv run pytest` passes cleanly (1 collected, 1 passed, 75% coverage), and both `ruff check` and `ruff format --check` report no issues.

Initialised the git repo with `git init -b master`, committed all files, then added a `.gitignore` and stripped the inadvertently tracked `.coverage` and `__pycache__` files in a second commit. Final state: 3 commits on master.

## Verification

```
cd /Users/disko/Projects/ipn/kotti_file
uv run pytest          # 1 passed
uv run ruff check .    # All checks passed!
uv run ruff format --check .   # 3 files already formatted
git log --oneline -1   # 683923b chore: untrack pycache and coverage artefacts
```

## Verification Evidence

| # | Command | Exit Code | Verdict | Duration |
|---|---------|-----------|---------|----------|
| 1 | `cd kotti_file && uv run pytest` | 0 | ✅ pass | ~2.8 s |
| 2 | `uv run ruff check .` | 0 | ✅ pass | ~2.8 s |
| 3 | `uv run ruff format --check .` | 0 | ✅ pass | <1 s |
| 4 | `git log --oneline -1` | 0 | ✅ pass | <1 s |

## Diagnostics

- `uv run pytest` with `--cov=kotti_file` prints a coverage table after each run — useful baseline signal as real code is added.
- `uv run ruff check . --fix` auto-fixes most lint issues if they appear.

## Deviations

- Added `[tool.hatch.metadata] allow-direct-references = true` — not in the original plan but required by hatchling for git-URL deps.
- Added `setuptools<80` to the test dependency group — not in the original plan; required because pyramid 1.x uses `import pkg_resources` which modern setuptools dropped.
- Added `.gitignore` — not listed in expected outputs but necessary to avoid committing `__pycache__` and `.coverage` artefacts.

## Known Issues

None.

## Files Created/Modified

- `pyproject.toml` — package metadata, hatchling build config, pytest/ruff settings, dependency groups
- `src/kotti_file/__init__.py` — package init with `includeme` Pyramid hook
- `src/kotti_file/py.typed` — PEP 561 marker
- `tests/conftest.py` — empty conftest, establishes tests/ as test root
- `tests/test_smoke.py` — smoke test asserting `includeme` is callable
- `.github/workflows/ci.yml` — sqlite-only matrix (3.10–3.13) + lint job
- `.pre-commit-config.yaml` — ruff-pre-commit v0.15.4, pre-commit-hooks v6.0.0
- `uv.lock` — 121-package lockfile
- `mkdocs.yml` — MkDocs Material site config
- `docs/index.md` — minimal docs index
- `README.md` — project readme
- `LICENSE.txt` — RPL / BSD-derived (same as Kotti)
- `CHANGES.txt` — initial changelog stub
- `.gitignore` — excludes pycache, .coverage, .venv, dist
