# SLR Status Update — Relevance Triage Complete

**Vibe Coding Governance Systematic Literature Review**
**Date:** 2026-07-08
**Since:** `Stage3_Relevance_Triage_and_CrossModel_QA.md` (2026-07-06)
**Headline:** **Stage 3 (relevance triage) is complete.** The 983-item eligible pool has been human-reviewed, deduplicated, and filed into a tiered extraction corpus in Zotero. This is a major milestone — the corpus is now defined for extraction.

---

## 1. What was completed since 07-06

The 07-06 doc defined the Stage-3 instrument, ran the AI triage (Opus) and the cross-model + human QA. Since then:

- **Human confirmation of the full core/context boundary.** All Opus "core" candidates (197) plus the adjacent high-context band were human-reviewed via four centrality-banded worksheets (`work/review/`), using a per-bucket marking convention (A/B: blank = confirm core; C/D: blank = keep context; overrides marked with rationale). Every row was read.
- **Scope deliberately narrowed** (see §3) to a two-part frame, which drove the demotion decisions.
- **Seven previously-undetected duplicate pairs** (published + preprint of the same work, missed by the DOI/title dedup) were found and reconciled in Zotero.
- **The corpus was filed** into a new `Phase 3 - Relevance Triage` collection tree with `s3:` provenance tags.
- **Two parallel, dissertation-scoped activities** were scoped and (for HOS) tooled: a contrarian/disconfirming-evidence hunt and an HOS-relevance identification pass.

## 2. Final corpus

Deduplication removed 7 records (each superseded record moved to its source stream's `04-Superceded` with a `superseded-by:` ↔ `supersedes:` pointer pair, and pulled from the Phase-2 pool). Final Stage-3 disposition across **969 unique primary records**:

| Tier | Count | Extraction | Zotero |
|---|---|---|---|
| **Core** | 114 | full text | `Phase 3 / 01-Core` |
| **Context** | 716 | abstract-level | `Phase 3 / 02-Context` |
| **Discard** | 139 | excluded | `Phase 3 / 03-Discard` |

Provenance is tagged: `s3:opus:<bin>` on all items (the model call), `s3:human:<final>` on the 301 human-reviewed items, `lit-review` on secondary literature, and `framing` on the definitional anchor. Filing was **additive** — no existing collection membership (source lineage, Phase-1/2, query collections) was altered.

## 3. Scope refinement (documented post-hoc change)

The initial broad RQ ("organizational human oversight of AI-generated code") yielded an unwieldy 983-item pool — a review of a field, not a question. Scope was refined to a **two-part core**:

1. **Quantify the problem** — including the *insufficiency* layer (evidence that current/automated oversight doesn't close the gap).
2. **Characterize the solution** — oversight mechanisms/frameworks across the full design space.

Consequently, **behavioral / effectiveness / adoption / perception / tool-benchmark studies were routed to Context** (retained at abstract level; they inform the planned organizational survey but are not core evidence). This aligns the SLR with its role in the dissertation: the empirical contribution is a **survey of organizations** on how they frame and solve the oversight problem; the SLR builds the knowledge base that shapes that survey. (The HOS prototype is a *learning vehicle*, not the contribution.)

Operational discriminators adopted during review (for reproducibility):
- **Effectiveness of oversight** (augment-vs-replace, SNR driving human attention) = candidate core; **tool capability benchmark** = context; **bare leaderboard** = context/discard.
- **Human oversight** (review/escalation/risk-triage) = in scope; **agent self-conformance / "make the agent follow best practices"** = out of core.
- **Secondary literature** (surveys, reviews, meta-analyses) → default context + `lit-review` tag (mined for reference-snowballing); promoted to core only for a novel central framework, a prior review on the exact topic, or an on-scope meta-analysis. ("Literature review" ≠ "code review" — the code-review-practice papers are primary domain content.)
- **Framing/definitional** sources kept tight — one empirically-grounded anchor at core; additional definitions → context.
- **What+how carve-out (AMENDMENT, arbiter ruling 2026-07-20 — `slr-phase4/Taxonomy_Changelog.md`
  §23):** a paper that **names the risk/quality elements to track AND defines operationalizable
  metrics for tracking them** (full specification: formulas/thresholds/tools) **clears core bar (2)
  as measurement even when unevaluated** — instrumentation *specification* is solution
  characterization, not mere applicability. Evaluation status is carried by the `design-only`
  facet, not demotion. What-only enumerations and borrowed-metrics papers remain context
  candidates. First ruled on `R4WJZBSF`.

## 4. Quality-assurance findings (finalized)

- **Cross-model agreement (250-item sample):** pairwise Cohen's κ 0.49–0.64; Spearman ρ ≈ 0.69 (all three legs — Opus, GPT-5.5, Gemini 3.1 Pro — rank centrality alike but cut bins at different heights).
- **Human Trust Check (blinded, n=50):** binary keep/discard κ = 0.30 — reproducing the Pass-1 pilot (κ = 0.27); "fair," below the 0.4 IRR floor. Re-confirms the standing posture: **AI is a consistency-check tool; the human is the arbiter.**
- **Model dissent does not predict human judgment** (codex/Gemini keep/discard κ vs human ≈ 0.01–0.04). There is no model shortcut for reviewing the keeps — which is *why* all cores were human-confirmed.
- **Opus core precision vs the human standard ≈ 64%** on the full ≥70 review (the n=10 Trust Check's alarming ~30% was small-sample noise). This full confirm/demote tally is the operative core-precision figure.
- **Reliability sampling note:** the n=50 check is a *gate*, not the citable κ; κ precision depends on sample size, not population (FPC negligible at N≈976). The inclusion decision needing IRR is keep/discard (binary); core/context is an extraction-depth allocation, resolved by direct human confirmation.

## 5. Parallel activities (dissertation-scope, not SLR steps)

- **Contrarian / disconfirming-evidence hunt** — a documented reflexivity step feeding survey design; deliberately *not* an SLR screening step (the SLR still synthesizes in-corpus contrary findings fairly). To run over the surviving corpus (incl. discards, to avoid baking in bias).
- **HOS-relevance identification** — an orthogonal pass (Opus, `hos_identify.py`) over the whole corpus flagging articles with buildable mechanisms for the HOS prototype (risk-routing, LLM-as-judge, guardrails, observability, escalation, calibration metrics). Flagged items get `hos-relevant` + `hos-area:<area>` tags and membership in "HOS Related Articles" — additive, orthogonal to `s3:` bins. Calibrated; full run pending.

## 6. Next

1. **Stage 4 — full-text fetch + extraction of the 114 confirmed cores** (PDF coverage is the constraint; fetched from the Zotero client). Context tier extracted at abstract level.
2. Complete the HOS-relevance pass; review flagged articles for prototype refinement.
3. Contrarian hunt → survey-instrument development.
4. Methods-chapter reliability paragraph (Stage-3 instrument is 3-way ordinal — report weighted κ).

## 7. Reproducibility

Tooling in `~/Code/SLR/slr-tools/stage3/`: `stage3_screen.py` (triage), `stage3_qa_sample.py` / `stage3_qa_screen.py` / `stage3_qa_score.py` (QA), `stage3_review_buckets.py` (review sheets), `stage3_import.py` (Zotero filing), `hos_identify.py` (HOS pass). QA sample seed 20260706. Data in `work/` and `work/review/` (CSV is authoritative; XLSX deprecated).
