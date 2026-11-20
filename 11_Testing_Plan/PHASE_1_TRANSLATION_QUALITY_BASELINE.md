# VIVARTHA Phase 1 Translation Quality Baseline

**Phase 1 Internal Translation Quality Baseline**

## Run metadata

- Benchmark: `PHASE_1_TRANSLATION_QUALITY_BENCHMARK.md` (100 fixed cases)
- Run time (UTC): `2026-10-03T11:54:11.892597+00:00`
- Model/checkpoint: `ai4bharat/indictrans2-indic-indic-dist-320M`
- Runtime: Python 3.14.8, PyTorch 2.14.1+cpu, Transformers 4.48.3, IndicTransToolkit 1.1.1
- Evaluation path: `POST http://127.0.0.1:3001/api/translate` → Python `/translate` → IndicTrans2
- Evaluation: semantic reviewer labels; not a formal accuracy percentage

## Overall summary

- Total cases: 100
- PASS: 88
- PARTIAL: 7
- FAIL: 5
- PASS + PARTIAL: 95

## Summary by language

| Language | PASS | PARTIAL | FAIL | Total |
|---|---:|---:|---:|---:|
| English | 17 | 2 | 1 | 20 |
| Tamil | 18 | 1 | 1 | 20 |
| Telugu | 18 | 1 | 1 | 20 |
| Kannada | 18 | 1 | 1 | 20 |
| Hindi | 17 | 2 | 1 | 20 |

## Summary by category

| Category | PASS | PARTIAL | FAIL | Total |
|---|---:|---:|---:|---:|
| AI/computer science | 5 | 0 | 0 | 5 |
| Coreference | 5 | 0 | 0 | 5 |
| Date | 5 | 0 | 0 | 5 |
| Everyday conversation | 5 | 0 | 0 | 5 |
| Future perfect | 0 | 5 | 0 | 5 |
| Future tense | 5 | 0 | 0 | 5 |
| Idiom | 5 | 0 | 0 | 5 |
| Long sentence | 5 | 0 | 0 | 5 |
| Multiple clauses | 5 | 0 | 0 | 5 |
| Name | 5 | 0 | 0 | 5 |
| Negative | 5 | 0 | 0 | 5 |
| Number | 5 | 0 | 0 | 5 |
| Past tense | 5 | 0 | 0 | 5 |
| Place | 5 | 0 | 0 | 5 |
| Present tense | 5 | 0 | 0 | 5 |
| Pronoun | 3 | 2 | 0 | 5 |
| Question | 5 | 0 | 0 | 5 |
| Structure | 4 | 0 | 1 | 5 |
| Technical/academic | 5 | 0 | 0 | 5 |
| Time | 1 | 0 | 4 | 5 |

## Case results

### English → Malayalam

