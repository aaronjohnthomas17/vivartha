# UI/UX Plan

## Phase 1 screens
**Translator:** source-language selector, text input, translate button, Malayalam output, copy, clear, history entry point if approved. **History:** paginated records, empty state, delete/privacy explanation if enabled. **Help/error state:** plain-language validation, unavailable-service, timeout, and retry guidance.

## States and accessibility
Show idle, validating, loading, success, partial/error, and empty states. Preserve entered text on recoverable errors. Disable duplicate submission while processing, announce status to assistive technology, support keyboard navigation, readable contrast, responsive layout, and Malayalam text rendering.

## Later extensions
Voice adds recording/upload, transcript editor, verification gate, and audio permissions. Files/images add upload progress, extraction preview/editor, OCR warnings, and translation. Community adds account, library, search/read, bookmark, publish-permission, and moderation states. Do not design these as Phase 1 implementation scope.
