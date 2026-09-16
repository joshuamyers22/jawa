# M1 completion: reproducible engineering foundation

- Status: Complete
- Completed: 2026-09-16
- Accountable owner and approver: Joshua Myers
- Scope: Engineering, evidence-envelope, and release foundation only
- Statistical implementation authorized: No; M2 remains blocked

## Decision

M1 is complete. A clean checkout has a locked environment, explicit supported
runtime matrix, one local quality command, isolated distribution verification,
release identity and supply-chain controls, and a stable screening-evidence
envelope. These controls make future work reviewable; they do not establish that
any screening estimator is correct.

## Deliverable evidence

| M1 requirement | Evidence | Result |
|---|---|---|
| Typed `src/` layout and locked dependency graph | `src/jawa/`; `uv.lock` | Pass |
| Pinned read-only CI across supported runtimes | `.github/workflows/ci.yml`; CPython 3.11/3.12 checks | Pass |
| One complete local gate | `make check` in `Makefile` | Pass |
| Separate vulnerability and dependency-license audit | `make audit`; `tools/check_licenses.py` | Pass |
| Wheel and sdist identity verification | `tools/verify_release.py`; release-tool tests | Pass |
| Isolated wheel and sdist installation/CLI smoke | `tools/smoke_dist.py`; `make check` | Pass |
| One package version source and tag parity | `pyproject.toml`; `tools/verify_release.py` | Pass |
| Checksums and tamper detection | `tools/checksums.py`; release-tool tests | Pass |
| SBOM and signed build provenance | pinned tag workflow; `docs/RELEASE_PROCESS.md` | Pass |
| Stable future screening result envelope | schema, fixture, contract doc, schema tests | Pass |
| Security, contribution, change, and release policy | repository root and `checklists/` | Pass |

## Runtime and clean-build evidence

The supported range is deliberately bounded to CPython 3.11 and 3.12 in package
metadata. Both runtimes passed Ruff, strict Pyright, 41 unit/contract tests,
wheel and source-distribution builds, embedded artifact identity checks, separate
temporary-environment installs, package import, metadata parity, and all four
console-entry-point help paths.

The first local 3.11 rehearsal found that `.python-version` could make `uv run`
silently recreate the matrix environment with 3.12. The Make interface now
accepts `PYTHON=<version>`, CI passes that value through every Python gate, and a
second 3.11 run demonstrated that both isolated installations used CPython
3.11.16. This failure is retained here because it materially changed the
verification design.

GitHub CI and secret scanning on the milestone commit provide clean-checkout
evidence. The `v0.1.0` GitHub release exercises tag/manifest/artifact parity,
CycloneDX SBOM generation, deterministic checksums, signed Sigstore provenance,
and same-job release publication.

## Evidence contract boundary

`jawa-screening-evidence/v1` requires revision, environment and lock identity,
input and plan hashes, RNG and seeds, full candidate history, signed effects,
warnings, numerical diagnostics, validation structure, and limitations. Its
fixture is explicitly `not_evaluated`. No estimator, error target, multiplicity
procedure, threshold, benchmark, or inferential claim is selected by M1.

## Exit-gate verification

```sh
make check PYTHON=3.11
make check PYTHON=3.12
make audit PYTHON=3.12
uv run python tools/checksums.py write dist
uv run python tools/checksums.py verify dist
git diff --check
```

M1 reopens if either supported runtime fails, a distribution cannot be installed
in isolation, tag/manifest/artifact identity diverges, the checksum manifest is
incomplete, provenance cannot be verified, or the schema permits untracked
candidate selection.

## Next gate

M2 must name an independent statistical reviewer and approve the estimator,
conditional target, candidate family, multiplicity procedure, calibration
tolerance, practical threshold, and frozen benchmark boundary before Jawa gains
screening implementation or inferential claims.
