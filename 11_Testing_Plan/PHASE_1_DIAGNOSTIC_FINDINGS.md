# VIVARTHA Phase 1 Diagnostic Findings

**Scope:** diagnosis only. The official benchmark, baseline, model, dependencies, and application behavior were not changed.

## Files inspected

- `translation-service/service.py`
- `translation-service/requirements.txt`
- `11_Testing_Plan/PHASE_1_TRANSLATION_QUALITY_BENCHMARK.md`
- `11_Testing_Plan/PHASE_1_TRANSLATION_QUALITY_BASELINE.md`
- `backend/src/server.js`
- `11_Testing_Plan/run_phase1_quality_benchmark.py`

## Pipeline traced

```text
Node POST /api/translate
  → Python POST /translate
  → IndicProcessor.preprocess_batch
  → tokenizer
  → IndicTrans2.generate
  → tokenizer.batch_decode
  → IndicProcessor.postprocess_batch
  → Python JSON response
  → Node JSON response
```

## Time diagnosis

The four official failures were traced with direct Python intermediate values and the final Node API response. In each case, the clock string is already damaged by `IndicProcessor.preprocess_batch`; decoded model output and final API output preserve that damaged form.

| Case | Source time | Preprocessed evidence | Decoded/final evidence | Location |
|---|---:|---|---|---|
| Tamil | 10:20 | `... இரவு < ID1 > மணிக்கு ...` | Malayalam contains `<ഐ. ഡി. 1>` | **B — preprocessing** |
| Telugu | 4:15 | `... సాయంత్రం \\1᱕15కి ...` | Malayalam contains `\\1:15` | **B — preprocessing** |
| Kannada | 7:30 | `... ಬೆಳಿಗ್ಗೆ \\1᱕30ಕ್ಕೆ ...` | Malayalam contains `\\1:30` | **B — preprocessing** |
| Hindi | 8:40 | `... सुबह \\1᱕40 बजे ...` | Malayalam contains `\\1:40` | **B — preprocessing** |

The exact escaped display above represents the raw diagnostic text; it is shown escaped to keep terminal encoding unambiguous.

### Additional time-only diagnostics

Additional colon-formatted times were tested across Tamil, Telugu, Kannada, Hindi, and English: `10:20`, `4:15`, `7:30`, `8:40`, `6:45`, `12:00`, `1:05`, and `11:55`.

- English controls preserved the clock string through preprocessing and final output for all tested values.
- Non-English inputs consistently showed corruption before inference:
  - values with minutes `:15`, `:30`, `:40`, `:45`, and `:05` commonly became `\\1:<minutes>`;
  - `10:20`, `12:00`, and `11:55` commonly became an `<ID1>`-like token in preprocessing/output;
  - the behavior occurred across Tamil, Telugu, Kannada, and Hindi.
- This is systematic across non-English Indic preprocessing, not specific to the four benchmark numbers or one sentence.

## Future-perfect diagnosis

The five official future-perfect cases were traced at the same stages.

- Source and preprocessed text retained the future-completion meaning.
- The decoded model output changed the aspect:
  - English output became a simple future completion (`... പൂർത്തിയാക്കും`).
  - Tamil output used a less precise completed-future form.
  - Telugu and Hindi outputs used an uncertain completed form (`... പൂർത്തിയാക്കിയിരിക്കാം`).
  - Kannada output became a simple future completion (`... പൂർത്തിയാക്കും`).
- `postprocess_batch` did not introduce the change; its output matched the decoded semantic choice.
- Node returned the same postprocessed result.

Conclusion: this appears to be a **C — model inference/decoding behavior**, not an input-formatting or API issue. It is consistent with a current-model limitation for this tense/aspect construction.

## Isolated errors

### English negation

The source and preprocessed text retained the intended affirmative “not only ... but also ...” construction. IndicTrans2 generated Malayalam containing a negated “did not solve” meaning. Postprocessing and Node preserved that output.

This is evidence of a model-generation semantic error in this construction, but one case is insufficient to call it systematic.

### English pronoun-role case

The source and preprocessing were unchanged. The model output preserved the key-giving event and identity-card reference, but the role assignment around “they/she/them” was less explicit than the reference. Postprocessing and Node did not change it.

This is an isolated model coreference/role-resolution weakness in the current sample, not evidence of an API or preprocessing defect.

## Confirmed versus suspected

Confirmed:

- Non-English clock corruption occurs in `IndicProcessor.preprocess_batch` before tokenizer/model inference.
- English clock controls preserve times through the whole pipeline.
- Future-perfect weakening occurs in generated model text; postprocessing and API forwarding do not cause it.
- The negation and pronoun issues are already present in decoded model output.
- No transport or benchmark-runner corruption was found; the Node API returned the Python result unchanged.

Suspected:

- The `<ID1>` and `\\1` forms are normalization/tokenization behavior in IndicTransToolkit’s preprocessing rules for colon-separated numeric expressions.
- The future-perfect results reflect a model limitation or decoding preference rather than a service bug.

## Recommended controlled next investigation (not implemented)

1. Build a preprocessing-only regression matrix for non-English times and inspect IndicTransToolkit’s numeric/time normalization behavior.
2. Test a narrow, opt-in time-preservation strategy outside the official benchmark, then compare raw model input/output without changing the baseline.
3. For future perfect, evaluate additional unambiguous examples and decoding settings in a separate experiment; do not change the production configuration yet.
4. Add targeted negation and pronoun examples only to a future diagnostic set, not to the frozen 100-case benchmark.

## Exact diagnostic command

```powershell
cd C:\Users\aaron\OneDrive\Desktop\VIVARTHA\11_Testing_Plan
..\translation-service\.venv\Scripts\python.exe diagnose_phase1.py
```

The diagnostic script was temporary and is not part of the official benchmark. Its captured output was used to create this document and is not mixed into the official baseline.
