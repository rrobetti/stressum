from __future__ import annotations

from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from stressum.aggregate import is_open_loop
from stressum.load import RunBundle, read_node_csv


def plot_comparison_throughput(
    labels: list[str],
    totals: list[float],
    out: Path,
    *,
    ylabel: str = "Successful throughput (sum of replicas, RPS)",
    title: str = "Successful throughput by scenario",
) -> None:
    fig, ax = plt.subplots(figsize=(max(7.5, len(labels) * 0.9), 3.6))
    ax.bar(labels, totals, color="steelblue")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.tick_params(axis="x", rotation=25)
    fig.tight_layout()
    fig.savefig(out, format="png")
    plt.close(fig)


def plot_comparison_completed_throughput(
    labels: list[str],
    successful: list[float],
    errors: list[float],
    out: Path,
) -> None:
    fig, ax = plt.subplots(figsize=(max(7.5, len(labels) * 0.9), 3.6))
    x = np.arange(len(labels))
    ax.bar(x, successful, label="Successful RPS", color="steelblue")
    ax.bar(x, errors, bottom=successful, label="Error RPS", color="coral")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=25)
    ax.set_ylabel("Completed throughput (sum of replicas, RPS)")
    ax.set_title("Completed throughput by scenario (successful + error)")
    ax.legend(loc="upper right", fontsize=8)
    fig.tight_layout()
    fig.savefig(out, format="png")
    plt.close(fig)


def plot_comparison_proxy_service_cpu_aligned_peak(
    labels: list[str],
    aligned_peaks: list[float],
    out: Path,
) -> None:
    fig, ax = plt.subplots(figsize=(max(7.5, len(labels) * 0.9), 3.6))
    ax.bar(labels, aligned_peaks, color="darkorange")
    ax.set_ylabel("service_cpu aligned_peak (%)")
    ax.set_title("Proxy tier CPU — time-aligned peak sum")
    ax.tick_params(axis="x", rotation=25)
    fig.tight_layout()
    fig.savefig(out, format="png")
    plt.close(fig)


def plot_comparison_latency_percentile(
    labels: list[str],
    values_ms: list[float],
    percentile: str,
    title: str,
    out: Path,
) -> None:
    fig, ax = plt.subplots(figsize=(max(7.5, len(labels) * 0.9), 3.6))
    ax.bar(labels, values_ms, color="steelblue")
    ax.set_ylabel("Latency (ms)")
    ax.set_title(f"{title} — {percentile}")
    ax.tick_params(axis="x", rotation=25)
    fig.tight_layout()
    fig.savefig(out, format="png")
    plt.close(fig)


def plot_comparison_error_rate(labels: list[str], rates: list[float], out: Path) -> None:
    fig, ax = plt.subplots(figsize=(max(7.5, len(labels) * 0.9), 3.6))
    ax.bar(labels, [r * 100.0 for r in rates], color="coral")
    ax.set_ylabel("Aggregate error rate (%)")
    ax.set_title("Errors by scenario")
    ax.tick_params(axis="x", rotation=25)
    fig.tight_layout()
    fig.savefig(out, format="png")
    plt.close(fig)


def plot_comparison_open_loop(
    labels: list[str],
    missed: list[int],
    delay_ms: list[float],
    out: Path,
) -> None:
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(10, 3.8))
    ax0.bar(labels, missed, color="teal")
    ax0.set_ylabel("Sum of openLoopMissedOpportunities")
    ax0.set_title("Open loop — missed opportunities")
    ax0.tick_params(axis="x", rotation=25)
    ax1.bar(labels, delay_ms, color="slategray")
    ax1.set_ylabel("Sum of openLoopSchedulingDelayMs")
    ax1.set_title("Open loop — scheduling delay (ms)")
    ax1.tick_params(axis="x", rotation=25)
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


def plot_comparison_pg_backends(
    scenarios: list[tuple[str, RunBundle]],
    out: Path,
) -> bool:
    series_list: list[tuple[str, pd.Series, pd.Series]] = []
    for label, bundle in scenarios:
        p = _pick_pg_path(bundle)
        if p is None:
            continue
        pr = _pg_backends_series(p)
        if pr is None:
            continue
        t0, y = pr
        series_list.append((label, t0, y))
    if not series_list:
        return False
    n = len(series_list)
    fig, axes = plt.subplots(n, 1, figsize=(9, max(2.8, 2.4 * n)), sharex=False)
    if n == 1:
        axes = [axes]
    for ax, (label, t0, y) in zip(axes, series_list, strict=True):
        ax.plot(t0, y, color="darkgreen", linewidth=0.8)
        ax.set_ylabel("backends")
        ax.set_title(label)
    axes[-1].set_xlabel("Time since run start (s)")
    fig.suptitle("PostgreSQL backends (pg_metrics.csv)", y=1.02)
    fig.tight_layout()
    fig.savefig(out, format="png")
    plt.close(fig)
    return True


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


