from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd

from stressum.aggregate import RunAggregates
from stressum.load import RunBundle


def _md_table(df: pd.DataFrame, float_fmt: str = "{:.4g}") -> str:
    """Markdown pipe table from a small DataFrame."""
    if df.empty:
        return "_empty_\n"
    headers = list(df.columns)
    lines = ["| " + " | ".join(str(h) for h in headers) + " |"]
    lines.append("| " + " | ".join("---" for _ in headers) + " |")
    for _, row in df.iterrows():
        cells = []
        for h in headers:
            v = row[h]
            if isinstance(v, float):
                cells.append(float_fmt.format(v))
            elif v is None or (isinstance(v, float) and pd.isna(v)):
                cells.append("")
            else:
                cells.append(str(v))
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def write_replica_csv(agg: RunAggregates, out: Path) -> None:
    pd.DataFrame(agg.rows).to_csv(out, index=False)


def run_summary_dict(
    bundle: RunBundle,
    agg: RunAggregates,
    *,
    proxy_cpu: dict[str, float] | None = None,
    postgres_process: dict[str, float] | None = None,
    total_footprint: dict[str, float] | None = None,
    open_loop: bool = False,
) -> dict[str, Any]:
    meta = bundle.metadata or {}
    first = bundle.summaries[0].get("runInfo") or {} if bundle.summaries else {}
    row: dict[str, Any] = {
        "run_dir": bundle.run_dir.name,
        "scenario": meta.get("scenario"),
        "bench_replica_count": meta.get("bench_replica_count"),
        "replicas_in_bundle": len(agg.replica_ids),
        "sut": first.get("sut"),
        "workload": first.get("workload"),
        "load_mode": first.get("loadMode"),
        "target_rps_per_replica": first.get("targetRps"),
        "open_loop": open_loop,
        "total_achieved_rps_sum": agg.total_successful_rps,
        "total_successful_rps_sum": agg.total_successful_rps,
        "total_error_rps_sum": agg.total_error_rps,
        "total_completed_rps_sum": agg.total_completed_rps,
        "total_attempted_rps_sum": agg.total_attempted_rps,
        "total_requests": agg.total_requests,
        "total_successful_requests": agg.total_successful_requests,
        "total_failed_requests": agg.total_failed,
        "aggregate_error_rate": agg.aggregate_error_rate,
        "top_error_types": _format_top_errors(agg.errors_by_type),
        "median_replica_p50_ms": agg.median_p50_ms,
        "median_replica_p95_ms": agg.median_p95_ms,
        "median_replica_p99_ms": agg.median_p99_ms,
        "median_replica_p999_ms": agg.median_p999_ms,
    }
    if proxy_cpu is not None:
        row["proxy_service_cpu_aligned_peak_pct"] = proxy_cpu["service_cpu_aligned_peak_pct"]
        row["proxy_service_cpu_legacy_peak_sum_pct"] = proxy_cpu[
            "service_cpu_legacy_peak_sum_pct"
        ]
        row["proxy_host_cpu_aligned_peak_pct"] = proxy_cpu.get("host_cpu_aligned_peak_pct", "")
    else:
        row["proxy_service_cpu_aligned_peak_pct"] = ""
        row["proxy_service_cpu_legacy_peak_sum_pct"] = ""
        row["proxy_host_cpu_aligned_peak_pct"] = ""
    if postgres_process is not None:
        row["postgres_cpu_pct_peak"] = postgres_process.get("cpu_pct_peak", "")
        row["postgres_cpu_pct_mean"] = postgres_process.get("cpu_pct_mean", "")
        row["postgres_rss_mb_peak"] = postgres_process.get("rss_mb_peak", "")
        row["postgres_rss_mb_mean"] = postgres_process.get("rss_mb_mean", "")
    else:
        row["postgres_cpu_pct_peak"] = ""
        row["postgres_cpu_pct_mean"] = ""
        row["postgres_rss_mb_peak"] = ""
        row["postgres_rss_mb_mean"] = ""
    if total_footprint is not None:
        row["bench_cpu_sum_pct"] = total_footprint["bench_cpu_sum_pct"]
        row["proxy_rss_mb_aligned_peak"] = total_footprint.get("proxy_rss_mb_aligned_peak", "")
        row["total_cpu_pct"] = total_footprint["total_cpu_pct"]
        row["total_rss_mb_peak"] = total_footprint["total_rss_mb_peak"]
    else:
        row["bench_cpu_sum_pct"] = ""
        row["proxy_rss_mb_aligned_peak"] = ""
        row["total_cpu_pct"] = ""
        row["total_rss_mb_peak"] = ""
    return row


def _format_top_errors(errors_by_type: dict[str, int], limit: int = 5) -> str:
    if not errors_by_type:
        return ""
    ranked = sorted(errors_by_type.items(), key=lambda x: (-x[1], x[0]))[:limit]
    return "; ".join(f"{name}:{count}" for name, count in ranked)


def write_run_summary_row(
    bundle: RunBundle,
    agg: RunAggregates,
    out: Path,
) -> None:
    pd.DataFrame([run_summary_dict(bundle, agg)]).to_csv(out, index=False)


def write_node_summary_csv(df: pd.DataFrame, out: Path) -> None:
    df.to_csv(out, index=False)


def write_tables_readme(paths: dict[str, Path], out: Path) -> None:
    """Index of generated tables with embedded key summaries."""
    run_df = pd.read_csv(paths["run_summary.csv"])
    rep_df = pd.read_csv(paths["replica_breakdown.csv"])
    parts = [
        "# Tables",
        "Generated artifacts in this folder (CSV, Markdown, PNG as applicable).",
        "",
        "## Files",
        "",
    ]
    for name in sorted(paths.keys()):
        parts.append(f"- [`{name}`]({name})")
    parts.extend(
        [
            "",
            "## Run summary (copy)",
            "",
            _md_table(run_df),
            "## Replica latency / throughput (copy)",
            "",
            _md_table(
                rep_df[
                    [
                        "replica_id",
                        "achieved_throughput_rps",
                        "error_rate",
                        "p50_ms",
                        "p95_ms",
                        "p99_ms",
                    ]
                ]
            ),
        ]
    )
    out.write_text("\n".join(parts), encoding="utf-8")
