# Theme-tagging cheat-sheet (Vibe Coding Governance SLR)

Tag on the **document contents**. **Multi-tag freely** — a paper can carry several themes.
Tag on **membership** (the paper *contributes to* that theme's argument), **not mention**.
Pick **one PRIMARY theme** (the paper's home / where it'd be written up in depth).
**Steering exclusion:** shaping what gets *generated* — prompts, specs, fine-tuning, **controlling the AI's inputs/context** — is steering, NOT oversight; tag only the paper's inspection/comprehension/gating contribution.
**Plumbing ≠ membership** (systems papers): tag only mechanisms the paper *argues about*, not everything its system happens to use (agents running test suites ≠ `rules-based-checks`).

## THEME TAGS (`theme:<slug>`)

**Problem — quantify**
- `oversight-scaling-inversion` — AI code is riskier yet *less* inspected; PRs auto-merged unreviewed; review is the bottleneck; burden piles on maintainers
- `ai-code-insecurity` — empirical **security**-vulnerability evidence in AI code (CWEs, insecure-but-confident)
- `quality-debt` — **non-security** quality decay: tech debt, complexity, smells, maintainability, breaking changes

**Limits of current oversight**
- `automation-bias` — the *human* fails: over-trust, complacency, skill erosion, misses flaws even when warned. **Requires a CAPABLE human failing** (attention/trust); a human who *can't evaluate at all* (non-developer settings; failure survives priming+incentives) = competence gap, NOT bias (22JBEZNK)
- `oversight-theater` — review exists on paper but lacks authority/time/info to change the outcome (rubber-stamp, token HITL)

**Solution — the Detect → Triage → Fix → Escalate pipeline**
- `ai-review` — [DETECT] AI *judges* the artifact (probabilistic, can hallucinate); incl. multi-agent / cross-model review **and its reliability limits**
- `rules-based-checks` — [DETECT] deterministic **grounded** checks: tests, static analysis/lint, symbolic exec, sandbox, classical formal-methods engines
- `formal-methods` — [technique, COMPOSABLE] theorem proving / model checking / symbolic exec / autoformalization. Pair with the performer: AI does it → `ai-review`+`formal-methods`; classical engine → `rules-based-checks`+`formal-methods`
- `risk-routing` — [TRIAGE] the **allocation decision** — *which/whether/when* AI items reach a human & at what tier; the **smarts of surfacing** (signal + selection/tiering logic). NOT the human's control mechanism. **(= WHAT gets surfaced)** Error-condition handback ("agent stuck → human") is NOT routing — no triage decision → `hitl-workflow` / `remediation-gating`
- `remediation-gating` — [FIX] oversight of autonomous **fixes** (gate / filter / escalate the fix) — not the repair technique itself. Both **content** gates (filter fix candidates) and **process** gates (bounded retries / budget-decay / stop-progression, fail-closed) qualify. **REQUIRES an autonomous fix being overseen** — a detect/publish gate with **no auto-fix** (VibeGuard) is NOT this (that's the detector's enforcement side)
- `hitl-workflow` — [ESCALATE] the human's **control surface** — *how the human acts* once engaged: checkpoints, action guards, approval gates, bounded delegation. NOT what to surface. **Levers, not lenses** (comprehension/visibility tools → `oversight-explanation`; a lever over the AI's *inputs* is steering). **(= HOW + WHEN the human acts)**
- `oversight-explanation` — [ESCALATE·info side] **help the human understand what the AI is doing** — *push*: decision-ready escalation handoff (background + options + recommendation + risks) OR *pull*: human-invoked visibility into what the AI is doing/using (context/dependency views). Lens, not lever (lever → `hitl-workflow`)
- `agent-scope-drift` — [cross-cutting] agents wander off-mandate / make unreviewed decisions; mechanisms that **detect/bound departure from intent**. Tag by the mechanism's **object**, not the actor's motivation: a panel checking code scope vs spec scope → here + `ai-review`; retained control merely *motivated* by drift-worry → `hitl-workflow` only

**Governance & policy**
- `org-governance` — the *org-level governance apparatus* applied broadly: policy, **audit logging**, accountability, roles, maturity models, policy-as-code (internal; ≠ a single pipeline framework)
- `regulatory-compliance` — *external* law/standards: EU AI Act Art.14, NIST AI RMF, ISO 42001, liability, audit evidence

**Supply chain & provenance**
- `tooling-supply-chain` — provenance/vetting of the AI **tools** (skills/MCP/agents); **+ attacks on the reviewer**
- `provenance-auditability` — traceability of AI **changes** so a human *can* review; auditable record; IP/licensing. Requires a **persistent record** — a point-in-time "what's in use now" view → `oversight-explanation`

