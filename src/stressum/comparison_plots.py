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


def _load_point_from_label(label: str) -> str:
    technology = _technology_from_label(label)
    prefix = f"{technology} "
    if label.startswith(prefix):
        return label[len(prefix) :]
    return label


def _group_scenarios_by_load_point(
    scenarios: list[dict[str, Any]],
) -> list[tuple[str, list[dict[str, Any]]]]:
    groups: dict[str, list[dict[str, Any]]] = {}
    order: list[str] = []
    for scenario in scenarios:
        load_point = _load_point_from_label(scenario["label"])
        if load_point not in groups:
            groups[load_point] = []
            order.append(load_point)
        groups[load_point].append(scenario)
    return [(load_point, groups[load_point]) for load_point in order]


def _cross_technology_plot_context(
    scenarios: list[dict[str, Any]],
) -> tuple[list[str], list[str], dict[tuple[str, str], dict[str, Any]]] | None:
    """
    Return (technologies, load_points, lookup) for cross-technology charts.

    lookup maps (load_point, technology) -> scenario dict.
    Returns None when fewer than two technologies share at least one load point.
    """
    technologies: list[str] = []
    load_points: list[str] = []
    lookup: dict[tuple[str, str], dict[str, Any]] = {}
    for scenario in scenarios:
        label = scenario["label"]
        technology = _technology_from_label(label)
        load_point = _load_point_from_label(label)
        if technology not in technologies:
            technologies.append(technology)
        if load_point not in load_points:
            load_points.append(load_point)
        lookup[(load_point, technology)] = scenario

    shared_load_points = [
        load_point
        for load_point in load_points
        if len(
            {
                _technology_from_label(s["label"])
                for s in scenarios
                if _load_point_from_label(s["label"]) == load_point
            }
        )
        >= 2
    ]
    if len(technologies) < 2 or not shared_load_points:
        return technologies, load_points, None

    filtered_lookup = {
        key: value
        for key, value in lookup.items()
        if key[0] in shared_load_points
    }
    return technologies, shared_load_points, filtered_lookup


_CROSS_TECH_COLORS = (
    "steelblue",
    "darkorange",
    "mediumseagreen",
    "coral",
    "slateblue",
    "teal",
)

_TECHNOLOGY_COLOR_MAP: dict[str, str] = {
    "OJP": "steelblue",
    "Hikari": "darkorange",
    "pgBouncer": "mediumseagreen",
}


def _technology_colors(technologies: list[str]) -> dict[str, str]:
    colors: dict[str, str] = {}
    fallback_index = 0
    for technology in technologies:
        if technology in _TECHNOLOGY_COLOR_MAP:
            colors[technology] = _TECHNOLOGY_COLOR_MAP[technology]
        else:
            colors[technology] = _CROSS_TECH_COLORS[fallback_index % len(_CROSS_TECH_COLORS)]
            fallback_index += 1
    return colors


def _color_for_label(label: str) -> str:
    technology = _technology_from_label(label)
    return _technology_colors([technology])[technology]


def _cross_tech_figsize(n_groups: int, n_technologies: int) -> tuple[float, float]:
    width = min(max(8.0, n_groups * max(1.1, n_technologies * 0.35)), 16.0)
    return (width, 4.2)


def _cross_tech_output_path(out_dir: Path, base: str) -> Path:
    return out_dir / f"{base}.png"


def _footprint_metric(scenario: dict[str, Any], key: str) -> float:
    footprint = scenario.get("total_footprint") or {}
    value = footprint.get(key)
    if isinstance(value, (int, float)):
        return float(value)
    return 0.0


