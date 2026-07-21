# Set C Pilot — Review Packet: ZUM76CCG
**"Generative AI in systems engineering: a framework for risk assessment of LLMs" (LRF)**
Triage disposition: **LIGHT-REVIEW** → consensus primary `risk-routing` (2/1) · tripwires: `demote:context` ×3 (unanimous)
Pilot protocol: full human review regardless of disposition. TXT: `slr-phase4/txt/ZUM76CCG.txt`

## Three-way panel

| | opus | codex | gemini |
|---|---|---|---|
| **primary** | risk-routing | risk-routing | org-governance |
| **themes** | risk-routing, org-governance | risk-routing, hitl-workflow, org-governance | org-governance |
| **facets** | general-ai, intro-framing, risk-overreliance, assistive, agentic | design-only, general-ai, assistive, agentic, metrics, risk-quality, risk-overreliance | intro-framing, assistive, agentic |
| **flags** | demote:context | demote:context | demote:context |

Facet voting: **3/3** assistive, agentic · **2/3** general-ai (o+c), intro-framing (o+g), risk-overreliance (o+c) · **1/3** design-only, metrics, risk-quality (codex only).

## Adjudication questions for the arbiter

1. **Primary — routing or governance?** The LRF's autonomy×impact classes *prescribe required
   human-oversight levels per use case* — opus/codex read that as the allocation decision
   (Hedwig-kin, at org altitude); gemini reads the whole as org apparatus (6DXZGHD9-kin). Note the
   signal-vs-selection boundary: unlike E95T8E88, the LRF *does* specify selection logic
   (class → oversight tier), but at use-case rather than artifact granularity. Is use-case-level
   allocation still `risk-routing`, or is org-level classification `org-governance`'s territory?
   (Whatever you rule becomes the altitude precedent for classification frameworks in the sweep.)
2. **The contradiction pair — `intro-framing` (opus, gemini) vs `design-only`+`metrics` (codex).**
   Conflicting reads of the same text: opus says "no operationalized metrics, deferred to future
   work"; codex says the matrix + mitigations are specified with metrics. Buildable-detail test:
   components/thresholds present, or concept-level classification only? Your read decides which of
   the mutually-exclusive facets survives.
3. **Demote — unanimous, and probably right.** General-AI object (systems engineering broadly,
   coding not specific) + unevaluated. §30 look-at-keeping check: this is a *risk-classification*
   dive, not a regulatory-operationalization dive, and UW2R6BBJ already holds that exemplar slot —
   so the exception likely doesn't trigger. Confirm or invoke.
4. **Mode pair — both (3/3).** The autonomy levels 0–3 span assistive→agentic by design; "both"
   looks correct. Confirm.
5. Minor: `risk-overreliance` (2/3, focal over-reliance paragraph per opus) — keep/drop.

## Pilot-run observations (pipeline mechanics)
- L0 caught a silent codex empty-output twice; root cause = codex reading stdin in background
  context; fixed in the runner (`< /dev/null`). Retry protocol worked.
- Wall-clock per paper ≈ 5–10 min model time (parallel); triage instantaneous.
