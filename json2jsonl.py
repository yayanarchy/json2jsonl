import json
import sys

def convert_json_to_jsonl(json_file, jsonl_file):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    with open(jsonl_file, "w", encoding="utf-8") as f:
        for entry in data:
            json.dump(entry, f)
            f.write("\n")

    print(f"Converted {json_file} to {jsonl_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 convert_jsonl.py input.json output.jsonl")
        sys.exit(1)

    convert_json_to_jsonl(sys.argv[1], sys.argv[2])