def _write_total_footprint_cross_tech_charts(
    load_points: list[str],
    technologies: list[str],
    lookup: dict[tuple[str, str], dict[str, Any]],
    out_dir: Path,
    paths: dict[str, Path],
    *,
    _values: Any,
) -> None:
    chart_specs = (
        (
            "comparison_cross_tech_total_cpu_peak",
            "total_cpu_pct",
            "Total CPU peak (virtual core budget, %)",
            "Cross-technology total CPU peak by load point (bench + PostgreSQL + proxy/LB)",
            "comparison_cross_tech_throughput_total_cpu_peak",
            "Cross-technology throughput–total CPU peak curve",
        ),
        (
            "comparison_cross_tech_total_cpu_mean",
            "total_cpu_mean_pct",
            "Total CPU mean (virtual core budget, %)",
            "Cross-technology total CPU mean by load point (bench + PostgreSQL + proxy/LB)",
            "comparison_cross_tech_throughput_total_cpu_mean",
            "Cross-technology throughput–total CPU mean curve",
        ),
        (
            "comparison_cross_tech_total_cpu_p95",
            "total_cpu_p95_pct",
            "Total CPU p95 (virtual core budget, %)",
            "Cross-technology total CPU p95 by load point (bench + PostgreSQL + proxy/LB)",
            "comparison_cross_tech_throughput_total_cpu_p95",
            "Cross-technology throughput–total CPU p95 curve",
        ),
        (
            "comparison_cross_tech_total_rss_peak",
            "total_rss_mb_peak",
            "Total RSS peak (MB; excludes bench/LG)",
            "Cross-technology total RSS peak by load point (PostgreSQL + proxy/LB only)",
            "comparison_cross_tech_throughput_total_rss_peak",
            "Cross-technology throughput–total RSS peak curve",
        ),
        (
            "comparison_cross_tech_total_rss_mean",
            "total_rss_mb_mean",
            "Total RSS mean (MB; excludes bench/LG)",
            "Cross-technology total RSS mean by load point (PostgreSQL + proxy/LB only)",
            "comparison_cross_tech_throughput_total_rss_mean",
            "Cross-technology throughput–total RSS mean curve",
        ),
        (
            "comparison_cross_tech_total_rss_p95",
            "total_rss_mb_p95",
            "Total RSS p95 (MB; excludes bench/LG)",
            "Cross-technology total RSS p95 by load point (PostgreSQL + proxy/LB only)",
            "comparison_cross_tech_throughput_total_rss_p95",
            "Cross-technology throughput–total RSS p95 curve",
        ),
    )
    for base, metric_key, ylabel, title, curve_base, curve_title in chart_specs:
        out = _cross_tech_output_path(out_dir, base)
        out.parent.mkdir(parents=True, exist_ok=True)
        plot_cross_technology_grouped_bars(
            load_points,
            technologies,
            _values(lambda scenario, key=metric_key: _footprint_metric(scenario, key)),
            out,
            ylabel=ylabel,
            title=title,
        )
        _register_plot_path(paths, out, out_dir)
        _write_cross_technology_throughput_metric_curve(
            load_points,
            technologies,
            lookup,
            out_dir,
            paths,
            base=curve_base,
            metric_getter=lambda scenario, key=metric_key: _footprint_metric(scenario, key),
            ylabel=ylabel,
            title=curve_title,
        )


def plot_cross_technology_grouped_bars(
    load_points: list[str],
    technologies: list[str],
    values_by_load_point: dict[str, dict[str, float]],
    out: Path,
    *,
    ylabel: str,
    title: str,
    value_scale: float = 1.0,
    figsize: tuple[float, float] | None = None,
) -> None:
    colors = _technology_colors(technologies)
    n_groups = len(load_points)
    n_techs = len(technologies)
    x = np.arange(n_groups)
    width = min(0.8 / max(n_techs, 1), 0.28)
    fig, ax = plt.subplots(figsize=figsize or _cross_tech_figsize(n_groups, n_techs))
    for index, technology in enumerate(technologies):
        offsets = x + (index - (n_techs - 1) / 2) * width
        heights = [
            values_by_load_point.get(load_point, {}).get(technology, np.nan)
            for load_point in load_points
        ]
        scaled = [height * value_scale if np.isfinite(height) else np.nan for height in heights]
        ax.bar(
            offsets,
            scaled,
            width,
            label=technology,
            color=colors[technology],
        )
    ax.set_xticks(x)
    ax.set_xticklabels(load_points, rotation=25)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend(loc="upper right", fontsize=8)
    fig.tight_layout()
    fig.savefig(out, format="png")
    plt.close(fig)


