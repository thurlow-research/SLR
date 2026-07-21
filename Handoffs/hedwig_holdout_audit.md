# Audit — Hedwig hold-out integrity of `Tag_Prompt_ASSIGNMENT_hedwig-free.md`
**2026-07-21 · scope: this variant is validated as a held-out instrument for T72TU8B5 (Hedwig) ONLY.**
Live instrument (`slr-phase4/Tag_Prompt.md`) untouched. Deltas vs live prompt: exactly 2 lines.

## 1. What was changed and why

| Line | Live prompt | Assignment variant | Why |
|---|---|---|---|
| ~50 (framework facet) | "…qualifies (VibeGuard, Hedwig)." | "…qualifies (e.g., a pre-publish security gate that drops into CI, or a single-concern multi-agent review pipeline)." | Removes Hedwig's name. First replacement draft used "(VibeGuard, CodeAgent)"; **rejected** because CodeAgent (`7V7SRG43`) is itself a Set B calibration paper with gold — swapping one calibration name for another is not a fix. Final wording is name-free. |
| ~78 (primary tie-breaker) | "(Hedwig: novelty = the dynamic-autonomy classifier → `risk-routing`, not the check-in surface.)" | "(e.g., a checkpoint-placement system: novelty = where and how approval checkpoints are inserted into the agent workflow → `hitl-workflow`, not the generic riskiness signal that triggers them.)" | Removes Hedwig's named answer AND reverses the example's polarity (see §3). |

Verified: the final variant contains zero occurrences of "Hedwig" or "T72TU8B5".

## 2. Analogy-distance finding (interim draft vs Hedwig's actual mechanism)

Hedwig's distinctive features, from `slr-phase4/txt/T72TU8B5.txt`: a **learned** policy engine
(online SGD, developer-persona adaptation, corrections stored as guidance) that **dynamically
calibrates an agent's autonomy level per interaction**, with **check-in frequency/granularity** as
the oversight surface; `change_pattern_risk` is one hand-engineered feature among learned ones.

The interim diff-risk example shared **none** of these: it described a *static* computed score, at
*diff* granularity, driving a *binary gate into a review queue* — no learning, no adaptation, no
autonomy levels, no check-in surface. The only shared structure was the generic
compute-a-signal-then-select shape — which the `risk-routing` **definition itself necessarily
teaches** ("the smarts of surfacing (signal + selection/tiering logic)… signal must be computed &
producer-independent"). A model seeing the interim example could infer the general rule
("novelty-on-the-routing-side → risk-routing"), not Hedwig's verdict specifically: applying it to
Hedwig still requires the model to judge that Hedwig's novelty lies on the routing side — which is
precisely the judgment under test. Residue assessed as: **rule-level only, but same polarity as
Hedwig's gold** — hence the final step below.

## 3. Final line-78 choice: the reverse-polarity (hitl-leaning) example

Both candidates teach the identical rule (novelty over scaffolding, at the route↔control-surface
adjacency):

- **Interim (routing-leaning):** "a diff-risk gating system: novelty = the computed risk score
  deciding what reaches review → `risk-routing`, not the standard review queue it feeds."
- **FINAL (hitl-leaning):** "a checkpoint-placement system: novelty = where and how approval
  checkpoints are inserted into the agent workflow → `hitl-workflow`, not the generic riskiness
  signal that triggers them." (Anchored by a real corpus class — checkpoint-placement papers —
  named nowhere.)

The final example resolves toward the **opposite pole from Hedwig's gold answer**, so any bias it
introduces at the adjacency runs *against* risk-routing: if models still choose `risk-routing` on
Hedwig under this variant, the result is strengthened, not assisted. **Pedagogy lost:** line 78 no
longer illustrates the routing-side resolution — mitigated by §4 (the routing direction remains
taught in three other places).

## 4. Census of other routing-resolving examples in the variant

Three worked micro-examples resolving to `risk-routing` remain (they are rule text shared with the
live instrument, describing no Hedwig-like mechanism):
1. Line ~26 (`remediation-gating`): "deciding when a human must engage on the fix path (risky
   fixes → human) = `risk-routing` layered on top."
2. Line ~32 (worked decomposition): "deciding which findings matter, e.g. by severity +
   cross-model agreement (a computed, producer-independent signal) → `risk-routing`."
3. Line ~32 (same block): "deciding when a fix must engage a human (risk tiers on the fix path) →
   `risk-routing`."

So the tie-breaker illustration was one of four routing-direction teachings; its replacement
removes the only one that sat at Hedwig's exact adjacency, while the class remains represented —
the marginal-leak argument holds in both directions.

## 5. Known residual limitations (disclose)

- **Scope:** the variant is held-out-clean for **Hedwig only**. Other calibration papers remain
  named or recognizably described (VibeGuard-shaped and CodeAgent-shaped descriptors at line ~50;
  "CodeAgent ruling", "2CKL96B8", "R4WJZBSF", "22JBEZNK", "F9JM9CI6", "UB2EVUFU", "VibeGuard"
  elsewhere — unchanged from the live prompt to keep the delta minimal and attributable). Do not
  reuse this variant as a held-out instrument for those papers without further de-referencing.
- The `risk-routing` definition necessarily teaches the computed-signal→selection shape; no
  variant can remove that without changing what is being tested.

**Quotable sentence for the assignment:** "The held-out prompt removes every reference that names
or describes Hedwig; the only residual overlap between its worked examples and Hedwig is the
generic computed-signal-then-select shape that the risk-routing definition itself necessarily
teaches, and the tie-breaker illustration was deliberately re-polarized toward `hitl-workflow`, so
any residual bias at the decisive adjacency runs against, not toward, Hedwig's gold answer."

## 6. Authoritative v2.13 gold for T72TU8B5 (score against THIS — 3-facet copies are stale)

```json
{"primary": "risk-routing",
 "themes": ["hitl-workflow", "oversight-explanation", "risk-routing"],
 "facets": ["agentic", "built-system", "framework", "method-self-report", "metrics", "survey-input"],
 "demote": false}
```
Source: `slr-phase4/data/tags-v213/human_gold.json` (fetched from Zotero adjudicated tags,
2026-07-21). Note for facet scoring: `metrics` and `method-self-report` postdate the v2.1-era
scheme; a "3-facet" working copy (built-system/framework/survey-input) predates the v2.3–v2.8
facet expansions and will produce false errors.
