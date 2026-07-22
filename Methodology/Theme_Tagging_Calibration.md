# Theme-Tagging Calibration — Design & Findings

**Vibe Coding Governance SLR · methodology + results record**
**Started:** 2026-07-14 · Status (2026-07-18 EOD): **validation cycle complete; GATE = PASS
(Scott, 2026-07-18); instrument frozen v2.1+altitude; Set A human tags fully reconciled in Zotero;
next = Scott tags Set B blind (Set B remains model-free until then)**

Purpose: before applying the 16-theme controlled vocabulary (see `Emerging_Themes.md` → *Tag
reference*) to all 149 cores, establish **tagging reliability** on a small calibrated sample —
cross-model agreement first, then human-vs-model. This mirrors the Stage-3 cross-model QA approach
(κ, human-confirm) but for a *different task*: multi-label theme assignment rather than keep/discard
screening, so calibration is re-established from scratch.

---

## 1. Design

**Sample.** 20 cores drawn at random (Python `random.seed(714)`, reproducible) from the 149-item
Core set, split into two disjoint sets of 10:
- **Set A — "01-AI Calibration Run"** (Zotero collection `JFN8693L`): tagged by 3 models →
  cross-*model* agreement + worked examples.
- **Set B — "02-Human Calibration Run"** (Zotero collection `IURU9UTA`): **Scott tags first, blind**,
  then the 3 models → human-vs-model agreement. (Blind-first preserves an unbiased human baseline.)

| Set A (`JFN8693L`) | Set B (`IURU9UTA`) |
|---|---|
| UB2EVUFU UDVHQ5HR Z8TPRNEU T8E8SCCG M74M3RFJ | B644HQFS 6DXZGHD9 E95T8E88 7V7SRG43 UW2R6BBJ |
| 2CKL96B8 T72TU8B5 VG6CIDQW 22JBEZNK F9JM9CI6 | BAWCBT9R E3E5YA2E 5VTAJISY TF56EPIP R4WJZBSF |

**Taggers (three distinct frontier families, top reasoning tier).**
| Label | Model | How run |
|---|---|---|
| `opus` | Claude Opus (this assistant) | 5 subagents, 2 papers each, full-text read |
| `fable` | Claude Fable 5 | 5 subagents (`model:fable`), 2 papers each, full-text read (added 2026-07-14) |
| `codex` | `gpt-5.6-sol` (OpenAI) | `codex exec --skip-git-repo-check -c model_reasoning_effort=high` |
| `gemini` | Gemini 3.1 Pro (High), via `agy` | `agy -p … --model "Gemini 3.1 Pro (High)"` |

Deliberately three *different* vendors (not `agy`'s Claude option, which would duplicate Opus; not
Gemini Flash, which is not Opus-equivalent).

**Input.** **Full document text** (child TXT attachments, 2k–32k words each) — per Scott, tagging is
on document contents, not title/abstract. All 20 items had both PDF + TXT.

**Instrument.** Identical vocabulary cheat-sheet + prompt for every tagger (`TAG_CHEATSHEET.md`,
`model_prompt_prefix.txt`). Each tagger returns, per paper: one **primary** theme, all **theme**
memberships (multi-label, on *membership not mention*), any **facet** tags, and a ≤12-word rationale
per tag. Output = strict JSON.

**Tag scheme in Zotero (source-encoded so all taggers coexist on one item, fully reversible via the
`cal:` prefix):**
- `cal:<model>:theme:<slug>` — each theme membership (explicit `theme:` marker added 2026-07-15, so it
  strip-maps to the final `theme:<slug>` convention)
- `cal:<model>:primary:theme:<slug>` — the single primary theme (same `theme:<slug>` tail as the
  membership tag, with `primary:` prepended — consistent schema)
- `cal:<model>:facet:<slug>` — each facet
- `demote:<state>` (plain, not source-encoded) — transient re-scope flag, e.g. `demote:context`: this
  core looks like it belongs in another disposition; batch-reviewed then moved + flag removed.
- (human will be `cal:human:*`). After adjudication, the agreed set lands as plain `theme:<slug>`.

**Tooling** (now under `slr-phase4/tools/`; scripts are resumable/idempotent): `run_cli.sh`
(codex+gemini loop with per-call `timeout 300` + JSON salvage), Opus subagents, `write_tags.py`
(additive/replace-mode PATCH with `If-Unmodified-Since-Version`; reads `ZOTERO_API_KEY_RW` for writes,
falls back to `ZOTERO_API_KEY`). Model outputs kept as per-tagger JSON files (`data/tags/<model>/<key>.json`)
→ comparison; no plain `theme:` writes during calibration.

**Process notes / lessons (for the full run):** (1) don't double-background (`nohup … &` inside a
background call spawned racing runners); run one tracked process. (2) Concurrent writers can
concatenate two JSON objects into one file — normalize each file to its first valid object
(`json.JSONDecoder().raw_decode`) before parsing. (3) `agy`/`codex` occasionally emit empty output on
a long paper; the idempotent `[ ! -s ]` guard + re-run fills gaps. (4) Zotero PATCH returns 204 with
an empty body — don't `json.loads` it.

---

## 2. What we did

- Drew the sample, populated the two Zotero collections (additive collection membership).
- Downloaded the 20 TXT full-texts.
- Tagged **Set A** with all three models on full text; wrote 30 source-encoded tag sets to the
  `01-AI Calibration Run` items in Zotero.
