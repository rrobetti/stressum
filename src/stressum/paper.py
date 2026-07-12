from __future__ import annotations

import json
import math
import re
from pathlib import Path
from typing import Any

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from stressum.aggregate import proxy_tier_rss_summary
from stressum.comparison_plots import _technology_from_label
from stressum.load import RunBundle, read_node_csv

_T_95_DF4 = 2.776
_PAPER_TECH_ORDER = ("HikariCP", "OJP", "PgBouncer")
_PAPER_COLORS = {
    "HikariCP": "darkorange",
    "OJP": "steelblue",
    "PgBouncer": "mediumseagreen",
}
_PROXY_TIER_TECH_ORDER = ("OJP", "PgBouncer")
_SLO_COLORS = {
    "pass": "#4daf4a",
    "fail latency": "#ffb000",
    "fail error rate": "#377eb8",
    "fail both": "#e41a1c",
}
_ERROR_CATEGORIES = (
    "SQLTransientException",
    "SQLTransientConnectionException",
    "StatusRuntimeException",
    "SQLException",
    "timeout",
    "connection acquisition failure",
    "admission control failure",
    "other",
)
_SUMMARY_METRICS: dict[str, str] = {
    "offered_rps": "offered_rps",
    "attempted_rps": "attempted_rps",
    "successful_rps": "successful_rps",
    "error_rps": "error_rps",
    "error_rate_pct": "error_rate_pct",
    "p95_latency_ms": "p95_latency_ms",
    "p99_latency_ms": "p99_latency_ms",
    "mean_failed_latency_ms": "mean_failed_latency_ms",
    "postgres_backend_connections": "postgres_backend_connections",
    "rps_per_db_connection": "rps_per_db_connection",
    "postgres_cpu_pct_avg": "postgres_cpu_pct_avg",
    "postgres_rss_mib": "postgres_rss_mib",
    "proxy_tier_cpu_pct": "proxy_tier_cpu_pct",
    "proxy_tier_rss_mib": "proxy_tier_rss_mib",
    "ojp_heap_used_mib": "ojp_heap_used_mib",
    "ojp_heap_committed_mib": "ojp_heap_committed_mib",
    "ojp_heap_max_mib": "ojp_heap_max_mib",
    "ojp_heap_utilisation_percent": "ojp_heap_utilisation_percent",
}


