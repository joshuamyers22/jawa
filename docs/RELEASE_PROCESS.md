# Release process

Jawa releases are built only from semantic-version tags whose value exactly
matches `[project].version` in `pyproject.toml`. The manifest is the sole version
source; source modules do not duplicate it.

## Candidate verification

From a clean checkout of the candidate commit:

```sh
make setup
make check
make audit
uv run python tools/verify_release.py --tag v0.1.1 --dist-dir dist
```

`make check` runs lint/format checks, strict typing, unit and contract tests,
builds wheel and sdist, verifies their embedded name/version, and installs each
distribution in a separate temporary environment before exercising every public
entry point. CI repeats this on CPython 3.11 and 3.12 by passing the matrix value
through `make check PYTHON=<version>` so `.python-version` cannot mask a runtime.

## Tagged release output

The tag workflow rebuilds from the checked-out tag, repeats the quality and audit
gates, validates tag/manifest/wheel/sdist identity, generates a CycloneDX SBOM,
writes and re-verifies `SHA256SUMS`, and creates signed Sigstore-backed GitHub
provenance for every file named by the checksum manifest. GitHub Release receives
the distributions, SBOM, and checksum manifest from that same job.

The workflow uses immutable action commit pins and only tag-scoped permissions.
There is no PyPI publishing path in M1.

After publication, download the release assets and verify them:

```sh
uv run python tools/checksums.py verify path/to/downloaded-assets
gh attestation verify path/to/downloaded-assets/jawa-0.1.1-py3-none-any.whl \
  --repo joshuamyers22/jawa
gh attestation verify path/to/downloaded-assets/jawa-0.1.1.tar.gz \
  --repo joshuamyers22/jawa
```

Do not create or move a release tag until the exact commit has passed required
main-branch checks. A failed release remains failed evidence; fix forward with a
new version rather than silently replacing published assets.

Release publication uses an explicit allowlist for wheel, sdist, SBOM, and
`SHA256SUMS`. `uv build` clears the output directory and suppresses its generated
`.gitignore`; build-tool housekeeping files are neither checksummed nor published.
