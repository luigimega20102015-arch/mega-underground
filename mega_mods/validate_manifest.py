#!/usr/bin/env python3
"""Validate MEGA UNDERGROUND add-on metadata without touching copyrighted game files."""
import json
import re
import sys
from pathlib import PurePosixPath, Path

ALLOWED_TYPES = {"addon", "replacement"}
ALLOWED_STATES = {"metadata-only", "native-pc-tested", "web-tested"}
ALLOWED_PART_STATES = {"yes", "no", "unknown"}
ID_RE = re.compile(r"^[a-z0-9][a-z0-9._-]{2,79}$")

def validate(doc):
    errors = []
    if not isinstance(doc, dict):
        return ["Manifest must be an object"]
    if type(doc.get("schemaVersion")) is not int or doc["schemaVersion"] != 1:
        errors.append("schemaVersion must be integer 1")
    for key in ("id", "displayName", "author", "sourceUrl"):
        if not isinstance(doc.get(key), str) or not doc[key].strip():
            errors.append(f"{key} must be a nonempty string")
    if isinstance(doc.get("id"), str) and not ID_RE.fullmatch(doc["id"]):
        errors.append("id must be lowercase letters, digits, dots, underscores or dashes (3-80 chars)")
    if doc.get("installType") not in ALLOWED_TYPES:
        errors.append("installType must be addon or replacement")
    if doc.get("compatibility") not in ALLOWED_STATES:
        errors.append("invalid compatibility status")
    if not isinstance(doc.get("requires"), list) or not all(isinstance(x, str) for x in doc["requires"]):
        errors.append("requires must be a list of strings")
    files = doc.get("files")
    if not isinstance(files, list) or not files:
        errors.append("files must be a nonempty list")
    else:
        seen = set()
        for i, entry in enumerate(files):
            if not isinstance(entry, dict) or not isinstance(entry.get("path"), str) or not isinstance(entry.get("role"), str):
                errors.append(f"files[{i}] requires path and role strings")
                continue
            p = entry["path"].replace("\\", "/")
            path = PurePosixPath(p)
            if p.startswith("/") or any(c in (".", "..") for c in p.split("/")) or ":" in p or not p.strip():
                errors.append(f"files[{i}] unsafe relative path")
            if p.lower() in seen:
                errors.append(f"files[{i}] duplicate path")
            seen.add(p.lower())
    parts = doc.get("parts")
    if not isinstance(parts, list):
        errors.append("parts must be a list")
    else:
        for i, part in enumerate(parts):
            if not isinstance(part, dict) or not isinstance(part.get("category"), str) or part.get("available") not in ALLOWED_PART_STATES:
                errors.append(f"parts[{i}] invalid category or availability")
    return errors

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 mega_mods/validate_manifest.py vehicle.json")
        return 2
    try:
        doc = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}")
        return 2
    errors = validate(doc)
    for err in errors:
        print("ERROR:", err)
    if errors:
        return 1
    print("OK: manifest metadata valid (not proof of game compatibility)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
