#!/usr/bin/env python3
"""Jidoka triage for the v2.13+ tagging pipeline.

Ladder (calibration-validated 2026-07-21, n=20):
  L0  schema check per model output (bare slugs, primary in themes, legal flags)
  L1  primary consensus: 3/3 unanimous -> ACCEPT (10% seeded random audit sample)
      2/1 majority -> LIGHT-REVIEW (accept majority, human confirms dissent)
      3-way split  -> HUMAN (andon cord)
  L2  computed struggle tripwires (never model self-confidence):
      - sprawl: any model asserts > SPRAWL_MAX themes (TF56EPIP class)
      - any model demote flag (flag proposes, human disposes)
  Facet layer, per-tag voting: 3/3 accept | 2/3 accept-noted | 1/3 drop-logged.
  Replication stage (2026-07-22): any primary disagreement triggers 2 extra runs
  per model (files KEY.r2.json, KEY.r3.json). With replicates present, each
  model's vote = its MODAL primary (ties -> run 1); tags = asserted in >=2 of 3
  runs. Re-triage on modals; modal 3/3 = ACCEPT annotated noise-resolved.
  Within-model instability (any run-level self-disagreement) = a tripwire that
  biases disposition one rung toward review. Papers with disagreement and NO
  replicates yet -> disposition RERUN-NEEDED (the worklist).

Pilot mode (--pilot): dispositions computed as usual, but EVERY paper is
emitted for full human review (Set C protocol: Scott reviews all; sampling
starts only in the production sweep).
"""
import argparse, json, pathlib, random, sys

MODELS = ["opus", "codex", "gemini"]
SPRAWL_MAX = 6
LEGAL_FLAGS = {"demote:context", "demote:discard", "insufficient-input"}


def load_one(p, model, key):
    if not p.exists() or p.stat().st_size == 0:
        return None, f"{model}/{key}: missing/empty"
    try:
        d = json.loads(p.read_text())
    except Exception as e:
        return None, f"{model}/{key}: unparseable ({e})"
    for field in ("key", "primary_theme", "themes", "facets"):
        if field not in d:
            return None, f"{model}/{key}: missing field {field}"
    if d["primary_theme"] not in d["themes"]:
        return None, f"{model}/{key}: primary not in themes"
    bad = set(d.get("flags", [])) - LEGAL_FLAGS
    if bad:
        return None, f"{model}/{key}: illegal flags {bad}"
    return d, None


