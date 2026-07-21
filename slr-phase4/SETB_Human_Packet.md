# Set B — Human Calibration Tagging Packet

**You tag these 10 first (blind).** Then I run Opus + codex + agy on the same 10 and we compare.
Read the **document contents** (each paper is in Zotero → **02-Human Calibration Run**, with PDF + TXT).

**How to record:** fill the template at the bottom (or tag in Zotero — your call). For each paper:
- **Primary** = the one home theme. Tie-breaker: distinctive novelty, not scaffolding. **Altitude:** prefer the most specific theme that still captures where the paper's main effort lives — but a component mechanism inside a broader contribution does not outrank it.
- **Themes** = all `theme:` slugs that fit (membership, not mention).
- **Facets** = any facet tags that apply. **Run the seven-question facet checklist on every paper**
  (misses cluster here): **role** (anchor / survey-input / intro-framing / lit-review / counterpoint)? · **form**
  (design-only | framework → built-system → adopted)? · **scope** (general-ai? general-code? non-developer?)? · **mode**
  (assistive / agentic)? · **contribution** (steering? metrics?)? · **risk-types** (security / quality / over-reliance / ip / bias —
  substantive treatment only, never intro-lists)? · **method** (self-report / mining / experiment / field-study — own evidence only)?
- **Thin input:** if only title+abstract (or degenerate text) is available → tag conservatively (no form facets / `lit-review` unless explicit in the abstract) and flag `insufficient-input` instead of guessing.
- **Struggle signals → check the core bar:** can't pick a primary / stretching a definition = likely `demote:context`.
- **Thin input:** title+abstract only → tag conservatively (no form facets / `lit-review` unless explicit) + flag `insufficient-input`.
- (optional) a few words of *why* for the primary.

---

## Vocabulary cheat-sheet

*(Refreshed 2026-07-18 to match `Tag_Cheatsheet.md` — the earlier packet embedded a stale v0-vintage
copy. The Zotero Actions menu was already current. **Backfill note:** TF56EPIP was tagged before the
`assistive`/`agentic` pair existed — revisit it for the mode facet. **2026-07-19:** `design-only` form
facet added mid-Set-B off the R4WJZBSF probe (changelog §19) — menu now 33 toggles, re-import needed;
papers 1–9 of this set are unaffected unless one proposes an unbuilt mechanism. **2026-07-20:** roster
reconciled — Set B = exactly the 10 below (calib_sets.json now agrees); ZUM76CCG, which sat in the
02-Human collection but never in this packet, is NOT Set B — it seeds **Set C** (AI-tag-first,
human-validate; calibration doc §5·7); TF56EPIP restored to the 02-Human collection.)*

