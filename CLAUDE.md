# Project instructions — SLR (Scalable Human Oversight)

- **Keep the local copy in sync — always.** This working tree (the OneDrive dir; `~/Code/SLR` is
  a symlink to it, one tree not two clones) must be kept current with `origin/main`: pull before
  starting work, and commit + push completed work rather than leaving it sitting uncommitted.
  Canonical remote: `https://github.com/thurlow-research/SLR-Scalable-Human-Oversight.git`.
- The repo is **PUBLIC**. Never commit: copyrighted paper full texts (`slr-phase4/txt/`),
  `Backups/`, `Downloads/`, `.envrc`/secrets, or PDFs — all gitignored; secret-scan staged
  content before every commit (see global instructions).
- **All assistant-authored changes land via PR, never direct to main** (adopted 2026-07-23):
  branch `claude/<topic>` → push → open PR with a summary of what changed and why → Scott
  reviews and approves/merges (bypass at his discretion). The assistant never merges without
  Scott's explicit say-so. After merge: pull `main`, delete the branch (sync rule above).
  This is the project's own oversight thesis applied to itself — AI-authored changes get a
  human inspect-and-gate step. Direct pushes to main are reserved for Scott's own hand edits.
- `main` is protected by a GitHub ruleset (PRs required; Scott holds bypass).
- Project conventions live in the `slr-conventions` skill; methodology source of truth is
  `Methodology/`; the current handoff doc in `handoffs/` is the session entry point.
