from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from stressum.aggregate import (
    is_open_loop,
    proxy_tier_cpu_timeseries,
    proxy_tier_host_cpu_timeseries,
)
from stressum.load import RunBundle, read_node_csv


def _slug(text: str, fallback: str = "unknown") -> str:
    slug = re.sub(r"[^\w\-]+", "_", text.strip(), flags=re.UNICODE)
    slug = re.sub(r"_+", "_", slug).strip("_")
    return slug or fallback


def _technology_from_label(label: str) -> str:
    stripped = label.strip()
    if not stripped:
        return "unknown"
    if " " in stripped:
        return stripped.rsplit(" ", 1)[0]
    return stripped


def _group_scenarios_by_technology(
    scenarios: list[dict[str, Any]],
) -> list[tuple[str, list[dict[str, Any]]]]:
    groups: dict[str, list[dict[str, Any]]] = {}
    order: list[str] = []
    for scenario in scenarios:
        technology = _technology_from_label(scenario["label"])
        if technology not in groups:
            groups[technology] = []
            order.append(technology)
        groups[technology].append(scenario)
    return [(technology, groups[technology]) for technology in order]


def _technology_bar_output_path(out_dir: Path, base: str, technology: str) -> Path:
    return out_dir / base / f"{base}__{_slug(technology)}.png"


def _bar_figsize(n_labels: int) -> tuple[float, float]:
    width = min(max(7.5, n_labels * 0.55), 14.0)
    return (width, 4.0)


def _short_bar_labels(labels: list[str], technology: str) -> list[str]:
    prefix = f"{technology} "
    if all(label.startswith(prefix) for label in labels):
        return [label[len(prefix) :] for label in labels]
    return labels


def _title_with_technology(title: str, technology: str | None) -> str:
    if technology:
        return f"{title} — {technology}"
    return title


def plot_comparison_throughput(
    labels: list[str],
    totals: list[float],
    out: Path,
    *,
    ylabel: str = "Successful throughput (sum of replicas, RPS)",
    title: str = "Successful throughput by scenario",
    technology: str | None = None,
    figsize: tuple[float, float] | None = None,
) -> None:
    fig, ax = plt.subplots(figsize=figsize or _bar_figsize(len(labels)))
    ax.bar(labels, totals, color="steelblue")
    ax.set_ylabel(ylabel)
    ax.set_title(_title_with_technology(title, technology))
    ax.tick_params(axis="x", rotation=25)
    fig.tight_layout()
    fig.savefig(out, format="png")
    plt.close(fig)


def plot_comparison_completed_throughput(
    labels: list[str],
    successful: list[float],
    errors: list[float],
    out: Path,
    *,
    technology: str | None = None,
    figsize: tuple[float, float] | None = None,
) -> None:
    fig, ax = plt.subplots(figsize=figsize or _bar_figsize(len(labels)))
    x = np.arange(len(labels))
    ax.bar(x, successful, label="Successful RPS", color="steelblue")
    ax.bar(x, errors, bottom=successful, label="Error RPS", color="coral")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=25)
    ax.set_ylabel("Completed throughput (sum of replicas, RPS)")
    ax.set_title(
        _title_with_technology(
            "Completed throughput by scenario (successful + error)",
            technology,
        )
    )
    ax.legend(loc="upper right", fontsize=8)
    fig.tight_layout()
    fig.savefig(out, format="png")
    plt.close(fig)


def _artifact_slug(label: str, bundle: RunBundle) -> str:
    return _slug(label, bundle.run_dir.name)


def _per_scenario_filename(base: str, label: str, bundle: RunBundle) -> str:
    return f"{base}__{_artifact_slug(label, bundle)}.png"


def _per_scenario_output_path(
    out_dir: Path, base: str, label: str, bundle: RunBundle
) -> Path:
    return out_dir / base / _per_scenario_filename(base, label, bundle)


