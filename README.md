# Stressar results — paper artifacts

This repository holds Stressar benchmark exports under `results/` and documentation under `stressar-docs/`. The `stressum` tool’s **default** mode compares multiple runs from a JSON config. For a **single** run bundle, use `stressum run`.

## Setup

Install [uv](https://docs.astral.sh/uv/), then:

```bash
uv sync
```

## Default: compare multiple runs (cross-scenario)

Create a JSON config (by default **`stressum-comparison.json`** at the repository root, or pass `--config`). Each `path` is resolved **relative to the directory containing the config file**. At least two runs are required.

```json
{
  "runs": [
    { "path": "results/hikari-prod-20260511-232048", "label": "Hikari" },
    { "path": "results/ojp-prod-20260512-044306" }
  ]
}
```

```bash
uv run stressum
# or
uv run stressum --config /path/to/my-comparison.json --out /path/to/output-dir
```

Output defaults to `<project-root>/output/comparison-<YYYY-MM-dd-HHMMSS-microseconds>/` and includes:

- `comparison_metadata.json` — scenarios, paths, HDR merge status, fairness warnings when `workload` / `loadMode` / `targetRps` differ across runs
- `comparison_summary.csv` — one row per run (throughput, error rate, median replica percentiles, optional **merged** percentiles when `.hlog` HDR logs exist)
- PNG figures: total throughput, latency (HDR merged across replicas **within** each run when logs are present; otherwise median of `summary.json` percentiles), error rate, optional open-loop / PostgreSQL backends / JVM heap / timeseries plots when data exists

Options: `--config`, `--out`, `--no-plots`, `--seed` (same meanings as for `stressum run`).

## One bundle: `stressum run`

```bash
uv run stressum run results/ojp-prod-20260512-044306
```

Artifacts are written to `<project-root>/output/<run-folder>/<YYYY-MM-dd-HHMMSS-microseconds>/` when the run path is inside this repository (otherwise `<run-dir>/output/…` if you point at a bundle outside the checkout). Override with `--out DIR` to write directly to `DIR`.

Options:

- `--out DIR` — output directory (default: project `output/<run-folder>/<timestamp>/` as above)
- `--no-plots` — skip PNG generation
- `--seed N` — RNG seed for deterministic styling where applicable

## Interpretation

See `stressar-docs/` (especially `METRICS.md` and `RESULTS_FORMAT.md`). Aggregate client throughput is the **sum** of per-replica `achievedThroughputRps`. In the **default comparison** mode, latency bars use **HDR histogram merge across replicas** when readable `.hlog` files are found under each run; otherwise they use the **median** of per-replica `summary.json` percentiles (indicative only). `stressum run <dir>` figures remain per-replica / median summaries from `summary.json`.
