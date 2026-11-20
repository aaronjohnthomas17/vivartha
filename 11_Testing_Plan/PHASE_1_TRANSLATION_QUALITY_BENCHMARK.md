# VIVARTHA Phase 1 Internal Translation-Quality Benchmark

## Purpose and scope

This is a fixed, internal quality benchmark for the Phase 1 Core Text Translation MVP. It evaluates IndicTrans2 output from five source languages into Malayalam; it is not a formal accuracy percentage, certification, or human-evaluation study.

The same source sentences and reference translations must be retained for before/after comparisons. Do not tune the model against this set and do not change the selected IndicTrans2 checkpoint as part of this benchmark.

Target language: Malayalam (`mal_Mlym`)

Source languages: English (`eng_Latn`), Tamil (`tam_Taml`), Telugu (`tel_Telu`), Kannada (`kan_Knda`), and Hindi (`hin_Deva`). Malayalam-to-Malayalam is covered by the service smoke tests, but is outside this five-language quality benchmark.

## Evaluation procedure

1. Run every case through the same service version, model checkpoint, decoding settings, and preprocessing.
2. Record the raw output exactly as returned.
3. Compare meaning, not spelling or punctuation alone, with the reference translation.
4. Have two reviewers independently label each case where practical; resolve disagreements with a short note.
5. Preserve the benchmark version and model/runtime metadata with every result.

### Labels

- **PASS** — Meaning, polarity, tense/aspect, entities, numbers, and relationships are preserved. Minor harmless punctuation or stylistic variation is acceptable.
- **PARTIAL** — The main meaning is recoverable, but there is a material omission, awkward terminology, tense/detail error, or ambiguity that does not completely invalidate the sentence.
- **FAIL** — Meaning is wrong, important content is omitted or invented, polarity/tense is reversed, an entity or number is materially corrupted, or the output is unusable.

Do not calculate a percentage accuracy claim from this small set. Summaries may report counts of PASS/PARTIAL/FAIL by language and category, with reviewer notes.

## Fixed benchmark cases

Each row is `ID | Category | Source sentence | Reference Malayalam translation`.

### English → Malayalam