def plot_comparison_latency_percentile(
    labels: list[str],
    values_ms: list[float],
    percentile: str,
    title: str,
    out: Path,
    *,
    technology: str | None = None,
    figsize: tuple[float, float] | None = None,
) -> None:
    fig, ax = plt.subplots(figsize=figsize or _bar_figsize(len(labels)))
    ax.bar(labels, values_ms, color="steelblue")
    ax.set_ylabel("Latency (ms)")
    ax.set_title(_title_with_technology(f"{title} — {percentile}", technology))
    ax.tick_params(axis="x", rotation=25)
    fig.tight_layout()
    fig.savefig(out, format="png")
    plt.close(fig)


def plot_comparison_total_successful_requests(
    labels: list[str],
    totals: list[int],
    out: Path,
    *,
    technology: str | None = None,
    figsize: tuple[float, float] | None = None,
) -> None:
    fig, ax = plt.subplots(figsize=figsize or _bar_figsize(len(labels)))
    ax.bar(labels, totals, color="steelblue")
    ax.set_ylabel("Total successful requests (sum of replicas)")
    ax.set_title(_title_with_technology("Total successful by scenario", technology))
    ax.tick_params(axis="x", rotation=25)
    fig.tight_layout()
    fig.savefig(out, format="png")
    plt.close(fig)


def plot_comparison_proxy_host_cpu_aligned_peak(
    labels: list[str],
    peaks_pct: list[float],
    out: Path,
    *,
    technology: str | None = None,
    figsize: tuple[float, float] | None = None,
) -> None:
    fig, ax = plt.subplots(figsize=figsize or _bar_figsize(len(labels)))
    ax.bar(labels, peaks_pct, color="slateblue")
    ax.set_ylabel("host_cpu aligned peak sum (%)")
    ax.set_title(
        _title_with_technology(
            "Proxy tier host CPU — time-aligned peak by scenario",
            technology,
        )
    )
    ax.tick_params(axis="x", rotation=25)
    fig.tight_layout()
    fig.savefig(out, format="png")
    plt.close(fig)


def plot_comparison_error_rate(
    labels: list[str],
    rates: list[float],
    out: Path,
    *,
    technology: str | None = None,
    figsize: tuple[float, float] | None = None,
) -> None:
    fig, ax = plt.subplots(figsize=figsize or _bar_figsize(len(labels)))
    ax.bar(labels, [r * 100.0 for r in rates], color="coral")
    ax.set_ylabel("Aggregate error rate (%)")
    ax.set_title(_title_with_technology("Errors by scenario", technology))
    ax.tick_params(axis="x", rotation=25)
    fig.tight_layout()
    fig.savefig(out, format="png")
    plt.close(fig)


def plot_comparison_open_loop_missed_opportunities(
    labels: list[str],
    missed: list[int],
    out: Path,
    *,
    technology: str | None = None,
    figsize: tuple[float, float] | None = None,
) -> None:
    fig, ax = plt.subplots(figsize=figsize or _bar_figsize(len(labels)))
    ax.bar(labels, missed, color="teal")
    ax.set_ylabel("Sum of openLoopMissedOpportunities")
    ax.set_title(_title_with_technology("Open loop — missed opportunities", technology))
    ax.tick_params(axis="x", rotation=25)
    fig.tight_layout()
    fig.savefig(out, format="png")
    plt.close(fig)


def plot_comparison_open_loop_scheduling_delay(
    labels: list[str],
    delay_ms: list[float],
    out: Path,
    *,
    technology: str | None = None,
    figsize: tuple[float, float] | None = None,
) -> None:
    fig, ax = plt.subplots(figsize=figsize or _bar_figsize(len(labels)))
    ax.bar(labels, delay_ms, color="slategray")
    ax.set_ylabel("Sum of openLoopSchedulingDelayMs")
    ax.set_title(_title_with_technology("Open loop — scheduling delay (ms)", technology))
    ax.tick_params(axis="x", rotation=25)
    fig.tight_layout()
    fig.savefig(out, format="png")
    plt.close(fig)


def _pick_pg_path(bundle: RunBundle) -> Path | None:
    for key, p in bundle.node_metrics_csvs.items():
        if key.endswith("pg_metrics.csv"):
            return p
    return None


