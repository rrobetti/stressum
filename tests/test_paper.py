from __future__ import annotations

import json
import math
import shutil
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import pytest

from stressum.aggregate import aggregate_bundle, postgres_process_summary, proxy_tier_cpu_summary
from stressum.cli import main
from stressum.hdr_merge import merge_run_histogram
from stressum.load import load_run_bundle
from stressum.paper import (
    _paper_color,
    _paper_repetition_dataframe,
    _plot_metric_line,
    _summary_stats_dataframe,
)

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "minimal-run"


def _latest_comparison_out(fake_root: Path) -> Path:
    outs = sorted((fake_root / "output").glob("comparison-*"))
    assert outs
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


def _scenario_entry(run_dir: Path, label: str) -> dict[str, object]:
    bundle = load_run_bundle(run_dir)
    merged, _ = merge_run_histogram(bundle.hdr_paths)
    return {
        "label": label,
        "bundle": bundle,
        "agg": aggregate_bundle(bundle),
        "merged": merged,
        "proxy_cpu": proxy_tier_cpu_summary(bundle),
        "postgres_process": postgres_process_summary(bundle),
        "total_footprint": None,
        "run_metadata": bundle.metadata or {},
    }


def _write_ojp_jvm_metrics(
    run_dir: Path,
    *,
    node_specs: dict[str, list[tuple[float, float, float | None]]],
    xmx: str | None = None,
) -> None:
    proxy_dir = run_dir / "node_metrics" / "proxy"
    proxy_dir.mkdir(parents=True, exist_ok=True)
    for node_name, rows in node_specs.items():
        has_heap_max = any(heap_max is not None for _, _, heap_max in rows)
        header = "timestamp,heap_used_mb,heap_committed_mb"
        if has_heap_max:
            header += ",heap_max_mb"
        lines = [header]
        for index, (used, committed, heap_max) in enumerate(rows):
            timestamp = f"2026-01-01T00:00:0{index}Z"
            line = f"{timestamp},{used:.2f},{committed:.2f}"
            if has_heap_max:
                line += f",{heap_max:.2f}" if heap_max is not None else ","
            lines.append(line)
        (proxy_dir / f"{node_name}_jvm_metrics.csv").write_text(
            "\n".join(lines) + "\n",
            encoding="utf-8",
        )
    if xmx is not None:
        metadata_path = run_dir / "run_metadata.json"
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        metadata["environment"] = {"jvmArgs": [f"-Xmx{xmx}"]}
        metadata_path.write_text(json.dumps(metadata), encoding="utf-8")


def test_paper_repetition_grouping_and_ci(tmp_path: Path) -> None:
    scenarios: list[dict[str, object]] = []
    for index in range(5):
        run_dir = tmp_path / f"hikari-{index}"
        shutil.copytree(FIXTURE, run_dir)
        for replica_name in ("replica-0", "replica-1"):
            summary_path = run_dir / replica_name / "summary.json"
            summary = json.loads(summary_path.read_text(encoding="utf-8"))
            summary["runInfo"]["targetRps"] = 100
            summary["successfulThroughputRps"] = 45.0 + index
            summary["achievedThroughputRps"] = 45.0 + index
            summary["attemptedRps"] = 50.0
            summary["errorThroughputRps"] = 5.0
            summary_path.write_text(json.dumps(summary), encoding="utf-8")
            _write_single_interval_hlog(run_dir / replica_name / "latency.hlog")
        scenarios.append(_scenario_entry(run_dir, f"Hikari {chr(ord('A') + index)}"))

    repetition_df, warnings = _paper_repetition_dataframe(
        scenarios,
        load_map={},
        expected_repetitions=5,
    )
    assert not warnings
    assert repetition_df["repetition"].tolist() == [1, 2, 3, 4, 5]
    assert repetition_df["repetition_count"].tolist() == [5, 5, 5, 5, 5]
    assert repetition_df["aggregate_rps"].tolist() == [100.0] * 5
    assert repetition_df["per_node_rps"].tolist() == [50.0] * 5

    summary_df = _summary_stats_dataframe(repetition_df)
    successful = summary_df.loc[summary_df["metric_name"] == "successful_rps"].iloc[0]
    assert successful["repetition_count"] == 5
    assert pytest.approx(successful["mean"], rel=1e-6) == 94.0
    assert successful["stddev"] > 0.0
    assert successful["ci95_high"] > successful["mean"]
    assert successful["ci95_low"] < successful["mean"]
    # HDR-derived latency metrics have ci95 set to NaN (no distributional CI)
    p95_row = summary_df.loc[summary_df["metric_name"] == "p95_latency_ms"].iloc[0]
    assert math.isnan(p95_row["ci95_low"])
    assert math.isnan(p95_row["ci95_high"])
    p99_row = summary_df.loc[summary_df["metric_name"] == "p99_latency_ms"].iloc[0]
    assert math.isnan(p99_row["ci95_low"])
    assert math.isnan(p99_row["ci95_high"])
    mean_failed = summary_df.loc[summary_df["metric_name"] == "mean_failed_latency_ms"].iloc[0]
    assert pytest.approx(mean_failed["mean"], rel=1e-6) == ((5.0 * 10.0 + 6.0 * 20.0) / 30.0)


