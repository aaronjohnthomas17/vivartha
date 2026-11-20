# Initial Database Design (Planning Only)

## Phase 1 entities
`users` is optional pending account decision. `translation_records` stores request metadata, source/target language, source/output content only if retention is approved, provider/model version, status, timestamps, and error category. `saved_translations` is later and should reference a translation record or snapshot according to retention policy.

## Later entities
`files`/`processing_jobs` for upload metadata and lifecycle; `voice_inputs` for consented audio metadata and transcript version; `community_content` for owner, permission declaration, publication/moderation state, language metadata, and content reference; `bookmarks` for user/content relationships.

## Relationships and indexing
Users own records, files, voice inputs, saved items, and bookmarks. Index user/time and status/time for history and operations; unique compound indexes should prevent duplicate bookmark relationships. Search indexes are a Phase 4 decision. Avoid indexing raw text until privacy and search requirements justify it.

## Lifecycle/privacy/scalability
Define retention, deletion, export, and redaction before storing source text, audio, or files. Store large binaries in object storage, not database documents. Use provider/model version fields for reproducibility. MongoDB is provisional; PostgreSQL remains a credible alternative if relational constraints, reporting, or community relationships dominate.