def _pg_backends_series(path: Path) -> tuple[pd.Series, pd.Series] | None:
    df = read_node_csv(path)
    col = None
    for c in ("active_backends", "numbackends"):
        if c in df.columns:
            col = c
            break
    if col is None or "timestamp" not in df.columns:
        return None
    ts = pd.to_datetime(df["timestamp"], utc=True, errors="coerce")
    y = pd.to_numeric(df[col], errors="coerce")
    t0 = (ts - ts.min()).dt.total_seconds()
    return t0, y


def _pick_db_proc_path(bundle: RunBundle) -> Path | None:
    for key, p in sorted(bundle.node_metrics_csvs.items()):
        if key.endswith("db/db_proc_metrics.csv"):
            return p
    return None


def _db_proc_time_series(path: Path, column: str) -> tuple[pd.Series, pd.Series] | None:
    df = read_node_csv(path)
    if "timestamp" not in df.columns or column not in df.columns:
        return None
    ts = pd.to_datetime(df["timestamp"], utc=True, errors="coerce")
    y = pd.to_numeric(df[column], errors="coerce")
    t0 = (ts - ts.min()).dt.total_seconds()
    return t0, y


def _pick_jvm_path(bundle: RunBundle) -> Path | None:
    for key, p in sorted(bundle.node_metrics_csvs.items()):
        if "jvm_metrics" in key.lower():
            return p
    return None


def plot_scenario_pg_backends(label: str, bundle: RunBundle, out: Path) -> bool:
    p = _pick_pg_path(bundle)
    if p is None:
        return False
    pr = _pg_backends_series(p)
    if pr is None:
        return False
    t0, y = pr
    fig, ax = plt.subplots(figsize=(9, 2.8))
    ax.plot(t0, y, color="darkgreen", linewidth=0.8)
    ax.set_ylabel("backends")
    ax.set_xlabel("Time since run start (s)")
    ax.set_title(f"PostgreSQL backends (pg_metrics.csv) — {label}")
    fig.tight_layout()
    fig.savefig(out, format="png")
    plt.close(fig)
    return True


def _plot_scenario_db_proc_series(
    label: str,
    bundle: RunBundle,
    out: Path,
    *,
    column: str,
    ylabel: str,
    color: str,
    title: str,
) -> bool:
    p = _pick_db_proc_path(bundle)
    if p is None:
        return False
    pr = _db_proc_time_series(p, column)
    if pr is None:
        return False
    t0, y = pr
    fig, ax = plt.subplots(figsize=(9, 2.8))
    ax.plot(t0, y, color=color, linewidth=0.8)
    ax.set_ylabel(ylabel)
    ax.set_xlabel("Time since sample start (s)")
    ax.set_title(f"{title} — {label}")
    fig.tight_layout()
    fig.savefig(out, format="png")
    plt.close(fig)
    return True


def plot_scenario_postgres_process_cpu(label: str, bundle: RunBundle, out: Path) -> bool:
    return _plot_scenario_db_proc_series(
        label,
        bundle,
        out,
        column="cpu_pct",
        ylabel="cpu_pct (%)",
        color="darkorange",
        title="PostgreSQL server process CPU (db_proc_metrics.csv)",
    )


def plot_scenario_postgres_process_rss(label: str, bundle: RunBundle, out: Path) -> bool:
    return _plot_scenario_db_proc_series(
        label,
        bundle,
        out,
        column="rss_mb",
        ylabel="rss_mb",
        color="steelblue",
        title="PostgreSQL server process RSS (db_proc_metrics.csv)",
    )


def plot_scenario_jvm_heap(label: str, bundle: RunBundle, out: Path) -> bool:
    p = _pick_jvm_path(bundle)
    if p is None:
        return False
    df = read_node_csv(p)
    if "timestamp" not in df.columns or "heap_used_mb" not in df.columns:
        return False
    ts = pd.to_datetime(df["timestamp"], utc=True, errors="coerce")
    y = pd.to_numeric(df["heap_used_mb"], errors="coerce")
    t0 = (ts - ts.min()).dt.total_seconds()
    fig, ax = plt.subplots(figsize=(9, 2.8))
    ax.plot(t0, y, color="purple", linewidth=0.8)
    ax.set_ylabel("heap_used_mb")
    ax.set_xlabel("Time since sample start (s)")
    ax.set_title(f"OJP / JVM heap (first proxy jvm_metrics.csv per run) — {label}")
    fig.tight_layout()
    fig.savefig(out, format="png")
    plt.close(fig)
    return True


