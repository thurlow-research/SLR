# Taxonomy iteration log — v0 → current

How the theme-tagging taxonomy evolved through cross-model + human calibration. Each entry:
**disparity observed → diagnosis → change → outcome.** Companion to `Tag_Cheatsheet_v0.md` (the
starting point) and `Tag_Cheatsheet.md` / `Methodology/Emerging_Themes.md` (current).

Method: a 5-tagger panel (Claude **opus**, Claude **fable 5**, **codex** = gpt-5.6-sol, **gemini** =
Gemini 3.1 Pro, **gemini-fast** = Gemini 3.5 Flash) plus a **human**, each tagging the same papers'
full text against the taxonomy. Disagreements were treated as *signals about the instrument*, not noise.

---

## 1. Breadth divergence & "model consensus ≠ human"
- **Disparity (Set A, v0):** themes-per-paper ranged **opus 4.7 · codex 5.0 · fable 2.6 · gemini 2.7**.
  Primary theme was stable (9/10 unanimous), but *secondary* breadth split widely: ~half of all
  secondary tags were asserted by a single model. Only **Opus** reached the "limits-of-oversight"
  themes (`automation-bias`, `oversight-theater`, `tooling-supply-chain`).
- **Key finding:** adding **Fable** (a Claude model) showed it clustered with **Gemini** (Jaccard 0.86),
  *not* with Opus (0.49) — so tagging breadth is a **model disposition, not a vendor/family trait**.
  A naïve model-majority vote would have *dropped* exactly the subtle themes only Opus caught —
  reproducing the project's earlier screening finding that **model consensus ≠ human; Opus ≈ human.**
- **Change:** reinforced *membership-not-mention*; later boundary-sharpening (below) trimmed the long tail.
- **Outcome:** on the refined re-run, breadth converged (**opus 4.7 → 2.5**; all models ~2.3–2.5 except
  codex 4.2), and the "Opus outlier" pattern largely dissolved.

## 2. "Is formal methods really rules-based?"
- **Disparity:** `formal-methods` was lumped inside `rules-based-checks`, conflating *proof-based*
  guarantees with *heuristic* checks — and mislabeling who performs them (AI vs classical engine).
- **Change:** added a **composable `formal-methods` tag**, orthogonal to the *performer* (`ai-review`
  if an LLM does it, `rules-based-checks` if a classical engine does). The composition **encodes an
  adoption hypothesis**: classical+human-authored formal methods = niche; AI-automated (autoformalization)
  = the plausible uptake path.
- **Outcome:** corpus check — only ~4/149 cores foreground formal methods (one a position paper),
  confirming a minor, aspirational thread; the tag now segments it cleanly.

## 3. `framework` vs `governance-frameworks` collision + fuzzy `framework`
- **Disparity:** a human tagged `governance-frameworks` intending "it's a framework" — the two shared
  the word "framework." Separately, the `framework` facet split across taggers (VG6CIDQW 1/4; Hedwig
  human-vs-4-models).
- **Change:** renamed the theme **`governance-frameworks` → `org-governance`** (the org *apparatus* —
  policy, audit logging, accountability); sharpened the **`framework` facet** = a *pipeline-integratable
  technical framework/architecture*, **breadth not required**, excluding bare *point-results*.
- **Outcome:** the two stopped competing (form vs. topic); the VibeGuard/Hedwig consistency case
  clarified that a single-concern architecture still qualifies.

## 4. `remediation-gating` over-tagging
- **Disparity:** a human **and Opus** both tagged VibeGuard (`T8E8SCCG`) `remediation-gating` — but it's
  a *pre-publish gate with no auto-fix*.
- **Change:** sharpened the boundary — **requires an autonomous fix being overseen**; a pure
  detection/publish/quality gate is the enforcement side of the *detector*, not remediation.
- **Outcome:** both the human and Opus dropped it on re-read.

## 5. `risk-routing` ↔ `hitl-workflow` — the persistent primary split
- **Disparity:** the *only* recurring primary disagreements were on this adjacency (Hedwig `T72TU8B5`
  and `UB2EVUFU`), split ~2/3 across models.
- **Diagnosis:** not noise — a **definitional gap**. Both themes co-occur in systems that both *decide
  what to surface* and *provide the control point*.