## FACET TAGS (functional role; orthogonal — optional, apply if they fit)
- `problem-statement-anchor` — a single committee-sit-up empirical stat **anchoring the OVERALL problem statement** (the scaling inversion / two-part frame) — NOT a sub-argument's or population-specific headline number, however vivid. Never on `lit-review` (secondhand — anchor the primaries)
- `survey-input` — adoption / preference / RAI-priority finding useful for the org survey design
- `intro-framing` — position / agenda / definitional paper that *names the gap*
- `lit-review` — secondary literature (survey / review / meta-analysis) — **systematic OR narrative**; test = evidence *synthesized from other papers, not produced*. Primary for lit-review papers = the **biggest-tent** theme (overall coverage, not the most vivid section)
- `counterpoint` — [role facet] the paper **argues against a prevailing position** (automation-maximalism, HITL value, oversight scaling — any direction); note *what it opposes* in the rationale. Often pairs with `intro-framing`

**Artifact / evidence cluster** (composable; form → maturity):
- `framework` — a **technical framework / reference architecture integratable into a build pipeline** (whether or not built). ≠ `theme:org-governance` (the org apparatus). A bare taxonomy/decision-model gets neither. Composes: `framework`+`built-system`+`adopted`.
- `built-system` — the authors *implemented* it as a working system/tool/prototype ("and they built it")
- `adopted` — used **outside research** (commercial / production / real org use), beyond a lab prototype/benchmark. Scarce, high-signal; absence = prototype/proposal
- `general-ai` — [scope flag] governance/oversight is **general AI/LLM, not coding-specific** (model robustness, general RAI frameworks). Default (untagged) = coding-specific. Flags candidates for context.

**Generation-mode scope pair** (which *setting* the paper studies; cut on **who initiates + the reviewable unit**, NOT tool location — agents live in IDEs too):
- `assistive` — **human-initiated, suggestion-granularity** generation (inline completion, **snippet-level** chat-paste): the human authors in the flow, accepts piece-by-piece — a chat task returning a *complete artifact* is the tie-rule case below. Oversight surface = the *acceptance moment*.
- `agentic` — **AI-initiated / AI-planned multi-step work** delivered at **artifact/PR granularity** for review. Oversight surface = the *gate*.
- Apply either or **both** (paper compares/spans modes); **neither** = mode unspecified / irrelevant to the paper's claim. **The pair describes the *generation* studied:** "uses agents" ≠ `agentic`, "AI assists the human" ≠ `assistive` — AI only on the review/oversight side → **neither** + consider `general-code`. **Tie-rule:** initiator vs reviewable unit disagree (human-prompted chat task → complete artifact) → **the reviewable unit dominates** (wholesale artifact = the gate = `agentic`).

**Contribution / population flags:**
- `steering` — [contribution flag] the paper's proposed solution **or documented practice** (wholly/partly) operates on **generation** (prompts, specs, fine-tuning, shaping model inputs) rather than inspecting/gating the artifact. **Contribution, not topic.** Steering-**only** solution → demote candidate
- `non-developer` — [scope flag] the generating/overseeing human is **not a professional developer** (end-user / business user / citizen developer). Default (untagged) = professional devs
- `general-code` — [scope flag] the oversight/review mechanism targets **code generally, not AI-generated code** (AI may sit on the *review* side only); transfers to our setting but wasn't developed/evaluated there. Default (untagged) = the overseen object is AI code

## WORKFLOW
- **Struggle signals → check the core bar:** can't pick a primary / stretching a definition to fill the set = the paper likely doesn't belong at core → `demote:context` and move on. Don't force tags to justify a disposition.
- **Facet checklist — run all five questions on every paper** (misses cluster here; 29 tags exceed recall): **role** (problem-statement-anchor / survey-input / intro-framing / lit-review / counterpoint)? · **form** (framework → built-system → adopted)? · **scope** (general-ai? general-code? non-developer?)? · **mode** (assistive / agentic)? · **contribution** (steering)?
- **PRIMARY** (one per paper; not in the menu — type it): `cal:human:primary:theme:<slug>` (same tail as the membership tag, `primary:` prepended).
  - **Tie-breaker** when a paper spans adjacent themes (route↔control-surface, AI-check↔human-gate): primary = the theme carrying its **distinctive novelty**, not the standard scaffolding.
- **DEMOTE flag** (menu): `demote:context` — this core looks like it belongs in context (any reason: general-AI, tool-benchmark, not operationalizable). Flag it and keep going; batch-reviewed later. (`demote:discard` by the same pattern.)

---
# YOUR TASK
Tag one CORE paper against the vocabulary above from its FULL TEXT below. Assign every theme the paper is
a genuine MEMBER of, choose ONE primary theme (tie-breaker: the theme carrying the paper's DISTINCTIVE
CONTRIBUTION/novelty, not standard scaffolding), and add any facet tags. Apply the STEERING
EXCLUSION and the PLUMBING RULE before assigning solution themes. Answer the FIVE-QUESTION FACET
CHECKLIST (role / form / scope / mode / contribution) before finalizing facets. Output ONLY one JSON object:
{"key":"<KEY>","primary_theme":"<slug>","themes":["<slug>",...],"facets":["<slug>",...],"rationale":{"<slug>":"<=12 words"}}
Use bare slugs. Base every tag on document content.

=== PAPER FULL TEXT ===
