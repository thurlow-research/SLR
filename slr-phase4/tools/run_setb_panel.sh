#!/bin/bash
# v2.13 panel run: codex + gemini over Sets A+B (20 papers). Fable EXCLUDED —
# runs only with Scott's explicit per-run permission (tie-breaks).
# Idempotent: skips non-empty outputs. codex & gemini loops run concurrently.
S="${PANEL_S:?set PANEL_S to the scratchpad panel dir}"
R="$(cd "$(dirname "$0")/.." && pwd)"
KEYS=$(python3 -c "import json; d=json.load(open('$R/data/calib_sets.json')); print(' '.join(d['setA']+d['setB']))")

extract_json () { python3 -c "
import sys,re,json
s=sys.stdin.read()
cands=re.findall(r'\{.*\}', s, re.DOTALL)
for c in sorted(cands,key=len,reverse=True):
    try: json.loads(c); print(c); break
    except: continue
"; }

codex_loop () {
  for k in $KEYS; do
    o="$R/data/tags-v213/codex/$k.json"
    [ -s "$o" ] && continue
    timeout 900 codex exec --skip-git-repo-check -c model_reasoning_effort="high" "$(cat "$S/prompts/$k.txt")" < /dev/null > "$S/codex_$k.raw" 2>"$S/codex_$k.err"
    extract_json < "$S/codex_$k.raw" > "$o"
    echo "codex $k -> $(wc -c < "$o") bytes"
  done
}
gemini_loop () {
  for k in $KEYS; do
    o="$R/data/tags-v213/gemini/$k.json"
    [ -s "$o" ] && continue
    timeout 900 agy --add-dir "$S/prompts" -p "Read the file $S/prompts/$k.txt and follow its instructions exactly. Output ONLY the single JSON object it requires — no commentary." --model "Gemini 3.1 Pro (High)" < /dev/null > "$S/gemini_$k.raw" 2>"$S/gemini_$k.err"
    extract_json < "$S/gemini_$k.raw" > "$o"
    echo "gemini $k -> $(wc -c < "$o") bytes"
  done
}
codex_loop & CP=$!
gemini_loop & GP=$!
wait $CP $GP
echo "PANEL_V213_DONE"