| Case | Category | Source | Reference | Actual output | Result | Reviewer note |
|---|---|---|---|---|---|---|
| EN-01 | Everyday conversation | Please close the window before you leave. | നിങ്ങൾ പോകുന്നതിന് മുമ്പ് ജനൽ അടയ്ക്കുക. | ദയവായി നിങ്ങൾ പോകുന്നതിനുമുമ്പ് വിൻഡോ അടയ്ക്കുക. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| EN-02 | Question | Which bus goes to the railway station? | റെയിൽവേ സ്റ്റേഷനിലേക്ക് പോകുന്ന ബസ് ഏതാണ്? | ഏത് ബസ് റെയിൽവേ സ്റ്റേഷനിലേക്ക് പോകുന്നു? | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| EN-03 | Negative | I did not forget your message. | ഞാൻ നിങ്ങളുടെ സന്ദേശം മറന്നിട്ടില്ല. | നിങ്ങളുടെ സന്ദേശം ഞാൻ മറന്നില്ല. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| EN-04 | Present tense | The children study in the library every evening. | കുട്ടികൾ എല്ലാ വൈകുന്നേരവും ലൈബ്രറിയിൽ പഠിക്കുന്നു. | എല്ലാ വൈകുന്നേരവും ലൈബ്രറിയിൽ കുട്ടികൾ പഠിക്കുന്നു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| EN-05 | Past tense | Anil bought a new notebook yesterday. | അനിൽ ഇന്നലെ ഒരു പുതിയ നോട്ട്‌ബുക്ക് വാങ്ങി. | ഇന്നലെ അനിൽ ഒരു പുതിയ നോട്ട്ബുക്ക് വാങ്ങി. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| EN-06 | Future tense | The meeting will start at nine tomorrow. | യോഗം നാളെ ഒമ്പത് മണിക്ക് ആരംഭിക്കും. | നാളെ ഒൻപത് മണിക്ക് യോഗം ആരംഭിക്കും. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| EN-07 | Future perfect | By Friday, the engineers will have completed the bridge inspection. | വെള്ളിയാഴ്ചയ്ക്കുള്ളിൽ എഞ്ചിനീയർമാർ പാലത്തിന്റെ പരിശോധന പൂർത്തിയാക്കിയിട്ടുണ്ടാകും. | വെള്ളിയാഴ്ച, എഞ്ചിനീയർമാർ പാലം പരിശോധന പൂർത്തിയാക്കും. | **PARTIAL** | Future-perfect meaning is reduced to a simple future completion. |
| EN-08 | Date | The final examination is scheduled for 18 March 2027. | അന്തിമ പരീക്ഷ 2027 മാർച്ച് 18-ന് നിശ്ചയിച്ചിരിക്കുന്നു. | 2027 മാർച്ച് 18നാണ് അന്തിമ പരീക്ഷ ഷെഡ്യൂൾ ചെയ്തിരിക്കുന്നത്. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| EN-09 | Time | The train leaves at 6:45 in the morning. | ട്രെയിൻ രാവിലെ 6:45-ന് പുറപ്പെടും. | രാവിലെ 6:45 ന് ട്രെയിൻ വിടുന്നു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| EN-10 | Number | The warehouse received 2,450 kilograms of rice. | ഗോഡൗണിൽ 2,450 കിലോഗ്രാം അരി ലഭിച്ചു. | 2, 450 കിലോഗ്രാം അരി വെയർഹൌസിൽ നിന്ന് ലഭിച്ചു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| EN-11 | Name | Dr. Meera Thomas signed the report. | ഡോ. മീര തോമസ് റിപ്പോർട്ടിൽ ഒപ്പുവച്ചു. | ഡോ. മീര തോമസ് റിപ്പോർട്ടിൽ ഒപ്പുവച്ചു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| EN-12 | Place | The conference will be held in Kochi, Kerala. | സമ്മേളനം കേരളത്തിലെ കൊച്ചിയിൽ നടക്കും. | കേരളത്തിലെ കൊച്ചിയിലാണ് കോൺഫറൻസ് നടക്കുക. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| EN-13 | Pronoun | They gave her the keys after she showed them her identity card. | അവൾ തന്റെ തിരിച്ചറിയൽ കാർഡ് അവരെ കാണിച്ചതിന് ശേഷം അവർ അവൾക്ക് താക്കോലുകൾ നൽകി. | അവർ അവളുടെ തിരിച്ചറിയൽ കാർഡ് കാണിച്ചതിന് ശേഷം അവൾക്ക് താക്കോലുകൾ നൽകി. | **PARTIAL** | The output reverses the roles in the identity-card clause; the main key-giving event remains understandable. |
| EN-14 | Coreference | Riya told Maya that she had finished the assignment. | റിയ മായയോട് താൻ അസൈൻമെന്റ് പൂർത്തിയാക്കിയെന്ന് പറഞ്ഞു. | താൻ അസൈൻമെന്റ് പൂർത്തിയാക്കിയതായി റിയ മായയോട് പറഞ്ഞു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| EN-15 | Long sentence | Although the road was crowded, the ambulance reached the hospital quickly because the drivers made room for it. | റോഡ് തിരക്കേറിയിരുന്നെങ്കിലും ഡ്രൈവർമാർ വഴിയൊരുക്കിയതിനാൽ ആംബുലൻസ് ആശുപത്രിയിലെത്തിയത് വേഗത്തിലായിരുന്നു. | റോഡ് തിരക്കേറിയതാണെങ്കിലും, ഡ്രൈവർമാർ റൂം ഉണ്ടാക്കിയതിനാൽ ആംബുലൻസ് ഉടൻ തന്നെ ആശുപത്രിയിൽ എത്തി. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| EN-16 | Multiple clauses | When the rain stops, we will inspect the fields and decide whether the farmers can plant the seeds this week. | മഴ നിൽക്കുമ്പോൾ ഞങ്ങൾ വയലുകൾ പരിശോധിച്ച് ഈ ആഴ്ച കർഷകർക്ക് വിത്ത് നടാനാകുമോ എന്ന് തീരുമാനിക്കും. | മഴ നിർത്തുമ്പോൾ, ഈ ആഴ്ച കർഷകർക്ക് വിത്ത് നട്ടുപിടിപ്പിക്കാൻ കഴിയുമോ എന്ന് ഞങ്ങൾ ഫീൽഡുകൾ പരിശോധിക്കുകയും തീരുമാനിക്കുകയും ചെയ്യും. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| EN-17 | Technical/academic | The experiment measured the relationship between temperature and battery efficiency. | പരീക്ഷണം താപനിലയും ബാറ്ററിയുടെ കാര്യക്ഷമതയും തമ്മിലുള്ള ബന്ധം അളന്നു. | താപനിലയും ബാറ്ററി കാര്യക്ഷമതയും തമ്മിലുള്ള ബന്ധം ഈ പരീക്ഷണം അളന്നു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| EN-18 | AI/computer science | The neural network classifies images after training on labeled data. | ലേബൽ ചെയ്ത ഡാറ്റയിൽ പരിശീലനം നേടിയ ശേഷം ന്യൂറൽ നെറ്റ്‌വർക്ക് ചിത്രങ്ങളെ വർഗീകരിക്കുന്നു. | ലേബൽ ചെയ്ത ഡാറ്റയെക്കുറിച്ചുള്ള പരിശീലനത്തെത്തുടർന്ന് ന്യൂറൽ നെറ്റ്വർക്ക് വർഗ്ഗീകരിക്കുന്ന ചിത്രങ്ങൾ. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| EN-19 | Idiom | She kept an eye on the equipment during the demonstration. | പ്രദർശനത്തിനിടെ അവൾ ഉപകരണങ്ങളിൽ ശ്രദ്ധവെച്ചു. | പ്രദർശന വേളയിൽ അവൾ ഒരു കണ്ണ് ഉപകരണത്തിൽ സൂക്ഷിച്ചു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| EN-20 | Structure | Not only did the team solve the problem, but it also documented the solution. | സംഘം പ്രശ്നം പരിഹരിച്ചതുമാത്രമല്ല, പരിഹാരവും രേഖപ്പെടുത്തി. | ടീം പ്രശ്നം പരിഹരിച്ചില്ല, പക്ഷേ അത് പരിഹാരവും രേഖപ്പെടുത്തിയിട്ടുണ്ട്. | **FAIL** | Negation is introduced: the output says the team did not solve the problem. |
### Tamil → Malayalam

