from __future__ import annotations

import os
import runpy
import shutil
import subprocess
import sys
from pathlib import Path


def _read_origin_line(path: Path) -> str:
    return path.read_text(encoding="utf-8").splitlines()[0]


def test_origin_is_recorded_on_first_import(tmp_path, monkeypatch):
    repo_root = Path(__file__).resolve().parents[1]
    monkeypatch.syspath_prepend(str(repo_root))

    script = tmp_path / "example.py"
    script.write_text("from filestate import folderleap\nprint('hello')\n", encoding="utf-8")

    runpy.run_path(str(script), run_name="__main__")

    origin_line = _read_origin_line(script)
    assert origin_line.startswith("# ORIGIN:")
    assert origin_line.split(":", 1)[1].strip() == str(tmp_path.resolve())


def test_folder_leap_rewrites_origin_without_trigger(monkeypatch, tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    original_dir = tmp_path / "original"
    moved_dir = tmp_path / "moved"
    original_dir.mkdir()
    moved_dir.mkdir()

    script = original_dir / "example.py"
    script.write_text("from filestate import folderleap\nprint('hi')\n", encoding="utf-8")

    env = os.environ.copy()
    env["PYTHONPATH"] = os.pathsep.join([str(repo_root), env.get("PYTHONPATH", "")])
    env["FILESTATE_DISABLE_TRIGGER"] = "1"

    # First run embeds the origin tag.
    result = subprocess.run([sys.executable, str(script)], env=env, capture_output=True)
    assert result.returncode == 0, result.stderr.decode()
    origin_line = _read_origin_line(script)
    assert origin_line.split(":", 1)[1].strip() == str(original_dir.resolve())

    copied = moved_dir / script.name
    shutil.copy(script, copied)

    # Second run in a different directory updates the origin tag to the new folder.
    result = subprocess.run([sys.executable, str(copied)], env=env, capture_output=True)
    assert result.returncode == 0, result.stderr.decode()
    moved_origin_line = _read_origin_line(copied)
    assert moved_origin_line.split(":", 1)[1].strip() == str(moved_dir.resolve())
