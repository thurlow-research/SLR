# Emerging Themes — cross-cutting patterns surfacing during triage/extraction

**Vibe Coding Governance SLR · synthesis source document**
**Started:** 2026-07-13 · Updated 2026-07-14 (full theme catalogue added) · Grows as themes recur across the corpus

Themes that span multiple items and warrant a dedicated synthesis section in the review /
dissertation. Each names its anchor + the corpus cluster (Zotero item keys) so it is traceable.

---

## Tag reference — full working vocabulary (2026-07-14)

Derived **bottom-up** from open-coding all 149 Core abstracts (4 parallel coders, identical frame)
→ merged emergent clusters → cross-checked against the 76 HOS experiential findings. Grouped by the
review question's own structure. `theme:<slug>` is the tag applied; the cross-doc **T-label** (T0–T3)
ties back to the handoff / `Problem_Statement_Evidence.md`. Example keys are **illustrative members**
surfaced during coding, not final rosters — the systematic sweep confirms/completes each. Counts (~N)
are approximate, for sizing. **Two themes have full write-ups below** (`tooling-supply-chain`,
`oversight-explanation`).

### How tagging works (read before applying)

Tags live in **three independent layers**; a paper normally carries several across them:
- **Lineage layer** (screening ground truth, every paper): `source:` · `s3:human:<bin>` · `centrality:<n>`.
- **Facet layer** (functional role in the write-up): `problem-statement-anchor` / `survey-input` /
  `intro-framing` / `lit-review` — zero or more.
- **Theme layer** (`theme:<slug>`): cross-cutting membership — **apply liberally**; a core paper
  typically belongs to 1–3 themes.

- **Multiple tags: expected.** The layers answer different questions ("where from / is it core?",
  "what role?", "what argument does it feed?"), so they stack. A paper can also hold several *themes*
  (e.g. a system that reviews, risk-scores, and escalates tags all three stages).
- **Mutual exclusivity: only one dimension.** Disposition `core`/`context`/`discard` (lineage layer)
  is exactly one per paper. **Among synthesis tags, nothing is mutually exclusive** — they are built
  to overlap; the Detect pair (`ai-review`/`rules-based-checks`) *expects* dual-tagging on gray-zone
  systems (rubric-grounded LLM-judge; "LLM writes tests then runs them"). Theme tags are **orthogonal
  to disposition** — a *context* paper can still carry `survey-input` or a `theme:`.
- **Membership, not mention.** Tag a theme only where the paper *contributes to that theme's argument*
  (with a one-line rationale), never because the abstract name-drops the topic. Keeps a `theme:` filter
  returning a real roster, not keyword noise.
- **Plumbing ≠ membership (systems papers, 2026-07-18).** A built system *uses* many mechanisms —
  its agents run tests, sandbox code, retry fixes — but tag only the mechanisms the paper
  *contributes an argument about*. (Calibration: three models tagged `rules-based-checks` on
  `UB2EVUFU` because its agents run test suites — instrumental plumbing; the paper's contribution is
  the agentic verification architecture → `ai-review`.)
- **Steering exclusion (apply before any solution theme).** Contributions that shape *what gets
  generated* — better prompts, specs, fine-tuning, and **controlling the AI's inputs/context** — are
  *steering*, not oversight; only a paper's inspection/comprehension/gating remainder earns solution
  themes. (Calibration: all four models missed the input-side case on Lumen `VG6CIDQW`, whose
  "context control" lever is steering — see decision log 2026-07-18.)
- **"Transparency" is never tagged as such — route it by object:** artifact/provenance *record* →
  `provenance-auditability` · reviewer comprehension (live view or handoff) → `oversight-explanation`
  · agent-behavior monitoring → `agent-scope-drift` · institutional evidence/audit trails →
  `org-governance` / `regulatory-compliance`.
- **Primary theme (one per paper) — tie-breaker.** The paper's *home*, where it'd be written up in
  depth. When a paper spans **adjacent** themes (`risk-routing`↔`hitl-workflow` = route vs. control-surface;
  `ai-review`↔`hitl-workflow` = the AI check vs. the human's gate), the primary is the theme carrying the
  paper's **distinctive contribution / novelty**, *not* the standard scaffolding. (Hedwig `T72TU8B5`:
  novelty = the dynamic-autonomy classifier → `risk-routing`, not the check-in surface.)
  **Altitude refinement (Scott, 2026-07-18 late, F9JM9CI6):** when a broader and a more specific
  theme both fit, primary = the most specific theme that still captures **where the paper's main
  effort lives** (F9JM9CI6: an AI-review vision whose energy goes into explanation design →
  `oversight-explanation` primary). Guard: a specific mechanism that is one *component* of a broader
  contribution does NOT outrank the broader theme (UB2EVUFU: budget-halving inside the verification
  architecture → primary stays `ai-review` — the exact codex/gemini v2 retag error).

---

### FACET TAGS (functional role; orthogonal to theme)

**`problem-statement-anchor`** — a single "committee-sit-up" empirical statistic strong enough to anchor
the problem statement. Feeds `Problem_Statement_Evidence.md`; also gets a child note. *Selective — few papers.*
**Bar (sharpened 2026-07-18):** the stat must anchor the **overall** problem statement (the
oversight-scaling inversion / two-part frame) — not a sub-argument's headline number (e.g. LLM-judge
unreliability) or a population-specific finding, however vivid. Models over-apply this facet by
*salience* (any impressive number); the calibration human applied it zero times in 10 papers on this
bar. **Never on a `lit-review` paper** — its stats are secondhand; chase and anchor the primaries.
- `59KP8GTP` — ~80% of AI-co-authored PRs merged with no explicit review.
- `3Z45M3V3` — 29.5% of Python / 24.2% of JS Copilot snippets carry security weaknesses.

**`survey-input`** — empirical adoption / preference / RAI-priority findings that inform the **org survey
design** (what practitioners want, prioritize, or limit). *Valuable even at context tier — that's the point.*
- `29NBUJWT` — developer AI-adoption appraisals and RAI priorities by task type.

**`intro-framing`** — position / agenda / definitional papers that *name the gap* but don't operationalize
a mechanism; cite in the Introduction. Usually context-tier (+ often `lit-review`).
- `4TUNZ7FU` — position/agenda paper establishing the need.