Tag on the **document contents**. **Multi-tag freely** — a paper can carry several themes.
Tag on **membership** (the paper *contributes to* that theme's argument), **not mention**.
Pick **one PRIMARY theme** (the paper's home / where it'd be written up in depth; tie-breaker and lit-review override below).
**Steering exclusion:** shaping what gets *generated* — prompts, specs, fine-tuning, **controlling the AI's inputs/context** — is steering, NOT oversight; tag only the paper's inspection/comprehension/gating contribution.
**Plumbing ≠ membership** (systems papers): tag only mechanisms the paper *argues about*, not everything its system happens to use (agents running test suites ≠ `rules-based-checks`).
**Documented practice counts:** empirical evidence of practitioners *exercising* a stage's mechanism earns membership in that stage's theme. **Vision-paper floor:** a stage mentioned in one scenario sentence = mention, not membership.

## THEME TAGS (`theme:<slug>`)

**Problem — quantify**
- `oversight-scaling-inversion` — AI code is riskier yet *less* inspected; PRs auto-merged unreviewed; review is the bottleneck; burden piles on maintainers
- `ai-code-insecurity` — empirical **security**-vulnerability evidence in AI code (CWEs, insecure-but-confident), **incl. hallucinated/poisoned dependencies in the output** (D4 ruling). Incident analyses & original vulnerability taxonomies count; secondhand rate citations alone don't
- `quality-debt` — **non-security** quality decay: tech debt, complexity, smells, maintainability, breaking changes

**Limits of current oversight**
- `automation-bias` — the *human* fails: over-trust, complacency, skill erosion, misses flaws even when warned. **Requires a CAPABLE human failing** (attention/trust); a human who *can't evaluate at all* (non-developer settings; failure survives priming+incentives) = competence gap, NOT bias (22JBEZNK). Competence-gap papers **stay core-eligible**: tag the remainder (explanation/mode/population facets) — the missing theme is a staged candidate, not a demote signal
- `oversight-theater` — review exists on paper but lacks authority/time/info to change the outcome (rubber-stamp, token HITL)

**Solution — the Detect → Triage → Fix → Escalate pipeline** *(gray-zone detectors — rubric-grounded LLM-judge, "LLM writes tests then runs them" — expect dual-tagging of both Detect themes)*
- `ai-review` — [DETECT] AI *judges* the artifact (probabilistic, can hallucinate); incl. multi-agent / cross-model review, **its reliability limits**, and empirical evidence of practitioners *using* agents to validate agents' output
- `rules-based-checks` — [DETECT] deterministic **grounded** checks: tests, static analysis/lint, symbolic exec, sandbox, classical formal-methods engines
- `formal-methods` — [technique, COMPOSABLE] theorem proving / model checking / symbolic exec / autoformalization. Pair with the performer: AI does it → `ai-review`+`formal-methods`; classical engine → `rules-based-checks`+`formal-methods`; no performer (pure advocacy/position) → `formal-methods` + the `intro-framing` *facet*
- `risk-routing` — [TRIAGE] the **allocation decision** — *which/whether/when* AI items reach a human & at what tier; the **smarts of surfacing** (signal + selection/tiering logic). NOT the human's control mechanism. **(= WHAT gets surfaced)** Error-condition handback ("agent stuck → human") is NOT routing — no triage decision → `hitl-workflow` / `remediation-gating`. Signal must be **computed & producer-independent** — model self-confidence is disqualified. **Defining a risk metric/score without the allocation decision is NOT routing** → `metrics` facet
- `remediation-gating` — [FIX] governance of **autonomous** fixing (Jidoka: the system fixes *without per-fix human involvement*, kept safe by machinery) — **content** gates (filter fix candidates) and **process** gates (bounded retries / budget-decay / convergence / stop-progression, fail-closed); not the repair technique itself. **REQUIRES an autonomous fix being overseen** — a detect/publish gate with **no auto-fix** (VibeGuard) is NOT this (detector's enforcement side). Deciding when a **human** must engage on the fix path (risky fixes → human) = `risk-routing` layered on top
  - *Anti-pattern note:* a human approving **every** fix is NOT remediation-gating — review-everything is the unscalable anti-pattern (a paper *advocating* it → `counterpoint` candidate). Such a design *introduces* automation-bias risk — that's a critique to note, NOT `automation-bias` membership (membership requires the paper to *study* the human failure)
- `hitl-workflow` — [ESCALATE] the human's **control surface** — *how the human acts* once engaged: checkpoints, action guards, approval gates, bounded delegation. NOT what to surface. **Levers, not lenses** (comprehension/visibility tools → `oversight-explanation`; a lever over the AI's *inputs* is steering). **Plan-gate rule:** a human gate over an AI-produced plan IS hitl-workflow when it's a **designed checkpoint in a lifecycle** (defined gate, authority to block); the same approval inside a conversational guide-then-"go do it" flow is steering. **(= HOW + WHEN the human acts)**
- `oversight-explanation` — [ESCALATE·info side] **help the human understand what the AI is doing** — any system-provided or human-invoked support for understanding/judging AI output. Modes (illustrative, NOT exhaustive): *push* = decision-ready escalation handoff (background + options + recommendation + risks); *pull* = human-invoked visibility into what the AI is doing/using; *standing* = explanations attached to AI output that support the human's verdict. Lens, not lever (lever → `hitl-workflow`). **Explainability routes by object:** support for judging the AI/its output → here; **comprehensibility of the code itself** (unclear logic, undocumented) → `quality-debt` territory / `risk-quality`; model-XAI → `general-ai`
- `agent-scope-drift` — [cross-cutting] agents wander off-mandate / make unreviewed decisions; mechanisms that **detect/bound departure from intent**. Tag by the mechanism's **object**, not the actor's motivation: a panel checking code scope vs spec scope → here + `ai-review`; retained control merely *motivated* by drift-worry → `hitl-workflow` only

**Worked decomposition (multi-stage systems — assign each mechanism by its object):** producer's own pre-submit checking/iterating = self-conformance, NO theme · independent evaluation of the submitted artifact = detector (`rules-based-checks`/`ai-review` by epistemics; the *additional, producer-independent* checks are the oversight value; blocking on failure = the detector's enforcement edge) · deciding which findings matter, e.g. by severity + cross-model agreement (a computed, producer-independent signal) → `risk-routing` · governing the ensuing **autonomous fix path** (filters, bounds, convergence, fail-closed stop — no per-fix human) → `remediation-gating` · deciding when a fix must engage a **human** (risk tiers on the fix path) → `risk-routing`