- Computed cross-model agreement (below).
- Delivered Scott a self-contained **Set B human-tagging packet** (`SETB_PACKET_FULL.md`).
- **Froze the instrument** pending Set B (see §4 decision).

---

## 3. What we observed — Set A cross-model agreement (n=10)

### 3.1 Primary "home" theme — highly reliable
Unanimous **9/10**. Pairwise primary match: **codex–gemini 10/10, opus–codex 9/10, opus–gemini 9/10.**

| key | opus | codex | gemini |
|---|---|---|---|
| UB2EVUFU | **hitl-workflow** | ai-review | ai-review |
| UDVHQ5HR | ai-review | ai-review | ai-review |
| Z8TPRNEU | hitl-workflow | hitl-workflow | hitl-workflow |
| T8E8SCCG | rules-based-checks | rules-based-checks | rules-based-checks |
| M74M3RFJ | regulatory-compliance | regulatory-compliance | regulatory-compliance |
| 2CKL96B8 | ai-code-insecurity | ai-code-insecurity | ai-code-insecurity |
| T72TU8B5 | risk-routing | risk-routing | risk-routing |
| VG6CIDQW | hitl-workflow | hitl-workflow | hitl-workflow |
| 22JBEZNK | automation-bias | automation-bias | automation-bias |
| F9JM9CI6 | hitl-workflow | hitl-workflow | hitl-workflow |

The lone disagreement (`UB2EVUFU`) is a **ranking** call, not a miss: each model's chosen primary is
*present in the other two's membership sets* (ai-review ↔ hitl-workflow, a multi-agent framework with
async human oversight).

### 3.2 Secondary (multi-label) breadth — where all the noise is
- **Themes per paper:** opus **4.7**, codex **5.0**, gemini **2.7**.
- **Pairwise theme-set Jaccard:** opus–codex 0.53, opus–gemini 0.48, **codex–gemini 0.62**.
- **Consensus core vs long tail:** across the 10 papers, **23** tags all-three agree on vs **27**
  asserted by a *single* model. ~Half the secondary tags are one model's opinion.

### 3.3 Model signatures (directional bias) — assignment counts / 10 papers
| theme | opus | codex | gemini | read |
|---|---|---|---|---|
| hitl-workflow | 5 | 5 | 5 | unambiguous |
| regulatory-compliance | 1 | 1 | 1 | unambiguous |
| provenance-auditability | 4 | 4 | **0** | gemini blind to it |
| risk-routing | 4 | 5 | **1** | gemini under |
| agent-scope-drift | 3 | 4 | **1** | gemini under |
| governance-frameworks | 2 | 4 | 1 | codex over |
| oversight-explanation | 5 | **7** | 4 | codex over |
| rules-based-checks | 4 | **7** | 4 | codex over |
| automation-bias | **4** | 1 | 1 | opus only |
| oversight-theater | **2** | 0 | 0 | **opus only** |
| tooling-supply-chain | **1** | 0 | 0 | **opus only** |

- **gemini = conservative floor** — anchors on the primary; skips relational themes
  (provenance-auditability 0, risk-routing/agent-scope-drift 1).
- **codex = liberal ceiling** — over-extends process themes (rules-based-checks, oversight-explanation 7).
- **opus = middle, but the *only* model reaching the insufficiency layer** (oversight-theater,
  tooling-supply-chain, automation-bias).
- **Facets** follow the same shape: gemini under-tags (survey-input 2 vs 4/4; problem-statement-anchor
  3 vs 5/5).

### 3.5 Fable 5 added as a 4th tagger (2026-07-14) — the decisive comparison
Ran Claude **Fable 5** on Set A (same instrument, full text). It produced the run's most telling result.

- **Fable clusters with Gemini, not with Opus** — despite both being Claude. Pairwise theme Jaccard:
  **fable–gemini 0.86** (tightest pair in the whole matrix), fable–codex 0.62, codex–gemini 0.62,
  opus–codex 0.53, **fable–opus 0.49**, opus–gemini 0.48. → Tagging breadth is **not a vendor/family
  effect**; it's a verbosity disposition. Vendor doesn't predict behavior.
- **Two breadth camps:** liberal = codex 5.0 / opus 4.7 themes/paper; conservative = gemini 2.7 /
  **fable 2.6** (the most conservative tagger).
- **Opus is the outlier among *all four*, 3-to-1, on the insufficiency layer.** Fable (a Claude model)
  skips these just like Gemini/codex: automation-bias (opus 4 · fable 1 · codex 1 · gemini 1),
  oversight-theater (2 · 0 · 0 · 0), tooling-supply-chain (1 · 0 · 0 · 0), oversight-scaling-inversion
  (2 · 0 · 1 · 1). Only Opus reaches them.
- **Primary theme across 4 models: 8/10 unanimous.** Two splits, both *ranking calls at known theme
  adjacencies*: `UB2EVUFU` (Opus hitl-workflow vs three ai-review) and `T72TU8B5`/Hedwig (Fable
  hitl-workflow vs three risk-routing — the routing↔control-surface boundary).
