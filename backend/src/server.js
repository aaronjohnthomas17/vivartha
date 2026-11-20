import 'dotenv/config';
import cors from 'cors';
import express from 'express';

const app = express();
const port = Number(process.env.PORT || 3001);
const serviceUrl = process.env.TRANSLATION_SERVICE_URL || 'http://127.0.0.1:8000';
const timeoutMs = Number(process.env.TRANSLATION_TIMEOUT_MS || 120000);
const languages = new Set(['ml', 'ta', 'te', 'kn', 'hi', 'en']);

app.use(cors());
app.use(express.json({ limit: '256kb' }));

app.get('/api/health', (_req, res) => res.json({ success: true, service: 'backend' }));

app.post('/api/translate', async (req, res) => {
  const { sourceLanguage, text } = req.body ?? {};
  if (typeof sourceLanguage !== 'string' || !languages.has(sourceLanguage)) {
    return res.status(400).json({ success: false, error: 'Unsupported source language.' });
  }
  if (typeof text !== 'string' || !text.trim()) {
    return res.status(400).json({ success: false, error: 'Enter text to translate.' });
  }
  if (text.length > 10000) {
    return res.status(413).json({ success: false, error: 'Text is too long. Limit is 10,000 characters.' });
  }

  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);
  try {
    const response = await fetch(`${serviceUrl}/translate`, {
      method: 'POST', headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ sourceLanguage, targetLanguage: 'ml', text }), signal: controller.signal
    });
    const payload = await response.json().catch(() => ({}));
    if (!response.ok) return res.status(502).json({ success: false, error: payload.error || 'Translation service failed.' });
    if (typeof payload.translation !== 'string') return res.status(502).json({ success: false, error: 'Translation service returned an invalid response.' });
    return res.json({ success: true, translation: payload.translation });
  } catch (error) {
    const message = error.name === 'AbortError' ? 'Translation timed out.' : 'Translation service is unavailable.';
    return res.status(503).json({ success: false, error: message });
  } finally { clearTimeout(timer); }
});

app.use((_req, res) => res.status(404).json({ success: false, error: 'Not found.' }));
app.listen(port, () => console.log(`VIVARTHA backend listening on http://127.0.0.1:${port}`));
