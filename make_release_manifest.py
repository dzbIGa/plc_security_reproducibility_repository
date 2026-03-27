"""
Publication-safe reproducibility script for the PLC security manuscript.
This code supports analysis and validation only.
"""

from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    manifest = {}
    for path in sorted(ROOT.rglob("*")):
        if path.is_file():
            rel = path.relative_to(ROOT).as_posix()
            manifest[rel] = sha256(path)

    out = ROOT / "results" / "manifest.json"
    out.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Saved {out}")

if __name__ == "__main__":
    main()