**Governance & policy**
- `org-governance` — the *org-level governance apparatus* applied broadly: policy, **audit logging**, accountability, roles, maturity models, policy-as-code (internal; ≠ a single pipeline framework)
- `regulatory-compliance` — *external* law/standards: EU AI Act Art.14, NIST AI RMF, ISO 42001, liability, audit evidence

**Supply chain & provenance**
- `tooling-supply-chain` — provenance/vetting of the AI **tools** (skills/MCP/agents); **+ attacks on the reviewer**. **Dependency risk *in generated code*** (hallucinated/poisoned packages the AI writes in) → `ai-code-insecurity`, NOT here (D4 ruling). Excl. keyword false-positives (hardware trojans, classic supply-chain incidents)
- `provenance-auditability` — traceability of AI **changes** so a human *can* review; auditable record; IP/licensing. Requires a **persistent record serving HUMAN reviewability/audit** — a point-in-time "what's in use now" view → `oversight-explanation`; persistence serving only agent coordination = plumbing

## FACET TAGS (functional role; orthogonal — optional, apply if they fit)
- `problem-statement-anchor` — a single committee-sit-up empirical stat **anchoring the OVERALL problem statement** (the scaling inversion / two-part frame) — NOT a sub-argument's or population-specific headline number, however vivid. Never on `lit-review` (secondhand — anchor the primaries)
- `survey-input` — adoption / preference / RAI-priority finding useful for the org survey design; requires **substantive** findings — one incidental adoption stat ≠ membership
- `intro-framing` — position / agenda / definitional paper that *names the gap* but **doesn't operationalize a mechanism**
- `lit-review` — secondary literature (survey / review / meta-analysis) — **systematic OR narrative**; test = evidence *synthesized from other papers, not produced*. **A framing related-work section ≠ this facet** — the facet is the PAPER's role; a paper producing its own results with a review as framing is primary literature. **If `lit-review` applies, the primary MUST be the biggest-tent theme** = the theme under which the largest share of the synthesized evidence would be cited; ties → the review's own framing question (never the most vivid/quantified section)
- `counterpoint` — [role facet] the paper **argues against a prevailing position** (automation-maximalism, HITL value, oversight scaling — any direction); note *what it opposes* in the rationale. Often pairs with `intro-framing`

**Artifact / evidence cluster** (composable; form → maturity):
- `framework` — a **technical framework / reference architecture integratable into a build pipeline** (whether or not built). ≠ `theme:org-governance` (the org apparatus). A bare taxonomy/decision-model gets neither; **not a one-off point tool / bare point result** — a focused single-concern architecture qualifies (VibeGuard, Hedwig). Test: *would someone adopt it as a reusable pipeline design?* Composes: `framework`+`built-system`+`adopted`.
- `design-only` — the paper **specifies a mechanism in buildable detail** (components, formulas, thresholds, architecture) **but never credibly runs it**: no working implementation, no evaluation on the intended object. **A mock demo ≠ built** — a demo that fabricates the mechanism's core outputs (random/synthetic stand-ins for what it's supposed to compute) is still design-only (R4WJZBSF). Only for papers that *propose* something — an empirical study with no proposed mechanism gets nothing. Mutually exclusive with `built-system`/`adopted`; composes with `framework`. ≠ `intro-framing` (which specifies NO mechanism — discriminator = buildable detail; **a stated architectural-design contribution qualifies even when realization is deferred to a research agenda** — F9JM9CI6 ruling). Core bar: **what+how carve-out** — names the elements to track AND defines operationalizable metrics → **clears the bar as measurement even unevaluated** (R4WJZBSF); what-only enumerations / borrowed-metrics / unevaluated frameworks *without* defined metrics → context candidates
- `built-system` — the authors *implemented* it as a working system/tool/prototype ("and they built it")
- `adopted` — used **outside research** (commercial / production / real org use), beyond a lab prototype/benchmark. Scarce, high-signal; absence = prototype/proposal. **Pilot rule:** "outside the research *context*" ≠ "outside the research *org*" — a pilot/case study run *as the paper's field evaluation* (org = study site) evidences `built-system`, NOT adoption; `adopted` = use for the org's **own operational purposes**, continuing beyond the study (integrated/org-initiated/ongoing)

