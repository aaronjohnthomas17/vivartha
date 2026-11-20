"""Execute the fixed Phase 1 benchmark through the Node API and save raw outputs."""
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).parent
BENCHMARK = ROOT / "PHASE_1_TRANSLATION_QUALITY_BENCHMARK.md"
OUTPUT = ROOT / "PHASE_1_TRANSLATION_RAW_RUN.json"
LANGUAGES = {"EN": "en", "TA": "ta", "TE": "te", "KA": "kn", "HI": "hi"}

rows = re.findall(
    r"^\| ((?:EN|TA|TE|KA|HI)-\d{2}) \| ([^|]+) \| (.*?) \| (.*?) \|$",
    BENCHMARK.read_text(encoding="utf-8"),
    re.M,
)
results = []
for case_id, category, source, reference in rows:
    payload = json.dumps(
        {"sourceLanguage": LANGUAGES[case_id[:2]], "text": source}
    ).encode("utf-8")
    request = Request(
        "http://127.0.0.1:3001/api/translate",
        data=payload,
        headers={"content-type": "application/json"},
    )
    try:
        with urlopen(request, timeout=180) as response:
            body = json.loads(response.read().decode("utf-8"))
        actual, error = body.get("translation", ""), ""
    except Exception as exc:  # preserve failures for review
        actual, error = "", str(exc)
    results.append(
        {
            "id": case_id,
            "category": category.strip(),
            "sourceLanguage": LANGUAGES[case_id[:2]],
            "source": source,
            "reference": reference,
            "actual": actual,
            "error": error,
        }
    )

OUTPUT.write_text(
    json.dumps(
        {"runAt": datetime.now(timezone.utc).isoformat(), "results": results},
        ensure_ascii=False,
        indent=2,
    ),
    encoding="utf-8",
)
print(f"cases={len(results)} failures={sum(bool(row['error']) for row in results)}")