| ID | Category | Source sentence | Reference Malayalam translation |
|---|---|---|---|
| EN-01 | Everyday conversation | Please close the window before you leave. | നിങ്ങൾ പോകുന്നതിന് മുമ്പ് ജനൽ അടയ്ക്കുക. |
| EN-02 | Question | Which bus goes to the railway station? | റെയിൽവേ സ്റ്റേഷനിലേക്ക് പോകുന്ന ബസ് ഏതാണ്? |
| EN-03 | Negative | I did not forget your message. | ഞാൻ നിങ്ങളുടെ സന്ദേശം മറന്നിട്ടില്ല. |
| EN-04 | Present tense | The children study in the library every evening. | കുട്ടികൾ എല്ലാ വൈകുന്നേരവും ലൈബ്രറിയിൽ പഠിക്കുന്നു. |
| EN-05 | Past tense | Anil bought a new notebook yesterday. | അനിൽ ഇന്നലെ ഒരു പുതിയ നോട്ട്‌ബുക്ക് വാങ്ങി. |
| EN-06 | Future tense | The meeting will start at nine tomorrow. | യോഗം നാളെ ഒമ്പത് മണിക്ക് ആരംഭിക്കും. |
| EN-07 | Future perfect | By Friday, the engineers will have completed the bridge inspection. | വെള്ളിയാഴ്ചയ്ക്കുള്ളിൽ എഞ്ചിനീയർമാർ പാലത്തിന്റെ പരിശോധന പൂർത്തിയാക്കിയിട്ടുണ്ടാകും. |
| EN-08 | Date | The final examination is scheduled for 18 March 2027. | അന്തിമ പരീക്ഷ 2027 മാർച്ച് 18-ന് നിശ്ചയിച്ചിരിക്കുന്നു. |
| EN-09 | Time | The train leaves at 6:45 in the morning. | ട്രെയിൻ രാവിലെ 6:45-ന് പുറപ്പെടും. |
| EN-10 | Number | The warehouse received 2,450 kilograms of rice. | ഗോഡൗണിൽ 2,450 കിലോഗ്രാം അരി ലഭിച്ചു. |
| EN-11 | Name | Dr. Meera Thomas signed the report. | ഡോ. മീര തോമസ് റിപ്പോർട്ടിൽ ഒപ്പുവച്ചു. |
| EN-12 | Place | The conference will be held in Kochi, Kerala. | സമ്മേളനം കേരളത്തിലെ കൊച്ചിയിൽ നടക്കും. |
| EN-13 | Pronoun | They gave her the keys after she showed them her identity card. | അവൾ തന്റെ തിരിച്ചറിയൽ കാർഡ് അവരെ കാണിച്ചതിന് ശേഷം അവർ അവൾക്ക് താക്കോലുകൾ നൽകി. |
| EN-14 | Coreference | Riya told Maya that she had finished the assignment. | റിയ മായയോട് താൻ അസൈൻമെന്റ് പൂർത്തിയാക്കിയെന്ന് പറഞ്ഞു. |
| EN-15 | Long sentence | Although the road was crowded, the ambulance reached the hospital quickly because the drivers made room for it. | റോഡ് തിരക്കേറിയിരുന്നെങ്കിലും ഡ്രൈവർമാർ വഴിയൊരുക്കിയതിനാൽ ആംബുലൻസ് ആശുപത്രിയിലെത്തിയത് വേഗത്തിലായിരുന്നു. |
| EN-16 | Multiple clauses | When the rain stops, we will inspect the fields and decide whether the farmers can plant the seeds this week. | മഴ നിൽക്കുമ്പോൾ ഞങ്ങൾ വയലുകൾ പരിശോധിച്ച് ഈ ആഴ്ച കർഷകർക്ക് വിത്ത് നടാനാകുമോ എന്ന് തീരുമാനിക്കും. |
| EN-17 | Technical/academic | The experiment measured the relationship between temperature and battery efficiency. | പരീക്ഷണം താപനിലയും ബാറ്ററിയുടെ കാര്യക്ഷമതയും തമ്മിലുള്ള ബന്ധം അളന്നു. |
| EN-18 | AI/computer science | The neural network classifies images after training on labeled data. | ലേബൽ ചെയ്ത ഡാറ്റയിൽ പരിശീലനം നേടിയ ശേഷം ന്യൂറൽ നെറ്റ്‌വർക്ക് ചിത്രങ്ങളെ വർഗീകരിക്കുന്നു. |
| EN-19 | Idiom | She kept an eye on the equipment during the demonstration. | പ്രദർശനത്തിനിടെ അവൾ ഉപകരണങ്ങളിൽ ശ്രദ്ധവെച്ചു. |
| EN-20 | Structure | Not only did the team solve the problem, but it also documented the solution. | സംഘം പ്രശ്നം പരിഹരിച്ചതുമാത്രമല്ല, പരിഹാരവും രേഖപ്പെടുത്തി. |

### Tamil → Malayalam

