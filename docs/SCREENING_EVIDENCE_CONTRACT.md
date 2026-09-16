# Screening evidence contract

`schemas/screening-evidence.schema.json` defines the stable v1 envelope that a
future Jawa screening run must emit. It fixes provenance and review structure,
not statistical semantics. The M2 analysis plan must still approve the target,
estimator, candidate family, multiplicity procedure, tolerances, and validation
design before any real screening artifact may use this contract.

## Required record

Every artifact records:

- a full Git revision, UTC evaluation time, and hashed analysis plan;
- the lockfile hash and exact Python/Jawa/numerical-library versions;
- immutable input identifiers, source revisions, licenses, and SHA-256 hashes;
- the random generator and every seed;
- outcome, ordered controls and candidates, candidate-family boundary, and
  multiplicity declaration;
- every candidate in evaluation order, including failures, signed effects,
  uncertainty, raw/adjusted p-values, selection decisions, and warnings;
- rank, residual degrees of freedom, condition information, singular values,
  tolerance, and numerical failures;
- validation design, fold count, executed leakage controls, metrics, global
  warnings, and limitations.

The content hash of the completed JSON artifact is stored by its run manifest or
review record rather than embedded recursively inside the artifact. Producers
must serialize deterministically and report that external digest.

## Compatibility

The schema identifier is `jawa-screening-evidence/v1`. Producers may add no
undeclared fields. A compatible change may clarify documentation or relax a
constraint without changing recorded meaning. New or renamed fields, changed
units, or changed semantics require a new schema version and migration note.

The fixture at `tests/fixtures/screening-evidence-v1.json` intentionally contains
no result. Its `not_evaluated` entries exercise the structural contract without
approving or simulating an M2 method. CI validates the schema itself, the fixture,
required candidate history, and full-revision enforcement.
