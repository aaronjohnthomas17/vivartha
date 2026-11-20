import json, re
from pathlib import Path
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from IndicTransToolkit.processor import IndicProcessor

MODEL='ai4bharat/indictrans2-indic-indic-dist-320M'
codes={'ta':'tam_Taml','te':'tel_Telu','kn':'kan_Knda','hi':'hin_Deva','en':'eng_Latn'}
clock=re.compile(r'(?<!\d)(?:[01]?\d|2[0-3]):[0-5]\d(?!\d)')
contexts={
 'ta': [('10:20','வகுப்பு 10:20 மணிக்கு தொடங்கும்.'),('4:15','கூட்டம் 4:15 மணிக்கு தொடங்கும்.'),('7:30','நாங்கள் 7:30 மணிக்கு புறப்படுவோம்.'),('8:40','பேருந்து 8:40 மணிக்கு வரும்.'),('6:45','தேர்வு 6:45 மணிக்கு தொடங்கும்.'),('12:00','நிகழ்ச்சி 12:00 மணிக்கு தொடங்கும்.'),('1:05','ரயில் 1:05 மணிக்கு புறப்படும்.'),('11:55','அலுவலகம் 11:55 மணிக்கு மூடப்படும்.')],
 'te': [('10:20','తరగతి 10:20కి ప్రారంభమవుతుంది.'),('4:15','సమావేశం 4:15కి ప్రారంభమవుతుంది.'),('7:30','మేము 7:30కి బయలుదేరుతాము.'),('8:40','బస్సు 8:40కి వస్తుంది.'),('6:45','పరీక్ష 6:45కి ప్రారంభమవుతుంది.'),('12:00','కార్యక్రమం 12:00కి ప్రారంభమవుతుంది.'),('1:05','రైలు 1:05కి బయలుదేరుతుంది.'),('11:55','కార్యాలయం 11:55కి మూసివేయబడుతుంది.')],
 'kn': [('10:20','ತರಗತಿ 10:20ಕ್ಕೆ ಪ್ರಾರಂಭವಾಗುತ್ತದೆ.'),('4:15','ಸಭೆ 4:15ಕ್ಕೆ ಪ್ರಾರಂಭವಾಗುತ್ತದೆ.'),('7:30','ನಾವು 7:30ಕ್ಕೆ ಹೊರಡುತ್ತೇವೆ.'),('8:40','ಬಸ್ 8:40ಕ್ಕೆ ಬರುತ್ತದೆ.'),('6:45','ಪರೀಕ್ಷೆ 6:45ಕ್ಕೆ ಪ್ರಾರಂಭವಾಗುತ್ತದೆ.'),('12:00','ಕಾರ್ಯಕ್ರಮ 12:00ಕ್ಕೆ ಪ್ರಾರಂಭವಾಗುತ್ತದೆ.'),('1:05','ರೈಲು 1:05ಕ್ಕೆ ಹೊರಡುತ್ತದೆ.'),('11:55','ಕಚೇರಿ 11:55ಕ್ಕೆ ಮುಚ್ಚುತ್ತದೆ.')],
 'hi': [('10:20','कक्षा 10:20 बजे शुरू होगी।'),('4:15','बैठक 4:15 बजे शुरू होगी।'),('7:30','हम 7:30 बजे निकलेंगे।'),('8:40','बस 8:40 बजे आएगी।'),('6:45','परीक्षा 6:45 बजे शुरू होगी।'),('12:00','कार्यक्रम 12:00 बजे शुरू होगा।'),('1:05','ट्रेन 1:05 बजे रवाना होगी।'),('11:55','कार्यालय 11:55 बजे बंद होगा।')],
 'en': [('10:20','The class starts at 10:20.'),('4:15','The meeting starts at 4:15.'),('7:30','We will leave at 7:30.'),('8:40','The bus arrives at 8:40.'),('6:45','The exam begins at 6:45.'),('12:00','The event starts at 12:00.'),('1:05','The train leaves at 1:05.'),('11:55','The office closes at 11:55.')],
}
controls={'ratio':'The ratio is 4:1.','port':'The service uses port 3001.','date':'The meeting is on 12 June 2026.','punctuation':'Note: bring your identity card.','multiple':'The ratio is 4:1 and the service uses port 3001.','none':'The library opens every day.'}

def esc(x): return x.encode('unicode_escape').decode()
def preprocess(src,text,proc):
 return proc.preprocess_batch([text],src_lang=codes[src],tgt_lang='mal_Mlym')[0]
def infer(src,text,tok,model,proc):
 p=preprocess(src,text,proc); inp=tok(p,truncation=True,padding='longest',return_tensors='pt')
 with torch.inference_mode(): out=model.generate(**inp,max_length=256,num_beams=5)
 decoded=tok.batch_decode(out,skip_special_tokens=True)[0]
 return p,decoded,proc.postprocess_batch([decoded],lang='mal_Mlym')[0]
def protect(text):
 found=clock.findall(text); return clock.sub(lambda _: 'CLOCKTOKEN',text),found
def restore(out,found):
 for value in found: out=out.replace('CLOCKTOKEN',value,1)
 return out

tok=AutoTokenizer.from_pretrained(MODEL,trust_remote_code=True); model=AutoModelForSeq2SeqLM.from_pretrained(MODEL,trust_remote_code=True); proc=IndicProcessor(inference=True)
data={'pattern':clock.pattern,'matrix':[],'contexts':[],'controls':[]}
for src,items in contexts.items():
 for value,text in items:
  plain=infer(src,text,tok,model,proc); protected,found=protect(text); exp=infer(src,protected,tok,model,proc)
  data['matrix'].append({'lang':src,'time':value,'source':text,'plainPrep':esc(plain[0]),'protectedSource':protected,'protectedPrep':esc(exp[0]),'plainOutput':plain[2],'protectedOutput':restore(exp[2],found),'protectedRawOutput':exp[2],'preservedInPrep':'CLOCKTOKEN' in exp[0]})
for name,text in controls.items():
 p,d,o=infer('en',text,tok,model,proc); protected,found=protect(text); ep,ed,eo=infer('en',protected,tok,model,proc); data['controls'].append({'name':name,'source':text,'plainPrep':esc(p),'protectedSource':protected,'protectedPrep':esc(ep),'plainOutput':o,'protectedOutput':restore(eo,found),'changedByPattern':bool(found)})
(Path(__file__).parent/'PHASE_1_TIME_EXPERIMENT_RAW.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print('matrix',len(data['matrix']),'controls',len(data['controls']))