| ID | Category | Source sentence | Reference Malayalam translation |
|---|---|---|---|
| TA-01 | Everyday conversation | தயவுசெய்து கதவை மூடுங்கள். | ദയവായി വാതിൽ അടയ്ക്കൂ. |
| TA-02 | Question | இந்த பேருந்து மருத்துவமனைக்கு செல்கிறதா? | ഈ ബസ് ആശുപത്രിയിലേക്ക് പോകുമോ? |
| TA-03 | Negative | நான் இன்று அலுவலகத்திற்கு செல்லவில்லை. | ഞാൻ ഇന്ന് ഓഫീസിലേക്ക് പോയില്ല. |
| TA-04 | Present tense | மாணவர்கள் தினமும் தமிழ் பாடத்தைப் படிக்கிறார்கள். | വിദ്യാർത്ഥികൾ ദിവസവും തമിഴ് പാഠം പഠിക്കുന്നു. |
| TA-05 | Past tense | லதா நேற்று சென்னைக்கு சென்றார். | ലത ഇന്നലെ ചെന്നൈയിലേക്ക് പോയി. |
| TA-06 | Future tense | அவர்கள் அடுத்த வாரம் புதிய திட்டத்தை தொடங்குவார்கள். | അവർ അടുത്ത ആഴ്ച പുതിയ പദ്ധതി ആരംഭിക്കും. |
| TA-07 | Future perfect | அடுத்த மாதத்திற்குள் குழு அறிக்கையை முடித்திருக்கும். | അടുത്ത മാസത്തിനുള്ളിൽ സംഘം റിപ്പോർട്ട് പൂർത്തിയാക്കിയിട്ടുണ്ടാകും. |
| TA-08 | Date | கூட்டம் 12 ஜூலை 2027 அன்று நடைபெறும். | യോഗം 2027 ജൂലൈ 12-ന് നടക്കും. |
| TA-09 | Time | விமானம் இரவு 10:20 மணிக்கு புறப்படும். | വിമാനം രാത്രി 10:20-ന് പുറപ്പെടും. |
| TA-10 | Number | கடையில் 875 புத்தகங்கள் உள்ளன. | കടയിൽ 875 പുസ്തകങ്ങളുണ്ട്. |
| TA-11 | Name | பேராசிரியர் அருண் குமார் மாணவர்களை வரவேற்றார். | പ്രൊഫസർ അരുൺ കുമാർ വിദ്യാർത്ഥികളെ സ്വാഗതം ചെയ്തു. |
| TA-12 | Place | நிகழ்ச்சி மதுரையில் உள்ள நகர மண்டபத்தில் நடக்கும். | പരിപാടി മധുരയിലെ നഗര ഹാളിൽ നടക്കും. |
| TA-13 | Pronoun | அவள் அவரிடம் தனது ஆவணத்தை கொடுத்தாள். | അവൾ അവന് തന്റെ രേഖ നൽകി. |
| TA-14 | Coreference | குமார் ரவியிடம் தான் திட்டத்தை முடித்ததாக கூறினார். | കുമാർ രവിയോട് താൻ പദ്ധതി പൂർത്തിയാക്കിയെന്ന് പറഞ്ഞു. |
| TA-15 | Long sentence | மின்சாரம் தடைப்பட்டபோதும், செவிலியர்கள் நோயாளிகளைக் கவனித்து சிகிச்சையைத் தொடர்ந்தனர். | വൈദ്യുതി മുടങ്ങിയിട്ടും നഴ്സുമാർ രോഗികളെ പരിചരിച്ച് ചികിത്സ തുടർന്നു. |
| TA-16 | Multiple clauses | மழை பெய்தால், பள்ளி நிர்வாகம் விளையாட்டு போட்டியை வெள்ளிக்கிழமைக்கு மாற்றும். | മഴ പെയ്താൽ സ്കൂൾ ഭരണകൂടം കായികമത്സരം വെള്ളിയാഴ്ചയിലേക്ക് മാറ്റും. |
| TA-17 | Technical/academic | இந்த ஆய்வு நீரின் தரம் மற்றும் மண் வளம் இடையிலான தொடர்பை விளக்குகிறது. | ഈ പഠനം ജലത്തിന്റെ ഗുണനിലവാരവും മണ്ണിന്റെ ഫലഭൂയിഷ്ഠതയും തമ്മിലുള്ള ബന്ധം വിശദീകരിക്കുന്നു. |
| TA-18 | AI/computer science | இயந்திரக் கற்றல் மாதிரி புதிய தரவிலிருந்து வடிவங்களை கண்டறிகிறது. | മെഷീൻ ലേണിംഗ് മാതൃക പുതിയ ഡാറ്റയിൽ നിന്ന് മാതൃകകൾ കണ്ടെത്തുന്നു. |
| TA-19 | Idiom | அவன் செய்தியை கேட்டதும் கைகளை கட்டிக்கொண்டு உட்காரவில்லை. | വാർത്ത കേട്ട ശേഷം അവൻ കൈകെട്ടി ഇരുന്നില്ല. |
| TA-20 | Structure | வேலை முடிந்த பிறகு மட்டுமே அவர்கள் வீட்டிற்கு திரும்பினர். | ജോലി പൂർത്തിയായതിന് ശേഷമാണ് അവർ വീട്ടിലേക്ക് മടങ്ങിയത്. |

