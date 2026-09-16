# M0 completion: claim containment, provenance, and project contract

- Status: Complete
- Completed: 2026-09-16
- Accountable owner and approver: Joshua Myers
- Scope: Governance and documentation only
- Implementation authorized: No; M2 remains blocked as described below

## Decision

M0 is complete. Jawa has an approved identity, provenance record, claim boundary,
project brief, and license. This decision does not approve a screening estimator,
an inferential procedure, a causal estimand, or any consequential use.

The statistical analysis plan is approved only for its M0 boundary: Jawa's
intended supported core is predictive/associational, causal interpretation is
excluded, all learned decisions must respect evaluation boundaries, and evidence
must be reproducible. The unresolved estimator, multiplicity procedure,
calibration tolerance, practical threshold, benchmark freeze, and independent
statistical reviewer are mandatory M2 gates.

## Deliverable evidence

| M0 requirement | Evidence | Result |
|---|---|---|
| Prominent independent-downstream and non-endorsement statement | `README.md`; `UPSTREAM.md` | Pass |
| Reviewed upstream revision pinned | `README.md`; `UPSTREAM.md`; ADR-0001 | Pass |
| Copied/adapted-code provenance rule | `UPSTREAM.md`; ADR-0001 | Pass |
| Predictive/associational supported-core language | `README.md`; `PROJECT_BRIEF.md`; analysis plan | Pass |
| Causal, local-model, and drift capabilities marked experimental | `README.md`; `PROJECT_BRIEF.md`; ADR-0001 | Pass |
| Project brief approved | `PROJECT_BRIEF.md` | Pass |
| Statistical scope and claim boundary approved | `docs/STATISTICAL_ANALYSIS_PLAN.md` | Pass, bounded to M0 |
| Upstream relationship decision accepted | `docs/adr/0001-project-scope-and-upstream-relationship.md` | Pass |
| Owner-selected license recorded | `LICENSE`; `pyproject.toml`; `UPSTREAM.md` | Pass — MIT |

## Exit-gate review

- README, package description, project brief, ADR, and statistical plan agree
  that the intended core is conditional predictive/associational screening.
- Public API modules contain no Jawa causal-screening implementation or causal
  result vocabulary; the current commands are explicitly labeled template
  fixtures.
- No supported claim relies on a causal identification assumption.
- The remaining use of “causal” documents prohibited claims, experimental scope,
  upstream context, or the future requirements for a separately approved mode.
- M0 completion does not change the repository's pre-implementation status.

## Verification

The completion change must pass:

```sh
make check
make audit
make build
uv run python tools/verify_release.py --tag v0.1.0
git diff --check
```

The published commit and GitHub CI/security checks provide the final execution
record. Any failure reopens M0 until corrected.

Local verification on 2026-09-16 passed: Ruff lint/format, Pyright strict mode,
34 unit tests, OSV vulnerability audit, dependency-license policy, wheel and
source-distribution builds, `v0.1.0` metadata parity, and Git diff checks. The
first sandboxed build attempt could not resolve PyPI DNS; the authorized network
retry completed successfully without a source change.

## Remaining blockers before M2 implementation

1. Name an independent statistical reviewer.
2. Choose and justify the primary estimator and conditional target quantity.
3. Choose the candidate-family boundary, error target, and multiplicity procedure.
4. Predeclare Monte Carlo calibration tolerances and practical-effect thresholds.
5. Freeze development versus final benchmark identities and review rules.

Until these are approved, Jawa may improve infrastructure and test harnesses but
must not implement or publish inferential screening results.