| Case | Category | Source | Reference | Actual output | Result | Reviewer note |
|---|---|---|---|---|---|---|
| TA-01 | Everyday conversation | தயவுசெய்து கதவை மூடுங்கள். | ദയവായി വാതിൽ അടയ്ക്കൂ. | ദയവായി വാതിൽ അടയ്ക്കുക. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TA-02 | Question | இந்த பேருந்து மருத்துவமனைக்கு செல்கிறதா? | ഈ ബസ് ആശുപത്രിയിലേക്ക് പോകുമോ? | ഈ ബസ് ആശുപത്രിയിൽ പോകുന്നുണ്ടോ? | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TA-03 | Negative | நான் இன்று அலுவலகத்திற்கு செல்லவில்லை. | ഞാൻ ഇന്ന് ഓഫീസിലേക്ക് പോയില്ല. | ഞാൻ ഇന്ന് ഓഫീസിൽ പോയിട്ടില്ല. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TA-04 | Present tense | மாணவர்கள் தினமும் தமிழ் பாடத்தைப் படிக்கிறார்கள். | വിദ്യാർത്ഥികൾ ദിവസവും തമിഴ് പാഠം പഠിക്കുന്നു. | വിദ്യാർത്ഥികൾ എല്ലാ ദിവസവും തമിഴ് പാഠം പഠിക്കുന്നു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TA-05 | Past tense | லதா நேற்று சென்னைக்கு சென்றார். | ലത ഇന്നലെ ചെന്നൈയിലേക്ക് പോയി. | ലതാ ഇന്നലെ ചെന്നൈയിലേക്ക് പോയി. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TA-06 | Future tense | அவர்கள் அடுத்த வாரம் புதிய திட்டத்தை தொடங்குவார்கள். | അവർ അടുത്ത ആഴ്ച പുതിയ പദ്ധതി ആരംഭിക്കും. | അവർ അടുത്തയാഴ്ച ഒരു പുതിയ പദ്ധതി ആരംഭിക്കും. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TA-07 | Future perfect | அடுத்த மாதத்திற்குள் குழு அறிக்கையை முடித்திருக்கும். | അടുത്ത മാസത്തിനുള്ളിൽ സംഘം റിപ്പോർട്ട് പൂർത്തിയാക്കിയിട്ടുണ്ടാകും. | അടുത്ത മാസത്തോടെ സമിതി റിപ്പോർട്ട് പൂർത്തിയാക്കുമായിരുന്നു. | **PARTIAL** | Future-perfect aspect is rendered with a less precise completed-future form. |
| TA-08 | Date | கூட்டம் 12 ஜூலை 2027 அன்று நடைபெறும். | യോഗം 2027 ജൂലൈ 12-ന് നടക്കും. | 2027 ജൂലൈ 12നാണ് യോഗം നടക്കുന്നത്. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TA-09 | Time | விமானம் இரவு 10:20 மணிக்கு புறப்படும். | വിമാനം രാത്രി 10:20-ന് പുറപ്പെടും. | വിമാനം രാത്രി <ഐ. ഡി. 1> ന് പറക്കും. | **FAIL** | The departure time is corrupted and is not recoverable as 10:20. |
| TA-10 | Number | கடையில் 875 புத்தகங்கள் உள்ளன. | കടയിൽ 875 പുസ്തകങ്ങളുണ്ട്. | കടയിൽ 875 പുസ്തകങ്ങളുണ്ട്. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TA-11 | Name | பேராசிரியர் அருண் குமார் மாணவர்களை வரவேற்றார். | പ്രൊഫസർ അരുൺ കുമാർ വിദ്യാർത്ഥികളെ സ്വാഗതം ചെയ്തു. | പ്രൊഫസർ അരുൺ കുമാർ വിദ്യാർത്ഥികളെ സ്വാഗതം ചെയ്തു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TA-12 | Place | நிகழ்ச்சி மதுரையில் உள்ள நகர மண்டபத்தில் நடக்கும். | പരിപാടി മധുരയിലെ നഗര ഹാളിൽ നടക്കും. | മധുരയിലെ സിറ്റി ഹാളിൽ പരിപാടി നടക്കും. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TA-13 | Pronoun | அவள் அவரிடம் தனது ஆவணத்தை கொடுத்தாள். | അവൾ അവന് തന്റെ രേഖ നൽകി. | അവൾ അവന് തൻ്റെ രേഖ നൽകി. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TA-14 | Coreference | குமார் ரவியிடம் தான் திட்டத்தை முடித்ததாக கூறினார். | കുമാർ രവിയോട് താൻ പദ്ധതി പൂർത്തിയാക്കിയെന്ന് പറഞ്ഞു. | താൻ പദ്ധതി പൂർത്തിയാക്കിയതായി കുമാർ രവിയോട് പറഞ്ഞു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TA-15 | Long sentence | மின்சாரம் தடைப்பட்டபோதும், செவிலியர்கள் நோயாளிகளைக் கவனித்து சிகிச்சையைத் தொடர்ந்தனர். | വൈദ്യുതി മുടങ്ങിയിട്ടും നഴ്സുമാർ രോഗികളെ പരിചരിച്ച് ചികിത്സ തുടർന്നു. | വൈദ്യുതി മുടങ്ങിയിട്ടും നഴ്സുമാർ രോഗികളെ ശ്രദ്ധിക്കുകയും ചികിത്സ തുടരുകയും ചെയ്തു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TA-16 | Multiple clauses | மழை பெய்தால், பள்ளி நிர்வாகம் விளையாட்டு போட்டியை வெள்ளிக்கிழமைக்கு மாற்றும். | മഴ പെയ്താൽ സ്കൂൾ ഭരണകൂടം കായികമത്സരം വെള്ളിയാഴ്ചയിലേക്ക് മാറ്റും. | മഴ ലഭിക്കുകയാണെങ്കിൽ സ്കൂൾ ഭരണകൂടം സ്പോർട്സ് മത്സരം വെള്ളിയാഴ്ചയിലേക്ക് മാറ്റും. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TA-17 | Technical/academic | இந்த ஆய்வு நீரின் தரம் மற்றும் மண் வளம் இடையிலான தொடர்பை விளக்குகிறது. | ഈ പഠനം ജലത്തിന്റെ ഗുണനിലവാരവും മണ്ണിന്റെ ഫലഭൂയിഷ്ഠതയും തമ്മിലുള്ള ബന്ധം വിശദീകരിക്കുന്നു. | ജലത്തിന്റെ ഗുണനിലവാരവും മണ്ണിന്റെ സമൃദ്ധിയും തമ്മിലുള്ള ബന്ധം ഈ പഠനം വിശദീകരിക്കുന്നു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TA-18 | AI/computer science | இயந்திரக் கற்றல் மாதிரி புதிய தரவிலிருந்து வடிவங்களை கண்டறிகிறது. | മെഷീൻ ലേണിംഗ് മാതൃക പുതിയ ഡാറ്റയിൽ നിന്ന് മാതൃകകൾ കണ്ടെത്തുന്നു. | മെഷീൻ ലേണിംഗ് മോഡൽ പുതിയ ഡാറ്റയിൽ നിന്ന് പാറ്റേണുകൾ കണ്ടെത്തുന്നു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TA-19 | Idiom | அவன் செய்தியை கேட்டதும் கைகளை கட்டிக்கொண்டு உட்காரவில்லை. | വാർത്ത കേട്ട ശേഷം അവൻ കൈകെട്ടി ഇരുന്നില്ല. | വാർത്ത കേട്ടപ്പോൾ കൈകൾ ചേർത്ത് ഇരുന്നില്ല. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TA-20 | Structure | வேலை முடிந்த பிறகு மட்டுமே அவர்கள் வீட்டிற்கு திரும்பினர். | ജോലി പൂർത്തിയായതിന് ശേഷമാണ് അവർ വീട്ടിലേക്ക് മടങ്ങിയത്. | ജോലി പൂർത്തിയായതിന് ശേഷം മാത്രമാണ് അവർ വീട്ടിലേക്ക് മടങ്ങിയത്. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
### Telugu → Malayalam

