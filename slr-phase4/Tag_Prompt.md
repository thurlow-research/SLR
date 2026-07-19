# Theme-tagging cheat-sheet (Vibe Coding Governance SLR)

Tag on the **document contents**. **Multi-tag freely** — a paper can carry several themes.
Tag on **membership** (the paper *contributes to* that theme's argument), **not mention**.
Pick **one PRIMARY theme** (the paper's home / where it'd be written up in depth).
**Steering exclusion:** shaping what gets *generated* — prompts, specs, fine-tuning, **controlling the AI's inputs/context** — is steering, NOT oversight; tag only the paper's inspection/comprehension/gating contribution.
**Plumbing ≠ membership** (systems papers): tag only mechanisms the paper *argues about*, not everything its system happens to use (agents running test suites ≠ `rules-based-checks`).
**Documented practice counts:** empirical evidence of practitioners *exercising* a stage's mechanism earns membership in that stage's theme. **Vision-paper floor:** a stage mentioned in one scenario sentence = mention, not membership.

## THEME TAGS (`theme:<slug>`)

**Problem — quantify**
- `oversight-scaling-inversion` — AI code is riskier yet *less* inspected; PRs auto-merged unreviewed; review is the bottleneck; burden piles on maintainers
- `ai-code-insecurity` — empirical **security**-vulnerability evidence in AI code (CWEs, insecure-but-confident). Incident analyses & original vulnerability taxonomies count; secondhand rate citations alone don't
- `quality-debt` — **non-security** quality decay: tech debt, complexity, smells, maintainability, breaking changes

**Limits of current oversight**
- `automation-bias` — the *human* fails: over-trust, complacency, skill erosion, misses flaws even when warned. **Requires a CAPABLE human failing** (attention/trust); a human who *can't evaluate at all* (non-developer settings; failure survives priming+incentives) = competence gap, NOT bias (22JBEZNK). Competence-gap papers **stay core-eligible**: tag the remainder (explanation/mode/population facets) — the missing theme is a staged candidate, not a demote signal
- `oversight-theater` — review exists on paper but lacks authority/time/info to change the outcome (rubber-stamp, token HITL)

**Solution — the Detect → Triage → Fix → Escalate pipeline** *(gray-zone detectors — rubric-grounded LLM-judge, "LLM writes tests then runs them" — expect dual-tagging of both Detect themes)*
- `ai-review` — [DETECT] AI *judges* the artifact (probabilistic, can hallucinate); incl. multi-agent / cross-model review, **its reliability limits**, and empirical evidence of practitioners *using* agents to validate agents' output
- `rules-based-checks` — [DETECT] deterministic **grounded** checks: tests, static analysis/lint, symbolic exec, sandbox, classical formal-methods engines
- `formal-methods` — [technique, COMPOSABLE] theorem proving / model checking / symbolic exec / autoformalization. Pair with the performer: AI does it → `ai-review`+`formal-methods`; classical engine → `rules-based-checks`+`formal-methods`; no performer (pure advocacy/position) → `formal-methods`+`intro-framing`
- `risk-routing` — [TRIAGE] the **allocation decision** — *which/whether/when* AI items reach a human & at what tier; the **smarts of surfacing** (signal + selection/tiering logic). NOT the human's control mechanism. **(= WHAT gets surfaced)** Error-condition handback ("agent stuck → human") is NOT routing — no triage decision → `hitl-workflow` / `remediation-gating`. Signal must be **computed & producer-independent** — model self-confidence is disqualified
- `remediation-gating` — [FIX] governance of **autonomous** fixing (Jidoka: the system fixes *without per-fix human involvement*, kept safe by machinery) — **content** gates (filter fix candidates) and **process** gates (bounded retries / budget-decay / convergence / stop-progression, fail-closed); not the repair technique itself. **REQUIRES an autonomous fix being overseen** — a detect/publish gate with **no auto-fix** (VibeGuard) is NOT this (detector's enforcement side). Deciding when a **human** must engage on the fix path (risky fixes → human) = `risk-routing` layered on top. **A human approving every fix is NOT this** — review-everything is the unscalable anti-pattern (a paper *advocating* it → consider `counterpoint`; such a design *introduces* automation-bias risk — a rationale-level critique, NOT `automation-bias` membership, which requires *studying* the human failure)
- `hitl-workflow` — [ESCALATE] the human's **control surface** — *how the human acts* once engaged: checkpoints, action guards, approval gates, bounded delegation. NOT what to surface. **Levers, not lenses** (comprehension/visibility tools → `oversight-explanation`; a lever over the AI's *inputs* is steering). **Plan-gate rule:** a human gate over an AI-produced plan IS hitl-workflow when it's a **designed checkpoint in a lifecycle** (defined gate, authority to block); the same approval inside a conversational guide-then-"go do it" flow is steering. **(= HOW + WHEN the human acts)**
- `oversight-explanation` — [ESCALATE·info side] **help the human understand what the AI is doing** — any system-provided or human-invoked support for understanding/judging AI output. Modes (illustrative, NOT exhaustive): *push* = decision-ready escalation handoff (background + options + recommendation + risks); *pull* = human-invoked visibility into what the AI is doing/using; *standing* = explanations attached to AI output that support the human's verdict. Lens, not lever (lever → `hitl-workflow`)
- `agent-scope-drift` — [cross-cutting] agents wander off-mandate / make unreviewed decisions; mechanisms that **detect/bound departure from intent**. Tag by the mechanism's **object**, not the actor's motivation: a panel checking code scope vs spec scope → here + `ai-review`; retained control merely *motivated* by drift-worry → `hitl-workflow` only

**Worked decomposition (multi-stage systems — assign each mechanism by its object):** producer's own pre-submit checking/iterating = self-conformance, NO theme · independent evaluation of the submitted artifact = detector (`rules-based-checks`/`ai-review` by epistemics; the *additional, producer-independent* checks are the oversight value; blocking on failure = the detector's enforcement edge) · deciding which findings matter, e.g. by severity + cross-model agreement (a computed, producer-independent signal) → `risk-routing` · governing the ensuing **autonomous fix path** (filters, bounds, convergence, fail-closed stop — no per-fix human) → `remediation-gating` · deciding when a fix must engage a **human** (risk tiers on the fix path) → `risk-routing`