def plot_scenario_proxy_service_cpu_aligned_peak(
    label: str,
    bundle: RunBundle,
    out: Path,
    *,
    aligned_peak_pct: float | None = None,
) -> bool:
    ts = proxy_tier_cpu_timeseries(bundle)
    if ts is None:
        return False
    t0, tier_sum, peak = ts
    peak_pct = aligned_peak_pct if aligned_peak_pct is not None else peak
    fig, ax = plt.subplots(figsize=(9, 2.8))
    ax.plot(t0, tier_sum, color="darkorange", linewidth=0.8)
    ax.set_ylabel("service_cpu sum (%)")
    ax.set_xlabel("Time since sample start (s)")
    ax.set_title(
        f"Proxy tier CPU — time-aligned sum (aligned_peak={peak_pct:.1f}%) — {label}"
    )
    fig.tight_layout()
    fig.savefig(out, format="png")
    plt.close(fig)
    return True


def plot_scenario_proxy_host_cpu_aligned_peak(
    label: str,
    bundle: RunBundle,
    out: Path,
    *,
    aligned_peak_pct: float | None = None,
) -> bool:
    ts = proxy_tier_host_cpu_timeseries(bundle)
    if ts is None:
        return False
    t0, tier_sum, peak = ts
    peak_pct = aligned_peak_pct if aligned_peak_pct is not None else peak
    fig, ax = plt.subplots(figsize=(9, 2.8))
    ax.plot(t0, tier_sum, color="slateblue", linewidth=0.8)
    ax.set_ylabel("host_cpu sum (%)")
    ax.set_xlabel("Time since sample start (s)")
    ax.set_title(
        f"Proxy tier host CPU — time-aligned sum (aligned_peak={peak_pct:.1f}%) — {label}"
    )
    fig.tight_layout()
    fig.savefig(out, format="png")
    plt.close(fig)
    return True


def _combined_timeseries(bundle: RunBundle) -> pd.DataFrame | None:
    frames: list[pd.DataFrame] = []
    for rid in bundle.replica_ids:
        p = bundle.run_dir / f"replica-{rid}" / "timeseries.csv"
        if not p.is_file():
            continue
        df = pd.read_csv(p)
        if "timestamp_iso" not in df.columns:
            continue
        frames.append(df)
    if not frames:
        return None
    all_df = pd.concat(frames, ignore_index=True)
    all_df["timestamp_iso"] = pd.to_datetime(all_df["timestamp_iso"], utc=True, errors="coerce")
    g = (
        all_df.groupby("timestamp_iso")
        .agg(
            achieved_rps=("achieved_rps", "sum"),
            p99_ms=("p99_ms", "median"),
        )
        .reset_index()
    )
    g = g.sort_values("timestamp_iso")
    g["t_rel_s"] = (g["timestamp_iso"] - g["timestamp_iso"].min()).dt.total_seconds()
    return g


def plot_comparison_timeseries_rps_p99(
    scenarios: list[tuple[str, RunBundle]],
    out: Path,
) -> bool:
    data: list[tuple[str, pd.DataFrame]] = []
    for label, bundle in scenarios:
        g = _combined_timeseries(bundle)
        if g is not None and not g.empty:
            data.append((label, g))
    if not data:
        return False
    fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(9, 5.5), sharex=True)
    for label, g in data:
        ax0.plot(g["t_rel_s"], g["achieved_rps"], label=label, linewidth=0.9)
        ax1.plot(g["t_rel_s"], g["p99_ms"], label=label, linewidth=0.9)
    ax0.set_ylabel("Sum achieved RPS / s")
    ax0.set_title("Timeseries (not HDR): total RPS and median p99 across replicas")
    ax0.legend(loc="upper right", fontsize=8)
    ax0.grid(True, alpha=0.25)
    ax1.set_ylabel("Median p99 (ms)")
    ax1.set_xlabel("Time since run start (s)")
    ax1.legend(loc="upper right", fontsize=8)
    ax1.grid(True, alpha=0.25)
    fig.tight_layout()
    fig.savefig(out, format="png")
    plt.close(fig)
    return True