| Case | Category | Source | Reference | Actual output | Result | Reviewer note |
|---|---|---|---|---|---|---|
| TE-01 | Everyday conversation | దయచేసి నాకు ఒక గ్లాసు నీరు ఇవ్వండి. | ദയവായി എനിക്ക് ഒരു ഗ്ലാസ് വെള്ളം തരൂ. | ദയവായി എനിക്ക് ഒരു ഗ്ലാസ് വെള്ളം നൽകുക. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TE-02 | Question | ఈ రైలు విజయవాడకు వెళ్తుందా? | ഈ ട്രെയിൻ വിജയവാഡയിലേക്ക് പോകുമോ? | ഈ ട്രെയിൻ വിജയവാഡയിലേക്ക് പോകുമോ? | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TE-03 | Negative | నేను నిన్న ఆ పుస్తకం చదవలేదు. | ഞാൻ ഇന്നലെ ആ പുസ്തകം വായിച്ചില്ല. | ഇന്നലെ ഞാൻ ആ പുസ്തകം വായിച്ചില്ല. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TE-04 | Present tense | ఆమె ప్రతి ఉదయం వార్తలు చదువుతుంది. | അവൾ എല്ലാ രാവിലെയും വാർത്തകൾ വായിക്കുന്നു. | അവൾ എല്ലാ ദിവസവും രാവിലെ വാർത്തകൾ വായിക്കുന്നു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TE-05 | Past tense | రవి గత వారం హైదరాబాద్‌కు వెళ్లాడు. | രവി കഴിഞ്ഞ ആഴ്ച ഹൈദരാബാദിലേക്ക് പോയി. | രവി കഴിഞ്ഞയാഴ്ച ഹൈദരാബാദിലേക്ക് പോയി. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TE-06 | Future tense | మేము రేపు కొత్త కార్యాలయాన్ని ప్రారంభిస్తాము. | ഞങ്ങൾ നാളെ പുതിയ ഓഫീസ് ആരംഭിക്കും. | നാളെ ഞങ്ങൾ ഒരു പുതിയ ഓഫീസ് തുറക്കും. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TE-07 | Future perfect | వచ్చే నెల నాటికి వారు ప్రాజెక్టును పూర్తి చేసి ఉంటారు. | അടുത്ത മാസത്തോടെ അവർ പദ്ധതി പൂർത്തിയാക്കിയിട്ടുണ്ടാകും. | അടുത്ത മാസത്തോടെ അവർ പദ്ധതി പൂർത്തിയാക്കിയിരിക്കാം. | **PARTIAL** | Future-perfect aspect is weakened to an uncertain completed action. |
| TE-08 | Date | పరీక్ష 5 ఆగస్టు 2027న జరుగుతుంది. | പരീക്ഷ 2027 ഓഗസ്റ്റ് 5-ന് നടക്കും. | 2027 ഓഗസ്റ്റ് 5നാണ് പരീക്ഷ നടക്കുന്നത്. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TE-09 | Time | బస్సు సాయంత్రం 4:15కి బయలుదేరుతుంది. | ബസ് വൈകുന്നേരം 4:15-ന് പുറപ്പെടും. | വൈകുന്നേരം \1:15 ന് ബസ് പുറപ്പെടും. | **FAIL** | The departure time is malformed and is not recoverable as 4:15. |
| TE-10 | Number | రైతు 360 కిలోల గోధుమలను విక్రయించాడు. | കർഷകൻ 360 കിലോഗ്രാം ഗോതമ്പ് വിറ്റു. | കർഷകൻ 360 കിലോഗ്രാം ഗോതമ്പ് വിറ്റു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TE-11 | Name | డాక్టర్ సుజాత రెడ్డి నివేదికను పరిశీలించారు. | ഡോക്ടർ സുജാത റെడ్డి റിപ്പോർട്ട് പരിശോധിച്ചു. | ഡോ. സുജാത റെഡ്ഡി റിപ്പോർട്ട് പരിശോധിച്ചു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TE-12 | Place | సమావేశం విశాఖపట్నంలోని విశ్వవిద్యాలయంలో జరుగుతుంది. | സമ്മേളനം വിശാഖപട്ടണത്തിലെ സർവകലാശാലയിൽ നടക്കും. | വിശാഖപട്ടണത്തെ സർവകലാശാലയിലാണ് യോഗം നടക്കുന്നത്. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TE-13 | Pronoun | అతను ఆమెకు తన పత్రాలను చూపించాడు. | അവൻ അവൾക്ക് തന്റെ രേഖകൾ കാണിച്ചു. | അദ്ദേഹം അവൾക്ക് തന്റെ രേഖകൾ കാണിച്ചു തന്നു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TE-14 | Coreference | సీత రమ్యకు తాను పని పూర్తి చేశానని చెప్పింది. | സീത രമ്യയോട് താൻ ജോലി പൂർത്തിയാക്കിയെന്ന് പറഞ്ഞു. | താൻ ജോലി പൂർത്തിയാക്കിയതായി സീത രാമയോട് പറഞ്ഞു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TE-15 | Long sentence | రహదారి మూసివేసినా, డ్రైవర్ ప్రత్యామ్నాయ మార్గం ద్వారా సమయానికి పాఠశాలకు చేరుకున్నాడు. | റോഡ് അടച്ചിരുന്നെങ്കിലും ഡ്രൈവർ മറ്റൊരു വഴിയിലൂടെ സമയത്ത് സ്കൂളിലെത്തി. | റോഡ് അടച്ചിരുന്നുവെങ്കിലും ഡ്രൈവർ ഒരു ബദൽ മാർഗത്തിലൂടെ കൃത്യസമയത്ത് സ്കൂളിൽ എത്തി. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TE-16 | Multiple clauses | విద్యుత్ వస్తే, మేము కంప్యూటర్లను ఆన్ చేసి పాఠాన్ని కొనసాగిస్తాము. | വൈദ്യുതി വന്നാൽ ഞങ്ങൾ കമ്പ്യൂട്ടറുകൾ ഓണാക്കി പാഠം തുടരും. | വൈദ്യുതി വന്നാൽ ഞങ്ങൾ കമ്പ്യൂട്ടറുകൾ ഓണാക്കുകയും പാഠം തുടരുകയും ചെയ്യും. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TE-17 | Technical/academic | ఈ అధ్యయనం గాలి కాలుష్యం మరియు శ్వాసకోశ ఆరోగ్యం మధ్య సంబంధాన్ని పరిశీలిస్తుంది. | ഈ പഠനം വായു മലിനീകരണവും ശ്വസനാരോഗ്യവും തമ്മിലുള്ള ബന്ധം പരിശോധിക്കുന്നു. | വായു മലിനീകരണവും ശ്വസന ആരോഗ്യവും തമ്മിലുള്ള ബന്ധം ഈ പഠനം പരിശോധിക്കുന്നു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TE-18 | AI/computer science | కృత్రిమ మేధస్సు వ్యవస్థ పెద్ద డేటాసెట్‌లో నమూనాలను గుర్తిస్తుంది. | കൃത്രിമ ബുദ്ധി സംവിധാനം വലിയ ഡാറ്റാസെറ്റിലെ മാതൃകകൾ തിരിച്ചറിയുന്നു. | ആർട്ടിഫിഷ്യൽ ഇന്റലിജൻസ് സിസ്റ്റം ഒരു വലിയ ഡാറ്റാസെറ്റിലെ പാറ്റേണുകൾ തിരിച്ചറിയുന്നു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TE-19 | Idiom | అతను సమస్యను చూసి చేతులు ఎత్తలేదు. | പ്രശ്നം കണ്ടപ്പോൾ അവൻ കൈയൊഴിഞ്ഞില്ല. | പ്രശ്നം കണ്ട് അദ്ദേഹം കൈകൾ ഉയർത്തിയില്ല. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| TE-20 | Structure | నివేదికను సమర్పించిన తర్వాత మాత్రమే కమిటీ నిర్ణయం తీసుకుంది. | റിപ്പോർട്ട് സമർപ്പിച്ചതിന് ശേഷമാണ് കമ്മിറ്റി തീരുമാനം എടുത്തത്. | റിപ്പോർട്ട് സമർപ്പിച്ചതിനുശേഷം മാത്രമാണ് സമിതി തീരുമാനം എടുത്തത്. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
### Kannada → Malayalam

