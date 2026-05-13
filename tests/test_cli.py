from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

import pytest

from stressum.cli import (
    comparison_output_dir,
    default_output_dir,
    discover_stressum_repo_root,
    main,
)

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "minimal-run"

_STAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-\d{6}-\d{6}$")
_COMPARISON_DIR_RE = re.compile(r"^comparison-\d{4}-\d{2}-\d{2}-\d{6}-\d{6}$")


def _write_single_interval_hlog(path: Path) -> None:
    from hdrh.histogram import HdrHistogram
    from hdrh.log import HistogramLogWriter

    h = HdrHistogram(1, 60_000_000_000, 5)
    for ns in (1_000_000, 2_000_000, 3_000_000):
        h.record_value(ns)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        w = HistogramLogWriter(f)
        w.output_log_format_version()
        w.output_legend()
        w.output_interval_histogram(h, 0.0, 1.0, 1_000_000.0)


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


def test_batch_processes_all_run_subfolders(tmp_path: Path) -> None:
    results = tmp_path / "results"
    run_a = results / "run-a"
    run_b = results / "run-b"
    shutil.copytree(FIXTURE, run_a)
    shutil.copytree(FIXTURE, run_b)
    code = main(["batch", str(results)])
    assert code == 0
    out_a = _single_output_session(run_a)
    out_b = _single_output_session(run_b)
    assert (out_a / "narrative.md").is_file()
    assert (out_b / "narrative.md").is_file()


def test_batch_skips_empty_and_non_bundles(tmp_path: Path) -> None:
    results = tmp_path / "results"
    good = results / "z-good"
    shutil.copytree(FIXTURE, good)
    (results / "empty-dir").mkdir(parents=True)
    bad = results / "not-a-run"
    bad.mkdir()
    (bad / "readme.txt").write_text("x", encoding="utf-8")
    code = main(["batch", str(results)])
    assert code == 0
    assert _single_output_session(good)
    assert not (results / "empty-dir" / "output").exists()
    assert not (bad / "output").exists()


def test_batch_missing_results_root(tmp_path: Path) -> None:
    code = main(["batch", str(tmp_path / "does-not-exist")])
    assert code == 2


def test_batch_rejects_out() -> None:
    with pytest.raises(SystemExit) as excinfo:
        main(["batch", "--out", "/tmp"])
    assert excinfo.value.code == 2


def test_default_output_dir_uses_repo_output_when_run_inside_repo() -> None:
    root = discover_stressum_repo_root()
    assert root is not None
    run = root / "tests" / "fixtures" / "minimal-run"
    assert run.is_dir()
    out = default_output_dir(run)
    assert out.parent.parent == root / "output"
    assert out.parent.name == "minimal-run"
    assert _STAMP_RE.match(out.name)


def test_comparison_output_dir_pattern() -> None:
    root = discover_stressum_repo_root()
    assert root is not None
    out = comparison_output_dir()
    assert out.parent == root / "output"
    assert _COMPARISON_DIR_RE.match(out.name)


def test_compare_writes_artifacts(tmp_path: Path) -> None:
    cfg_dir = tmp_path
    run_a = cfg_dir / "cmp-a"
    run_b = cfg_dir / "cmp-b"
    shutil.copytree(FIXTURE, run_a)
    shutil.copytree(FIXTURE, run_b)
    cfg_path = cfg_dir / "stressum-comparison.json"
    cfg_path.write_text(
        json.dumps({"runs": [{"path": "cmp-a"}, {"path": "cmp-b", "label": "B"}]}),
        encoding="utf-8",
    )
    out = cfg_dir / "compare-out"
    code = main(["compare", "--config", str(cfg_path), "--out", str(out), "--seed", "0"])
    assert code == 0
    meta = json.loads((out / "comparison_metadata.json").read_text(encoding="utf-8"))
    assert len(meta["scenarios"]) == 2
    assert meta["scenarios"][0]["latency_percentiles_source"] == "summary_json_median"
    assert meta["scenarios"][1]["label"] == "B"
    assert (out / "comparison_summary.csv").is_file()
    assert (out / "comparison_total_throughput.png").is_file()
    assert (out / "comparison_latency_p50.png").is_file()
    assert (out / "comparison_latency_p95.png").is_file()
    assert (out / "comparison_latency_p99.png").is_file()
    assert (out / "comparison_latency_p999.png").is_file()


