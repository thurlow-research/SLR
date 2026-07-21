# Handoff — Model Calibration via Human Tagging + Cross-Model Validation
## Context pack for the prompt-optimization assignment (case: Hedwig)

**Vibe Coding Governance SLR · 2026-07-21 · for use with Claude Desktop**
**Assignment scope: optimizing the tagging prompt, with the Hedwig paper (`T72TU8B5`) as the case
study.** This doc is self-contained: everything needed to write about how the instrument was
calibrated, what changed in the prompt, and what effect each change measurably had.

---

## 1. The task being prompted

A systematic literature review on human oversight of AI-generated code tags each paper against a
controlled vocabulary (currently **17 themes + 27 facets**, instrument v2.13). Themes follow a
Detect→Triage→Fix→Escalate pipeline spine. Each tagger (human or model) reads the **full paper
text** and returns: one **primary** theme (the paper's home), all theme **memberships**
("membership, not mention" — the paper must *contribute to* the theme's argument), applicable
facets, optional flags, and a ≤12-word rationale per tag, as strict JSON.

**The prompt** = a compressed vocabulary cheat-sheet + a `# YOUR TASK` block, prepended to the
paper's full text. Four copies of the instrument exist (model prompt, human cheat-sheet, human
packet, full Tag reference) and are kept **in lockstep — copy drift is a named instrument bug**.
Files: `slr-phase4/Tag_Prompt.md` (current), `Tag_Prompt_v0.md` (original, preserved verbatim for
before/after comparison), `Methodology/Emerging_Themes.md` (full reference).

## 2. Calibration design (three sets, one arbiter)

20 core papers sampled reproducibly (`random.seed(714)`) into two sets, plus a third defined later:

- **Set A (10) — models first.** A 5-tagger panel (Claude Opus, Claude Fable 5, GPT codex, Gemini
  Pro, Gemini Flash) tagged blind under the v0/v1 instrument; disagreements were treated as
  **signals about the instrument, not noise**. The human then tagged all 10 as a
  *vocabulary-vetting pass* — every place the vocabulary resisted produced a definition change.
- **Set B (10) — human first, blind.** The human tagged with no model tags in existence
  ("co-tagging": an AI assistant QA'd each set *after* the blind read; blind snapshots preserved;
  the human performed all tagging judgment, the AI only audit).
- **Set C — AI-first pilot.** Models tag first, human validates — the production workflow
  rehearsal.

**Governing doctrine (validated repeatedly): model consensus ≠ correctness.** Two papers where
**all four models were unanimous** were overturned by the human on full-text grounds (Lumen
`VG6CIDQW`: input-side steering misread as a control surface; `22JBEZNK`: a capability gap misread
as automation bias — the paper *controls for* over-trust and rejects it). Both overturns happened
at *blind* first read. The human is the arbiter; critique and consensus propose, the arbiter
disposes.

**The iteration loop** (logged per-entry in `slr-phase4/Taxonomy_Changelog.md`, §1–§30):
*disparity observed → diagnosis → instrument/prompt change → outcome measured by re-run.* Thirty
logged iterations took the instrument v0 → v2.13 in one week.

## 3. THE HEDWIG ARC — the assignment's centerpiece

Hedwig (`T72TU8B5`) is a dynamic-autonomy system: a learned classifier decides which coding-agent
actions require a human check-in. It sits exactly on the adjacency between two themes:
`risk-routing` (the allocation decision — WHAT gets surfaced) and `hitl-workflow` (the human's
control surface — HOW/WHEN the human acts).

1. **v0 disparity:** the only *recurring* primary disagreement in Set A was on this adjacency —
   Hedwig split ~2/3 across models (some chose risk-routing, some hitl-workflow). Diagnosis: not
   noise but a **definitional gap** — both themes genuinely co-occur in systems that both decide
   what to surface and provide the control point.
2. **The fix (two changes at once — remember this):**
   - *Definitions:* sharpened to a mnemonic — **`risk-routing` = WHAT** (what gets surfaced, at
     what tier) vs **`hitl-workflow` = HOW + WHEN** (the control mechanism and checkpoint timing).
   - *Prompt task block:* added an explicit **primary tie-breaker instruction** — "the theme
     carrying the paper's DISTINCTIVE CONTRIBUTION/novelty, not standard scaffolding."
3. **Measured outcome:** re-running the models collapsed the split **2/3 → 5/5 unanimous
   `risk-routing`**, with models *citing the tie-breaker verbatim* in their rationales. The human
   later independently confirmed `risk-routing` (calibration log §7 row 5 — the instrument's first
   "no-change probe": it held on its previously hardest case).
4. **⚠️ The documented confound (changelog §9) — this is the assignment's opening.** Both the
   *definitions* and the *task-block instruction* changed between runs. Because the tie-breaker
   directly instructs the primary choice, it is plausibly the dominant driver. The honest claim is
   "the refined prompt (definitions + explicit tie-breaker) collapsed the split," NOT "the
   definitions did it." The changelog explicitly proposes the missing experiment: **a factorial
   isolation test — defs-only vs tie-breaker-only vs both — on Hedwig-class papers.** That is a
   ready-made prompt-optimization study design.
5. **Stability:** in the v2.13 panel (2026-07-21), all three standing models (opus, codex, gemini)
   again chose `risk-routing` on Hedwig. The fix has now survived four instrument versions and a
   near-doubling of the facet vocabulary.

## 4. The validation machinery (what "calibrated" means here)

- **Known-answer dry-run:** 5 fresh-context taggers applied the instrument to the 10 adjudicated
  Set A papers; 8/10 primaries + all four regression checks passed; the 2 misses each produced a
  wording fix.
- **Instrument-critique panel:** three frontier models (fresh contexts, frozen input, human tags
  only) critiqued the instrument text (~40 findings). Critique taxonomy: (a) ambiguity/omission →
  fix; (b) disagreement with an adjudicated boundary → recorded, **arbiter's call stands**
  (otherwise the loop re-tunes toward model consensus — the known-wrong target).
- **Round-2 smoke test:** a fresh tagger run over the *revised* prompt found **10
  revision-introduced defects** (contradictions, stale counts, a schema constraint that existed
  only implicitly). Lesson: every prompt edit needs its own regression pass.
- **Regression tests:** targeted re-runs after each boundary fix (e.g., the altitude rule: 8/9,
  with one model flipping back *because of* the guard — and one model ignoring a verbatim named
  worked example, a recorded model-compliance signature, not a wording gap).

## 5. Quantified outcome trajectory

| Milestone | Primary match vs human | Notes |
|---|---|---|
| v1 instrument (3 models, Set A) | 6/10 each | breadth noise dominant |
| v2 gate (post-vetting) | fable 10/10 · codex 9/10 · gemini 9/10 | facet Jaccard doubled (.34–.42 → .61–.70) |
| v2.13 full panel (Sets A+B, n=20) | **opus 17/20 · gemini 14/20 · codex 13/20** | facet-J .71/.67/.64; leakage caveat below |
| Consensus triage (retrospective, n=20) | unanimous 10/11 correct; 2/1 majority 6/6; 3-way splits = exactly the 3 hardest papers | basis of the production Jidoka ladder |

**Leakage caveat for any accuracy claim:** several calibration papers are *named* in the
instrument as worked examples/counter-examples, which inflates model scores on those papers
relative to unseen sweep papers. Disclose it.

## 6. Prompt-engineering lessons catalog (assignment raw material)

1. **Compression-gap principle:** a boundary only protects taggers if it's in the copy they tag
   from — the same documented error recurred (human, VibeGuard) because the exclusion lived in the
   reference but not the compressed cheat-sheet. Now enforced: every human-catching boundary lands
   in all copies, same commit.
2. **Imperative wording matters:** a "should" convention got ignored; re-worded as "the primary
   MUST be the biggest-tent theme" it started binding (dry-run evidence).
3. **Slug connotation is load-bearing:** taggers read tag *names* before definitions.
   `survey-input` was misread as "is a survey" (fixed by `method-self-report`, deliberately not
   `method-survey`); `proposal` was rejected as a slug because every paper "proposes"
   (`design-only` carries its exclusion in the name).
4. **Word-collision routing:** corpus-frequent words (framework, transparency, risk, bias,
   explainability) are never tagged as words — each routes by the *object* of the contribution,
   with explicit routing rules in the prompt.
5. **Worked examples and counter-examples both work — until a model ignores one:** a named
   verbatim counter-example fixed two models and was ignored by a third (a model-disposition
   finding: tagging behavior is a model property, not a vendor property — Fable clustered with
   Gemini, not Opus).
6. **Checklists beat recall:** with 40+ possible tags, facet misses clustered until a mandatory
   seven-question checklist (role/form/scope/mode/contribution/risk-types/method) made coverage
   mechanical. Coder fatigue is a *human* reliability factor too — the checklist protects both.
7. **Schema constraints must be stated, not assumed:** "primary MUST appear in themes" entered the
   prompt only after a model violated it.
8. **Every prompt change is an experiment:** re-run, measure, log — and beware multi-change
   commits (the §9 confound). Version everything (v0 preserved verbatim; v0→v2.13 fully diffable).

## 7. Where things live (repo `thurlow-research/SLR`, main)

- `slr-phase4/Tag_Prompt.md` / `Tag_Prompt_v0.md` — current vs original prompt (the before/after).
- `slr-phase4/Taxonomy_Changelog.md` — §1–§30, every iteration; §5 (Hedwig fix), §9 (confound).
- `Methodology/Theme_Tagging_Calibration.md` — design, agreement numbers, §7 running log,
  co-tagging protocol, comparability accounting.
- `slr-phase4/data/tags*/` — per-model tag JSONs for every run vintage (v1, v2, v2.1, v2.13);
  `data/tags-v213/human_gold.json` = the adjudicated human sets.
- Hedwig full text: `slr-phase4/txt/T72TU8B5.txt`.
- **`Handoffs/Tag_Prompt_ASSIGNMENT_hedwig-free.md`** — the assignment's experimental prompt: the
  live v2.13 prompt with the two Hedwig references replaced (framework exemplar "(VibeGuard,
  Hedwig)" → "(VibeGuard, CodeAgent)"; the tie-breaker's worked example swapped for a
  structurally-parallel diff-risk-gate example that neither names nor describes Hedwig's
  mechanism). **Use THIS for any model re-runs on Hedwig** — the live prompt names Hedwig's
  answer, which contaminates the experiment (the worked-example-leakage caveat, made concrete).
  The live instrument is unchanged; this variant exists only for the assignment.

## 8. Ground rules for the Desktop session

- The assignment is **prompt optimization analysis/design** — e.g., the §9 isolation test
  (defs-only vs tie-breaker-only factorial on Hedwig). It is NOT a license to change the live
  instrument: mainline instrument changes go through the arbiter loop in the repo, all copies in
  lockstep.
- Any experiment claims should carry the two standing disclosures: the §9 multi-change confound
  and the §5 worked-example leakage caveat.
- Cite the HOS software where invoked: Thurlow, S. (2026). HumanOversightSystem (Version 0.5.0)
  [Computer software]. Purdue University. https://doi.org/10.5281/zenodo.21347272
