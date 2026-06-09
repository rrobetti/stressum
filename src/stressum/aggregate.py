from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd

from stressum.load import RunBundle, read_node_csv


@dataclass
class RunAggregates:
    replica_ids: list[int]
    rows: list[dict[str, Any]]
    total_achieved_rps: float
    total_successful_rps: float
    total_error_rps: float
    total_completed_rps: float
    total_attempted_rps: float
    total_requests: int
    total_failed: int
    total_successful_requests: int
    aggregate_error_rate: float
    errors_by_type: dict[str, int]
    median_p50_ms: float | None
    median_p95_ms: float | None
    median_p99_ms: float | None
    median_p999_ms: float | None


def _f(summary: dict[str, Any], *keys: str, default: float | None = None) -> float | None:
    cur: Any = summary
    for k in keys:
        if not isinstance(cur, dict) or k not in cur:
            return default
        cur = cur[k]
    if isinstance(cur, (int, float)):
        return float(cur)
    return default


def _successful_rps(summary: dict[str, Any]) -> float:
    v = summary.get("successfulThroughputRps")
    if isinstance(v, (int, float)):
        return float(v)
    v = summary.get("achievedThroughputRps")
    if isinstance(v, (int, float)):
        return float(v)
    return 0.0


def _error_rps(summary: dict[str, Any]) -> float:
    v = summary.get("errorThroughputRps")
    if isinstance(v, (int, float)):
        return float(v)
    return 0.0


def _total_rps(summary: dict[str, Any]) -> float:
    v = summary.get("totalThroughputRps")
    if isinstance(v, (int, float)):
        return float(v)
    return _successful_rps(summary) + _error_rps(summary)


def is_open_loop(run_info: dict[str, Any]) -> bool:
    if run_info.get("openLoop") is True:
        return True
    load_mode = run_info.get("loadMode")
    if isinstance(load_mode, str):
        normalized = load_mode.replace("_", "-").lower()
        if normalized == "open-loop":
            return True
    return False


def _merge_errors_by_type(
    target: dict[str, int],
    summary: dict[str, Any],
) -> None:
    raw = summary.get("errorsByType")
    if not isinstance(raw, dict):
        return
    for key, count in raw.items():
        if isinstance(count, (int, float)):
            target[str(key)] = target.get(str(key), 0) + int(count)


def aggregate_bundle(bundle: RunBundle) -> RunAggregates:
    rows: list[dict[str, Any]] = []
    total_successful = 0.0
    total_error = 0.0
    total_completed = 0.0
    total_attempted = 0.0
    total_req = 0
    total_fail = 0
    total_success = 0
    errors_by_type: dict[str, int] = {}

    p50s: list[float] = []
    p95s: list[float] = []
    p99s: list[float] = []
    p999s: list[float] = []

    for rid, summary in zip(bundle.replica_ids, bundle.summaries, strict=True):
        ri = summary.get("runInfo") or {}
        lat = summary.get("latencyMs") or {}

        succ = _successful_rps(summary)
        err_rps = _error_rps(summary)
        tot_rps = _total_rps(summary)
        att = float(summary.get("attemptedRps") or 0.0)
        tr = int(summary.get("totalRequests") or 0)
        fr = int(summary.get("failedRequests") or 0)
        sr = int(summary.get("successfulRequests") or (tr - fr))

        total_successful += succ
        total_error += err_rps
        total_completed += tot_rps
        total_attempted += att
        total_req += tr
        total_fail += fr
        total_success += sr
        _merge_errors_by_type(errors_by_type, summary)

        p50 = lat.get("p50")
        p95 = lat.get("p95")
        p99 = lat.get("p99")
        p999 = lat.get("p999")
        if isinstance(p50, (int, float)):
            p50s.append(float(p50))
        if isinstance(p95, (int, float)):
            p95s.append(float(p95))
        if isinstance(p99, (int, float)):
            p99s.append(float(p99))
        if isinstance(p999, (int, float)):
            p999s.append(float(p999))

        rows.append(
            {
                "replica_id": rid,
                "sut": ri.get("sut"),
                "workload": ri.get("workload"),
                "load_mode": ri.get("loadMode"),
                "target_rps": ri.get("targetRps"),
                "achieved_throughput_rps": succ,
                "successful_throughput_rps": succ,
                "error_throughput_rps": err_rps,
                "total_throughput_rps": tot_rps,
                "attempted_rps": att,
                "error_rate": float(summary.get("errorRate") or 0.0),
                "total_requests": tr,
                "successful_requests": sr,
                "failed_requests": fr,
                "p50_ms": p50,
                "p95_ms": p95,
                "p99_ms": p99,
                "p999_ms": p999,
                "max_ms": lat.get("max"),
                "mean_ms": lat.get("mean"),
                "mean_successful_ms": lat.get("meanSuccessful"),
                "mean_failed_ms": lat.get("meanFailed"),
                "mean_total_ms": lat.get("meanTotal"),
                "duration_s": ri.get("durationSeconds"),
                "pool_size": ri.get("poolSize"),
            }
        )

    agg_er = (total_fail / total_req) if total_req else 0.0

    def _median(xs: list[float]) -> float | None:
        if not xs:
            return None
        s = pd.Series(xs)
        return float(s.median())

    return RunAggregates(
        replica_ids=bundle.replica_ids,
        rows=rows,
        total_achieved_rps=total_successful,
        total_successful_rps=total_successful,
        total_error_rps=total_error,
        total_completed_rps=total_completed,
        total_attempted_rps=total_attempted,
        total_requests=total_req,
        total_failed=total_fail,
        total_successful_requests=total_success,
        aggregate_error_rate=agg_er,
        errors_by_type=errors_by_type,
        median_p50_ms=_median(p50s),
        median_p95_ms=_median(p95s),
        median_p99_ms=_median(p99s),
        median_p999_ms=_median(p999s),
    )


