"""Folder-leap detection and origin tracking utility.

Importing :mod:`filestate` from another script records the script's directory
in the file itself using a ``# ORIGIN:`` tag. If the script is later run from a
new directory, the module detects the leap, invokes a trigger, and updates the
embedded origin.
"""
from __future__ import annotations

import inspect
import os
import subprocess
import sys
from pathlib import Path
from typing import Optional, Tuple

TAG = "# ORIGIN:"
DISABLE_TRIGGER_ENV = "FILESTATE_DISABLE_TRIGGER"
DISABLE_PRIME_ENV = "FILESTATE_DISABLE_AUTO_PRIME"

__all__ = ["folderleap"]


def _get_calling_script() -> Optional[Path]:
    """Return the path to the first non-filestate module on the call stack."""
    this_file = Path(__file__).resolve()

    for frame_info in reversed(inspect.stack()):
        fname = frame_info.frame.f_globals.get("__file__")
        if not fname:
            continue
        candidate = Path(fname).resolve()
        if candidate != this_file and candidate.exists():
            return candidate
    return None


def _read_origin(path: Path) -> Tuple[Optional[str], str]:
    """Return the stored origin directory (if any) and the remainder of the file."""
    content = path.read_text(encoding="utf-8")
    first_line, sep, rest = content.partition("\n")
    if first_line.startswith(TAG):
        origin = first_line.split(":", 1)[1].strip()
        return origin, rest
    return None, content


def _write_origin(path: Path, origin: str, body: str) -> None:
    """Rewrite *path* with the origin tag followed by the prior content."""
    with path.open("w", encoding="utf-8") as handle:
        handle.write(f"{TAG}{origin}\n")
        handle.write(body)


def _on_leap(path: Path, old_dir: str, new_dir: str) -> None:
    """Default handler executed when a folder leap is detected."""
    print(f"[folderleap] {path.name} moved:")
    print(f"  from: {old_dir}")
    print(f"    to: {new_dir}")
    subprocess.run([sys.executable, str(path)], check=False)


def folderleap() -> None:
    """Public symbol imported by user scripts to activate folder-leap tracking."""
    return None


def _auto_prime() -> None:
    debug_enabled = os.getenv("FILESTATE_DEBUG")

    argv_path: Optional[Path] = None
    argv0 = sys.argv[0]
    if argv0 not in {"", "-c", "-m"}:
        candidate = Path(argv0).resolve()
        if candidate.exists():
            argv_path = candidate

    calling_script = _get_calling_script()
    stdlib_root = Path(sys.base_prefix).resolve()

    if argv_path and (calling_script is None or stdlib_root in calling_script.parents):
        calling_script = argv_path

    if not calling_script or not calling_script.exists():
        return

    if debug_enabled:
        print(f"[filestate] detected script: {calling_script}")

    current_dir = str(calling_script.parent.resolve())
    origin_dir, body = _read_origin(calling_script)

    if origin_dir is None:
        _write_origin(calling_script, current_dir, body)
        return

    if current_dir != origin_dir:
        if not os.getenv(DISABLE_TRIGGER_ENV):
            _on_leap(calling_script, origin_dir, current_dir)
        _write_origin(calling_script, current_dir, body)


if not os.getenv(DISABLE_PRIME_ENV):
    _auto_prime()
