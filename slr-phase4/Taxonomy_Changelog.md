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
- **Resolved (same day):** after weighing the ground-of-the-act test (quality knob = steering vs
  trust/risk input-gating = supply-chain-kin vs incidental control), Scott confirmed **controlling
  the input is steering, and it's a big part of Lumen** — Lumen is now the facet's worked example;
  the §11 "input-side steering" diagnosis stands unchanged. The ground-of-the-act test itself is the
  reusable rule: input *curation for output quality* = steering; input *vetting on trust/provenance
  grounds* = `tooling-supply-chain` territory.
- **Outcome:** pending the sweep (facet counts + whether the competence-gap candidate promotes).

## 13. The Z8TPRNEU probe — object-of-mechanism rule; drift boundary; steering amendment
- **Disparities (2026-07-18):** on "Professional Software Developers Don't Vibe, They Control":
  (a) 3 of 4 models tagged `agent-scope-drift`; the human rejected it — the paper documents *control
  practices*, with drift only the tangential *motivation*; the Tag reference itself was citing
  Z8TPRNEU as a drift **example**, encoding the over-broad reading. (b) The human applied `steering`
  to a *descriptive* practices paper, an unanticipated use (the facet was defined on *proposed*
  solutions). (c) The human initially read `ai-review` as "AI code review" — slug connotation
  narrower than the written scope (which covers agent-checks-agent by the locked §T3-dissolution
  decision); watch whether models repeat this in the re-run before adding a clarifier.
- **Change:** the **object-of-mechanism rule** — *tag by the object of the mechanism, not the
  motivation of the actor* — added to `agent-scope-drift`'s Boundary with a worked pair: positive
  (multi-agent panel checking code scope vs spec scope → drift + `ai-review`, the object+performer
  composition grammar) and negative (Z8TPRNEU's retained control → `hitl-workflow` only; removed from
  the drift example roster, converted to counter-example). Captures tail tightened: "keep them in
  scope" → "detect or bound departure from intent" (the old wording could absorb any control
  mechanism). `steering` facet amended: "proposed solution **or documented practice** operates on
  generation."
- **Outcome:** human tags on Z8TPRNEU: primary `hitl-workflow` (matches 4/4 models) + `ai-review`
  (sides with codex alone — breadth data point) + `agentic`/`steering`/`survey-input`. Re-run check:
  do fable/gemini/codex drop `agent-scope-drift` under the counter-example?

## 14. The UB2EVUFU probe — error-condition handback; process gates; plumbing rule; coder fatigue
- **Disparities (2026-07-18):** on "Self-organizing multi-agent systems for continuous software
  development": (a) the human's primary `ai-review` resolved Set A's original v1 split **3 models +
  human vs Opus** (`hitl-workflow`) — the tie-breaker's "distinctive novelty, not scaffolding" applied
  by the arbiter. (b) The human initially tagged `risk-routing` for "agent fails → escalates to
  human," then **self-corrected**: an error-condition handback is an exception path, not a
  discretionary triage decision. (c) Three models tagged `rules-based-checks`; a full-text scan
  confirmed tests appear only as the agents' *instruments* — pattern-matched plumbing. (d) The
  human's first-pass tag set had several oversights (facets missed), corrected on a second look —
  self-diagnosed **"dinner fatigue."** With 29 tags per paper, recall-based tagging degrades with
  coder fatigue; this is a *reliability factor of the human instrument*, not just an anecdote.