def _proxy_tier_proc_paths(bundle: RunBundle) -> list[Path]:
    paths: list[Path] = []
    for rel, path in sorted(bundle.node_metrics_csvs.items()):
        if "/proxy/" in rel and rel.endswith("_proc_metrics.csv"):
            paths.append(path)
    for rel, path in sorted(bundle.node_metrics_csvs.items()):
        if "/lb/" in rel and rel.endswith("_proc_metrics.csv"):
            paths.append(path)
    return paths


def _proxy_tier_service_cpu_rollups(
    bundle: RunBundle,
) -> tuple[pd.Series, float, float, list[Path]] | None:
    """Return (tier_sum series, aligned_peak, legacy_peak_sum, proc_paths) or None."""
    proc_paths = _proxy_tier_proc_paths(bundle)
    if not proc_paths:
        return None

    series_by_node: list[pd.Series] = []
    legacy_peak_sum = 0.0

    for path in proc_paths:
        try:
            df = read_node_csv(path)
        except Exception:
            continue
        if "timestamp" not in df.columns or "cpu_pct" not in df.columns:
            continue
        ts = pd.to_datetime(df["timestamp"], utc=True, errors="coerce")
        cpu = pd.to_numeric(df["cpu_pct"], errors="coerce")
        valid = ts.notna() & cpu.notna()
        if not valid.any():
            continue
        node = pd.Series(cpu[valid].values, index=ts[valid])
        node = node.groupby(level=0).mean()
        series_by_node.append(node)
        legacy_peak_sum += float(node.max())

    if not series_by_node:
        return None

    combined = pd.concat(series_by_node, axis=1).fillna(0.0)
    tier_sum = combined.sum(axis=1)
    aligned_peak = float(tier_sum.max())
    return tier_sum, aligned_peak, legacy_peak_sum, proc_paths


def _proxy_tier_host_cpu_rollups(
    bundle: RunBundle,
) -> tuple[pd.Series, float] | None:
    """Return (time-aligned host_cpu sum series, aligned_peak) or None."""
    proc_paths = _proxy_tier_proc_paths(bundle)
    if not proc_paths:
        return None

    host_series: list[pd.Series] = []
    for path in proc_paths:
        try:
            df = read_node_csv(path)
        except Exception:
            continue
        if "timestamp" not in df.columns or "host_cpu_pct" not in df.columns:
            continue
        ts = pd.to_datetime(df["timestamp"], utc=True, errors="coerce")
        host = pd.to_numeric(df["host_cpu_pct"], errors="coerce")
        valid = ts.notna() & host.notna()
        if not valid.any():
            continue
        node = pd.Series(host[valid].values, index=ts[valid])
        node = node.groupby(level=0).mean()
        host_series.append(node)

    if not host_series:
        return None

    host_combined = pd.concat(host_series, axis=1).fillna(0.0)
    tier_sum = host_combined.sum(axis=1)
    aligned_peak = float(tier_sum.max())
    return tier_sum, aligned_peak