def test_paper_aggregates_ojp_heap_metrics_and_summary_stats(tmp_path: Path) -> None:
    scenarios: list[dict[str, object]] = []
    expected_heap_used: list[float] = []
    for index in range(5):
        run_dir = tmp_path / f"ojp-{index}"
        shutil.copytree(FIXTURE, run_dir)
        for replica_name in ("replica-0", "replica-1"):
            summary_path = run_dir / replica_name / "summary.json"
            summary = json.loads(summary_path.read_text(encoding="utf-8"))
            summary["runInfo"]["targetRps"] = 100
            summary_path.write_text(json.dumps(summary), encoding="utf-8")
            _write_single_interval_hlog(run_dir / replica_name / "latency.hlog")
        _write_ojp_jvm_metrics(
            run_dir,
            xmx="256m",
            node_specs={
                "ojp-1": [(10.0 + index, 20.0, None), (12.0 + index, 20.0, None)],
                "ojp-2": [(30.0 + index, 40.0, None), (32.0 + index, 40.0, None)],
            },
        )
        expected_heap_used.append((11.0 + index) + (31.0 + index))
        scenarios.append(_scenario_entry(run_dir, f"OJP {chr(ord('A') + index)}"))

    repetition_df, warnings = _paper_repetition_dataframe(
        scenarios,
        load_map={},
        expected_repetitions=5,
    )

    assert not warnings
    assert repetition_df["ojp_heap_used_mib"].tolist() == expected_heap_used
    assert repetition_df["ojp_heap_committed_mib"].tolist() == [60.0] * 5
    assert repetition_df["ojp_heap_max_mib"].tolist() == [512.0] * 5
    assert repetition_df["ojp_heap_utilisation_percent"].tolist() == pytest.approx(
        [(value / 512.0) * 100.0 for value in expected_heap_used]
    )

    summary_df = _summary_stats_dataframe(repetition_df)
    assert {
        "ojp_heap_used_mib",
        "ojp_heap_committed_mib",
        "ojp_heap_max_mib",
        "ojp_heap_utilisation_percent",
    }.issubset(set(summary_df["metric_name"]))
    heap_used = summary_df.loc[summary_df["metric_name"] == "ojp_heap_used_mib"].iloc[0]
    assert heap_used["mean"] == pytest.approx(sum(expected_heap_used) / len(expected_heap_used))
    assert heap_used["max"] == max(expected_heap_used)


def test_paper_detects_missing_load_metadata(tmp_path: Path) -> None:
    run_dir = tmp_path / "missing-load"
    shutil.copytree(FIXTURE, run_dir)
    for replica_name in ("replica-0", "replica-1"):
        summary_path = run_dir / replica_name / "summary.json"
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
        summary["runInfo"]["targetRps"] = None
        summary_path.write_text(json.dumps(summary), encoding="utf-8")
        _write_single_interval_hlog(run_dir / replica_name / "latency.hlog")
    scenario = _scenario_entry(run_dir, "Hikari A")
    with pytest.raises(ValueError, match="Could not infer load metadata"):
        _paper_repetition_dataframe([scenario], load_map={}, expected_repetitions=5)


def test_paper_missing_hdr_raises_value_error(tmp_path: Path) -> None:
    run_dir = tmp_path / "no-hdr"
    shutil.copytree(FIXTURE, run_dir)
    for replica_name in ("replica-0", "replica-1"):
        summary_path = run_dir / replica_name / "summary.json"
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
        summary["runInfo"]["targetRps"] = 100
        summary_path.write_text(json.dumps(summary), encoding="utf-8")
    # Deliberately do NOT write any .hlog files — merged will be None
    scenario = _scenario_entry(run_dir, "Hikari A")
    assert scenario["merged"] is None
    with pytest.raises(ValueError, match="missing HDR histogram data"):
        _paper_repetition_dataframe([scenario], load_map={}, expected_repetitions=5)