**Generation-mode scope pair** (which *setting* the paper studies; cut on **who initiates + the reviewable unit**, NOT tool location — agents live in IDEs too):
- `assistive` — **human-initiated, suggestion-granularity** generation (inline completion, **snippet-level** chat-paste): the human authors in the flow, accepts piece-by-piece — a chat task returning a *complete artifact* is the tie-rule case below. Oversight surface = the *acceptance moment*.
- `agentic` — **AI-initiated / AI-planned multi-step work** delivered at **artifact/PR granularity** for review. Oversight surface = the *gate*.
- Apply either or **both** (paper compares/spans modes); **neither** = mode unspecified / irrelevant to the paper's claim. **The pair describes the *generation* studied:** "uses agents" ≠ `agentic`, "AI assists the human" ≠ `assistive` — AI only on the review/oversight side → **neither** + consider `general-code`. **Tie-rule:** initiator vs reviewable unit disagree (human-prompted chat task → complete artifact) → **the reviewable unit dominates** (wholesale artifact = the gate = `agentic`).

**Scope / contribution / population / risk-type flags:**
- `general-ai` — [scope flag] governance/oversight is **general AI/LLM, not coding-specific** (model robustness, general RAI frameworks). Default (untagged) = coding-specific. Flags candidates for context.
- `steering` — [contribution flag] the paper's proposed solution **or documented practice** operates on **generation** (prompts, specs, fine-tuning, shaping model inputs) rather than inspecting/gating the artifact, as a **substantive part of the contribution** — NOT any incidental prompt-shaping component every AI system has. **Contribution, not topic.** Steering-**only** solution → demote candidate
- `metrics` — [contribution flag] the paper **defines metrics/scores/indices** (risk, quality, oversight, compliance) **as a deliverable** — not merely *uses* metrics to evaluate something (every empirical paper has an evaluation apparatus; that gets nothing). **Contribution, not apparatus.** The metrics' *object* comes from co-tagged themes (+`regulatory-compliance` = compliance-risk metrics; + an oversight theme = oversight metrics). Composes with `design-only` (defined, never run on real data — R4WJZBSF) or with problem themes (defined AND applied → the findings earn the theme; the facet marks the reusable instrument). **Rationale MUST name the measurand** using the fixed vocabulary: security · quality · comprehensibility · over-reliance · ip-plagiarism · bias · compliance · privacy. **Defining a metric for X does NOT by itself earn X's theme** (define-only → `metrics` + the matching `risk-*` flag; the theme requires the lift — first catch: R4WJZBSF)
- `non-developer` — [scope flag] the generating/overseeing human is **not a professional developer** (end-user / business user / citizen developer). Default (untagged) = professional devs
- `general-code` — [scope flag] the oversight/review mechanism targets **code generally, not AI-generated code** (AI may sit on the *review* side only); transfers to our setting but wasn't developed/evaluated there. Default (untagged) = the overseen object is AI code
- `risk-security` / `risk-quality` / `risk-overreliance` / `risk-ip` / `risk-bias` — [risk-type flags, uniform bar] **substantive treatment of the harm**: defines a metric for it · contributes/evaluates a mitigation for it · reports an empirical result about it · devotes focal analysis. **An intro risk-list sentence = mention, NO tag** — rationale cites which clause fired. Types: security · quality (incl. **code comprehensibility** — "explainability of the code") · over-reliance · IP/plagiarism/licensing · bias in generated code. **Flag ≠ theme:** the flag marks substantive engagement (define-level suffices); the matching theme (`ai-code-insecurity` / `quality-debt` / `automation-bias`) still requires the paper to *do the lift* — heavy-lift papers carry **both** (expected co-occurrence). Matrix: identified/measured axis = these flags, one query, one bar. **Lit-reviews CAN earn these flags via focal secondhand synthesis** (2CKL96B8: security+quality) — the matrix segments secondhand engagement via `lit-review`; passing enumeration still never fires; `problem-statement-anchor` stays never-on-lit-review. `risk-ip`/`risk-bias` have no theme home — a contribution-level cluster promotes flag → theme

