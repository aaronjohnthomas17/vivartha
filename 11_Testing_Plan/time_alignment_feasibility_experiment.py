import json
import re
from pathlib import Path
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from IndicTransToolkit.processor import IndicProcessor

MODEL = "ai4bharat/indictrans2-indic-indic-dist-320M"
TARGET = "mal_Mlym"
CODES = {"ta":"tam_Taml", "te":"tel_Telu", "kn":"kan_Knda", "hi":"hin_Deva", "en":"eng_Latn"}
CLOCK = re.compile(r"(?<!\d)(?:[01]?\d|2[0-3]):[0-5]\d(?!\d)")

CASES = [
 ("ta", "நான் 4:15 மணிக்கு வீட்டிற்கு வருவேன்."), ("ta", "வகுப்பு 10:20 மணிக்கு தொடங்கும்."),
 ("ta", "அவர் 7:30 மணிக்கு அலுவலகத்தை அடைந்தார்."), ("ta", "நாம் நாளை 6:45 மணிக்கு சந்திப்போம்."),
 ("te", "నేను 4:15కి ఇంటికి వస్తాను."), ("te", "తరగతి 10:20కి ప్రారంభమవుతుంది."),
 ("te", "ఆమె 7:30కి కార్యాలయానికి చేరుకుంది."), ("te", "మేము రేపు 6:45కి కలుస్తాము."),
 ("kn", "ನಾನು 4:15ಕ್ಕೆ ಮನೆಗೆ ಬರುತ್ತೇನೆ."), ("kn", "ತರಗತಿ 10:20ಕ್ಕೆ ಪ್ರಾರಂಭವಾಗುತ್ತದೆ."),
 ("kn", "ಅವರು 7:30ಕ್ಕೆ ಕಚೇರಿಗೆ ತಲುಪಿದರು."), ("kn", "ನಾವು ನಾಳೆ 6:45ಕ್ಕೆ ಭೇಟಿಯಾಗುತ್ತೇವೆ."),
 ("hi", "मैं 4:15 बजे घर आऊँगा।"), ("hi", "कक्षा 10:20 बजे शुरू होगी।"),
 ("hi", "वह 7:30 बजे कार्यालय पहुँची।"), ("hi", "हम कल 6:45 बजे मिलेंगे।"),
 ("en", "I will come home at 4:15."), ("en", "The class starts at 10:20."),
 ("en", "She reached the office at 7:30."), ("en", "We will meet tomorrow at 6:45."),
]
TRACE = [("ta", "நான் 10:20 மணிக்கு வருவேன்."), ("ta", "ரயில் 6:45 மணிக்கு புறப்படும்."),
         ("te", "சந்திப்பு 4:15க்கு தொடங்கும்."), ("te", "பேருந்து 7:30కి వస్తుంది."),
         ("kn", "ಸಭೆ 7:30ಕ್ಕೆ ಪ್ರಾರಂಭವಾಗುತ್ತದೆ."), ("kn", "ಕಚೇರಿ 11:55ಕ್ಕೆ ಮುಚ್ಚುತ್ತದೆ."),
         ("hi", "बस 8:40 बजे आएगी।"), ("hi", "ट्रेन 1:05 बजे रवाना होगी।"),
         ("en", "The meeting starts at 4:15.")]
CONTROLS = ["4:1", "4:1 ratio", "3:2", "2026:10", "Note: bring your card.", "The value is 4:15 units."]

def run(src, text, tok, model, proc):
    prepared = proc.preprocess_batch([text], src_lang=CODES[src], tgt_lang=TARGET)[0]
    inputs = tok(prepared, truncation=True, padding="longest", return_tensors="pt")
    with torch.inference_mode():
        generated = model.generate(**inputs, max_length=256, num_beams=5)
    decoded = tok.batch_decode(generated, skip_special_tokens=True)[0]
    final = proc.postprocess_batch([decoded], lang=TARGET)[0]
    return {"original": text, "preprocessed": prepared, "model_input": prepared,
            "model_output": decoded, "postprocessed": final, "final": final}

def detect(text):
    return [{"value": m.group(0), "start": m.start(), "end": m.end(),
             "context": text[max(0, m.start()-12):m.end()+12]} for m in CLOCK.finditer(text)]

def main():
    tok = AutoTokenizer.from_pretrained(MODEL, trust_remote_code=True, local_files_only=True)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL, trust_remote_code=True, local_files_only=True)
    proc = IndicProcessor(inference=True)
    traces = []
    for src, text in TRACE:
        original = run(src, text, tok, model, proc)
        found = detect(text)
        removed = CLOCK.sub("", text)
        gap = CLOCK.sub("[TIME_REMOVED]", text)
        traces.append({"language":src, "detection":found, "original_trace":original,
                       "removed_source":removed, "removed_trace":run(src, removed, tok, model, proc),
                       "gap_source":gap, "gap_trace":run(src, gap, tok, model, proc)})
    matrix = []
    for src, text in CASES:
        found = detect(text)
        removed = CLOCK.sub("", text)
        matrix.append({"language":src, "source":text, "detection":found,
                       "removed_source":removed,
                       "removed_output":run(src, removed, tok, model, proc)["final"]})
    controls = [{"text": x, "matches": detect(x)} for x in CONTROLS]
    result = {"model":MODEL, "target":TARGET, "clock_regex":CLOCK.pattern,
              "case_count":len(CASES), "trace_count":len(TRACE),
              "matrix":matrix, "traces":traces, "controls":controls}
    out = Path(__file__).parent / "PHASE_1_TIME_ALIGNMENT_FEASIBILITY_RAW.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"cases={len(CASES)} traces={len(TRACE)} controls={len(CONTROLS)} output={out}")

if __name__ == "__main__":
    main()