| Case | Category | Source | Reference | Actual output | Result | Reviewer note |
|---|---|---|---|---|---|---|
| KA-01 | Everyday conversation | ದಯವಿಟ್ಟು ಬೆಳಕನ್ನು ಆಫ್ ಮಾಡಿ. | ദയവായി ലൈറ്റ് ഓഫ് ചെയ്യൂ. | ദയവായി ലൈറ്റ് ഓഫ് ചെയ്യുക. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| KA-02 | Question | ಈ ಬಸ್ ಮೈಸೂರು ನಗರಕ್ಕೆ ಹೋಗುತ್ತದೆಯೇ? | ഈ ബസ് മൈസൂർ നഗരത്തിലേക്ക് പോകുമോ? | ഈ ബസ് മൈസൂർ നഗരത്തിലേക്ക് പോകുമോ? | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| KA-03 | Negative | ನಾನು ಆ ಸುದ್ದಿಯನ್ನು ನಂಬಲಿಲ್ಲ. | ഞാൻ ആ വാർത്ത വിശ്വസിച്ചില്ല. | ആ വാർത്ത ഞാൻ വിശ്വസിച്ചില്ല. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| KA-04 | Present tense | ಮಕ್ಕಳು ಪ್ರತಿದಿನ ಉದ್ಯಾನವನದಲ್ಲಿ ಆಟವಾಡುತ್ತಾರೆ. | കുട്ടികൾ എല്ലാ ദിവസവും പാർക്കിൽ കളിക്കുന്നു. | കുട്ടികൾ എല്ലാ ദിവസവും പാർക്കിൽ കളിക്കുന്നു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| KA-05 | Past tense | ಶೇಖರ್ ನಿನ್ನೆ ಮಾರುಕಟ್ಟೆಯಿಂದ ಹಣ್ಣುಗಳನ್ನು ತಂದನು. | ശേഖർ ഇന്നലെ മാർക്കറ്റിൽ നിന്ന് പഴങ്ങൾ കൊണ്ടുവന്നു. | ശേഖർ ഇന്നലെ മാർക്കറ്റിൽ നിന്ന് പഴങ്ങൾ കൊണ്ടുവന്നു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| KA-06 | Future tense | ನಾವು ಮುಂದಿನ ವಾರ ತರಬೇತಿ ಶಿಬಿರಕ್ಕೆ ಹೋಗುತ್ತೇವೆ. | ഞങ്ങൾ അടുത്ത ആഴ്ച പരിശീലന ക്യാമ്പിലേക്ക് പോകും. | അടുത്തയാഴ്ച ഞങ്ങൾ പരിശീലന ക്യാമ്പിലേക്ക് പോകും. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| KA-07 | Future perfect | ಡಿಸೆಂಬರ್ ವೇಳೆಗೆ ಸಂಶೋಧಕರು ವರದಿಯನ್ನು ಪೂರ್ಣಗೊಳಿಸಿರುತ್ತಾರೆ. | ഡിസംബറോടെ ഗവേഷകർ റിപ്പോർട്ട് പൂർത്തിയാക്കിയിട്ടുണ്ടാകും. | ഡിസംബറോടെ ഗവേഷകർ റിപ്പോർട്ട് പൂർത്തിയാക്കും. | **PARTIAL** | Future-perfect aspect is reduced to a simple future completion. |
| KA-08 | Date | ಕಾರ್ಯಕ್ರಮವು 21 ಸೆಪ್ಟೆಂಬರ್ 2027ರಂದು ನಡೆಯಲಿದೆ. | പരിപാടി 2027 സെപ്റ്റംബർ 21-ന് നടക്കും. | 2027 സെപ്റ്റംബർ 21നാണ് പരിപാടി നടക്കുന്നത്. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| KA-09 | Time | ರೈಲು ಬೆಳಿಗ್ಗೆ 7:30ಕ್ಕೆ ಹೊರಡುತ್ತದೆ. | ട്രെയിൻ രാവിലെ 7:30-ന് പുറപ്പെടും. | ട്രെയിൻ രാവിലെ \1:30 ന് പുറപ്പെടും. | **FAIL** | The departure time is malformed and is not recoverable as 7:30. |
| KA-10 | Number | ಗ್ರಂಥಾಲಯದಲ್ಲಿ 1,200 ಹೊಸ ಪುಸ್ತಕಗಳಿವೆ. | ലൈബ്രറിയിൽ 1,200 പുതിയ പുസ്തകങ്ങളുണ്ട്. | ലൈബ്രറിയിൽ 1,200 പുതിയ പുസ്തകങ്ങളുണ്ട്. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| KA-11 | Name | ಇಂಜಿನಿಯರ್ ಕವಿತಾ ನಾಯಕ್ ಯೋಜನೆಯನ್ನು ವಿವರಿಸಿದರು. | എഞ്ചിനീയർ കവിത നായക് പദ്ധതി വിശദീകരിച്ചു. | എഞ്ചിനീയർ കവിത നായിക് പദ്ധതി വിശദീകരിച്ചു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| KA-12 | Place | ಸಭೆ ಬೆಂಗಳೂರಿನ ವಿಜ್ಞಾನ ಕೇಂದ್ರದಲ್ಲಿ ನಡೆಯುತ್ತದೆ. | യോഗം ബെംഗളൂരുവിലെ ശാസ്ത്രകേന്ദ്രത്തിൽ നടക്കും. | ബാംഗ്ലൂരിലെ സയൻസ് സെന്ററിലാണ് യോഗം നടക്കുന്നത്. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| KA-13 | Pronoun | ಅವನು ಅವಳಿಗೆ ತನ್ನ ಗುರುತಿನ ಚೀಟಿಯನ್ನು ತೋರಿಸಿದನು. | അവൻ അവൾക്ക് തന്റെ തിരിച്ചറിയൽ കാർഡ് കാണിച്ചു. | അദ്ദേഹം അവൾക്ക് തന്റെ തിരിച്ചറിയൽ കാർഡ് കാണിച്ചു തന്നു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| KA-14 | Coreference | ರಮೇಶ್ ಸುರೇಶ್‌ಗೆ ತಾನು ದಾಖಲೆ ಕಳುಹಿಸಿದ್ದಾಗಿ ತಿಳಿಸಿದನು. | രമേഷ് സുരേഷിനോട് താൻ രേഖ അയച്ചതായി അറിയിച്ചു. | രേഖ അയച്ചതായി രമേഷ് സുരേഷിനോട് പറഞ്ഞു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| KA-15 | Long sentence | ಬಿಸಿಲು ತೀವ್ರವಾಗಿದ್ದರೂ, ಕಾರ್ಮಿಕರು ಸುರಕ್ಷತಾ ನಿಯಮಗಳನ್ನು ಪಾಲಿಸಿ ಕೆಲಸವನ್ನು ಮುಗಿಸಿದರು. | ചൂട് കഠിനമായിരുന്നെങ്കിലും തൊഴിലാളികൾ സുരക്ഷാനിയമങ്ങൾ പാലിച്ച് ജോലി പൂർത്തിയാക്കി. | കടുത്ത ചൂട് ഉണ്ടായിരുന്നിട്ടും, തൊഴിലാളികൾ സുരക്ഷാ നിയമങ്ങൾ പാലിച്ച് ജോലി പൂർത്തിയാക്കി. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| KA-16 | Multiple clauses | ಮಳೆ ನಿಂತ ನಂತರ, ನಾವು ಸೇತುವೆಯನ್ನು ಪರಿಶೀಲಿಸಿ ಸಂಚಾರವನ್ನು ಪುನರಾರಂಭಿಸುತ್ತೇವೆ. | മഴ നിന്നതിന് ശേഷം ഞങ്ങൾ പാലം പരിശോധിച്ച് ഗതാഗതം പുനരാരംഭിക്കും. | മഴ നിർത്തിയ ശേഷം ഞങ്ങൾ പാലം പരിശോധിക്കുകയും ഗതാഗതം പുനരാരംഭിക്കുകയും ചെയ്യും. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| KA-17 | Technical/academic | ಈ ಅಧ್ಯಯನವು ಮಣ್ಣಿನ ತೇವಾಂಶ ಮತ್ತು ಬೆಳೆ ಉತ್ಪಾದನೆಯ ನಡುವಿನ ಸಂಬಂಧವನ್ನು ಅಳೆಯುತ್ತದೆ. | ഈ പഠനം മണ്ണിലെ ഈർപ്പവും വിളവുത്പാദനവും തമ്മിലുള്ള ബന്ധം അളക്കുന്നു. | മണ്ണിന്റെ ഈർപ്പവും വിള ഉൽപാദനവും തമ്മിലുള്ള ബന്ധം ഈ പഠനം അളക്കുന്നു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| KA-18 | AI/computer science | ಕೃತಕ ಬುದ್ಧಿಮತ್ತೆಯ ಮಾದರಿ ತರಬೇತಿ ದತ್ತಾಂಶದಿಂದ ಭಾಷಾ ಮಾದರಿಗಳನ್ನು ಕಲಿಯುತ್ತದೆ. | കൃത്രിമ ബുദ്ധിയുടെ മാതൃക പരിശീലന ഡാറ്റയിൽ നിന്ന് ഭാഷാ മാതൃകകൾ പഠിക്കുന്നു. | ആർട്ടിഫിഷ്യൽ ഇന്റലിജൻസ് മോഡൽ പരിശീലന ഡാറ്റയിൽ നിന്ന് ഭാഷാ മോഡലുകൾ പഠിക്കുന്നു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| KA-19 | Idiom | ಅವಳು ಕಷ್ಟ ಬಂದಾಗ ಕೈಚೆಲ್ಲಲಿಲ್ಲ. | ബുദ്ധിമുട്ട് വന്നപ്പോൾ അവൾ കൈവിട്ടില്ല. | ബുദ്ധിമുട്ടുമ്പോൾ അവൾ കൈവിട്ടില്ല. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| KA-20 | Structure | ವರದಿಯನ್ನು ಪರಿಶೀಲಿಸಿದ ನಂತರವೇ ನಿರ್ದೇಶಕರು ಅನುಮೋದನೆ ನೀಡಿದರು. | റിപ്പോർട്ട് പരിശോധിച്ചതിന് ശേഷമാണ് ഡയറക്ടർ അനുമതി നൽകിയത്. | റിപ്പോർട്ട് പരിശോധിച്ചതിനുശേഷം മാത്രമാണ് ഡയറക്ടർ അംഗീകാരം നൽകിയത്. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
### Hindi → Malayalam