- **Change:** sharpened the definitions to a mnemonic — **`risk-routing` = WHAT** (what gets surfaced,
  at what tier) vs **`hitl-workflow` = HOW + WHEN** (the human's control mechanism + checkpoint timing) —
  and added a **primary tie-breaker**: primary = the theme carrying the paper's *distinctive novelty*,
  not the standard scaffolding.
- **Outcome (measured):** re-running the four models on Hedwig collapsed the split from **2/3 → 5/5
  unanimous `risk-routing`** (both Opus and Fable *moved*, citing the tie-breaker verbatim), matching
  the human. A clean demonstration that a definitional fix can be *empirically verified* by re-run.

## 6. Scope: general-AI papers slipping into core
- **Disparity:** `M74M3RFJ` (assurance cases for *LLM adversarial robustness* + EU AI Act) was tagged
  `regulatory-compliance` by **all four models** — theme-level in-scope-looking — but its governance
  *object is the model*, not the produced code. The human scoped it out.
- **Change:** added a **`general-ai` scope flag** (governance is general-AI, not coding-specific) and a
  **`demote:context` workflow flag** for batch re-scoping.
- **Outcome:** `M74M3RFJ` demoted **core → context** (core count 149 → 148). Disposition is a human
  judgment the models are weak at — the flag is the tripwire.

## 7. Encoding-scheme consistency
- Made theme membership explicit (`theme:<slug>`) and standardized **primary = `primary:theme:<slug>`**
  (same tail as membership, `primary:` prepended) so calibration tags strip-map to the final convention.
- Menu labels prefixed `theme:` / `facet:` so theme-vs-facet is unmistakable in the tagging UI (which
  had caused the §3 mix-up).

## 8. Facet expansion (artifact / evidence axis)
- Added the composable **`framework` → `built-system` → `adopted`** cluster (form → maturity) to power a
  **proposed-vs-adopted** analysis, plus **`general-ai`**. In the refined Set A: `built-system` reached
  **10/10 all-model agreement**, `adopted` correctly **0/10** (nothing production-deployed) — high-signal,
  objective facets.

## 9. The PROMPT changed too — not only the definitions ⚠️
The full model prompt = **cheat-sheet (definitions) + `# YOUR TASK` block**. Both evolved. The task
block's key change was the **primary tie-breaker instruction**:
- **v0:** *"…choose **ONE primary theme**, and add any facet tags."*
- **current:** *"…choose **ONE primary theme (tie-breaker: the theme carrying the paper's DISTINCTIVE
  CONTRIBUTION/novelty, not standard scaffolding)**, and add any facet tags."*
  (also added: mentions of the `framework`/`built-system`/`adopted` facets and `formal-methods` composition.)

**Confound for the causal claim (§5).** The Hedwig **2/3 → 5/5** convergence combined *two* changes at
once: (a) the sharpened `risk-routing`/`hitl-workflow` **definitions** and (b) the new **tie-breaker
instruction** in the prompt. Because (b) directly instructs the primary choice, it is plausibly the
dominant driver. Accurate framing: *"the refined prompt (definitions + explicit tie-breaker) collapsed
the split"* — **not** "the definitions alone did it." A clean **isolation test** (defs-only vs
tie-breaker-only, factorial on one paper) would separate the two effects.
- v0 prompt preserved verbatim in `Tag_Prompt_v0.md`; current in `Tag_Prompt.md`.

## 10. Generation-mode axis missing (`assistive` vs `agentic`)
- **Gap (2026-07-18):** the corpus mixes two oversight settings — human-initiated,
  suggestion-granularity generation (Copilot-style: oversight = the acceptance moment) vs AI-initiated
  multi-step work at artifact/PR granularity (oversight = the gate) — and no tag separated them. The
  automation-bias evidence lives mostly in the first; the scaling inversion and the
  Detect→Triage→Fix→Escalate solution pipeline mostly presuppose the second. Not recoverable from
  existing tags (`agent-scope-drift` only catches it where drift is the topic).
- **Change:** added the **`assistive` / `agentic` scope-facet pair**, cut on *who initiates + the
  reviewable unit* — explicitly NOT "IDE vs not" (agents live in IDEs). Either / both / neither
  (= unspecified or mode-irrelevant). Additive (no theme redefined), so added **mid-Set-B** under the
  `formal-methods` precedent; Set A model outputs unaffected; calibration papers to be backfilled.
  At the same time the Set B human packet's embedded cheat-sheet was found **stale (v0-vintage:
  `governance-frameworks`, no `formal-methods`, 4 facets)** and refreshed to the current instrument —
  the Zotero Actions menu was already current, and the one paper tagged so far (TF56EPIP) used
  current slugs, so no human tags were affected.