**Data-collection method facets** (data-source axis — how the paper's **own evidence** was produced):
- `method-self-report` (humans tell you: questionnaires, interviews, focus groups, diaries) · `method-mining` (artifacts measured: repos, PRs, commits, posts, logs, telemetry) · `method-experiment` (controlled tasks with manipulation, lab or crowdsourced) · `method-field-study` (deployment / case study observed in a real setting). **Apply all that fit** (mixed methods expected — a survey + observation study gets two). Applies to the paper's **own evidence production**: `lit-review` papers get **none** (evidence synthesized — the methods live in the primaries); absence = no empirical evidence produced (position papers, pure designs). Note `method-self-report` ≠ `survey-input` (method vs the finding's utility to the org survey — a mined study can be survey-input). **World-or-tool test:** results describing the *world* → method facet; results describing only the *tool* (benchmarks, self-run tests over constructed corpora) → no facet, that's `built-system` evaluation; a detector run over real repos gets `method-mining` only if the findings characterize the repos. Humans using the artifact always fires one: **assigned tasks / controlled conditions → `method-experiment`; real work, own setting, natural use → `method-field-study`** (study-site pilots & case-study evaluations = field-study); both can apply. **Subjects may be systems:** controlled studies of *third-party* tools/models whose findings characterize those systems = `method-experiment` (UDVHQ5HR); running **your own** system on a benchmark — even a standardized third-party one (UB2EVUFU on ProjDevBench) — is still tool-results, no facet (whose-properties test; benchmark-grade evidence = a `built-system` maturity note, staged `benchmark-evaluated` candidate)


---

## The 10 papers (Set B)

| # | Key | Title |
|---|---|---|
| 1 | `B644HQFS` | "An Endless Stream of AI Slop": How Developers Discuss AI-generated code |
| 2 | `6DXZGHD9` | A generative-AI cybersecurity risks mitigation model |
| 3 | `E95T8E88` | What to cut? Predicting unnecessary methods in agentic code |
| 4 | `7V7SRG43` | CodeAgent: autonomous communicative agents for code review |
| 5 | `UW2R6BBJ` | Secure AI-SDLC for critical infrastructure (NIST AI RMF) |
| 6 | `BAWCBT9R` | Bias in the loop: auditing LLM-as-a-judge for SE |
| 7 | `E3E5YA2E` | Redefining the programmer: human-AI collaboration |
| 8 | `5VTAJISY` | Human-in-the-loop software development agents (HULA) |
| 9 | `TF56EPIP` | Rethinking autonomy: preventing failures in AI-driven software |
| 10 | `R4WJZBSF` | A framework for quantifying ethical & regulatory risks |

---

## Fill-in template

```
1. B644HQFS  primary: __________   themes: __________________   facets: ________   why: ____
2. 6DXZGHD9  primary: __________   themes: __________________   facets: ________   why: ____
3. E95T8E88  primary: __________   themes: __________________   facets: ________   why: ____
4. 7V7SRG43  primary: __________   themes: __________________   facets: ________   why: ____
5. UW2R6BBJ  primary: __________   themes: __________________   facets: ________   why: ____
6. BAWCBT9R  primary: __________   themes: __________________   facets: ________   why: ____
7. E3E5YA2E  primary: __________   themes: __________________   facets: ________   why: ____
8. 5VTAJISY  primary: __________   themes: __________________   facets: ________   why: ____
9. TF56EPIP  primary: __________   themes: __________________   facets: ________   why: ____
10. R4WJZBSF primary: __________   themes: __________________   facets: ________   why: ____
```