def test_compare_generates_report_and_debug_outputs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("stressum.cli.discover_stressum_repo_root", lambda: tmp_path)
    labels = []
    for technology in ("hikari", "ojp"):
        for index in range(5):
            run_name = f"{technology}-{index}"
            run_dir = tmp_path / run_name
            shutil.copytree(FIXTURE, run_dir)
            for replica_name in ("replica-0", "replica-1"):
                summary_path = run_dir / replica_name / "summary.json"
                summary = json.loads(summary_path.read_text(encoding="utf-8"))
                summary["runInfo"]["targetRps"] = 100
                summary_path.write_text(json.dumps(summary), encoding="utf-8")
                _write_single_interval_hlog(run_dir / replica_name / "latency.hlog")
            labels.append(
                {
                    "path": run_name,
                    "label": (
                        f"{'Hikari' if technology == 'hikari' else 'OJP'} "
                        f"{chr(ord('A') + index)}"
                    ),
                }
            )
    (tmp_path / "stressum-comparison.json").write_text(
        json.dumps({"runs": labels}),
        encoding="utf-8",
    )

    assert main(["--all", "--repetitions", "5"]) == 0
    out = _latest_comparison_out(tmp_path)
    report = out / "report"
    debug = out / "debug"
    assert (report / "summary_stats.csv").is_file()
    assert (report / "repetition_values.csv").is_file()
    assert (report / "throughput_vs_load.png").is_file()
    assert (report / "mean_failed_latency_vs_load.png").is_file()
    assert (report / "slo_heatmap.png").is_file()
    assert (debug / "comparison_cross_tech_total_throughput.png").is_file()
    summary_df = pd.read_csv(report / "summary_stats.csv")
    assert {
        "scenario",
        "technology",
        "per_node_rps",
        "aggregate_rps",
        "repetition_count",
        "metric_name",
        "mean",
        "median",
        "stddev",
        "min",
        "max",
        "ci95_low",
        "ci95_high",
    }.issubset(summary_df.columns)
    assert "mean_failed_latency_ms" in set(summary_df["metric_name"])


