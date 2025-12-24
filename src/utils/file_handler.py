import json
import os


def read_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def read_json(path: str) -> dict:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"JSON file not found: {path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON in file: {path}")
    

def write_json(path, data):
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
