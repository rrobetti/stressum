from __future__ import annotations

from pathlib import Path

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


def write_run_summary_row(
    bundle: RunBundle,
    agg: RunAggregates,
    out: Path,
) -> None:
    meta = bundle.metadata or {}
    first = bundle.summaries[0].get("runInfo") or {} if bundle.summaries else {}
    row = {
        "run_dir": bundle.run_dir.name,
        "scenario": meta.get("scenario"),
        "bench_replica_count": meta.get("bench_replica_count"),
        "replicas_in_bundle": len(agg.replica_ids),
        "sut": first.get("sut"),
        "workload": first.get("workload"),
        "load_mode": first.get("loadMode"),
        "target_rps_per_replica": first.get("targetRps"),
        "total_achieved_rps_sum": agg.total_achieved_rps,
        "total_attempted_rps_sum": agg.total_attempted_rps,
        "total_requests": agg.total_requests,
        "total_failed_requests": agg.total_failed,
        "aggregate_error_rate": agg.aggregate_error_rate,
        "median_replica_p50_ms": agg.median_p50_ms,
        "median_replica_p95_ms": agg.median_p95_ms,
        "median_replica_p99_ms": agg.median_p99_ms,
        "median_replica_p999_ms": agg.median_p999_ms,
    }
    pd.DataFrame([row]).to_csv(out, index=False)


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
