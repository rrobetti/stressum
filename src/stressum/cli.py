from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

from stressum.comparison import run_comparison
from stressum.plots import apply_paper_style


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


def comparison_output_dir() -> Path:
    """``<repo>/output/comparison-<timestamp>/`` or ``./output/comparison-<timestamp>/``."""
    stamp = datetime.now().strftime("%Y-%m-%d-%H%M%S-%f")
    root = discover_stressum_repo_root()
    base = (root / "output") if root is not None else Path.cwd() / "output"
    return base / f"comparison-{stamp}"


def main_compare(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Compare two or more Stressar run bundles using stressum-comparison.json "
            "at the repository root (or current working directory if the checkout "
            "cannot be detected). HDR merge across replicas per run when logs are present."
        ),
    )
    output_mode = parser.add_mutually_exclusive_group()
    output_mode.add_argument(
        "--report",
        dest="report",
        action="store_true",
        help="Generate only report outputs for main figures under report/.",
    )
    output_mode.add_argument(
        "--paper",
        dest="report",
        action="store_true",
        help=argparse.SUPPRESS,
    )
    output_mode.add_argument(
        "--debug",
        dest="debug",
        action="store_true",
        help="Generate only debug outputs for appendix figures under debug/.",
    )
    output_mode.add_argument(
        "--appendix",
        dest="debug",
        action="store_true",
        help=argparse.SUPPRESS,
    )
    output_mode.add_argument(
        "--all",
        action="store_true",
        help="Generate both report and debug outputs (default).",
    )
    parser.add_argument(
        "--repetitions",
        type=int,
        default=5,
        help="Expected repetition count per technology/load level group.",
    )
    parser.add_argument(
        "--load-map",
        type=str,
        help="Optional JSON file mapping run labels to load levels when metadata is insufficient.",
    )
    parser.add_argument(
        "--slo-p95-ms",
        type=float,
        default=10_000.0,
        help="p95 latency SLO threshold in milliseconds for the main-figure heatmap.",
    )
    parser.add_argument(
        "--slo-error-rate",
        type=float,
        default=1.0,
        help="Error-rate SLO threshold in percent for the main-figure heatmap.",
    )
    args = parser.parse_args(argv)

    base = discover_stressum_repo_root() or Path.cwd()
    cfg_path = (base / "stressum-comparison.json").expanduser().resolve()
    if not cfg_path.is_file():
        print(f"Comparison config not found: {cfg_path}", file=sys.stderr)
        return 2

    load_map_path = None
    if args.load_map:
        load_map_path = Path(args.load_map).expanduser()
        if not load_map_path.is_absolute():
            load_map_path = (cfg_path.parent / load_map_path).resolve()

    out = comparison_output_dir()
    print(f"Reading comparison config: {cfg_path}", flush=True)
    print(f"Output directory: {out}", flush=True)
    apply_paper_style()

    generate_paper = args.report or not args.debug
    generate_appendix = args.debug or args.all or not args.report

    code, _meta = run_comparison(
        cfg_path,
        out,
        generate_paper=generate_paper,
        generate_appendix=generate_appendix,
        expected_repetitions=args.repetitions,
        load_map_path=load_map_path,
        slo_p95_ms=args.slo_p95_ms,
        slo_error_rate_pct=args.slo_error_rate,
    )
    return code


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    return main_compare(argv)


if __name__ == "__main__":
    raise SystemExit(main())
