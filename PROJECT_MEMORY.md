# Jawa Project Memory

This is a bounded index of durable project facts, not an activity log or source
of truth. Verify entries against the linked artifact before acting. Do not store
secrets, personal data, client data, or hidden reasoning here.

## Durable constraints

| Key | Constraint | Evidence | Last verified |
|---|---|---|---|
| `independent-downstream` | Jawa must be described as an independent downstream iteration of `causalscreen`, with no affiliation or endorsement implied. | `UPSTREAM.md`; ADR-0001 | 2026-09-15 |
| `claims-before-code` | Predictive/associational language is the default; causal wording requires an approved causal estimand, identification argument, and falsification plan. | `PROJECT_BRIEF.md`; `docs/STATISTICAL_ANALYSIS_PLAN.md` | 2026-09-16 |
| `research-only` | All capabilities are research-only until their capability-specific release gates pass. | `docs/PROJECT_PLAN.md` | 2026-09-15 |
| `data-boundary` | Initial work uses only synthetic and appropriately licensed public data. | `PROJECT_BRIEF.md` | 2026-09-15 |
| `locked-evidence` | Consequential results bind inputs, plan, environment, revision, seeds, search history, and output hashes. | `REPRODUCIBILITY.md` | 2026-09-15 |
| `runtime-support` | Supported runtimes are CPython 3.11 and 3.12; CI and distribution smoke checks must run under both rather than relying on `.python-version`. | `pyproject.toml`; `.github/workflows/ci.yml` | 2026-09-16 |

## Accepted decisions

| Key | Decision and rationale | Evidence | Last verified |
|---|---|---|---|
| `template-origin` | Use the `python-data-quant` production template at commit `ecbfe0272c5d546f63b7ffc44600864b1d8689fd` for typed, tested, reproducible foundations. | `README.md` | 2026-09-15 |
| `initial-lineage` | The initial scaffold copies no `causalscreen` source; conceptual provenance is documented separately. | `UPSTREAM.md`; ADR-0001 | 2026-09-15 |
| `capability-staging` | Build and validate the conditional predictive screen before local modeling, drift, or any causal research track. | `docs/PROJECT_PLAN.md` | 2026-09-15 |
| `project-license` | Distribute Jawa under the MIT License, selected explicitly by the owner. | `LICENSE`; `pyproject.toml` | 2026-09-15 |
| `m0-contract` | M0 is complete: provenance, independent-downstream identity, claim containment, and the project boundary are approved; no statistical method or inferential claim was approved. | `docs/milestones/M0_COMPLETION.md` | 2026-09-16 |
| `m1-foundation` | M1 is complete: clean-build, runtime-matrix, isolated distribution, release identity, checksum/SBOM/provenance, and screening-envelope controls are established; no screening method was approved. | `docs/milestones/M1_COMPLETION.md` | 2026-09-16 |
| `screening-envelope-v1` | `jawa-screening-evidence/v1` fixes future result provenance and review structure without selecting statistical semantics. | `docs/SCREENING_EVIDENCE_CONTRACT.md`; schema | 2026-09-16 |

## Non-obvious current state

| Key | State worth retrieving later | Evidence | Last verified |
|---|---|---|---|
| `preimplementation` | M0 and M1 are complete, but the CLI and regression modules remain template fixtures rather than a released Jawa screening implementation. | `README.md`; M0/M1 completion records | 2026-09-16 |
| `probe-fs-role` | `probe_fs` is a possible full-conditioning LOCO benchmark comparator, not a dependency or truth oracle. | `docs/PROJECT_PLAN.md` | 2026-09-15 |

## Verified traps and failed approaches

| Key | Symptom and cause | Evidence or reproducer | Last verified |
|---|---|---|---|
| `sign-reversal` | Magnitude-only “missing power” can report no loss even when conditioning reverses a coefficient's sign. | `docs/PROJECT_PLAN.md` | 2026-09-15 |
| `adaptive-multiplicity` | Repeated nominal tests inflate global-null selection probability unless the adaptive family is controlled. | `docs/PROJECT_PLAN.md` | 2026-09-15 |
| `sequential-projection` | One-control-at-a-time residual peeling can reintroduce earlier controls when controls are correlated. | `docs/PROJECT_PLAN.md` | 2026-09-15 |

## Open threads

| Key | Unresolved question or next evidence | Owner | Review by |
|---|---|---|---|
| `statistical-contract` | For M2, select the estimator, multiplicity target/procedure, calibration tolerance, practical threshold, and final benchmark, then obtain independent statistical approval. | Joshua Myers | Before screening implementation |
