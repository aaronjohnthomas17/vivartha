# Technical Research

## IndicTrans2 — recommended candidate, not yet final
AI4Bharat's official repository lists Malayalam (`mal_Mlym`), Tamil, Telugu, Kannada, Hindi, and English among supported languages and publishes model, data, evaluation, and inference resources. It is directly relevant to the product's Indian-language focus. Risks include model size/compute, inference latency, licensing/compliance review, domain variation, and the need for VIVARTHA-specific evaluation. No accuracy percentage is adopted here. Alternatives to benchmark include commercial translation APIs, NLLB, and other Indic models. Decision: recommended for Phase 1 feasibility prototype; deployment selection remains provisional.

## Speech-to-text
OpenAI Whisper is an official open-source multilingual ASR reference with multiple model sizes. It is a possible Phase 2 baseline because it can transcribe spoken language, but Malayalam quality, latency, hardware, audio privacy, and model license must be tested. Alternatives include faster-whisper/CTranslate2, cloud speech APIs, and other Indic ASR models. Decision: possible candidate, not selected.

## OCR
Tesseract 5 is an open-source OCR engine under Apache 2.0 with language trained-data packages. It is a possible offline/server baseline for printed Malayalam and other scripts. Risks include scan quality, layout, mixed scripts, tables, handwriting, and correction burden. Alternatives include cloud OCR and specialized document AI services. Decision: possible candidate for Phase 3 prototype.

## PDF/DOCX/TXT
PyMuPDF documents direct PDF text extraction; it is suitable for text-based PDFs but cannot make scanned pages readable without OCR and may lose complex layout. `python-docx` is a common DOCX paragraph/table extraction option but does not preserve every Word feature. TXT processing is straightforward but requires encoding, size, and line-ending validation. Alternatives include Apache Tika and commercial document extraction. Decision: research candidates only.

## Language detection
Possible options are fastText language identification, CLD3, compact language-detector libraries, or provider detection. Short Malayalam/Indic text and code-switching can be difficult; explicit source selection should remain available. Decision: detection is later-phase and must not override user choice silently.

## Service architecture
A Node/Express API can own HTTP, validation, auth boundaries, and orchestration while a Python service owns model-specific inference. A single deployable may be simpler for early learning; a separate service is more replaceable but adds operational complexity. Recommended architecture is logical separation first, physical separation when model/runtime needs justify it.

## Frontend/backend/database candidates
React is a viable component UI; alternatives include Vue or Svelte. Node.js/Express is a viable API layer; alternatives include FastAPI or Django. MongoDB fits flexible metadata and document-shaped history; PostgreSQL offers stronger relational constraints and mature querying. This is a provisional comparison, not a popularity decision.

## Authentication/security
Phase 1 can defer accounts if anonymous use is approved. Later options include managed OIDC/OAuth, session cookies, or short-lived tokens. Regardless of provider, use TLS, secret management, rate limiting, authorization, safe upload handling, audit logs, and privacy-aware retention.

## Sources consulted
- AI4Bharat, IndicTrans2 repository: https://github.com/AI4Bharat/IndicTrans2
- IndicTrans2 paper: https://arxiv.org/abs/2305.16307
- OpenAI Whisper model card: https://github.com/openai/whisper/blob/main/model-card.md
- Tesseract documentation: https://tesseract-ocr.github.io/tessdoc/
- PyMuPDF basics: https://pymupdf.readthedocs.io/en/latest/the-basics.html

Research date: 2026-09-27. Versions, costs, licenses, and service availability must be rechecked before implementation.
