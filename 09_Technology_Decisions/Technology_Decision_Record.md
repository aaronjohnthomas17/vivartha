# Technology Decision Record

## Decision set (2026-09-27)

| Area | Current position | Status |
|---|---|---|
| Translation | IndicTrans2 is the planned candidate; benchmark locally before committing hosting/configuration. | Provisional |
| Application shape | React client plus HTTP API, with Python model boundary if runtime requires it. | Provisional |
| API runtime | Node.js/Express is acceptable candidate; FastAPI remains an alternative for a Python-first service. | Provisional |
| Database | MongoDB is acceptable candidate for flexible records; PostgreSQL remains open. | Provisional |
| OCR/ASR | No provider selected. Tesseract and Whisper are research candidates. | Undecided |
| Accounts | Not required until the Phase 1 privacy/history decision is made. | Open |

## Selection criteria
Malayalam and initial-language support, measurable quality, total cost, hardware needs, latency, privacy, licensing, maintainability, observability, and ability to replace the component.

## Consequence
No stack is final. Before Phase 1, run a small feasibility benchmark and record model/provider, hardware, license, latency, error rate, and representative-language quality. This document must be updated rather than silently treating the current direction as final.