- `provenance-auditability`/`risk-routing` split on the *liberal/conservative* axis (opus+codex reach
  them; fable+gemini don't), distinct from the insufficiency-layer axis.

### 3.4 Insights
1. **Structure agreed, breadth contested.** Primary theme is essentially solved; disagreement lives
   entirely in secondary membership.
2. **Opus is the outlier among all four models (3-to-1), and its outlier tags are the substantive
   ones.** With Fable added, three independent models (fable, codex, gemini) converge on a narrower
   reading and *only Opus* reaches the limits-of-oversight themes (automation-bias, oversight-theater,
   tooling-supply-chain). A naive **model-majority vote would systematically drop exactly those
   themes.** Crucially, Fable is a *Claude* model yet sides with the narrow camp (fable–gemini J=0.86),
   so this is **not vendor-driven** — it's a breadth disposition, and Opus's is the distinctive one.
   Reproduces the Stage-3 finding (**model consensus ≠ human; Opus ≈ human**). Do **not** auto-assign
   secondary tags by model majority; the human (Set B) is the arbiter on the now-3:1 split.
3. **Breadth is the tunable knob:** gemini too thin for complete rosters; codex slightly over; the
   right target is unknown until the human sets it.
4. **Well-defined vs fuzzy themes:** hitl-workflow / regulatory-compliance are crisp; the over/under-
   applied `oversight-explanation`, `rules-based-checks`, `provenance-auditability` are the boundaries
   to sharpen in `Emerging_Themes.md`.

---

## 4. Decisions

- **Freeze the instrument through Set B.** Do not iterate the prompt or tag definitions on Set A
  model results — that would tune the instrument toward *model consensus*, the known-wrong target
  (§3.4 #2), and break A/B comparability. Iterate **once, after Set B, anchored on the human tags.**
- Source-encode all calibration tags (`cal:<model>:…`); keep disposition-independent; reversible.
- Primary theme is reliable enough to model-assign with a light human check; secondary breadth is the
  open policy question Set B resolves.
- **2026-07-18 — `assistive`/`agentic` generation-mode facet pair added mid-Set-B** (additive, per the
  `formal-methods` precedent: no theme redefined, no Set A re-run needed). Human Set B tagging from this
  date can apply it; **TF56EPIP was human-tagged before the pair existed → backfill**; all 20
  calibration papers get it backfilled in the post-Set-B iteration. In the same pass the Set B human
  packet's embedded cheat-sheet was found stale (v0-vintage) and refreshed to the current instrument
  (the Zotero Actions menu was already current; TF56EPIP's tags used current slugs, so nothing recorded
  was affected). See `Taxonomy_Changelog.md` §10.

---

## 5. Open / next steps — REVISED 2026-07-18 (freeze lifted; two-stage sequence)

**Design change (2026-07-18):** the freeze-then-iterate-once plan is replaced by a two-stage
sequence. **Stage 1 — human vocabulary-vetting pass:** Scott human-tags the calibration papers;
gaps and *unanticipated uses* drive definition changes as they surface, each logged in
`Taxonomy_Changelog.md` (first product: §11 — `oversight-explanation` broadened to push/pull
"helping the human understand what the AI is doing"; steering exclusion extended to input-side
context control; "context transparency" relocated out of `hitl-workflow`; record-vs-live-view test
on `provenance-auditability`; the Lumen unanimity overturn that motivated all of it). **Stage 2 —
the summative human-vs-model experiment on the vetted instrument.** Rationale: tuning toward the
*human* was always the plan; doing it before the comparison means the experiment tests the final
instrument, so disagreement is attributable to the models, not to known-fuzzy definitions.

1. Scott completes the vetting pass over the 20 calibration papers (+ types the
   `cal:human:primary:theme:<slug>` tag per paper — the menu can't). **Comparability note (corrected
   2026-07-18, post-pass):** Set A model tags were *present in Zotero* during the pass, but **Scott
   reports he never viewed them during his initial reads** — so initial-read human tags were
   *effectively blind (self-report)*; model outputs entered only through the post-tagging audit
   dialogue, which drove the documented corrections and the two re-adjudications. Accurate
   description: **Set A = blind first read + model-aware adjudication.** Notably, the two
   unanimity overturns (Lumen §11, 22JBEZNK §16) occurred at *blind* first read — the human
   independently diverged without knowing four models were unanimous against him, and full text
   vindicated him both times, materially strengthening the "model consensus ≠ correctness" finding.
   **Set B remains the fully clean comparison** (no model tags will exist there at all — do not run
   models on Set B until the human tags are in).
1b. **Instrument-critique panel (added 2026-07-18; design detailed 2026-07-18 EOD):** after the Set A
   vetting pass, validate the instrument itself before spending the retag. Sequence: (i) Fable
   **known-answer dry-run** — fresh-context taggers apply the current instrument to the 10 Set A
   papers; diff vs human tags; fix residuals (finds where the text doesn't *force* the adjudicated
   answer); (ii) **critique panel** — Fable 5 + Gemini top tier + Codex top tier, fresh contexts,
   given the instrument + Tag reference + curated Set A (full text for the 5 adjudication-rich
   papers, title/abstract for the rest) **with human tags only** (injected into the prompt — no
   tool access needed; the prompt is archived as the frozen critique input); critique + propose
   improvements; adversarial test cases required per finding; (iii) Scott dispositions findings
   (suggestions are proposals, adoption is the arbiter's); (iv) freeze instrument v2; (v) **retag
   Set A** under v2 and evaluate improvement (human-vs-model agreement + the §10–§17 regression
   checks) — **gate: only after v2 is judged improved does Scott tag Set B**, under the frozen
   instrument, then models tag Set B for the clean comparison. **GATE CALLED: PASS (Scott,
   2026-07-18)** — fable 10/10 / codex 9/10 / gemini 9/10 primaries, facet agreement doubled,
   altitude regression 8/9. Set A backfills executed same day (counterpoint → Z8TPRNEU+VG6CIDQW,
   agentic → T8E8SCCG, general-code → UDVHQ5HR); all 10 Set A items verified consistent with every
   adjudication and ruling. Actions menu (32 toggles) re-imported by Scott. **Critique taxonomy — only the first category is directly actionable:** (a) *ambiguity /
   inconsistency / omission* in the written instrument → fix; (b) *disagreement with an adjudicated
   boundary decision* (e.g., the drift object-of-mechanism rule, the steering exclusion) → recorded
   but the human arbiter's call stands — otherwise the critique loop re-tunes the instrument toward
   model consensus, the known-wrong target. Critique agents run in fresh contexts, separate from the
   tagger runs.
2. Freeze the *vetted* instrument; **archive check:** v1-instrument model outputs preserved in
   `slr-phase4/data/tags-v1/` (done 2026-07-18) before any re-run overwrites `data/tags/`.
3. Re-run all 5 models on Sets A+B in fresh contexts under the vetted instrument; write `cal:<model>:*`.
   **AMENDED 2026-07-21 (panel economics):** the v2.13 comparison panel = **codex + gemini over
   both sets (20 papers)** — Set A re-run included because the instrument evolved substantially
   (v2 → v2.13) since its last model pass. **Fable is $$$$-tier and runs ONLY with Scott's explicit
   per-run permission**, deployed *targeted* (tie-breaks: contested primaries, schema violations) —
   the assistant proposes tie-break targets and waits for authorization. **AMENDED same day
   (Scott): OPUS is a standing panel member** — the run set going forward is
   **opus + codex + gemini** over all papers; **Fable is reserved for tie-breaks/input beyond
   those three** (per-run permission unchanged). Opus ran all 20 blind on 2026-07-21; Fable ran
   the trimmed contested six. Outputs:
   `data/tags-v213/<tagger>/<KEY>.json`; runner `tools/run_setb_panel.sh` (gemini via file-read
   mode — `agy --add-dir`, no permission-skipping flags; prompt files scratchpad-only so full
   texts can't be staged).
4. Compute human-vs-model agreement (primary match; theme-set Jaccard; per-theme confusion) —
   **headline on Set B**; Set A reported as model-informed.
5. Decisive tests: (a) the insufficiency-layer breadth question (§3.4 — does the human tag
   `automation-bias`/`oversight-theater` where only Opus did?); (b) does the broadened
   `oversight-explanation` + steering cue fix the Lumen class of error?
6. Set the breadth policy; run the **full 148** under the final instrument; human-confirm the long tail.
7. **Set C (defined 2026-07-20) — AI-first validation set.** The inverse protocol of Set B and a
   pilot of the production sweep workflow: **models tag first** under the frozen instrument, the
   human **validates/adjudicates** rather than tags blind — measuring validation burden, catch
   rate, and error profile at review time (the mode the 148-sweep actually runs in; Sets A/B can't
   measure this). Membership = designated test cases, growing as probes surface. First member:
   `ZUM76CCG` (surfaced by the 2026-07-20 Set B roster reconciliation — it sat in the 02-Human
   collection and `calib_sets.json` but never in the human packet; Scott ruled it a Set C test case
   rather than an 11th Set B paper). Same reconciliation restored `TF56EPIP` to the 02-Human
   collection (it had been mis-shelved in 01-AI Calibration Run — all docs and its human-only tags
   confirm it is Set B). Zotero: `03-Set C - AI Tag, Human Validate` [U65X7JNA]; Set B = the
   packet's 10, matching `calib_sets.json`. **Pilot protocol (Scott, 2026-07-21):** Set C runs the
   full production ladder (`tools/triage_v213.py`: L0 schema → L1 consensus [3/3 ACCEPT + **10%
   seeded random audit**, 2/1 LIGHT-REVIEW, split HUMAN] → L2 computed tripwires [sprawl >6
   themes, any demote flag] → per-tag facet voting), but **Scott reviews ALL Set C papers**
   regardless of disposition — the pilot scores the ladder itself; sampling begins only in the
   sweep. **Replication stage (Scott, 2026-07-22 — disagreement-triggered, not universal):**
   observing run-to-run variability during the assignment work, the design adds targeted
   replication: any primary disagreement triggers **2 extra runs per model (k=3)**; each model's
   vote becomes its **modal** primary (tags = asserted in ≥2/3 runs); re-triage on modals —
   modal 3/3 = ACCEPT annotated *noise-resolved*, persistent 2/1 = LIGHT-REVIEW, persistent split
   = HUMAN. **Within-model instability** (a model disagreeing with itself across runs) is a new
   computed tripwire biasing one rung toward review — the operationalized "low-confidence" signal
   (computed, never self-reported, per doctrine). Unanimous first-pass papers are never
   replicated; the 10% audit covers residual false unanimity. The contested-subset replicates
   double as the gauge-R&R (repeatability) study for the methods chapter. Note: CLI taggers offer
   no temperature/seed control — nondeterminism is a property of the gauge, characterized rather
   than eliminated. Retrospective validation on the calibration 20: 7 ACCEPT (6 correct; the 1 divergence =
   the documented B644HQFS altitude ruling), 10 LIGHT-REVIEW (consensus proposal matched gold in
   all 10), 3 HUMAN (exactly the three hardest papers: 2CKL96B8, E95T8E88, TF56EPIP).

---

## 6. Reproducibility, versioning & write-safety (2026-07-15)

Infrastructure hardening done this date so the phase is reproducible and the instrument's evolution
is auditable (relevant for the course assignment and the dissertation methods chapter):

- **The whole SLR is now version-controlled.** Private GitHub repo **`thurlow-research/SLR`** (repo
  root = the OneDrive `Systemic Literature Review` dir; branch `main`). Phase-4 working materials live
  under `slr-phase4/` (prompt, cheat-sheet, calibration sets, per-tagger tag JSON, tools). Copyrighted
  full-texts (`slr-phase4/txt/`) and secrets are gitignored; `.gitignore` also excludes editor
  swap/backup files (`*.swp`, `.envrc.*`) so no credential-bearing temp file can be staged.
- **Instrument provenance captured as v0-vs-current.** `Tag_Prompt_v0.md` / `Tag_Cheatsheet_v0.md`
  (16 themes + 4 facets, original defs) preserved alongside the current `Tag_Prompt.md` /
  `Tag_Cheatsheet.md`; `Taxonomy_Changelog.md` logs each disparity → diagnosis → change → measured
  outcome, and flags the confound that *both* the definitions and the prompt's task block changed
  between versions (so the v0→current delta is not attributable to definitions alone).
- **Zotero Actions-menu self-select hazard (2026-07-20):** with the menu at 40+ toggles, scrolling
  can silently fire a toggle on the focused item — caught twice (a facet swap on 6DXZGHD9; a
  `risk-security` drop on 7V7SRG43). Standing mitigation: **post-paper server-side verification**
  (sync, then API-echo the tag set) after every tagging session; keyboard shortcuts on
  high-frequency toggles are the ergonomic fix if it recurs.
- **Zotero write-safety tightened after a key leak.** The single Zotero API key was found hard-coded in
  older scripts/skills; **all keys were revoked and rotated**, then **split least-privilege**:
  `ZOTERO_API_KEY_RO` (reads) / `ZOTERO_API_KEY_RW` (writes), with fallback to a single
  `ZOTERO_API_KEY`. Calibration/tagging tooling reads RO for GETs and RW only for the tag PATCH.
  The custom Zotero skills now **default to dry-run** and require an explicit `--commit` to write, and
  were re-released secret-free (`ResearchClaudeCodeSkills` v0.1.1). A standing global rule now scans
  staged content for key-shaped literals before any commit.

---

## 7. Human vetting pass — method & running log (Stage 1, 2026-07-17 → )

**What this is.** Before the summative human-vs-model experiment, Scott human-tags the 20
calibration papers as a **vocabulary-vetting pass**. The unit of work is not the tag set but the
*probe*: each paper tests whether the vocabulary can express what the paper actually is. This
reframes the human's first read from "baseline data collection" (the original blind design) to
**instrument validation** — the strongest use of the arbiter's limited attention, since Stage 2 then
measures the models against a vetted instrument and disagreement becomes attributable to the models.

**Method (per paper).**
1. Read full text; tag in Zotero via the Actions menu (`cal:human:theme:*` / `cal:human:facet:*`);
   **type** the `cal:human:primary:theme:<slug>` tag (the menu cannot toggle primaries).
2. Where the vocabulary resists, classify the failure before resolving it:
   - **Uncaptured concept** → candidate new tag; stage in `HOS_Seeded_Theme_Candidates.md` unless
     clearly needed now (bar: the concept recurs and no existing tag's *reasonable broadening* holds it).
   - **Unanticipated use of an existing tag** → the definition MUST be updated to sanction the use.
     "No new tag needed" does not mean "no instrument change": models tag from the written text, so
     an unwritten broadening would be scored as model error when it is doc lag.
   - **Boundary collision** → sharpen *both* themes' Boundary lines with the discriminating test.
3. Land every change immediately in the Tag reference + `Taxonomy_Changelog.md` (no batching), so
   the instrument converges monotonically and the models eventually see the settled text.
4. Model tags are *visible* on Set A during this pass (they already ran) — used **diagnostically**
   (does the human's difficulty reproduce a model split?). Set B carries no model tags; it stays
   clean for Stage 2.

**Decisions / learnings so far (through the first papers of the current 10):**
- **The Lumen unanimity overturn (§5, changelog §11).** 4-model unanimous primaries can encode a
  shared *category error*, not just ranking noise — unanimity is not a proxy for correctness even on
  the "solved" primary task. Boundary rules that exist only in the triage discriminator (steering
  exclusion) must be restated in the tagging instrument or models won't apply them.
- **The unanticipated-use principle** (method step 2b) — the pass's first-order product is
  definition text, not tags.
- **Facets carry explanatory load.** `assistive` (added a day earlier) *explained* the Lumen
  difficulty: in assistive mode there is no handoff for the old `oversight-explanation` to bite on.
  Mode facets validated on day one.
- **Word-collision discipline.** "Transparency" joins "framework" as a word that must route by
  object, never be tagged as such — now a preamble rule.
- **Lens-vs-lever** emerged as a cross-theme discriminator: information themes
  (`oversight-explanation`, `provenance-auditability`) vs action themes (`hitl-workflow`,
  `risk-routing`), with persistence (record vs live view) separating the two information themes.
- **Instrument-copy drift is real.** The Set B packet's embedded cheat-sheet was silently v0-vintage
  while the Zotero menu was current — caught 2026-07-18. All copies (cheat-sheet, prompt, packet)
  must be updated in the same commit as the Tag reference.
- **Tooling gap:** the Actions menu cannot set primaries → primaries are typed; early-tagged papers
  need backfill when the vocabulary moves under them (TF56EPIP: mode facet + primary pending).
- **Coder fatigue is a reliability factor of the human instrument** (UB2EVUFU, self-diagnosed
  "dinner fatigue"): the first-pass tag set had several oversights (facets missed, one theme
  mis-filed), all caught on a second look. With 29 tags/paper, recall-based tagging degrades when
  tired. Mitigations now in the instrument/process: the **five-question facet checklist** (mechanical
  coverage, not recall) and a **second-look verification** of each paper's tags before moving on —
  worth reporting in the methods chapter as an honest human-reliability observation alongside the
  model biases.
- **Self-correction is evidence the boundaries work:** the human's own `risk-routing` retraction on
  UB2EVUFU (error-condition handback ≠ triage decision) shows the sharpened definitions catch the
  arbiter too — the instrument is doing work independent of who holds it.
- **A boundary only protects taggers if it's in the copy they tag from** (VibeGuard recurrence, §17):
  the same human repeated the same documented error on the same paper because the exclusion lived in
  the reference doc but not the compressed cheat-sheet. Compression gaps are instrument bugs.
- **The struggle signal is a disposition tripwire:** difficulty picking a primary, or stretching a
  definition to fill a tag set, reliably indicated the paper didn't belong at core (2CKL96B8,
  UDVHQ5HR — both demote-flagged; 3 demotes / 10 calibration papers → expect a demote tail in the
  full sweep; the tagging pass doubles as a scope audit).
- **Model salience bias:** models anchor primaries and `problem-statement-anchor` on a paper's most
  vivid/quantified section rather than its overall shape or the facet's bar — a distinct failure mode
  from plumbing over-tagging and boundary pattern-matching.
- **Unanimity overturned twice:** Lumen (§11) and 22JBEZNK (§16) — in both, 4-model unanimous
  primaries encoded a shared category error the human caught. Model consensus ≠ correctness holds
  even at n-of-4 unanimity; the human vetting pass is what caught it.

**Running log** *(update at the end of the current 10)*:

| # | Paper | Set | Human outcome | Instrument action |
|---|---|---|---|---|
| 1 | `TF56EPIP` | B | 6 themes incl. `automation-bias`, `provenance-auditability`; no primary/facets yet | pre-dates mode pair → backfill primary + mode facet |
| 2 | `VG6CIDQW` (Lumen) | A | **COMPLETE & verified 2026-07-18:** primary `oversight-explanation` + `assistive` + `built-system` + `steering`; overturned 4-model unanimous `hitl-workflow` | changelog §11: `oversight-explanation` broadened (push/pull); steering exclusion → input side (confirmed, §12); `hitl-workflow` levers-only; `provenance-auditability` record test; transparency routing rule |
| 3 | `Z8TPRNEU` | A | **COMPLETE & verified 2026-07-18:** primary `hitl-workflow` (= 4/4 models) + `ai-review` (sides with codex alone) + `agentic`/`steering`/`survey-input`; rejected 3-model `agent-scope-drift` | changelog §13: object-of-mechanism rule; drift Captures tightened + Z8TPRNEU → counter-example; `steering` amended to cover documented practice; `ai-review` slug-connotation noted (watch in re-run) |
| 4 | `UB2EVUFU` | A | **COMPLETE & verified 2026-07-18** (after self-corrected second pass — "dinner fatigue"): primary `ai-review` (resolves v1 split: 3 models + human vs Opus) + `hitl-workflow`/`provenance-auditability`/`remediation-gating`; facets `agentic`/`built-system`/`framework`/`steering`; rejected `rules-based-checks` (plumbing — confirmed by full-text scan) and self-retracted `risk-routing` | changelog §14: error-condition-handback boundary on `risk-routing`; `remediation-gating` process gates; plumbing ≠ membership rule; five-question facet checklist |
| 5 | `T72TU8B5` (Hedwig) | A | **COMPLETE & verified 2026-07-18:** primary `risk-routing` — **human confirms the 5/5 post-fix model unanimity** (the tie-breaker sharpening's flagship result now human-validated); themes exact-match opus/fable v1 (`risk-routing`+`hitl-workflow`+`oversight-explanation`); facets `agentic`/`built-system`/`framework`/`survey-input` (resolves the framework 1/4 split against gemini); rejected codex's 4 plumbing extras + drift (object-of-mechanism applied consistently) | **none — first no-change probe**; instrument held on its previously hardest case |
| 6 | `F9JM9CI6` | A | **COMPLETE; primary RE-ADJUDICATED 2026-07-18 late** → `oversight-explanation` (altitude refinement: the vision's energy lives in explanation design; models unanimous there in v2) — was `ai-review` + `oversight-explanation`/`risk-routing`; facets `intro-framing`/`counterpoint`/`general-code`; **no mode facet** (AI on review side only — human reversed twice before the clarifier settled it) | changelog §15: `counterpoint` role facet (stance polarity, direction-agnostic); `general-code` scope flag (object-of-oversight); mode-pair clarifier ("uses agents" ≠ agentic); narrowness ruled extent-not-tagged |
| 7 | `22JBEZNK` | A | **COMPLETE & verified 2026-07-18:** primary `oversight-explanation` + `agentic`/`non-developer`/`survey-input`; **overturned 4-model unanimous `automation-bias`** (paper controls for + rejects overconfidence — capability gap, not bias); self-corrected `risk-routing` off | changelog §16: capability discriminator on `automation-bias` (22JBEZNK → counter-example); competence-gap candidate upgraded to arbiter-validated; mode tie-rule (reviewable unit dominates) |
| 8 | `T8E8SCCG` (VibeGuard) | A | **COMPLETE & verified:** primary `rules-based-checks` (= 4/4 models) + `ai-code-insecurity` + `framework`/`built-system`; `remediation-gating` re-applied then removed — **the documented §4 error recurred** | changelog §17: root cause = exclusion absent from the compressed cheat-sheet (the day-1 compression gap); exclusion now in all copies; "every human-catching boundary goes in the compressed instrument" |
| 9 | `2CKL96B8` | A | **COMPLETE & verified; primary RE-ADJUDICATED 2026-07-18 late** → `ai-code-insecurity` (human conceded to the operationalized biggest-tent after all 3 v2 models converged there; original `ai-review` was "scope-expanding its definition") + `ai-review`/`quality-debt` themes + `lit-review`/`intro-framing`/`assistive`; `demote:context` stands | changelog §17: lit-review structure-not-required clarifier; biggest-tent primary convention; struggle-signal workflow cue |
| 10 | `UDVHQ5HR` | A | **COMPLETE & verified:** `demote:context` flagged (LLM-judge capability benchmark, `VP7TS6CX` precedent); `ai-review` primary + sole theme (= all 4 models after removing stretched `quality-debt`/`intro-framing`) | changelog §17: demote-signature validation; anchor bar set (overall problem statement only; never on lit-review) |
| — | `M74M3RFJ` | A | verified (pre-pass tags stand): primary `regulatory-compliance` + `general-ai`/`framework`/`intro-framing`; demoted core→context 2026-07-15 | none — the `general-ai` tripwire case, already §6. **2026-07-20 reconciliation:** restored to the 01-AI Calibration collection (roster = frozen infrastructure); +`demote:context` (predated the flag); +`design-only` (2nd confirmed — GSN exemplars, engine = future work); −`intro-framing` (contradiction rule) |
| 11 | `R4WJZBSF` | B | **COMPLETE 2026-07-20** (blind snapshot v156638; blind read + model-aware adjudication): blind primary `risk-routing` → final **`regulatory-compliance`** + `hitl-workflow`; facets `metrics`/`framework`/`design-only`/`risk-ip`/`risk-bias`/`risk-quality`/`risk-overreliance`; no mode facet; **core, no demote** (what+how carve-out). Blind primary = the signal-without-allocation stretch — the boundary's first catch. Two define-only theme over-tags (`automation-bias`, `quality-debt` + `oversight-explanation`) caught in audit and removed | changelog §19 (`design-only`), §20 (`metrics` + routing boundary), §21–§22 (risk-flag family), §23 (what+how carve-out — this paper's ruling) — the most instrument-productive paper of the calibration |
| 12 | `6DXZGHD9` | B | **COMPLETE 2026-07-20** (blind snapshot v156680; final v156686): blind primary `ai-code-insecurity` (sole theme) → final **`org-governance`** + `ai-code-insecurity` secondary; facets `built-system`/`metrics`/`risk-security`/`risk-quality`/`risk-overreliance`/`survey-input`; `framework` OFF (pipeline test); no mode facet. **Four arbiter reads to converge** (detection → governance assessment) — logged as diagnostic: if models scatter here, human difficulty predicted it. Template-family caution (ANN-ISM) in child record | changelog §24: risk-quality consistency catch (PA-2 = PA-5 clause); metrics measurand settled by output-is-the-score test; Set B consultation Q&A on this paper produced the lit-review framing rule + input-side expert-panel ruling |
| — | *Set B process note (superseded same day — see the co-tagging protocol below)* | B | Original note: papers 1, 3–8 fully clean. By EOD 2026-07-20 the audit loop had extended to papers 1 (B644HQFS), 4 (7V7SRG43), and 6 (BAWCBT9R); only **3, 5, 7, 8 (E95T8E88, UW2R6BBJ, E3E5YA2E, 5VTAJISY)** remain audit-free (+ TF56EPIP backfill pending). No Set B paper has model tags | — |
| 13 | `B644HQFS` | B | **COMPLETE 2026-07-20** (blind v156722 → final v156726): primary `quality-debt` — **arbiter altitude ruling** (coded volume over the commons-framing wrapper; a documented human data point for the models' identical choice) + `oversight-scaling-inversion`/`automation-bias`/`org-governance`/`hitl-workflow` (documented-practice: the slop-mitigations); `risk-quality` parity catch; −`tooling-supply-chain` (no AI-tooling object; **knowledge-ecosystem pollution noted as a homeless observation** — watch in sweep) | mining-study archetype for the risk flags via coded categories |
| 14 | `BAWCBT9R` | B | **COMPLETE 2026-07-20** (blind v156730): primary `ai-review` + `demote:context` (judge-audit = validates-which-tool); `metrics` (measurand: judge bias-sensitivity/consistency); `method-experiment` (subjects-may-be-systems); QA removed `agentic` (mode-clarifier verbatim case) + `risk-quality` (wrong object — the evaluator, not the code) | changelog §27: the carve-out tool-validation **exclusion** encodes this paper's demote |
| 15 | `7V7SRG43` (CodeAgent) | B | **COMPLETE 2026-07-20** (blind v156742 → final v156790): primary `ai-review` + `agent-scope-drift` (**the §13 worked-pair, missed blind — QA catch**); +`general-code`; −`method-experiment` (whose-properties, 2nd occurrence); `risk-security`+`risk-quality` kept per the **source-agnostic ruling** (§27) — `risk-security` was then dropped by the **menu self-select hazard** and restored | §27 source-agnostic rule born here; menu hazard discovered here |
| 16 | `E95T8E88` (What to Cut) | B | **COMPLETE 2026-07-21** (blind v156811 → final v156819): blind primary `risk-routing` → **`oversight-scaling-inversion`** — the **second blind catch** of the signal-without-allocation boundary; +`routing-signal` (the facet's seed); malformed typed primary schema-fixed | changelog §29: `routing-signal` facet born here |
| 17 | `5VTAJISY` (HULA) | B | **COMPLETE 2026-07-21** (blind v156761 → final v156815): primary `hitl-workflow` ✓ blind (plan-gate home case); **first `adopted` of the calibration** (Atlassian JIRA internal deployment — the facet's scarcity bar held until a real one); method swap −`experiment` (own-system offline eval — whose-properties, 3rd occurrence) +`field-study`; −`metrics` (apparatus), −`ai-review` (the human reviews in HULA); `steering` ✓ (hybrid steer-and-check documented) | none — nine facet axes exercised cleanly |
| 18 | `UW2R6BBJ` (Secure AI-SDLC) | B | **COMPLETE 2026-07-21** (blind = final v156802 — **zero QA tag deltas, first human-solo-perfect set**): primary `regulatory-compliance` + `provenance-auditability`/`tooling-supply-chain`; `expert-validated` (the **promotion instance**, §V.E structured 12-expert post-implementation validation; Phase-1 consultation separately input-side); `general-ai` kept as audit trail — **core via the sole-exemplar exception** (§30, arbiter-weighed) | changelog §28 (promotion) + §30 (kept-core exception) born here |
| 19 | `E3E5YA2E` | B | **COMPLETE 2026-07-21** (blind v156770 → final v156826): primary moved `hitl-workflow` → **`automation-bias`** (named in its own abstract + skill erosion); +`survey-input` (perception-study archetype) + `demote:context` (§3 perception class); −`theme:ai-code-insecurity` (perception ≠ empirical — B644HQFS consistency; `risk-security` flag stays), −`method-field-study` (interviews only), −`org-governance` (implications ≠ lift) | none |
| 20 | `TF56EPIP` (backfill) | B | **COMPLETE 2026-07-21** (v156789): retagged under the mature instrument — 3 themes (from the pre-mode-pair 6), both mode facets, `lit-review` + `metrics` + `steering` + risk flags; `demote:context` (agreed: model-evaluation focus per UDVHQ5HR/VP7TS6CX precedent; **background wealth preserved via context tier, child note, and reference snowballing**); primary `ai-review` confirmed as biggest tent under the binding lit-review rule | none |

**Co-tagging protocol (named 2026-07-20; role division clarified same day; documented for the
methods chapter).** During Set B the working mode evolved from "human tags blind, alone" into
**co-tagging — precisely: human-tags + AI-QA**. The role asymmetry is the design: **the human
performs ALL tagging judgment; the AI never proposes tags before the human's blind set is
recorded** — it performs quality assurance after. The loop: (1) the human tags each paper blind
(no model tags exist; the assistant has not read the paper); (2) on request, the assistant
*audits* the recorded tag set against the instrument text and the full text — consistency checks,
rule-pointers, textual evidence — and answers definition questions at rule level; (3) the arbiter
rules on every delta (the assistant's audit findings are proposals; adoption is the arbiter's, per
the §5·1b critique-taxonomy rule); (4) every boundary that catches or nearly catches the human
lands in the compressed instrument the same day (compression-gap principle). Where the assistant
wrote tags via API, it executed the arbiter's already-made rulings mechanically (e.g., the
M74M3RFJ reconciliation, the agreed method-facet corrections) — execution, not judgment. **Yield:** instrument v2.2 → v2.10
in two days (changelog §19–§27: design-only, metrics, the five-flag risk family, the method
family, the what+how carve-out, ~a dozen boundary rules), a per-paper catch record (define-only
over-tags, word-trap saves, the §13 worked-pair miss on 7V7SRG43), and near-model-error
prediction (the human's difficulty spots flag where models are expected to scatter).
**Comparability accounting (state precisely in writeups; AMENDED 2026-07-21 at Set B close):**
ALL TEN Set B papers were ultimately co-tagged (the arbiter chose QA for the final four as well) —
every Set B human set is **"blind first read + AI-audited adjudication, model-tag-free."** The
**human-solo layer is preserved for all ten** as pre-audit Zotero versions: R4WJZBSF v156638 ·
6DXZGHD9 v156680 · B644HQFS v156722 · BAWCBT9R v156730 · 7V7SRG43 v156742 · 5VTAJISY v156761 ·
E3E5YA2E v156770 · TF56EPIP v156784 · E95T8E88 v156811 · UW2R6BBJ v156802 (blind = final there —
zero QA deltas). Scoring plan: **headline = models vs the final adjudicated sets** (the
co-tagging gold standard); secondary = models vs the blind snapshots (human-solo performance).
**Disclosed confound:** the instrument moved during the pass (v2.2→v2.13), so blind tags for
early papers predate rules the models will see (the §9 confound's smaller sibling); the final
adjudicated sets are consistent with the closing instrument. The **fully-clean comparison role
rests on Set C** (AI-first protocol, untouched). Set B tally: 3 `demote:context` flags in 10
(BAWCBT9R, TF56EPIP, E3E5YA2E) — matching Set A's 3/10 demote rate exactly.

