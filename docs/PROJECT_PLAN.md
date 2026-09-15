# Jawa production-quality project plan

## Plan metadata

- Status: Proposed; implementation not started
- Accountable owner: Joshua Myers
- Upstream reference: `rahulkm3/causalscreen` at
  `ff3fb593a926df5f1db422e63a514d2591df245e`
- Risk: High if represented as causal or used for consequential decisions;
  material for ordinary predictive feature selection
- Change control: Changes to scope, estimand, error criterion, final benchmark,
  or release gates require an ADR and independent statistical review.

## Outcome

Build an independently implemented, reproducible research library for
conditional feature screening. The first supportable result is a transparent
predictive/associational ranking with calibrated selection behavior. Causal
interpretation, local models, and drift signals are separate research tracks and
remain experimental until each passes capability-specific evidence gates.

## Success criteria

- Every output maps to a documented target quantity and permitted claim.
- A pre-specified FWER, FDR, or other approved error target is calibrated on a
  locked null/mixed-signal suite, including correlated candidates.
- Control projection matches a direct joint least-squares reference, is
  orthogonal to the control span when identifiable, and reports rank and
  conditioning failures.
- All learned operations occur within training folds; the final benchmark is
  untouched until the protocol and implementation are frozen.
- Results expose uncertainty, selection stability, tested candidates, numerical
  diagnostics, and refusal conditions—not only selected names or p-values.
- A clean clone completes locked setup, format, lint, type checking, tests,
  dependency audit, build, and wheel/sdist smoke checks.
- Every public claim is reproducible from immutable inputs, a code revision,
  lockfile, seeds, command, result schema, and artifact hashes.

## Non-goals

- Generic causal discovery from observational partial correlations.
- Treating prediction, temporal precedence, or conditioning as identification.
- Supporting `p >= n`, nonlinear inference, local modeling, or live monitoring
  without a separately approved statistical and operational contract.
- Reproducing upstream APIs or preserving upstream terminology for compatibility.
- Treating `probe_fs`, upstream examples, or private anecdotes as ground truth.

## Core invariants

- No association is labeled causal without an approved estimand and
  identification argument.
- No p-value is presented at a nominal level that ignores adaptive selection.
- Controls are projected jointly; a sequential residual is never described as a
  joint unexplained component.
- Coefficient direction is preserved and reported; magnitude-only summaries may
  supplement but never replace signed changes.
- Development, model selection, and locked final assessment remain separate.
- Unsupported data, ranks, degrees of freedom, or feature roles fail closed.
- Passing software tests does not validate a scientific claim, and passing a
  benchmark does not validate release security or operations.

## Delivery sequence

```text
M0 contract and provenance ─┐
                           ├─> M2 corrected screen ─> M3 locked evidence ─> M6 candidate
M1 reproducible foundation ┘            │                    ▲
                                        ├─> M4 local models ─┤
                                        └─> M5 drift ────────┘
```

M0 and M1 may run together. M4 and M5 start only after M2 freezes shared data,
evaluation, and evidence contracts. M6 is an evidence decision, not an automatic
consequence of finishing code.

## Milestones

### M0 — Claim containment, provenance, and project contract

Deliverables:

- Keep the independent-downstream and non-endorsement statement prominent.
- Pin the reviewed upstream revision and track any later copied/adapted code at
  file level with required notices.
- Use predictive/associational language for the intended supported core.
- Mark causal, local-model, and drift capabilities experimental.
- Approve `PROJECT_BRIEF.md`, the statistical analysis plan, and ADR-0001.
- Record Jawa's owner-selected MIT License in the package and repository.

Exit gate: README, package metadata, API vocabulary, and analysis plan describe
the same scope; no supported claim depends on an unapproved causal assumption.

### M1 — Reproducible engineering foundation

Deliverables:

- Retain the typed `src/` layout, generated lockfile, pinned CI actions, security
  policy, contribution guide, changelog, and release checklist.
- Run one local command that covers formatting, linting, strict types, tests, and
  build checks; run dependency audit separately and visibly.
- Test all supported Python versions and smoke-test wheel and sdist in isolated
  environments.
- Use one version source and require tag/package/artifact agreement.
- Emit checksums, SBOM, provenance, and signed or trusted-published releases.
- Define stable result schemas with revision, environment, input/plan hashes,
  seeds, warnings, candidate history, and numerical diagnostics.

Exit gate: clean clone to reproducible artifacts passes locally and in CI; the
release candidate is traceable without uncommitted state.

