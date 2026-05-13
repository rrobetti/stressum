# Stressar results — paper artifacts

This repository holds Stressar benchmark exports under `results/` and documentation under `stressar-docs/`. The `stressum` CLI compares **two or more** exported runs from a JSON config and writes comparison artifacts (CSVs, figures, metadata).

## Setup

Install [uv](https://docs.astral.sh/uv/), then:

```bash
uv sync
```

## Compare multiple runs (cross-scenario)

Create **`stressum-comparison.json`** at the repository root (or in the current working directory when the checkout root cannot be detected). Each `path` is resolved **relative to the directory containing the config file**. At least two runs are required.

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
```

Output is written to `<project-root>/output/comparison-<YYYY-MM-dd-HHMMSS-microseconds>/` (or `./output/...` from the current working directory when the checkout root cannot be detected) and includes:

- `comparison_metadata.json` — scenarios, paths, HDR merge status, fairness warnings when `workload` / `loadMode` / `targetRps` differ across runs
- `comparison_summary.csv` — one row per run (throughput, error rate, median replica percentiles, optional **merged** percentiles when `.hlog` HDR logs exist)
- PNG figures: total throughput, latency (HDR merged across replicas **within** each run when logs are present; otherwise median of `summary.json` percentiles), error rate, optional open-loop / PostgreSQL backends / JVM heap / timeseries plots when data exists. Plot styling uses a fixed NumPy RNG seed for reproducible figures.

## Interpretation

See `stressar-docs/` (especially `METRICS.md` and `RESULTS_FORMAT.md`). Aggregate client throughput is the **sum** of per-replica `achievedThroughputRps`. Latency bars in comparison figures use **HDR histogram merge across replicas** when readable `.hlog` files are found under each run; otherwise they use the **median** of per-replica `summary.json` percentiles (indicative only).
