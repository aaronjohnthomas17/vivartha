import React, { useState } from 'react';
import { createRoot } from 'react-dom/client';
import './styles.css';

const languages = [['ml','Malayalam'],['ta','Tamil'],['te','Telugu'],['kn','Kannada'],['hi','Hindi'],['en','English']];

function App() {
  const [sourceLanguage, setSourceLanguage] = useState('en');
  const [text, setText] = useState('');
  const [translation, setTranslation] = useState('');
  const [status, setStatus] = useState('idle');
  const [error, setError] = useState('');
  const [copied, setCopied] = useState(false);
  const [file, setFile] = useState(null);
  const [detectedLanguage, setDetectedLanguage] = useState('');
  const [translatedFileName, setTranslatedFileName] = useState('');

  async function translate() {
    if (!text.trim()) { setError('Enter text to translate.'); setStatus('error'); return; }
    setStatus('loading'); setError(''); setTranslation(''); setCopied(false);
    try {
      const response = await fetch(`${import.meta.env.VITE_API_URL || 'http://127.0.0.1:3001'}/api/translate`, {
        method: 'POST', headers: {'content-type':'application/json'}, body: JSON.stringify({ sourceLanguage, text })
      });
      const payload = await response.json().catch(() => ({}));
      if (!response.ok || !payload.success) throw new Error(payload.error || 'Translation failed.');
      setTranslation(payload.translation); setStatus('success');
    } catch (e) { setError(e.message || 'Unable to translate right now.'); setStatus('error'); }
  }
  function clear() { setText(''); setTranslation(''); setError(''); setStatus('idle'); setCopied(false); setDetectedLanguage(''); setTranslatedFileName(''); }
  async function translateFile() {
    if (!file) { setError('Choose a text file to translate.'); setStatus('error'); return; }
    setStatus('loading'); setError(''); setTranslation(''); setDetectedLanguage(''); setTranslatedFileName('');
    try {
      const form = new FormData(); form.append('file', file);
      const response = await fetch(`${import.meta.env.VITE_API_URL || 'http://127.0.0.1:3001'}/api/translate-file`, { method: 'POST', body: form });
      const payload = await response.json().catch(() => ({}));
      if (!response.ok || !payload.success) throw new Error(payload.error || 'File translation failed.');
      setText(payload.extractedText || ''); setTranslation(payload.translation); setDetectedLanguage(payload.detectedLanguageName); setTranslatedFileName(`${file.name.replace(/\.[^.]+$/, '')}-malayalam.txt`); setStatus('success');
    } catch (e) { setError(e.message || 'Unable to translate the file right now.'); setStatus('error'); }
  }
  function downloadFile() {
    if (!translation || !translatedFileName) return;
    const blob = new Blob([translation], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob); const link = document.createElement('a');
    link.href = url; link.download = translatedFileName; link.click(); URL.revokeObjectURL(url);
  }
  async function copy() {
    if (!translation) return;
    try { await navigator.clipboard.writeText(translation); setCopied(true); setTimeout(() => setCopied(false), 1800); }
    catch { setError('Copying is unavailable in this browser. Select the translation and copy it manually.'); }
  }

  return <main className="shell"><section className="card">
    <header><p className="eyebrow">VIVARTHA</p><h1>Translate into Malayalam</h1><p className="intro">A simple Malayalam-centered translation workspace.</p></header>
    <div className="controls"><label>Source language<select value={sourceLanguage} onChange={e=>setSourceLanguage(e.target.value)}>{languages.map(([code,name])=><option key={code} value={code}>{name}</option>)}</select></label><div className="target"><span>Target language</span><strong>Malayalam</strong></div></div>
    <label className="field">Text to translate<textarea value={text} onChange={e=>setText(e.target.value)} placeholder="Enter text here..." maxLength="10000" /></label>
    {error && <p className="error" role="alert">{error}</p>}
    <div className="actions"><button className="primary" onClick={translate} disabled={status==='loading'}>{status==='loading'?'Translating...':'Translate'}</button><button onClick={clear}>Clear</button></div>
    <div className="file-panel"><label className="field">Translate a text file<input type="file" accept=".txt,.md,.csv,text/plain,text/markdown,text/csv" onChange={e=>setFile(e.target.files?.[0] || null)} /></label><button onClick={translateFile} disabled={status==='loading'}>Translate file</button>{detectedLanguage && <p className="detected">Detected language: <strong>{detectedLanguage}</strong></p>}</div>
    <label className="field">Malayalam translation<textarea value={translation} readOnly placeholder="Your translation will appear here..." /></label>
    <div className="output-actions"><button className="copy" onClick={copy} disabled={!translation}>{copied ? 'Copied' : 'Copy translation'}</button>{translatedFileName && <button className="download" onClick={downloadFile}>Download translated file</button>}</div>
  </section></main>;
}
createRoot(document.getElementById('root')).render(<App />);
