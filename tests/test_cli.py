from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

import pandas as pd
import pytest

from stressum.cli import (
    comparison_output_dir,
    discover_stressum_repo_root,
    main,
)

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "minimal-run"

_COMPARISON_DIR_RE = re.compile(r"^comparison-\d{4}-\d{2}-\d{2}-\d{6}-\d{6}$")


def _latest_comparison_out(fake_root: Path) -> Path:
    outs = sorted((fake_root / "output").glob("comparison-*"))
    assert outs, "expected output/comparison-* under fake root"
    return outs[-1]


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


def _assert_unrecognized_subcommand(argv: list[str], capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exc:
        main(argv)
    assert exc.value.code == 2
    err = capsys.readouterr().err
    assert "unrecognized arguments" in err


def test_batch_token_rejected_by_argparse(capsys: pytest.CaptureFixture[str]) -> None:
    _assert_unrecognized_subcommand(["batch"], capsys)


def test_compare_token_rejected_by_argparse(capsys: pytest.CaptureFixture[str]) -> None:
    _assert_unrecognized_subcommand(["compare"], capsys)


def test_run_token_rejected_by_argparse(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    _assert_unrecognized_subcommand(["run", str(tmp_path / "some-run")], capsys)


def test_comparison_output_dir_pattern() -> None:
    root = discover_stressum_repo_root()
    assert root is not None
    out = comparison_output_dir()
    assert out.parent == root / "output"
    assert _COMPARISON_DIR_RE.match(out.name)


def test_compare_writes_artifacts(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("stressum.cli.discover_stressum_repo_root", lambda: tmp_path)
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
    code = main([])
    assert code == 0
    out = _latest_comparison_out(tmp_path)
    meta = json.loads((out / "comparison_metadata.json").read_text(encoding="utf-8"))
    assert len(meta["scenarios"]) == 2
    assert meta["scenarios"][0]["latency_percentiles_source"] == "summary_json_median"
    assert meta["scenarios"][1]["label"] == "B"
    assert (out / "comparison_summary.csv").is_file()
    bar_bases = (
        "comparison_total_throughput",
        "comparison_total_completed_rps",
        "comparison_total_successful_requests",
        "comparison_open_loop_missed_opportunities",
        "comparison_open_loop_scheduling_delay",
        "comparison_latency_p50",
        "comparison_latency_p95",
        "comparison_latency_p99",
        "comparison_latency_p999",
    )
    for base in bar_bases:
        assert (
            out / base / f"{base}__cmp-a.png"
        ).is_file(), f"missing per-technology bar chart for cmp-a: {base}"
        assert (
            out / base / f"{base}__B.png"
        ).is_file(), f"missing per-technology bar chart for B: {base}"
        legacy = out / f"{base}.png"
        assert not legacy.exists(), f"legacy monolithic bar chart still exists: {base}"
    summary = pd.read_csv(out / "comparison_summary.csv")
    assert "total_successful_rps_sum" in summary.columns
    assert "total_successful_requests" in summary.columns
    assert "proxy_host_cpu_aligned_peak_pct" in summary.columns
    assert "postgres_cpu_pct_peak" in summary.columns
    assert "postgres_rss_mb_peak" in summary.columns
    assert "bench_cpu_sum_pct" in summary.columns
    assert "total_cpu_pct" in summary.columns
    assert "proxy_rss_mb_aligned_peak" in summary.columns
    assert "total_rss_mb_peak" in summary.columns
    assert "total_error_rps_sum" in summary.columns
    assert "total_completed_rps_sum" in summary.columns
    assert "open_loop" in summary.columns
    assert summary["open_loop"].all()
    assert (out / "comparison_pg_numbackends" / "comparison_pg_numbackends__cmp-a.png").is_file()
    assert (out / "comparison_pg_numbackends" / "comparison_pg_numbackends__B.png").is_file()
    assert (
        out / "comparison_postgres_process_cpu" / "comparison_postgres_process_cpu__cmp-a.png"
    ).is_file()
    assert (
        out / "comparison_postgres_process_cpu" / "comparison_postgres_process_cpu__B.png"
    ).is_file()
    assert (
        out / "comparison_postgres_process_rss" / "comparison_postgres_process_rss__cmp-a.png"
    ).is_file()
    assert (
        out / "comparison_postgres_process_rss" / "comparison_postgres_process_rss__B.png"
    ).is_file()
    assert not (out / "comparison_pg_numbackends__cmp-a.png").exists()
    assert not (out / "comparison_pg_numbackends.png").exists()
    assert not (out / "comparison_postgres_process_cpu.png").exists()
    assert not (out / "comparison_postgres_process_rss.png").exists()


def test_compare_writes_cross_technology_bar_charts(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("stressum.cli.discover_stressum_repo_root", lambda: tmp_path)
    cfg_dir = tmp_path
    run_h = cfg_dir / "hikari-a"
    run_o = cfg_dir / "ojp-a"
    shutil.copytree(FIXTURE, run_h)
    shutil.copytree(FIXTURE, run_o)
    cfg_path = cfg_dir / "stressum-comparison.json"
    cfg_path.write_text(
        json.dumps(
            {
                "runs": [
                    {"path": "hikari-a", "label": "Hikari A"},
                    {"path": "ojp-a", "label": "OJP A"},
                ]
            }
        ),
        encoding="utf-8",
    )
    code = main([])
    assert code == 0
    out = _latest_comparison_out(tmp_path)
    cross_tech_bases = (
        "comparison_cross_tech_total_throughput",
        "comparison_cross_tech_total_completed_rps",
        "comparison_cross_tech_total_successful_requests",
        "comparison_cross_tech_open_loop_missed_opportunities",
        "comparison_cross_tech_open_loop_scheduling_delay",
        "comparison_cross_tech_latency_p50",
        "comparison_cross_tech_latency_p95",
        "comparison_cross_tech_latency_p99",
        "comparison_cross_tech_latency_p999",
        "comparison_cross_tech_error_rate",
        "comparison_cross_tech_throughput_latency_p95",
        "comparison_cross_tech_throughput_latency_p99",
        "comparison_cross_tech_postgres_process_cpu_peak",
        "comparison_cross_tech_postgres_process_rss_peak",
        "comparison_cross_tech_throughput_postgres_cpu",
        "comparison_cross_tech_throughput_postgres_rss",
        "comparison_cross_tech_total_cpu_peak",
        "comparison_cross_tech_total_rss_peak",
        "comparison_cross_tech_throughput_total_cpu",
        "comparison_cross_tech_throughput_total_rss",
    )
    for base in cross_tech_bases:
        assert (out / f"{base}.png").is_file(), f"missing cross-tech chart: {base}"
    meta = json.loads((out / "comparison_metadata.json").read_text(encoding="utf-8"))
    for scenario in meta["scenarios"]:
        assert "postgres_cpu_pct_peak" in scenario
        assert "postgres_rss_mb_peak" in scenario
        assert "total_cpu_pct" in scenario
        assert "total_rss_mb_peak" in scenario
        assert "bench_cpu_sum_pct" in scenario


def test_compare_hdr_merged_metadata(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("stressum.cli.discover_stressum_repo_root", lambda: tmp_path)
    cfg_dir = tmp_path
    run_a = cfg_dir / "ha"
    run_b = cfg_dir / "hb"
    shutil.copytree(FIXTURE, run_a)
    shutil.copytree(FIXTURE, run_b)
    _write_single_interval_hlog(run_a / "replica-0" / "latency.hlog")
    _write_single_interval_hlog(run_a / "replica-1" / "latency.hlog")
    _write_single_interval_hlog(run_b / "replica-0" / "latency.hlog")
    _write_single_interval_hlog(run_b / "replica-1" / "latency.hlog")
    cfg_path = cfg_dir / "stressum-comparison.json"
    cfg_path.write_text(json.dumps({"runs": [{"path": "ha"}, {"path": "hb"}]}), encoding="utf-8")
    code = main([])
    assert code == 0
    out = _latest_comparison_out(tmp_path)
    meta = json.loads((out / "comparison_metadata.json").read_text(encoding="utf-8"))
    for sc in meta["scenarios"]:
        assert sc["latency_percentiles_source"] == "hdr_merged"
        ml = sc["merged_latency_ms"]
        assert abs(float(ml["p50"]) - 2.0) < 0.05


def test_compare_missing_config(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("stressum.cli.discover_stressum_repo_root", lambda: tmp_path)
    code = main([])
    assert code == 2


def test_compare_config_requires_two_runs(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("stressum.cli.discover_stressum_repo_root", lambda: tmp_path)
    cfg = tmp_path / "stressum-comparison.json"
    cfg.write_text(json.dumps({"runs": [{"path": "only-one"}]}), encoding="utf-8")
    code = main([])
    assert code == 2


def test_compare_fairness_warning(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("stressum.cli.discover_stressum_repo_root", lambda: tmp_path)
    cfg_dir = tmp_path
    run_a = cfg_dir / "fa"
    run_b = cfg_dir / "fb"
    shutil.copytree(FIXTURE, run_a)
    shutil.copytree(FIXTURE, run_b)
    summ = json.loads((run_b / "replica-0" / "summary.json").read_text(encoding="utf-8"))
    summ["runInfo"]["workload"] = "W2_MIXED"
    (run_b / "replica-0" / "summary.json").write_text(json.dumps(summ), encoding="utf-8")
    cfg_path = cfg_dir / "stressum-comparison.json"
    cfg_path.write_text(json.dumps({"runs": [{"path": "fa"}, {"path": "fb"}]}), encoding="utf-8")
    assert main([]) == 0
    out = _latest_comparison_out(tmp_path)
    meta = json.loads((out / "comparison_metadata.json").read_text(encoding="utf-8"))
    assert any("workload" in w for w in meta["global_warnings"])


def test_compare_proxy_host_cpu_charts(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("stressum.cli.discover_stressum_repo_root", lambda: tmp_path)
    cfg_dir = tmp_path
    run_a = cfg_dir / "proxy-a"
    run_b = cfg_dir / "proxy-b"
    shutil.copytree(FIXTURE, run_a)
    shutil.copytree(FIXTURE, run_b)
    for run in (run_a, run_b):
        proxy_dir = run / "node_metrics" / "proxy"
        proxy_dir.mkdir(parents=True, exist_ok=True)
        (proxy_dir / "node-a_proc_metrics.csv").write_text(
            "timestamp,pid,cpu_pct,host_cpu_pct,rss_mb,vsz_mb\n"
            "2026-01-01T00:00:00Z,1,10.0,20.0,100,200\n"
            "2026-01-01T00:00:01Z,1,30.0,40.0,100,200\n",
            encoding="utf-8",
        )
    cfg_path = cfg_dir / "stressum-comparison.json"
    cfg_path.write_text(
        json.dumps({"runs": [{"path": "proxy-a"}, {"path": "proxy-b"}]}),
        encoding="utf-8",
    )
    assert main([]) == 0
    out = _latest_comparison_out(tmp_path)
    summary = pd.read_csv(out / "comparison_summary.csv")
    assert summary["proxy_host_cpu_aligned_peak_pct"].tolist() == [40.0, 40.0]
    host_cpu_base = "comparison_proxy_host_cpu_aligned_peak"
    assert (
        out / host_cpu_base / f"{host_cpu_base}__proxy-a.png"
    ).is_file()
    assert (
        out / host_cpu_base / f"{host_cpu_base}__proxy-b.png"
    ).is_file()
    assert not (out / f"{host_cpu_base}.png").exists()
