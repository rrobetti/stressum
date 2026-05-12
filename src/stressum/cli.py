from __future__ import annotations

import argparse
import sys
from pathlib import Path

from stressum.aggregate import aggregate_bundle, node_metrics_numeric_summary
from stressum.load import load_run_bundle
from stressum.narrative import write_narrative
from stressum.plots import (
    apply_paper_style,
    plot_error_rates,
    plot_jvm_heap,
    plot_latency_percentiles,
    plot_pg_backends,
    plot_throughput,
)
from stressum.tables import (
    write_node_summary_csv,
    write_replica_csv,
    write_run_summary_row,
    write_tables_readme,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Generate CSV/Markdown tables, PNG figures, and narrative from one Stressar run bundle."
        ),
    )
    parser.add_argument(
        "run_dir",
        type=Path,
        help=(
            "Path to exported run directory "
            "(contains run_metadata.json, replica-*/summary.json, …)."
        ),
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Output directory (default: <run_dir>/paper).",
    )
    parser.add_argument(
        "--no-plots",
        action="store_true",
        help="Skip PNG figure generation.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Optional RNG seed for deterministic plot styling.",
    )
    args = parser.parse_args(argv)

    run_dir = args.run_dir.expanduser().resolve()
    try:
        bundle = load_run_bundle(run_dir)
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        return 2

    if not bundle.summaries:
        print(f"No replica summary.json files found under {run_dir}", file=sys.stderr)
        return 2

    out_dir = args.out.expanduser().resolve() if args.out else (run_dir / "paper")
    out_dir.mkdir(parents=True, exist_ok=True)

    agg = aggregate_bundle(bundle)

    paths: dict[str, Path] = {}
    rep_csv = out_dir / "replica_breakdown.csv"
    run_csv = out_dir / "run_summary.csv"
    write_replica_csv(agg, rep_csv)
    write_run_summary_row(bundle, agg, run_csv)
    paths["replica_breakdown.csv"] = rep_csv
    paths["run_summary.csv"] = run_csv

    node_df = node_metrics_numeric_summary(bundle.node_metrics_csvs)
    if not node_df.empty:
        node_csv = out_dir / "node_metrics_summary.csv"
        write_node_summary_csv(node_df, node_csv)
        paths["node_metrics_summary.csv"] = node_csv

    apply_paper_style(seed=args.seed)
    if not args.no_plots:
        tp = out_dir / "throughput_per_replica.png"
        lp = out_dir / "latency_percentiles_per_replica.png"
        ep = out_dir / "error_rate_per_replica.png"
        plot_throughput(agg, tp)
        plot_latency_percentiles(agg, lp)
        plot_error_rates(agg, ep)
        paths["throughput_per_replica.png"] = tp
        paths["latency_percentiles_per_replica.png"] = lp
        paths["error_rate_per_replica.png"] = ep

        pgp = out_dir / "pg_node_timeseries.png"
        if plot_pg_backends(bundle, pgp):
            paths["pg_node_timeseries.png"] = pgp

        jvmp = out_dir / "jvm_heap_timeseries.png"
        if plot_jvm_heap(bundle, jvmp):
            paths["jvm_heap_timeseries.png"] = jvmp

    narrative_path = out_dir / "narrative.md"
    paths["narrative.md"] = narrative_path
    tables_md = out_dir / "tables.md"
    paths["tables.md"] = tables_md
    write_tables_readme(paths, tables_md)
    write_narrative(bundle, agg, paths, narrative_path)

    print(f"Wrote artifacts to {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
