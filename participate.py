#!/usr/bin/env python3
"""Deterministic assignment and exact prompt printing for The Octopi Trial."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import unicodedata


ROOT = Path(__file__).resolve().parent
VERSION = "octopi-v0.1"
SALT = f"theoctopitrial|{VERSION}"
ARM_FILES = {
    "A": ROOT / "prompts" / "arm-a-control.md",
    "B": ROOT / "prompts" / "arm-b-geology.md",
    "C": ROOT / "prompts" / "arm-c-cephalopods.md",
    "D": ROOT / "prompts" / "arm-d-self-selected.md",
}
COMMON_FILES = {
    "benchmark": ROOT / "prompts" / "benchmark.md",
    "survey": ROOT / "prompts" / "post-benchmark-survey.md",
}


def normalize_participant(raw: str) -> str:
    normalized = unicodedata.normalize("NFKC", raw).strip().casefold()
    if normalized.startswith("@"):
        normalized = normalized[1:]
    if not normalized:
        raise ValueError("participant identifier must not be empty")
    return normalized


def assignment(raw: str) -> dict[str, str | bool]:
    participant = normalize_participant(raw)
    digest = hashlib.sha256(f"{SALT}|{participant}".encode("utf-8")).hexdigest()
    arm = "ABCD"[int(digest[:2], 16) % 4]
    return {
        "participant_id": participant,
        "assignment_version": VERSION,
        "assignment_digest": digest,
        "arm": arm,
        "warmup_required": arm != "A",
    }


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def print_message(path: Path) -> None:
    print("BEGIN TEST MESSAGE")
    print(path.read_text(encoding="utf-8").strip())
    print("END TEST MESSAGE")


def cmd_assign(participant: str) -> None:
    receipt = assignment(participant)
    print("ASSIGNMENT RECEIPT")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    print()
    arm = str(receipt["arm"])
    if arm == "A":
        print("Arm A has no warm-up. Send no message to the tested session yet.")
        print("Run `python3 participate.py benchmark` and paste that message first.")
    else:
        print_message(ARM_FILES[arm])


def cmd_receipt(participant: str) -> None:
    print(json.dumps(assignment(participant), indent=2, sort_keys=True))


def cmd_common(stage: str) -> None:
    print_message(COMMON_FILES[stage])


def cmd_hashes() -> None:
    payload = {
        path.relative_to(ROOT).as_posix(): file_sha256(path)
        for path in [*ARM_FILES.values(), *COMMON_FILES.values()]
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="command", required=True)
    assign_p = sub.add_parser("assign", help="print an assignment receipt and warm-up")
    assign_p.add_argument("--participant", required=True)
    receipt_p = sub.add_parser("receipt", help="reproduce an assignment receipt")
    receipt_p.add_argument("--participant", required=True)
    sub.add_parser("benchmark", help="print the common benchmark")
    sub.add_parser("survey", help="print the post-benchmark survey")
    sub.add_parser("hashes", help="print SHA-256 hashes for every prompt")
    return p


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        if args.command == "assign":
            cmd_assign(args.participant)
        elif args.command == "receipt":
            cmd_receipt(args.participant)
        elif args.command in COMMON_FILES:
            cmd_common(args.command)
        elif args.command == "hashes":
            cmd_hashes()
        else:  # pragma: no cover
            raise AssertionError(args.command)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

