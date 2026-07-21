# HOS-Seeded Theme Candidates (staging — graft before classifying cores)

**Canonical citation:** Thurlow, S. (2026). HumanOversightSystem (Version 0.5.0) [Computer software]. Purdue University. https://doi.org/10.5281/zenodo.21347272
**Status:** staging / not yet grafted. Source: synthesis of ~76 HOS research findings
(`~/Code/HumanOversightSystem/Human/research/`) against the SLR themes, 2026-07-13.
**Do not treat as finalized themes.** Graft the corpus-grounded ones into
`Emerging_Themes.md` / `Problem_Statement_Evidence.md` / `slr-conventions` *before* the
core-article classification pass.

## Guardrail — how HOS may and may not inform the SLR

HOS is the **learning vehicle, not an SLR data source**. Two kinds of HOS findings, neither
is direct SLR evidence:
1. **Pass-through corpus reading-notes** — HOS's notes on *corpus papers* (Mitropoulos 2026
   framing attack; Ferdous 2026 confidence/refactor-risk; Charoenwet/AgenticSCR 2026
   corroboration-ranking; Parris/AIRA 2026 scanner-masking; Kumar/SWE-PRBench single-reviewer
   recall; Watanabe 2026 agentic-PR size; Loker/CodeRabbit 2025 the "1.7×" claim). These point
   to *papers* — ground themes on those, don't double-count as HOS corroboration.
2. **HOS-original experience** — HOS's own design lessons. These are **theme hypotheses to
   validate against the corpus**, never self-validating (avoid the reflexivity trap).

**Action before grafting:** cross-check the pass-through papers against the library (some are
likely already cores/contexts; missing ones are retrieval/snowball candidates), so each grafted
theme stands on corpus evidence.

## A. Sharpeners for T0 — the oversight-scaling inversion (graft into Problem_Statement_Evidence)

- ⭐ **"The gap is enforcement, not knowledge."** A governance audit found ~21 fail-opens,
  nearly every one violating a principle already *written down*. Reframes the insufficiency
  layer: orgs don't lack oversight *policy* — the policy is **documented but not mechanically
  enforced**. Upgrades the problem statement from "do orgs oversee AI code?" to "**is their
  oversight enforced or merely advisory?**" (HOS: `unenforceable-rules-need-verification-mechanisms`.)
- **Task-class, not touched-content, is the agentic risk axis.** Refactor/chore break most yet
  read as "maintenance" and get lightest review → a concrete mechanism for *why* the riskiest AI
  output is least inspected. (Pass-through: Ferdous 2026, Watanabe 2026.)
- **Citation-hygiene caveat for the T0 anchor:** the "AI code ~1.7× buggier" premise traces to
  ONE source (Loker/CodeRabbit 2025, 470 PRs, AI-*co-authored* ≠ autonomous). Cite the chain
  precisely or the premise is attackable.
- **Unit of analysis:** AI-code quality is a *session* property, not a single-PR one — errors
  interlock across steps ("house of cards"). (HOS-original: `working-state-invariant`.)

## B. New theme candidate — T3: "The overseer is itself an untrusted, attackable component"

*Thesis:* AI reviewers/scanners are not a trusted oracle — they emit confident false signal, can
be socially engineered, and can suppress true signal — so the oversight layer needs its own
verification before its output drives action. This is the **strengths/limits-of-current-oversight**
limb of the RQ, and it cross-links T1 (a framing attack *is* a supply-chain attack on the
oversight layer).
- Confident non-reproducing reports (3/4). (HOS-original: `reviewer-agents-file-confident-non-reproducing-reports`.)
- 100% success flipping reviewer verdicts via PR-prose framing. (Corpus: Mitropoulos 2026.)
- LLM synthesis layer masks a real scanner FAIL as "this is fine." (Corpus: Parris/AIRA 2026.)
- Guard that records-but-doesn't-halt executes the refused action. (HOS: `a-guard-that-doesnt-halt-is-not-a-guard`.)
**Graft plan:** anchor on the *corpus* papers (Mitropoulos/Parris/…); check they're in the library first.

## C. Core-criteria refinement (graft into slr-conventions §criteria)