**`lit-review`** — secondary literature (survey / review / meta-analysis); default context + reference-
snowball source. **Structure not required (2026-07-18):** systematic *or* narrative — the test is
whether the evidence is *synthesized from other papers rather than produced*. A casual stat-assembly
needs this facet *most* (marks the evidence derivative → cite the underlying primaries, don't
double-count). **Primary convention for lit-review papers — binding:** if this facet applies, the primary MUST be
the "biggest-tent" theme covering the synthesis *overall* — never the most vivid/quantified section
(the models' salience bias on `2CKL96B8`; the dry-run showed a non-imperative wording gets ignored).
**A framing related-work section ≠ this facet (2026-07-20, Set B consultation):** the facet marks
the PAPER's role — a paper producing its own results (study/system/design) with a literature review
as framing/input is primary literature; both facet jobs (derivative-evidence marker, biggest-tent
convention) would misfire on it. Hybrid edge: tag only if the review component is itself a citable
contribution ("would you send someone to this paper *for the review*?").
- `5I2W8IC6` — systematic review mapping trust/distrust concepts for LLMs in SE.

**`counterpoint`** (role facet, added 2026-07-18) — the paper **argues against a prevailing position**
in the AI-coding/oversight discourse: full-automation maximalism, the value of HITL, oversight
scaling — any direction. **Direction-agnostic**: record *what it opposes* in the rationale (a paper
can be contrarian toward automation yet aligned with this review's thesis, or vice versa). Two jobs:
(a) the Discussion's alternative-views roster / confirmation-bias defense; (b) operationalizes the
earmarked "contrarian hunt" — the roster accumulates during tagging rather than a separate later
hunt. Often co-occurs with `intro-framing`; absence = no counter-position staked.
- `F9JM9CI6` — against review-automation maximalism (note the polarity: *pro*-human-oversight).

**Artifact / evidence cluster** (added 2026-07-15; `design-only` added 2026-07-19) — four composable
facets capturing the *form and maturity* of the contribution, powering the **proposed-vs-adopted**
adoption story (esp. formal-methods aspirational-vs-niche). Maturity ladder: `design-only` →
`built-system` → `adopted`; `framework` marks the *form* and composes at any rung.

**`framework`** — a **technical framework / reference architecture / integratable design** — a concrete,
adoptable structure you could plug into a build/dev pipeline (whether or not yet implemented). **Not** an
org-policy apparatus (that's `theme:org-governance`) and **not** a one-off point tool. The distinction is
*altitude/integratability*: `facet:framework` = a pipeline-integratable technical framework;
`theme:org-governance` = the org-level governance apparatus that pulls oversight together. A purely
*conceptual* framework that's neither (a bare taxonomy/decision model) does **not** get this facet —
it's captured by its theme. Composes freely (e.g. `lit-review` + `framework`).
- **Breadth is NOT the criterion.** A *focused, single-concern* architecture still qualifies (VibeGuard's
  security gate, Hedwig's autonomy-control layer). What's excluded is a **point result** — a bare
  algorithm, benchmark, or measurement with no adoptable/reusable structure. Test: *"would someone adopt
  this as a reusable design into their pipeline?"* → framework; *"is it a one-off result?"* → not.
- `T8E8SCCG` — VibeGuard's security-gate framework (drops into publish/CI). *(A policy-as-code engine is
  the gray zone: `org-governance` topic **and** `framework` form — both.)*

**`design-only`** (form facet, added 2026-07-19 mid-Set-B under the §10 additive precedent) — the paper
**specifies a mechanism/architecture in buildable detail** (components, formulas, thresholds,
architecture) **but never credibly runs it**: no working implementation and no evaluation on the
intended object. The *positive* marker for "proposed, not built" — a missing `built-system` alone is
ambiguous three ways (facet not applicable vs tagger miss vs genuinely unbuilt); this disambiguates
and powers the synthesis claim "N of the solution papers exist only on paper."
- **A mock demo does not count as building.** A demonstration that fabricates the mechanism's core
  outputs — random/synthetic stand-ins for the very values the mechanism is supposed to compute — is
  still design-only. Worked example: `R4WJZBSF`, whose "production-ready Google Colab implementation"
  computes two of its four metrics as literal `np.random` draws, whose results table reproduces the
  mock's hard-coded probabilities, and whose claimed validation (κ=0.72, 90% precision, three
  institutions) has no corresponding artifact in the paper.
- **Applies only to papers that propose something.** An empirical study with no proposed mechanism
  gets neither this facet nor `built-system` — the facet marks the *presence of an unbuilt design*,
  not the absence of building.
- **Boundaries.** ≠ `intro-framing` (which specifies NO mechanism — the discriminator is *buildable
  detail*; carrying both on one paper is a contradiction). Mutually exclusive with `built-system` and
  `adopted`; composes with `framework` (a proposed reference architecture = `framework` +
  `design-only`). Completes the maturity spectrum: `intro-framing` (gap named) → `design-only`
  (mechanism designed) → `built-system` (running) → `adopted` (in real use).
  **Inclusive-side ruling (Scott, 2026-07-20, §23):** a *stated architectural-design contribution*
  (F9JM9CI6's AI-OS review-platform architecture) meets buildable detail even when the authors
  defer realization to a research agenda — F9JM9CI6 is the worked example on this side; genuinely
  mechanism-free gap-naming papers remain `intro-framing`.
- **Disposition tripwire** (parallel to steering-only and `general-ai`): a design-only *solution*
  paper meets the "proposes an unevaluated methodology/framework → context" discriminator — check
  the core bar / `demote:context` candidate. Not automatic: a novel central framework can stay core
  by the promote exception, **and the what+how carve-out (arbiter ruling 2026-07-20, §23) keeps a
  paper core when it names the elements to track AND defines operationalizable metrics for tracking
  them — instrumentation specification clears bar (2) as measurement even unevaluated (R4WJZBSF).**
- **Slug rationale:** chosen over `proposal` — every solution paper "proposes" something, so that
  slug invites over-firing (the `ai-review` slug-connotation lesson, §13); the exclusion lives in
  the name. Re-run regression pair: `R4WJZBSF` (design-only) vs the built Set A systems
  (`T8E8SCCG` VibeGuard, `T72TU8B5` Hedwig, `VG6CIDQW` Lumen — `built-system`, never design-only).

**`expert-validated`** (form facet, staged 2026-07-20, **promoted 2026-07-21** on its first genuine
instance — `UW2R6BBJ`, changelog §28) — the contribution was **evaluated by documented expert
judgment**: expert panel, Delphi rounds, structured practitioner review, with the process
described as method (who, how many, what protocol). The middle rung of evidence strength:
unvalidated design < expert-validated design < built prototype < adopted.
- **The panel judges the *contribution*, not produces the *data*.** Experts shaping requirements
  or filtering lit-review inputs (input-side — the dissolved 6DXZGHD9-era probe) don't count;
  experts as study *subjects* = `method-self-report`, not this; ≠ peer review (every published
  paper); ≠ undocumented collegial feedback. The same panel can do both jobs — provide data AND
  validate the design → `method-self-report` + this facet co-hold.
- Composes with `design-only` (the common case: specified, never run, expert-vetted) or with
  `built-system` (a running system additionally panel-reviewed).

**`built-system`** — the authors *implemented* the approach as a working system / tool / prototype
("…and they built it"), beyond describing it.
- `T8E8SCCG` — VibeGuard, a built pre-publish security gate.

**`adopted`** — evidence the system is used **outside the research context** — commercial / production /
real organizational use (by the authors' own company or third parties), **beyond a lab prototype or
benchmark**. The scarce, high-signal adoption bit; absence = prototype / proposal / study. Usually
co-occurs with `built-system`.
- **Pilot rule (2026-07-20, Set B consultation — applied same day by the arbiter):** "outside the
  research *context*" ≠ "outside the research *organization*". The discriminator is **study site vs
  user**: a pilot/multi-org case study run *as the paper's field evaluation* (authors deploy,
  instrument, observe — remove the study and the use ends) is the research context extended to a
  field site → strong `built-system` evidence, NOT adoption. `adopted` = use for the org's **own
  operational purposes** — integrated, org-initiated, or continuing beyond the study window.
  Textual cues: "we deployed at X for a 3-month pilot and measured…" → evaluation; "X has
  integrated it into their CI pipeline" / "in use at X since…" → adopted.
- `CTGGMIX9`, `V4IRKSFI` — industrially deployed review systems.

**`general-ai`** (scope flag, added 2026-07-15) — the governance/oversight contribution is **general
AI/LLM, not coding-specific** (transferable from the broader AI-governance space: model adversarial-
robustness, general RAI frameworks, general model-assurance). A *scope* flag; default (untagged) =
coding-specific (the SLR's core focus). Two jobs: (a) **scope audit** — surface cores that are
general-rather-than-coding-specific → candidates to demote to **context** (per the "broader governance
that transfers → context" rule); (b) **synthesis separation** — keep borrowed general-AI governance
distinct from coding-specific governance. Object-of-governance = the *model*, not the produced code.
- `M74M3RFJ` — assurance cases for LLM adversarial robustness + EU AI Act compliance (general-AI;
  **demoted core → context** 2026-07-15). The models all tagged it `regulatory-compliance` (theme-level,
  in-scope-looking); the human scoped it out — the flag is the tripwire for that.
- **Kept-core exception (arbiter, 2026-07-21 — adjudication-layer rule, changelog §30):** a deep
  regulatory-operationalization dive in a general-AI paper triggers a **look-at-keeping review —
  not an automatic keep**; the arbiter then weighs whether it is the corpus's **sole
  operationalization exemplar for a review-question limb**. `UW2R6BBJ` kept on that weighing (the
  only deep dive applying regulatory frameworks to engineering controls; evaluated deployment +
  expert-validated), serving the RQ's governance/policy limb. Parallel to the one-framing-anchor principle and `general-code`'s
  kept-core transfers; the flag stays on as audit trail. **Taggers/models still flag
  `demote:context` on general-AI objects** — the flag proposes, the human disposes; M74M3RFJ's
  demote stands (unevaluated, robustness-focused, not sole).

**`assistive` / `agentic`** (generation-mode scope pair, added 2026-07-18) — which *generation setting*
the paper studies. The cut is **who initiates + the reviewable unit**, NOT tool location — "in the IDE"
is the wrong axis, since agents live in IDEs too (Cursor, Copilot agent mode):
- **`assistive`** — human-initiated, **suggestion-granularity** generation (inline completion,
  *snippet-level* chat-paste): the human authors in the flow and accepts piece-by-piece (a chat task
  returning a *complete artifact* is the tie-rule case: reviewable unit dominates → `agentic`). Oversight surface = the
  *acceptance moment* (`automation-bias` territory).
- **`agentic`** — **AI-initiated / AI-planned multi-step work** delivered at **artifact/PR granularity**
  for review. Oversight surface = the *gate* (`oversight-scaling-inversion` territory; the setting the
  Detect→Triage→Fix→Escalate pipeline mostly presupposes).

Apply either or **both** (a paper that compares or spans modes); **neither** = the paper doesn't
specify, or mode is irrelevant to its claim (same absence convention as `adopted`).
**Clarifier (2026-07-18, F9JM9CI6):** the pair describes the **generation** studied — "uses agents"
≠ `agentic`, and "AI assists the human" ≠ `assistive`. A paper whose AI sits only on the
*review/oversight* side studies no AI generation → tag **neither**, and consider `general-code`.
**Tie-rule (2026-07-18, 22JBEZNK):** when the two criteria disagree — e.g. a *human-initiated* chat
task returning a *complete artifact* — **the reviewable unit dominates**: the facet's job is to
identify the oversight surface, and a wholesale-delivered artifact puts the human at the gate
(→ `agentic`) regardless of who initiated. Two jobs:
(a) **synthesis separation** — which oversight evidence/mechanisms belong to which mode; (b) **survey
stratification** — mode-specific items in the org survey.
- Illustrative: `3Z45M3V3` / `YBHHYR4P` — assistive (Copilot-snippet CWEs / users trust insecure code
  more); `SHK6KAX6` / `UIXCRBQX` — agentic (agentic-PR merge & maintenance studies); `T72TU8B5`
  (Hedwig autonomy tiers) — agentic.

**`steering`** (contribution-type flag, added 2026-07-18; amended same day; materiality qualifier added
after the dry-run) — the paper's proposed solution **or the practice it documents** operates on
**generation** as a **substantive part of the contribution** (not any incidental prompt-shaping
component — every AI system shapes a prompt somewhere) — better
prompts, specs/executable requirements, fine-tuning, shaping model inputs — rather than
inspecting/gating the produced artifact. **Contribution, not topic**: every AI-coding paper touches
generation; the flag applies only when steering is *offered as the solution* or is *the documented
practice under study* (empirical amendment from `Z8TPRNEU`: the "control" professional devs exercise
is largely generation-directing — the facet explains the thin solution-theme roster). Three jobs: (a) **audit trail** for the steering exclusion — documents why a solution
component earned no solution theme; (b) explains sparse theme rosters on hybrid steer-and-check
systems in the sweep; (c) **tripwire**: a *steering-only* solution is a demote-to-context candidate
(the `spec-driven-guardrails` resolution, now enforceable — parallel to `general-ai` for object
scope). Illustrative: `VG6CIDQW` (Lumen — context control over the assistant's inputs, confirmed
steering 2026-07-18, a big part of the system; its oversight remainder is `oversight-explanation`
pull); `DPKKMXSA` (prompt-enhancement as the fix); the spec-driven cluster (`C88VGWMI` `7SH86C2W`
`JCTP8VXP`, context-tier).

**`metrics`** (contribution flag, added 2026-07-20) — the paper **defines metrics / scores / indices**
(risk, quality, oversight, compliance) **as a deliverable** — not merely *uses* metrics to evaluate
something (every empirical paper has an evaluation apparatus; that earns nothing). The
**defines-vs-uses test is the guardrail** — "metrics" is as collision-prone a word as "framework."
**Contribution, not apparatus.** The metrics' **object comes from the co-tagged themes**
(+`regulatory-compliance` = compliance-risk metrics · + an oversight theme = oversight metrics ·
+`quality-debt` = quality metrics · +`risk-routing` = metrics that *drive* allocation, VTDG995V-class).
Composes with `design-only` (metrics defined, never run on real data — R4WJZBSF) or with problem
themes (defined AND applied → the findings earn theme membership; the facet marks the reusable
instrument).
- **Rationale MUST name the measurand** — *what* the metrics measure ("regulatory/ethical risk
  exposure," "defect likelihood," "review coverage"), not just the domain. The tag layer records the
  domain via themes; the risk-ness (or other nature) of the measurand lives in the rationale. A
  saturating `risks` facet was considered and **rejected** (2026-07-20): "talks about risk" is a
  mention-level criterion in a governance corpus — near-100% base rate, zero discrimination.
- **Boundary with `risk-routing`:** defining the signal without the allocation decision is NOT
  routing (see that theme's Boundary); papers that define AND route get theme + facet.
- Genesis: `R4WJZBSF` — four regulatory-risk indices, no allocation decision; the human's blind
  `risk-routing` primary was the stretch that exposed the gap (changelog §20). Staged kin:
  risk-quantification instrument family (`HOS_Seeded_Theme_Candidates.md`, sweep-cluster tripwire).

**`routing-signal`** (contribution flag, added 2026-07-21 §29) — the paper contributes a
**computed, producer-independent signal framed for review-attention allocation** (which artifacts
deserve human scrutiny) **without operationalizing the selection/gating logic** — no threshold,
tier, or engagement decision. The `steering`-grammar audit trail for the **signal-without-
allocation boundary**, which caught the arbiter blind twice in two days (R4WJZBSF `risk-routing`
primary; E95T8E88 `risk-routing` primary) — the instrument's most human-catching line gets its
positive marker.
- **Framing test:** the paper itself must frame the signal as review-attention input (E95T8E88:
  "allow reviewers to prioritize their attention"). Signals framed for other purposes get
  `metrics` only (R4WJZBSF's org-risk score) — keeps generic defect predictors out.
- **Mutually exclusive with `theme:risk-routing`** by construction: operationalized selection →
  the theme (+`metrics`); signal-only → this flag (+`metrics`, usually).
- **Synthesis job:** the Triage supply chain — "N papers supply routing signals vs M operationalize
  routing" is a field-maturity finding the review question predicts. Seed: `E95T8E88`
  (deletion-likelihood at PR creation, AUC 87.1, selection logic absent).

**`general-code`** (scope flag, object axis, added 2026-07-18) — the paper's oversight/review
mechanism targets **code generally, not AI-generated code specifically**; the AI (if any) sits on
the *oversight side* (review support), not the producing side. Such work *transfers* to the AI-code
setting but wasn't developed or evaluated there — keep it distinguishable so synthesis doesn't
overclaim (mechanisms *built for* AI code vs mechanisms *imported from* general review practice).
Default (untagged) = the overseen object is AI-generated code. Completes the wrong-object tripwire
family: `general-ai` (object = the model) · `general-code` (object = any code) · `non-developer`
(population) · `steering` (contribution type). Doubles as the audit trail for the "broader-setting
oversight that transfers" triage rule when such a paper is kept core.
- `F9JM9CI6` — AI-supported review prep (agents generate higher-level descriptions for the reviewer)
  for code review *in general*; kept core (augment-vs-replace), object = general code.

**`non-developer`** (scope flag, population axis, added 2026-07-18) — the generating/overseeing
human studied is **not a professional developer**: end-user, business user, citizen developer —
the "democratization" endgame of vibe coding. Default (untagged) = professional-developer context.
Completes the three scope axes: **mode** (`assistive`/`agentic`) · **object** (`general-ai`) ·
**population** (`non-developer`). Also the tripwire for the staged **oversight-competence-gap** theme
candidate (escalation presupposes a competent receiver; democratization removes it — see
`HOS_Seeded_Theme_Candidates.md`): if flagged papers accumulate making that argument, it promotes.
Illustrative: `22JBEZNK` — business users can't detect flaws in AI analyses even when warned.

**`risk-security` / `risk-quality` / `risk-overreliance` / `risk-ip` / `risk-bias`** (risk-type flag
family, added 2026-07-20 §21 as homeless-types-only, **extended to the uniform family same day §22**) —
**substantive treatment of the harm**, one bar for every flag: defines a metric for it ·
contributes/evaluates a mitigation for it · reports an empirical result about it · devotes focal
analysis to it. An intro risk-list sentence = mention, no tag; the rationale cites which clause fired.
Types: security · quality (incl. **code comprehensibility** — "explainability of the code," see the
routing note below) · over-reliance · IP/plagiarism/licensing · bias in generated code.
- **A deliberate, bounded exception to membership-not-mention**, justified by the synthesis
  deliverable it powers: the **risk×mitigation matrix** — which harms the corpus identifies vs which
  have actual mechanisms; the gap cells (identified-but-unmitigated) are Discussion findings.
- **Flag ≠ theme — the co-occurrence grammar:** the flag marks substantive *engagement*
  (define-level suffices); the matching theme (`ai-code-insecurity` / `quality-debt` /
  `automation-bias`) still requires the paper to *do the lift* (study/evidence/argue). Heavy-lift
  papers carry **both** — expected, not double-counting: the matrix reads flags for the
  identified/measured axis and themes/mechanisms for the evidenced/mitigated axis. **Matrix
  reconstruction = one query per column, one bar** (the uniform family replaced §21's asymmetric
  design — themed columns no longer depend on rationale text-matching).
- **Explainability routes by object** (word-collision list entry): support for the human *judging
  the AI/its output* → `oversight-explanation`; **comprehensibility of the code itself** (unclear
  logic, undocumented sections) → quality territory (`risk-quality`, `theme:quality-debt` if the
  lift is done); model-XAI → `general-ai`.
- **Source-agnostic (arbiter ruling 2026-07-20, CodeAgent `7V7SRG43`):** the flags track the
  **harm**, regardless of the overseen code's source — a `general-code` mechanism that mitigates
  security/quality harms earns the flags plus `general-code`, and the matrix segments transferable
  mechanisms via that flag (parallel to `lit-review` segmenting secondhand rows). The `general-ai`
  exclusion stands (M74M3RFJ: object = the *model*, not code).
- **Lit-review interplay (arbiter ruling 2026-07-20, reversing an initial lean):** focal secondhand
  synthesis CAN fire these flags — `2CKL96B8` (narrative review; focal security-stats + quality
  synthesis) carries `risk-security` + `risk-quality`. The matrix segments secondhand engagement
  via the `lit-review` facet; passing enumeration ("need quality metrics") still never fires; and
  `problem-statement-anchor` remains never-on-lit-review (different facet, different bar — the
  anchor requires a citable headline stat, chase the primaries).
- **Extensible on the same bar** if the sweep surfaces a new type (privacy the likely next).
  **Promotion path** (for the homeless types `risk-ip`/`risk-bias`): a cluster at contribution
  level converts flag → theme, definition ready-made.
- Genesis: `R4WJZBSF` (defines PRS/BPI/EG/ADS → earns all four applicable flags: risk-ip,
  risk-bias, risk-quality, risk-overreliance); informal corpus recurrence of IP risk observed by
  the arbiter; HOS's IP scanner = experiential corroboration (kin, not driver — the HOS guardrail
  holds). Changelog §21–§22.

**`method-self-report` / `method-mining` / `method-experiment` / `method-field-study`**
(data-collection method family, added 2026-07-20 §25) — the standard SLR study-characteristics
axis: **how the paper's own evidence was produced.** `method-self-report` = humans tell you
(questionnaires, interviews, focus groups, diaries — perception/attitude data); `method-mining` =
artifacts measured (repos, PRs, commits, forum posts, logs, telemetry — behavior/artifact data);
`method-experiment` = controlled tasks with manipulation (lab or crowdsourced);
`method-field-study` = deployment/case study observed in a real setting. **Apply all that fit**
(mixed methods expected: `Z8TPRNEU` = self-report + field observation).
- **Own evidence only:** `lit-review` papers get none (their evidence is synthesized — the methods
  live in the primaries); absence = no empirical evidence produced (position papers, pure designs).
- **World-or-tool test (2026-07-20, systems-paper consultation):** results describing the *world*
  → method facet; results describing only the *tool* (benchmarks, self-run tests over constructed
  corpora) → no facet — that evaluation is carried by `built-system`. A detector run over real
  repos earns `method-mining` only if the findings characterize the repos, not just the detector's
  precision. **Humans using the artifact always fires one:** assigned tasks / controlled
  conditions → `method-experiment`; real work in the org's own setting, natural use →
  `method-field-study` (the adopted pilot rule's study-site pilots and case-study evaluations land
  here); a lab study plus a deployment gets both.
- **Subjects may be systems (2026-07-20, calibration backfill audit):** controlled studies of
  **third-party** tools/models whose findings characterize those systems = `method-experiment`
  (UDVHQ5HR probing external LLM verifiers — the findings are about the world's tooling). Running
  **your own** system on a benchmark — even a standardized third-party one (UB2EVUFU on
  ProjDevBench, retry-on-fail conditions prescribed) — is still tool-results: no facet, by the
  whose-properties test; parity with VibeGuard's untagged "controlled experiments on synthetic
  projects." The triangle: VibeGuard (own tool, synthetic) none · UB2EVUFU (own tool, standardized
  bench) none · UDVHQ5HR (others' tools studied) experiment. Benchmark-grade evidence for own
  systems = evidence-strength within `built-system` — staged `benchmark-evaluated` candidate.
- **Slug rationale:** `method-self-report`, not `method-survey` — avoids colliding with
  `survey-input`, whose slug already misled the arbiter once (B644HQFS probe: the facet tests the
  finding's *utility to the org survey*, method-independent; a mined study can be survey-input).
- **Jobs:** (a) evidence-weight separation in synthesis — perception vs artifact evidence disagree
  routinely in this corpus (users *believe* insecure code is more secure, YBHHYR4P); (b) the
  methods chapter's study-designs table, collected free during the sweep; (c) matrix provenance
  (identified-by-perception vs identified-by-measurement). Single-home note: if the Stage-4
  extraction codebook gains a data-collection field, reconcile — these tags are now the home.

---

### THEME TAGS

Each entry: **Captures** (what earns the tag) · **Boundary** (include/exclude, where it helps) · **Examples**.

#### Family 1 — QUANTIFY THE PROBLEM (why oversight must scale)

**`theme:oversight-scaling-inversion`** (T0) · ~8
- **Captures:** the spine — AI code is *riskier yet less inspected*; PRs auto-merged unreviewed;
  review becomes the bottleneck; burden concentrates on a shrinking pool of maintainers.
- **Boundary:** measures the *oversight gap itself* (the gating act, or its absence / cost). Not a
  generic "AI is buggy" measurement (that's the two below).
- **Examples:** `59KP8GTP` — ~80% of AI PRs merged unreviewed; `SHK6KAX6` — 61% of agentic PRs merge
  with minimal human intervention; `F2C2DWSI` — Copilot shifts rework/review burden onto core devs;
  `B644HQFS` — "AI slop" externalizes review cost onto maintainers.

**`theme:ai-code-insecurity`** · ~7
- **Captures:** empirical evidence AI-generated code carries **security** vulnerabilities (CWE rates,
  security benchmarks, insecure-but-confident).
- **Boundary:** security/vulnerability specifically. Non-security quality issues → `quality-debt`.
- **Examples:** `3Z45M3V3` — real-repo Copilot CWE prevalence; `4PSM6ZCD` — agent code only 10.5%
  secure, hint-based mitigations fail; `YBHHYR4P` — users write less secure code yet believe it *more* secure.

**`theme:quality-debt`** · ~7
- **Captures:** **non-security** quality degradation — technical debt, complexity, code smells,
  maintainability, breaking changes — accumulating from AI code.
- **Boundary:** maintainability/debt, not vulnerabilities (→ `ai-code-insecurity`). **Code
  comprehensibility ("explainability of the code") lives here** — unclear logic, undocumented
  sections, code lacking human-understandable rationale is a maintainability/review-burden attribute
  (2026-07-20; NOT `oversight-explanation`, which is judging-support for the human). Define-only
  measurement of quality attributes → `metrics` + `risk-quality`, no theme (membership = the lift).
- **Examples:** `9H6FWJME` — AI commits introduce persistent smells surviving to HEAD; `REZGA5WF` —
  causal ↑ in complexity/warnings (Cursor); `UIXCRBQX` — agentic PRs riskier in *maintenance* (confidence trap).

#### Family 2 — LIMITS OF CURRENT OVERSIGHT (the insufficiency layer)

**`theme:automation-bias`** · ~7
- **Captures:** the *human* fails at oversight — over-reliance, complacency, skill erosion, cognitive
  disengagement; people miss flaws even when warned/prompted.
- **Boundary — the failing human must be CAPABLE (2026-07-18):** automation-bias is an attention/trust
  failure by someone who *could have caught it* (over-reliance, complacency). If the failure persists
  despite priming, distrust instructions, and incentives — or the human *lacks the ability/support to
  evaluate at all* (typically `non-developer` settings) — that is the **oversight-competence gap**
  (staged candidate, `HOS_Seeded_Theme_Candidates.md`), NOT bias. Counter-example: `22JBEZNK` — the
  study *controls for* over-reliance (primed distrust, prompts, pay) and its Discussion explicitly
  rejects overconfidence: "the difficulty is rooted in applying domain expertise or critical thinking
  to unfamiliar technical contexts." All four models mis-tagged it automation-bias primary on the
  surface phrase "missed flaws even when warned" — the warning was the *control*, not the finding.
  Process failure (hollow/unenforced review) → `oversight-theater`.
- **Examples:** `E689ZAXC` — adding a review step makes workers *less* likely to revise; `5BAZZWHG` —
  cognitive engagement declines with agentic assistants.

**`theme:oversight-theater`** · ~5
- **Captures:** oversight that exists on paper but lacks authority/time/information to change the
  outcome — rubber-stamp, token HITL, "meaningful vs. checkbox", moral-crumple-zone. *Enforcement, not
  knowledge* (HOS).
- **Boundary:** about the *structure/authority* of the review being empty. Human cognitive failure → `automation-bias`.
- **Examples:** `9MV2IVNU` — names "Rubber-Stamp Risk"; `JVWUYDME` — "Human-in-Command" replacing
  token HITL with an enforced operating envelope; `ZGST9CY6` — designing *meaningful* oversight vs. automation-in-disguise.

#### Family 3 — CHARACTERIZE THE SOLUTION · organized on the **Detect → Triage → Fix → Escalate** pipeline

The solution themes are stages of one loop. A single system often spans stages → multi-tag it.
Cross-cutting: `agent-scope-drift`.

**— DETECT (is there a problem?) — two *kinds of detector*, split by signal epistemics —**

**`theme:ai-review`** (**probabilistic detector**) · ~16
- **Captures:** AI/LLM/agentic review that *judges* the produced artifact — fallible, can hallucinate.
  Single-reviewer, multi-agent panels, and **independent / cross-model review** (one agent validating
  another). **Also carries the reliability limits** of agent-checks-agent review.
- **Boundary:** the output is a *judgment/opinion* ("this looks wrong"). Grounded/checkable output →
  `rules-based-checks`. *Deciding which findings matter* → `risk-routing`. *Making the fix* → remediation.
- **Examples:** `CTGGMIX9` — spec-grounded LLM review, industrially deployed; `5RKMGRNA` — multi-agent
  PR review (bug/security/perf specialists); `A6ZE2A26` — unanimous LLM jury as accept/reject gate.
  *Limits:* `BAWCBT9R` — LLM-judge prompt-bias; `UDVHQ5HR` — LLMs misjudge NL-spec conformance;
  `TA6GIUK2` — AI-reviewing-AI is circular without an executable spec.

**`theme:rules-based-checks`** (**deterministic detector**) · ~8
- **Captures:** grounded, checkable verdicts — can't hallucinate, but blind outside their spec.
  Static analysis / lint, type-checkers, **tests**, symbolic-execution & **classical formal-methods
  engines** (CBMC, theorem provers), sandboxed execution, rubric checks.
- **Boundary:** a *computed/executable* verdict against a spec/test/oracle. Note: value as *oversight*
  depends on the oracle's independence — AI code passing AI-written tests is near-circular. A classical
  formal verifier here **also** carries the composable `formal-methods` tag (see below).
- **Examples:** `PR4GS7SP` — symbolic execution assesses correctness at near-human accuracy; `9R6TGN82`
  — program-analysis + test signals train toward secure code; `QWHE9EXH` — sandboxed transpiler/executor;
  `72W6R4JG` — automated verification via fine-grained constraint-violation feedback.

**`theme:formal-methods`** (**composable technique tag** — annotates the performer, not a pipeline stage) · ~4–6
- **Captures:** the paper uses/proposes *formal methods* — theorem proving, model checking, symbolic
  execution, deductive verification, formal specification / autoformalization. **Orthogonal to the
  performer**: always pair it with the theme that says *who* does the formal reasoning.
- **Compose:**
  - AI/LLM does the formal reasoning → `ai-review` + `formal-methods` (e.g. `5DI9B43K` verified LLM
    reasoning; `6ZW9QNQH` autoformalization).
  - Classical engine (CBMC, theorem prover, symbolic executor) → `rules-based-checks` + `formal-methods`
    (e.g. `PR4GS7SP`; TF56EPIP's surveyed CBMC/theorem-proving).
  - Pure advocacy / position, no performer → `formal-methods` + `intro-framing`.
- **Why a tag, not a solution section:** only ~4/149 cores foreground it (`PR4GS7SP` `E5SQKRH7`
  `6ZW9QNQH` `5DI9B43K`), one a *position* paper — a minor, largely aspirational academic thread.
  A standalone section would read as a recommendation that won't land with practitioners.
- **Adoption-gap framing (synthesis point):** the barrier is the *human expertise/effort to author
  specs & proofs*, **not** the value of the guarantees — practitioners reject *doing* formal methods,
  not its output. So the composed tags predict uptake:
  - `formal-methods` + `rules-based-checks` (classical, human-authored) → **niche / high-assurance only**
    (lives-on-the-line exceptions), near-zero mainstream uptake; vibe coding's speed ethos won't change it.
  - `formal-methods` + `ai-review` (AI-automated / autoformalization) → **the plausible adoption path**:
    if AI removes the authoring burden, practitioners accept it as just another pipeline check.
  - **Economics caveat:** that uptake still hinges on the AI-driven check being cheap/fast/quiet —
    formal methods' compute cost doesn't vanish, and correct-but-uneconomical oversight gets turned off
    (cf. `three-tier-review-cost-model`, `cost-gating`). A testable hypothesis for the org survey.

**— TRIAGE (what matters / what to do / escalate?) —**

**`theme:risk-routing`** · ~12
- **Captures:** the **allocation / triage decision** — compute a signal → decide *which* AI actions/
  artifacts reach a human, *whether* to escalate, at *what* priority/autonomy tier. The contribution is
  the **smarts of surfacing** (signal + selection/prioritization/tiering logic). *Gate on a **computed,
  producer-independent** signal* (HOS); model self-confidence is disqualified. **Mnemonic: risk-routing = WHAT**
  (what gets surfaced, at what priority) vs. `hitl-workflow` = *how & when* the human then acts.
- **Boundary:** the contribution is the *selection/prioritization/escalation logic* (which/whether/when
  a human is engaged). The review that *produced* the finding → `ai-review`/`rules-based-checks`; the
  interface the human then uses → `hitl-workflow`. **Error-condition handback is NOT risk-routing
  (2026-07-18, UB2EVUFU):** "agent stuck / can't converge → hand back to the human" is an *exception
  path*, not a discretionary triage decision — no computed signal selects among items. The handback
  mechanism, if contributed, → `hitl-workflow`; oversight of the failed-fix loop → `remediation-gating`.
  **Defining a risk metric/score without the allocation decision is NOT routing (2026-07-20,
  R4WJZBSF):** routing = signal *plus* selection/tiering logic; a paper that contributes only the
  signal (metrics, scores, composite indices) with no which/whether/when decision built on it gets
  the `metrics` facet, not this theme. Papers that define AND route get both.
- **Examples:** `BU73N7PC` — Meta diff-risk-score gates risky diffs; `74GE3TF7` — creation-time
  circuit-breaker predicts high-maintenance PRs for gated triage; `VTDG995V` — calibration → *computed*
  review intensity; `T72TU8B5` — autonomy tier adjusts by earned developer trust.

**— FIX (remediate the problem) —**

**`theme:remediation-gating`** · ~3 (thin — populate in sweep)
- **Captures (D3 ruling, 2026-07-18): governance of AUTONOMOUS fixing** — the system fixes *without
  per-fix human involvement* (Jidoka: autonomation that stops/corrects itself), kept safe by
  machinery: **content** gates (filter/arbitrate *which* fix candidates are acceptable) and
  **process** gates (bounded retries, budget-decay, convergence rules, stop-progression — fail-closed
  termination + handback when the fix won't converge). The *acting* step brought under control.
  Deciding when a **human** must engage on the fix path (risk tiers over fixes) = `risk-routing`
  layered on top — the andon cord, not the gate. **A human approving every fix is NOT this theme:**
  review-everything is the unscalable anti-pattern this review exists to move past (attention
  collapse → automation-bias territory); a paper *advocating* blanket per-fix human approval is a
  `counterpoint` candidate. Note the distinction: such a design *introduces* automation-bias risk —
  a rationale-level critique — whereas `automation-bias` *membership* requires the paper to
  study/evidence the human failure, not merely risk causing it.
- **Boundary:** the *gating/oversight of the fix*, **not** the repair technique itself (generating a
  fix is generation, outside the oversight frame). **Requires an autonomous fix/repair action being
  overseen** — a pure *detection or publish/quality gate* that blocks bad code with **no auto-fix** is
  NOT remediation-gating; that's the enforcement side of the detector (`rules-based-checks`/`ai-review`).
  Re-checking a landed fix → `rules-based-checks` / `ai-review`; deciding *which* fixes need sign-off →
  `risk-routing`. *(Calibration note: both a human and Opus over-tagged VibeGuard `T8E8SCCG` here — a
  publish gate, no auto-fix — which is why this exclusion is now explicit. **The same human repeated
  the same error on the same paper 2026-07-18** — root cause: this exclusion lived only in this doc,
  never in the compressed cheat-sheet the tagger works from. Now carried in every copy. Principle:
  every boundary that has ever caught a human must appear in the compressed instrument.)*
- **Examples:** `GAD5Z8PV` — multi-LLM ensemble filters harmful AI fix suggestions with minimal-edit
  arbitration before deployment (content gate); `UB2EVUFU` — budget-halving retry cycles with
  stop-progression when verification keeps failing (process gate); (sweep to add
  auto-repair-with-approval systems).

**— ESCALATE (human enters on disagreement / low-confidence / high-stakes) —**

**`theme:hitl-workflow`** · ~9
- **Captures:** the human's **control surface** — the mechanism an *already-engaged* human acts through:
  confirmation checkpoints, action guards, approval gates, human-as-director/orchestrator, bounded
  delegation. The contribution is the **design of the control point**, not the
  logic deciding what to surface. **Mnemonic: hitl-workflow = HOW + WHEN** the human acts (control
  mechanism + checkpoint placement/frequency) vs. `risk-routing` = *what* to surface.
- **Boundary:** *how the human exercises control* — **levers, not lenses**: comprehension/visibility
  tooling (the former "context transparency", relocated 2026-07-18) → `oversight-explanation`.
  Deciding *whether/what* to escalate → `risk-routing`. NB the steering exclusion: a lever over the
  AI's *inputs/context* is steering, not a control point over the artifact (the Lumen error).
  **Plan-gate rule (Scott, 2026-07-18 panel ruling):** a human gate over an AI-produced plan IS
  hitl-workflow when it is a *designed checkpoint in a lifecycle with checks and balances* (defined
  gate, authority to block, resumable process); the same approval act inside a conversational
  guide-then-"go do it" flow is steering.
- **Examples:** `XK3P9C96` — optimal placement of confirmation checkpoints; `U9VZQXGI` — HITL agent UI
  with action guards; `N7E3MR2V` — full-SDLC agent with human-approval guardrails + audit trails;
  `ID7IN65K` — 860-dev survey: demand for bounded delegation with authority scoping.

**`theme:oversight-explanation`** (T2) · ~5 — *full write-up below*
- **Captures (broadened 2026-07-18): helping the human understand what the AI is doing** — the
  *information* side of oversight, in either direction:
  - **push** — the system escalates and makes the handoff **comprehensible and decision-ready** to a
    reviewer not embedded in the code: background + options + recommendation + risks; uplevel from
    code detail to decision framing (the agentic-mode manifestation);
  - **pull** — tools the human *invokes* to understand what the AI is doing/using: context and
    dependency visibility, live "what is it drawing on" views (the assistive-mode manifestation;
    absorbs "context transparency", relocated here from `hitl-workflow`);
  - **standing** (added 2026-07-18, critique panel) — explanations *attached to AI output* that
    support the human's verdict (`7UB2MD8Z`'s patch explanations; 22JBEZNK's reformatted responses).
    The modes are **illustrative, not exhaustive** — the headline governs.
- **Boundary:** information/lens, never the lever — *acting* on the understanding (gates, checkpoints,
  approvals) → `hitl-workflow`; *where* to look → `risk-routing`; a **persistent auditable record**
  (vs a point-in-time view) → `provenance-auditability`.
- **Examples:** `7UB2MD8Z` — explanations improve human patch-correctness judgment (5/6 bugs);
  `KF5MGIBI` — fine-tuned LLM improves review-comment comprehensibility (localization/explanation/fix);
  `IM6DJDEE` — "Consultation Request / Merge-Readiness Packs" as structured handoff artifacts;
  `VG6CIDQW` (Lumen) — human-invoked context/dependency visibility in assistive mode (pull).

**— CROSS-CUTTING (keep the agent on-mandate) —**

**`theme:agent-scope-drift`** (HOS-A) · ~5
- **Captures:** agents range **beyond mandate** / make unreviewed architectural decisions / drift from
  intent; mechanisms that **detect or bound departure from intent** — intent telemetry, guardrails,
  earned-trust autonomy. (Tightened 2026-07-18 from "keep them in scope," which read as absorbing
  *any* control mechanism.)
- **Boundary — tag by the object of the mechanism, not the motivation of the actor (2026-07-18):**
  about *the agent departing from what was asked* (a distinct failure mode from producing buggy code).
  Applies when drift is the mechanism's **operand** — e.g., a multi-agent panel checking the code's
  scope against the spec's scope → `agent-scope-drift` + `ai-review` (object + performer, same
  composition grammar as `formal-methods`). Does NOT apply to generic retained control merely
  *motivated* by drift-worry — counter-example: `Z8TPRNEU` (devs deliberately retain control) →
  `hitl-workflow`, not here. Human-directed control → `hitl-workflow`.
- **Examples:** `95CPB7CF` — intent-level telemetry exposes drift from architectural intent; `8AW26GFK`
  — agents make unreviewed architectural decisions ("vibe architecting").

#### Family 4 — GOVERNANCE & POLICY LANDSCAPE

**`theme:org-governance`** (renamed from `governance-frameworks`, 2026-07-15) · ~9
- **Captures:** the **organizational governance apparatus** — how governance is applied *broadly* across
  the org, pulling oversight together: policy, **audit logging / audit trails**, accountability, roles,
  maturity models, responsible-adoption, runtime policy-as-code. The org's own rules for AI code.
- **Boundary:** the *holistic org-level* governance structure — **not** a single pipeline-integratable
  framework (that's `facet:framework`) and not external law (`regulatory-compliance`). Pairs as
  `org-governance` (internal) / `regulatory-compliance` (external).
- **Examples:** `B4TVIG5Y` — org maturity model for AI-assisted dev; `XJAXB98T` — 12 GenAI governance
  strategies across 67 OSS projects; `HBR7QZ2C` — policy engine → runtime enforcement for agentic AI.

**`theme:regulatory-compliance`** · ~10
- **Captures:** external regulation/standards and legal accountability — EU AI Act Art.14, NIST AI RMF,
  ISO 42001, liability, auditor-ready evidence.
- **Boundary:** driven by an *external* mandate/law/standard. Internal org governance → `org-governance`.
- **Examples:** `XZEHQYNZ` — operationalizing EU AI Act human-oversight for agentic SE; `UW2R6BBJ` —
  NIST AI RMF into lifecycle controls with evidence artifacts; `27YULT5I` — accountability/transparency
  in regulated-finance code migration.

#### Family 5 — SUPPLY CHAIN & PROVENANCE

**`theme:tooling-supply-chain`** (T1) · *full write-up below*
- **Captures:** provenance & vetting of the **AI tooling** that writes/touches code (agent *skills*,
  *MCP servers*, external agents) as its own oversight surface; poisoned/hallucinated dependencies;
  **+ attacks on the oversight layer** (framing attacks, evasion, spec-gaming — a supply-chain attack
  on the reviewer, absorbed from the dissolved T3).
- **Boundary:** governance of *what enters* (tools/deps) and *attacks on the reviewer*, distinct from
  reviewing the emitted code. **D4 ruling (Scott, 2026-07-18, final):** dependency risk
  *in generated code* — hallucinated/poisoned packages the AI writes in — → `ai-code-insecurity`,
  NOT here; this theme keeps the AI *tooling* (skills/MCP/agents entering the toolchain) and attacks
  on the reviewer. Excludes keyword false-positives (hardware
  trojans, classic SolarWinds-class incidents).
- **Examples:** `6ZC3H7AF` — 26% of scanned agent skills carry ≥1 vulnerability, minimal vetting;
  *attacks:* `X7EN6DXZ` — PR-metadata framing biases LLM review, 100% attack success; `T3XTXIXW` —
  obfuscation reliably bypasses CoT LLM review.

**`theme:provenance-auditability`** · ~7
- **Captures:** traceability/provenance of AI *changes* so a human **can** review them — an auditable
  record of what changed and why; IP/licensing vetting; certified components.
- **Boundary:** restoring *reviewability/auditability of the output*, and it **requires a persistent
  record/trace** — a *point-in-time* "what is it using right now" view that captures nothing is
  `oversight-explanation` (pull), not provenance (sharpened 2026-07-18, Lumen). Vetting the *tools* →
  `tooling-supply-chain`.
- **Examples:** `2KPHQ5IV` — AI code leaves no auditable record; typed-graph consensus layer restores it;
  `RG4A4D6K` — provenance-tracking given 20–30% enterprise code is GenAI; `VCI88UZD` — human-certified
  module repositories with provenance + interface contracts.

### Decision log & scoping calls (2026-07-14)
- **`untrusted-overseer` (T3) — DISSOLVED, papers redistributed (Scott, 2026-07-14).** The original T3
  conflated two strands; rather than a standalone theme (scope-expansion risk), its papers were absorbed
  into existing themes:
  - **Attacks on the oversight mechanism** (framing attacks flipping verdicts, obfuscation evading the
    reviewer, spec-gaming/evaluation-evasion: `X7EN6DXZ` `T3XTXIXW` `WBS9U5N7` `T8E8SCCG`) →
    **`theme:tooling-supply-chain`** (an attack on the reviewer is a supply-chain attack on the oversight layer).
  - **Independent / cross-model verification and its reliability limits** — what Scott had called
    "adversarial agents" (one agent validating another): LLM-judge bias, over-rejection, spec-conformance
    misjudgment, AI-reviewing-AI circularity (`BAWCBT9R` `A5WDGC7J` `UDVHQ5HR` `TA6GIUK2` `5NZ2EDEK`) →
    **`theme:ai-review`** (its reliability-limits dimension).
  - No `theme:overseer-reliability` / no standalone T3. **Terminology:** call the agent-checks-agent case
    *independent / cross-model verification*, not "adversarial" — reserve "adversarial" for the attack sense.
- **`spec-driven-guardrails` — RESOLVED → context, NOT a theme (Scott, 2026-07-14).** Secure-by-
  construction / spec-as-gate / executable-requirements / active-rules (`C88VGWMI` `TA6GIUK2` `7SH86C2W`
  `JCTP8VXP` `6ZW9QNQH` `WRXR2VTP`) constrain *what gets generated* — by the oversight-vs-steering
  discriminator this is **steering, not oversight**, so it does not get a solution theme (consistent with
  `DPKKMXSA` and other steering papers). Such a paper still gets tagged by any *oversight* facet it does
  carry (e.g. `TA6GIUK2`'s AI-reviewing-AI point → `ai-review` limits); the steering contribution itself
  is context.
- **`theme:remediation-gating` — ADDED (Scott, 2026-07-14).** Fills the **Fix** slot in the
  Detect→Triage→Fix→Escalate pipeline; scoped to *oversight of autonomous fixes* (gating/filtering/
  escalating the fix), not the repair technique. Thin at present (seed `GAD5Z8PV`) — populate in the sweep.
- **HOS axes thin at the core tier** (kept as HOS-side design findings, not themes): context-window
  assembly ("less is more"), cost-tiered review economics.
- **Detect-stage naming (Scott, 2026-07-14):** the two detector themes are named for legibility to a
  non-specialist reader — `theme:ai-review` (**probabilistic** detector — AI judges, can hallucinate)
  and `theme:rules-based-checks` (**deterministic** detector — grounded/checkable, incl. tests & formal
  methods). Kept **separate** (retracting the earlier fold idea): the judgment-vs-grounded distinction is
  the load-bearing "gate on a computed, producer-independent signal" axis and `TA6GIUK2`'s
  "AI-reviewing-AI is circular without an executable spec." Both sit under **Detect** in the
  Detect→Triage→Fix→Escalate pipeline.
- **`theme:formal-methods` — ADDED as a composable technique tag (Scott, 2026-07-15).** Resolves the
  "is formal methods really rules-based?" question without splitting a standalone solution theme.
  Formal methods is a *technique* orthogonal to the *performer*: pair `formal-methods` with `ai-review`
  (AI does it) or `rules-based-checks` (classical engine does it). This makes the **rename of
  `rules-based-checks` unnecessary** (the technique is now tagged separately) and **encodes the adoption
  hypothesis** in the taxonomy: classical+human-authored = niche/high-assurance; **AI-automated
  (autoformalization) = the plausible uptake path** because it removes the spec/proof-authoring burden
  practitioners actually object to — gated on the check being cheap/fast (economics caveat). Added
  **now** because it is *additive* (doesn't redefine existing themes) and no Set A paper involves formal
  methods, so it doesn't disturb the frozen calibration.
- **Open pruning question:** Family 1's three problem themes could collapse toward one
  `theme:problem-evidence` if the problem side should be smaller. Left expanded pending review.
- **`oversight-explanation` BROADENED + freeze lifted → human vetting pass (Scott, 2026-07-18).**
  Reading Lumen `VG6CIDQW` (Set A), the human overturned all four models' **unanimous** primary
  `hitl-workflow` — a category error, not a ranking call: Lumen's "context control" lever is
  *input-side steering*, and its oversight contribution is comprehension. `provenance-auditability`
  was also rejected (point-in-time view, no persistent record). Resolution: `oversight-explanation`
  = **helping the human understand what the AI is doing** — *push* (decision-ready escalation
  handoff) or *pull* (human-invoked visibility); "context transparency" relocated out of
  `hitl-workflow` (now levers-only); steering exclusion extended to input-side control; transparency
  routing rule added to the preamble. **Process change:** the instrument freeze is lifted — Scott is
  human-tagging the calibration papers as a *vocabulary-vetting pass*; the human-vs-model experiment
  then runs on the vetted instrument (models re-run both sets; Set A human tags are model-informed,
  Set B is the clean comparison). See `Taxonomy_Changelog.md` §11.
- **Set A audit decisions (Scott, 2026-07-18 EOD; changelog §16–§17).** `automation-bias` requires a
  **capable** human (capability discriminator; `22JBEZNK` example → counter-example; the
  oversight-competence-gap candidate is now arbiter-validated). `problem-statement-anchor` bar =
  the **overall** problem statement only; **never on `lit-review`**. `lit-review` = systematic OR
  narrative (synthesized-not-produced test); lit-review primary = **biggest-tent** theme. Mode
  **tie-rule**: reviewable unit dominates initiator. Workflow: **struggle signal** (primary struggle /
  definition-stretching → check the core bar). VibeGuard `remediation-gating` recurrence →
  **compression-gap principle**: every boundary that has ever caught a human must appear in the
  compressed instrument, not just this reference.
- **`steering` + `non-developer` facets — ADDED (Scott, 2026-07-18, vetting pass).** `steering` =
  contribution-type flag (solution operates on generation; audit trail for the steering exclusion;
  steering-only → demote candidate). `non-developer` = population scope flag (end-user/business-user/
  citizen-developer settings; the democratization endgame), completing the mode/object/population
  scope axes and serving as tripwire for the staged *oversight-competence-gap* theme candidate
  (22JBEZNK seed). Facet count 10 → 12. Changelog §12.
- **`assistive` / `agentic` generation-mode facet pair — ADDED (Scott, 2026-07-18).** The oversight
  problem differs qualitatively by mode — acceptance-moment micro-decisions (automation-bias evidence)
  vs artifact-level gating (the scaling inversion + the solution pipeline) — and the axis is not
  recoverable from existing tags. Added **mid-Set-B** under the `formal-methods` precedent: purely
  *additive* scope facets (no theme redefined), so Set A model outputs are undisturbed; the 20
  calibration papers get backfilled in the post-Set-B iteration; TF56EPIP's human tags predate the
  pair. Logged as `Taxonomy_Changelog.md` §10.
- **`design-only` form facet — ADDED (Scott, 2026-07-19, Set B pass).** Positive marker for
  "mechanism specified in buildable detail but never credibly run" (mock demos that fabricate their
  own outputs don't count as building — R4WJZBSF worked example). Motivated by the human stretching
  `intro-framing` to record proposal-ness on R4WJZBSF — evidence the vocabulary had a hole; absence
  of `built-system` was the only carrier and absence is ambiguous. Completes the maturity spectrum
  intro-framing → design-only → built-system → adopted; design-only solution = demote tripwire
  (unevaluated-framework discriminator). Mid-Set-B under the §10 additive precedent. Facet count
  14 → 15; menu 32 → 33. Changelog §19.
- **`metrics` contribution facet — ADDED (Scott, 2026-07-20, Set B pass).** Defines-vs-uses
  guardrail; measurand-rationale rule; object supplied by co-tagged themes (a separate `risks`
  facet was considered and rejected — mention-saturation). Paired with the `risk-routing` boundary
  line: signal-without-allocation ≠ routing (the R4WJZBSF stretch). Risk-quantification instrument
  family staged with a sweep-cluster tripwire. Facet count 15 → 16; menu 33 → 34. Changelog §20.
- **`risk-ip` + `risk-bias` risk-type flags — ADDED (Scott, 2026-07-20, Set B pass).** Bounded
  membership-exception flags for risk types with no theme home, powering the synthesis
  risk×mitigation matrix; substantive-treatment bar (metric / mitigation / empirical result / focal
  analysis — never intro-lists); themed risks excluded (their themes are the columns). Facet count
  16 → 18; menu 34 → 36; facet checklist five → six questions. Changelog §21.
- **`routing-signal` contribution flag — ADDED (Scott, 2026-07-21, E95T8E88 probe; landed
  same-conversation on two-catch evidence).** Signal-framed-for-review-attention without
  operationalized selection; audit trail for the signal-without-allocation boundary (steering
  grammar); mutually exclusive with theme:risk-routing; Triage supply-chain roster. Facet count
  26 → 27; menu 44 → 45. Changelog §29.
- **Data-collection method family — ADDED (Scott, 2026-07-20, B644HQFS probe).**
  `method-self-report` / `method-mining` / `method-experiment` / `method-field-study` — the SLR
  study-characteristics axis; own-evidence-only; multi-apply; lit-reviews get none. Facet count
  21 → 25; menu 39 → 43; checklist six → seven questions. Changelog §25.
- **Risk-flag family made UNIFORM — `risk-security` + `risk-quality` + `risk-overreliance` ADDED
  (Scott, 2026-07-20, same day).** The §21 homeless-only scoping made matrix columns depend on
  rationale text-matching for themed risks (heterogeneous inclusion bars — a methods-validity
  problem the arbiter flagged three ways). Now one bar for all five flags; flag = engagement,
  theme = lift, co-occurrence expected. Also: explainability three-way routing (judging-support →
  oversight-explanation · code comprehensibility → quality · model-XAI → general-ai); measurand
  fixed vocabulary; define-only ≠ theme-membership line (first catch: R4WJZBSF automation-bias +
  oversight-explanation over-tags). Facet count 18 → 21; menu 36 → 39. Changelog §22.

⚠️ **Namespace note:** a *legacy* topical `theme:*` set already exists at scale (`theme:governance` 170,
`theme:oversight` 163, `theme:risk` 104, `theme:orgs` 105, …) from an earlier bulk pass. Exact-slug
filtering on the synthesis slugs above is unambiguous; decide separately whether to re-prefix synthesis
themes (e.g. `syn:<slug>`) or leave them.

---

## Theme 1 — The AI-tooling supply chain as an under-governed oversight surface

**One line:** software supply-chain governance is a mature, largely *solved* discipline for
open-source dependencies (allowlists, provenance/SLSA, review gates) — but it has **not** been
extended to the AI tooling that now writes and touches code (agent *skills*, *MCP servers*,
externally-sourced agents), which install and execute with *implicit trust and minimal vetting*.
Governing the **provenance and vetting of the tools** is an oversight surface in its own right,
distinct from reviewing the code they emit.

**Origin:** Scott's practitioner observation — Microsoft (and mature orgs) enforce strict OSS
supply-chain security (approved-package allowlists, restrict-to-vetted, SLSA provenance, review
processes). The same discipline *should* apply to externally-sourced skills/agents, but the
evidence shows it currently doesn't — so the analysis must scope the supply chain **broadly**.

**Three layers to scope:**
- **Layer 0 — the established discipline to inherit from:** `7S24HQUN` (accountability in
  algorithmic supply chains), `2WGHN2NR` (reproducible builds), the SLSA/provenance cluster
  (`3PZZ4ADM`, `NTVE3RS8`, `P2KI2BFW`, `T49KME27`…), `CMNVQ7CX` (code provenance).
- **Layer 1 — the code the AI *generates* (poisoned/hallucinated dependencies):** `2KQ93JHX`
  (package hallucination / slopsquatting), `QKWS7WF4` + `TA8IPAW4` (trojan-trigger detection in
  code LLMs). *(Numerous model-poisoning studies exist but were mostly discarded as model-internals
  without an org-oversight angle: `7FKKZFHN`, `PK3MHVVN`, `GUR6XUU2`, `W49WX6KP`, `HUVIWYNF`.)*
- **Layer 2 — the AI *tooling* itself, sourced externally (the new surface):**
  - **Anchor:** `6ZC3H7AF` "Agent Skills in the Wild" — 26.1% of 31,132 scanned skills carry ≥1
    vulnerability (prompt injection, data exfiltration, privilege escalation, supply-chain), 5.2%
    high-severity; skills "execute with implicit trust and minimal vetting."
  - Defenses/architecture: `RMRMXUT4` (skill-poisoning attack taxonomies + defense architectures),
    `CIP9FBM3` (MCP-server security, empirical), `7ECA3PNE` (MCP guardian), `CJ6UBWCX`
    (authorization boundary / AI gateways), `Z6RB7NDA` (secure tool-integration patterns),
    `33HNWZ53` (AgentClick — skill-based human-in-the-loop review), `LZPAIXTQ` (model supply-chain
    security).

**Why it's core-relevant (not just security trivia):** it is *oversight of what enters the
codebase* — the provenance/vetting gate for the tools, mirroring the code-review gate for the
output. It connects to the oversight-scaling inversion (`Problem_Statement_Evidence.md`): the same
"install and run with minimal vetting" reflex that merges AI PRs unreviewed also installs agent
skills unvetted.

**Research angle:** treat externally-sourced agent tooling as a **new dependency class** requiring
the same — or adapted — software-supply-chain governance (allowlists, provenance, vetting/review
gates); characterize where that governance exists, where it's absent, and what adaptation the
agentic setting demands.

**Scope note — keyword false positives excluded:** hardware trojans (`DMLNDC2K`, `TPRVD7RL`,
`GNN4TJ`, `SPICED`), classic/general supply-chain incidents (`2DWGC5EB` SolarWinds/Kaseya, the xz
news items, `SH5GMI78` Industry-5.0, `TQ9696RG` logistics), and MCP-labelled off-topic items
(`I9RZSX7J` Llama-3, `RBI76C2G` MCP marketplace commerce) matched the sweep but are out of scope.

---

## Theme 2 — Explanation comprehensibility: the last mile of oversight

**One line:** an accurate escalation or finding is **inert if the human can't act on it**.
Effective oversight requires the AI's *handoff explanation* to be comprehensible and
decision-ready to a reviewer who is **not already embedded in the code** — which means
**upleveling** from code-level detail to a decision framing: *context → the problem →
options/tradeoffs*. Routing the human's attention (see `VTDG995V`) is only half the job; the
handoff explanation is the other half, and it is where oversight silently fails.

**Scope broadened (2026-07-18):** the theme now covers the *information side of oversight*
generally — not only the **push** handoff this write-up describes, but **pull** comprehension
tooling the human invokes to see what the AI is doing/using (Lumen `VG6CIDQW`: context/dependency
visibility in assistive mode). The write-up below is the push/agentic manifestation; the Tag
reference above is the operative definition.

**Anchor — `7UB2MD8Z`** (Explainable automated debugging / AutoSD): empirical — participants
*with* explanations judged AI-generated patch correctness **more accurately in 5 of 6 bugs**, and
the tool signals *when it is confident*. The unstated corollary (and the design crux): the
explanation only helps if it is comprehensible — an accurate escalation with an opaque rationale
does not improve the human's gate decision.

**Corpus cross-refs:**
- `IM6DJDEE` — its "Consultation Request Packs" / "Merge-Readiness Packs" are exactly structured
  escalation/handoff artifacts for this; the vocabulary for a decision-ready explanation.
- `VTDG995V` — attention-routing (confidence → review intensity) is the complement: *where* to look
  vs *what to understand once you look*.

**Practitioner instance (HOS field note).** In HOS, raw model-generated explanations assumed the
reader was already embedded in the code, so they were **unusable to the very reviewer being
escalated to** (escalated *because* they are not in the weeds). Fix: force structure — explicit
instructions to supply **context, articulate the problem, and lay out options/tradeoffs** — and
**uplevel the discussion** from implementation minutiae to the decision level. This is the
real-world validation of the theme; recorded in HOS `Improvements/ENHANCEMENT_IDEAS.md`.

**Why core-relevant:** the explanation is the **interface between the AI's finding and the human's
gate decision** — an oversight mechanism (core Part-2), with empirical support. It is the design
dimension the tool-capability/eval papers miss.

**Research angle:** characterize what makes an oversight/escalation explanation *actionable* —
abstraction level (upleveling), required context, and explicit options/tradeoffs — as a first-class
design requirement of scalable human oversight, not an afterthought.

---

## Synthesis / theme-tag vocabulary (for the theme-tagging pass)

**→ The operative reference is the [Tag reference — full working vocabulary](#tag-reference--full-working-vocabulary-2026-07-14)
section at the top of this doc** (facet tags + all theme tags, each with what it captures, boundaries,
and example keys, plus how the three tag layers stack and what's mutually exclusive). This section is
kept only as a pointer so there is a single source of truth.

Synthesis tags are distinct from the screening-lineage tags (`source:`, `s1:`, `s2:`, `s3:`,
`centrality:`, `superseded-by:`, `cocite:`): they mark *why an item matters to the argument*,
independent of core/context disposition, and are applied liberally (an item can carry several).