- **Outcome:** pending — pilot on the 20 calibration papers in the post-Set-B iteration. Expected
  high agreement: near-factual property of the study, like `built-system` (10/10 in Set A).

## 11. The Lumen episode — unanimous-model category error; `oversight-explanation` broadened
- **Disparity (2026-07-18):** on Lumen (`VG6CIDQW`, Set A — "developer agency through transparent
  context control"), **all four models chose primary `hitl-workflow` unanimously, and the human
  overturned it.** First unanimity overturn in the calibration — it qualifies the "primary theme is
  essentially solved" finding: unanimity survived a boundary the oversight-vs-steering discriminator
  already covers.
- **Diagnosis:** (a) "context control" pattern-matched to *control surface*, but a lever over the
  AI's **inputs** is **input-side steering**, not oversight of an artifact — none of the four applied
  the steering exclusion there. (b) The human also rejected `provenance-auditability`: a point-in-time
  "what's in use now" view records nothing, so nothing is auditable after the fact. (c) The paper's
  real oversight contribution — human-invoked comprehension — had no sanctioned home:
  `oversight-explanation` was handoff-framed, and the lens-ish "context transparency" clause sat
  inside the otherwise lever-themed `hitl-workflow`.
- **Change:** `oversight-explanation` **broadened to "helping the human understand what the AI is
  doing"** with two manifestations — **push** (system escalates; decision-ready handoff:
  background + options + recommendation + risks) and **pull** (human-invoked visibility into what the
  AI is doing/using). "Context transparency" relocated out of `hitl-workflow` (now levers-only, with
  an explicit lens→`oversight-explanation` boundary); `provenance-auditability` gains the
  record-vs-live-view test; the **input-side steering cue** and a **transparency routing rule** added
  to the preamble and cheat-sheet. Human tags on Lumen: `oversight-explanation` (primary) +
  `assistive` + `built-system` — the day-old `assistive` facet did real work (it explains why no
  handoff exists for the old definition to bite on).
- **Process change:** the **freeze is lifted**. Scott human-tags the calibration papers as a
  *vocabulary-vetting pass*; the summative human-vs-model experiment then runs on the vetted
  instrument (models re-run Sets A+B in fresh contexts; Set A human tags are model-informed, Set B is
  the clean blind comparison). v1-instrument model outputs archived to `data/tags-v1/`.
- **Outcome:** pending the re-run — the decisive check is whether the broadened definition + steering
  cue flips the models' Lumen primary to `oversight-explanation`.

## 12. `steering` + `non-developer` facets (vetting pass, papers 2–3)
- **Gaps (2026-07-18):** (a) steering existed only as an *exclusion* — nothing marked a paper's
  steering component, so exclusion decisions left no audit trail and hybrid steer-and-check systems
  would read as under-tagged in the sweep; `assistive` cannot carry this (mode of the *setting* ≠
  type of the *contribution*). (b) Reading `22JBEZNK`: "non-programmers generating code" — the
  democratization endgame of vibe coding — had no population marker, though it up-ends the Escalate
  stage (escalation presupposes a competent receiver).
- **Change:** two facets. **`steering`** (contribution-type flag; contribution-not-topic guardrail;
  steering-*only* → demote candidate — makes the `spec-driven-guardrails` resolution enforceable,
  parallel to `general-ai`). **`non-developer`** (population scope flag; default = professional
  devs), completing the scope axes: mode (`assistive`/`agentic`) · object (`general-ai`) ·
  population (`non-developer`). The *argument* (oversight-competence gap) is staged in
  `HOS_Seeded_Theme_Candidates.md`, NOT made a theme (n=1; `non-developer` is its tripwire —
  promote if flagged papers accumulate making the argument). Facets 10 → 12; menu 28 → 30 actions.
- **Open:** whether Lumen `VG6CIDQW` carries `steering` is disputed (Scott: the human curating the
  assistant's context may be agency/comprehension, not generation-shaping) — under discussion; Lumen
  deliberately NOT cited as a `steering` example pending resolution.
- **Outcome:** pending the sweep (facet counts + whether the competence-gap candidate promotes).

---

### Headline for the writeup
The taxonomy improved **measurably** as a *validated instrument*: disagreements were used diagnostically,
each fix was re-tested, and the sharpest result — the `risk-routing`/`hitl-workflow` definitional
refinement — converted a persistent **2/3 model split into 5/5 unanimity aligned with the human**.
Cross-model tagging behavior is a **model disposition, not a vendor trait** (Fable≈Gemini), and **model
consensus does not substitute for human judgment** on breadth and scope.