### Telugu → Malayalam

| ID | Category | Source sentence | Reference Malayalam translation |
|---|---|---|---|
| TE-01 | Everyday conversation | దయచేసి నాకు ఒక గ్లాసు నీరు ఇవ్వండి. | ദയവായി എനിക്ക് ഒരു ഗ്ലാസ് വെള്ളം തരൂ. |
| TE-02 | Question | ఈ రైలు విజయవాడకు వెళ్తుందా? | ഈ ട്രെയിൻ വിജയവാഡയിലേക്ക് പോകുമോ? |
| TE-03 | Negative | నేను నిన్న ఆ పుస్తకం చదవలేదు. | ഞാൻ ഇന്നലെ ആ പുസ്തകം വായിച്ചില്ല. |
| TE-04 | Present tense | ఆమె ప్రతి ఉదయం వార్తలు చదువుతుంది. | അവൾ എല്ലാ രാവിലെയും വാർത്തകൾ വായിക്കുന്നു. |
| TE-05 | Past tense | రవి గత వారం హైదరాబాద్‌కు వెళ్లాడు. | രവി കഴിഞ്ഞ ആഴ്ച ഹൈദരാബാദിലേക്ക് പോയി. |
| TE-06 | Future tense | మేము రేపు కొత్త కార్యాలయాన్ని ప్రారంభిస్తాము. | ഞങ്ങൾ നാളെ പുതിയ ഓഫീസ് ആരംഭിക്കും. |
| TE-07 | Future perfect | వచ్చే నెల నాటికి వారు ప్రాజెక్టును పూర్తి చేసి ఉంటారు. | അടുത്ത മാസത്തോടെ അവർ പദ്ധതി പൂർത്തിയാക്കിയിട്ടുണ്ടാകും. |
| TE-08 | Date | పరీక్ష 5 ఆగస్టు 2027న జరుగుతుంది. | പരീക്ഷ 2027 ഓഗസ്റ്റ് 5-ന് നടക്കും. |
| TE-09 | Time | బస్సు సాయంత్రం 4:15కి బయలుదేరుతుంది. | ബസ് വൈകുന്നേരം 4:15-ന് പുറപ്പെടും. |
| TE-10 | Number | రైతు 360 కిలోల గోధుమలను విక్రయించాడు. | കർഷകൻ 360 കിലോഗ്രാം ഗോതമ്പ് വിറ്റു. |
| TE-11 | Name | డాక్టర్ సుజాత రెడ్డి నివేదికను పరిశీలించారు. | ഡോക്ടർ സുജാത റെడ్డి റിപ്പോർട്ട് പരിശോധിച്ചു. |
| TE-12 | Place | సమావేశం విశాఖపట్నంలోని విశ్వవిద్యాలయంలో జరుగుతుంది. | സമ്മേളനം വിശാഖപട്ടണത്തിലെ സർവകലാശാലയിൽ നടക്കും. |
| TE-13 | Pronoun | అతను ఆమెకు తన పత్రాలను చూపించాడు. | അവൻ അവൾക്ക് തന്റെ രേഖകൾ കാണിച്ചു. |
| TE-14 | Coreference | సీత రమ్యకు తాను పని పూర్తి చేశానని చెప్పింది. | സീത രമ്യയോട് താൻ ജോലി പൂർത്തിയാക്കിയെന്ന് പറഞ്ഞു. |
| TE-15 | Long sentence | రహదారి మూసివేసినా, డ్రైవర్ ప్రత్యామ్నాయ మార్గం ద్వారా సమయానికి పాఠశాలకు చేరుకున్నాడు. | റോഡ് അടച്ചിരുന്നെങ്കിലും ഡ്രൈവർ മറ്റൊരു വഴിയിലൂടെ സമയത്ത് സ്കൂളിലെത്തി. |
| TE-16 | Multiple clauses | విద్యుత్ వస్తే, మేము కంప్యూటర్లను ఆన్ చేసి పాఠాన్ని కొనసాగిస్తాము. | വൈദ്യുതി വന്നാൽ ഞങ്ങൾ കമ്പ്യൂട്ടറുകൾ ഓണാക്കി പാഠം തുടരും. |
| TE-17 | Technical/academic | ఈ అధ్యయనం గాలి కాలుష్యం మరియు శ్వాసకోశ ఆరోగ్యం మధ్య సంబంధాన్ని పరిశీలిస్తుంది. | ഈ പഠനം വായു മലിനീകരണവും ശ്വസനാരോഗ്യവും തമ്മിലുള്ള ബന്ധം പരിശോധിക്കുന്നു. |
| TE-18 | AI/computer science | కృత్రిమ మేధస్సు వ్యవస్థ పెద్ద డేటాసెట్‌లో నమూనాలను గుర్తిస్తుంది. | കൃത്രിമ ബുദ്ധി സംവിധാനം വലിയ ഡാറ്റാസെറ്റിലെ മാതൃകകൾ തിരിച്ചറിയുന്നു. |
| TE-19 | Idiom | అతను సమస్యను చూసి చేతులు ఎత్తలేదు. | പ്രശ്നം കണ്ടപ്പോൾ അവൻ കൈയൊഴിഞ്ഞില്ല. |
| TE-20 | Structure | నివేదికను సమర్పించిన తర్వాత మాత్రమే కమిటీ నిర్ణయం తీసుకుంది. | റിപ്പോർട്ട് സമർപ്പിച്ചതിന് ശേഷമാണ് കമ്മിറ്റി തീരുമാനം എടുത്തത്. |