def plot_cross_technology_completed_throughput(
    load_points: list[str],
    technologies: list[str],
    successful_by_load_point: dict[str, dict[str, float]],
    errors_by_load_point: dict[str, dict[str, float]],
    out: Path,
    *,
    figsize: tuple[float, float] | None = None,
) -> None:
    colors = _technology_colors(technologies)
    n_groups = len(load_points)
    n_techs = len(technologies)
    x = np.arange(n_groups)
    width = min(0.8 / max(n_techs, 1), 0.28)
    fig, ax = plt.subplots(figsize=figsize or _cross_tech_figsize(n_groups, n_techs))
    for index, technology in enumerate(technologies):
        offsets = x + (index - (n_techs - 1) / 2) * width
        successful = [
            successful_by_load_point.get(load_point, {}).get(technology, np.nan)
            for load_point in load_points
        ]
        errors = [
            errors_by_load_point.get(load_point, {}).get(technology, np.nan)
            for load_point in load_points
        ]
        ax.bar(
            offsets,
            successful,
            width,
            label=f"{technology} successful",
            color=colors[technology],
        )
        ax.bar(
            offsets,
            errors,
            width,
            bottom=successful,
            color=colors[technology],
            alpha=0.45,
            hatch="//",
        )
    ax.set_xticks(x)
    ax.set_xticklabels(load_points, rotation=25)
    ax.set_ylabel("Completed throughput (sum of replicas, RPS)")
    ax.set_title("Cross-technology completed throughput by load point (successful + error)")
    handles, labels = ax.get_legend_handles_labels()
    deduped: dict[str, Any] = {}
    for handle, label in zip(handles, labels, strict=True):
        tech = label.removesuffix(" successful")
        if tech not in deduped:
            deduped[tech] = handle
    ax.legend(deduped.values(), deduped.keys(), loc="upper right", fontsize=8)
    fig.tight_layout()
    fig.savefig(out, format="png")
    plt.close(fig)


def plot_cross_technology_throughput_metric_curve(
    technologies: list[str],
    points_by_technology: dict[str, list[tuple[float, float]]],
    out: Path,
    *,
    ylabel: str,
    title: str,
    log_y_scale: bool = False,
    figsize: tuple[float, float] | None = None,
) -> None:
    colors = _technology_colors(technologies)
    fig, ax = plt.subplots(figsize=figsize or (9.0, 4.2))
    for technology in technologies:
        series = sorted(points_by_technology.get(technology, []), key=lambda item: item[0])
        if not series:
            continue
        xs, ys = zip(*series, strict=True)
        ax.plot(xs, ys, marker="o", linewidth=1.2, label=technology, color=colors[technology])
    ax.set_xlabel("Target RPS (aggregate)")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    if log_y_scale:
        ax.set_yscale("log")
    ax.legend(loc="upper left", fontsize=8)
    ax.grid(True, which="both", alpha=0.25)
    fig.tight_layout()
    fig.savefig(out, format="png")
    plt.close(fig)


def plot_cross_technology_throughput_latency_curve(
    technologies: list[str],
    points_by_technology: dict[str, list[tuple[float, float]]],
    out: Path,
    *,
    percentile: str,
    figsize: tuple[float, float] | None = None,
) -> None:
    plot_cross_technology_throughput_metric_curve(
        technologies,
        points_by_technology,
        out,
        ylabel=f"{percentile} latency (ms)",
        title=f"Cross-technology throughput–latency curve ({percentile})",
        log_y_scale=True,
        figsize=figsize,
    )


def _target_rps_for_scenario(scenario: dict[str, Any]) -> float | None:
    summaries = scenario["bundle"].summaries
    if not summaries:
        return None
    run_info = summaries[0].get("runInfo") or {}
    target = run_info.get("targetRps")
    if isinstance(target, (int, float)):
        return float(target)
    return None


def _postgres_process_metric(
    scenario: dict[str, Any],
    key: str,
) -> float | None:
    value = (scenario.get("postgres_process") or {}).get(key)
    if isinstance(value, (int, float)):
        return float(value)
    return None


def _throughput_metric_curve_points(
    load_points: list[str],
    technologies: list[str],
    lookup: dict[tuple[str, str], dict[str, Any]],
    metric_getter: Any,
) -> dict[str, list[tuple[float, float]]]:
    curve_points: dict[str, list[tuple[float, float]]] = {
        technology: [] for technology in technologies
    }
    for load_point in load_points:
        for technology in technologies:
            scenario = lookup.get((load_point, technology))
            if scenario is None:
                continue
            target_rps = _target_rps_for_scenario(scenario)
            metric = metric_getter(scenario)
            if target_rps is None or metric is None:
                continue
            curve_points[technology].append((target_rps, metric))
    return curve_points