**Governance & policy**
- `org-governance` — the *org-level governance apparatus* applied broadly: policy, **audit logging**, accountability, roles, maturity models, policy-as-code (internal; ≠ a single pipeline framework)
- `regulatory-compliance` — *external* law/standards: EU AI Act Art.14, NIST AI RMF, ISO 42001, liability, audit evidence

**Supply chain & provenance**
- `tooling-supply-chain` — provenance/vetting of the AI **tools** (skills/MCP/agents); **+ attacks on the reviewer**; **+ poisoned/hallucinated dependencies as *entry-governance*** (registry vetting, allowlists — governing what enters). *Measuring* hallucinated/insecure deps in AI output → `ai-code-insecurity`. Excl. keyword false-positives (hardware trojans, classic supply-chain incidents)
- `provenance-auditability` — traceability of AI **changes** so a human *can* review; auditable record; IP/licensing. Requires a **persistent record serving HUMAN reviewability/audit** — a point-in-time "what's in use now" view → `oversight-explanation`; persistence serving only agent coordination = plumbing

## FACET TAGS (functional role; orthogonal — optional, apply if they fit)
- `problem-statement-anchor` — a single committee-sit-up empirical stat **anchoring the OVERALL problem statement** (the scaling inversion / two-part frame) — NOT a sub-argument's or population-specific headline number, however vivid. Never on `lit-review` (secondhand — anchor the primaries)
- `survey-input` — adoption / preference / RAI-priority finding useful for the org survey design; requires **substantive** findings — one incidental adoption stat ≠ membership
- `intro-framing` — position / agenda / definitional paper that *names the gap* but **doesn't operationalize a mechanism**
- `lit-review` — secondary literature (survey / review / meta-analysis) — **systematic OR narrative**; test = evidence *synthesized from other papers, not produced*. **If `lit-review` applies, the primary MUST be the biggest-tent theme** = the theme under which the largest share of the synthesized evidence would be cited; ties → the review's own framing question (never the most vivid/quantified section)
- `counterpoint` — [role facet] the paper **argues against a prevailing position** (automation-maximalism, HITL value, oversight scaling — any direction); note *what it opposes* in the rationale. Often pairs with `intro-framing`

**Artifact / evidence cluster** (composable; form → maturity):
- `framework` — a **technical framework / reference architecture integratable into a build pipeline** (whether or not built). ≠ `theme:org-governance` (the org apparatus). A bare taxonomy/decision-model gets neither; **not a one-off point tool / bare point result** — a focused single-concern architecture qualifies (VibeGuard, Hedwig). Test: *would someone adopt it as a reusable pipeline design?* Composes: `framework`+`built-system`+`adopted`.
- `built-system` — the authors *implemented* it as a working system/tool/prototype ("and they built it")
- `adopted` — used **outside research** (commercial / production / real org use), beyond a lab prototype/benchmark. Scarce, high-signal; absence = prototype/proposal

