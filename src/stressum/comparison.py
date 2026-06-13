from __future__ import annotations

import json
import sys
from datetime import UTC, datetime
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any

import pandas as pd

from stressum.aggregate import (
    aggregate_bundle,
    is_open_loop,
    postgres_process_summary,
    proxy_tier_cpu_summary,
    total_resource_footprint_summary,
)
from stressum.comparison_plots import write_comparison_plots
from stressum.hdr_merge import merge_run_histogram
from stressum.load import RunBundle, load_run_bundle
from stressum.paper import write_paper_outputs
from stressum.tables import run_summary_dict


def load_comparison_config(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or "runs" not in data:
        raise ValueError("Config must be a JSON object with a 'runs' array")
    runs = data["runs"]
    if not isinstance(runs, list) or len(runs) < 2:
        raise ValueError("Config 'runs' must list at least two benchmark directories")
    for i, item in enumerate(runs):
        if not isinstance(item, dict) or "path" not in item:
            raise ValueError(f"runs[{i}] must be an object with a 'path' string")
        if not isinstance(item["path"], str):
            raise ValueError(f"runs[{i}].path must be a string")
    return data


def resolve_run_path(config_path: Path, path_str: str) -> Path:
    p = Path(path_str)
    if not p.is_absolute():
        p = (config_path.parent / p).resolve()
    else:
        p = p.resolve()
    return p


def _open_loop_totals(bundle: RunBundle) -> tuple[bool, int, float]:
    missed = 0
    delay = 0.0
    any_open = False
    for summ in bundle.summaries:
        ri = summ.get("runInfo") or {}
        if is_open_loop(ri):
            any_open = True
        missed += int(ri.get("openLoopMissedOpportunities") or 0)
        v = ri.get("openLoopSchedulingDelayMs")
        if isinstance(v, (int, float)):
            delay += float(v)
    return any_open, missed, delay


def _top_error_types(errors_by_type: dict[str, int], limit: int = 5) -> str:
    if not errors_by_type:
        return ""
    ranked = sorted(errors_by_type.items(), key=lambda x: (-x[1], x[0]))[:limit]
    return "; ".join(f"{name}:{count}" for name, count in ranked)


def _fairness_warnings(scenarios: list[dict[str, Any]]) -> list[str]:
    warnings: list[str] = []
    if len(scenarios) < 2:
        return warnings
    keys = ("workload", "loadMode", "targetRps")
    baser = scenarios[0]["bundle"].summaries[0].get("runInfo") or {}
    for s in scenarios[1:]:
        ri = s["bundle"].summaries[0].get("runInfo") or {}
        for k in keys:
            if baser.get(k) != ri.get(k):
                warnings.append(
                    f"runInfo mismatch for '{s['label']}': {k} "
                    f"{baser.get(k)!r} vs {ri.get(k)!r} (baseline {scenarios[0]['label']})"
                )
    return warnings


def run_comparison(
    config_path: Path,
    out_dir: Path,
    *,
    generate_paper: bool = True,
    generate_appendix: bool = True,
    expected_repetitions: int = 5,
    load_map_path: Path | None = None,
    slo_p95_ms: float = 50.0,
    slo_error_rate_pct: float = 1.0,
) -> tuple[int, dict[str, Any]]:
    """
    Execute multi-run comparison. Returns (exit_code, metadata_dict).
    """
    try:
        cfg = load_comparison_config(config_path)
    except (OSError, ValueError, json.JSONDecodeError) as e:
        print(e, file=sys.stderr)
        return 2, {}

    runs_cfg = cfg["runs"]
    scenarios_payload: list[dict[str, Any]] = []
    scenario_rows: list[dict[str, Any]] = []
    scenarios_plot: list[dict[str, Any]] = []

    print(f"Loading {len(runs_cfg)} benchmark run(s)...", flush=True)
    for run_idx, item in enumerate(runs_cfg, start=1):
        path_str = item["path"]
        run_path = resolve_run_path(config_path, path_str)
        label = item.get("label")
        if not isinstance(label, str) or not label.strip():
            label = run_path.name

        print(f"  [{run_idx}/{len(runs_cfg)}] {label} ({run_path})", flush=True)

        try:
            bundle = load_run_bundle(run_path)
        except FileNotFoundError as e:
            print(e, file=sys.stderr)
            return 2, {}

        if not bundle.summaries:
            print(f"No replica summary.json under {run_path}", file=sys.stderr)
            return 2, {}

        agg = aggregate_bundle(bundle)
        proxy_cpu = proxy_tier_cpu_summary(bundle)
        postgres_process = postgres_process_summary(bundle)
        total_footprint = total_resource_footprint_summary(bundle)
        ref_p50 = agg.median_p50_ms
        if bundle.hdr_paths:
            print(
                f"    Merging HDR histograms ({len(bundle.hdr_paths)} file(s))...",
                flush=True,
            )
        merged, hdr_warnings = merge_run_histogram(bundle.hdr_paths, ref_p50_ms=ref_p50)
        latency_source = "hdr_merged" if merged is not None else "summary_json_median"

        ol_any, ol_missed, ol_delay = _open_loop_totals(bundle)
        meta = bundle.metadata or {}
        first_ri = bundle.summaries[0].get("runInfo") or {}

        has_pg = any(k.endswith("pg_metrics.csv") for k in bundle.node_metrics_csvs)
        has_jvm = any("jvm_metrics" in k.lower() for k in bundle.node_metrics_csvs)
        has_db_proc = any(k.endswith("db/db_proc_metrics.csv") for k in bundle.node_metrics_csvs)

        scenario_meta: dict[str, Any] = {
            "label": label,
            "path_in_config": path_str,
            "path_resolved": str(run_path),
            "run_metadata": meta,
            "run_info_sample": {
                "sut": first_ri.get("sut"),
                "workload": first_ri.get("workload"),
                "loadMode": first_ri.get("loadMode"),
                "targetRps": first_ri.get("targetRps"),
            },
            "total_achieved_rps": agg.total_successful_rps,
            "total_successful_rps": agg.total_successful_rps,
            "total_error_rps": agg.total_error_rps,
            "total_completed_rps": agg.total_completed_rps,
            "total_attempted_rps": agg.total_attempted_rps,
            "total_successful_requests": agg.total_successful_requests,
            "aggregate_error_rate": agg.aggregate_error_rate,
            "errors_by_type": agg.errors_by_type,
            "top_error_types": _top_error_types(agg.errors_by_type),
            "median_replica_p50_ms": agg.median_p50_ms,
            "latency_percentiles_source": latency_source,
            "hdr_file_count": len(bundle.hdr_paths),
            "hdr_paths_used": list(merged.hdr_paths_used) if merged else [],
            "has_pg_metrics": has_pg,
            "has_db_proc_metrics": has_db_proc,
            "has_jvm_metrics": has_jvm,
            "open_loop": ol_any,
            "open_loop_missed_opportunities_sum": ol_missed,
            "open_loop_scheduling_delay_ms_sum": ol_delay,
            "warnings": list(hdr_warnings),
        }
        if postgres_process is not None:
            scenario_meta["postgres_process"] = postgres_process
            if "cpu_pct_peak" in postgres_process:
                scenario_meta["postgres_cpu_pct_peak"] = postgres_process["cpu_pct_peak"]
            if "rss_mb_peak" in postgres_process:
                scenario_meta["postgres_rss_mb_peak"] = postgres_process["rss_mb_peak"]
        if proxy_cpu is not None:
            scenario_meta["proxy_tier_cpu"] = proxy_cpu
            scenario_meta["proxy_service_cpu_aligned_peak_pct"] = proxy_cpu[
                "service_cpu_aligned_peak_pct"
            ]
            scenario_meta["proxy_service_cpu_legacy_peak_sum_pct"] = proxy_cpu[
                "service_cpu_legacy_peak_sum_pct"
            ]
            host_peak = proxy_cpu.get("host_cpu_aligned_peak_pct")
            if isinstance(host_peak, (int, float)):
                scenario_meta["proxy_host_cpu_aligned_peak_pct"] = float(host_peak)
        scenario_meta["total_footprint"] = total_footprint
        scenario_meta["bench_cpu_sum_pct"] = total_footprint["bench_cpu_sum_pct"]
        scenario_meta["total_cpu_pct"] = total_footprint["total_cpu_pct"]
        scenario_meta["total_cpu_mean_pct"] = total_footprint["total_cpu_mean_pct"]
        scenario_meta["total_cpu_p95_pct"] = total_footprint["total_cpu_p95_pct"]
        scenario_meta["proxy_rss_mb_aligned_peak"] = total_footprint["proxy_rss_mb_aligned_peak"]
        scenario_meta["total_rss_mb_peak"] = total_footprint["total_rss_mb_peak"]
        scenario_meta["total_rss_mb_mean"] = total_footprint["total_rss_mb_mean"]
        scenario_meta["total_rss_mb_p95"] = total_footprint["total_rss_mb_p95"]
        if merged is not None:
            scenario_meta["merged_latency_ms"] = {
                "p50": merged.p50_ms,
                "p95": merged.p95_ms,
                "p99": merged.p99_ms,
                "p999": merged.p999_ms,
                "unit_divisor": merged.unit_divisor,
            }

        scenarios_payload.append(scenario_meta)

        row = run_summary_dict(
            bundle,
            agg,
            proxy_cpu=proxy_cpu,
            postgres_process=postgres_process,
            total_footprint=total_footprint,
            open_loop=ol_any,
        )
        row["comparison_label"] = label
        row["comparison_path_resolved"] = str(run_path)
        row["latency_percentiles_source"] = latency_source
        if merged is not None:
            row["merged_p50_ms"] = merged.p50_ms
            row["merged_p95_ms"] = merged.p95_ms
            row["merged_p99_ms"] = merged.p99_ms
            row["merged_p999_ms"] = merged.p999_ms
            row["hdr_unit_divisor"] = merged.unit_divisor
        else:
            row["merged_p50_ms"] = ""
            row["merged_p95_ms"] = ""
            row["merged_p99_ms"] = ""
            row["merged_p999_ms"] = ""
            row["hdr_unit_divisor"] = ""
        scenario_rows.append(row)

        scenarios_plot.append(
            {
                "label": label,
                "bundle": bundle,
                "agg": agg,
                "merged": merged,
                "proxy_cpu": proxy_cpu,
                "postgres_process": postgres_process,
                "total_footprint": total_footprint,
                "run_metadata": meta,
            }
        )

    global_warnings = _fairness_warnings(scenarios_plot)

    out_dir.mkdir(parents=True, exist_ok=True)
    plot_paths: dict[str, Path] = {}
    paper_warnings: list[str] = []
    if generate_appendix:
        appendix_dir = out_dir / "appendix"
        print("Generating appendix/debug plots...", flush=True)
        appendix_paths = write_comparison_plots(scenarios_plot, appendix_dir)
        plot_paths.update(
            {f"appendix/{rel_path}": path for rel_path, path in appendix_paths.items()}
        )
        print(f"  Generated {len(appendix_paths)} appendix/debug chart(s)", flush=True)
    if generate_paper:
        paper_dir = out_dir / "paper"
        print("Generating paper plots and summary tables...", flush=True)
        try:
            paper_paths, paper_warnings = write_paper_outputs(
                scenarios_plot,
                paper_dir,
                expected_repetitions=expected_repetitions,
                load_map_path=load_map_path,
                slo_p95_ms=slo_p95_ms,
                slo_error_rate_pct=slo_error_rate_pct,
            )
        except ValueError as e:
            print(e, file=sys.stderr)
            return 2, {}
        plot_paths.update({f"paper/{rel_path}": path for rel_path, path in paper_paths.items()})
        print(f"  Generated {len(paper_paths)} paper artifact(s)", flush=True)

    try:
        stressum_ver = version("stressum")
    except PackageNotFoundError:
        stressum_ver = "0.0.0"

    artifacts: dict[str, str] = {
        k: p.relative_to(out_dir).as_posix() for k, p in sorted(plot_paths.items())
    }
    artifacts["comparison_metadata.json"] = "comparison_metadata.json"
    artifacts["comparison_summary.csv"] = "comparison_summary.csv"

    full_meta: dict[str, Any] = {
        "generated_at": datetime.now(UTC).isoformat(),
        "stressum_version": stressum_ver,
        "config_path": str(config_path.resolve()),
        "output_dir": str(out_dir.resolve()),
        "global_warnings": global_warnings,
        "paper_warnings": paper_warnings,
        "scenarios": scenarios_payload,
        "artifacts": artifacts,
    }
    print("Writing comparison metadata and summary CSV...", flush=True)
    (out_dir / "comparison_metadata.json").write_text(
        json.dumps(full_meta, indent=2),
        encoding="utf-8",
    )
    pd.DataFrame(scenario_rows).to_csv(out_dir / "comparison_summary.csv", index=False)

    print(f"Wrote comparison artifacts to {out_dir}")
    return 0, full_meta
