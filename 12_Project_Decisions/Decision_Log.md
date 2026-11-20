# Project Decision Log

| ID | Date | Decision/context | Alternatives/reason | Consequence/status |
|---|---|---|---|---|
| D-001 | 2026-09-27 | Keep Phase 0 documentation-only; baseline PRD/phases govern scope. | Start application work / defer planning. User explicitly requires planning first. | No frontend/backend/database/API implementation. Confirmed. |
| D-002 | 2026-09-27 | Malayalam is primary target; initial priorities are Malayalam, Tamil, Telugu, Kannada, Hindi, English. | Broader initial language set. Follows PRD. | Evaluation and UI metadata must reflect these priorities. Confirmed. |
| D-003 | 2026-09-27 | IndicTrans2 remains planned candidate, not final deployment decision. | Commercial APIs, NLLB, other Indic models. Need evidence on quality, cost, hardware, license. | Run feasibility benchmark before Phase 1. Provisional. |
| D-004 | 2026-09-27 | Use modular logical boundaries before splitting services. | Immediate microservices / single tightly coupled app. | Lower early complexity while preserving replacement points. Proposed. |
| D-005 | 2026-09-27 | Begin Phase 1 with React, Node/Express, Python, and IndicTrans2; omit MongoDB from the request path. | User's Phase 1 transition instructions and no persistence requirement. | Translation remains independently testable; persistence can be added later. Confirmed. |
| D-006 | 2026-09-27 | Use the IndicTrans2 Hugging Face Indic-to-Indic distilled checkpoint as the default adapter target, configurable by environment. | Fairseq/manual checkpoint wiring. | Smaller practical starting point; checkpoint/hardware still require runtime verification. Provisional. |
| D-007 | 2026-11-20 | Treat Phase 0 as complete for roadmap purposes and continue from Phase 1. | Earlier checklist wording suggested that Phase 1 had not started, but later implementation and validation records confirm the Phase 1 MVP is operational. | Update status documents; do not redo Phase 0. Phase 1 closure and Phase 2 scope review are next. Confirmed. |

Important future decisions requiring the owner: account requirement, history retention, hosting/hardware/budget, privacy jurisdiction, Phase 2 ASR choice and scope, and final database/API/runtime choices where not already resolved by the Phase 1 MVP.