- **Gate on a computed/independent signal, never the model's self-report.** Model confidence is
  saturated (99.9% at 8–10) and flat vs defect rate; a reviewer's own "approve" can't override its
  own findings list. **Bounds the SNR-driving-attention discriminator:** the routing signal must be
  independent of the producer. This is exactly why `VTDG995V` (calibration → *computed*
  review-intensity) is core, but "route review by the model's own confidence" is disqualified.
  (HOS/corpus: `agent-confidence-is-uninformative…`, `gate-on-computed-signal-not-self-reported-verdict`,
  `self-classification-cannot-gate-the-human-boundary`, Ferdous 2026.)

## D. Corroborations of existing themes (fold as supporting points)

- **T1 (tooling supply chain)** extends from *installed* tooling to *invoked* tooling: oversight
  instruments that shell out to vendor CLIs **fail open** (removed flag, changed output, auth lapse
  → "ran, found nothing"); CI is a generous superset so absence-failures are invisible until field
  install ("green can mean the gate never ran"). (`tooling-drift-in-validation-pipelines`,
  `ci-is-blind-to-consumer-environment-failures`, `oversight-gate-must-declare-its-deps-and-fail-loud`.)
- **T2 (explanation)**: near-verbatim support — an escalation drives action only with three layers
  (descriptive/contextual/actionable) and project-calibrated thresholds
  (`structured-fault-explanation-drives-developer-action`, corpus Adejumo & Johnson 2025); review
  *volume* is itself a failure mode → rank by corroboration strength, not LLM plausibility
  (`corroboration-ranked-review…`); and for *review*, more context degrades detection
  (`more-context-makes-llm-review-worse-not-better`).

## E. Backlog — strong lenses, HOS-design-heavy, validate against corpus before promoting