def _write_cross_technology_throughput_metric_curve(
    load_points: list[str],
    technologies: list[str],
    lookup: dict[tuple[str, str], dict[str, Any]],
    out_dir: Path,
    paths: dict[str, Path],
    *,
    base: str,
    metric_getter: Any,
    ylabel: str,
    title: str,
) -> None:
    curve_points = _throughput_metric_curve_points(
        load_points,
        technologies,
        lookup,
        metric_getter,
    )
    if not any(curve_points[technology] for technology in technologies):
        return
    out = _cross_tech_output_path(out_dir, base)
    out.parent.mkdir(parents=True, exist_ok=True)
    plot_cross_technology_throughput_metric_curve(
        technologies,
        curve_points,
        out,
        ylabel=ylabel,
        title=title,
    )
    _register_plot_path(paths, out, out_dir)


def _write_cross_technology_plots(
    scenarios: list[dict[str, Any]],
    out_dir: Path,
    paths: dict[str, Path],
    *,
    lat_title: str,
) -> None:
    technologies, load_points, lookup = _cross_technology_plot_context(scenarios)
    if lookup is None:
        return

    def _values(getter: Any) -> dict[str, dict[str, float]]:
        values: dict[str, dict[str, float]] = {}
        for load_point in load_points:
            values[load_point] = {}
            for technology in technologies:
                scenario = lookup.get((load_point, technology))
                if scenario is None:
                    continue
                values[load_point][technology] = float(getter(scenario))
        return values

    throughput_values = _values(lambda scenario: scenario["agg"].total_successful_rps)
    out = _cross_tech_output_path(out_dir, "comparison_cross_tech_total_throughput")
    out.parent.mkdir(parents=True, exist_ok=True)
    plot_cross_technology_grouped_bars(
        load_points,
        technologies,
        throughput_values,
        out,
        ylabel="Successful throughput (sum of replicas, RPS)",
        title="Cross-technology successful throughput by load point",
    )
    _register_plot_path(paths, out, out_dir)

    successful_values = throughput_values
    error_values = _values(lambda scenario: scenario["agg"].total_error_rps)
    out = _cross_tech_output_path(out_dir, "comparison_cross_tech_total_completed_rps")
    out.parent.mkdir(parents=True, exist_ok=True)
    plot_cross_technology_completed_throughput(
        load_points,
        technologies,
        successful_values,
        error_values,
        out,
    )
    _register_plot_path(paths, out, out_dir)

    for pct, getter in (
        ("p50", lambda scenario: _latency_percentiles_for_scenario(scenario)[0]),
        ("p95", lambda scenario: _latency_percentiles_for_scenario(scenario)[1]),
        ("p99", lambda scenario: _latency_percentiles_for_scenario(scenario)[2]),
        ("p999", lambda scenario: _latency_percentiles_for_scenario(scenario)[3]),
    ):
        out = _cross_tech_output_path(out_dir, f"comparison_cross_tech_latency_{pct}")
        out.parent.mkdir(parents=True, exist_ok=True)
        plot_cross_technology_grouped_bars(
            load_points,
            technologies,
            _values(getter),
            out,
            ylabel="Latency (ms)",
            title=f"Cross-technology {lat_title} — {pct}",
        )
        _register_plot_path(paths, out, out_dir)

    out = _cross_tech_output_path(out_dir, "comparison_cross_tech_error_rate")
    out.parent.mkdir(parents=True, exist_ok=True)
    plot_cross_technology_grouped_bars(
        load_points,
        technologies,
        _values(lambda scenario: scenario["agg"].aggregate_error_rate),
        out,
        ylabel="Aggregate error rate (%)",
        title="Cross-technology error rate by load point",
        value_scale=100.0,
    )
    _register_plot_path(paths, out, out_dir)

    out = _cross_tech_output_path(out_dir, "comparison_cross_tech_total_successful_requests")
    out.parent.mkdir(parents=True, exist_ok=True)
    plot_cross_technology_grouped_bars(
        load_points,
        technologies,
        _values(lambda scenario: float(scenario["agg"].total_successful_requests)),
        out,
        ylabel="Total successful requests (sum of replicas)",
        title="Cross-technology total successful requests by load point",
    )
    _register_plot_path(paths, out, out_dir)

    host_cpu_values: dict[str, dict[str, float]] = {}
    host_cpu_any = False
    for load_point in load_points:
        host_cpu_values[load_point] = {}
        for technology in technologies:
            scenario = lookup.get((load_point, technology))
            if scenario is None:
                continue
            peak = (scenario.get("proxy_cpu") or {}).get("host_cpu_aligned_peak_pct")
            if isinstance(peak, (int, float)):
                host_cpu_values[load_point][technology] = float(peak)
                host_cpu_any = True
    if host_cpu_any:
        out = _cross_tech_output_path(out_dir, "comparison_cross_tech_proxy_host_cpu_aligned_peak")
        out.parent.mkdir(parents=True, exist_ok=True)
        plot_cross_technology_grouped_bars(
            load_points,
            technologies,
            host_cpu_values,
            out,
            ylabel="host_cpu aligned peak sum (%)",
            title="Cross-technology proxy tier host CPU peak by load point",
        )
        _register_plot_path(paths, out, out_dir)

    postgres_cpu_values: dict[str, dict[str, float]] = {}
    postgres_rss_values: dict[str, dict[str, float]] = {}
    postgres_any = False
    for load_point in load_points:
        postgres_cpu_values[load_point] = {}
        postgres_rss_values[load_point] = {}
        for technology in technologies:
            scenario = lookup.get((load_point, technology))
            if scenario is None:
                continue
            cpu_peak = _postgres_process_metric(scenario, "cpu_pct_peak")
            rss_peak = _postgres_process_metric(scenario, "rss_mb_peak")
            if cpu_peak is not None:
                postgres_cpu_values[load_point][technology] = cpu_peak
                postgres_any = True
            if rss_peak is not None:
                postgres_rss_values[load_point][technology] = rss_peak
                postgres_any = True
    if postgres_any:
        out = _cross_tech_output_path(out_dir, "comparison_cross_tech_postgres_process_cpu_peak")
        out.parent.mkdir(parents=True, exist_ok=True)
        plot_cross_technology_grouped_bars(
            load_points,
            technologies,
            postgres_cpu_values,
            out,
            ylabel="PostgreSQL process CPU peak (%)",
            title="Cross-technology PostgreSQL process CPU peak by load point",
        )
        _register_plot_path(paths, out, out_dir)

        out = _cross_tech_output_path(out_dir, "comparison_cross_tech_postgres_process_rss_peak")
        out.parent.mkdir(parents=True, exist_ok=True)
        plot_cross_technology_grouped_bars(
            load_points,
            technologies,
            postgres_rss_values,
            out,
            ylabel="PostgreSQL process RSS peak (MB)",
            title="Cross-technology PostgreSQL process RSS peak by load point",
        )
        _register_plot_path(paths, out, out_dir)

        _write_cross_technology_throughput_metric_curve(
            load_points,
            technologies,
            lookup,
            out_dir,
            paths,
            base="comparison_cross_tech_throughput_postgres_cpu",
            metric_getter=lambda scenario: _postgres_process_metric(scenario, "cpu_pct_peak"),
            ylabel="PostgreSQL process CPU peak (%)",
            title="Cross-technology throughput–PostgreSQL CPU curve",
        )
        _write_cross_technology_throughput_metric_curve(
            load_points,
            technologies,
            lookup,
            out_dir,
            paths,
            base="comparison_cross_tech_throughput_postgres_rss",
            metric_getter=lambda scenario: _postgres_process_metric(scenario, "rss_mb_peak"),
            ylabel="PostgreSQL process RSS peak (MB)",
            title="Cross-technology throughput–PostgreSQL RSS curve",
        )

    footprint_any = any(
        lookup.get((load_point, technology), {}).get("total_footprint") is not None
        for load_point in load_points
        for technology in technologies
    )
    if footprint_any:
        _write_total_footprint_cross_tech_charts(
            load_points,
            technologies,
            lookup,
            out_dir,
            paths,
            _values=_values,
        )

    open_loop_any = False
    missed_values: dict[str, dict[str, float]] = {}
    delay_values: dict[str, dict[str, float]] = {}
    for load_point in load_points:
        missed_values[load_point] = {}
        delay_values[load_point] = {}
        for technology in technologies:
            scenario = lookup.get((load_point, technology))
            if scenario is None:
                continue
            open_loop, missed, delay = _open_loop_totals_for_scenario(scenario)
            if open_loop:
                open_loop_any = True
            missed_values[load_point][technology] = float(missed)
            delay_values[load_point][technology] = delay
    if open_loop_any:
        out = _cross_tech_output_path(
            out_dir,
            "comparison_cross_tech_open_loop_missed_opportunities",
        )
        out.parent.mkdir(parents=True, exist_ok=True)
        plot_cross_technology_grouped_bars(
            load_points,
            technologies,
            missed_values,
            out,
            ylabel="Sum of openLoopMissedOpportunities",
            title="Cross-technology open loop missed opportunities by load point",
        )
        _register_plot_path(paths, out, out_dir)

        out = _cross_tech_output_path(
            out_dir,
            "comparison_cross_tech_open_loop_scheduling_delay",
        )
        out.parent.mkdir(parents=True, exist_ok=True)
        plot_cross_technology_grouped_bars(
            load_points,
            technologies,
            delay_values,
            out,
            ylabel="Sum of openLoopSchedulingDelayMs",
            title="Cross-technology open loop scheduling delay by load point",
        )
        _register_plot_path(paths, out, out_dir)

    curve_points = _throughput_metric_curve_points(
        load_points,
        technologies,
        lookup,
        lambda scenario: _latency_percentiles_for_scenario(scenario)[1],
    )
    if any(curve_points[technology] for technology in technologies):
        out = _cross_tech_output_path(
            out_dir,
            "comparison_cross_tech_throughput_latency_p95",
        )
        out.parent.mkdir(parents=True, exist_ok=True)
        plot_cross_technology_throughput_latency_curve(
            technologies,
            curve_points,
            out,
            percentile="p95",
        )
        _register_plot_path(paths, out, out_dir)

    curve_points_p99 = _throughput_metric_curve_points(
        load_points,
        technologies,
        lookup,
        lambda scenario: _latency_percentiles_for_scenario(scenario)[2],
    )
    if any(curve_points_p99[technology] for technology in technologies):
        out = _cross_tech_output_path(
            out_dir,
            "comparison_cross_tech_throughput_latency_p99",
        )
        out.parent.mkdir(parents=True, exist_ok=True)
        plot_cross_technology_throughput_latency_curve(
            technologies,
            curve_points_p99,
            out,
            percentile="p99",
        )
        _register_plot_path(paths, out, out_dir)


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


