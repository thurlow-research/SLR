# Set B — Human Calibration Tagging Packet

**You tag these 10 first (blind).** Then I run Opus + codex + agy on the same 10 and we compare.
Read the **document contents** (each paper is in Zotero → **02-Human Calibration Run**, with PDF + TXT).

**How to record:** fill the template at the bottom (or tag in Zotero — your call). For each paper:
- **Primary** = the one home theme.
- **Themes** = all `theme:` slugs that fit (membership, not mention).
- **Facets** = any facet tags that apply. **Run the five-question facet checklist on every paper**
  (misses cluster here): **role** (anchor / survey-input / intro-framing / lit-review / counterpoint)? · **form**
  (framework → built-system → adopted)? · **scope** (general-ai? general-code? non-developer?)? · **mode**
  (assistive / agentic)? · **contribution** (steering)?
- (optional) a few words of *why* for the primary.

---

## Vocabulary cheat-sheet

*(Refreshed 2026-07-18 to match `Tag_Cheatsheet.md` — the earlier packet embedded a stale v0-vintage
copy. The Zotero Actions menu was already current. **Backfill note:** TF56EPIP was tagged before the
`assistive`/`agentic` pair existed — revisit it for the mode facet.)*

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
- `automation-bias` — the *human* fails: over-trust, complacency, skill erosion, misses flaws even when warned
- `oversight-theater` — review exists on paper but lacks authority/time/info to change the outcome (rubber-stamp, token HITL)

**Solution — the Detect → Triage → Fix → Escalate pipeline**
- `ai-review` — [DETECT] AI *judges* the artifact (probabilistic, can hallucinate); incl. multi-agent / cross-model review **and its reliability limits**
- `rules-based-checks` — [DETECT] deterministic **grounded** checks: tests, static analysis/lint, symbolic exec, sandbox, classical formal-methods engines
- `formal-methods` — [technique, COMPOSABLE] theorem proving / model checking / symbolic exec / autoformalization. Pair with the performer: AI does it → `ai-review`+`formal-methods`; classical engine → `rules-based-checks`+`formal-methods`
- `risk-routing` — [TRIAGE] the **allocation decision** — *which/whether/when* AI items reach a human & at what tier; the **smarts of surfacing** (signal + selection/tiering logic). NOT the human's control mechanism. **(= WHAT gets surfaced)** Error-condition handback ("agent stuck → human") is NOT routing — no triage decision → `hitl-workflow` / `remediation-gating`
- `remediation-gating` — [FIX] oversight of autonomous **fixes** (gate / filter / escalate the fix) — not the repair technique itself. Both **content** gates (filter fix candidates) and **process** gates (bounded retries / budget-decay / stop-progression, fail-closed) qualify
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
- `problem-statement-anchor` — a single committee-sit-up empirical stat
- `survey-input` — adoption / preference / RAI-priority finding useful for the org survey design
- `intro-framing` — position / agenda / definitional paper that *names the gap*
- `lit-review` — secondary literature (survey / review / meta-analysis)
- `counterpoint` — [role facet] the paper **argues against a prevailing position** (automation-maximalism, HITL value, oversight scaling — any direction); note *what it opposes* in the rationale. Often pairs with `intro-framing`

**Artifact / evidence cluster** (composable; form → maturity):
- `framework` — a **technical framework / reference architecture integratable into a build pipeline** (whether or not built). ≠ `theme:org-governance` (the org apparatus). A bare taxonomy/decision-model gets neither. Composes: `framework`+`built-system`+`adopted`.
- `built-system` — the authors *implemented* it as a working system/tool/prototype ("and they built it")
- `adopted` — used **outside research** (commercial / production / real org use), beyond a lab prototype/benchmark. Scarce, high-signal; absence = prototype/proposal
- `general-ai` — [scope flag] governance/oversight is **general AI/LLM, not coding-specific** (model robustness, general RAI frameworks). Default (untagged) = coding-specific. Flags candidates for context.

**Generation-mode scope pair** (which *setting* the paper studies; cut on **who initiates + the reviewable unit**, NOT tool location — agents live in IDEs too):
- `assistive` — **human-initiated, suggestion-granularity** generation (inline completion, chat-paste): the human authors in the flow, accepts piece-by-piece. Oversight surface = the *acceptance moment*.
- `agentic` — **AI-initiated / AI-planned multi-step work** delivered at **artifact/PR granularity** for review. Oversight surface = the *gate*.
- Apply either or **both** (paper compares/spans modes); **neither** = mode unspecified / irrelevant to the paper's claim. **The pair describes the *generation* studied:** "uses agents" ≠ `agentic`, "AI assists the human" ≠ `assistive` — AI only on the review/oversight side → **neither** + consider `general-code`.

**Contribution / population flags:**
- `steering` — [contribution flag] the paper's proposed solution **or documented practice** (wholly/partly) operates on **generation** (prompts, specs, fine-tuning, shaping model inputs) rather than inspecting/gating the artifact. **Contribution, not topic.** Steering-**only** solution → demote candidate
- `non-developer` — [scope flag] the generating/overseeing human is **not a professional developer** (end-user / business user / citizen developer). Default (untagged) = professional devs
- `general-code` — [scope flag] the oversight/review mechanism targets **code generally, not AI-generated code** (AI may sit on the *review* side only); transfers to our setting but wasn't developed/evaluated there. Default (untagged) = the overseen object is AI code


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
