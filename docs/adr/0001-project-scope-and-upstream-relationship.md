# ADR-0001: Project scope and upstream relationship

- Status: Accepted
- Date: 2026-09-15
- Owner: Joshua Myers

## Context

`causalscreen` explores partial-correlation screening, iterative conditioning,
local exact-match models, and drift. Adversarial review found valuable research
questions but also a mismatch between some causal terminology and the evidence,
plus risks from adaptive testing, sequential residualization, sign-insensitive
summaries, and in-sample local selection.

## Decision

Jawa is an independent downstream iteration, not an affiliated fork or endorsed
release. Its default contract is conditional predictive/associational screening.
Causal discovery, local modeling, and drift are separate experimental
capabilities that cannot inherit validation from the core screen.

The initial repository copies no upstream source code. Any later copied or
adapted code must record provenance and satisfy the upstream license. Public API
names and documentation must not imply compatibility with upstream unless that
compatibility is explicitly tested and versioned.

## Consequences

- Documentation always links and credits the upstream project while stating
  independence and non-endorsement.
- “Causal” claims require a pre-specified estimand, identification assumptions,
  negative controls/falsification, and capability-specific review.
- Release maturity is assigned per capability; one passing component cannot
  confer production status on another.
- The project may use `probe_fs` as an external LOCO comparator without importing
  its product claims, code, or assumptions.