- **Decorrelated / cross-vendor ensemble review** as load-bearing coverage (single-reviewer recall
  15–31%). (`cross-vendor-review-finds-real-bugs`, `gates-and-review-are-complementary`,
  `oversight-blindspot-documentation-discoverability` — the "N-dimension overseer is blind to
  dimension N+1 and to its own blindness" point is distinctive.)
- **Tiered, cost-aware review economics — "deployability = correctness"**: oversight that is correct
  but uneconomical or unforced *gets turned off*; gate expensive review by transition significance
  (inner-loop/pre-PR/release) with a cheap deterministic trigger. (`three-tier-review-cost-model`,
  `cost-gating-autonomous-oversight-loops`.)
- **Governance invariants** (governance/policy limb): only automation-tightens / human-relaxes
  (`ratchet-principle`); an override with no expiry becomes the policy (`an-override-must-expire…`);
  the recorder must not be in the recorded set; the oversight-*disabling* valve must be more
  auditable than the gates; forge-proof human gate needs identity-separation + server-side
  enforcement (`human-gate-enforcement-limits`); two-key enable.
- **Silent non-execution = clean result**: bypassed/skipped/never-invoked oversight is
  indistinguishable from "reviewed and clean" → force unskippable execution + loud, distinct N/A
  (`orchestrator-absorbs-roles-pipeline-bypassed-by-default`, `explicit-na-audit-entries`). *(Closely
  related to the T0 "enforcement not knowledge" reframe.)*
- **Non-deterministic reviewer convergence** ("pass = zero-NEW, feed it its own issue tracker,
  allow an accept disposition").
- **Interactive vs autonomous = one role, two modes** (governance boundary, not code boundary);
  specify the post-action handoff or the agent bypasses the review loop.
- **(Corpus-seeded, 2026-07-18; ARBITER-VALIDATED same day) Oversight-competence gap — escalation
  without a competent receiver.** The Escalate stage presupposes a human *capable* of judging what's
  escalated; the democratization endgame (non-programmers generating code) removes that
  presupposition. Distinct from `automation-bias` (attention/trust failure of a *capable* human),
  `oversight-theater` (hollow authority), and the scaling inversion (volume vs. inspection): here the
  gap is **capability absence**. **Anchor: `22JBEZNK`** — and the distinction is now
  author-corroborated: the study *controls for* over-reliance (primed distrust, prompts, incentives)
  and its Discussion explicitly rejects overconfidence ("difficulty is rooted in applying domain
  expertise or critical thinking to unfamiliar technical contexts"). All four calibration models
  conflated the two failure modes (unanimous automation-bias primary — Taxonomy_Changelog §16); the
  human separated them. Tripwire: the `non-developer` facet — promote to a theme iff flagged papers
  accumulate *making this argument*; otherwise it's a Discussion point. Don't name it
  "democratization" (phenomenon-name; would keyword-attract adoption papers that belong in
  `survey-input`).
- **(Corpus-seeded, 2026-07-18) Authority-allocation spectrum — "human in absolute control."** A
  recurring *stance*, not yet a tag: not human-in-the-loop of an AI-driven flow but AI-as-tool inside
  a human-commanded flow; the spectrum runs absolute control → bounded delegation → tiered autonomy →
  autonomous+gates. Corpus cluster: Lumen `VG6CIDQW` (developer agency), `JVWUYDME` (Human-in-Command),
  `Z8TPRNEU` (devs deliberately retain control), `ID7IN65K` (authority scoping), Hedwig `T72TU8B5`
  (earned-trust tiers). HOS kin: interactive-vs-autonomous above; ratchet-principle. Likely a
  Discussion *axis* reconstructed from `hitl-workflow` + `oversight-theater` + the `assistive`/`agentic`
  facets rather than a new tag — decide after the sweep.
- **(Corpus-seeded, 2026-07-20) Risk-quantification instrument family.** If the sweep surfaces a
  *cluster* of `metrics` papers whose measurand is prospective risk (vs compliance status, quality,
  coverage) and the Discussion needs them as a roster the tags can't reconstruct, promote a
  dedicated tag then — with the evidence in hand. **Tripwire: `metrics` facet + rationale-measurand
  = risk accumulating.** Until then the family is retrievable as `metrics` + rationale text; the
  object is carried by co-tagged themes (Taxonomy_Changelog §20 — same staging logic as the
  competence gap: tripwire first, tag only on recurrence). Seeds: `R4WJZBSF` (regulatory/ethical
  risk indices, Set B), `ZUM76CCG` (LRF autonomy×impact risk levels, Set C).
- **(Corpus-seeded, 2026-07-20) `expert-validated` form facet — STAGED.** Definition ready-made
  (Taxonomy_Changelog §24): contribution **evaluated by documented expert judgment** (panel /
  Delphi / structured practitioner review, process described as method). **Discriminator: the
  panel judges the *contribution*, not produces the *data*** — experts shaping requirements or
  filtering lit-review findings (input-side, the 6DXZGHD9-era probe) don't count; experts as study
  subjects don't count; ≠ peer review; ≠ undocumented collegial feedback. Would slot between
  `design-only` and `built-system` on the evidence-strength ladder (unvalidated design <
  expert-validated design < built prototype < adopted). **Tripwire: papers where a documented
  panel validates the contribution itself accumulate** — the motivating instance dissolved on
  closer read (its panel was input-side), so the facet waits for a genuine first instance.
- **(Corpus-seeded, 2026-07-20) `benchmark-evaluated` form facet — STAGED.** Own system evaluated
  **under a standardized third-party benchmark's prescribed conditions** (UB2EVUFU on ProjDevBench
  = first genuine instance) — an evidence-strength rung *within* `built-system`: self-tests <
  standardized benchmark < field study < adopted. Deliberately NOT a `method-*` value (that would
  reverse the world-or-tool cut — the results still describe the tool). **Tripwire: built-system
  papers with standardized-benchmark evaluations accumulate** such that the Discussion wants the
  roster ("N of M systems have benchmark-grade evidence") — likely fast, given agentic-systems
  papers' benchmark habits; promote then. ≠ the paper *being* a benchmark study of third-party
  systems (that's `method-experiment`, subjects-may-be-systems rule).

## Grafting checklist (do before classifying cores)
1. Cross-check pass-through corpus papers (Mitropoulos, Ferdous, Charoenwet, Parris, Kumar,
   Watanabe, Loker) against the library → in-corpus? retrieval/snowball candidates?
2. Ground **T3 (untrusted overseer)** on those corpus papers → add to `Emerging_Themes.md`.
3. Fold **A** (enforcement-not-knowledge, task-class-risk, 1.7× caveat) into `Problem_Statement_Evidence.md`.
4. Add **C** (computed-signal-not-self-report) to `slr-conventions` core criteria.
5. Decide which **E** backlog lenses have corpus support → promote or drop.