def _plot_comparison_db_proc_series(
    scenarios: list[tuple[str, RunBundle]],
    out: Path,
    *,
    column: str,
    ylabel: str,
    color: str,
    suptitle: str,
) -> bool:
    series_list: list[tuple[str, pd.Series, pd.Series]] = []
    for label, bundle in scenarios:
        p = _pick_db_proc_path(bundle)
        if p is None:
            continue
        pr = _db_proc_time_series(p, column)
        if pr is None:
            continue
        t0, y = pr
        series_list.append((label, t0, y))
    if not series_list:
        return False
    n = len(series_list)
    fig, axes = plt.subplots(n, 1, figsize=(9, max(2.8, 2.4 * n)))
    if n == 1:
        axes = [axes]
    for ax, (label, t0, y) in zip(axes, series_list, strict=True):
        ax.plot(t0, y, color=color, linewidth=0.8)
        ax.set_ylabel(ylabel)
        ax.set_title(label)
    axes[-1].set_xlabel("Time since sample start (s)")
    fig.suptitle(suptitle, y=1.02)
    fig.tight_layout()
    fig.savefig(out, format="png")
    plt.close(fig)
    return True


def plot_comparison_postgres_process_cpu(
    scenarios: list[tuple[str, RunBundle]],
    out: Path,
) -> bool:
    return _plot_comparison_db_proc_series(
        scenarios,
        out,
        column="cpu_pct",
        ylabel="cpu_pct (%)",
        color="darkorange",
        suptitle="PostgreSQL server process CPU (db_proc_metrics.csv)",
    )


def plot_comparison_postgres_process_rss(
    scenarios: list[tuple[str, RunBundle]],
    out: Path,
) -> bool:
    return _plot_comparison_db_proc_series(
        scenarios,
        out,
        column="rss_mb",
        ylabel="rss_mb",
        color="steelblue",
        suptitle="PostgreSQL server process RSS (db_proc_metrics.csv)",
    )


def _pick_jvm_path(bundle: RunBundle) -> Path | None:
    for key, p in sorted(bundle.node_metrics_csvs.items()):
        if "jvm_metrics" in key.lower():
            return p
    return None


def plot_comparison_jvm_heap(
    scenarios: list[tuple[str, RunBundle]],
    out: Path,
) -> bool:
    series_list: list[tuple[str, pd.Series, pd.Series]] = []
    for label, bundle in scenarios:
        p = _pick_jvm_path(bundle)
        if p is None:
            continue
        df = read_node_csv(p)
        if "timestamp" not in df.columns or "heap_used_mb" not in df.columns:
            continue
        ts = pd.to_datetime(df["timestamp"], utc=True, errors="coerce")
        y = pd.to_numeric(df["heap_used_mb"], errors="coerce")
        t0 = (ts - ts.min()).dt.total_seconds()
        series_list.append((label, t0, y))
    if not series_list:
        return False
    n = len(series_list)
    fig, axes = plt.subplots(n, 1, figsize=(9, max(2.8, 2.4 * n)))
    if n == 1:
        axes = [axes]
    for ax, (label, t0, y) in zip(axes, series_list, strict=True):
        ax.plot(t0, y, color="purple", linewidth=0.8)
        ax.set_ylabel("heap_used_mb")
        ax.set_title(label)
    axes[-1].set_xlabel("Time since sample start (s)")
    fig.suptitle("OJP / JVM heap (first proxy jvm_metrics.csv per run)", y=1.02)
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


