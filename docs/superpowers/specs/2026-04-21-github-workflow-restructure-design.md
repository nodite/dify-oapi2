# GitHub Workflow Restructure Design

**Date:** 2026-04-21  
**Status:** Approved  
**Goal:** Remove the `release` branch entirely. All release operations happen directly on `main` via manual `workflow_dispatch`.

---

## Background

The current workflow chain relies on a dedicated `release` branch:

1. Develop on `main` → merge to `release`
2. Manually trigger `bump-version.yml` (release branch only)
3. `release.yml` auto-triggers on `pyproject.toml` change → creates GitHub Release
4. `publish.yml` auto-triggers on GitHub Release → publishes to PyPI, then opens PR to sync back to `main`

This introduces unnecessary branch management overhead and a multi-hop trigger chain that is hard to trace when failures occur.

---

## Design

### File Changes

| File | Action |
|------|--------|
| `.github/workflows/bump-version.yml` | Delete |
| `.github/workflows/publish.yml` | Delete |
| `.github/workflows/release.yml` | Rewrite (all-in-one release) |
| `.github/workflows/test.yml` | Modify (remove `release` branch references) |
| `.github/workflows/publish-test.yml` | Modify (minor cleanup, remove `release` refs if any) |

---

### New `release.yml` — All-in-One Release Workflow

**Trigger:** `workflow_dispatch` on `main` branch only, with a required `version_type` input (`patch` / `minor` / `major`, default `patch`).

**Safety guard:** `if: github.ref == 'refs/heads/main'` — the job refuses to run on any other branch even if manually triggered there.

**Job steps (in order):**

1. `actions/checkout` — full history (`fetch-depth: 0`) with `PAT_TOKEN` for push permission
2. Setup Python 3.11 + install Poetry
3. `poetry install --with dev,format` — install all dependencies
4. **Run full checks:** `ruff check .` + `mypy .` + `pytest tests/ -v --tb=short`
   - Uses secrets: `DOMAIN`, `CHAT_KEY`, `COMPLETION_KEY`, `APP_KEY`, `WORKFLOW_KEY`
   - If any check fails, the job aborts here. No version bump or publish occurs.
5. `poetry version <version_type>` — bump version in `pyproject.toml`
6. Read new version: `poetry version -s` → export as step output
7. Commit and push: `git commit -m "chore: bump version to vX.Y.Z [skip ci]"` + `git push`
   - `[skip ci]` prevents `test.yml` and `publish-test.yml` from re-triggering on this commit
8. Create GitHub Release via `softprops/action-gh-release@v3`:
   - `tag_name: vX.Y.Z`
   - `name: Release vX.Y.Z`
   - `target_commitish: main`
   - `generate_release_notes: true`
9. `poetry build` — build sdist + wheel
10. `poetry publish` — publish to PyPI using `PYPI_TOKEN` secret

**Error semantics:** Steps are sequential with no intermediate checkpoints. A failure at step 4 (tests) leaves the repo unchanged. A failure at step 10 (publish) means the tag and release exist but PyPI upload failed — in this case re-running the workflow with the same version type would bump again, so the operator must manually publish via `make publish` or re-trigger carefully.

---

### Modified `test.yml`

Remove all references to the `release` branch:

```yaml
# Before
on:
  push:
    branches: [main, release]
  pull_request:
    branches: [main, release]

# After
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
```

No other changes to `test.yml`.

---

### `publish-test.yml` (kept, minor cleanup)

Behavior unchanged: auto-triggers on every push to `main` and supports manual `workflow_dispatch`. The `[skip ci]` tag on the version bump commit means this workflow does **not** re-run after a release. Normal development pushes to `main` continue to auto-publish to TestPyPI as before.

If there are any stale `release` branch references in this file, remove them.

---

## Failure Recovery

| Scenario | Recovery |
|----------|----------|
| Tests fail (step 4) | Fix code, push to main, re-trigger workflow |
| Version bump committed but release/publish failed | Manually run `make publish` locally, or push an empty commit to re-trigger |
| Accidental double-trigger (same version) | PyPI rejects duplicate versions; TestPyPI uses `--skip-existing`; safe to ignore |

---

## Secrets Required

No new secrets are needed. Existing secrets continue to work as-is:

- `PAT_TOKEN` (or fallback `GITHUB_TOKEN`) — for push permission and release creation
- `PYPI_TOKEN` — for PyPI publish
- `TESTPYPI_TOKEN` — for TestPyPI publish (publish-test.yml)
- `DOMAIN`, `CHAT_KEY`, `COMPLETION_KEY`, `APP_KEY`, `WORKFLOW_KEY` — for integration tests

---

## Out of Scope

- Migrating to OIDC trusted publishing (separate future improvement)
- Multi-Python-version test matrix (current: 3.11 only)
- Changelog automation beyond `generate_release_notes: true`
