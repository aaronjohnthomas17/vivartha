# VIVARTHA Phase 1 — Time Preservation / Alignment Feasibility

**Status:** Diagnostic investigation complete  
**Date:** 2026-10-03  
**Model:** `ai4bharat/indictrans2-indic-indic-dist-320M`  
**Target:** Malayalam (`mal_Mlym`)  

## 1. Objective

This investigation tested whether clock times can be detected before IndicTrans2 preprocessing, removed externally, and then restored exactly after translation using source-span tracking or alignment. No production fix was implemented.

The official 100-case benchmark and baseline remain frozen.

## 2. Confirmed facts

- The current IndicTrans2 pipeline can reinterpret clock expressions during preprocessing for several non-English inputs.
- A previous synthetic-placeholder approach failed because the model did not copy placeholders as opaque markers.
- A robust candidate clock pattern was tested:

```text
(?<!\d)(?:[01]?\d|2[0-3]):[0-5]\d(?!\d)
```

- The pattern detects valid 24-hour `HH:MM` forms including `1:05`, `4:15`, `6:45`, `7:30`, `8:40`, `10:20`, `11:55`, and `12:00`.
- It does not detect `4:1`, `3:2`, or `2026:10` in the tested controls.
- It does detect `4:15` in “The value is 4:15 units.” This is a deliberate limitation: syntax alone cannot prove whether a valid `HH:MM` string is a clock time.

## 3. Previous placeholder experiment

`CLOCKTOKEN`, `TIME_4_15`, `X4X15`, `<extra_id_0>`, and `99999` were previously tested. They were split, translated, altered, dropped, or treated as ordinary text. No placeholder was reliable enough for production restoration.

## 4. Source-span detection and position tracking

The diagnostic detector records:

- exact original time string;
- zero-based character start and end offsets;
- a short surrounding context window;
- source language supplied by the test case.

For example, the detector records `4:15` and its original offsets before any IndicProcessor call. This part is technically straightforward and worked for all 20 matrix cases and all 9 trace cases.

Character offsets are valid only in the original source string. They cannot be copied directly into the Malayalam output because translation changes word order, token count, morphology, and sentence length.

## 5. Controlled experiment

The diagnostic script tested:

- 20 translation cases: 4 each for Tamil, Telugu, Kannada, Hindi, and English;
- 9 detailed trace cases covering the requested representative values;
- times at beginning/middle/end-like positions and multiple sentence structures;
- removal of the clock string entirely;
- a structural `[TIME_REMOVED]` gap for the detailed trace cases;
- six false-positive/control strings.

The detailed trace recorded original input, preprocessed text, model input, raw model output, postprocessed output, and final output.

## 6. Time-removal results

Removing the time before translation produced understandable translations of the surrounding event or action in many cases. It also removed the time information completely, as expected. The model did not provide a reliable marker indicating where the removed span belonged.

The structural gap was not treated as a protected alignment object; it is ordinary model input and therefore cannot be trusted as an output anchor. This is intentionally different from claiming that a placeholder solution works.

### Results by language

| Language | Removal cases | Source-span detection | Output anchor demonstrated |
|---|---:|---|---|
| Tamil | 4 | 4/4 detected | No |
| Telugu | 4 | 4/4 detected | No |
| Kannada | 4 | 4/4 detected | No |
| Hindi | 4 | 4/4 detected | No |
| English | 4 | 4/4 detected | No |
| **Total** | **20** | **20/20** | **0/20** |

The existing pipeline successfully generated Malayalam for the time-removed sentences, but translation quality is not the same as reinsertion feasibility. Exact original strings such as `4:15` were not restored by this experiment.

## 7. Alignment approaches investigated

