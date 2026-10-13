import json
from pathlib import Path

json_path = Path(__file__).parent / "data" / "agent_terms.json"

try:
    terms = json.loads(json_path.read_text(encoding="utf-8"))
except FileNotFoundError:
    print(f"找不到文件：{json_path}")
except json.JSONDecodeError as error:
    print(f"JSON 格式错误：{error}")
else:
    for term in terms:
        print(f"{term['name']}: {term['description']}")