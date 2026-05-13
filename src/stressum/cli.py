from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

from stressum.aggregate import aggregate_bundle, node_metrics_numeric_summary
from stressum.comparison import run_comparison
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


def discover_stressum_repo_root() -> Path | None:
    """Checkout root for this package, or None (e.g. wheel install)."""
    here_pkg = Path(__file__).resolve().parent
    for cur in [here_pkg, *here_pkg.parents]:
        manifest = cur / "pyproject.toml"
        if not manifest.is_file():
            continue
        try:
            text = manifest.read_text(encoding="utf-8")
        except OSError:
            continue
        if 'name = "stressum"' in text or "name = 'stressum'" in text:
            return cur
    return None


def default_output_dir(run_dir: Path) -> Path:
    """When the run lives inside this repo, write under ``<repo>/output/<run-name>/…``."""
    stamp = datetime.now().strftime("%Y-%m-%d-%H%M%S-%f")
    run_resolved = run_dir.resolve()
    root = discover_stressum_repo_root()
    if root is not None:
        try:
            run_resolved.relative_to(root.resolve())
        except ValueError:
            pass
        else:
            return root / "output" / run_resolved.name / stamp
    return run_resolved / "output" / stamp


def comparison_output_dir() -> Path:
    """``<repo>/output/comparison-<timestamp>/`` or ``./output/comparison-<timestamp>/``."""
    stamp = datetime.now().strftime("%Y-%m-%d-%H%M%S-%f")
    root = discover_stressum_repo_root()
    base = (root / "output") if root is not None else Path.cwd() / "output"
    return base / f"comparison-{stamp}"


def process_run(
    run_dir: Path,
    *,
    out_dir: Path | None = None,
    no_plots: bool = False,
    seed: int | None = None,
    apply_plot_style: bool = True,
) -> int:
    """Load one bundle, write artifacts. Returns 0 on success, 2 on recoverable CLI errors."""
    try:
        bundle = load_run_bundle(run_dir)
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        return 2

    if not bundle.summaries:
        print(f"No replica summary.json files found under {run_dir}", file=sys.stderr)
        return 2

    resolved_out = out_dir.expanduser().resolve() if out_dir else default_output_dir(run_dir)
    resolved_out.mkdir(parents=True, exist_ok=True)

    agg = aggregate_bundle(bundle)

    paths: dict[str, Path] = {}
    rep_csv = resolved_out / "replica_breakdown.csv"
    run_csv = resolved_out / "run_summary.csv"
    write_replica_csv(agg, rep_csv)
    write_run_summary_row(bundle, agg, run_csv)
    paths["replica_breakdown.csv"] = rep_csv
    paths["run_summary.csv"] = run_csv

    node_df = node_metrics_numeric_summary(bundle.node_metrics_csvs)
    if not node_df.empty:
        node_csv = resolved_out / "node_metrics_summary.csv"
        write_node_summary_csv(node_df, node_csv)
        paths["node_metrics_summary.csv"] = node_csv

    if apply_plot_style:
        apply_paper_style(seed=seed)
    if not no_plots:
        tp = resolved_out / "throughput_per_replica.png"
        lp = resolved_out / "latency_percentiles_per_replica.png"
        ep = resolved_out / "error_rate_per_replica.png"
        plot_throughput(agg, tp)
        plot_latency_percentiles(agg, lp)
        plot_error_rates(agg, ep)
        paths["throughput_per_replica.png"] = tp
        paths["latency_percentiles_per_replica.png"] = lp
        paths["error_rate_per_replica.png"] = ep

        pgp = resolved_out / "pg_node_timeseries.png"
        if plot_pg_backends(bundle, pgp):
            paths["pg_node_timeseries.png"] = pgp

        jvmp = resolved_out / "jvm_heap_timeseries.png"
        if plot_jvm_heap(bundle, jvmp):
            paths["jvm_heap_timeseries.png"] = jvmp

    narrative_path = resolved_out / "narrative.md"
    paths["narrative.md"] = narrative_path
    tables_md = resolved_out / "tables.md"
    paths["tables.md"] = tables_md
    write_tables_readme(paths, tables_md)
    write_narrative(bundle, agg, paths, narrative_path)

    print(f"Wrote artifacts to {resolved_out}")
    return 0


def main_compare(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Default stressum mode: compare two or more Stressar run bundles from a JSON "
            "config (HDR merge across replicas per run when logs are present)."
        ),
    )
    root = discover_stressum_repo_root()
    default_cfg = (root / "stressum-comparison.json") if root is not None else None
    parser.add_argument(
        "--config",
        type=Path,
        default=default_cfg,
        help=(
            "Path to comparison JSON (default: <repo-root>/stressum-comparison.json "
            "when running from this checkout)."
        ),
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Output directory (default: <repo>/output/comparison-<timestamp>/).",
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

    if args.config is None:
        print(
            "No default config path (checkout root not detected). Pass --config /path/to.json",
            file=sys.stderr,
        )
        return 2
    cfg_path = args.config.expanduser().resolve()
    if not cfg_path.is_file():
        print(f"Comparison config not found: {cfg_path}", file=sys.stderr)
        return 2

    out = args.out.expanduser().resolve() if args.out else comparison_output_dir()
    apply_paper_style(seed=args.seed)

    code, _meta = run_comparison(cfg_path, out, no_plots=args.no_plots)
    return code


def main_run(argv: list[str] | None = None) -> int:
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
        help=(
            "Output directory (default: <project-root>/output/<run-folder>/<timestamp>/ when "
            "the run path is inside this repository, else <run_dir>/output/<timestamp>/)."
        ),
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
    out = args.out.expanduser().resolve() if args.out else None
    return process_run(
        run_dir,
        out_dir=out,
        no_plots=args.no_plots,
        seed=args.seed,
        apply_plot_style=True,
    )


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] == "batch":
        print(
            "The `batch` subcommand was removed. Use `stressum run <run_dir>` once per bundle.",
            file=sys.stderr,
        )
        return 2
    if argv and argv[0] == "compare":
        print(
            "The `compare` subcommand was removed; cross-scenario comparison is the default. "
            "Invoke `stressum` or `stressum --config …` (without `compare`).",
            file=sys.stderr,
        )
        return 2
    if argv and argv[0] == "run":
        return main_run(argv[1:])
    return main_compare(argv)


if __name__ == "__main__":
    raise SystemExit(main())