### M2 — Statistical specification and corrected screening core

Deliverables:

- Approve the primary target: conditional linear association and/or incremental
  out-of-sample predictive contribution. Keep distinct modes distinct.
- Define the candidate family and pre-select the multiplicity/selective-inference
  target with justified dependence assumptions.
- Implement joint control projection with pivoted QR or SVD and expose effective
  rank, residual degrees of freedom, tolerance, and condition diagnostics.
- Preserve signed coefficients and define effect-difference quantities directly.
- Validate unique names, shapes, finite values, constants, roles, fit state, and
  design identity; refuse unsupported `p >= n` inference.
- Add bootstrap/subsample selection stability if approved in the analysis plan.
- Document why conditioning on mediators, colliders, or descendants can change
  the scientific question and cannot be automated away.

Mandatory adversarial families:

- independent and correlated global nulls over multiple `n` and `p`;
- confounders, proxies, mediators, colliders, descendants, instruments, direct
  causes, indirect causes, and irrelevant variables;
- sign reversal and effect cancellation;
- nonlinear zero-correlation signals and interactions;
- heteroskedastic, dependent, heavy-tailed, and contaminated errors;
- constant, duplicate, collinear, ill-scaled, rank-deficient, and `p >= n` input;
- candidate-order permutations and weak-signal instability.

Exit gate: an independent statistical reviewer approves the target, null,
assumptions, error criterion, and locked tolerances; adversarial cases either pass
or trigger documented refusal behavior.

### M3 — Public evidence and benchmark program

Deliverables:

- Publish the protocol and freeze final-assessment datasets/seeds before viewing
  their results.
- Compare marginal association, ordinary full regression, regularized linear
  baselines, stability selection, and appropriate nonlinear baselines.
- Include `probe_fs` full-conditioning LOCO as an external comparator where its
  contract matches. Record its revision and environment; do not make it a Jawa
  dependency or infer truth from agreement.
- Nest preprocessing, screening, hyperparameter selection, binning, and routing
  within folds. Retain per-observation predictions and every candidate tried.
- Report calibration, power/recall, false selections, selection stability,
  predictive delta versus baseline, uncertainty, failures, runtime, and memory.
- Use licensed public data only when the predictive question and time boundary
  are defensible; otherwise prefer transparent synthetic generators.
- Require an independently briefed reviewer to reproduce every published table.

Exit gate: a clean environment reproduces the complete evidence bundle and its
hashes; claims include negative results and do not exceed tested regimes.

### M4 — Honest localized modeling

Deliverables:

- Separate partition definition, fold-local binning, support checks, estimator
  fitting, routing, and storage.
- Replace continuous exact equality with pre-specified bins, neighborhoods, or a
  declared smooth model; version learned boundaries.
- Derive minimum cell sizes from estimator dimension and uncertainty.
- Enable local prediction only after untouched validation meets a predeclared
  improvement/noninferiority rule; otherwise route to the global model.
- Bound cell/model counts, memory, latency, unknown-category behavior, and cache
  semantics; ensure serialized artifacts are deterministic and concurrency-safe.

Exit gate: nested out-of-sample evidence supports the routing rule, and rare,
unknown, or shifted inputs safely fall back without fitting during prediction.

### M5 — Drift research

Deliverables:

- Define each signal separately: signed coefficient change, partial association,
  predictive performance, residual scale, calibration, feature distribution,
  and support coverage.
- Benchmark coefficient sign, magnitude, intercept, variance, noise, support,
  category, missingness, label, prevalence, and measurement shifts.
- Measure detection delay, lead time, alert precision/recall, false-alert rate,
  and downstream harm with uncertainty on a later locked window.
- Define threshold fitting, cadence, label delay, alert action, suppression,
  fallback, rollback, refit, and retirement.
- Explicitly test the sign-reversal blind spot: a magnitude-only statistic can be
  zero when coefficients change from `+b` to `-b`.

Exit gate: each retained signal has a bounded claim, known blind spots, and an
owned operational response; no universal early-warning claim is made.

### M6 — Capability-specific production candidate

Deliverables:

- Complete threat model, release readiness, production readiness, model/method
  card, compatibility policy, and rollback exercise.
- Verify lockfile, licenses, vulnerability status, CI provenance, SBOM,
  checksums, tag/version parity, and installation smoke tests.
- Freeze the supported API, result schema, serialization format, numerical
  tolerances, deprecation policy, and monitoring/retirement triggers.
