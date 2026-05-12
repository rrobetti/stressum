from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd

from stressum.load import RunBundle


@dataclass
class RunAggregates:
    replica_ids: list[int]
    rows: list[dict[str, Any]]
    total_achieved_rps: float
    total_attempted_rps: float
    total_requests: int
    total_failed: int
    aggregate_error_rate: float
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


def aggregate_bundle(bundle: RunBundle) -> RunAggregates:
    rows: list[dict[str, Any]] = []
    total_rps = 0.0
    total_attempted = 0.0
    total_req = 0
    total_fail = 0

    p50s: list[float] = []
    p95s: list[float] = []
    p99s: list[float] = []
    p999s: list[float] = []

    for rid, summary in zip(bundle.replica_ids, bundle.summaries, strict=True):
        ri = summary.get("runInfo") or {}
        lat = summary.get("latencyMs") or {}

        ach = float(summary.get("achievedThroughputRps") or 0.0)
        att = float(summary.get("attemptedRps") or 0.0)
        tr = int(summary.get("totalRequests") or 0)
        fr = int(summary.get("failedRequests") or 0)

        total_rps += ach
        total_attempted += att
        total_req += tr
        total_fail += fr

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
                "achieved_throughput_rps": ach,
                "attempted_rps": att,
                "error_rate": float(summary.get("errorRate") or 0.0),
                "total_requests": tr,
                "failed_requests": fr,
                "p50_ms": p50,
                "p95_ms": p95,
                "p99_ms": p99,
                "p999_ms": p999,
                "max_ms": lat.get("max"),
                "mean_ms": lat.get("mean"),
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
        total_achieved_rps=total_rps,
        total_attempted_rps=total_attempted,
        total_requests=total_req,
        total_failed=total_fail,
        aggregate_error_rate=agg_er,
        median_p50_ms=_median(p50s),
        median_p95_ms=_median(p95s),
        median_p99_ms=_median(p99s),
        median_p999_ms=_median(p999s),
    )


def node_metrics_numeric_summary(paths: dict[str, Path]) -> pd.DataFrame:
    """One row per CSV file: path + mean/std for numeric columns."""
    from stressum.load import read_node_csv

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
