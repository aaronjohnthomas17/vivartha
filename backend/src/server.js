import 'dotenv/config';
import cors from 'cors';
import express from 'express';
import multer from 'multer';

const app = express();
const port = Number(process.env.PORT || 3001);
const serviceUrl = process.env.TRANSLATION_SERVICE_URL || 'http://127.0.0.1:8000';
const timeoutMs = Number(process.env.TRANSLATION_TIMEOUT_MS || 120000);
const languages = new Set(['ml', 'ta', 'te', 'kn', 'hi', 'en']);
const languageNames = { ml: 'Malayalam', ta: 'Tamil', te: 'Telugu', kn: 'Kannada', hi: 'Hindi', en: 'English' };
const maxFileBytes = 256 * 1024;
const supportedExtensions = new Set(['.txt', '.md', '.csv']);
const upload = multer({ storage: multer.memoryStorage(), limits: { fileSize: maxFileBytes, files: 1 } });

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

function detectLanguage(text) {
  const counts = { ml: 0, ta: 0, te: 0, kn: 0, hi: 0 };
  for (const char of text) {
    const code = char.codePointAt(0);
    if (code >= 0x0d00 && code <= 0x0d7f) counts.ml++;
    else if (code >= 0x0b80 && code <= 0x0bff) counts.ta++;
    else if (code >= 0x0c00 && code <= 0x0c7f) counts.te++;
    else if (code >= 0x0c80 && code <= 0x0cff) counts.kn++;
    else if (code >= 0x0900 && code <= 0x097f) counts.hi++;
  }
  const detected = Object.entries(counts).sort((a, b) => b[1] - a[1])[0];
  return detected[1] > 0 ? detected[0] : 'en';
}

app.post('/api/translate-file', (req, res) => upload.single('file')(req, res, async (uploadError) => {
  if (uploadError) {
    const message = uploadError.code === 'LIMIT_FILE_SIZE' ? 'File is too large. Limit is 256 KB.' : 'Upload one supported text file.';
    return res.status(uploadError.code === 'LIMIT_FILE_SIZE' ? 413 : 400).json({ success: false, error: message });
  }
  if (!req.file) return res.status(400).json({ success: false, error: 'Choose a text file to translate.' });
  const extension = req.file.originalname.slice(req.file.originalname.lastIndexOf('.')).toLowerCase();
  if (!supportedExtensions.has(extension)) return res.status(415).json({ success: false, error: 'Supported files are .txt, .md, and .csv.' });
  const text = req.file.buffer.toString('utf8');
  if (text.includes('\ufffd')) return res.status(400).json({ success: false, error: 'The file must be valid UTF-8 text.' });
  if (!text.trim()) return res.status(400).json({ success: false, error: 'The file is empty.' });
  if (text.length > 10000) return res.status(413).json({ success: false, error: 'Text is too long. Limit is 10,000 characters.' });
  const sourceLanguage = detectLanguage(text);
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);
  try {
    const response = await fetch(`${serviceUrl}/translate`, { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify({ sourceLanguage, targetLanguage: 'ml', text }), signal: controller.signal });
    const payload = await response.json().catch(() => ({}));
    if (!response.ok || typeof payload.translation !== 'string') return res.status(502).json({ success: false, error: payload.error || 'Translation service failed.' });
    return res.json({ success: true, fileName: req.file.originalname, extractedText: text, detectedLanguage: sourceLanguage, detectedLanguageName: languageNames[sourceLanguage], translation: payload.translation });
  } catch (error) {
    return res.status(error.name === 'AbortError' ? 504 : 503).json({ success: false, error: error.name === 'AbortError' ? 'Translation timed out.' : 'Translation service is unavailable.' });
  } finally { clearTimeout(timer); }
}));

app.use((_req, res) => res.status(404).json({ success: false, error: 'Not found.' }));
app.listen(port, () => console.log(`VIVARTHA backend listening on http://127.0.0.1:${port}`));
