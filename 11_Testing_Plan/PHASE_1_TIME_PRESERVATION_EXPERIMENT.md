# VIVARTHA Phase 1 — Time Preservation Experiment

**Status:** Completed controlled experiment; no production fix applied  
**Classification:** Internal diagnostic experiment, not an official benchmark result  
**Date:** 2026-10-03  

## Objective

Determine whether clock times can be protected before `IndicProcessor.preprocess_batch`, translated through the current IndicTrans2 pipeline, and restored exactly afterward without changing the model or production application code.

This experiment does not modify the official benchmark, baseline, model, dependencies, frontend, backend, or Python service.

## Scope and setup

- Model: `ai4bharat/indictrans2-indic-indic-dist-320M`
- Target: Malayalam (`mal_Mlym`)
- Source languages: Tamil, Telugu, Kannada, Hindi, English
- Clock values: `10:20`, `4:15`, `7:30`, `8:40`, `6:45`, `12:00`, `1:05`, `11:55`
- Main matrix: 40 real sentence contexts, 8 per language
- Controls: ratio `4:1`, port `3001`, date, ordinary colon punctuation, multiple numeric values, and a sentence with no time
- Narrow clock regex tested:

```text
(?<!\d)(?:[01]?\d|2[0-3]):[0-5]\d(?!\d)
```

The protected strategy replaced each matched clock value with `CLOCKTOKEN`, ran the normal preprocessing, inference, and postprocessing path, then attempted exact restoration.

## Trace findings

### Current preprocessing

For non-English inputs, ordinary clock text such as `4:15` is transformed by the current IndicTrans2 preprocessing into an internal representation before model generation. This confirms the previously observed time-corruption point is upstream of decoding.

### Protected preprocessing

`CLOCKTOKEN` survived `IndicProcessor.preprocess_batch` in the tested contexts. This proves only that the sentinel reaches the model input; it does not prove that the model will copy it.

### Model output and restoration

IndicTrans2 did not preserve the sentinel as an opaque token. Across the tested languages it variously:

- rendered `CLOCKTOKEN` as Malayalam word-like text (for example, a transliteration/translation of “clock token”);
- split structured markers such as `TIME_4_15` into ordinary pieces;
- dropped or altered angle-bracket markers such as `<extra_id_0>`;
- copied numeric `99999` in some cases, but without providing an exact, semantically safe clock marker.

Consequently, exact post-inference restoration was not possible with these placeholders. The protected output did not retain the required placeholder identity, so replacing it after inference would either fail or risk changing unrelated model output.

## Results

| Measure | Result |
|---|---:|
| Real sentence contexts | 40 |
| Languages with tested contexts | 5 |
| Contexts whose protected output retained an exact restorable `CLOCKTOKEN` | 0/40 |
| Languages where the strategy was reliable | 0/5 |
| Controls falsely matched by the clock regex | 0 observed |

The surrounding sentence meaning was often broadly understandable, but the clock value was missing or replaced by placeholder-derived wording. That is not acceptable for exact time preservation.

## Control results

The tested regex did not match the following non-clock controls:

- ratio `4:1`;
- port `3001`;
- date text;
- ordinary colon punctuation;
- sentences containing multiple numeric values without a clock pattern;
- sentences containing no time.

The protected and unprotected preprocessing inputs were equivalent for these controls. No regex false positive was observed in this control set. This is evidence about the tested examples only, not a formal proof that the regex is universally safe.

## Comparison: current vs experimental

The current path preserves the original clock text into preprocessing only in cases where the processor does not reinterpret it; for the problematic non-English clock contexts, the processor changes the representation before generation. The experimental path successfully changed the input to a sentinel, but the model treated that sentinel as translatable text rather than a protected span. Therefore the experiment did not improve exact time preservation and introduced placeholder-related output risk.

## Answers to the required questions

1. **Can times be safely protected with the tested approach?** No.
2. **Are times preserved exactly?** No; `0/40` protected contexts retained an exact restorable sentinel.
3. **Does it work across Tamil, Telugu, Kannada, Hindi, and English?** No. No language produced a reliable result.
4. **What happens for English?** English was included in the same matrix; the placeholder was still not reliably copied as an opaque marker.
5. **Were false positives found?** None in the defined controls. Broader testing would still be required before production use.
6. **Is surrounding translation quality preserved?** Often broadly understandable, but the time was omitted or converted into placeholder-derived wording; therefore the result is not acceptable for time-sensitive text.
7. **Is this safe for production?** No. The tested strategy must not be deployed.
8. **Smallest possible future production change if a later strategy succeeds:** isolate only validated clock spans, use a model-compatible sentinel proven to survive inference, restore the exact original span, and add regression tests for all five languages plus the controls. This experiment did not identify such a sentinel, so that change is not implemented here.

## Reproducibility

The experiment utility and raw trace are retained as clearly labelled diagnostic artifacts:

- `11_Testing_Plan/time_preservation_experiment.py`
- `11_Testing_Plan/PHASE_1_TIME_EXPERIMENT_RAW.json`

Command executed:

```powershell
python 11_Testing_Plan/time_preservation_experiment.py
```

The utility loads the existing translation-service virtual environment, model, tokenizer, and IndicTrans2 processor directly. It does not call or modify the production service and does not modify the official 100-case benchmark or baseline.

## Conclusion

**Experiment result: FAIL for the tested placeholder-restoration strategy.**

The experiment identified a real preprocessing-sensitive time problem, but it did not produce a safe fix. The model does not reliably preserve arbitrary placeholders through generation. No production code, model, dependency, benchmark sentence, or reference translation was changed.
