# Statistical analysis plan: conditional feature screening

- Status: Approved for the M0 scope and claim boundary; not approved for
  statistical implementation or inferential claims
- Initial date: 2026-09-15
- M0 scope approval: Joshua Myers, 2026-09-16
- Owner: Joshua Myers
- Independent statistical reviewer: Required and not yet assigned; blocks M2
  implementation

This approval fixes the predictive/associational scope, causal prohibition, and
evidence boundary. It deliberately does not approve an estimator, multiplicity
procedure, calibration tolerance, practical threshold, or final benchmark.
Those choices require an updated plan and independent statistical approval in
M2 before screening code or inferential claims are permitted.

## Decision and target quantity

- **Decision:** Rank or select variables for further predictive investigation.
- **Population:** Defined separately for each immutable benchmark scenario or
  dataset; no cross-population generalization is assumed.
- **Primary target:** Incremental linear predictive information for a candidate
  given a pre-specified set of controls, measured in held-out data and supported
  by a conditional linear-association estimate.
- **Primary null:** The candidate's conditional linear coefficient is zero in the
  stated projection model. This is not a general conditional-independence null.
- **Action/horizon:** Analyst review; no automated intervention or live action.
- **Practical threshold:** Must be selected before the final benchmark in the
  outcome's natural units and/or held-out loss delta; a p-value alone is not
  practically significant.
- **Exploration boundary:** Candidate families, transformations, error targets,
  and thresholds may be developed on the development suite only. The final suite
  is evaluated after protocol freeze.
- **Causal estimand:** Deferred. No causal effect is estimated by this plan.
  A causal mode requires a separate approved plan stating treatment, outcome,
  intervention, adjustment set, identification assumptions, and falsification.

## Data and sample

- Initial evidence uses versioned synthetic generators and appropriately licensed
  public data with source URL/license, hashes, as-of time, and schema manifest.
- Observation unit, range, frequency, expected sample size, outcome, candidate
  roles, control roles, units, and transformations are fixed in each scenario.
- Missingness, outlier handling, encoding, scaling, and imputation are explicit,
  never silent, and fitted within training folds.
- Temporal analyses preserve ordering and record prediction, feature-availability,
  and target-availability times. Labels unavailable before a fold are purged.
- Duplicate names, non-finite values, constants, incompatible lengths, and
  insufficient residual degrees of freedom fail before estimation.

## Model specification

- The reference conditional-association estimator is OLS with an explicit
  intercept and all approved controls projected jointly.
- The numerical implementation uses pivoted QR or SVD with a declared rank
  tolerance. It records ordered design columns, effective rank, residual degrees
  of freedom, condition diagnostics, and refusal/fallback provenance.
- Candidate coefficients retain sign and units. Report coefficient, uncertainty,
  partial correlation where defined, and incremental held-out loss. Do not infer
  stability from absolute magnitude alone.
- HC3 is the initial cross-sectional covariance baseline. Cluster/HAC covariance
  is required where grouping or dependence warrants it and must be pre-specified.
- The candidate family is all variables explicitly registered before a run.
  Every tested candidate and selection decision is retained.
- **Multiplicity target:** Unresolved before implementation. Select one primary
  target (such as FWER or FDR), the procedure, family boundary, and acceptable
  Monte Carlo calibration interval before final-suite access. Naive repeated
  alpha-level testing is prohibited.
- Candidate transformations and interactions belong to the multiplicity/search
  family. Learned transformations are fold-local.
- Baselines: training-fold mean, marginal association, full OLS, regularized
  linear prediction, permutation/null ranking, stability selection, and—where
  contract-compatible—external `probe_fs` full-conditioning LOCO.
- Random generators, seeds, solver tolerances, and tie-breaking are explicit.

## Diagnostics and validation

- Check rank, singular values/condition diagnostics, leverage/influence,
  heteroskedasticity, residual dependence, and selection stability.
- Use nested cross-validation or expanding-window evaluation as appropriate.
  Screening, preprocessing, tuning, and threshold selection occur inside the
  training boundary. The baseline is refit in every fold.
- Retain development, selection, and locked final-assessment suite identifiers.
  Any reuse of final results for design creates a new benchmark version.
- Preserve per-observation held-out predictions, fold membership, all candidate
  results, failures, and aggregate uncertainty.
- Mandatory sensitivity families include global nulls, correlated controls,
  confounding/proxy/mediator/collider structures, sign reversal, effect
  cancellation, nonlinear zero-correlation signals, heteroskedastic/heavy-tailed
  errors, contamination, collinearity, `p >= n`, and candidate-order changes.
- Calibration reports the Monte Carlo confidence interval around the achieved
  error rate. Power is secondary to passing calibration and refusal behavior.
- Report selection frequency and rank stability across resamples; do not hide
  unstable selections behind a single run.

## Locked benchmark protocol

1. Develop only on public development seeds and datasets.
2. Freeze generator code, scenario parameters, candidate family, error procedure,
   baselines, metrics, practical thresholds, and numerical tolerances.
3. Hash and register a separate final seed manifest before execution.
4. Run the final suite once for a release candidate in the locked environment.
5. Store raw candidate histories, failures, predictions, diagnostics, timings,
   summaries, and hashes—not only favorable plots.
6. Have a reviewer who did not tune the method reproduce the report.

`probe_fs` comparisons must pin its revision and environment, use equivalent data
and outer splits, and state differences in target quantity. Agreement is not
validation; disagreement triggers investigation rather than winner selection.

## Evidence and approval

Every result records the command, Git revision, lockfile/environment fingerprint,
analysis-plan hash, input/generator hashes, seed and RNG, UTC time, hardware for
performance claims, complete configuration, output hash, and software versions.

Required evidence includes signed effects with uncertainty, error calibration,
selection stability, predictive comparison to baselines, numerical/refusal
diagnostics, negative results, and limitations. Release is blocked by calibration
failure, leakage, final-suite reuse, sign-loss, unexplained order sensitivity,
or an unsupported causal claim.

Approval requires the owner, an independent statistical reviewer, and an
artifact reviewer. Consequential or live use additionally requires a new plan,
operational owner, monitoring contract, threat model, and rollback exercise.