### Kannada → Malayalam

| ID | Category | Source sentence | Reference Malayalam translation |
|---|---|---|---|
| KA-01 | Everyday conversation | ದಯವಿಟ್ಟು ಬೆಳಕನ್ನು ಆಫ್ ಮಾಡಿ. | ദയവായി ലൈറ്റ് ഓഫ് ചെയ്യൂ. |
| KA-02 | Question | ಈ ಬಸ್ ಮೈಸೂರು ನಗರಕ್ಕೆ ಹೋಗುತ್ತದೆಯೇ? | ഈ ബസ് മൈസൂർ നഗരത്തിലേക്ക് പോകുമോ? |
| KA-03 | Negative | ನಾನು ಆ ಸುದ್ದಿಯನ್ನು ನಂಬಲಿಲ್ಲ. | ഞാൻ ആ വാർത്ത വിശ്വസിച്ചില്ല. |
| KA-04 | Present tense | ಮಕ್ಕಳು ಪ್ರತಿದಿನ ಉದ್ಯಾನವನದಲ್ಲಿ ಆಟವಾಡುತ್ತಾರೆ. | കുട്ടികൾ എല്ലാ ദിവസവും പാർക്കിൽ കളിക്കുന്നു. |
| KA-05 | Past tense | ಶೇಖರ್ ನಿನ್ನೆ ಮಾರುಕಟ್ಟೆಯಿಂದ ಹಣ್ಣುಗಳನ್ನು ತಂದನು. | ശേഖർ ഇന്നലെ മാർക്കറ്റിൽ നിന്ന് പഴങ്ങൾ കൊണ്ടുവന്നു. |
| KA-06 | Future tense | ನಾವು ಮುಂದಿನ ವಾರ ತರಬೇತಿ ಶಿಬಿರಕ್ಕೆ ಹೋಗುತ್ತೇವೆ. | ഞങ്ങൾ അടുത്ത ആഴ്ച പരിശീലന ക്യാമ്പിലേക്ക് പോകും. |
| KA-07 | Future perfect | ಡಿಸೆಂಬರ್ ವೇಳೆಗೆ ಸಂಶೋಧಕರು ವರದಿಯನ್ನು ಪೂರ್ಣಗೊಳಿಸಿರುತ್ತಾರೆ. | ഡിസംബറോടെ ഗവേഷകർ റിപ്പോർട്ട് പൂർത്തിയാക്കിയിട്ടുണ്ടാകും. |
| KA-08 | Date | ಕಾರ್ಯಕ್ರಮವು 21 ಸೆಪ್ಟೆಂಬರ್ 2027ರಂದು ನಡೆಯಲಿದೆ. | പരിപാടി 2027 സെപ്റ്റംബർ 21-ന് നടക്കും. |
| KA-09 | Time | ರೈಲು ಬೆಳಿಗ್ಗೆ 7:30ಕ್ಕೆ ಹೊರಡುತ್ತದೆ. | ട്രെയിൻ രാവിലെ 7:30-ന് പുറപ്പെടും. |
| KA-10 | Number | ಗ್ರಂಥಾಲಯದಲ್ಲಿ 1,200 ಹೊಸ ಪುಸ್ತಕಗಳಿವೆ. | ലൈബ്രറിയിൽ 1,200 പുതിയ പുസ്തകങ്ങളുണ്ട്. |
| KA-11 | Name | ಇಂಜಿನಿಯರ್ ಕವಿತಾ ನಾಯಕ್ ಯೋಜನೆಯನ್ನು ವಿವರಿಸಿದರು. | എഞ്ചിനീയർ കവിത നായക് പദ്ധതി വിശദീകരിച്ചു. |
| KA-12 | Place | ಸಭೆ ಬೆಂಗಳೂರಿನ ವಿಜ್ಞಾನ ಕೇಂದ್ರದಲ್ಲಿ ನಡೆಯುತ್ತದೆ. | യോഗം ബെംഗളൂരുവിലെ ശാസ്ത്രകേന്ദ്രത്തിൽ നടക്കും. |
| KA-13 | Pronoun | ಅವನು ಅವಳಿಗೆ ತನ್ನ ಗುರುತಿನ ಚೀಟಿಯನ್ನು ತೋರಿಸಿದನು. | അവൻ അവൾക്ക് തന്റെ തിരിച്ചറിയൽ കാർഡ് കാണിച്ചു. |
| KA-14 | Coreference | ರಮೇಶ್ ಸುರೇಶ್‌ಗೆ ತಾನು ದಾಖಲೆ ಕಳುಹಿಸಿದ್ದಾಗಿ ತಿಳಿಸಿದನು. | രമേഷ് സുരേഷിനോട് താൻ രേഖ അയച്ചതായി അറിയിച്ചു. |
| KA-15 | Long sentence | ಬಿಸಿಲು ತೀವ್ರವಾಗಿದ್ದರೂ, ಕಾರ್ಮಿಕರು ಸುರಕ್ಷತಾ ನಿಯಮಗಳನ್ನು ಪಾಲಿಸಿ ಕೆಲಸವನ್ನು ಮುಗಿಸಿದರು. | ചൂട് കഠിനമായിരുന്നെങ്കിലും തൊഴിലാളികൾ സുരക്ഷാനിയമങ്ങൾ പാലിച്ച് ജോലി പൂർത്തിയാക്കി. |
| KA-16 | Multiple clauses | ಮಳೆ ನಿಂತ ನಂತರ, ನಾವು ಸೇತುವೆಯನ್ನು ಪರಿಶೀಲಿಸಿ ಸಂಚಾರವನ್ನು ಪುನರಾರಂಭಿಸುತ್ತೇವೆ. | മഴ നിന്നതിന് ശേഷം ഞങ്ങൾ പാലം പരിശോധിച്ച് ഗതാഗതം പുനരാരംഭിക്കും. |
| KA-17 | Technical/academic | ಈ ಅಧ್ಯಯನವು ಮಣ್ಣಿನ ತೇವಾಂಶ ಮತ್ತು ಬೆಳೆ ಉತ್ಪಾದನೆಯ ನಡುವಿನ ಸಂಬಂಧವನ್ನು ಅಳೆಯುತ್ತದೆ. | ഈ പഠനം മണ്ണിലെ ഈർപ്പവും വിളവുത്പാദനവും തമ്മിലുള്ള ബന്ധം അളക്കുന്നു. |
| KA-18 | AI/computer science | ಕೃತಕ ಬುದ್ಧಿಮತ್ತೆಯ ಮಾದರಿ ತರಬೇತಿ ದತ್ತಾಂಶದಿಂದ ಭಾಷಾ ಮಾದರಿಗಳನ್ನು ಕಲಿಯುತ್ತದೆ. | കൃത്രിമ ബുദ്ധിയുടെ മാതൃക പരിശീലന ഡാറ്റയിൽ നിന്ന് ഭാഷാ മാതൃകകൾ പഠിക്കുന്നു. |
| KA-19 | Idiom | ಅವಳು ಕಷ್ಟ ಬಂದಾಗ ಕೈಚೆಲ್ಲಲಿಲ್ಲ. | ബുദ്ധിമുട്ട് വന്നപ്പോൾ അവൾ കൈവിട്ടില്ല. |
| KA-20 | Structure | ವರದಿಯನ್ನು ಪರಿಶೀಲಿಸಿದ ನಂತರವೇ ನಿರ್ದೇಶಕರು ಅನುಮೋದನೆ ನೀಡಿದರು. | റിപ്പോർട്ട് പരിശോധിച്ചതിന് ശേഷമാണ് ഡയറക്ടർ അനുമതി നൽകിയത്. |

