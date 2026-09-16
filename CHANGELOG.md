# Changelog

Notable changes are recorded here using semantic versioning.

## 0.1.1 - 2026-09-16

- Established Jawa as an independent downstream iteration of `causalscreen`.
- Added the production project brief, statistical analysis plan, staged delivery
  plan, upstream provenance, and initial architecture decision.
- Generated a typed, locked Python data/quant foundation from the production
  project template.
- Adopted the MIT License.
- Completed M0 with an evidence-linked project contract, upstream provenance,
  bounded statistical-plan approval, and explicit M2 implementation gates.
- Completed M1 with a Python 3.11/3.12 CI matrix, isolated wheel/sdist smoke
  checks, artifact identity verification, checksum/SBOM/signed-provenance release
  controls, and a tested v1 screening-evidence envelope.
- Restricted release publication to the checksummed wheel, sdist, SBOM, and
  checksum manifest after consumer verification found an untracked housekeeping
  file in the superseded `v0.1.0` release.