def _technology_bar_color(technology: str | None) -> str:
    if technology is None:
        return "steelblue"
    return _technology_colors([technology])[technology]


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
    ax.bar(labels, totals, color=_technology_bar_color(technology))
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
    bar_color = _technology_bar_color(technology)
    ax.bar(x, successful, label="Successful RPS", color=bar_color)
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
    ax.bar(labels, values_ms, color=_technology_bar_color(technology))
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
    ax.bar(labels, totals, color=_technology_bar_color(technology))
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
        color = _color_for_label(label)
        ax0.plot(g["t_rel_s"], g["achieved_rps"], label=label, linewidth=0.9, color=color)
        ax1.plot(g["t_rel_s"], g["p99_ms"], label=label, linewidth=0.9, color=color)
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

    tech_groups = list(_group_scenarios_by_technology(scenarios))
    for tech_idx, (technology, group) in enumerate(tech_groups, start=1):
        print(
            f"  Technology charts [{tech_idx}/{len(tech_groups)}]: "
            f"{technology} ({len(group)} scenario(s))",
            flush=True,
        )
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
    print(f"  Per-scenario charts ({len(scenarios)} scenario(s))...", flush=True)
    for scenario_idx, s in enumerate(scenarios, start=1):
        label = s["label"]
        bundle = s["bundle"]
        print(f"    [{scenario_idx}/{len(scenarios)}] {label}", flush=True)
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

    print("  Cross-technology charts...", flush=True)
    _write_cross_technology_plots(scenarios, out_dir, paths, lat_title=lat_title)

    print("  Timeseries chart...", flush=True)
    ts = out_dir / "comparison_timeseries_rps_p99.png"
    if plot_comparison_timeseries_rps_p99([(s["label"], s["bundle"]) for s in scenarios], ts):
        paths["comparison_timeseries_rps_p99.png"] = ts

    return paths
