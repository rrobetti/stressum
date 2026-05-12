from __future__ import annotations

import re
import shutil
from pathlib import Path

from stressum.cli import main

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "minimal-run"

_STAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-\d{6}-\d{6}$")


def _single_output_session(run_copy: Path) -> Path:
    out_root = run_copy / "output"
    assert out_root.is_dir()
    children = [p for p in out_root.iterdir() if p.is_dir()]
    assert len(children) == 1
    assert _STAMP_RE.match(children[0].name)
    return children[0]


def test_cli_writes_artifacts(tmp_path: Path) -> None:
    run_copy = tmp_path / "minimal-run"
    shutil.copytree(FIXTURE, run_copy)
    code = main([str(run_copy), "--seed", "0"])
    assert code == 0
    out = _single_output_session(run_copy)
    assert (out / "narrative.md").is_file()
    assert (out / "tables.md").is_file()
    assert (out / "replica_breakdown.csv").is_file()
    assert (out / "run_summary.csv").is_file()
    assert (out / "throughput_per_replica.png").is_file()


def test_cli_no_plots(tmp_path: Path) -> None:
    run_copy = tmp_path / "minimal-run-np"
    shutil.copytree(FIXTURE, run_copy)
    code = main([str(run_copy), "--no-plots"])
    assert code == 0
    out = _single_output_session(run_copy)
    assert (out / "narrative.md").is_file()
    assert not (out / "throughput_per_replica.png").exists()
