# VIVARTHA Project Definition

## Vision and problem
VIVARTHA is a Malayalam-centered multilingual translation platform. It addresses the fragmentation of tools for translating text, speech, documents, and images into Malayalam. Users should be able to verify text produced by speech recognition, OCR, or extraction before translation.

## Objectives and value
- Make translation into Malayalam accessible through a consistent workflow.
- Prioritize Malayalam output and the initial languages Malayalam, Tamil, Telugu, Kannada, Hindi, and English.
- Start with a focused text-to-Malayalam MVP and grow through documented phases.
- Keep processing components replaceable and the platform scalable.

## Users and workflows
Primary users are Malayalam readers, students, educators, researchers, and people working across the initial languages. Core workflows are text input → source language → translation → Malayalam output; later voice and file/image workflows add verification/editing before translation. Community workflows add accounts, personal libraries, permitted publishing, search, reading, and bookmarks.

## Scope boundaries
Phase 1 includes text input, source selection, Malayalam output, copy/clear, and basic history. Voice, files/images, community, intelligent translation, mobile, offline, browser extension, and live conversation translation remain later-phase or long-term scope. Phase 0 itself produces documentation and research, not application code.

## Scalability goals
Support new languages, translation engines, input methods, clients, storage providers, and AI services through clear interfaces. Avoid coupling user-facing workflows to one model vendor or one processing implementation.

## Source of truth
The baseline is `VIVARTHA_PRD.md` and `VIVARTHA_PHASES.md`. Refinements are recorded in `12_Project_Decisions/` and must not silently replace those documents.
