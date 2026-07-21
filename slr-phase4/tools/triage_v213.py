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

Pilot mode (--pilot): dispositions computed as usual, but EVERY paper is
emitted for full human review (Set C protocol: Scott reviews all; sampling
starts only in the production sweep).
"""
import argparse, json, pathlib, random, sys

MODELS = ["opus", "codex", "gemini"]
SPRAWL_MAX = 6
LEGAL_FLAGS = {"demote:context", "demote:discard", "insufficient-input"}


def load(base, model, key):
    p = base / model / f"{key}.json"
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
        if topn == 3:
            dispo, consensus = "ACCEPT", top
        elif topn == 2:
            dispo, consensus = "LIGHT-REVIEW", top
        else:
            dispo, consensus = "HUMAN", None
        tripwires = []
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