- **Change:** `risk-routing` boundary — **error-condition handback is NOT routing** (mechanism →
  `hitl-workflow`; failed-fix loop → `remediation-gating`). `remediation-gating` Captures — **two
  gate kinds**: content (filter fix candidates) and **process** (bounded retries / budget-decay /
  stop-progression, fail-closed; UB2EVUFU's budget-halving cycles = worked example). Preamble +
  cheat-sheet — **"plumbing ≠ membership"** rule for systems papers (UB2EVUFU's test-running agents
  as counter-example). Workflow — **five-question facet checklist** (role · form · scope · mode ·
  contribution) so facet coverage is mechanical, not recall-dependent; packet gains the same
  checklist + a second-look verification habit.
- **Outcome:** human final set: primary `ai-review` + `hitl-workflow`/`provenance-auditability`/
  `remediation-gating` + `agentic`/`built-system`/`framework`/`steering`. Re-run checks: do models
  stop tagging `rules-based-checks` here, and does Opus's primary move to `ai-review`?

## 15. The F9JM9CI6 probe — `counterpoint` + `general-code` facets; mode-pair clarifier
- **Gaps (2026-07-18):** on "Support, not automation" (AI-supported review *prep* — agents generate
  higher-level code descriptions for the reviewer): (a) nothing captured **stance polarity** — the
  paper argues *against* review-automation maximalism, and the earmarked "contrarian hunt" had no
  operationalization; (b) nothing captured the **object-of-oversight** — the mechanism targets code
  review *generally* (the reviewed code isn't AI-authored; the AI sits on the review side only), so
  on tags alone the paper reads broader than it is; (c) the human tagged mode twice, reversing
  (`assistive` → `agentic`), because both slugs invite readings the definition doesn't support
  ("uses agents", "AI assists the human").
- **Change:** **`counterpoint`** role facet (argues against a prevailing position; direction-agnostic,
  rationale records what's opposed; Discussion-balance + confirmation-bias defense).
  **`general-code`** scope flag (object = code generally, not AI code; transfers but wasn't
  developed/evaluated on AI code), completing the wrong-object family: `general-ai` (model) ·
  `general-code` (any code) · `non-developer` (population) · `steering` (contribution). Mode-pair
  **clarifier**: the pair describes the *generation* studied — AI only on the review/oversight side
  → tag *neither*. Facet checklist updated (role +counterpoint; scope +general-code). Facets 12 → 14;
  menu 30 → 32 actions.
- **Narrowness ruling:** the paper's thin scenario (review-prep only) is **extent, deliberately not
  tagged** — carried by primary, rationale, child note, and the withheld `framework`/`built-system`;
  a narrowness scalar would have poor reliability (every paper is narrow along some axis).
- **Outcome:** F9JM9CI6 expected final set: primary `ai-review` + `oversight-explanation`/
  `risk-routing`; facets `intro-framing` + `counterpoint` + `general-code`, **no mode facet**
  (`agentic` removed). Re-run check: do models apply `general-code` instead of a mode facet here?

## 16. The 22JBEZNK overturn — capability vs bias; the second unanimous-model error
- **Disparity (2026-07-18):** all four models tagged `automation-bias` as unanimous primary on the
  paper the Tag reference itself cited as the theme's example. The human tagged no automation-bias at
  all. Full-text read vindicated the human decisively: the study **controls for over-reliance**
  (primed distrust, explicit error-hunting prompts, monetary incentives) and its Discussion
  **explicitly rejects overconfidence** — "the difficulty is rooted in applying domain expertise or
  critical thinking to unfamiliar technical contexts." The models pattern-matched "missed flaws even
  when warned" — but the warning was the experimental *control*, not the finding.
- **Change:** `automation-bias` Boundary gains the **capability discriminator** (the failing human
  must be *capable*; can't-evaluate → the oversight-competence gap); 22JBEZNK moves from example to
  boundary counter-example; the **oversight-competence-gap candidate upgrades** to arbiter-validated
  + author-corroborated, 22JBEZNK its anchor. Mode-pair gains the **tie-rule** (initiator vs
  reviewable unit disagree → the reviewable unit dominates; human-prompted complete-artifact = the
  gate = `agentic`). Human also self-corrected `risk-routing` off ("how humans respond to raised
  risks," not triage).
- **Outcome:** second unanimity overturn (after Lumen), and the more damning: the models tagged the
  mechanism the paper explicitly rules out. Re-run check: does the discriminator flip them?

## 17. Set A audit — VibeGuard recurrence, demote signature, salience bias, anchor bar
- **VibeGuard (`T8E8SCCG`) recurrence — the compression-gap proof.** The human re-applied
  `remediation-gating` to VibeGuard — the *same documented error* (§4) whose exclusion was written
  from his own earlier mistake. Root cause is mechanical, not cognitive: the exclusion lived only in
  `Emerging_Themes.md`; the compressed cheat-sheet (what the tagger actually works from) never
  carried it, and the §14 process-gate broadening made the line *more* inclusive. **Principle now
  enforced: every boundary that has ever caught a human must appear in the compressed instrument.**
  Tag removed; exclusion added to all copies.
- **The demote signature, validated twice.** `2CKL96B8` (narrative stat-assembly; primary struggle)
  and `UDVHQ5HR` (LLM-judge capability benchmark; definition-stretching to `quality-debt`) both
  flagged `demote:context` — matching the `VP7TS6CX` worked call (tool-capability benchmark →
  context) and the secondary-lit rule. **Workflow cue added:** struggle to pick a primary /
  stretching a definition = check the core bar, don't force tags. With M74M3RFJ, the calibration
  sample has produced **3 demotes / 10 papers** — the sweep should expect a substantial demote tail
  (the tagging pass doubles as a scope audit).
- **Salience bias (models).** Models anchor on a paper's most vivid section: `2CKL96B8` primary
  ai-code-insecurity from its security-stats section (secondary-lit primary = **biggest-tent** theme
  now conventioned); 4 `problem-statement-anchor` applications by impressiveness rather than bar.
- **`problem-statement-anchor` bar set:** must anchor the OVERALL problem statement — not a
  sub-argument or population-specific stat, however vivid; never on `lit-review` (secondhand — chase
  primaries). Human's zero-anchors-in-10 recorded as the considered bar. `lit-review` clarified:
  structure not required (systematic OR narrative; test = synthesized-not-produced).
- **Outcome:** Set A human pass complete — all 10 papers tagged, verified, and adjudicated; ~20
  instrument products across §10–§17 from six probe papers + this audit.

## 18. Instrument-critique panel + known-answer dry-run → v2 revision
- **Dry-run (2026-07-18):** 5 blind fresh-context Fable taggers applied the instrument to the 10
  adjudicated Set A papers: **8/10 primary match; all four regression checks passed** (Lumen flip,
  VibeGuard exclusion, 22JBEZNK not-bias with the discriminator cited verbatim, tie-rule applied by
  name). Residual fixes: flags field, steering materiality, binding biggest-tent, ai-review practice
  clause. The two primary misses: 2CKL96B8 (biggest-tent non-binding) and F9JM9CI6 (the new
  ai-review↔oversight-explanation adjacency).
- **Panel (same day):** Fable 5 + GPT-5 Codex (high) + Gemini 3.1 Pro (High), fresh contexts, frozen
  input (instrument + Tag reference + Set A dev set with human tags only; input generator committed,
  artifact gitignored). ~40 findings; verdicts converge on "one revision cycle, then sweep." Full
  merged table: `data/critique/DISPOSITION.md`. Known-answer synthesis: theme-level calls are
  *forced* by the text; facet/flag-level calls mostly only *permitted* → divergence risk lives in
  facets/flags, mirroring Set A's breadth noise.
- **Applied (v2):** all A-group schema fixes (demote trigger list corrected — `general-code` is NOT
  a demote reason; criteria unified; bare-slug primary governs; flags vocabulary enumerated incl.
  `insufficient-input`); all B-group compression-gap restorations (computed-signal rule,
  framework point-tool exclusion + adoption test, dependencies clause, Detect dual-tagging,
  formal-methods third composition, intro-framing qualifier, Hedwig tie-break exemplar); all C-group
  sharpenings (oversight-explanation gains the **standing** mode — modes illustrative, headline
  governs; documented-practice clause generalized; biggest-tent operationalized; provenance record
  must serve *human* review; thin-input floor; insecurity evidence bar; vision-paper membership
  floor; survey-input substantiveness; competence-gap keep-core note); scope flags regrouped.
- **Arbiter rulings encoded:** **D1 plan-gate rule** (designed lifecycle checkpoint = hitl-workflow;
  conversational guide-then-go = steering). **D2 who-checks-what decomposition** with the HOS release
  cycle as worked example (HOS: Thurlow, S. (2026). HumanOversightSystem (Version 0.5.0) [Computer software]. Purdue University. https://doi.org/10.5281/zenodo.21347272) (producer self-checks = no theme; independent evaluation = detector by
  epistemics; severity + cross-model agreement = risk-routing on a computed producer-independent
  signal; fix approval/escalation + refix-loop governance = remediation-gating). **D4 (arbiter final, superseding the
  proposed split): dependency risk in generated code → ai-code-insecurity**; tooling-supply-chain
  keeps the AI tooling + attacks on the reviewer.
- **D3 RESOLVED (Scott, 2026-07-18) — the Jidoka ruling.** `remediation-gating` = the system fixes
  **autonomously, without per-fix human involvement**, kept safe by machinery (content/process
  gates, convergence, fail-closed stops); `risk-routing` **layers on top** to engage the human only
  when absolutely required — the andon cord. Risky-fix escalation to a human is therefore *routing*,
  not remediation (corrects a comingling in the first-draft worked example). **Human-approves-every-
  fix is NOT remediation-gating**: review-everything is the unscalable anti-pattern the review
  exists to move past (attention collapse); a paper *advocating* it is a `counterpoint` candidate —
  and *introducing* automation-bias risk by design is a rationale-level critique, distinct from
  `automation-bias` membership (which requires *studying* the failure). **Instrument FROZEN as v2**
  → Set A retag (improvement gate) → Set B.
- **Set A retag under v2 (2026-07-18, three fresh models):** improvement across every metric —
  primary fable 6/10→8/10, codex 6→7, gemini 6→7; theme Jaccard .50–.66 → .67–.78; **facet Jaccard
  roughly doubled** (.34–.42 → .61–.70); demote flags 8–9/10 correct. Both v1 unanimity errors
  (Lumen, 22JBEZNK) now called correctly by all three. Residual misses concentrate in 3 papers:
  2CKL96B8 (all three follow the *operationalized* biggest-tent to ai-code-insecurity — **resolved:
  human re-adjudicated to ai-code-insecurity**, conceding the original ai-review primary stretched
  that theme's definition; a case of the written rule out-performing the recorded intent), F9JM9CI6 (**resolved: human re-adjudicated to
  oversight-explanation** via the new **altitude refinement** — primary = most specific theme still
  capturing the paper's main effort; guard: a component mechanism doesn't outrank the broader
  contribution, so UB2EVUFU stays ai-review), UB2EVUFU
  (codex+gemini overcorrect to primary remediation-gating after the D2/D3 text raised its salience;
  gemini violated the then-unstated primary∈themes constraint).
- **Altitude-rule regression test (2026-07-18, latest):** 3 papers × 3 fresh taggers under the
  updated instrument — **8/9**. Flip-check UB2EVUFU: **codex flipped back to ai-review** (the guard
  worked; rationale decomposes per the rule); fable held correct. Hold-checks: F9JM9CI6
  oversight-explanation 3/3, Hedwig risk-routing 3/3 (nothing destabilized). Gemini's schema
  violation is gone (primary now in themes). **Residual: gemini kept remediation-gating on UB2EVUFU
  despite the compressed copy naming that exact case verbatim** — model non-compliance, not a
  wording gap; recorded as a gemini signature (v1 conservative floor → schema violation → ignores
  named worked example). Sweep implication: gemini primaries on multi-mechanism systems papers get
  the human check the design already prescribes.
- **Round-2 smoke test (fresh Fable, v2 text only): 10 revision-introduced defects found & fixed** —
  primary∈themes schema line added; best-effort-primary-when-demoting contradiction resolved;
  task-block demote copy restored the benchmark-evaluating-a-contributed-system carve-out; stale
  tag count; steering splice regrammared; formal-methods intro-framing marked as *facet*; rationale
  coverage specified; primary triple-definition cross-referenced; demote:discard given criteria;
  remediation-gating density split (anti-pattern note → sub-bullet). Cross-references verified clean.

## 19. `design-only` facet — positive marker for proposed-not-built (the R4WJZBSF probe) → v2.2
- **Gap (2026-07-19, Set B pass, paper 10):** R4WJZBSF proposes a four-metric ethical-risk framework
  whose "production-ready Google Colab implementation" fabricates its core outputs — EG and ADS are
  literal `np.random` draws, the results table reproduces the mock's hard-coded probabilities
  (ADS 60% = `p=[0.6, 0.4]`), BPI is substring matching despite the claimed BERT semantics, and the
  Methodology's validation claims (κ=0.72, 90% precision, three institutions) have no corresponding
  artifact. The human's blind read correctly saw "proposing, not building" but **reached for
  `intro-framing` to record it** — a definition stretch (intro-framing = names the gap, NO mechanism;
  this paper operationalizes formulas/thresholds/architecture) that also contradicted his own
  `framework` tag. Classified per §7 method step 2a: uncaptured concept, recurring (the
  unbuilt-proposal shape shows up repeatedly in the corpus), and no reasonable broadening holds it —
  broadening `intro-framing` would destroy its no-mechanism boundary, and absence of `built-system`
  is ambiguous three ways (not applicable vs tagger miss vs genuinely unbuilt).
- **Change:** added **`design-only`** form facet — mechanism **specified in buildable detail but
  never credibly run** (no working implementation, no evaluation on the intended object); **a mock
  demo that fabricates the mechanism's core outputs ≠ building** (R4WJZBSF worked example); applies
  only to papers that *propose* something; mutually exclusive with `built-system`/`adopted`,
  composes with `framework`; ≠ `intro-framing` (discriminator = buildable detail). Completes the
  maturity spectrum intro-framing → design-only → built-system → adopted. Disposition tripwire
  (parallel to steering-only / `general-ai`): design-only *solution* paper → the
  unevaluated-framework context discriminator → check the core bar. **Slug chosen over `proposal`**
  (every solution paper "proposes" — slug-connotation over-fire risk, the `ai-review` lesson §13).
  Facets 14 → 15; menu 32 → 33 (re-import pending); all four instrument copies updated in this
  commit (cheat-sheet, prompt, Set B packet, Tag reference). Additive mid-Set-B under the §10
  precedent — no theme redefined; Set B papers 1–9 untouched. **Instrument = v2.2.**
- **Comparability note:** R4WJZBSF's blind first-read human tags were snapshotted (Zotero v156638)
  *before* the audit dialogue that produced this facet — the paper is Set-A-style
  "blind first read + model-aware adjudication"; Set B papers 1–8 (untagged) remain fully clean.
- **Outcome:** pending — Set A backfill piloted post-Set-B (expected sparse: VibeGuard/Hedwig/
  Lumen/UB2EVUFU all built; F9JM9CI6 stays intro-framing unless its vision meets the
  buildable-detail bar). Re-run regression pair: R4WJZBSF design-only vs the built systems; watch
  codex for over-fire (breadth signature) and check the facet behaves like the near-factual
  `built-system` (10/10 in Set A). **2026-07-20 backfill:** `M74M3RFJ` confirmed the second
  design-only (GSN assurance-case framework, exemplars only, engine = future work) — design-only
  ON, intro-framing OFF per the contradiction rule; also reconciled: restored to the 01-AI
  Calibration collection (the calibration roster is frozen experiment infrastructure, orthogonal to
  disposition) + retroactive `demote:context` (its 2026-07-15 demotion predated the flag mechanism).
  F9JM9CI6: **RULED design-only (Scott, 2026-07-20 — overriding the assistant's stays-intro-framing
  assessment; §23)** — a stated architectural-design contribution meets buildable detail even with
  realization deferred to a research agenda; intro-framing off per the contradiction rule. The
  other seven calibration papers: four built, three propose nothing — facet correctly inapplicable.

## 20. `metrics` facet + risk-routing signal boundary (R4WJZBSF follow-on) → v2.3
- **Gap (2026-07-20, Set B pass):** R4WJZBSF defines four regulatory/ethical-risk indices with
  essentially no discussion of what to do with them — no allocation decision. The human's blind
  primary was `risk-routing`: with no home for a metric-definition contribution, the
  nearest-sounding theme absorbed it — and model salience bias will replicate that stretch at sweep
  scale (many papers define scores). Brainstorm considered a composable pair — `risks` ("talks
  about risks") + `metrics` — mixing to capture essences like "risk metrics" / "oversight metrics."
  **`risks` REJECTED:** a mention-level criterion in a governance corpus (near-100% base rate, zero
  discrimination; "risk" is a worse word-collision hazard than "framework"/"transparency," which
  get routing rules, not tags). The mixing falls out for free from `metrics` × the co-tagged
  themes: +`regulatory-compliance` = compliance-risk metrics, + an oversight theme = oversight
  metrics (Scott's own worked example), +`quality-debt` = quality metrics, +`risk-routing` =
  metrics that drive allocation.
- **Change:** **`metrics`** contribution flag — defines metrics/scores/indices **as a deliverable**
  (defines-vs-uses guardrail: an evaluation apparatus earns nothing; contribution, not apparatus);
  object supplied by co-tagged themes; composes with `design-only` (defined, never run on real
  data) or problem themes (defined AND applied → findings earn the theme, facet marks the
  instrument); **rationale must name the measurand** (the residual "measures *prospective risk*"
  nuance lives there — per the F9JM9CI6 narrowness precedent, below tag altitude).
  `risk-routing` Boundary += **defining a risk metric/score without the allocation decision is NOT
  routing** → `metrics` facet; define-AND-route gets both. Staged candidate:
  **risk-quantification instrument family** (`HOS_Seeded_Theme_Candidates.md`) — promote only if
  the sweep surfaces a cluster the tags can't reconstruct; tripwire = `metrics` + rationale-measurand
  = risk accumulating. Facets 15 → 16; menu 33 → 34 (re-import pending); all copies in lockstep.
  **Instrument = v2.3.**
- **Adjudication (Scott, 2026-07-20):** R4WJZBSF's measured risks are regulatory/ethical, so
  `regulatory-compliance` correctly carries the object — expected final set: primary
  `regulatory-compliance`, facets `metrics`+`framework`+`design-only`; Scott executes the toggles
  himself; §7 log updates on verification. If `risk-routing` drops there, the blind primary becomes
  the boundary's first logged catch.
- **Outcome:** pending — Set C's first member `ZUM76CCG` (LRF: autonomy×impact → oversight levels)
  exercises this boundary from the AI-first side (it plausibly routes, not just measures — a good
  contrast case); watch whether models stretch `risk-routing` on metric-definition papers in the
  Set B run.

## 21. `risk-ip` + `risk-bias` risk-type flags — the harms axis (→ v2.4)
- **Gap (2026-07-20, R4WJZBSF follow-on):** the synthesis needs a **risk-types ×
  identified/mitigated matrix** — which harms the corpus recognizes, which have actual mechanisms;
  the gap cells (identified-but-unmitigated) are Discussion findings. The theme spine organizes
  *mechanisms*, not *harms*; four risk types have theme columns (security / quality / over-reliance /
  explainability-deficit) but **IP/plagiarism and code-bias have no home**, and rationale free-text
  can't be queried into a matrix. Arbiter reports informal recurrence of IP risk across the corpus;
  HOS ships an IP scanner (experiential corroboration — kin, not driver). The §20 measurand
  tripwire was designed to wait for recurrence; the arbiter ruled it has effectively fired for
  these two types.
- **Change:** **`risk-ip` / `risk-bias`** risk-type flags. **Substantive-treatment bar** (defines a
  metric for it · contributes/evaluates a mitigation · reports an empirical result · focal
  analysis; an intro risk-list sentence = mention, no tag); **scoped to homeless types only** —
  themed risks get no flag (saturation guard; the same reason the generic `risks` facet was
  rejected in §20). A **deliberate, bounded exception to membership-not-mention**, justified by the
  synthesis axis it serves. Extensible on the same bar (privacy = likely third); promotion path:
  contribution-level cluster → theme, definition ready-made. Facet checklist gains a sixth
  question (**risk-types**); stale "31 tags" count corrected to 35. Facets 16 → 18; menu 34 → 36
  (re-import pending); all copies in lockstep. **Instrument = v2.4.**
- **Outcome:** pending — R4WJZBSF earns both flags (PRS/BPI are *defined metrics* for the two
  types — passes the bar via its first clause). Watch model compliance with the substantive bar in
  the Set B run: intro risk-lists are salience bait (codex breadth signature especially).
  **Superseded same day by §22** — the family went uniform.

## 22. Risk-flag family made uniform; explainability routed by object (→ v2.5)
- **Disparity (2026-07-20, same-day probe of §21):** the arbiter pressed the homeless-only scoping
  from three angles and it failed the smell test each time: (a) "measures IP risk" was
  tag-queryable but "measures quality debt" was not (rationale-text only); (b) matrix columns
  carried **heterogeneous inclusion bars** (flag columns = define-level; theme columns =
  study-level) — a methods-validity objection a committee could land; (c) the human's own
  R4WJZBSF over-tags (`automation-bias`, `oversight-explanation` off its ADS/EG metric definitions)
  showed taggers *will* reach for the theme when define-level treatment has no tag home. The §21
  parsimony argument (avoid theme/flag redundancy) lost to uniformity: the real saturation guard
  was always the substantive-treatment bar, not the scoping.
- **Change:** **`risk-security` + `risk-quality` + `risk-overreliance` added** → one five-flag
  family, one bar (metric · mitigation · empirical result · focal analysis; intro-lists never
  count; rationale cites the fired clause). **Co-occurrence grammar:** flag = substantive
  engagement, theme = the lift; heavy-lift papers carry both. Matrix = one query per column, one
  bar; §21's rationale-text reconstruction retired. **Explainability three-way routing** encoded
  (human-catch: the arbiter almost mapped EG → oversight-explanation): judging-support →
  `oversight-explanation` · **code comprehensibility → quality** (quality-debt Boundary + flag) ·
  model-XAI → `general-ai`; "explainability" joins the route-by-object word list. **Measurand
  vocabulary fixed** (security · quality · comprehensibility · over-reliance · ip-plagiarism ·
  bias · compliance · privacy). **Define-only ≠ theme-membership** stated explicitly in the
  compressed copies (compression-gap principle; first catch R4WJZBSF). Facets 18 → 21; menu
  36 → 39 (re-import pending); all copies in lockstep. **Instrument = v2.5.**
- **Adjudications encoded (Scott, 2026-07-20):** R4WJZBSF flags = risk-ip + risk-bias +
  risk-quality + risk-overreliance (all four metrics define-level); themes `automation-bias` and
  `oversight-explanation` come OFF (define-only; wrong object respectively). Both then-pending
  rulings (what+how core-bar carve-out; F9JM9CI6 design-only) were **confirmed by Scott the same
  day → §23**.
- **Outcome:** pending — the Set B model run tests bar compliance on five flags (risk-security =
  codex salience bait); Set C's ZUM76CCG tests define-vs-route from the AI-first side.

## 23. Two arbiter rulings: the what+how core-bar carve-out; F9JM9CI6 = design-only (→ v2.6)
- **Ruling 1 — what+how carve-out (Scott, 2026-07-20).** A paper that **names the risk/quality
  elements to track AND defines operationalizable metrics for tracking them** (full specification:
  formulas/thresholds/tools) **clears core bar (2) as measurement, even unevaluated**. Rationale
  (as pressure-tested): instrumentation *specification* is solution characterization — the Triage
  stage's computed producer-independent signals have to come from somewhere — not mere
  applicability; "value to the survey" is explicitly NOT the rationale (survey-input papers have
  value at context tier). This **amends the 2026-07-13 trap clause** ("do the measuring or the
  gating") — defining the instrumentation now counts as doing solution-work. Back-catalogue
  checked: no prior call flips (VP7TS6CX/DPKKMXSA/UDVHQ5HR/2CKL96B8/M74M3RFJ demote reasons all
  untouched). Class consequence accepted: what+how metric papers stay core with
  `design-only`+`metrics` as markers; what-only enumerations and borrowed-metrics papers remain
  context candidates; demote stays reserved for its listed triggers. Encoded in: `slr-conventions`
  quick discriminators, `SLR_Status_Update_2026-07-08.md` §3 (dated amendment), the `design-only`
  line in all compressed copies. First application: **R4WJZBSF kept core, no demote** (the paper's
  fabricated-evaluation problem is documented by `design-only`'s mock-demo clause; quality ≠ tier).
- **Ruling 2 — F9JM9CI6 = `design-only` (Scott, 2026-07-20, overriding the assistant's
  assessment).** A **stated architectural-design contribution** (F9JM9CI6 §3: AI-OS-based review
  platform architecture) **meets the buildable-detail bar even when the authors defer realization
  to a research agenda**; `intro-framing` comes off per the contradiction rule (`counterpoint` +
  `general-code` retained; no mode facet — unchanged). F9JM9CI6 becomes the *inclusive*-side
  worked example of the design-only/intro-framing boundary (R4WJZBSF = the mock-demo side;
  genuinely mechanism-free gap-naming papers remain intro-framing). Zotero updated (design-only
  added 2026-07-20 after a concurrent-edit check — Scott had removed intro-framing; the audit of
  all 10 calibration items found no other drift). **Instrument = v2.6** (text-only; menu unchanged
  at 39).
- **Outcome:** pending the re-run — watch whether models apply design-only to F9JM9CI6-class
  visions (stated-architecture clause) without over-firing on pure position papers.

---

### Headline for the writeup
The taxonomy improved **measurably** as a *validated instrument*: disagreements were used diagnostically,
each fix was re-tested, and the sharpest result — the `risk-routing`/`hitl-workflow` definitional
refinement — converted a persistent **2/3 model split into 5/5 unanimity aligned with the human**.
Cross-model tagging behavior is a **model disposition, not a vendor trait** (Fable≈Gemini), and **model
consensus does not substitute for human judgment** on breadth and scope.
