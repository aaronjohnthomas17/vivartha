# Development Roadmap

## Phase 0 — Research & Planning
Objective: produce the blueprint, research, decisions, and Phase 1 gate. Prerequisites: baseline PRD and phases. Deliverables: this documentation set, open questions, evaluation plan. Completion: checklist approved and decisions needed for Phase 1 resolved.

## Phase 1 — Core Text Translation MVP
Objective: usable text-to-Malayalam workflow. Prerequisites: Phase 0 gate, model feasibility, privacy/retention decision. Tasks: UI, API, translation adapter, selected engine, history if approved, validation, observability, tests. Deliverable: working MVP. Completion: end-to-end acceptance and quality/performance baseline.

**Current status:** Phase 1 implementation and validation are complete from a core-MVP perspective. The pipeline is operational, the frozen benchmark baseline is documented, and known translation-quality limitations are recorded for future improvement. The immediate next action is to formally close Phase 1 and approve Phase 2 scope; Phase 2 must not begin automatically.

## Phase 2 — Text File Translation
Prerequisite: Phase 1 workflow and language-identification evaluation. Tasks: supported text-file upload, safe text extraction, automatic source-language identification, translation integration, Malayalam output display, validation, limits, and privacy. Deliverable: verified text-file-to-Malayalam workflow. Test representative languages, encoding, empty/unreadable files, size limits, unsupported formats, detection errors, translation errors, and deletion/retention behavior.

## Phase 3 — Document & Image Translation
Prerequisite: stable translation workflow and extraction/OCR research. Tasks: safe PDF/DOCX uploads, OCR, preview/edit, jobs, output handling. Deliverable: verified document/image workflow. Test layouts, scans, Malayalam scripts, limits, malware handling, and extraction errors.

## Phase 4 — Community Platform
Prerequisite: account/security/privacy design and content-permission policy. Tasks: users, library, publishing, moderation, search, bookmarks. Deliverable: permitted community library. Test authorization, abuse reporting, takedown, copyright metadata, and privacy.

## Phase 5 — Intelligent Translation
Prerequisite: evaluation data and user feedback. Tasks: detection, alternatives, context/style, glossary, feedback. Deliverable: measured improvements. Test regressions, confidence communication, and domain behavior.

## Phase 6 — Platform Expansion
Prerequisite: stable platform operations. Tasks: camera/live OCR, handwriting research, TTS, downloads, languages, mobile. Deliverable: selected expansion features. Test device/accessibility/performance matrix.

## Phase 7 — Advanced AI Ecosystem
Prerequisite: product evidence, safety/privacy review, sustainable operations. Tasks: conversation translation, assistant, learning, offline, extension. Deliverable: individually approved ecosystem capabilities. Test safety, consent, quality, and resource use.

The roadmap has no arbitrary deadlines; phase gates depend on evidence and decisions.
