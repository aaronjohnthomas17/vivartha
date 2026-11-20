# VIVARTHA Phase 1 — Core Text Translation MVP

This repository now contains the Phase 1 service boundaries: React frontend, Node/Express backend, and Python translation service. MongoDB is intentionally not part of the translation request path because Phase 1 does not require persistence.

## Prerequisites

- Node.js 20+
- Python 3.10+
- A Python environment with the IndicTrans2 dependencies and model artifacts installed

## Run locally

1. Start the Python service:

   ```powershell
   cd translation-service
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   $env:INDICTRANS2_MODEL_PATH = 'C:\path\to\model'
   python service.py
   ```

2. In another terminal, start the Node backend:

   ```powershell
   cd backend
   npm install
   Copy-Item .env.example .env
   npm run dev
   ```

3. In another terminal, start React:

   ```powershell
   cd frontend
   npm install
   npm run dev
   ```

Open the Vite URL shown in the terminal. The frontend calls `POST /api/translate`; the backend forwards to the Python service at `TRANSLATION_SERVICE_URL`.

IndicTrans2 model setup is intentionally environment-specific. The service fails clearly if the model path or required package is missing; it does not substitute an unrelated translation engine.