### Hindi → Malayalam

| ID | Category | Source sentence | Reference Malayalam translation |
|---|---|---|---|
| HI-01 | Everyday conversation | कृपया मेज पर रखी किताब मुझे दें। | ദയവായി മേശപ്പുറത്തുള്ള പുസ്തകം എനിക്ക് തരൂ. |
| HI-02 | Question | यह सड़क हवाई अड्डे तक जाती है क्या? | ഈ റോഡ് വിമാനത്താവളം വരെ പോകുമോ? |
| HI-03 | Negative | मैंने आज नाश्ता नहीं किया। | ഞാൻ ഇന്ന് പ്രഭാതഭക്ഷണം കഴിച്ചില്ല. |
| HI-04 | Present tense | किसान हर सुबह खेत में काम करता है। | കർഷകൻ എല്ലാ രാവിലെയും വയലിൽ ജോലി ചെയ്യുന്നു. |
| HI-05 | Past tense | सीमा ने पिछले महीने नई नौकरी शुरू की। | സീമ കഴിഞ്ഞ മാസം പുതിയ ജോലി ആരംഭിച്ചു. |
| HI-06 | Future tense | हम अगले रविवार संग्रहालय जाएंगे। | ഞങ്ങൾ അടുത്ത ഞായറാഴ്ച മ്യൂസിയത്തിലേക്ക് പോകും. |
| HI-07 | Future perfect | शाम तक डॉक्टर मरीज की जांच पूरी कर चुके होंगे। | വൈകുന്നേരത്തോടെ ഡോക്ടർ രോഗിയുടെ പരിശോധന പൂർത്തിയാക്കിയിട്ടുണ്ടാകും. |
| HI-08 | Date | परिणाम 30 नवंबर 2027 को घोषित किए जाएंगे। | ഫലം 2027 നവംബർ 30-ന് പ്രഖ്യാപിക്കും. |
| HI-09 | Time | कार्यालय सुबह 8:40 बजे खुलता है। | ഓഫീസ് രാവിലെ 8:40-ന് തുറക്കും. |
| HI-10 | Number | कंपनी ने 725 कंप्यूटर खरीदे। | കമ്പനി 725 കമ്പ്യൂട്ടറുകൾ വാങ്ങി. |
| HI-11 | Name | प्रोफेसर नीलम शर्मा ने व्याख्यान दिया। | പ്രൊഫസർ നീലം ശർമ്മ പ്രഭാഷണം നടത്തി. |
| HI-12 | Place | प्रतियोगिता जयपुर के खेल मैदान में होगी। | മത്സരം ജയ്പൂരിലെ കായികമൈതാനത്ത് നടക്കും. |
| HI-13 | Pronoun | उसने उसे अपनी फाइल भेजी। | അവൻ അവന് തന്റെ ഫയൽ അയച്ചു. |
| HI-14 | Coreference | मोहन ने रोहित से कहा कि उसने आवेदन जमा कर दिया है। | മോഹൻ രോഹിതിനോട് താൻ അപേക്ഷ സമർപ്പിച്ചെന്ന് പറഞ്ഞു. |
| HI-15 | Long sentence | तेज बारिश के बावजूद, बचाव दल ने पुल के पास फंसे यात्रियों को सुरक्षित बाहर निकाला। | കനത്ത മഴയുണ്ടായിരുന്നിട്ടും രക്ഷാസംഘം പാലത്തിന് സമീപം കുടുങ്ങിയ യാത്രക്കാരെ സുരക്ഷിതമായി പുറത്തെടുത്തു. |
| HI-16 | Multiple clauses | यदि बस समय पर आती है, तो हम बाजार जाएंगे और लौटते समय दवा खरीदेंगे। | ബസ് സമയത്ത് വന്നാൽ ഞങ്ങൾ മാർക്കറ്റിൽ പോയി മടങ്ങുമ്പോൾ മരുന്ന് വാങ്ങും. |
| HI-17 | Technical/academic | यह शोध मिट्टी के तापमान और बीज के अंकुरण के बीच संबंध का अध्ययन करता है। | ഈ ഗവേഷണം മണ്ണിന്റെ താപനിലയും വിത്തിന്റെ മുളപ്പും തമ്മിലുള്ള ബന്ധം പഠിക്കുന്നു. |
| HI-18 | AI/computer science | कंप्यूटर दृष्टि प्रणाली तस्वीर में वस्तुओं की पहचान करती है। | കമ്പ്യൂട്ടർ വിഷൻ സംവിധാനം ചിത്രത്തിലെ വസ്തുക്കളെ തിരിച്ചറിയുന്നു. |
| HI-19 | Idiom | उसने कठिन समय में भी हिम्मत नहीं हारी। | പ്രയാസകാലത്തും അവൻ ധൈര്യം കൈവിട്ടില്ല. |
| HI-20 | Structure | रिपोर्ट पढ़ने के बाद ही समिति ने अंतिम निर्णय लिया। | റിപ്പോർട്ട് വായിച്ചതിന് ശേഷമാണ് കമ്മിറ്റി അന്തിമ തീരുമാനം എടുത്തത്. |