def test_compare_generates_ojp_heap_outputs_and_rationale(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("stressum.cli.discover_stressum_repo_root", lambda: tmp_path)
    labels = []
    for index in range(5):
        run_name = f"ojp-{index}"
        run_dir = tmp_path / run_name
        shutil.copytree(FIXTURE, run_dir)
        for replica_name in ("replica-0", "replica-1"):
            summary_path = run_dir / replica_name / "summary.json"
            summary = json.loads(summary_path.read_text(encoding="utf-8"))
            summary["runInfo"]["targetRps"] = 100
            summary_path.write_text(json.dumps(summary), encoding="utf-8")
            _write_single_interval_hlog(run_dir / replica_name / "latency.hlog")
        _write_ojp_jvm_metrics(
            run_dir,
            node_specs={
                "ojp-1": [(20.0 + index, 40.0, 256.0), (22.0 + index, 40.0, 256.0)],
                "ojp-2": [(30.0 + index, 45.0, 256.0), (32.0 + index, 45.0, 256.0)],
            },
        )
        labels.append({"path": run_name, "label": f"OJP {chr(ord('A') + index)}"})
    (tmp_path / "stressum-comparison.json").write_text(
        json.dumps({"runs": labels}),
        encoding="utf-8",
    )

    assert main(["--all", "--repetitions", "5"]) == 0
    out = _latest_comparison_out(tmp_path)
    report = out / "report"
    debug = out / "debug"
    for name in (
        "ojp_heap_used_committed_vs_load.png",
        "ojp_heap_utilisation_vs_load.png",
    ):
        assert (report / name).is_file()
    assert not (report / "ojp_heap_used_vs_load.png").exists()
    assert not (report / "ojp_heap_committed_vs_load.png").exists()
    assert not (report / "ojp_heap_used_committed_max_vs_load.png").exists()
    assert (debug / "ojp_heap_per_node_boxplot.png").is_file()
    rationale = (report / "GRAPH_RATIONALE.md").read_text(encoding="utf-8")
    assert (
        "OJP runs on the JVM, so RSS alone can overstate live application memory pressure."
        in rationale
    )
    assert "The shaded band above and below a line is the Min/Max Range:" in rationale
    assert "the plotted value is not a per-node median." in rationale
    assert "`throughput_vs_load.png`: the top-level throughput view." in rationale
    assert "`ojp_heap_used_committed_vs_load.png`: keeps heap used and heap committed" in rationale
    summary_df = pd.read_csv(report / "summary_stats.csv")
    assert {
        "ojp_heap_used_mib",
        "ojp_heap_committed_mib",
        "ojp_heap_max_mib",
        "ojp_heap_utilisation_percent",
    }.issubset(set(summary_df["metric_name"]))


def test_compare_handles_missing_metrics_safely(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("stressum.cli.discover_stressum_repo_root", lambda: tmp_path)
    run_a = tmp_path / "ha"
    run_b = tmp_path / "hb"
    shutil.copytree(FIXTURE, run_a)
    shutil.copytree(FIXTURE, run_b)
    for run_dir in (run_a, run_b):
        for replica_name in ("replica-0", "replica-1"):
            _write_single_interval_hlog(run_dir / replica_name / "latency.hlog")
        pg_metrics = run_dir / "node_metrics" / "pg_metrics.csv"
        if pg_metrics.exists():
            pg_metrics.unlink()
        db_proc = run_dir / "node_metrics" / "db" / "db_proc_metrics.csv"
        if db_proc.exists():
            db_proc.unlink()
    (tmp_path / "stressum-comparison.json").write_text(
        json.dumps(
            {
                "runs": [
                    {"path": "ha", "label": "Hikari A"},
                    {"path": "hb", "label": "OJP A"},
                ]
            }
        ),
        encoding="utf-8",
    )
    assert main(["--report"]) == 0
    out = _latest_comparison_out(tmp_path)
    assert (out / "report" / "postgres_backend_connections_vs_load.png").is_file()
    assert (out / "report" / "postgres_cpu_vs_load.png").is_file()
    assert not (out / "report" / "ojp_heap_used_vs_load.png").exists()
    meta = json.loads((out / "comparison_metadata.json").read_text(encoding="utf-8"))
    assert any("OJP JVM heap metrics" in warning for warning in meta["report_warnings"])


def test_paper_color_uses_central_ojp_blue() -> None:
    assert _paper_color("OJP") == "steelblue"


def test_proxy_tier_report_plots_skip_hikaricp(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    captured: dict[str, object] = {}

    def capture_plot(fig: object, out: Path) -> None:
        captured["fig"] = fig

    monkeypatch.setattr("stressum.paper._save_plot", capture_plot)
    summary_df = pd.DataFrame(
        [
            {
                "technology": "HikariCP",
                "metric_name": "proxy_tier_cpu_pct",
                "aggregate_rps": 100.0,
                "per_node_rps": 50.0,
                "mean": 0.0,
                "min": 0.0,
                "max": 0.0,
                "ci95_low": 0.0,
                "ci95_high": 0.0,
            },
            {
                "technology": "OJP",
                "metric_name": "proxy_tier_cpu_pct",
                "aggregate_rps": 100.0,
                "per_node_rps": 50.0,
                "mean": 12.0,
                "min": 11.0,
                "max": 13.0,
                "ci95_low": 11.0,
                "ci95_high": 13.0,
            },
            {
                "technology": "PgBouncer",
                "metric_name": "proxy_tier_cpu_pct",
                "aggregate_rps": 100.0,
                "per_node_rps": 50.0,
                "mean": 8.0,
                "min": 7.0,
                "max": 9.0,
                "ci95_low": 7.0,
                "ci95_high": 9.0,
            },
        ]
    )

    _plot_metric_line(
        summary_df,
        "proxy_tier_cpu_pct",
        tmp_path / "proxy_tier_cpu_vs_load.png",
        ylabel="Proxy-tier total CPU across nodes (%)",
        title="Proxy-tier total CPU across nodes vs load",
        warnings=[],
        technologies=("OJP", "PgBouncer"),
    )

    fig = captured["fig"]
    labels = fig.axes[0].get_legend_handles_labels()[1]
    assert labels == ["OJP", "Min/Max Range", "PgBouncer"]
    assert fig.axes[0].get_ylabel() == "Proxy-tier total CPU across nodes (%)"
    assert fig.axes[0].get_title() == "Proxy-tier total CPU across nodes vs load"
    plt.close(fig)
