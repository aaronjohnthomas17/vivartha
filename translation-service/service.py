import os
from flask import Flask, jsonify, request

app = Flask(__name__)
SUPPORTED = {'ml': 'mal_Mlym', 'ta': 'tam_Taml', 'te': 'tel_Telu', 'kn': 'kan_Knda', 'hi': 'hin_Deva', 'en': 'eng_Latn'}
translator = None
load_error = None

def load_translator():
    global translator, load_error
    try:
        # Hugging Face IndicTrans2 adapter. The model is loaded once at startup.
        import torch
        from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
        from IndicTransToolkit import IndicProcessor
        model_name = os.environ.get('INDICTRANS2_MODEL_PATH', 'ai4bharat/indictrans2-indic-indic-dist-320M')
        tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name, trust_remote_code=True)
        model.eval()
        processor = IndicProcessor(inference=True)
        translator = (tokenizer, model, processor, torch)
    except Exception as exc:
        load_error = str(exc)

@app.get('/health')
def health():
    status = 200 if translator is not None else 503
    return jsonify({'success': translator is not None, 'modelLoaded': translator is not None,
                    'error': None if translator is not None else 'IndicTrans2 is not ready.'}), status

@app.post('/translate')
def translate():
    body = request.get_json(silent=True) or {}
    source = body.get('sourceLanguage')
    target = body.get('targetLanguage')
    text = body.get('text')
    if source not in SUPPORTED or target != 'ml' or not isinstance(text, str) or not text.strip():
        return jsonify({'success': False, 'error': 'Invalid source language, target language, or text.'}), 400
    if translator is None:
        return jsonify({'success': False, 'error': 'IndicTrans2 is not ready. Configure the model and restart the service.'}), 503
    try:
        tokenizer, model, processor, torch = translator
        prepared = processor.preprocess_batch([text], src_lang=SUPPORTED[source], tgt_lang=SUPPORTED[target])
        inputs = tokenizer(prepared, truncation=True, padding='longest', return_tensors='pt')
        with torch.inference_mode():
            generated = model.generate(**inputs, max_length=256, num_beams=5)
        decoded = tokenizer.batch_decode(generated, skip_special_tokens=True)
        result = processor.postprocess_batch(decoded, lang=SUPPORTED[target])[0]
        return jsonify({'success': True, 'translation': result})
    except Exception:
        return jsonify({'success': False, 'error': 'Translation failed.'}), 500

load_translator()
if __name__ == '__main__':
    app.run(host=os.environ.get('HOST', '127.0.0.1'), port=int(os.environ.get('PORT', '8000')))
