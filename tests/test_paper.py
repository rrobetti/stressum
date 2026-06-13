from __future__ import annotations

import json
import shutil
from pathlib import Path

import pandas as pd
import pytest

from stressum.aggregate import aggregate_bundle, postgres_process_summary, proxy_tier_cpu_summary
from stressum.cli import main
from stressum.load import load_run_bundle
from stressum.paper import _paper_repetition_dataframe, _summary_stats_dataframe

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "minimal-run"


def _latest_comparison_out(fake_root: Path) -> Path:
    outs = sorted((fake_root / "output").glob("comparison-*"))
    assert outs
    return outs[-1]


def _scenario_entry(run_dir: Path, label: str) -> dict[str, object]:
    bundle = load_run_bundle(run_dir)
    return {
        "label": label,
        "bundle": bundle,
        "agg": aggregate_bundle(bundle),
        "merged": None,
        "proxy_cpu": proxy_tier_cpu_summary(bundle),
        "postgres_process": postgres_process_summary(bundle),
        "total_footprint": None,
        "run_metadata": bundle.metadata or {},
    }


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


def test_paper_detects_missing_load_metadata(tmp_path: Path) -> None:
    run_dir = tmp_path / "missing-load"
    shutil.copytree(FIXTURE, run_dir)
    for replica_name in ("replica-0", "replica-1"):
        summary_path = run_dir / replica_name / "summary.json"
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
        summary["runInfo"]["targetRps"] = None
        summary_path.write_text(json.dumps(summary), encoding="utf-8")
    scenario = _scenario_entry(run_dir, "Hikari A")
    with pytest.raises(ValueError, match="Could not infer load metadata"):
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


def test_compare_handles_missing_metrics_safely(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("stressum.cli.discover_stressum_repo_root", lambda: tmp_path)
    run_a = tmp_path / "ha"
    run_b = tmp_path / "hb"
    shutil.copytree(FIXTURE, run_a)
    shutil.copytree(FIXTURE, run_b)
    for path in (run_a, run_b):
        pg_metrics = path / "node_metrics" / "pg_metrics.csv"
        if pg_metrics.exists():
            pg_metrics.unlink()
        db_proc = path / "node_metrics" / "db" / "db_proc_metrics.csv"
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
