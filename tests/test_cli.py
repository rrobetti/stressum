from __future__ import annotations

import shutil
from pathlib import Path

from stressum.cli import main

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "minimal-run"


def test_cli_writes_artifacts(tmp_path: Path) -> None:
    run_copy = tmp_path / "minimal-run"
    shutil.copytree(FIXTURE, run_copy)
    code = main([str(run_copy), "--seed", "0"])
    assert code == 0
    out = run_copy / "paper"
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
    out = run_copy / "paper"
    assert (out / "narrative.md").is_file()
    assert not (out / "throughput_per_replica.png").exists()
