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
    parser.parse_args(argv)

    base = discover_stressum_repo_root() or Path.cwd()
    cfg_path = (base / "stressum-comparison.json").expanduser().resolve()
    if not cfg_path.is_file():
        print(f"Comparison config not found: {cfg_path}", file=sys.stderr)
        return 2

    out = comparison_output_dir()
    print(f"Reading comparison config: {cfg_path}", flush=True)
    print(f"Output directory: {out}", flush=True)
    apply_paper_style()

    code, _meta = run_comparison(cfg_path, out)
    return code


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    return main_compare(argv)


if __name__ == "__main__":
    raise SystemExit(main())