def write_paper_outputs(
    scenarios: list[dict[str, Any]],
    out_dir: Path,
    *,
    expected_repetitions: int,
    load_map_path: Path | None,
    slo_p95_ms: float,
    slo_error_rate_pct: float,
) -> tuple[dict[str, Path], list[str]]:
    load_map = _load_map(load_map_path) if load_map_path is not None else {}
    repetition_df, _, warnings = _paper_dataframes(
        scenarios,
        load_map=load_map,
        expected_repetitions=expected_repetitions,
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    repetition_out = out_dir / "repetition_values.csv"
    repetition_df.to_csv(repetition_out, index=False)

    summary_df = _summary_stats_dataframe(repetition_df)
    summary_out = out_dir / "summary_stats.csv"
    summary_df.to_csv(summary_out, index=False)

    paths: dict[str, Path] = {
        repetition_out.relative_to(out_dir).as_posix(): repetition_out,
        summary_out.relative_to(out_dir).as_posix(): summary_out,
    }
    scenario_title = _scenario_title(repetition_df)

    # Strip-plot charts: per-run dots + median line (HDR-derived latency and throughput)
    for filename, metric, ylabel, title in (
        (
            "throughput_vs_load.png",
            "successful_rps",
            "Successful throughput (RPS)",
            f"Successful throughput vs load — {scenario_title}",
        ),
        (
            "p95_latency_vs_load.png",
            "p95_latency_ms",
            "p95 successful latency (ms)",
            f"p95 successful latency vs load — {scenario_title}",
        ),
        (
            "p99_latency_vs_load.png",
            "p99_latency_ms",
            "p99 successful latency (ms)",
            f"p99 successful latency vs load — {scenario_title}",
        ),
    ):
        out = out_dir / filename
        _plot_metric_strip(
            repetition_df,
            metric,
            out,
            ylabel=ylabel,
            title=title,
            warnings=warnings,
        )
        paths[out.relative_to(out_dir).as_posix()] = out

    # Mean ± CI line charts for remaining metrics
    for filename, metric, ylabel, title in (
        (
            "error_rate_vs_load.png",
            "error_rate_pct",
            "Error rate (%)",
            f"Error rate vs load — {scenario_title}",
        ),
        (
            "mean_failed_latency_vs_load.png",
            "mean_failed_latency_ms",
            "Mean failed-request latency (ms)",
            f"Mean failed-request latency vs load — {scenario_title}",
        ),
        (
            "postgres_backend_connections_vs_load.png",
            "postgres_backend_connections",
            "Observed PostgreSQL backend connections",
            f"Observed PostgreSQL backend connections vs load — {scenario_title}",
        ),
        (
            "rps_per_db_connection_vs_load.png",
            "rps_per_db_connection",
            "Successful RPS per DB connection",
            f"Successful RPS per DB connection vs load — {scenario_title}",
        ),
        (
            "postgres_cpu_vs_load.png",
            "postgres_cpu_pct_avg",
            "PostgreSQL average CPU (%)",
            f"PostgreSQL average CPU vs load — {scenario_title}",
        ),
        (
            "postgres_rss_vs_load.png",
            "postgres_rss_mib",
            "PostgreSQL RSS (MiB)",
            f"PostgreSQL RSS vs load — {scenario_title}",
        ),
        (
            "proxy_tier_cpu_vs_load.png",
            "proxy_tier_cpu_pct",
            "Proxy-tier total CPU across nodes (%)",
            f"Proxy-tier total CPU across nodes vs load — {scenario_title}",
        ),
        (
            "proxy_tier_rss_vs_load.png",
            "proxy_tier_rss_mib",
            "Proxy-tier total RSS across nodes (MiB)",
            f"Proxy-tier total RSS across nodes vs load — {scenario_title}",
        ),
    ):
        out = out_dir / filename
        _plot_metric_line(
            summary_df,
            metric,
            out,
            ylabel=ylabel,
            title=title,
            warnings=warnings,
            technologies=_PROXY_TIER_TECH_ORDER if metric.startswith("proxy_tier_") else None,
        )
        paths[out.relative_to(out_dir).as_posix()] = out

    attempted_out = out_dir / "attempted_completed_success_error_rps.png"
    _plot_attempted_completed_chart(
        summary_df,
        attempted_out,
        title=f"Offered, attempted, successful, and error RPS vs load — {scenario_title}",
        warnings=warnings,
    )
    paths[attempted_out.relative_to(out_dir).as_posix()] = attempted_out

    for metric, filename, ylabel, title in (
        (
            "p95_latency_ms",
            "p95_latency_boxplot.png",
            "p95 successful latency (ms)",
            f"p95 successful latency distribution by load — {scenario_title}",
        ),
        (
            "p99_latency_ms",
            "p99_latency_boxplot.png",
            "p99 successful latency (ms)",
            f"p99 successful latency distribution by load — {scenario_title}",
        ),
        (
            "successful_rps",
            "throughput_boxplot.png",
            "Successful throughput (RPS)",
            f"Successful throughput distribution by load — {scenario_title}",
        ),
    ):
        out = out_dir / filename
        _plot_metric_boxplot(
            repetition_df,
            metric,
            out,
            ylabel=ylabel,
            title=title,
            warnings=warnings,
        )
        paths[out.relative_to(out_dir).as_posix()] = out

    error_breakdown_out = out_dir / "error_type_breakdown.png"
    _plot_error_type_breakdown(
        repetition_df,
        error_breakdown_out,
        title=f"Error-type breakdown by technology and load — {scenario_title}",
        warnings=warnings,
    )
    paths[error_breakdown_out.relative_to(out_dir).as_posix()] = error_breakdown_out

    slo_out = out_dir / "slo_heatmap.png"
    _plot_slo_heatmap(
        summary_df,
        slo_out,
        title=f"SLO pass/fail heatmap — {scenario_title}",
        slo_p95_ms=slo_p95_ms,
        slo_error_rate_pct=slo_error_rate_pct,
    )
    paths[slo_out.relative_to(out_dir).as_posix()] = slo_out

    for filename, metric, ylabel, title in (
        (
            "ojp_heap_utilisation_vs_load.png",
            "ojp_heap_utilisation_percent",
            "Aggregate OJP heap utilisation (%)",
            f"OJP heap utilisation vs load — {scenario_title}",
        ),
    ):
        out = out_dir / filename
        if _plot_ojp_heap_metric_line(
            summary_df,
            metric,
            out,
            ylabel=ylabel,
            title=title,
            warnings=warnings,
        ):
            paths[out.relative_to(out_dir).as_posix()] = out

    heap_combined_out = out_dir / "ojp_heap_used_committed_vs_load.png"
    if _plot_ojp_heap_combined(
        summary_df,
        heap_combined_out,
        title=f"OJP heap used and committed vs load — {scenario_title}",
        warnings=warnings,
    ):
        paths[heap_combined_out.relative_to(out_dir).as_posix()] = heap_combined_out

    index_out = out_dir / "main_graphs_index.md"
    index_out.write_text(_paper_index_markdown(), encoding="utf-8")
    paths[index_out.relative_to(out_dir).as_posix()] = index_out
    rationale_out = out_dir / "GRAPH_RATIONALE.md"
    rationale_out.write_text(_graph_rationale_markdown(), encoding="utf-8")
    paths[rationale_out.relative_to(out_dir).as_posix()] = rationale_out
    return paths, list(dict.fromkeys(warnings))


def write_ojp_heap_debug_outputs(
    scenarios: list[dict[str, Any]],
    out_dir: Path,
    *,
    expected_repetitions: int,
    load_map_path: Path | None,
) -> tuple[dict[str, Path], list[str]]:
    load_map = _load_map(load_map_path) if load_map_path is not None else {}
    try:
        _, heap_node_df, warnings = _paper_dataframes(
            scenarios,
            load_map=load_map,
            expected_repetitions=expected_repetitions,
        )
    except ValueError as exc:
        return {}, [f"{exc}; skipping ojp_heap_per_node_boxplot.png"]
    paths: dict[str, Path] = {}
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "ojp_heap_per_node_boxplot.png"
    if _plot_ojp_heap_per_node_boxplot(
        heap_node_df,
        out,
        title="OJP heap used per node by load",
        warnings=warnings,
    ):
        paths[out.relative_to(out_dir).as_posix()] = out
    return paths, list(dict.fromkeys(warnings))


def _load_map(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Load map must be a JSON object: {path}")
    return data


def _paper_repetition_dataframe(
    scenarios: list[dict[str, Any]],
    *,
    load_map: dict[str, Any],
    expected_repetitions: int,
) -> tuple[pd.DataFrame, list[str]]:
    repetition_df, _, warnings = _paper_dataframes(
        scenarios,
        load_map=load_map,
        expected_repetitions=expected_repetitions,
    )
    return repetition_df, warnings


def _paper_dataframes(
    scenarios: list[dict[str, Any]],
    *,
    load_map: dict[str, Any],
    expected_repetitions: int,
) -> tuple[pd.DataFrame, pd.DataFrame, list[str]]:
    rows: list[dict[str, Any]] = []
    heap_node_rows: list[dict[str, Any]] = []
    warnings: list[str] = []
    missing_load_labels: list[str] = []
    for scenario in scenarios:
        row, scenario_heap_node_rows, warning_messages = _paper_row_for_scenario(
            scenario,
            load_map=load_map,
        )
        warnings.extend(warning_messages)
        if row is None:
            missing_load_labels.append(str(scenario["label"]))
            continue
        rows.append(row)
        heap_node_rows.extend(scenario_heap_node_rows)
    if missing_load_labels:
        missing_text = ", ".join(sorted(missing_load_labels))
        raise ValueError(
            "Could not infer load metadata for these runs; add targetRps metadata or provide "
            f"--load-map: {missing_text}"
        )

    df = pd.DataFrame(rows)
    heap_node_df = pd.DataFrame(heap_node_rows)
    if df.empty:
        return df, heap_node_df, warnings

    group_cols = ["scenario", "workload", "technology", "per_node_rps", "aggregate_rps"]
    df = df.sort_values(group_cols + ["label", "run_dir"]).reset_index(drop=True)
    df["repetition"] = df.groupby(group_cols).cumcount() + 1
    counts = df.groupby(group_cols)["label"].transform("size")
    df["repetition_count"] = counts

    if expected_repetitions > 0:
        mismatched = (
            df[group_cols + ["repetition_count"]]
            .drop_duplicates()
            .loc[lambda x: x["repetition_count"] != expected_repetitions]
        )
        for _, row in mismatched.iterrows():
            warnings.append(
                "Expected "
                f"{expected_repetitions} repetitions for {row['technology']} @ "
                f"{row['aggregate_rps']:g} RPS, found {int(row['repetition_count'])}"
            )
    if not heap_node_df.empty:
        node_group_cols = group_cols + ["node_name"]
        heap_node_df = heap_node_df.sort_values(node_group_cols + ["label", "run_dir"]).reset_index(
            drop=True
        )
        heap_node_df["repetition"] = heap_node_df.groupby(node_group_cols).cumcount() + 1
    return df, heap_node_df, list(dict.fromkeys(warnings))


def _paper_row_for_scenario(
    scenario: dict[str, Any],
    *,
    load_map: dict[str, Any],
) -> tuple[dict[str, Any] | None, list[dict[str, Any]], list[str]]:
    bundle: RunBundle = scenario["bundle"]
    agg = scenario["agg"]
    run_info = bundle.summaries[0].get("runInfo") or {}
    metadata = bundle.metadata or {}
    technology = _canonical_technology_name(str(scenario["label"]), run_info.get("sut"))
    workload = str(run_info.get("workload") or metadata.get("scenario") or "unknown")
    scenario_name = str(metadata.get("scenario") or workload)
    load_level = _infer_load_level(
        label=str(scenario["label"]),
        run_info=run_info,
        metadata=metadata,
        aggregate_attempted_rps=agg.total_attempted_rps,
        load_map=load_map,
        bundle=bundle,
    )
    if load_level is None:
        return None, [], []

    p95_ms, p99_ms = _paper_latency_percentiles(scenario)
    postgres_process = scenario.get("postgres_process") or {}
    proxy_cpu = scenario.get("proxy_cpu") or {}
    proxy_rss = proxy_tier_rss_summary(bundle) or {}
    pg_backends = _postgres_backend_connections(bundle)
    heap_metrics = {
        "ojp_heap_used_mib": math.nan,
        "ojp_heap_committed_mib": math.nan,
        "ojp_heap_max_mib": math.nan,
        "ojp_heap_utilisation_percent": math.nan,
    }
    heap_node_rows: list[dict[str, Any]] = []
    heap_warnings: list[str] = []

    row: dict[str, Any] = {
        "label": str(scenario["label"]),
        "run_dir": bundle.run_dir.name,
        "scenario": scenario_name,
        "workload": workload,
        "technology": technology,
        "per_node_rps": load_level["per_node_rps"],
        "aggregate_rps": load_level["aggregate_rps"],
        "load_source": load_level["source"],
        "successful_rps": agg.total_successful_rps,
        "completed_rps": agg.total_completed_rps,
        "error_rps": agg.total_error_rps,
        "attempted_rps": agg.total_attempted_rps,
        "offered_rps": load_level["aggregate_rps"],
        "error_rate_pct": agg.aggregate_error_rate * 100.0,
        "p95_latency_ms": p95_ms,
        "p99_latency_ms": p99_ms,
        "mean_failed_latency_ms": _paper_mean_failed_latency_ms(scenario),
        "postgres_backend_connections": pg_backends,
        "rps_per_db_connection": (
            agg.total_successful_rps / pg_backends if pg_backends and pg_backends > 0 else math.nan
        ),
        "postgres_cpu_pct_avg": _float_or_nan(postgres_process.get("cpu_pct_mean")),
        "postgres_rss_mib": _float_or_nan(postgres_process.get("rss_mb_mean")),
        "proxy_tier_cpu_pct": _float_or_zero(proxy_cpu.get("service_cpu_mean_pct"), technology),
        "proxy_tier_rss_mib": _float_or_zero(proxy_rss.get("rss_mb_mean"), technology),
        "duration_seconds": _float_or_nan(run_info.get("durationSeconds")),
        **heap_metrics,
    }
    if technology == "OJP":
        heap_metrics, heap_node_rows, heap_warnings = _ojp_heap_metrics_for_scenario(
            row,
            bundle=bundle,
            run_info=run_info,
            metadata=metadata,
        )
        row.update(heap_metrics)

    for category in _ERROR_CATEGORIES:
        row[f"error_count_{_slug_metric(category)}"] = 0.0
    for error_name, count in agg.errors_by_type.items():
        category = _error_category(error_name)
        row[f"error_count_{_slug_metric(category)}"] += float(count)
    warnings = _missing_metric_warnings(row)
    warnings.extend(heap_warnings)
    return row, heap_node_rows, list(dict.fromkeys(warnings))


def _infer_load_level(
    *,
    label: str,
    run_info: dict[str, Any],
    metadata: dict[str, Any],
    aggregate_attempted_rps: float,
    load_map: dict[str, Any],
    bundle: RunBundle,
) -> dict[str, float | str] | None:
    count = _load_generator_count(bundle, run_info, metadata)
    if label in load_map:
        return _load_level_from_mapping(load_map[label], count=count)

    target = run_info.get("targetRps")
    if isinstance(target, (int, float)) and count > 0:
        target = float(target)
        diff_as_aggregate = abs(aggregate_attempted_rps - target)
        diff_as_per_node = abs(aggregate_attempted_rps - (target * count))
        if diff_as_per_node + 1e-9 < diff_as_aggregate:
            return {
                "per_node_rps": target,
                "aggregate_rps": target * count,
                "source": "runInfo.targetRps_per_node",
            }
        return {
            "per_node_rps": target / count,
            "aggregate_rps": target,
            "source": "runInfo.targetRps_aggregate",
        }
    return None


def _load_generator_count(
    bundle: RunBundle,
    run_info: dict[str, Any],
    metadata: dict[str, Any],
) -> int:
    candidates = (
        metadata.get("bench_replica_count"),
        metadata.get("load_generator_count"),
        run_info.get("totalInstances"),
        run_info.get("configuredReplicas"),
        len(bundle.summaries),
    )
    for candidate in candidates:
        if isinstance(candidate, (int, float)) and int(candidate) > 0:
            return int(candidate)
    return 1


def _load_level_from_mapping(value: Any, *, count: int) -> dict[str, float | str] | None:
    if isinstance(value, (int, float)):
        per_node = float(value)
        return {
            "per_node_rps": per_node,
            "aggregate_rps": per_node * count,
            "source": "load_map_per_node",
        }
    if isinstance(value, str):
        per_node = float(value)
        return {
            "per_node_rps": per_node,
            "aggregate_rps": per_node * count,
            "source": "load_map_per_node",
        }
    if not isinstance(value, dict):
        return None
    per_node = value.get("per_node_rps")
    aggregate = value.get("aggregate_rps")
    if isinstance(per_node, (int, float)) and isinstance(aggregate, (int, float)):
        return {
            "per_node_rps": float(per_node),
            "aggregate_rps": float(aggregate),
            "source": "load_map",
        }
    if isinstance(per_node, (int, float)):
        per_node = float(per_node)
        return {
            "per_node_rps": per_node,
            "aggregate_rps": per_node * count,
            "source": "load_map_per_node",
        }
    if isinstance(aggregate, (int, float)):
        aggregate = float(aggregate)
        return {
            "per_node_rps": aggregate / max(count, 1),
            "aggregate_rps": aggregate,
            "source": "load_map_aggregate",
        }
    return None


def _paper_latency_percentiles(scenario: dict[str, Any]) -> tuple[float, float]:
    merged = scenario.get("merged")
    if merged is None:
        label = scenario.get("label", "<unknown>")
        raise ValueError(
            f"Run '{label}' is missing HDR histogram data. "
            "All runs must provide HDR .hlog files for paper latency metrics."
        )
    return float(merged.p95_ms), float(merged.p99_ms)


def _paper_mean_failed_latency_ms(scenario: dict[str, Any]) -> float:
    agg = scenario["agg"]
    weighted_sum = 0.0
    failed_total = 0.0
    for row in agg.rows:
        mean_failed_ms = row.get("mean_failed_ms")
        failed_requests = row.get("failed_requests")
        if not isinstance(mean_failed_ms, (int, float)) or not isinstance(
            failed_requests, (int, float)
        ):
            continue
        if failed_requests <= 0:
            continue
        weighted_sum += float(mean_failed_ms) * float(failed_requests)
        failed_total += float(failed_requests)
    if failed_total > 0:
        return weighted_sum / failed_total
    return math.nan


def _postgres_backend_connections(bundle: RunBundle) -> float:
    for key, path in bundle.node_metrics_csvs.items():
        if not key.endswith("pg_metrics.csv"):
            continue
        try:
            df = read_node_csv(path)
        except Exception:
            return math.nan
        for column in ("numbackends", "active_backends"):
            if column in df.columns:
                values = pd.to_numeric(df[column], errors="coerce").dropna()
                if not values.empty:
                    return float(values.median())
        return math.nan
    return math.nan


def _canonical_technology_name(label: str, sut: Any) -> str:
    raw = _technology_from_label(label).strip()
    normalized = raw.lower()
    sut_text = str(sut or "").lower()
    if "hikari" in normalized or "hikari" in sut_text:
        return "HikariCP"
    if "pgbouncer" in normalized or "pgbouncer" in sut_text:
        return "PgBouncer"
    if "ojp" in normalized or "ojp" in sut_text:
        return "OJP"
    return raw or "unknown"


def _ordered_technologies(values: list[str]) -> list[str]:
    seen = set(values)
    ordered = [name for name in _PAPER_TECH_ORDER if name in seen]
    return ordered + [name for name in values if name not in ordered]


def _paper_color(technology: str) -> str:
    return _PAPER_COLORS.get(technology, "gray")


_HDR_LATENCY_METRICS = frozenset({"p95_latency_ms", "p99_latency_ms"})


def _summary_stats_dataframe(repetition_df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    group_cols = ["scenario", "workload", "technology", "per_node_rps", "aggregate_rps"]
    for keys, group in repetition_df.groupby(group_cols, sort=False):
        base = dict(zip(group_cols, keys, strict=True))
        repetition_count = int(group["repetition"].nunique())
        for metric_name, column in _SUMMARY_METRICS.items():
            series = pd.to_numeric(group[column], errors="coerce").dropna()
            if series.empty:
                continue
            values = series.astype(float)
            mean = float(values.mean())
            median = float(values.median())
            min_value = float(values.min())
            max_value = float(values.max())
            stddev = float(values.std(ddof=1)) if len(values) > 1 else 0.0
            margin = _T_95_DF4 * stddev / math.sqrt(len(values)) if len(values) > 1 else 0.0
            # CI is not meaningful for HDR-derived latency percentiles (n=5 per-run
            # values are not exchangeable draws from a normal distribution).  Set
            # ci95_low/ci95_high to NaN for those metrics; keep CI for the others.
            if metric_name in _HDR_LATENCY_METRICS:
                ci_low: float = math.nan
                ci_high: float = math.nan
            else:
                ci_low = mean - margin
                ci_high = mean + margin
            rows.append(
                {
                    **base,
                    "repetition_count": repetition_count,
                    "metric_name": metric_name,
                    "mean": mean,
                    "median": median,
                    "stddev": stddev,
                    "min": min_value,
                    "max": max_value,
                    "ci95_low": ci_low,
                    "ci95_high": ci_high,
                }
            )
    out = pd.DataFrame(rows)
    if out.empty:
        return out
    return out.sort_values(
        ["scenario", "workload", "aggregate_rps", "technology", "metric_name"]
    ).reset_index(drop=True)


def _scenario_title(df: pd.DataFrame) -> str:
    scenarios = sorted(set(df["scenario"])) if not df.empty else []
    workloads = sorted(set(df["workload"])) if not df.empty else []
    if len(scenarios) == 1 and len(workloads) == 1:
        return f"{scenarios[0]} / {workloads[0]}"
    if len(scenarios) == 1:
        return scenarios[0]
    return "multiple scenarios"


def _summary_metric(summary_df: pd.DataFrame, metric_name: str) -> pd.DataFrame:
    if summary_df.empty:
        return summary_df
    return summary_df.loc[summary_df["metric_name"] == metric_name].copy()


def _metric_ticks(metric_df: pd.DataFrame) -> tuple[list[float], list[str]]:
    x_values = sorted(metric_df["aggregate_rps"].dropna().unique().tolist())
    labels: list[str] = []
    for x_value in x_values:
        subset = metric_df.loc[metric_df["aggregate_rps"] == x_value]
        per_node = float(subset["per_node_rps"].iloc[0])
        labels.append(f"{per_node:g}/node\n{x_value:g} agg")
    return x_values, labels


def _plot_metric_strip(
    repetition_df: pd.DataFrame,
    metric_name: str,
    out: Path,
    *,
    ylabel: str,
    title: str,
    warnings: list[str],
) -> None:
    """Strip plot: individual per-run dots at each load level, with a median line.

    Each dot is one repetition's value. The line connects the per-technology medians
    across load levels. No confidence interval is shown — the n=5 individual values
    speak for themselves.
    """
    if repetition_df.empty or metric_name not in repetition_df.columns:
        fig, ax = plt.subplots(figsize=(8.8, 4.3))
        _render_placeholder(ax, title, "No data available")
        _save_plot(fig, out)
        return

    col = pd.to_numeric(repetition_df[metric_name], errors="coerce")
    valid_df = repetition_df.loc[col.notna()].copy()
    valid_df[metric_name] = col.loc[col.notna()]
    if valid_df.empty:
        fig, ax = plt.subplots(figsize=(8.8, 4.3))
        _render_placeholder(ax, title, "No data available")
        _save_plot(fig, out)
        return

    ordered_technologies = _ordered_technologies(valid_df["technology"].tolist())
    x_values = sorted(valid_df["aggregate_rps"].dropna().unique().tolist())
    x_span = (x_values[-1] - x_values[0]) if len(x_values) > 1 else max(x_values[0], 1.0)
    n_tech = len(ordered_technologies)
    jitter_step = x_span * 0.012
    offsets = [jitter_step * (i - (n_tech - 1) / 2.0) for i in range(n_tech)]

    # Build tick labels using per_node_rps
    tick_labels: list[str] = []
    for xv in x_values:
        subset = valid_df.loc[valid_df["aggregate_rps"] == xv]
        per_node = float(subset["per_node_rps"].iloc[0])
        tick_labels.append(f"{per_node:g}/node\n{xv:g} agg")

    fig, ax = plt.subplots(figsize=(8.8, 4.3))
    any_series = False
    for i, technology in enumerate(ordered_technologies):
        tech_df = valid_df.loc[valid_df["technology"] == technology]
        if tech_df.empty:
            warnings.append(f"Missing {metric_name} series for {technology}; skipping")
            continue
        any_series = True
        color = _paper_color(technology)
        offset = offsets[i]
        medians_x: list[float] = []
        medians_y: list[float] = []
        for xv in x_values:
            group = tech_df.loc[tech_df["aggregate_rps"] == xv, metric_name]
            if group.empty:
                continue
            dot_x = xv + offset
            ax.scatter(
                [dot_x] * len(group),
                group.tolist(),
                color=color,
                alpha=0.65,
                s=28,
                zorder=3,
            )
            medians_x.append(dot_x)
            medians_y.append(float(group.median()))
        if medians_x:
            ax.plot(
                medians_x,
                medians_y,
                marker="D",
                markersize=5,
                linewidth=1.4,
                color=color,
                label=technology,
                zorder=4,
            )
    if not any_series:
        _render_placeholder(ax, title, "No data available")
        _save_plot(fig, out)
        return
    ax.set_xticks(x_values)
    ax.set_xticklabels(tick_labels)
    ax.set_xlabel("Load (per-node RPS / aggregate RPS)")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend(loc="best")
    _save_plot(fig, out)


def _plot_metric_line(
    summary_df: pd.DataFrame,
    metric_name: str,
    out: Path,
    *,
    ylabel: str,
    title: str,
    warnings: list[str],
    technologies: tuple[str, ...] | None = None,
) -> None:
    metric_df = _summary_metric(summary_df, metric_name)
    if technologies is not None:
        metric_df = metric_df.loc[metric_df["technology"].isin(technologies)].copy()
    fig, ax = plt.subplots(figsize=(8.8, 4.3))
    if metric_df.empty:
        _render_placeholder(ax, title, "No data available")
        _save_plot(fig, out)
        return
    x_values, tick_labels = _metric_ticks(metric_df)
    ordered_technologies = (
        [technology for technology in technologies if technology in set(metric_df["technology"])]
        if technologies is not None
        else _ordered_technologies(metric_df["technology"].tolist())
    )
    any_series = False
    range_label_added = False
    for technology in ordered_technologies:
        tech_df = metric_df.loc[metric_df["technology"] == technology].sort_values(
            "aggregate_rps"
        )
        if tech_df.empty:
            warnings.append(f"Missing {metric_name} series for {technology}; skipping")
            continue
        any_series = True
        xs = tech_df["aggregate_rps"].to_numpy(dtype=float)
        ys = tech_df["mean"].to_numpy(dtype=float)
        range_low = tech_df["min"].to_numpy(dtype=float)
        range_high = tech_df["max"].to_numpy(dtype=float)
        color = _paper_color(technology)
        ax.plot(xs, ys, marker="o", linewidth=1.4, color=color, label=technology)
        band_label = "Min/Max Range" if not range_label_added else None
        ax.fill_between(xs, range_low, range_high, color=color, alpha=0.18, label=band_label)
        range_label_added = True
    if not any_series:
        _render_placeholder(ax, title, "No data available")
        _save_plot(fig, out)
        return
    ax.set_xticks(x_values)
    ax.set_xticklabels(tick_labels)
    ax.set_xlabel("Load (per-node RPS / aggregate RPS)")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend(loc="best")
    _save_plot(fig, out)


def _plot_attempted_completed_chart(
    summary_df: pd.DataFrame,
    out: Path,
    *,
    title: str,
    warnings: list[str],
) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(11, 7), sharex=True)
    specs = (
        ("offered_rps", "Offered RPS"),
        ("attempted_rps", "Attempted RPS"),
        ("successful_rps", "Successful RPS"),
        ("error_rps", "Error RPS"),
    )
    for ax, (metric_name, ylabel) in zip(axes.flat, specs, strict=True):
        metric_df = _summary_metric(summary_df, metric_name)
        if metric_df.empty:
            _render_placeholder(ax, ylabel, "No data available")
            continue
        x_values, tick_labels = _metric_ticks(metric_df)
        for technology in _ordered_technologies(metric_df["technology"].tolist()):
            tech_df = metric_df.loc[metric_df["technology"] == technology].sort_values(
                "aggregate_rps"
            )
            if tech_df.empty:
                warnings.append(f"Missing {metric_name} series for {technology}; skipping")
                continue
            xs = tech_df["aggregate_rps"].to_numpy(dtype=float)
            ys = tech_df["mean"].to_numpy(dtype=float)
            color = _paper_color(technology)
            ax.plot(xs, ys, marker="o", linewidth=1.4, color=color, label=technology)
            if metric_name != "offered_rps":
                ax.fill_between(
                    xs,
                    tech_df["min"].to_numpy(dtype=float),
                    tech_df["max"].to_numpy(dtype=float),
                    color=color,
                    alpha=0.18,
                )
        ax.set_ylabel(ylabel)
        ax.set_xticks(x_values)
        ax.set_xticklabels(tick_labels)
        ax.grid(True, alpha=0.25)
    axes[0, 0].legend(loc="best")
    fig.suptitle(title)
    fig.tight_layout()
    fig.savefig(out, format="png")
    plt.close(fig)


def _plot_metric_boxplot(
    repetition_df: pd.DataFrame,
    metric_name: str,
    out: Path,
    *,
    ylabel: str,
    title: str,
    warnings: list[str],
) -> None:
    fig, ax = plt.subplots(figsize=(10.5, 4.8))
    groups = _boxplot_groups(repetition_df, metric_name)
    if not groups:
        _render_placeholder(ax, title, "No data available")
        _save_plot(fig, out)
        return
    positions: list[float] = []
    values: list[list[float]] = []
    colors: list[str] = []
    labels: list[str] = []
    for position, group in enumerate(groups, start=1):
        positions.append(float(position))
        values.append(group["values"])
        colors.append(_paper_color(group["technology"]))
        labels.append(group["label"])
    box = ax.boxplot(values, positions=positions, widths=0.6, patch_artist=True, showfliers=False)
    for patch, color in zip(box["boxes"], colors, strict=True):
        patch.set_facecolor(color)
        patch.set_alpha(0.35)
    for position, group, color in zip(positions, groups, colors, strict=True):
        jitter = np.linspace(-0.12, 0.12, max(len(group["values"]), 1))
        ax.scatter(
            position + jitter[: len(group["values"])],
            group["values"],
            color=color,
            s=18,
            zorder=3,
        )
    ax.set_xticks(positions)
    ax.set_xticklabels(labels, rotation=30, ha="right")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    legend_handles = [
        mpatches.Patch(color=_paper_color(name), label=name, alpha=0.35)
        for name in _ordered_technologies([group["technology"] for group in groups])
    ]
    ax.legend(handles=legend_handles, loc="best")
    _save_plot(fig, out)


def _ojp_metric_df(summary_df: pd.DataFrame, metric_name: str) -> pd.DataFrame:
    metric_df = _summary_metric(summary_df, metric_name)
    if metric_df.empty:
        return metric_df
    return metric_df.loc[metric_df["technology"] == "OJP"].copy()


def _plot_ojp_heap_metric_line(
    summary_df: pd.DataFrame,
    metric_name: str,
    out: Path,
    *,
    ylabel: str,
    title: str,
    warnings: list[str],
) -> bool:
    metric_df = _ojp_metric_df(summary_df, metric_name)
    if metric_df.empty:
        warnings.append(f"Missing {metric_name} series for OJP; skipping affected OJP heap graphs")
        return False
    x_values, tick_labels = _metric_ticks(metric_df)
    color = _paper_color("OJP")
    fig, ax = plt.subplots(figsize=(8.8, 4.3))
    tech_df = metric_df.sort_values("aggregate_rps")
    xs = tech_df["aggregate_rps"].to_numpy(dtype=float)
    ys = tech_df["mean"].to_numpy(dtype=float)
    ax.plot(xs, ys, marker="o", linewidth=1.4, color=color, label="OJP")
    ax.fill_between(
        xs,
        tech_df["min"].to_numpy(dtype=float),
        tech_df["max"].to_numpy(dtype=float),
        color=color,
        alpha=0.18,
    )
    ax.set_xticks(x_values)
    ax.set_xticklabels(tick_labels)
    ax.set_xlabel("Load (per-node RPS / aggregate RPS)")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend(loc="best")
    _save_plot(fig, out)
    return True


def _plot_ojp_heap_combined(
    summary_df: pd.DataFrame,
    out: Path,
    *,
    title: str,
    warnings: list[str],
) -> bool:
    metric_specs = (
        ("ojp_heap_used_mib", "Heap used (sum of per-node medians)", "-"),
        (
            "ojp_heap_committed_mib",
            "Heap committed (sum of per-node medians)",
            "--",
        ),
    )
    metric_frames = {name: _ojp_metric_df(summary_df, name) for name, _, _ in metric_specs}
    missing = [name for name, df in metric_frames.items() if df.empty]
    if missing:
        warnings.append(
            "Missing "
            + ", ".join(missing)
            + " series for OJP; skipping affected OJP heap graphs"
        )
        return False
    color = _paper_color("OJP")
    x_values, tick_labels = _metric_ticks(metric_frames["ojp_heap_used_mib"])
    fig, ax = plt.subplots(figsize=(8.8, 4.3))
    for metric_name, label, linestyle in metric_specs:
        metric_df = metric_frames[metric_name].sort_values("aggregate_rps")
        ax.plot(
            metric_df["aggregate_rps"].to_numpy(dtype=float),
            metric_df["mean"].to_numpy(dtype=float),
            marker="o",
            linewidth=1.4,
            linestyle=linestyle,
            color=color,
            label=label,
        )
    ax.set_xticks(x_values)
    ax.set_xticklabels(tick_labels)
    ax.set_xlabel("Load (per-node RPS / aggregate RPS)")
    ax.set_ylabel("Cluster OJP heap (MiB, sum of per-node medians)")
    ax.set_title(title)
    ax.legend(loc="best")
    _save_plot(fig, out)
    return True


def _plot_ojp_heap_per_node_boxplot(
    heap_node_df: pd.DataFrame,
    out: Path,
    *,
    title: str,
    warnings: list[str],
) -> bool:
    if heap_node_df.empty:
        warnings.append(
            "Missing ojp_heap_used_mib per-node series for OJP; "
            "skipping affected OJP heap graphs"
        )
        return False
    groups: list[dict[str, Any]] = []
    loads = (
        heap_node_df[["per_node_rps", "aggregate_rps"]]
        .drop_duplicates()
        .sort_values(["aggregate_rps", "per_node_rps"])
        .itertuples(index=False)
    )
    node_names = sorted(heap_node_df["node_name"].dropna().unique().tolist())
    for load in loads:
        for node_name in node_names:
            subset = heap_node_df.loc[
                (heap_node_df["per_node_rps"] == load.per_node_rps)
                & (heap_node_df["aggregate_rps"] == load.aggregate_rps)
                & (heap_node_df["node_name"] == node_name),
                "ojp_heap_used_mib",
            ]
            values = pd.to_numeric(subset, errors="coerce").dropna().tolist()
            if not values:
                continue
            groups.append(
                {
                    "label": f"{node_name}\n{load.per_node_rps:g}/node\n{load.aggregate_rps:g} agg",
                    "values": values,
                }
            )
    if not groups:
        warnings.append(
            "Missing ojp_heap_used_mib per-node series for OJP; "
            "skipping affected OJP heap graphs"
        )
        return False
    fig, ax = plt.subplots(figsize=(max(9.0, len(groups) * 0.8), 4.8))
    positions = [float(index) for index in range(1, len(groups) + 1)]
    color = _paper_color("OJP")
    box = ax.boxplot(
        [group["values"] for group in groups],
        positions=positions,
        widths=0.6,
        patch_artist=True,
        showfliers=False,
    )
    for patch in box["boxes"]:
        patch.set_facecolor(color)
        patch.set_alpha(0.35)
    for position, group in zip(positions, groups, strict=True):
        jitter = np.linspace(-0.12, 0.12, max(len(group["values"]), 1))
        ax.scatter(
            position + jitter[: len(group["values"])],
            group["values"],
            color=color,
            s=18,
            zorder=3,
        )
    ax.set_xticks(positions)
    ax.set_xticklabels([group["label"] for group in groups], rotation=30, ha="right")
    ax.set_ylabel("OJP heap used (MiB)")
    ax.set_title(title)
    ax.legend(handles=[mpatches.Patch(color=color, label="OJP", alpha=0.35)], loc="best")
    _save_plot(fig, out)
    return True


def _boxplot_groups(repetition_df: pd.DataFrame, metric_name: str) -> list[dict[str, Any]]:
    groups: list[dict[str, Any]] = []
    techs = (
        _ordered_technologies(repetition_df["technology"].tolist())
        if not repetition_df.empty
        else []
    )
    load_pairs = (
        repetition_df[["per_node_rps", "aggregate_rps"]]
        .drop_duplicates()
        .sort_values(["aggregate_rps", "per_node_rps"])
        .itertuples(index=False)
    )
    for per_node_rps, aggregate_rps in load_pairs:
        for technology in techs:
            subset = repetition_df.loc[
                (repetition_df["technology"] == technology)
                & (repetition_df["aggregate_rps"] == aggregate_rps)
                & (repetition_df["per_node_rps"] == per_node_rps),
                metric_name,
            ]
            values = pd.to_numeric(subset, errors="coerce").dropna().tolist()
            if not values:
                continue
            groups.append(
                {
                    "technology": technology,
                    "label": f"{technology}\n{per_node_rps:g}/node\n{aggregate_rps:g} agg",
                    "values": values,
                }
            )
    return groups


def _plot_error_type_breakdown(
    repetition_df: pd.DataFrame,
    out: Path,
    *,
    title: str,
    warnings: list[str],
) -> None:
    fig, ax = plt.subplots(figsize=(12, 5))
    if repetition_df.empty:
        _render_placeholder(ax, title, "No data available")
        _save_plot(fig, out)
        return
    group_cols = ["technology", "per_node_rps", "aggregate_rps"]
    category_columns = [f"error_count_{_slug_metric(category)}" for category in _ERROR_CATEGORIES]
    grouped = repetition_df.groupby(group_cols, sort=False)[category_columns].mean().reset_index()
    if grouped.empty:
        _render_placeholder(ax, title, "No data available")
        _save_plot(fig, out)
        return
    positions = np.arange(len(grouped))
    bottoms = np.zeros(len(grouped))
    color_map = plt.get_cmap("tab20")
    for index, category in enumerate(_ERROR_CATEGORIES):
        column = f"error_count_{_slug_metric(category)}"
        values = grouped[column].to_numpy(dtype=float)
        ax.bar(positions, values, bottom=bottoms, color=color_map(index), label=category)
        bottoms += values
    labels = [
        f"{row.technology}\n{row.per_node_rps:g}/node\n{row.aggregate_rps:g} agg"
        for row in grouped.itertuples(index=False)
    ]
    ax.set_xticks(positions)
    ax.set_xticklabels(labels, rotation=30, ha="right")
    ax.set_ylabel("Mean failed requests per repetition")
    ax.set_title(title)
    ax.legend(loc="upper right", fontsize=8)
    _save_plot(fig, out)


def _plot_slo_heatmap(
    summary_df: pd.DataFrame,
    out: Path,
    *,
    title: str,
    slo_p95_ms: float,
    slo_error_rate_pct: float,
) -> None:
    fig, ax = plt.subplots(figsize=(9.5, 3.5))
    p95_df = _summary_metric(summary_df, "p95_latency_ms")
    err_df = _summary_metric(summary_df, "error_rate_pct")
    if p95_df.empty or err_df.empty:
        _render_placeholder(ax, title, "No data available")
        _save_plot(fig, out)
        return
    merged = p95_df.merge(
        err_df[
            [
                "technology",
                "per_node_rps",
                "aggregate_rps",
                "mean",
            ]
        ].rename(columns={"mean": "error_rate_pct_mean"}),
        on=["technology", "per_node_rps", "aggregate_rps"],
        how="left",
    )
    techs = _ordered_technologies(merged["technology"].tolist())
    loads = (
        merged[["per_node_rps", "aggregate_rps"]]
        .drop_duplicates()
        .sort_values(["aggregate_rps", "per_node_rps"])
        .itertuples(index=False)
    )
    load_list = list(loads)
    for row_index, technology in enumerate(techs):
        for col_index, load in enumerate(load_list):
            subset = merged.loc[
                (merged["technology"] == technology)
                & (merged["per_node_rps"] == load.per_node_rps)
                & (merged["aggregate_rps"] == load.aggregate_rps)
            ]
            category = "pass"
            if not subset.empty:
                latency_fail = float(subset["mean"].iloc[0]) > slo_p95_ms
                error_fail = float(subset["error_rate_pct_mean"].iloc[0]) > slo_error_rate_pct
                if latency_fail and error_fail:
                    category = "fail both"
                elif latency_fail:
                    category = "fail latency"
                elif error_fail:
                    category = "fail error rate"
            rect = mpatches.Rectangle(
                (col_index, row_index),
                1,
                1,
                facecolor=_SLO_COLORS[category],
                edgecolor="white",
            )
            ax.add_patch(rect)
            ax.text(
                col_index + 0.5,
                row_index + 0.5,
                category,
                ha="center",
                va="center",
                fontsize=8,
            )
    ax.set_xlim(0, max(len(load_list), 1))
    ax.set_ylim(0, max(len(techs), 1))
    ax.invert_yaxis()
    ax.set_xticks(np.arange(len(load_list)) + 0.5)
    ax.set_xticklabels(
        [f"{load.per_node_rps:g}/node\n{load.aggregate_rps:g} agg" for load in load_list]
    )
    ax.set_yticks(np.arange(len(techs)) + 0.5)
    ax.set_yticklabels(techs)
    ax.set_title(title)
    legend_handles = [
        mpatches.Patch(color=color, label=label) for label, color in _SLO_COLORS.items()
    ]
    ax.legend(handles=legend_handles, loc="upper right", fontsize=8)
    _save_plot(fig, out)


def _paper_index_markdown() -> str:
    return "\n".join(
        [
            "# Main figures index",
            "",
            (
                "- `summary_stats.csv`: grouped summary by scenario, workload, technology, "
                "per_node_rps, aggregate_rps, and metric_name."
            ),
            (
                "- `repetition_values.csv`: one row per repetition/run with raw values used "
                "for main figures."
            ),
            (
                "- `throughput_vs_load.png`: `successful_rps` from `repetition_values.csv` "
                "(per-run dots with a median line; n=5 individual values per load level)."
            ),
            (
                "- `attempted_completed_success_error_rps.png`: `offered_rps`, "
                "`attempted_rps`, `successful_rps`, and `error_rps` from "
                "`summary_stats.csv`."
            ),
            "- `error_rate_vs_load.png`: `error_rate_pct` from `summary_stats.csv`.",
            (
                "- `p95_latency_vs_load.png`: `p95_latency_ms` from `repetition_values.csv` "
                "(HDR-derived; per-run dots with a median line; no CI)."
            ),
            (
                "- `p99_latency_vs_load.png`: `p99_latency_ms` from `repetition_values.csv` "
                "(HDR-derived; per-run dots with a median line; no CI)."
            ),
            (
                "- `mean_failed_latency_vs_load.png`: `mean_failed_latency_ms` from "
                "`summary_stats.csv`."
            ),
            "- `p95_latency_boxplot.png`: `p95_latency_ms` from `repetition_values.csv`.",
            "- `p99_latency_boxplot.png`: `p99_latency_ms` from `repetition_values.csv`.",
            "- `throughput_boxplot.png`: `successful_rps` from `repetition_values.csv`.",
            (
                "- `postgres_backend_connections_vs_load.png`: "
                "`postgres_backend_connections` from `summary_stats.csv`."
            ),
            (
                "- `rps_per_db_connection_vs_load.png`: `rps_per_db_connection` from "
                "`summary_stats.csv`."
            ),
            "- `postgres_cpu_vs_load.png`: `postgres_cpu_pct_avg` from `summary_stats.csv`.",
            "- `postgres_rss_vs_load.png`: `postgres_rss_mib` from `summary_stats.csv`.",
            (
                "- `proxy_tier_cpu_vs_load.png`: `proxy_tier_cpu_pct` from "
                "`summary_stats.csv` (per-run time-aligned sum across proxy/LB nodes; "
                "report line = mean across repetitions)."
            ),
            (
                "- `proxy_tier_rss_vs_load.png`: `proxy_tier_rss_mib` from "
                "`summary_stats.csv` (per-run time-aligned sum across proxy/LB nodes; "
                "report line = mean across repetitions)."
            ),
            (
                "- `ojp_heap_used_committed_vs_load.png`: `ojp_heap_used_mib` and "
                "`ojp_heap_committed_mib` from `summary_stats.csv` when OJP JVM "
                "heap data exists (cluster value = sum of per-node medians)."
            ),
            (
                "- `ojp_heap_utilisation_vs_load.png`: "
                "`ojp_heap_utilisation_percent` from `summary_stats.csv` when OJP JVM "
                "heap data exists."
            ),
            (
                "- `error_type_breakdown.png`: `error_count_*` columns from "
                "`repetition_values.csv` grouped by technology and load."
            ),
            (
                "- `slo_heatmap.png`: `p95_latency_ms` and `error_rate_pct` from "
                "`summary_stats.csv` compared against CLI SLO thresholds."
            ),
            (
                "- `GRAPH_RATIONALE.md`: explains why each main figure exists, including "
                "the OJP-specific heap diagnostics."
            ),
            "",
        ]
    )


def _graph_rationale_markdown() -> str:
    return "\n".join(
        [
            "# Graph rationale",
            "",
            "## How to read the latency and throughput strip plots",
            "",
            (
                "- `p95_latency_vs_load.png`, `p99_latency_vs_load.png`, and "
                "`throughput_vs_load.png` use per-run strip plots instead of mean ± CI. "
                "Each dot is the value from one of the n=5 repetitions. The line connects "
                "the per-technology medians across load levels."
            ),
            (
                "- All latency values in these charts are derived directly from merged "
                "HdrHistogram logs. HDR histograms record every individual request latency "
                "at full precision, so the per-run p95 and p99 values are exact percentiles "
                "of the observed request population, not estimates."
            ),
            (
                "- A t-distribution CI would assert that the five per-run HDR percentiles "
                "are exchangeable draws from a normal population. That assumption is not "
                "warranted: HDR-derived percentiles capture non-linear tail behaviour and "
                "can be bimodal under load variation. Showing the n=5 raw values is more "
                "honest and more informative."
            ),
            (
                "- `summary_stats.csv` records mean, median, stddev, min, and max for all "
                "metrics. The ci95_low and ci95_high columns are set to NaN for "
                "p95_latency_ms and p99_latency_ms for the reason above. CI is retained "
                "for throughput and other non-latency metrics."
            ),
            "",
            "## How to read the other line graphs",
            "",
            (
                "- The main line in a line graph is the mean across the five repetitions at "
                "that load level."
            ),
            (
                "- The shaded band above and below a line is the Min/Max Range: the absolute "
                "minimum and maximum values observed across the five repeated runs at that "
                "load level."
            ),
            (
                "- Narrower shaded bands mean the repetitions were more consistent. Wider "
                "bands mean the result moved around more from run to run."
            ),
            "",
            "## Where mean with Min/Max Range is used",
            "",
            (
                "- Mean with Min/Max Range is used in these report line graphs: "
                "`throughput_vs_load.png`, `error_rate_vs_load.png`, "
                "`p95_latency_vs_load.png`, `p99_latency_vs_load.png`, "
                "`mean_failed_latency_vs_load.png`, "
                "`postgres_backend_connections_vs_load.png`, "
                "`rps_per_db_connection_vs_load.png`, `postgres_cpu_vs_load.png`, "
                "`postgres_rss_vs_load.png`, `proxy_tier_cpu_vs_load.png`, "
                "`proxy_tier_rss_vs_load.png`, and `ojp_heap_utilisation_vs_load.png`."
            ),
            (
                "- Mean with Min/Max Range is also used in the measured panels of "
                "`attempted_completed_success_error_rps.png`: attempted RPS, successful RPS, "
                "and error RPS. The offered RPS panel does not show a shaded band "
                "because it is the configured target load, not an observed metric with run to "
                "run variation."
            ),
            (
                "- The combined OJP heap report graph "
                "(`ojp_heap_used_committed_vs_load.png`) shows mean lines without shaded "
                "bands to keep the two JVM series easy to compare on one view."
            ),
            (
                "- Boxplots, the error breakdown chart, and the SLO heatmap do not use mean "
                "with Min/Max Range because they are showing raw repetition spread, "
                "composition, or pass/fail status rather than one averaged line per load."
            ),
            (
                "- For `proxy_tier_cpu_vs_load.png` and `proxy_tier_rss_vs_load.png`, each run "
                "first time-aligns the proxy/LB node metrics and sums them across the tier. The "
                "report line then shows the mean of those per-run totals across repetitions, so "
                "the plotted value is not a per-node median."
            ),
            "",
            "## Core comparison figures",
            "",
            (
                "- `throughput_vs_load.png`: the top-level throughput view. It shows how much "
                "useful work each technology completes as load rises. Each dot is one run; "
                "the line is the per-technology median across runs."
            ),
            (
                "- `attempted_completed_success_error_rps.png`: separates target load, work "
                "actually attempted, work completed successfully, and work that failed so it is "
                "easy to see where a system starts falling behind."
            ),
            (
                "- `error_rate_vs_load.png`: the simplest reliability view. It shows when "
                "errors begin to grow with load."
            ),
            (
                "- `p95_latency_vs_load.png`: the main tail-latency view for normal service "
                "quality comparisons. Shows HDR-derived p95 per run (dots) with median line. "
                "All latency values are exact percentiles from merged HdrHistogram logs."
            ),
            (
                "- `p99_latency_vs_load.png`: a stricter tail-latency view that highlights "
                "worse outliers than p95. Uses the same per-run HDR strip-plot format."
            ),
            (
                "- `mean_failed_latency_vs_load.png`: shows how long failed requests took, which "
                "helps separate fast rejections from slow timeouts under load."
            ),
            (
                "- `p95_latency_boxplot.png`: shows the full repetition-to-repetition spread of "
                "p95 latency at each load, instead of only the average."
            ),
            (
                "- `p99_latency_boxplot.png`: shows the repetition spread for p99 latency so "
                "unstable tail behaviour is easier to spot."
            ),
            (
                "- `throughput_boxplot.png`: shows the repetition spread of successful "
                "throughput at each load."
            ),
            (
                "- `postgres_backend_connections_vs_load.png`: explains how much backend "
                "connection pressure reaches PostgreSQL as load rises."
            ),
            (
                "- `rps_per_db_connection_vs_load.png`: shows how efficiently each backend "
                "connection is being used."
            ),
            (
                "- `postgres_cpu_vs_load.png`: shows how much database CPU the workload costs."
            ),
            (
                "- `postgres_rss_vs_load.png`: shows the database memory footprint seen by the "
                "operating system."
            ),
            (
                "- `proxy_tier_cpu_vs_load.png`: shows total CPU cost across the "
                "proxy/application-tier nodes for technologies that actually have that tier."
            ),
            (
                "- `proxy_tier_rss_vs_load.png`: shows total RSS memory footprint across the "
                "proxy/application-tier nodes for technologies that actually have that tier."
            ),
            (
                "- `error_type_breakdown.png`: groups failures by kind so total error rate can "
                "be tied back to concrete failure modes."
            ),
            (
                "- `slo_heatmap.png`: gives a quick pass/fail view against the configured p95 "
                "latency and error-rate thresholds."
            ),
            "",
            "## OJP heap diagnostics",
            "",
            (
                "OJP runs on the JVM, so RSS alone can overstate live application memory pressure. "
                "Java may retain committed heap for reuse, which means high RSS does not "
                "necessarily mean high live object usage. For that reason, Stressum reports "
                "RSS, heap used, heap committed, and heap max separately. RSS shows memory "
                "reserved from the operating system. Heap used shows active Java object "
                "memory. Heap committed shows memory retained by the JVM for reuse. Heap "
                "max shows the configured JVM ceiling."
            ),
            "",
            (
                "- `ojp_heap_used_committed_vs_load.png`: keeps heap used and heap committed on "
                "the same graph so the gap between live object demand and JVM reserved space is "
                "easy to see. Each plotted value is the cluster total (sum of per-node medians)."
            ),
            (
                "- `ojp_heap_utilisation_vs_load.png`: shows how close OJP is to the "
                "configured JVM heap ceiling."
            ),
            (
                "- `debug/ojp_heap_per_node_boxplot.png`: shows whether one OJP node "
                "uses materially more heap than the others at the same load."
            ),
            "",
        ]
    )


def _missing_metric_warnings(row: dict[str, Any]) -> list[str]:
    warnings: list[str] = []
    for metric_name in (
        "postgres_backend_connections",
        "rps_per_db_connection",
        "postgres_cpu_pct_avg",
        "postgres_rss_mib",
    ):
        value = row.get(metric_name)
        if isinstance(value, float) and math.isnan(value):
            warnings.append(
                "Missing "
                f"{metric_name} for {row['label']}; affected main-figure series will be skipped"
            )
    return warnings


def _proxy_jvm_metric_paths(bundle: RunBundle) -> list[tuple[str, Path]]:
    paths: list[tuple[str, Path]] = []
    for key, path in sorted(bundle.node_metrics_csvs.items()):
        if "/proxy/" not in key or "jvm_metrics" not in key.lower():
            continue
        node_name = Path(key).name
        if node_name.endswith("_jvm_metrics.csv"):
            node_name = node_name[: -len("_jvm_metrics.csv")]
        else:
            node_name = Path(key).stem
        paths.append((node_name, path))
    return paths


def _median_metric(df: pd.DataFrame, columns: tuple[str, ...]) -> float | None:
    for column in columns:
        if column not in df.columns:
            continue
        values = pd.to_numeric(df[column], errors="coerce").dropna()
        if not values.empty:
            return float(values.median())
    return None


def _heap_max_mib_from_args(metadata: dict[str, Any], run_info: dict[str, Any]) -> float | None:
    candidates: list[str] = []
    for source in (
        run_info.get("jvmArgs"),
        metadata.get("jvmArgs"),
        (metadata.get("environment") or {}).get("jvmArgs"),
    ):
        if isinstance(source, str):
            candidates.append(source)
        elif isinstance(source, list):
            candidates.extend(str(item) for item in source)
    for arg in candidates:
        parsed = _parse_xmx_to_mib(arg)
        if parsed is not None:
            return parsed
    return None


def _parse_xmx_to_mib(arg: str) -> float | None:
    normalized = arg.strip()
    if not normalized.lower().startswith("-xmx"):
        return None
    raw_value = normalized[4:].strip()
    match = re.fullmatch(r"(?i)(\d+(?:\.\d+)?)([kmgt]?i?b?)?", raw_value)
    if match is None:
        return None
    magnitude = float(match.group(1))
    suffix = (match.group(2) or "").lower().rstrip("b")
    suffix = suffix[:-1] if suffix.endswith("i") else suffix
    factors = {
        "": 1.0 / (1024.0 * 1024.0),
        "k": 1.0 / 1024.0,
        "m": 1.0,
        "g": 1024.0,
        "t": 1024.0 * 1024.0,
    }
    factor = factors.get(suffix)
    if factor is None:
        return None
    return magnitude * factor


def _ojp_heap_metrics_for_scenario(
    base_row: dict[str, Any],
    *,
    bundle: RunBundle,
    run_info: dict[str, Any],
    metadata: dict[str, Any],
) -> tuple[dict[str, float], list[dict[str, Any]], list[str]]:
    label = str(base_row["label"])
    node_paths = _proxy_jvm_metric_paths(bundle)
    if not node_paths:
        return (
            {
                "ojp_heap_used_mib": math.nan,
                "ojp_heap_committed_mib": math.nan,
                "ojp_heap_max_mib": math.nan,
                "ojp_heap_utilisation_percent": math.nan,
            },
            [],
            [f"Missing OJP JVM heap metrics for {label}; skipping affected OJP heap graphs"],
        )
    fallback_heap_max = _heap_max_mib_from_args(metadata, run_info)
    per_node_rows: list[dict[str, Any]] = []
    warnings: list[str] = []
    missing_nodes: dict[str, list[str]] = {
        "ojp_heap_used_mib": [],
        "ojp_heap_committed_mib": [],
        "ojp_heap_max_mib": [],
    }
    aggregate_sums = {
        "ojp_heap_used_mib": 0.0,
        "ojp_heap_committed_mib": 0.0,
        "ojp_heap_max_mib": 0.0,
    }
    for node_name, path in node_paths:
        try:
            df = read_node_csv(path)
        except Exception:
            warnings.append(
                f"Could not read OJP JVM heap metrics for {label} ({node_name}); "
                "skipping affected OJP heap graphs"
            )
            missing_nodes["ojp_heap_used_mib"].append(node_name)
            missing_nodes["ojp_heap_committed_mib"].append(node_name)
            missing_nodes["ojp_heap_max_mib"].append(node_name)
            continue
        used_mib = _median_metric(df, ("heap_used_mib", "heap_used_mb"))
        committed_mib = _median_metric(df, ("heap_committed_mib", "heap_committed_mb"))
        heap_max_mib = _median_metric(df, ("heap_max_mib", "heap_max_mb"))
        if heap_max_mib is None:
            heap_max_mib = fallback_heap_max
        metric_values = {
            "ojp_heap_used_mib": used_mib,
            "ojp_heap_committed_mib": committed_mib,
            "ojp_heap_max_mib": heap_max_mib,
        }
        per_node_row = {
            key: base_row[key]
            for key in (
                "label",
                "run_dir",
                "scenario",
                "workload",
                "technology",
                "per_node_rps",
                "aggregate_rps",
            )
        }
        per_node_row["node_name"] = node_name
        per_node_row["ojp_heap_used_mib"] = (
            float(used_mib) if isinstance(used_mib, (int, float)) else math.nan
        )
        if isinstance(used_mib, (int, float)):
            per_node_rows.append(per_node_row)
        for metric_name, value in metric_values.items():
            if isinstance(value, (int, float)):
                aggregate_sums[metric_name] += float(value)
            else:
                missing_nodes[metric_name].append(node_name)
    aggregate_metrics: dict[str, float] = {}
    for metric_name, total in aggregate_sums.items():
        missing = missing_nodes[metric_name]
        if missing:
            metric_label = metric_name.removeprefix("ojp_").removesuffix("_mib").replace("_", " ")
            warnings.append(
                f"Missing OJP {metric_label} for {label} "
                f"({', '.join(sorted(set(missing)))}); skipping affected OJP heap graphs"
            )
            aggregate_metrics[metric_name] = math.nan
        else:
            aggregate_metrics[metric_name] = total
    heap_max_total = aggregate_metrics["ojp_heap_max_mib"]
    heap_used_total = aggregate_metrics["ojp_heap_used_mib"]
    if (
        isinstance(heap_max_total, float)
        and not math.isnan(heap_max_total)
        and heap_max_total > 0.0
    ):
        aggregate_metrics["ojp_heap_utilisation_percent"] = (
            heap_used_total / heap_max_total
        ) * 100.0
    else:
        aggregate_metrics["ojp_heap_utilisation_percent"] = math.nan
    return aggregate_metrics, per_node_rows, list(dict.fromkeys(warnings))


def _render_placeholder(ax: Any, title: str, text: str) -> None:
    ax.set_title(title)
    ax.text(0.5, 0.5, text, ha="center", va="center", transform=ax.transAxes)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)


def _save_plot(fig: Any, out: Path) -> None:
    fig.tight_layout()
    fig.savefig(out, format="png")
    plt.close(fig)


def _error_category(error_name: str) -> str:
    normalized = error_name.lower()
    if error_name == "SQLTransientConnectionException":
        return error_name
    if error_name == "SQLTransientException":
        return error_name
    if error_name == "StatusRuntimeException":
        return error_name
    if error_name == "SQLException":
        return error_name
    if "timeout" in normalized:
        return "timeout"
    if "acquisition" in normalized or "connection is not available" in normalized:
        return "connection acquisition failure"
    if "admission" in normalized:
        return "admission control failure"
    return "other"


def _slug_metric(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def _float_or_nan(value: Any) -> float:
    return float(value) if isinstance(value, (int, float)) else math.nan


def _float_or_zero(value: Any, technology: str) -> float:
    if isinstance(value, (int, float)):
        return float(value)
    if technology == "HikariCP":
        return 0.0
    return math.nan