def _latency_percentiles_for_scenario(
    scenario: dict[str, Any],
) -> tuple[float, float, float, float]:
    merged = scenario.get("merged")
    agg = scenario["agg"]
    if merged is not None:
        return merged.p50_ms, merged.p95_ms, merged.p99_ms, merged.p999_ms
    return (
        float(agg.median_p50_ms or 0.0),
        float(agg.median_p95_ms or 0.0),
        float(agg.median_p99_ms or 0.0),
        float(agg.median_p999_ms or 0.0),
    )


def _open_loop_totals_for_scenario(scenario: dict[str, Any]) -> tuple[bool, int, float]:
    missed = 0
    delay = 0.0
    open_loop = False
    for summ in scenario["bundle"].summaries:
        ri = summ.get("runInfo") or {}
        if is_open_loop(ri):
            open_loop = True
        missed += int(ri.get("openLoopMissedOpportunities") or 0)
        v = ri.get("openLoopSchedulingDelayMs")
        if isinstance(v, (int, float)):
            delay += float(v)
    return open_loop, missed, delay


def _register_plot_path(paths: dict[str, Path], out: Path, out_dir: Path) -> None:
    paths[out.relative_to(out_dir).as_posix()] = out


def write_comparison_plots(
    scenarios: list[dict[str, Any]],
    out_dir: Path,
) -> dict[str, Path]:
    """scenarios: dicts with keys label, bundle, agg, merged (MergedLatency|None)."""
    paths: dict[str, Path] = {}

    hdr_all = all(s.get("merged") is not None for s in scenarios)
    hdr_any = any(s.get("merged") is not None for s in scenarios)
    if hdr_all:
        lat_title = "Latency percentiles (HDR merged across replicas)"
    elif hdr_any:
        lat_title = "Latency percentiles (HDR merged where available; else summary.json median)"
    else:
        lat_title = "Latency percentiles (median of per-replica summary.json)"

    for technology, group in _group_scenarios_by_technology(scenarios):
        raw_labels = [s["label"] for s in group]
        labels = _short_bar_labels(raw_labels, technology)
        successful_totals = [s["agg"].total_successful_rps for s in group]
        error_totals = [s["agg"].total_error_rps for s in group]
        p50, p95, p99, p999 = zip(
            *(_latency_percentiles_for_scenario(s) for s in group),
            strict=True,
        )

        tp = _technology_bar_output_path(out_dir, "comparison_total_throughput", technology)
        tp.parent.mkdir(parents=True, exist_ok=True)
        plot_comparison_throughput(
            labels,
            successful_totals,
            tp,
            technology=technology,
        )
        _register_plot_path(paths, tp, out_dir)

        cp = _technology_bar_output_path(out_dir, "comparison_total_completed_rps", technology)
        cp.parent.mkdir(parents=True, exist_ok=True)
        plot_comparison_completed_throughput(
            labels,
            successful_totals,
            error_totals,
            cp,
            technology=technology,
        )
        _register_plot_path(paths, cp, out_dir)

        for pct, series in (
            ("p50", list(p50)),
            ("p95", list(p95)),
            ("p99", list(p99)),
            ("p999", list(p999)),
        ):
            lp = _technology_bar_output_path(out_dir, f"comparison_latency_{pct}", technology)
            lp.parent.mkdir(parents=True, exist_ok=True)
            plot_comparison_latency_percentile(
                labels,
                series,
                pct,
                lat_title,
                lp,
                technology=technology,
            )
            _register_plot_path(paths, lp, out_dir)

        ep = _technology_bar_output_path(out_dir, "comparison_error_rate", technology)
        ep.parent.mkdir(parents=True, exist_ok=True)
        plot_comparison_error_rate(
            labels,
            [s["agg"].aggregate_error_rate for s in group],
            ep,
            technology=technology,
        )
        _register_plot_path(paths, ep, out_dir)

        sr = _technology_bar_output_path(
            out_dir,
            "comparison_total_successful_requests",
            technology,
        )
        sr.parent.mkdir(parents=True, exist_ok=True)
        plot_comparison_total_successful_requests(
            labels,
            [s["agg"].total_successful_requests for s in group],
            sr,
            technology=technology,
        )
        _register_plot_path(paths, sr, out_dir)

        host_cpu_peaks: list[float] = []
        for s in group:
            peak = (s.get("proxy_cpu") or {}).get("host_cpu_aligned_peak_pct")
            host_cpu_peaks.append(
                float(peak) if isinstance(peak, (int, float)) else float("nan")
            )
        if any(np.isfinite(p) for p in host_cpu_peaks):
            hp = _technology_bar_output_path(
                out_dir,
                "comparison_proxy_host_cpu_aligned_peak",
                technology,
            )
            hp.parent.mkdir(parents=True, exist_ok=True)
            plot_comparison_proxy_host_cpu_aligned_peak(
                labels,
                host_cpu_peaks,
                hp,
                technology=technology,
            )
            _register_plot_path(paths, hp, out_dir)

        missed_tot: list[int] = []
        delay_tot: list[float] = []
        group_open_any = False
        for s in group:
            open_loop, missed, delay = _open_loop_totals_for_scenario(s)
            missed_tot.append(missed)
            delay_tot.append(delay)
            if open_loop:
                group_open_any = True
        if group_open_any:
            missed_op = _technology_bar_output_path(
                out_dir,
                "comparison_open_loop_missed_opportunities",
                technology,
            )
            missed_op.parent.mkdir(parents=True, exist_ok=True)
            plot_comparison_open_loop_missed_opportunities(
                labels,
                missed_tot,
                missed_op,
                technology=technology,
            )
            _register_plot_path(paths, missed_op, out_dir)

            delay_op = _technology_bar_output_path(
                out_dir,
                "comparison_open_loop_scheduling_delay",
                technology,
            )
            delay_op.parent.mkdir(parents=True, exist_ok=True)
            plot_comparison_open_loop_scheduling_delay(
                labels,
                delay_tot,
                delay_op,
                technology=technology,
            )
            _register_plot_path(paths, delay_op, out_dir)

    per_scenario_plots: list[tuple[str, Any]] = [
        ("comparison_pg_numbackends", plot_scenario_pg_backends),
        ("comparison_postgres_process_cpu", plot_scenario_postgres_process_cpu),
        ("comparison_postgres_process_rss", plot_scenario_postgres_process_rss),
        ("comparison_jvm_heap", plot_scenario_jvm_heap),
    ]
    for s in scenarios:
        label = s["label"]
        bundle = s["bundle"]
        for base, plot_fn in per_scenario_plots:
            out = _per_scenario_output_path(out_dir, base, label, bundle)
            out.parent.mkdir(parents=True, exist_ok=True)
            if plot_fn(label, bundle, out):
                rel = out.relative_to(out_dir).as_posix()
                paths[rel] = out
        proxy_cpu = s.get("proxy_cpu")
        if proxy_cpu is not None:
            base = "comparison_proxy_service_cpu_aligned_peak"
            out = _per_scenario_output_path(out_dir, base, label, bundle)
            out.parent.mkdir(parents=True, exist_ok=True)
            if plot_scenario_proxy_service_cpu_aligned_peak(
                label,
                bundle,
                out,
                aligned_peak_pct=float(proxy_cpu["service_cpu_aligned_peak_pct"]),
            ):
                rel = out.relative_to(out_dir).as_posix()
                paths[rel] = out
            host_peak = proxy_cpu.get("host_cpu_aligned_peak_pct")
            if isinstance(host_peak, (int, float)):
                base = "comparison_proxy_host_cpu_aligned_peak"
                out = _per_scenario_output_path(out_dir, base, label, bundle)
                out.parent.mkdir(parents=True, exist_ok=True)
                if plot_scenario_proxy_host_cpu_aligned_peak(
                    label,
                    bundle,
                    out,
                    aligned_peak_pct=float(host_peak),
                ):
                    rel = out.relative_to(out_dir).as_posix()
                    paths[rel] = out

    ts = out_dir / "comparison_timeseries_rps_p99.png"
    if plot_comparison_timeseries_rps_p99([(s["label"], s["bundle"]) for s in scenarios], ts):
        paths["comparison_timeseries_rps_p99.png"] = ts

    return paths