## Ambiguity controls

- Names and locations are explicitly identified as people or places through surrounding verbs and nouns.
- Dates use a four-digit year and an unambiguous day-month-year order in the source language.
- Times use an explicit morning/evening marker where needed and a 24-hour-safe minute format.
- Numbers include units or a concrete counted noun.
- Pronoun and coreference cases are deliberately short and documented with a single reference interpretation; they should be flagged PARTIAL if a system output cannot preserve the intended antecedent.
- The Kannada AI case uses “ಕೃತಕ ಬುದ್ಧಿಮತ್ತೆಯ ಮಾದರಿ” (artificial-intelligence model) and “ಭಾಷാ ಮಾದರികൾ” (language patterns), not the ambiguous term previously associated with “neural network.”
- Idioms are selected where the intended Malayalam sense is stated by the reference translation; literal renderings may be PARTIAL or FAIL depending on whether the idiomatic meaning survives.
- Sentences avoid sarcasm, culturally specific wordplay, unclear ellipsis, and competing readings.

## Before/after result record

For each run, create a result copy or spreadsheet with:

```text
Benchmark version:
Run date:
Model/checkpoint:
Transformers version:
Source language:
Case ID:
Raw output:
Label: PASS | PARTIAL | FAIL
Reviewer note:
```

The benchmark source and reference text must remain unchanged between runs. Improvements are reported as changed label counts and reviewer notes, not as an unsupported accuracy percentage.

## Recommended execution commands

Start the Python service and use the existing API contract:

```powershell
cd translation-service
.\.venv\Scripts\python.exe service.py
```

For each row, send `sourceLanguage` and `text` to `POST http://127.0.0.1:8000/translate` with `targetLanguage: "ml"`, or run the same cases through `POST http://127.0.0.1:3001/api/translate` for application-boundary validation.

## Status

This document defines the Phase 1 internal quality benchmark. It does not claim that the current model passes these cases and does not alter the application, model, or decoding configuration.