def proxy_tier_cpu_timeseries(
    bundle: RunBundle,
) -> tuple[pd.Series, pd.Series, float] | None:
    """Relative seconds, time-aligned proxy-tier service_cpu sum, and aligned peak."""
    rollups = _proxy_tier_service_cpu_rollups(bundle)
    if rollups is None:
        return None
    tier_sum, aligned_peak, _, _ = rollups
    t0 = pd.Series(
        (tier_sum.index - tier_sum.index.min()).total_seconds(),
        index=tier_sum.index,
    )
    return t0, tier_sum, aligned_peak


def proxy_tier_host_cpu_timeseries(
    bundle: RunBundle,
) -> tuple[pd.Series, pd.Series, float] | None:
    """Relative seconds, time-aligned proxy-tier host_cpu sum, and aligned peak."""
    rollups = _proxy_tier_host_cpu_rollups(bundle)
    if rollups is None:
        return None
    tier_sum, aligned_peak = rollups
    t0 = pd.Series(
        (tier_sum.index - tier_sum.index.min()).total_seconds(),
        index=tier_sum.index,
    )
    return t0, tier_sum, aligned_peak


def _db_proc_metrics_path(bundle: RunBundle) -> Path | None:
    for key, path in sorted(bundle.node_metrics_csvs.items()):
        if key.endswith("db/db_proc_metrics.csv"):
            return path
    return None


def postgres_process_summary(bundle: RunBundle) -> dict[str, float] | None:
    """Peak and mean CPU/RSS for the PostgreSQL server process (db_proc_metrics.csv)."""
    path = _db_proc_metrics_path(bundle)
    if path is None:
        return None
    try:
        df = read_node_csv(path)
    except Exception:
        return None
    if df.empty or "timestamp" not in df.columns:
        return None

    out: dict[str, float] = {}
    for col, peak_key, mean_key in (
        ("cpu_pct", "cpu_pct_peak", "cpu_pct_mean"),
        ("rss_mb", "rss_mb_peak", "rss_mb_mean"),
    ):
        if col not in df.columns:
            continue
        ser = pd.to_numeric(df[col], errors="coerce").dropna()
        if ser.empty:
            continue
        out[peak_key] = float(ser.max())
        out[mean_key] = float(ser.mean())
    return out or None


def proxy_tier_cpu_summary(bundle: RunBundle) -> dict[str, float] | None:
    """Time-aligned proxy tier CPU rollup (service_cpu from cpu_pct)."""
    rollups = _proxy_tier_service_cpu_rollups(bundle)
    if rollups is None:
        return None
    tier_sum, aligned_peak, legacy_peak_sum, _ = rollups

    host_rollups = _proxy_tier_host_cpu_rollups(bundle)
    host_aligned_peak: float | None = None
    if host_rollups is not None:
        _, host_aligned_peak = host_rollups

    out: dict[str, float] = {
        "service_cpu_aligned_peak_pct": aligned_peak,
        "service_cpu_legacy_peak_sum_pct": legacy_peak_sum,
        "service_cpu_mean_pct": float(tier_sum.mean()),
    }
    if host_aligned_peak is not None:
        out["host_cpu_aligned_peak_pct"] = host_aligned_peak
    return out


