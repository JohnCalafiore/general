#!/usr/bin/env python3
"""Dedup prefilter for the second brain's nightly run.

Splits each raw/*.md dump into blocks (separated by `---` dividers or H2 headers),
hashes each block, and compares against the ledger in state/seen.json. Only blocks
never seen before are written to state/new-since-last-run.md — that file is the sole
input to the synthesis step, which keeps token usage down and prevents the same
email/message from being re-summarized into duplicate memories on later runs.

Usage: python3 scripts/prefilter.py
"""

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "raw"
STATE_DIR = ROOT / "state"
LEDGER = STATE_DIR / "seen.json"
OUTPUT = STATE_DIR / "new-since-last-run.md"

BLOCK_SPLIT = re.compile(r"^---\s*$|^(?=## )", re.MULTILINE)


def blocks_of(text: str):
    for block in BLOCK_SPLIT.split(text):
        if block is None:
            continue
        block = block.strip()
        if block:
            yield block


def digest(block: str) -> str:
    # Normalize whitespace so trivial re-export differences don't defeat dedup.
    normalized = " ".join(block.split()).lower()
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def main() -> None:
    STATE_DIR.mkdir(exist_ok=True)
    ledger = {"last_run": None, "hashes": {}}
    if LEDGER.exists():
        ledger = json.loads(LEDGER.read_text())

    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    seen = ledger["hashes"]
    new_blocks = []
    total = 0

    for dump in sorted(RAW_DIR.glob("*.md")):
        for block in blocks_of(dump.read_text()):
            total += 1
            h = digest(block)
            if h in seen:
                continue
            seen[h] = now
            new_blocks.append(f"<!-- source: {dump.name} -->\n{block}")

    header = (
        f"<!-- generated {now} | {len(new_blocks)} new of {total} blocks; "
        "synthesis must read ONLY this file, not raw/ -->\n\n"
    )
    OUTPUT.write_text(header + "\n\n---\n\n".join(new_blocks) + "\n")

    ledger["last_run"] = now
    LEDGER.write_text(json.dumps(ledger, indent=2))
    print(f"{len(new_blocks)} new blocks of {total} total -> {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