**Generation-mode scope pair** (which *setting* the paper studies; cut on **who initiates + the reviewable unit**, NOT tool location — agents live in IDEs too):
- `assistive` — **human-initiated, suggestion-granularity** generation (inline completion, **snippet-level** chat-paste): the human authors in the flow, accepts piece-by-piece — a chat task returning a *complete artifact* is the tie-rule case below. Oversight surface = the *acceptance moment*.
- `agentic` — **AI-initiated / AI-planned multi-step work** delivered at **artifact/PR granularity** for review. Oversight surface = the *gate*.
- Apply either or **both** (paper compares/spans modes); **neither** = mode unspecified / irrelevant to the paper's claim. **The pair describes the *generation* studied:** "uses agents" ≠ `agentic`, "AI assists the human" ≠ `assistive` — AI only on the review/oversight side → **neither** + consider `general-code`. **Tie-rule:** initiator vs reviewable unit disagree (human-prompted chat task → complete artifact) → **the reviewable unit dominates** (wholesale artifact = the gate = `agentic`).

**Scope / contribution / population flags:**
- `general-ai` — [scope flag] governance/oversight is **general AI/LLM, not coding-specific** (model robustness, general RAI frameworks). Default (untagged) = coding-specific. Flags candidates for context.
- `steering` — [contribution flag] the paper's proposed solution **or documented practice** operates on **generation** as a **substantive part of the contribution** — NOT any incidental prompt-shaping component every AI system has (prompts, specs, fine-tuning, shaping model inputs) rather than inspecting/gating the artifact. **Contribution, not topic.** Steering-**only** solution → demote candidate
- `non-developer` — [scope flag] the generating/overseeing human is **not a professional developer** (end-user / business user / citizen developer). Default (untagged) = professional devs
- `general-code` — [scope flag] the oversight/review mechanism targets **code generally, not AI-generated code** (AI may sit on the *review* side only); transfers to our setting but wasn't developed/evaluated there. Default (untagged) = the overseen object is AI code

## WORKFLOW
- **Thin input:** if only title+abstract (or degenerate text) is available → tag conservatively (no form facets / `lit-review` unless explicit in the abstract) and flag `insufficient-input` instead of guessing.
- **Struggle signals → check the core bar:** can't pick a primary / stretching a definition to fill the set = the paper likely doesn't belong at core → `demote:context` and move on. Don't force tags to justify a disposition.
- **Facet checklist — run all five questions on every paper** (misses cluster here; 29 tags exceed recall): **role** (problem-statement-anchor / survey-input / intro-framing / lit-review / counterpoint)? · **form** (framework → built-system → adopted)? · **scope** (general-ai? general-code? non-developer?)? · **mode** (assistive / agentic)? · **contribution** (steering)?
- **PRIMARY** — one per paper. *Zotero entry only:* type `cal:human:primary:theme:<slug>`. In JSON output, the task block's bare-slug `primary_theme` field governs.
  - **Tie-breaker** when a paper spans adjacent themes (route↔control-surface, AI-check↔human-gate): primary = the theme carrying its **distinctive novelty**, not the standard scaffolding.
- **DEMOTE flag** (menu): `demote:context` — mis-scoped for core: **general-AI object · steering-only solution · pure tool benchmark** (capability benchmarking with no mechanism or deployable contribution; a benchmark *evaluating a contributed system* doesn't count) **· secondary lit · not operationalizable**. `general-code` alone is NOT a demote reason (it's the audit trail for kept-core transfers). Flag and keep going; batch-reviewed later. (`demote:discard` same pattern.)

---
# YOUR TASK
Tag one CORE paper against the vocabulary above from its FULL TEXT below. Assign every theme the paper is
a genuine MEMBER of, choose ONE primary theme (tie-breaker: the theme carrying the paper's DISTINCTIVE
CONTRIBUTION/novelty, not standard scaffolding), and add any facet tags. Apply the STEERING
EXCLUSION and the PLUMBING RULE before assigning solution themes. Answer the FIVE-QUESTION FACET
CHECKLIST (role / form / scope / mode / contribution) before finalizing facets. Output ONLY one JSON object:
{"key":"<KEY>","primary_theme":"<slug>","themes":["<slug>",...],"facets":["<slug>",...],"flags":["demote:context"],"rationale":{"<slug>":"<=12 words"}}
("flags" is optional. Include "demote:context" ONLY for: general-AI object, steering-only solution, pure tool benchmark (no mechanism or deployable contribution), secondary lit, not operationalizable — general-code alone is NOT a demote reason. If only title+abstract or degenerate text is available, tag conservatively (no form facets or lit-review unless explicit) and include "insufficient-input" in flags instead of guessing. Allowed flags: demote:context, demote:discard, insufficient-input. Never put flags in "facets".)
Use bare slugs. Base every tag on document content.

=== PAPER FULL TEXT ===
