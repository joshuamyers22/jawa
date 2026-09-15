# Jawa

Jawa is an independent, downstream iteration of Rahul Kumar Mandal's
[`causalscreen`](https://github.com/rahulkm3/causalscreen) project. It is not
affiliated with or endorsed by the original author.

The project is an early research scaffold for statistically defensible feature
screening and diagnostic experiments. Its intended supported core is
predictive and associational: conditional feature ranking, nested evaluation,
and reproducible evidence. Causal discovery, local-regime modeling, and drift
detection remain experimental until each capability has a stated estimand and
passes its own validation gates.

The initial scaffold contains no source code copied from `causalscreen`. It
draws on the project's problem framing and on an adversarial review of upstream
commit `ff3fb593a926df5f1db422e63a514d2591df245e`. See [UPSTREAM.md](UPSTREAM.md),
[the project plan](docs/PROJECT_PLAN.md), and
[the statistical analysis plan](docs/STATISTICAL_ANALYSIS_PLAN.md).

## Status

Pre-implementation and not suitable for consequential decisions. No output may
be described as causal merely because it is based on partial correlation,
residualization, feature selection, or temporal ordering.

## Development

Requires Python 3.11+ and [`uv`](https://docs.astral.sh/uv/).

```sh
make setup
make check
make audit
make build
```

The generated command-line examples are retained as infrastructure fixtures;
they are not yet the Jawa screening API:

```sh
uv run jawa data/example.csv
uv run jawa-regression data/regression-example.csv \
  --response return --predictor factor \
  --analysis-id example \
  --analysis-plan docs/STATISTICAL_ANALYSIS_PLAN.md \
  --revision "$(git rev-parse HEAD)" \
  --evaluated-at-utc "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  --sample-filters "complete synthetic fixture" \
  --validation-design "illustrative in-sample inference only" \
  --leakage-controls "synthetic fixture" \
  --output build/regression-evidence.json
```

## Working principles

- Define the target quantity and allowed claim before implementing an estimator.
- Fit preprocessing, screening, and tuning inside each training fold.
- Control the pre-specified error criterion across adaptive searches.
- Project controls jointly with rank-aware QR/SVD methods; do not repeatedly
  peel residuals one variable at a time.
- Test adversarial cases including global nulls, collinearity, sign reversal,
  nonlinear alternatives, exact-match sparsity, and distribution shift.
- Record locked environments, seeds, input hashes, code revisions, and complete
  candidate-search histories with every result.

Raw, private, or restricted data must not be committed. Initial development is
limited to synthetic and appropriately licensed public data.

## Project provenance

Jawa was generated from the `python-data-quant` archetype of
[`production-project-template`](https://github.com/joshuamyers22/production-project-template)
at commit `ecbfe0272c5d546f63b7ffc44600864b1d8689fd`.
