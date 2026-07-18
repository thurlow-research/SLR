# Theme-tagging cheat-sheet (Vibe Coding Governance SLR)

Tag on the **document contents**. **Multi-tag freely** — a paper can carry several themes.
Tag on **membership** (the paper *contributes to* that theme's argument), **not mention**.
Pick **one PRIMARY theme** (the paper's home / where it'd be written up in depth).
**Steering exclusion:** shaping what gets *generated* — prompts, specs, fine-tuning, **controlling the AI's inputs/context** — is steering, NOT oversight; tag only the paper's inspection/comprehension/gating contribution.

## THEME TAGS (`theme:<slug>`)

**Problem — quantify**
- `oversight-scaling-inversion` — AI code is riskier yet *less* inspected; PRs auto-merged unreviewed; review is the bottleneck; burden piles on maintainers
- `ai-code-insecurity` — empirical **security**-vulnerability evidence in AI code (CWEs, insecure-but-confident)
- `quality-debt` — **non-security** quality decay: tech debt, complexity, smells, maintainability, breaking changes

**Limits of current oversight**
- `automation-bias` — the *human* fails: over-trust, complacency, skill erosion, misses flaws even when warned
- `oversight-theater` — review exists on paper but lacks authority/time/info to change the outcome (rubber-stamp, token HITL)

**Solution — the Detect → Triage → Fix → Escalate pipeline**
- `ai-review` — [DETECT] AI *judges* the artifact (probabilistic, can hallucinate); incl. multi-agent / cross-model review **and its reliability limits**
- `rules-based-checks` — [DETECT] deterministic **grounded** checks: tests, static analysis/lint, symbolic exec, sandbox, classical formal-methods engines
- `formal-methods` — [technique, COMPOSABLE] theorem proving / model checking / symbolic exec / autoformalization. Pair with the performer: AI does it → `ai-review`+`formal-methods`; classical engine → `rules-based-checks`+`formal-methods`
- `risk-routing` — [TRIAGE] the **allocation decision** — *which/whether/when* AI items reach a human & at what tier; the **smarts of surfacing** (signal + selection/tiering logic). NOT the human's control mechanism. **(= WHAT gets surfaced)**
- `remediation-gating` — [FIX] oversight of autonomous **fixes** (gate / filter / escalate the fix) — not the repair technique itself
- `hitl-workflow` — [ESCALATE] the human's **control surface** — *how the human acts* once engaged: checkpoints, action guards, approval gates, bounded delegation. NOT what to surface. **Levers, not lenses** (comprehension/visibility tools → `oversight-explanation`; a lever over the AI's *inputs* is steering). **(= HOW + WHEN the human acts)**
- `oversight-explanation` — [ESCALATE·info side] **help the human understand what the AI is doing** — *push*: decision-ready escalation handoff (background + options + recommendation + risks) OR *pull*: human-invoked visibility into what the AI is doing/using (context/dependency views). Lens, not lever (lever → `hitl-workflow`)
- `agent-scope-drift` — [cross-cutting] agents wander off-mandate / make unreviewed decisions; keeping them in scope

**Governance & policy**
- `org-governance` — the *org-level governance apparatus* applied broadly: policy, **audit logging**, accountability, roles, maturity models, policy-as-code (internal; ≠ a single pipeline framework)
- `regulatory-compliance` — *external* law/standards: EU AI Act Art.14, NIST AI RMF, ISO 42001, liability, audit evidence

**Supply chain & provenance**
- `tooling-supply-chain` — provenance/vetting of the AI **tools** (skills/MCP/agents); **+ attacks on the reviewer**
- `provenance-auditability` — traceability of AI **changes** so a human *can* review; auditable record; IP/licensing. Requires a **persistent record** — a point-in-time "what's in use now" view → `oversight-explanation`

## FACET TAGS (functional role; orthogonal — optional, apply if they fit)
- `problem-statement-anchor` — a single committee-sit-up empirical stat
- `survey-input` — adoption / preference / RAI-priority finding useful for the org survey design
- `intro-framing` — position / agenda / definitional paper that *names the gap*
- `lit-review` — secondary literature (survey / review / meta-analysis)

**Artifact / evidence cluster** (composable; form → maturity):
- `framework` — a **technical framework / reference architecture integratable into a build pipeline** (whether or not built). ≠ `theme:org-governance` (the org apparatus). A bare taxonomy/decision-model gets neither. Composes: `framework`+`built-system`+`adopted`.
- `built-system` — the authors *implemented* it as a working system/tool/prototype ("and they built it")
- `adopted` — used **outside research** (commercial / production / real org use), beyond a lab prototype/benchmark. Scarce, high-signal; absence = prototype/proposal
- `general-ai` — [scope flag] governance/oversight is **general AI/LLM, not coding-specific** (model robustness, general RAI frameworks). Default (untagged) = coding-specific. Flags candidates for context.

**Generation-mode scope pair** (which *setting* the paper studies; cut on **who initiates + the reviewable unit**, NOT tool location — agents live in IDEs too):
- `assistive` — **human-initiated, suggestion-granularity** generation (inline completion, chat-paste): the human authors in the flow, accepts piece-by-piece. Oversight surface = the *acceptance moment*.
- `agentic` — **AI-initiated / AI-planned multi-step work** delivered at **artifact/PR granularity** for review. Oversight surface = the *gate*.
- Apply either or **both** (paper compares/spans modes); **neither** = mode unspecified / irrelevant to the paper's claim.

**Contribution / population flags:**
- `steering` — [contribution flag] the paper's proposed solution (wholly/partly) operates on **generation** (prompts, specs, fine-tuning, shaping model inputs) rather than inspecting/gating the artifact. **Contribution, not topic.** Steering-**only** solution → demote candidate
- `non-developer` — [scope flag] the generating/overseeing human is **not a professional developer** (end-user / business user / citizen developer). Default (untagged) = professional devs

## WORKFLOW
- **PRIMARY** (one per paper; not in the menu — type it): `cal:human:primary:theme:<slug>` (same tail as the membership tag, `primary:` prepended).
  - **Tie-breaker** when a paper spans adjacent themes (route↔control-surface, AI-check↔human-gate): primary = the theme carrying its **distinctive novelty**, not the standard scaffolding.
- **DEMOTE flag** (menu): `demote:context` — this core looks like it belongs in context (any reason: general-AI, tool-benchmark, not operationalizable). Flag it and keep going; batch-reviewed later. (`demote:discard` by the same pattern.)
