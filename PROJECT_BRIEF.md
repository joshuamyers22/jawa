# Project Brief

- **Problem and affected users:** Researchers need a reproducible way to test
  whether candidate features add conditional predictive information without
  turning exploratory association into unsupported causal claims. Initial users
  are Jawa maintainers and statistical reviewers.
- **Measurable success criteria:** The supported screening core controls its
  pre-specified error criterion in global-null simulations; reports selection
  stability and uncertainty; beats or appropriately ties naive baselines in
  locked, nested out-of-sample benchmarks; and reproduces byte-stable evidence
  from a pinned revision and environment.
- **Explicit non-goals:** Automatic causal discovery, proof of intervention
  effects from observational data, production trading decisions, universal
  feature-selection optimality, or compatibility with upstream internals.
- **Runtime/deployment environment:** Python 3.11+; offline research and batch
  evaluation first. No network service or live decision path is in scope.
- **Tabular engine:** Polars. Any pandas interoperability exception requires an ADR.
- **Statistical engine:** Statsmodels plus NumPy/SciPy where justified. Every
  analysis specifies its estimand, model, assumptions, covariance, diagnostics,
  multiplicity policy, and validation design before final assessment.
- **Statistical-learning point-of-view:** Prefer simple baselines, nested
  evaluation, full candidate-history retention, stability analysis, and
  fold-local learned steps. Departures require written rationale and evidence.
- **Decision objective:** Rank or select variables for further predictive study.
  The action is analyst review, not automated intervention. Utility is improved
  held-out prediction or reduced model complexity subject to calibrated false
  discovery/selection risk. Association-to-causation is the principal proxy gap.
- **Baselines:** Training-fold mean, marginal association, regularized linear
  models, permutation/null ranking, and full-conditioning leave-one-covariate-out
  (LOCO) comparisons. `probe_fs` may supply an external comparator, never an
  unexamined dependency or ground truth.
- **Data classification and retention:** Synthetic and appropriately licensed
  public data only for the initial project. No PII, secrets, client data, or raw
  restricted data in Git. Immutable versioned inputs and derived evidence follow
  documented source-license and retention terms.
- **Dataset contract:** Maintainers own schema versions. Breaking changes require
  a new dataset/schema version and migration note. Published datasets are
  immutable, hash-verified, and rebuildable; deletion follows source obligations.
- **Availability and recovery:** No service SLO initially. Source, lockfile,
  manifests, and evidence must be sufficient to reproduce a release from Git.
- **Latency/capacity:** Batch correctness takes precedence. Benchmark wall time,
  memory, and input shape before declaring scale support; no live-path claims.
- **Top failure or abuse scenarios:** False discovery under adaptive testing;
  sequential residualization that reintroduces prior controls; coefficient sign
  reversal hidden by magnitude-only summaries; leakage from selection outside
  folds; singular/near-singular designs; sparse exact matches; invalid causal
  language; and cherry-picked simulations or seeds.
- **Units and time:** Every column declares units. Timestamps are UTC and include
  feature/target availability when temporal prediction is used. Domain calendars
  must be explicit rather than inferred.
- **Missingness and outliers:** Pre-specified per analysis and fitted within the
  training fold. No silent row deletion, imputation, winsorization, or coercion.
- **Point-in-time controls:** Preserve source ordering and as-of metadata; purge
  unavailable labels; construct universes and transformations inside each fold.
- **Regression and multiplicity:** Use rank-aware joint projections. Pre-select
  the family and error target (for example FWER or FDR), account for adaptive
  search, report effect sizes and uncertainty, and retain all tested candidates.
- **Assessment separation:** Development and selection use simulation/training
  data. A locked final suite and seeds are evaluated once per release candidate.
- **Research-to-production parity:** A capability is unsupported until its
  evidence-producing path and public API share tested code. Monitor input schema,
  numerical failures, selection rate/stability, and predictive degradation.
- **Reconciliation:** Compare independent implementations and analytic reference
  cases with pre-specified absolute/relative tolerances; investigate every breach.
- **Streaming policy:** Not applicable until a live-path ADR defines ordering,
  replay, stale-data, overload, and recovery semantics.
- **Owner:** Joshua Myers.
