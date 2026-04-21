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
| `.github/workflows/bump-version.yml` | **Delete** |
| `.github/workflows/publish.yml` | **Delete** |
| `.github/workflows/release.yml` | **Rewrite** (all-in-one release) |
| `.github/workflows/test.yml` | **Modify** (remove `release` branch references) |
| `.github/workflows/publish-test.yml` | **No change** (already has no `release` branch references) |

---

### New `release.yml` — All-in-One Release Workflow

**Trigger:** `workflow_dispatch` on `main` branch only, with a required `version_type` input (`patch` / `minor` / `major`, default `patch`).

**Concurrency guard:** Define `concurrency: group: release, cancel-in-progress: false` at the workflow level to prevent simultaneous release runs from racing. `cancel-in-progress: false` is required — an in-flight release must never be cancelled mid-step.

**Safety guard on the job:** `if: github.ref == 'refs/heads/main'` — the job refuses to run on any other branch even if manually triggered there.

**Job timeout:** `timeout-minutes: 30` — prevents a hung publish step from blocking the concurrency queue for hours.

**Job steps (in order):**

1. `actions/checkout@v4` — full history (`fetch-depth: 0`) with `PAT_TOKEN` for push permission  
   (`token: ${{ secrets.PAT_TOKEN }}` — no fallback to `GITHUB_TOKEN`; see branch protection note below)
2. `actions/setup-python@v5` with Python 3.11; `snok/install-poetry@v1` with `version: latest`, `virtualenvs-create: true`, `virtualenvs-in-project: true`
3. `poetry install --with dev,format`
4. **Run full checks:** `ruff check .` + `mypy .` + `pylint .` + `pytest tests/ -v --tb=short`  
   - Uses secrets: `DOMAIN`, `CHAT_KEY`, `COMPLETION_KEY`, `APP_KEY`, `WORKFLOW_KEY`  
   - If any check fails, the job aborts here. No version bump or publish occurs.
5. `poetry version ${{ inputs.version_type }}` — bump version in `pyproject.toml`
6. **Capture version** (`id: version`): `echo "version=$(poetry version -s)" >> $GITHUB_OUTPUT`  
   Referenced in later steps as `${{ steps.version.outputs.version }}`
7. **Pre-flight tag check:** run `git tag -l "v${{ steps.version.outputs.version }}"` and fail immediately if the tag already exists, before committing anything
8. **Commit and push** (`id: bump_commit`):
   ```
   git config user.name github-actions
   git config user.email github-actions@github.com
   git add pyproject.toml
   git commit -m "chore: bump version to v${{ steps.version.outputs.version }} [skip actions]"
   git push
   echo "sha=$(git rev-parse HEAD)" >> $GITHUB_OUTPUT
   ```
   `[skip actions]` (the officially documented GitHub keyword, superseding the legacy `[skip ci]`) suppresses re-triggering of `test.yml` and `publish-test.yml` on this push event. This is load-bearing when `PAT_TOKEN` is used — a `PAT_TOKEN`-initiated push does trigger downstream workflows, unlike `GITHUB_TOKEN`.
9. **Create GitHub Release** via `softprops/action-gh-release@v3`:
   - `with.token: ${{ secrets.PAT_TOKEN }}`
   - `tag_name: v${{ steps.version.outputs.version }}`
   - `name: Release v${{ steps.version.outputs.version }}`
   - `target_commitish: ${{ steps.bump_commit.outputs.sha }}` — pins the tag to the exact bump commit SHA, not the branch name, to avoid a race between this step and any concurrent push to `main`
   - `generate_release_notes: true`
10. `poetry build`
11. `poetry publish` using `POETRY_PYPI_TOKEN_PYPI: ${{ secrets.PYPI_TOKEN }}`

---

### Branch Protection Requirement

The new `release.yml` pushes directly to `main`. This requires:

- `PAT_TOKEN` must be set as a repository secret (not optional — no `|| GITHUB_TOKEN` fallback)
- The account owning `PAT_TOKEN` must have **Contents: write** permission and must be on `main`'s branch protection bypass list if "Require a pull request before merging" is enabled
- If branch protection cannot be bypassed, the workflow must be redesigned to open a PR instead of pushing directly — that is out of scope for this spec

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

### `publish-test.yml` (no changes required)

The file already targets `main` only and has no `release` branch references. Behavior is unchanged: auto-triggers on every push to `main` and supports manual `workflow_dispatch`. The `[skip actions]` tag on the version bump commit suppresses the `push`-triggered run (but not a manually dispatched run — that is correct behavior). Normal development pushes continue to auto-publish to TestPyPI.

---

## Failure Recovery

| Scenario | Recovery |
|----------|----------|
| Tests fail (step 4) | Fix code, push to main, re-trigger workflow |
| Bump committed but GitHub Release creation failed (step 9) | The tag does not exist yet. Use GitHub's "Re-run failed jobs" button to re-run from step 9 without re-bumping the version |
| Tag/Release created but PyPI publish failed (step 11) | Run `make publish` locally using the already-bumped version in `pyproject.toml`. Do NOT re-trigger the full workflow — it will bump the version again |
| Accidental double-trigger (concurrency guard queues second run) | Cancel the queued second run from the GitHub Actions UI before it starts |
| Pre-existing tag blocks step 7 | Delete the conflicting tag manually, then re-trigger |

---

## Secrets Required

| Secret | Required | Purpose |
|--------|----------|---------|
| `PAT_TOKEN` | **Required** (no fallback) | Push to `main`, create GitHub Release |
| `PYPI_TOKEN` | Required | PyPI publish |
| `TESTPYPI_TOKEN` | Required | TestPyPI publish (`publish-test.yml`) |
| `DOMAIN` | Optional | Integration tests |
| `CHAT_KEY` | Optional | Integration tests |
| `COMPLETION_KEY` | Optional | Integration tests |
| `APP_KEY` | Optional | Integration tests |
| `WORKFLOW_KEY` | Optional | Integration tests |

---

## Out of Scope

- Migrating to OIDC trusted publishing (separate future improvement)
- Multi-Python-version test matrix (current: 3.11 only)
- Changelog automation beyond `generate_release_notes: true`
- Split prepare/publish jobs for safer partial-failure recovery (future improvement)
