# SLR Handoff — Theme Tagging (Instrument Validated → Set B)

**Vibe Coding Governance SLR · Zotero group 6505702 · 2026-07-18 (supersedes the 2026-07-15 handoff)**
**Next thing to do:** Scott's pending decisions (§2) → **Scott tags Set B blind** under the frozen
instrument → models tag Set B fresh → human-vs-model comparison → full 148-core sweep.
**At the start of the new chat: invoke `slr-conventions`**, read this file, then
`slr-phase4/Taxonomy_Changelog.md` (§10–§18 = today's full audit trail) and
`Methodology/Theme_Tagging_Calibration.md` §5 (revised design) + §7 (vetting log).
`.envrc` supplies keys (direnv; RO for reads, RW for writes).

---

## 1. Where we are — the 2026-07-18 validation cycle is COMPLETE

The instrument (17 themes + 14 facets + flags) went through a five-stage validation in one day and
is now **frozen at v2.1 + altitude rule** (repo `thurlow-research/SLR`, main @ `2c6bbc5`):

1. **Set A human vetting pass** (all 10 papers tagged/verified in Zotero; §7 log rows 1–10).
   ~20 instrument products, changelog §10–§17. Headlines: **two 4-model-unanimous primaries
   overturned by the human** (Lumen `VG6CIDQW` steering/category error §11; 22JBEZNK
   capability-vs-bias §16); VibeGuard recurrence → **compression-gap principle** (every
   human-catching boundary must be in the compressed copy, not just the Tag reference).
2. **Known-answer dry-run** — 5 blind fresh Fable taggers: 8/10 primaries, all regression checks
   pass; 4 residuals fixed.
3. **3-critic adversarial panel** (Fable 5 / GPT-5 Codex high / Gemini 3.1 Pro High, frozen input,
   human tags only): ~40 findings, merged in `slr-phase4/data/critique/DISPOSITION.md`; all
   A(schema)/B(compression-gap)/C(sharpening) groups applied; boundary questions D1–D4 ruled by
   Scott (§3 below). Critique input embeds copyrighted full texts → **gitignored**; regenerate with
   `slr-phase4/tools/build_critique_input.py`.
4. **Set A retag (improvement gate)** — 3 fresh models under v2: primaries 6/10 → **fable 10/10,
   codex 9/10, gemini 9/10** (after two human re-adjudications, §3); theme Jaccard .50–.66 →
   .67–.78; **facet Jaccard doubled** (.34–.42 → .61–.70); demote flags work.
5. **Round-2 smoke test** (10 revision-introduced defects fixed → v2.1) + **altitude-rule
   regression test 8/9** (codex flipped back on UB2EVUFU — the guard works; all hold-checks stable).

**Data layout:** `slr-phase4/data/tags/` = v1 model outputs (also archived `tags-v1/`) ·
`tags-v2/` = v2 retag · `tags-v21/` = altitude regression · `critique/` = panel JSONs +
DISPOSITION.md. Instrument copies (`Tag_Cheatsheet.md`, `Tag_Prompt.md` = cheatsheet + task block,
`SETB_Human_Packet.md`) are **kept in lockstep** — copy drift is a named instrument bug.

## 2. PENDING — Scott's queue at handoff

*(Update, same day: items 1–3 DONE — gate = PASS; Set A backfills written & all 10 items verified;
Actions menu re-imported. Remaining: items 4–5 — Scott tags Set B, then the comparison.)*

1. **Formal gate call** (recommendation on record: PASS — every metric improved, residuals are
   model signatures not wording gaps).
2. **Zotero backfill batch** (validation runs surfaced these; one API batch, authorized wording
   pending): `counterpoint` on `Z8TPRNEU` + `VG6CIDQW` · `agentic` on `T8E8SCCG` · `general-code`
   on `UDVHQ5HR` · `TF56EPIP` mode facet (tagged pre-mode-pair; its 6 themes + primary present).
3. **Re-import the Actions menu** (`slr-phase4/slr_human_tags_actions.yml`, now **32 toggles**).
4. **Scott tags Set B blind** (`IURU9UTA`: B644HQFS 6DXZGHD9 E95T8E88 7V7SRG43 UW2R6BBJ BAWCBT9R
   E3E5YA2E 5VTAJISY TF56EPIP R4WJZBSF). **Set B is still 100% model-free — keep it that way until
   the human tags are in.** Use the packet's five-question facet checklist + second-look habit
   (the "dinner fatigue" mitigation, §7).
5. Then: 3 models tag Set B fresh → human-vs-model comparison (**Set B = clean headline; Set A =
   model-informed**, state this in writeups) → breadth policy → **full 148-core sweep** → extend
   `survey-input`/`lit-review` over ~890 contexts → batch-review `demote:` flags.

## 3. Adjudicated rulings (all encoded in the instrument — do not re-litigate)

- **D1 plan-gate:** human gate over an AI plan = `hitl-workflow` when a *designed lifecycle
  checkpoint*; conversational guide-then-"go do it" = steering.
- **D2 who-checks-what:** producer self-checks = no theme · independent evaluation = detector by
  epistemics · severity/cross-model-agreement triage = `risk-routing` (computed,
  producer-independent signal; self-confidence disqualified) · fix-loop governance = `remediation-gating`.
- **D3 Jidoka:** `remediation-gating` = system fixes **without per-fix human**, safe via
  content/process gates; `risk-routing` = the andon cord on top. **Human-approves-every-fix is the
  anti-pattern** (advocacy → `counterpoint`; introduces-bias ≠ studies-bias).
- **D4:** dependency risk *in generated code* → `ai-code-insecurity`; `tooling-supply-chain` keeps
  AI tooling (skills/MCP/agents) + attacks on the reviewer.
- **Altitude rule:** primary = most specific theme still capturing *where the main effort lives*;
  a component mechanism doesn't outrank the broader contribution (UB2EVUFU guard).
- **Re-adjudications:** `2CKL96B8` primary → `ai-code-insecurity` (operationalized biggest-tent
  beat the human's original stretch); `F9JM9CI6` primary → `oversight-explanation` (altitude).
  Both updated in Zotero. `2CKL96B8` + `UDVHQ5HR` carry `demote:context` (with M74M3RFJ: 3/10
  demote rate → expect a demote tail in the sweep).

## 4. Model signatures (carry into the sweep)

- **Gemini:** ignored a *verbatim named worked example* on UB2EVUFU (primary remediation-gating
  despite the guard naming that case) — model non-compliance, not wording; its primaries on
  multi-mechanism systems papers need the human check. Earlier: schema violation (fixed by the
  primary∈themes line), v1 conservative floor. Also: `agy -p` arg limit ≈ >130KB fails silently
  truncated — **chunk large prompts** (see `critique/gemini_ka*.md` pattern).
- **Codex:** liberal breadth (+2–4 themes/paper) persists at v2; salience bias on vivid sections.
- **Fable:** best compliance (10/10 primaries at gate); cites rules verbatim in rationales.
- **Universal v1 lesson (now §16–§17):** 4-model unanimity can encode shared category errors —
  the human vetting pass caught two. Model consensus ≠ correctness, at any n.

## 5. Write-safety & ops (unchanged + today's additions)

- Zotero: RO key for GETs, RW for PATCH with `If-Unmodified-Since-Version`; PATCH returns 204
  empty. Library backup before batch writes. Actions menu can't set primaries — type them.
- **Secret-scan before every commit** (global rule). **Full texts never get committed** —
  `slr-phase4/txt/`, `critique_input.md`, `gemini_ka*.md` are gitignored; one accidental commit
  today was force-pushed out of history within a minute (lesson: check embeds before `git add`).
- CLI taggers: `codex exec --skip-git-repo-check -c model_reasoning_effort=high "<prompt>"`;
  `agy -p "<prompt>" --model "Gemini 3.1 Pro (High)"`. Idempotent `[ -s ]` loops; one tracked
  process; normalize concatenated JSON to first valid object.
- HOS canonical citation (memory `hos-citation`): Thurlow, S. (2026). HumanOversightSystem
  (Version 0.5.0) [Computer software]. Purdue University. https://doi.org/10.5281/zenodo.21347272

## 6. Reference docs

`Methodology/Emerging_Themes.md` = Tag reference (operative vocabulary incl. all rulings) ·
`Methodology/Theme_Tagging_Calibration.md` = design (§5 two-stage + critique panel 1b) + vetting
log (§7) · `slr-phase4/Taxonomy_Changelog.md` §1–§18 = the complete iteration record (dissertation
methods gold) · `slr-phase4/README.md` = phase home/file map ·
`Methodology/HOS_Seeded_Theme_Candidates.md` = staged candidates (oversight-competence gap is
arbiter-validated, tripwire = `non-developer`; authority-allocation spectrum staged). Memory:
`theme-tagging-vocabulary` (current), `hos-citation`, `model-screening-calibration`,
`zotero-library-structure`, `working-style-build-authorization`.

## 7. Standing working rules (don't skip)

- **Ask before running jobs / writing** — brainstorm and confirm; authorization is scoped and
  expires when the design changes. Scott often works from an iPad.
- **Set B stays model-free until the human tags are in.** The clean comparison depends on it.
- **Every boundary that catches a human goes into the compressed instrument** (not just the
  reference) — and instrument copies move in the same commit.
- **Struggle signals** (can't pick a primary / stretching a definition) = check the core bar,
  flag `demote:`, move on. **Second look** on every paper's tags before moving on.