| Approach | Current-stack feasibility | Finding |
|---|---|---|
| Source character positions | High for detection | Works before preprocessing; does not identify a target position. |
| Source word positions | Moderate | Can be recorded, but word reordering and morphology make direct target mapping unsafe. |
| Token positions | Moderate for diagnostics | Token indices are model/tokenizer-specific and do not establish semantic alignment. |
| Source/target token alignment | Possible in principle | Not exposed as a reliable alignment result by the current generation path; requires additional algorithmic validation. |
| Attention information | Technically possible to inspect | Not demonstrated as a stable word alignment signal; attention is not an exact restoration contract. |
| Translate after removing time | Works as a translation operation | Produces context without the time but no reliable insertion point. |
| Structural/context-based placement | Possible as a heuristic | Needs language-specific grammatical rules and can fail with reordering, omitted adjuncts, or multiple time-like phrases. |

None of these approaches was demonstrated reliable enough to claim safe production behavior across Tamil, Telugu, Kannada, Hindi, and English.

## 8. False-positive findings

The regex correctly rejected the tested non-clock forms:

- `4:1`;
- `4:1 ratio`;
- `3:2`;
- `2026:10`;
- ordinary punctuation such as `Note: bring your card.`

However, it matched `4:15` in “The value is 4:15 units.” This shows that valid clock syntax and semantic clock usage cannot be distinguished perfectly with the regex alone. A production detector would need context rules, user/document conventions, or an explicit ambiguity policy.

## 9. Experimental observations

- Source detection and source-span recording are feasible.
- Removing the time prevents the preprocessing corruption for that span, but also discards the time from the translation input.
- The translated sentence does not expose a tested, deterministic anchor from which the original time can be restored.
- Malayalam word order and time-expression placement vary by source construction, so fixed character offsets or fixed word offsets are unsafe.
- English is not automatically solved by external restoration; it still needs the same validation because sentence structure and output placement may vary.

## 10. Assumptions and possible future approaches

These are possibilities, not validated solutions:

- a separately validated source-target alignment algorithm;
- constrained decoding or model-supported span copying;
- language-aware placement rules for narrowly defined sentence patterns;
- a two-pass system with explicit metadata and regression tests.

Each would require new experiments, especially for multiple time expressions, reordered clauses, omitted adjuncts, punctuation, and ambiguous `HH:MM` strings. None was implemented here.

## 11. Risks and limitations

- Exact clock preservation is stricter than semantic similarity: `4:15` must remain exactly `4:15`.
- A wrong reinsertion location can change the meaning even when the Malayalam sentence remains grammatical.
- Removing every valid `HH:MM` pattern could corrupt ratios, labels, version-like values, or domain-specific numeric expressions.
- Character offsets do not survive translation.
- Heuristic placement may work on simple examples and fail on reordered or multi-clause sentences.
- The 20-case experiment is diagnostic evidence, not a formal accuracy metric.

## 12. Production-safety verdict

External source-span detection is technically feasible. Safe exact restoration is **not demonstrated** with the current stack and current approach. Production code must not be changed based on this experiment.

### Final conclusion

**B. FEASIBLE BUT REQUIRES MORE TESTING**

The conclusion is B rather than D because source-span detection, metadata recording, and time removal can be implemented with the existing runtime. It is not A because no reliable target alignment or reinsertion method was demonstrated. More testing is required before any production implementation could be considered safe.

## 13. Reproducibility

Created diagnostic files:

- `11_Testing_Plan/time_alignment_feasibility_experiment.py`
- `11_Testing_Plan/PHASE_1_TIME_ALIGNMENT_FEASIBILITY_RAW.json`
- this report

Command executed:

```powershell
& .\translation-service\.venv\Scripts\python.exe .\11_Testing_Plan\time_alignment_feasibility_experiment.py
```

The experiment was run in local-cache-only mode after the first attempt encountered a network permission error while Transformers tried to contact Hugging Face. No package was installed or upgraded.

## 14. Recommendation

The next development step should be a separate alignment-only study, not a production change. It should compare an explicitly implemented source-target alignment method against a larger adversarial set containing multiple times, reordered clauses, ratios, dates, and domain-specific numeric expressions. Production implementation should wait until exact-string recovery and false-positive handling are demonstrated across all five source languages.
