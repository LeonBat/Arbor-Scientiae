import json
from jsonschema import validate, ValidationError
from pathlib import Path
import sys

# Path to the JSON file (relative to this script)
json_file_path = Path("tests/test_data.json")

# Schema for an array of paper objects
schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "paperId": {"type": "string"},
            "title": {"type": "string"},
            "abstract": {"type": "string"},
            "citations": {
                "type": "array",
                "items": {"type": "object", "properties": {"paperId": {"type": "string"}}, "required": ["paperId"]}
            },
            "references": {
                "type": "array",
                "items": {"type": "object", "properties": {"paperId": {"type": "string"}}, "required": ["paperId"]}
            },
            "year": {"type": "integer"},
            "authors": {
                "type": "array",
                "items": {"type": "object", "properties": {"name": {"type": "string"}}, "required": ["name"]}
            }
        },
        "required": ["paperId", "title", "abstract", "year", "authors"]
    }
}

try:
    raw = json.loads(json_file_path.read_text(encoding="utf-8"))
except Exception as e:
    print(f"Failed to read/parse JSON file {json_file_path}:\n{e}")
    sys.exit(1)

try:
    validate(instance=raw, schema=schema)
    print(f"Validation succeeded for {json_file_path}")
except ValidationError as e:
    path = ".".join([str(p) for p in e.path])
    print(f"JSON schema validation error: {e.message}\nPath: {path}")
    sys.exit(2)
except Exception as e:
    print(f"During Validation an Exception was raised:\n{e}")
    sys.exit(3)