def _proxy_tier_rss_rollups(bundle: RunBundle) -> tuple[pd.Series, float] | None:
    """Return (time-aligned rss_mb sum series, aligned_peak) or None."""
    proc_paths = _proxy_tier_proc_paths(bundle)
    if not proc_paths:
        return None

    series_by_node: list[pd.Series] = []
    for path in proc_paths:
        try:
            df = read_node_csv(path)
        except Exception:
            continue
        if "timestamp" not in df.columns or "rss_mb" not in df.columns:
            continue
        ts = pd.to_datetime(df["timestamp"], utc=True, errors="coerce")
        rss = pd.to_numeric(df["rss_mb"], errors="coerce")
        valid = ts.notna() & rss.notna()
        if not valid.any():
            continue
        node = pd.Series(rss[valid].values, index=ts[valid])
        node = node.groupby(level=0).mean()
        series_by_node.append(node)

    if not series_by_node:
        return None

    combined = pd.concat(series_by_node, axis=1).fillna(0.0)
    tier_sum = combined.sum(axis=1)
    aligned_peak = float(tier_sum.max())
    return tier_sum, aligned_peak


def proxy_tier_rss_summary(bundle: RunBundle) -> dict[str, float] | None:
    """Time-aligned proxy tier RSS rollup (sum of rss_mb across proxy/LB nodes)."""
    rollups = _proxy_tier_rss_rollups(bundle)
    if rollups is None:
        return None
    tier_sum, aligned_peak = rollups
    return {
        "rss_mb_aligned_peak": aligned_peak,
        "rss_mb_mean": float(tier_sum.mean()),
    }


def bench_jvm_cpu_summary(bundle: RunBundle) -> dict[str, float]:
    """Sum of per-replica appCpuMedian (bench JVM service_cpu, in-process)."""
    total = 0.0
    for summary in bundle.summaries:
        v = summary.get("appCpuMedian")
        if isinstance(v, (int, float)):
            total += float(v)
    return {"bench_cpu_sum_pct": total}


def total_resource_footprint_summary(bundle: RunBundle) -> dict[str, float]:
    """
    Aggregated resource footprint: bench replicas + PostgreSQL + proxy/LB tier.

    CPU total sums independent peaks (components may peak at different times).
    Memory total excludes bench/LG RSS (not collected in exported bundles).
    """
    bench_cpu = bench_jvm_cpu_summary(bundle)["bench_cpu_sum_pct"]
    postgres = postgres_process_summary(bundle) or {}
    proxy_cpu = proxy_tier_cpu_summary(bundle) or {}
    proxy_rss = proxy_tier_rss_summary(bundle) or {}

    postgres_cpu_peak = float(postgres.get("cpu_pct_peak") or 0.0)
    proxy_cpu_peak = float(proxy_cpu.get("service_cpu_aligned_peak_pct") or 0.0)
    postgres_rss_peak = float(postgres.get("rss_mb_peak") or 0.0)
    proxy_rss_peak = float(proxy_rss.get("rss_mb_aligned_peak") or 0.0)

    return {
        "bench_cpu_sum_pct": bench_cpu,
        "postgres_cpu_pct_peak": postgres_cpu_peak,
        "proxy_service_cpu_aligned_peak_pct": proxy_cpu_peak,
        "total_cpu_pct": bench_cpu + postgres_cpu_peak + proxy_cpu_peak,
        "postgres_rss_mb_peak": postgres_rss_peak,
        "proxy_rss_mb_aligned_peak": proxy_rss_peak,
        "total_rss_mb_peak": postgres_rss_peak + proxy_rss_peak,
    }


def node_metrics_numeric_summary(paths: dict[str, Path]) -> pd.DataFrame:
    """One row per CSV file: path + mean/std for numeric columns."""
    out_rows: list[dict[str, Any]] = []
    for rel, path in paths.items():
        try:
            df = read_node_csv(path)
        except Exception:
            continue
        if df.empty:
            continue
        for col in df.columns:
            if col.lower() in ("timestamp", "time", "ts"):
                continue
            ser = pd.to_numeric(df[col], errors="coerce")
            if ser.notna().sum() == 0:
                continue
            out_rows.append(
                {
                    "file": rel,
                    "column": col,
                    "mean": float(ser.mean()),
                    "std": float(ser.std(ddof=0)) if ser.notna().sum() > 1 else 0.0,
                    "min": float(ser.min()),
                    "max": float(ser.max()),
                    "n": int(ser.notna().sum()),
                }
            )
    return pd.DataFrame(out_rows)
