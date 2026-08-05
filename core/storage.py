from __future__ import annotations

import json
from pathlib import Path
from typing import Any

DATA_FILE = Path("drafts.json")


def ensure_storage() -> None:
    if not DATA_FILE.exists():
        DATA_FILE.write_text(
            json.dumps({"drafts": []}, indent=2),
            encoding="utf-8",
        )


def load_drafts() -> list[dict[str, Any]]:
    ensure_storage()
    payload = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    return payload.get("drafts", [])


def save_drafts(drafts: list[dict[str, Any]]) -> None:
    DATA_FILE.write_text(
        json.dumps({"drafts": drafts}, indent=2),
        encoding="utf-8",
    )
