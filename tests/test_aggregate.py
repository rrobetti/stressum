from __future__ import annotations

from pathlib import Path

from stressum.aggregate import aggregate_bundle, is_open_loop, proxy_tier_cpu_summary
from stressum.load import load_run_bundle

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "minimal-run"


def test_aggregate_sums_rps_and_requests() -> None:
    bundle = load_run_bundle(FIXTURE)
    agg = aggregate_bundle(bundle)
    assert agg.total_successful_rps == 49.5 + 50.0
    assert agg.total_achieved_rps == agg.total_successful_rps
    assert agg.total_error_rps == 0.5 + 0.5
    assert agg.total_completed_rps == 50.0 + 50.5
    assert agg.total_requests == 3000
    assert agg.total_failed == 30
    assert agg.total_successful_requests == 2950
    assert abs(agg.aggregate_error_rate - (30 / 3000)) < 1e-9
    assert agg.median_p50_ms == 1.25
    assert agg.errors_by_type == {"SQLTimeoutException": 10, "PSQLException": 20}


def test_is_open_loop_from_load_mode() -> None:
    assert is_open_loop({"loadMode": "open-loop"}) is True
    assert is_open_loop({"loadMode": "open_loop"}) is True
    assert is_open_loop({"openLoop": True}) is True
    assert is_open_loop({"loadMode": "closed-loop"}) is False


def test_proxy_tier_cpu_aligned_peak(tmp_path: Path) -> None:
    run_dir = tmp_path / "proxy-run"
    proxy_dir = run_dir / "node_metrics" / "proxy"
    proxy_dir.mkdir(parents=True)
    csv_a = proxy_dir / "node-a_proc_metrics.csv"
    csv_b = proxy_dir / "node-b_proc_metrics.csv"
    csv_a.write_text(
        "timestamp,pid,cpu_pct,host_cpu_pct,rss_mb,vsz_mb\n"
        "2026-01-01T00:00:00Z,1,10.0,20.0,100,200\n"
        "2026-01-01T00:00:01Z,1,30.0,40.0,100,200\n",
        encoding="utf-8",
    )
    csv_b.write_text(
        "timestamp,pid,cpu_pct,host_cpu_pct,rss_mb,vsz_mb\n"
        "2026-01-01T00:00:00Z,2,5.0,10.0,100,200\n"
        "2026-01-01T00:00:01Z,2,25.0,30.0,100,200\n",
        encoding="utf-8",
    )
    bundle = load_run_bundle(FIXTURE)
    bundle.run_dir = run_dir
    bundle.node_metrics_csvs = {
        "node_metrics/proxy/node-a_proc_metrics.csv": csv_a,
        "node_metrics/proxy/node-b_proc_metrics.csv": csv_b,
    }
    summary = proxy_tier_cpu_summary(bundle)
    assert summary is not None
    assert summary["service_cpu_aligned_peak_pct"] == 55.0
    assert summary["service_cpu_legacy_peak_sum_pct"] == 55.0
