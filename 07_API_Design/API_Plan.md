# API Plan (Not Implemented)

## Conventions
Version under `/api/v1`; JSON UTF-8; request IDs; consistent error envelope `{code, message, details?, requestId}`; validate length, language codes, and content type; never return provider stack traces. Authentication is TBD for Phase 1.

## Phase 1 text endpoints
`POST /api/v1/translations` — submit `{sourceLanguage, targetLanguage: "ml", text}`; return `{id,status,sourceLanguage,targetLanguage,output,providerMetadata?}`. Validate non-empty text, maximum size, supported languages, and target Malayalam. `GET /api/v1/translations/:id` — retrieve status/result subject to ownership/privacy. `GET /api/v1/translations` — later history listing with pagination. `DELETE /api/v1/translations/:id` — only if retention/history is enabled.

## Future endpoint groups
Voice: `/voice-inputs`, `/voice-inputs/:id/transcript`, `/voice-inputs/:id/translate`. Files/OCR: `/files`, `/files/:id/extraction`, `/files/:id/translate`. Accounts: `/users/me`, sessions/OIDC callback. Community: `/community/content`, search, bookmarks, publication/moderation actions. Intelligent translation: suggestions, glossary, feedback. These are placeholders and require phase-specific design.

## Operational behavior
Use idempotency keys for retried submissions, bounded payloads, rate limits, timeouts, and asynchronous job status when processing is long. Authentication, authorization, CSRF/CORS, quotas, and audit events must be finalized before public deployment.
