# Stressar results — paper artifacts

This repository holds Stressar benchmark exports under `results/` and documentation under `stressar-docs/`. The `stressum` tool turns **one run directory** into CSV tables, Markdown summaries, and PNG figures suitable for scientific writing.

## Setup

Install [uv](https://docs.astral.sh/uv/), then:

```bash
uv sync
```

## One command per run

```bash
uv run stressum results/ojp-prod-20260512-044306
```

Artifacts are written to `<run-dir>/output/<YYYY-MM-dd-HHMMSS-microseconds>/` (one folder per invocation). Override with `--out DIR` to write directly to `DIR`.

Options:

- `--out DIR` — output directory (default: `<run-dir>/output/<timestamped subfolder>/`)
- `--no-plots` — skip PNG generation
- `--seed N` — RNG seed for deterministic styling where applicable

## Interpretation

See `stressar-docs/` (especially `METRICS.md` and `RESULTS_FORMAT.md`). Aggregate client throughput is the **sum** of per-replica `achievedThroughputRps`. Cross-replica latency percentiles in this tool are **descriptive** (per-replica summaries); true merged percentiles require HDR histogram merge when logs are present.