| Case | Category | Source | Reference | Actual output | Result | Reviewer note |
|---|---|---|---|---|---|---|
| HI-01 | Everyday conversation | कृपया मेज पर रखी किताब मुझे दें। | ദയവായി മേശപ്പുറത്തുള്ള പുസ്തകം എനിക്ക് തരൂ. | ദയവായി മേശപ്പുറത്ത് വെച്ചിരിക്കുന്ന പുസ്തകം എനിക്ക് നൽകുക. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| HI-02 | Question | यह सड़क हवाई अड्डे तक जाती है क्या? | ഈ റോഡ് വിമാനത്താവളം വരെ പോകുമോ? | ഈ റോഡ് വിമാനത്താവളത്തിലേക്ക് പോകുന്നുണ്ടോ? | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| HI-03 | Negative | मैंने आज नाश्ता नहीं किया। | ഞാൻ ഇന്ന് പ്രഭാതഭക്ഷണം കഴിച്ചില്ല. | ഇന്ന് ഞാൻ പ്രഭാതഭക്ഷണം കഴിച്ചില്ല. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| HI-04 | Present tense | किसान हर सुबह खेत में काम करता है। | കർഷകൻ എല്ലാ രാവിലെയും വയലിൽ ജോലി ചെയ്യുന്നു. | കർഷകൻ എല്ലാ ദിവസവും രാവിലെ വയലിൽ ജോലി ചെയ്യുന്നു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| HI-05 | Past tense | सीमा ने पिछले महीने नई नौकरी शुरू की। | സീമ കഴിഞ്ഞ മാസം പുതിയ ജോലി ആരംഭിച്ചു. | കഴിഞ്ഞ മാസം സീമ പുതിയ ജോലി ആരംഭിച്ചു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| HI-06 | Future tense | हम अगले रविवार संग्रहालय जाएंगे। | ഞങ്ങൾ അടുത്ത ഞായറാഴ്ച മ്യൂസിയത്തിലേക്ക് പോകും. | അടുത്ത ഞായറാഴ്ച ഞങ്ങൾ മ്യൂസിയത്തിലേക്ക് പോകും. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| HI-07 | Future perfect | शाम तक डॉक्टर मरीज की जांच पूरी कर चुके होंगे। | വൈകുന്നേരത്തോടെ ഡോക്ടർ രോഗിയുടെ പരിശോധന പൂർത്തിയാക്കിയിട്ടുണ്ടാകും. | വൈകുന്നേരത്തോടെ ഡോക്ടർ രോഗിയുടെ പരിശോധന പൂർത്തിയാക്കിയിരിക്കാം. | **PARTIAL** | Future-perfect aspect is weakened to an uncertain completed action. |
| HI-08 | Date | परिणाम 30 नवंबर 2027 को घोषित किए जाएंगे। | ഫലം 2027 നവംബർ 30-ന് പ്രഖ്യാപിക്കും. | 2027 നവംബർ 30ന് ഫലം പ്രഖ്യാപിക്കും. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| HI-09 | Time | कार्यालय सुबह 8:40 बजे खुलता है। | ഓഫീസ് രാവിലെ 8:40-ന് തുറക്കും. | രാവിലെ \1:40 ന് ഓഫീസ് തുറക്കുന്നു. | **FAIL** | The opening time is malformed and is not recoverable as 8:40. |
| HI-10 | Number | कंपनी ने 725 कंप्यूटर खरीदे। | കമ്പനി 725 കമ്പ്യൂട്ടറുകൾ വാങ്ങി. | കമ്പനി 725 കമ്പ്യൂട്ടറുകൾ വാങ്ങി. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| HI-11 | Name | प्रोफेसर नीलम शर्मा ने व्याख्यान दिया। | പ്രൊഫസർ നീലം ശർമ്മ പ്രഭാഷണം നടത്തി. | പ്രൊഫസർ നീലം ശർമ്മ പ്രഭാഷണം നടത്തി. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| HI-12 | Place | प्रतियोगिता जयपुर के खेल मैदान में होगी। | മത്സരം ജയ്പൂരിലെ കായികമൈതാനത്ത് നടക്കും. | ജയ്പൂരിലെ സ്പോർട്സ് ഗ്രൌണ്ടിലായിരിക്കും മത്സരം നടക്കുക. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| HI-13 | Pronoun | उसने उसे अपनी फाइल भेजी। | അവൻ അവന് തന്റെ ഫയൽ അയച്ചു. | അവൾ തന്റെ ഫയൽ അവൾക്ക് അയച്ചു. | **PARTIAL** | The pronoun roles are not fully resolved; the action is understandable but the antecedents are unclear. |
| HI-14 | Coreference | मोहन ने रोहित से कहा कि उसने आवेदन जमा कर दिया है। | മോഹൻ രോഹിതിനോട് താൻ അപേക്ഷ സമർപ്പിച്ചെന്ന് പറഞ്ഞു. | താൻ അപേക്ഷ സമർപ്പിച്ചിട്ടുണ്ടെന്ന് മോഹൻ രോഹിത്തിനോട് പറഞ്ഞു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| HI-15 | Long sentence | तेज बारिश के बावजूद, बचाव दल ने पुल के पास फंसे यात्रियों को सुरक्षित बाहर निकाला। | കനത്ത മഴയുണ്ടായിരുന്നിട്ടും രക്ഷാസംഘം പാലത്തിന് സമീപം കുടുങ്ങിയ യാത്രക്കാരെ സുരക്ഷിതമായി പുറത്തെടുത്തു. | കനത്ത മഴ ഉണ്ടായിരുന്നിട്ടും പാലത്തിന് സമീപം കുടുങ്ങിയ യാത്രക്കാരെ രക്ഷാപ്രവർത്തകർ സുരക്ഷിതമായി ഒഴിപ്പിച്ചു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| HI-16 | Multiple clauses | यदि बस समय पर आती है, तो हम बाजार जाएंगे और लौटते समय दवा खरीदेंगे। | ബസ് സമയത്ത് വന്നാൽ ഞങ്ങൾ മാർക്കറ്റിൽ പോയി മടങ്ങുമ്പോൾ മരുന്ന് വാങ്ങും. | സമയബന്ധിതമായി വന്നാൽ ഞങ്ങൾ മാർക്കറ്റിലേക്ക് പോകുകയും മടങ്ങുമ്പോൾ മരുന്ന് വാങ്ങുകയും ചെയ്യും. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| HI-17 | Technical/academic | यह शोध मिट्टी के तापमान और बीज के अंकुरण के बीच संबंध का अध्ययन करता है। | ഈ ഗവേഷണം മണ്ണിന്റെ താപനിലയും വിത്തിന്റെ മുളപ്പും തമ്മിലുള്ള ബന്ധം പഠിക്കുന്നു. | മണ്ണിന്റെ താപനിലയും വിത്ത് മുളപ്പിക്കലും തമ്മിലുള്ള ബന്ധം ഈ ഗവേഷണം പഠിക്കുന്നു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| HI-18 | AI/computer science | कंप्यूटर दृष्टि प्रणाली तस्वीर में वस्तुओं की पहचान करती है। | കമ്പ്യൂട്ടർ വിഷൻ സംവിധാനം ചിത്രത്തിലെ വസ്തുക്കളെ തിരിച്ചറിയുന്നു. | ഒരു കമ്പ്യൂട്ടർ വിഷൻ സിസ്റ്റം ചിത്രത്തിൽ ഉള്ള വസ്തുക്കൾ തിരിച്ചറിയുന്നു. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| HI-19 | Idiom | उसने कठिन समय में भी हिम्मत नहीं हारी। | പ്രയാസകാലത്തും അവൻ ധൈര്യം കൈവിട്ടില്ല. | കഠിനമായ സമയങ്ങളിൽ പോലും അവൾക്ക് ധൈര്യം നഷ്ടമായില്ല. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |
| HI-20 | Structure | रिपोर्ट पढ़ने के बाद ही समिति ने अंतिम निर्णय लिया। | റിപ്പോർട്ട് വായിച്ചതിന് ശേഷമാണ് കമ്മിറ്റി അന്തിമ തീരുമാനം എടുത്തത്. | റിപ്പോർട്ട് വായിച്ചതിനുശേഷം മാത്രമാണ് സമിതി അന്തിമ തീരുമാനം എടുത്തത്. | **PASS** | Meaning and key details are preserved; wording differs stylistically from the reference but remains semantically equivalent. |

## Observations

- All 100 requests returned successfully; no API or transport failures occurred.
- The most frequent issue was loss or corruption of clock times in the four affected time cases.
- Future-perfect meaning was commonly weakened to simple or uncertain completion.
- One English negation was reversed, producing a FAIL.
- Pronoun/coreference handling produced isolated PARTIAL cases.
- These results are a baseline for investigation only; no translation fixes were made.

## Reproducibility command

```powershell
cd 11_Testing_Plan
..\translation-service\.venv\Scripts\python.exe run_phase1_quality_benchmark.py
```