def write_comparison_plots(
    scenarios: list[dict[str, Any]],
    out_dir: Path,
) -> dict[str, Path]:
    """scenarios: dicts with keys label, bundle, agg, merged (MergedLatency|None)."""
    paths: dict[str, Path] = {}
    labels = [s["label"] for s in scenarios]
    successful_totals = [s["agg"].total_successful_rps for s in scenarios]
    error_totals = [s["agg"].total_error_rps for s in scenarios]
    p50, p95, p99, p999 = [], [], [], []
    for s in scenarios:
        m = s.get("merged")
        agg = s["agg"]
        if m is not None:
            p50.append(m.p50_ms)
            p95.append(m.p95_ms)
            p99.append(m.p99_ms)
            p999.append(m.p999_ms)
        else:
            p50.append(float(agg.median_p50_ms or 0.0))
            p95.append(float(agg.median_p95_ms or 0.0))
            p99.append(float(agg.median_p99_ms or 0.0))
            p999.append(float(agg.median_p999_ms or 0.0))

    hdr_all = all(s.get("merged") is not None for s in scenarios)
    hdr_any = any(s.get("merged") is not None for s in scenarios)
    if hdr_all:
        lat_title = "Latency percentiles (HDR merged across replicas)"
    elif hdr_any:
        lat_title = "Latency percentiles (HDR merged where available; else summary.json median)"
    else:
        lat_title = "Latency percentiles (median of per-replica summary.json)"

    tp = out_dir / "comparison_total_throughput.png"
    plot_comparison_throughput(labels, successful_totals, tp)
    paths["comparison_total_throughput.png"] = tp

    cp = out_dir / "comparison_total_completed_rps.png"
    plot_comparison_completed_throughput(labels, successful_totals, error_totals, cp)
    paths["comparison_total_completed_rps.png"] = cp

    for pct, series in (
        ("p50", p50),
        ("p95", p95),
        ("p99", p99),
        ("p999", p999),
    ):
        fname = f"comparison_latency_{pct}.png"
        lp = out_dir / fname
        plot_comparison_latency_percentile(labels, series, pct, lat_title, lp)
        paths[fname] = lp

    ep = out_dir / "comparison_error_rate.png"
    plot_comparison_error_rate(labels, [s["agg"].aggregate_error_rate for s in scenarios], ep)
    paths["comparison_error_rate.png"] = ep

    open_any = False
    missed_tot: list[int] = []
    delay_tot: list[float] = []
    for s in scenarios:
        missed = 0
        delay = 0.0
        open_loop = False
        for summ in s["bundle"].summaries:
            ri = summ.get("runInfo") or {}
            if is_open_loop(ri):
                open_loop = True
            missed += int(ri.get("openLoopMissedOpportunities") or 0)
            v = ri.get("openLoopSchedulingDelayMs")
            if isinstance(v, (int, float)):
                delay += float(v)
        missed_tot.append(missed)
        delay_tot.append(delay)
        if open_loop:
            open_any = True
    if open_any:
        op = out_dir / "comparison_open_loop.png"
        plot_comparison_open_loop(labels, missed_tot, delay_tot, op)
        paths["comparison_open_loop.png"] = op

    proxy_labels: list[str] = []
    proxy_peaks: list[float] = []
    for s in scenarios:
        proxy_cpu = s.get("proxy_cpu")
        if proxy_cpu is None:
            continue
        proxy_labels.append(s["label"])
        proxy_peaks.append(float(proxy_cpu["service_cpu_aligned_peak_pct"]))
    if proxy_labels:
        pp = out_dir / "comparison_proxy_service_cpu_aligned_peak.png"
        plot_comparison_proxy_service_cpu_aligned_peak(proxy_labels, proxy_peaks, pp)
        paths["comparison_proxy_service_cpu_aligned_peak.png"] = pp

    pg = out_dir / "comparison_pg_numbackends.png"
    if plot_comparison_pg_backends([(s["label"], s["bundle"]) for s in scenarios], pg):
        paths["comparison_pg_numbackends.png"] = pg

    pg_cpu = out_dir / "comparison_postgres_process_cpu.png"
    if plot_comparison_postgres_process_cpu([(s["label"], s["bundle"]) for s in scenarios], pg_cpu):
        paths["comparison_postgres_process_cpu.png"] = pg_cpu

    pg_rss = out_dir / "comparison_postgres_process_rss.png"
    if plot_comparison_postgres_process_rss([(s["label"], s["bundle"]) for s in scenarios], pg_rss):
        paths["comparison_postgres_process_rss.png"] = pg_rss

    jvm = out_dir / "comparison_jvm_heap.png"
    if plot_comparison_jvm_heap([(s["label"], s["bundle"]) for s in scenarios], jvm):
        paths["comparison_jvm_heap.png"] = jvm

    ts = out_dir / "comparison_timeseries_rps_p99.png"
    if plot_comparison_timeseries_rps_p99([(s["label"], s["bundle"]) for s in scenarios], ts):
        paths["comparison_timeseries_rps_p99.png"] = ts

    return paths
