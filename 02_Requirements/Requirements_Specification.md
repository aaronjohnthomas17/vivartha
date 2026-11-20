# Requirements Specification

## Status
Phase 0 working specification; Phase 1 requirements are the implementation gate.

## MVP functional requirements (Phase 1)
FR-1 The user can enter text and select a supported source language.
FR-2 Malayalam is the default/primary target language; target-language extensibility is designed but not required in the MVP.
FR-3 The system validates non-empty input and supported language codes.
FR-4 The system submits a translation request and displays Malayalam output with processing state.
FR-5 The user can copy output and clear input/output.
FR-6 The system records basic translation history only after a successful, policy-compliant request, subject to the final privacy decision.
FR-7 Errors are shown in understandable language without exposing internal details.

## Later-phase functional requirements
Voice: accept recording/upload, speech-to-text, show transcript, permit edit/verification, then translate verified text.
Files/images: accept supported PDF/DOCX/TXT/image inputs, extract/OCR text, show editable extracted text, then translate verified text.
Community: accounts, personal library, permitted publishing, search/read/bookmark. Publishing must capture permission status and support moderation/removal.
Intelligent translation: detection, alternatives, context/style, glossary, and feedback only after research validates each feature.

## Non-functional requirements
- Usability: clear Malayalam-oriented workflow, keyboard-accessible controls, responsive layout, and understandable states.
- Reliability: bounded retries, idempotency strategy, durable error records, and no silent loss of user text.
- Performance: establish baselines during Phase 1 prototype evaluation; do not promise latency before measuring model and deployment choices.
- Security/privacy: validate inputs, protect credentials, minimize retained content, encrypt transport, authorize private records, and define deletion/export behavior.
- Maintainability: typed contracts where practical, modular adapters, documented decisions, automated tests, and observable failures.
- Scalability: stateless API where possible, asynchronous job boundary for heavyweight model/file work, and replaceable persistence/storage adapters.

## Constraints, assumptions, dependencies
Constraints include Malayalam focus, phased delivery, beginner-readable design, legal limits on shared content, and no Phase 1 implementation during Phase 0. Assumptions include access to model artifacts/compute and a decision on retention policy. Dependencies include IndicTrans2 availability/licensing, model hardware, language evaluation data, and deployment/storage choices.

## Open questions
1. Should Phase 1 require accounts, or allow anonymous translation with optional history?
2. Should history retain source/output text, metadata only, or be opt-in?
3. What hosting budget and hardware are available for IndicTrans2?
4. Which license/privacy jurisdiction and deletion policy govern user content?
5. Is target-language selection needed in MVP, or is Malayalam-only output sufficient?
