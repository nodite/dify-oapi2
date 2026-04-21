# GitHub Workflow Restructure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Remove the `release` branch and all its associated workflow files; replace the multi-hop chain with a single all-in-one `release.yml` triggered manually from `main`.

**Architecture:** Two obsolete workflow files are deleted. One workflow file (`test.yml`) gets a two-line branch filter edit. One workflow file (`release.yml`) is completely rewritten as a self-contained `workflow_dispatch` pipeline that bumps the version, commits, creates a GitHub Release, and publishes to PyPI in a single job.

**Tech Stack:** GitHub Actions, `softprops/action-gh-release@v3`, `snok/install-poetry@v1`, Poetry, ruff, mypy, pylint, pytest

---

## File Map

| File | Change |
|------|--------|
| `.github/workflows/bump-version.yml` | **Delete** |
| `.github/workflows/publish.yml` | **Delete** |
| `.github/workflows/release.yml` | **Rewrite** (complete replacement) |
| `.github/workflows/test.yml` | **Modify** (2-line branch filter change) |
| `.github/workflows/publish-test.yml` | No change |

---

## Task 1: Delete Obsolete Workflow Files

**Files:**
- Delete: `.github/workflows/bump-version.yml`
- Delete: `.github/workflows/publish.yml`

- [ ] **Step 1: Delete both files**

```bash
git rm .github/workflows/bump-version.yml .github/workflows/publish.yml
```

Expected output:
```
rm '.github/workflows/bump-version.yml'
rm '.github/workflows/publish.yml'
```

- [ ] **Step 2: Verify they are gone**

```bash
ls .github/workflows/
```

Expected output (only these files remain):
```
publish-test.yml  release.yml  test.yml
```

- [ ] **Step 3: Commit**

```bash
git commit -m "ci: remove obsolete bump-version and publish workflows"
```

---

## Task 2: Update `test.yml` Branch Filters

**Files:**
- Modify: `.github/workflows/test.yml`

- [ ] **Step 1: Edit the `on:` block**

Open `.github/workflows/test.yml`. Replace the `on:` block:

```yaml
# BEFORE
on:
  push:
    branches: [main, release]
  pull_request:
    branches: [main, release]
```

```yaml
# AFTER
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
```

The rest of the file is unchanged.

- [ ] **Step 2: Validate YAML syntax**

```bash
python -c "import yaml; yaml.safe_load(open('.github/workflows/test.yml')); print('YAML valid')"
```

Expected: `YAML valid`

- [ ] **Step 3: Verify release branch is gone**

```bash
grep -n "release" .github/workflows/test.yml
```

Expected: no output (zero matches)

- [ ] **Step 4: Commit**

```bash
git add .github/workflows/test.yml
git commit -m "ci: remove release branch from test workflow triggers"
```

---

## Task 3: Write New All-in-One `release.yml`

**Files:**
- Modify: `.github/workflows/release.yml` (full rewrite)

- [ ] **Step 1: Replace the entire file content**

Write the following as the complete content of `.github/workflows/release.yml`:

```yaml
name: Release

on:
  workflow_dispatch:
    inputs:
      version_type:
        description: "Version bump type"
        required: true
        default: "patch"
        type: choice
        options:
          - patch
          - minor
          - major

concurrency:
  group: release
  cancel-in-progress: false

jobs:
  release:
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    timeout-minutes: 30

    steps:
      - uses: actions/checkout@v4
        with:
          token: ${{ secrets.PAT_TOKEN }}
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install Poetry
        uses: snok/install-poetry@v1
        with:
          version: latest
          virtualenvs-create: true
          virtualenvs-in-project: true

      - name: Install dependencies
        run: poetry install --with dev,format

      - name: Run checks
        run: |
          poetry run ruff check .
          poetry run mypy .
          poetry run pylint .
          poetry run pytest tests/ -v --tb=short
        env:
          DOMAIN: ${{ secrets.DOMAIN }}
          CHAT_KEY: ${{ secrets.CHAT_KEY }}
          COMPLETION_KEY: ${{ secrets.COMPLETION_KEY }}
          APP_KEY: ${{ secrets.APP_KEY }}
          WORKFLOW_KEY: ${{ secrets.WORKFLOW_KEY }}

      - name: Bump version
        run: poetry version ${{ inputs.version_type }}

      - name: Get version
        id: version
        run: echo "version=$(poetry version -s)" >> $GITHUB_OUTPUT

      - name: Check tag does not already exist
        run: |
          if git tag -l "v${{ steps.version.outputs.version }}" | grep -q .; then
            echo "::error::Tag v${{ steps.version.outputs.version }} already exists. Delete it first or choose a different version type."
            exit 1
          fi

      - name: Commit and push
        id: bump_commit
        run: |
          git config user.name github-actions
          git config user.email github-actions@github.com
          git add pyproject.toml
          git commit -m "chore: bump version to v${{ steps.version.outputs.version }} [skip actions]"
          git push
          echo "sha=$(git rev-parse HEAD)" >> $GITHUB_OUTPUT

      - name: Create GitHub Release
        uses: softprops/action-gh-release@v3
        with:
          token: ${{ secrets.PAT_TOKEN }}
          tag_name: v${{ steps.version.outputs.version }}
          name: Release v${{ steps.version.outputs.version }}
          target_commitish: ${{ steps.bump_commit.outputs.sha }}
          draft: false
          prerelease: false
          generate_release_notes: true

      - name: Build package
        run: poetry build

      - name: Publish to PyPI
        run: poetry publish
        env:
          POETRY_PYPI_TOKEN_PYPI: ${{ secrets.PYPI_TOKEN }}
```

- [ ] **Step 2: Validate YAML syntax**

```bash
python -c "import yaml; yaml.safe_load(open('.github/workflows/release.yml')); print('YAML valid')"
```

Expected: `YAML valid`

- [ ] **Step 3: Verify key structural properties**

```bash
# Must trigger only on workflow_dispatch
grep -n "workflow_dispatch" .github/workflows/release.yml
# Expected: line with "workflow_dispatch:"

# Must have concurrency guard
grep -n "cancel-in-progress: false" .github/workflows/release.yml
# Expected: one match

# Must gate on main only
grep -n "refs/heads/main" .github/workflows/release.yml
# Expected: one match

# Must have job timeout
grep -n "timeout-minutes" .github/workflows/release.yml
# Expected: one match

# Must use [skip actions] not [skip ci]
grep -n "skip actions" .github/workflows/release.yml
# Expected: one match

# Must NOT reference the release branch (branch filter check only)
grep -n "branches" .github/workflows/release.yml
# Expected: no output (workflow_dispatch has no branches filter)
```

- [ ] **Step 4: Commit**

```bash
git add .github/workflows/release.yml
git commit -m "ci: replace release workflow with all-in-one main-branch release"
```

---

## Post-Implementation Checklist

After merging to `main`, verify the following manually on GitHub:

- [ ] GitHub Actions tab shows only 3 workflows: **Test**, **Publish to TestPyPI**, **Release**
- [ ] The **Release** workflow shows `workflow_dispatch` as its only trigger
- [ ] The **Test** workflow triggers on push to `main` (confirm via a test push or PR)
- [ ] The `release` branch can be safely deleted if it still exists: `git push origin --delete release`