def test_compare_no_plots(tmp_path: Path) -> None:
    cfg_dir = tmp_path
    run_a = cfg_dir / "a"
    run_b = cfg_dir / "b"
    shutil.copytree(FIXTURE, run_a)
    shutil.copytree(FIXTURE, run_b)
    cfg_path = cfg_dir / "cfg.json"
    cfg_path.write_text(json.dumps({"runs": [{"path": "a"}, {"path": "b"}]}), encoding="utf-8")
    out = cfg_dir / "out-np"
    code = main(["compare", "--config", str(cfg_path), "--out", str(out), "--no-plots"])
    assert code == 0
    assert (out / "comparison_metadata.json").is_file()
    assert not (out / "comparison_latency_p50.png").exists()
    assert not (out / "comparison_latency_p95.png").exists()
    assert not (out / "comparison_latency_p99.png").exists()
    assert not (out / "comparison_latency_p999.png").exists()


def test_compare_hdr_merged_metadata(tmp_path: Path) -> None:
    cfg_dir = tmp_path
    run_a = cfg_dir / "ha"
    run_b = cfg_dir / "hb"
    shutil.copytree(FIXTURE, run_a)
    shutil.copytree(FIXTURE, run_b)
    _write_single_interval_hlog(run_a / "replica-0" / "latency.hlog")
    _write_single_interval_hlog(run_a / "replica-1" / "latency.hlog")
    _write_single_interval_hlog(run_b / "replica-0" / "latency.hlog")
    _write_single_interval_hlog(run_b / "replica-1" / "latency.hlog")
    cfg_path = cfg_dir / "cfg.json"
    cfg_path.write_text(json.dumps({"runs": [{"path": "ha"}, {"path": "hb"}]}), encoding="utf-8")
    out = cfg_dir / "out-hdr"
    code = main(["compare", "--config", str(cfg_path), "--out", str(out)])
    assert code == 0
    meta = json.loads((out / "comparison_metadata.json").read_text(encoding="utf-8"))
    for sc in meta["scenarios"]:
        assert sc["latency_percentiles_source"] == "hdr_merged"
        ml = sc["merged_latency_ms"]
        assert abs(float(ml["p50"]) - 2.0) < 0.05


def test_compare_missing_config(tmp_path: Path) -> None:
    code = main(["compare", "--config", str(tmp_path / "missing.json")])
    assert code == 2


def test_compare_config_requires_two_runs(tmp_path: Path) -> None:
    cfg = tmp_path / "bad.json"
    cfg.write_text(json.dumps({"runs": [{"path": "only-one"}]}), encoding="utf-8")
    code = main(["compare", "--config", str(cfg)])
    assert code == 2


def test_compare_fairness_warning(tmp_path: Path) -> None:
    cfg_dir = tmp_path
    run_a = cfg_dir / "fa"
    run_b = cfg_dir / "fb"
    shutil.copytree(FIXTURE, run_a)
    shutil.copytree(FIXTURE, run_b)
    summ = json.loads((run_b / "replica-0" / "summary.json").read_text(encoding="utf-8"))
    summ["runInfo"]["workload"] = "W2_MIXED"
    (run_b / "replica-0" / "summary.json").write_text(json.dumps(summ), encoding="utf-8")
    cfg_path = cfg_dir / "cfg.json"
    cfg_path.write_text(json.dumps({"runs": [{"path": "fa"}, {"path": "fb"}]}), encoding="utf-8")
    out = cfg_dir / "out-w"
    assert main(["compare", "--config", str(cfg_path), "--out", str(out), "--no-plots"]) == 0
    meta = json.loads((out / "comparison_metadata.json").read_text(encoding="utf-8"))
    assert any("workload" in w for w in meta["global_warnings"])