def load(base, model, key):
    """Run-aware: aggregate KEY.json (+ KEY.r2.json, KEY.r3.json if present) to modal votes."""
    runs, first_err = [], None
    for name in (f"{key}.json", f"{key}.r2.json", f"{key}.r3.json"):
        p = base / model / name
        if not p.exists():
            continue
        d, err = load_one(p, model, key)
        if err and name == f"{key}.json":
            first_err = err
        if d:
            runs.append(d)
    if not runs:
        return None, first_err or f"{model}/{key}: no valid runs"
    if len(runs) == 1:
        runs[0]["_runs"], runs[0]["_unstable"] = 1, False
        return runs[0], None
    prims = [r["primary_theme"] for r in runs]
    modal = max(set(prims), key=lambda x: (prims.count(x), -prims.index(x)))
    need = (len(runs) // 2) + 1
    def vote(field):
        c = {}
        for r in runs:
            for tag in set(r[field]):
                c[tag] = c.get(tag, 0) + 1
        return sorted(t for t, n in c.items() if n >= need)
    themes = vote("themes")
    if modal not in themes:
        themes = sorted(set(themes) | {modal})
    agg = {"key": key, "primary_theme": modal, "themes": themes,
           "facets": vote("facets"),
           "flags": [f for f in {f for r in runs for f in r.get("flags", [])}
                     if sum(f in r.get("flags", []) for r in runs) >= need],
           "_runs": len(runs), "_unstable": len(set(prims)) > 1}
    return agg, None


def triage(keys, base, seed, audit_rate, pilot):
    rng = random.Random(seed)
    papers, l0_failures = {}, []
    for k in keys:
        outs = {}
        for m in MODELS:
            d, err = load(base, m, k)
            if err:
                l0_failures.append(err)
            if d:
                outs[m] = d
        papers[k] = outs

    results = []
    for k, outs in papers.items():
        if len(outs) < len(MODELS):
            results.append({"key": k, "disposition": "L0-INCOMPLETE"})
            continue
        primaries = {m: outs[m]["primary_theme"] for m in MODELS}
        votes = {}
        for p in primaries.values():
            votes[p] = votes.get(p, 0) + 1
        top, topn = max(votes.items(), key=lambda x: x[1])
        n_runs = {m: outs[m].get("_runs", 1) for m in MODELS}
        replicated = all(v >= 3 for v in n_runs.values())
        note = None
        if topn == 3:
            dispo, consensus = "ACCEPT", top
            if replicated:
                note = "noise-resolved"
        elif not replicated:
            dispo, consensus = "RERUN-NEEDED", top if topn == 2 else None
        elif topn == 2:
            dispo, consensus = "LIGHT-REVIEW", top
        else:
            dispo, consensus = "HUMAN", None
        tripwires = []
        for m in MODELS:
            if outs[m].get("_unstable"):
                tripwires.append(f"unstable:{m}")
        for m in MODELS:
            if len(outs[m]["themes"]) > SPRAWL_MAX:
                tripwires.append(f"sprawl:{m}={len(outs[m]['themes'])}")
            for f in outs[m].get("flags", []):
                if f.startswith("demote:"):
                    tripwires.append(f"{f}:{m}")
        if tripwires and dispo == "ACCEPT":
            dispo = "LIGHT-REVIEW"
        # facet voting
        counts = {}
        for m in MODELS:
            for t in set(outs[m]["facets"]):
                counts[t] = counts.get(t, 0) + 1
        facets = {"accept": sorted(t for t, c in counts.items() if c == 3),
                  "noted": sorted(t for t, c in counts.items() if c == 2),
                  "dropped": sorted(t for t, c in counts.items() if c == 1)}
        results.append({"key": k, "disposition": dispo, "consensus_primary": consensus,
                        "note": note, "runs": n_runs,
                        "primaries": primaries, "tripwires": tripwires, "facets": facets,
                        "themes": {m: sorted(outs[m]["themes"]) for m in MODELS}})

    accepted = [r for r in results if r["disposition"] == "ACCEPT"]
    n_audit = max(1, round(len(accepted) * audit_rate)) if accepted else 0
    audit = sorted(r["key"] for r in rng.sample(accepted, n_audit)) if accepted else []
    for r in results:
        r["audit_sample"] = r["key"] in audit
        if pilot:
            r["pilot_full_review"] = True
    return results, l0_failures, audit


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--set", dest="setname", help="key of calib_sets.json list (e.g. setC)")
    ap.add_argument("--keys", nargs="*", help="explicit keys")
    ap.add_argument("--base", default="data/tags-v213")
    ap.add_argument("--seed", type=int, default=714)
    ap.add_argument("--audit-rate", type=float, default=0.10)
    ap.add_argument("--pilot", action="store_true")
    ap.add_argument("--out", help="write JSON results here")
    a = ap.parse_args()
    root = pathlib.Path(__file__).resolve().parent.parent
    keys = a.keys or json.load(open(root / "data/calib_sets.json"))[a.setname]
    results, l0, audit = triage(keys, root / a.base, a.seed, a.audit_rate, a.pilot)
    for e in l0:
        print("L0:", e, file=sys.stderr)
    counts = {}
    for r in results:
        counts[r["disposition"]] = counts.get(r["disposition"], 0) + 1
    print("dispositions:", counts)
    print("audit sample:", audit)
    for r in results:
        line = f"{r['key']}: {r['disposition']}"
        if r.get("consensus_primary"):
            line += f" -> {r['consensus_primary']}"
        if r.get("tripwires"):
            line += f" | tripwires: {','.join(r['tripwires'])}"
        print(line)
    if a.out:
        pathlib.Path(a.out).write_text(json.dumps(results, indent=1))
        print("wrote", a.out)


if __name__ == "__main__":
    main()
