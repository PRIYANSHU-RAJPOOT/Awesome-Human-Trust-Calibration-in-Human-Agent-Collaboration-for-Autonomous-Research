from pathlib import Path
import json

def load_jsonl(path):
    rows=[]
    with Path(path).open(encoding="utf-8") as f:
        for line_no,line in enumerate(f,1):
            if not line.strip(): continue
            try: rows.append(json.loads(line))
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON at {path}:{line_no}: {e}") from e
    return rows

def require_unique_ids(rows,key="id"):
    ids=[r.get(key) for r in rows]
    if any(x is None for x in ids): raise ValueError(f"Missing {key} field")
    if len(ids)!=len(set(ids)): raise ValueError(f"Duplicate {key} values")
    return True