- Obtain named software, statistical, artifact, and operational approvals.

Exit gate: support is awarded per capability. The screen may graduate while
causal interpretation, local models, and drift remain experimental. No open high
risk applies to the capability being released.

## Work breakdown

| ID | Work item | Milestone | Owner role | Acceptance evidence |
|---|---|---|---|---|
| GOV-001 | Finalize claims, license, provenance, and maturity labels | M0 | Owner + statistician | Documentation/API audit |
| ENG-001 | Maintain frozen environment and CI/runtime matrix | M1 | Maintainer | Clean frozen CI run |
| ENG-002 | Add stable screening/evidence schemas and negative contracts | M1/M2 | Maintainer | Schema and contract tests |
| SAP-001 | Approve target, null, roles, error target, and falsification plan | M2 | Statistical owner | Signed analysis plan |
| STAT-001 | Implement multiplicity-aware screening | M2 | Statistical owner | Locked calibration report |
| STAT-002 | Implement joint rank-aware projection | M2 | Numerical owner | Reference/orthogonality tests |
| STAT-003 | Preserve signed effects and uncertainty | M2 | Statistical owner | Sign-reversal tests |
| BENCH-001 | Freeze and reproduce comparative benchmark | M3 | Research owner | Independent evidence replay |
| LOCAL-001 | Fold-local partitions and safe global fallback | M4 | ML owner | Nested OOS evidence |
| DRIFT-001 | Prospective signal and alert contract | M5 | Model-risk owner | Later-window alert evidence |
| REL-001 | Capability-specific release and rollback | M6 | Release owner | Approved release checklist |

## Acceptance matrix

| Requirement | Verification | Approver |
|---|---|---|
| Vocabulary matches the target quantity | Documentation/API audit against approved plan | Statistical reviewer |
| Error criterion is calibrated | Locked null and mixed-signal simulation report | Statistical reviewer |
| Projection invariant holds | Direct joint reference, orthogonality, rank tests | Numerical reviewer |
| Sign changes cannot disappear | Signed-coefficient and reversal test family | Statistical reviewer |
| Unsupported designs fail closed | Parameterized negative test matrix | Maintainer |
| Selection and final assessment are separate | Frozen protocol, split IDs, search history | Artifact reviewer |
| Local path is safe where enabled | Nested OOS results and fallback tests | ML owner |
| Drift signal is bounded and actionable | Prospective later-window assessment | Model-risk owner |
| Repository and release reproduce | Clean CI, isolated artifact smoke, hashes | Release owner |

## Risk register

| Risk | Likelihood | Impact | Mitigation | Trigger |
|---|---|---|---|---|
| Causal overclaiming returns | Medium | High | Claim lint/review and capability labels | Public causal wording without approved plan |
| Adaptive false discoveries | High | High | Preselected family/error target and null calibration | Upper calibration bound exceeds tolerance |
| Leakage from selection outside folds | Medium | High | Pipeline/nested-fold tests and search log | Test information affects fitted step |
| Collinearity/numerical instability | High | Medium | QR/SVD, rank diagnostics, fail closed | Rank/tolerance changes alter selections |
| Benchmark overfitting | Medium | High | Locked final suite and version-on-reuse | Final result influences implementation |
| Local sparsity harms prediction | High | Medium | Support rule and global fallback | Validation noninferiority fails |
| Drift alert misses sign change | Medium | High | Signed metrics plus direct performance monitoring | Opposite-signed coefficients have same magnitude |
| Upstream/license ambiguity | Low | High | Provenance file and file-level notices | Upstream code is copied or adapted |

## First implementation PR

After M0 approval, the first implementation PR should be deliberately narrow:

1. Define typed input/result schemas and explicit refusal errors.
2. Implement a rank-aware joint projection primitive with direct least-squares
   reference tests.
3. Add the global-null, correlated-control, sign-reversal, collinearity, and
   candidate-order adversarial tests.
4. Emit an evidence artifact containing all candidates, signed effects,
   uncertainty, rank/df diagnostics, plan hash, input hash, revision, and seed.

It must not introduce causal, local-model, or drift APIs.

## Definition of done

A milestone is done only when its documented artifacts exist, local and CI gates
pass from a clean frozen environment, its acceptance evidence is independently
reviewed, and remaining limitations are reflected in public documentation. Three
review passes without new evidence trigger re-specification or escalation rather
than repeated review. Calibration regression, test-set reuse, unreproducible
claims, nondeterministic artifacts, or provenance/security failure block release.
