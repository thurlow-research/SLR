# Systematic Literature Review — Human Oversight of AI-Generated Code

Working repository for a dissertation systematic literature review (SLR) investigating:

> How do organizations practice and scale **human oversight of AI-generated code ("vibe
> coding")** so oversight keeps pace with code volume without sacrificing quality — including
> the governance/policy landscape and the strengths and limitations of current oversight
> practices.

This repo is the review's **methodological audit trail**: search and screening protocols,
cross-model calibration data, the theme-tagging instrument and its full change history, and the
tooling that runs the pipeline. It is public so the methodology can be referenced and inspected;
it is not a general-purpose software project.

## How the review works (short version)

- **Corpus**: managed in a Zotero group library (database queries + citation snowballing →
  multi-stage screening → relevance triage into Core / Context tiers).
- **Screening & tagging pipeline**: a multi-model panel (Claude Opus, GPT, Gemini — pinned to
  each vendor's frontier tier) tags papers under a versioned, human-vetted instrument. A
  Jidoka-style triage ladder (schema check → consensus vote → disagreement-triggered k=3
  replication → computed tripwires) routes every paper to auto-accept, light review, or full
  human adjudication. **A human arbiter confirms every consequential decision** — model
  consensus is treated as a proposal, never as ground truth (the calibration data here documents
  why: unanimous multi-model errors occurred and were caught by human review).
- **Instrument provenance**: every definition change is logged in
  `slr-phase4/Taxonomy_Changelog.md` with the disparity that motivated it, the ruling, and the
  measured outcome.

## Repository layout

| Path | Contents |
|---|---|
| `Methodology/` | Protocol documents — scope/relevance criteria, triage design, calibration reports |
| `slr-phase-1-2/` | Search-and-screening stage: query batches, screening prompts and scripts |
| `slr-phase4/` | Theme-tagging stage: tagging instrument, taxonomy changelog, per-model tag data, triage tooling |
| `slr-tools/` | Shared pipeline utilities (screening runners, Zotero loaders) |
| `Handoffs/`, `Knowledge Xfer/` | Session-to-session working notes and context documents |
| `Database Queries/` | Raw search exports from the source databases |

## Companion tooling

Zotero library access, deduplication prep, and PDF→text extraction are handled by a separate
set of open-source Claude Code skills maintained alongside this project:
**[thurlow-research/ResearchClaudeCodeSkills](https://github.com/thurlow-research/ResearchClaudeCodeSkills)**.

## What is deliberately not here

- **Copyrighted paper full texts** (`slr-phase4/txt/` is gitignored) — the repo carries only
  bibliographic metadata, tags, and analysis artifacts.
- **Credentials** (`.envrc` and friends are gitignored and have never been committed; API keys
  are split read-only/read-write and rotated).
- **The Zotero library itself** — the corpus lives in Zotero; this repo records the decisions
  made about it.

## Repository policy

This repository is public for **reference and citation**. The `main` branch is protected:
changes land via pull request (with a maintainer bypass for the author's own workflow), and
external contributions are not expected — it is a research record, not a collaborative
codebase. Feel free to open an issue if you spot an error or want to discuss the methodology.

## License

Dual-licensed by content type:

- **Code** (scripts and tooling) — [MIT License](LICENSE).
- **Documentation and data** (methodology documents, the tagging instrument and changelog,
  calibration/tag data, notes) — [CC BY 4.0](LICENSE-DOCS): reuse freely with attribution.

Neither license extends to the underlying papers referenced by the review or their publishers'
content.

## Author

Scott Thurlow — D.Tech. student, Purdue University.
