from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from stressum.chart_artifacts import save_chart_artifacts
from stressum.load import read_node_csv

# Fixed RNG so matplotlib/numpy-backed styling is reproducible across runs.
_PLOT_RNG_SEED = 0

if TYPE_CHECKING:
    from stressum.aggregate import RunAggregates
    from stressum.load import RunBundle


def apply_paper_style() -> None:
    np.random.seed(_PLOT_RNG_SEED)
    plt.rcParams.update(
        {
            "figure.dpi": 100,
            "savefig.dpi": 300,
            "font.size": 10,
            "axes.titlesize": 11,
            "axes.labelsize": 10,
            "legend.fontsize": 9,
            "figure.figsize": (7.5, 3.6),
            "axes.grid": True,
            "grid.alpha": 0.25,
        }
    )


def plot_throughput(agg: RunAggregates, out: Path) -> None:
    df = pd.DataFrame(agg.rows)
    fig, ax = plt.subplots()
    ax.bar(df["replica_id"].astype(str), df["achieved_throughput_rps"], color="steelblue")
    ax.axhline(
        agg.total_achieved_rps / max(len(df), 1),
        color="gray",
        linestyle="--",
        linewidth=1,
        label="mean per replica",
    )
    ax.set_xlabel("Replica")
    ax.set_ylabel("Achieved throughput (RPS)")
    ax.set_title("Per-replica achieved throughput")
    ax.legend(loc="upper right")
    save_chart_artifacts(fig, out)


def plot_latency_percentiles(agg: RunAggregates, out: Path) -> None:
    df = pd.DataFrame(agg.rows)
    labels = df["replica_id"].astype(str)
    x = range(len(df))
    width = 0.2
    fig, ax = plt.subplots(figsize=(max(8, len(df) * 0.6), 3.8))
    for i, col in enumerate(["p50_ms", "p95_ms", "p99_ms"]):
        vals = pd.to_numeric(df[col], errors="coerce").fillna(0)
        ax.bar([xi + (i - 1) * width for xi in x], vals, width=width, label=col.replace("_ms", ""))
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels)
    ax.set_xlabel("Replica")
    ax.set_ylabel("Latency (ms)")
    ax.set_title("Per-replica latency percentiles (from summary.json)")
    ax.legend(title="Percentile")
    save_chart_artifacts(fig, out)


def plot_error_rates(agg: RunAggregates, out: Path) -> None:
    df = pd.DataFrame(agg.rows)
    fig, ax = plt.subplots()
    ax.bar(df["replica_id"].astype(str), df["error_rate"] * 100.0, color="coral")
    ax.axhline(
        agg.aggregate_error_rate * 100.0,
        color="black",
        linestyle="-",
        linewidth=1.5,
        label="aggregate",
    )
    ax.set_xlabel("Replica")
    ax.set_ylabel("Error rate (%)")
    ax.set_title("Per-replica error rate vs aggregate (from counts)")
    ax.legend()
    save_chart_artifacts(fig, out)


def _pick_pg_path(bundle: RunBundle) -> Path | None:
    for key, p in bundle.node_metrics_csvs.items():
        if key.endswith("pg_metrics.csv"):
            return p
    return None


def _pick_jvm_path(bundle: RunBundle) -> Path | None:
    for key, p in sorted(bundle.node_metrics_csvs.items()):
        if "jvm_metrics" in key.lower():
            return p
    return None


def plot_pg_backends(bundle: RunBundle, out: Path) -> bool:
    p = _pick_pg_path(bundle)
    if p is None:
        return False
    df = read_node_csv(p)
    col = None
    for c in ("active_backends", "numbackends"):
        if c in df.columns:
            col = c
            break
    if col is None or "timestamp" not in df.columns:
        return False
    ts = pd.to_datetime(df["timestamp"], utc=True, errors="coerce")
    y = pd.to_numeric(df[col], errors="coerce")
    fig, ax = plt.subplots(figsize=(8, 3.2))
    ax.plot(ts, y, color="darkgreen", linewidth=0.8)
    ax.set_xlabel("Time (UTC)")
    ax.set_ylabel(col)
    ax.set_title("PostgreSQL node metric (from pg_metrics.csv)")
    fig.autofmt_xdate()
    save_chart_artifacts(fig, out)
    return True


def plot_jvm_heap(bundle: RunBundle, out: Path) -> bool:
    p = _pick_jvm_path(bundle)
    if p is None:
        return False
    df = read_node_csv(p)
    if "timestamp" not in df.columns or "heap_used_mb" not in df.columns:
        return False
    ts = pd.to_datetime(df["timestamp"], utc=True, errors="coerce")
    y = pd.to_numeric(df["heap_used_mb"], errors="coerce")
    fig, ax = plt.subplots(figsize=(8, 3.2))
    ax.plot(ts, y, color="purple", linewidth=0.8)
    ax.set_xlabel("Time (UTC)")
    ax.set_ylabel("heap_used_mb")
    ax.set_title(f"JVM heap (proxy) — {p.name}")
    fig.autofmt_xdate()
    save_chart_artifacts(fig, out)
    return True
