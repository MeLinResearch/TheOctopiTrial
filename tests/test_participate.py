from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import participate


class AssignmentTests(unittest.TestCase):
    def test_normalization_is_stable(self) -> None:
        self.assertEqual(
            participate.assignment("  @HarpySentinel "),
            participate.assignment("harpysentinel"),
        )

    def test_empty_identifier_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            participate.assignment(" @ ")

    def test_arm_is_valid_and_receipt_is_complete(self) -> None:
        receipt = participate.assignment("example-agent")
        self.assertIn(receipt["arm"], "ABCD")
        self.assertEqual(len(str(receipt["assignment_digest"])), 64)
        self.assertEqual(receipt["assignment_version"], "octopi-v0.1")

    def test_assignment_is_deterministic(self) -> None:
        first = participate.assignment("moltbook-volunteer")
        for _ in range(20):
            self.assertEqual(first, participate.assignment("moltbook-volunteer"))


class PromptTests(unittest.TestCase):
    def test_all_prompt_files_exist_and_are_nonempty(self) -> None:
        for path in [*participate.ARM_FILES.values(), *participate.COMMON_FILES.values()]:
            self.assertTrue(path.is_file(), path)
            self.assertGreater(path.stat().st_size, 100, path)

    def test_hash_command_is_valid_json(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(ROOT / "participate.py"), "hashes"],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(proc.stdout)
        self.assertEqual(len(payload), 6)
        self.assertTrue(all(len(value) == 64 for value in payload.values()))


if __name__ == "__main__":
    unittest.main()

