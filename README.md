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
- `comparison_summary.csv` — one row per run (throughput, error rate, median replica percentiles, optional **merged** percentiles when `.hlog` HDR logs exist, proxy-tier CPU, PostgreSQL process CPU/RSS when node metrics exist, **total resource footprint** columns — see [Total resource footprint](#total-resource-footprint-cross-technology))
- PNG figures — see [Generated figures](#generated-figures) below

Plot styling uses a fixed NumPy RNG seed for reproducible figures.

## Generated figures

Figures fall into three layouts:

| Layout | Location | When emitted |
|--------|----------|--------------|
| **Cross-technology** | Batch root (`comparison_cross_tech_*.png`) | At least two technologies share the same load-point suffix in their `label` (e.g. `Hikari A` and `OJP A`) |
| **Per-technology bars** | Subfolder per chart type (`comparison_<metric>/<chart>__<Technology>.png`) | Always (one PNG per technology prefix found in labels) |
| **Per-scenario time series** | Subfolder per chart type (`comparison_<metric>/<chart>__<label-slug>.png`) | Only when the underlying CSV exists for that run |

**Label convention.** Cross-technology matching uses the token before the last space as the technology (`Hikari`, `OJP`, `pgBouncer`) and the remainder as the load point (`A`, `B`, …). Example: `OJP T` and `Hikari T` are compared at load point `T`.

**Throughput and request counts** are always the **sum across bench replicas** within each run (`achievedThroughputRps`, `successfulRequests`, etc.).

**Latency bars** use **HDR histogram merge across replicas** when readable `.hlog` files exist under the run; otherwise the **median** of per-replica `summary.json` percentiles (indicative only — see `comparison_metadata.json` → `latency_percentiles_source`).

### Cross-technology charts (batch root)

Grouped bar charts place technologies side by side at each shared load point. Throughput–metric curves plot one line per technology: X = `targetRps` from the first replica’s `runInfo` (labelled “Target RPS (aggregate)”); Y = the metric at that load point.

| File | Chart type | Y-axis / metric | Notes |
|------|------------|-----------------|-------|
| `comparison_cross_tech_total_throughput.png` | Grouped bars | Successful throughput (RPS, sum of replicas) | Successful requests only |
| `comparison_cross_tech_total_completed_rps.png` | Stacked bars | Completed throughput (RPS) | Successful (solid) + error (hatched) per technology |
| `comparison_cross_tech_total_successful_requests.png` | Grouped bars | Total successful requests (sum of replicas) | Count over the run window |
| `comparison_cross_tech_latency_p50.png` | Grouped bars | p50 latency (ms) | HDR merge or summary.json median |
| `comparison_cross_tech_latency_p95.png` | Grouped bars | p95 latency (ms) | Same source as p50 |
| `comparison_cross_tech_latency_p99.png` | Grouped bars | p99 latency (ms) | Same source as p50 |
| `comparison_cross_tech_latency_p999.png` | Grouped bars | p999 latency (ms) | Same source as p50 |
| `comparison_cross_tech_error_rate.png` | Grouped bars | Aggregate error rate (%) | `failed / total` across replicas |
| `comparison_cross_tech_proxy_host_cpu_aligned_peak.png` | Grouped bars | Proxy tier `host_cpu` aligned peak sum (%) | Omitted if no proxy/LB `*_proc_metrics.csv` |
| `comparison_cross_tech_postgres_process_cpu_peak.png` | Grouped bars | PostgreSQL process CPU peak (%) | From `node_metrics/db/db_proc_metrics.csv` → `cpu_pct` max |
| `comparison_cross_tech_postgres_process_rss_peak.png` | Grouped bars | PostgreSQL process RSS peak (MB) | From `db_proc_metrics.csv` → `rss_mb` max |
| `comparison_cross_tech_open_loop_missed_opportunities.png` | Grouped bars | Sum of `openLoopMissedOpportunities` | Only when at least one run used open-loop load |
| `comparison_cross_tech_open_loop_scheduling_delay.png` | Grouped bars | Sum of `openLoopSchedulingDelayMs` | Only when at least one run used open-loop load |
| `comparison_cross_tech_throughput_latency_p95.png` | Line curve | p95 latency (ms) vs target RPS | Y-axis log scale |
| `comparison_cross_tech_throughput_latency_p99.png` | Line curve | p99 latency (ms) vs target RPS | Y-axis log scale |
| `comparison_cross_tech_throughput_postgres_cpu.png` | Line curve | PostgreSQL CPU peak (%) vs target RPS | Requires `db_proc_metrics.csv` |
| `comparison_cross_tech_throughput_postgres_rss.png` | Line curve | PostgreSQL RSS peak (MB) vs target RPS | Requires `db_proc_metrics.csv` |
| `comparison_cross_tech_total_cpu_peak.png` | Grouped bars | Total CPU (virtual core budget, %) | One bar per technology; `total_cpu_pct` (bench + PostgreSQL + proxy/LB) |
| `comparison_cross_tech_total_rss_peak.png` | Grouped bars | Total RSS peak (MB) | One bar per technology; `total_rss_mb_peak` (**excludes bench/LG**) |
| `comparison_cross_tech_throughput_total_cpu.png` | Line curve | Total CPU (%) vs target RPS | Sum of bench + PostgreSQL + proxy aligned peaks |
| `comparison_cross_tech_throughput_total_rss.png` | Line curve | Total RSS peak (MB) vs target RPS | PostgreSQL + proxy/LB RSS only |

Fixed colours: OJP = steelblue, Hikari = darkorange, pgBouncer = mediumseagreen.

## Total resource footprint (cross-technology)

Comparison figures and `comparison_summary.csv` include **aggregated resource totals**
intended to reflect the full benchmark stack: bench replicas (load generators),
PostgreSQL, and the proxy tier (OJP or pgBouncer nodes plus HAProxy when present).
These are **operational footprint proxies**, not cloud billing lines.

### What is included

| Layer | CPU | Memory (RSS) |
|-------|-----|--------------|
| **Bench replicas (LG)** | Yes — sum of per-replica `appCpuMedian` from `replica-*/summary.json` (`bench_jvm_cpu`, in-process median during steady-state) | **No** — load-generator RSS is not collected in exported bundles |
| **PostgreSQL** | Yes — peak of `cpu_pct` in `node_metrics/db/db_proc_metrics.csv` | Yes — peak of `rss_mb` in the same file |
| **Proxy tier** | Yes — time-aligned sum of `cpu_pct` across `node_metrics/proxy/*_proc_metrics.csv` and `node_metrics/lb/*_proc_metrics.csv`, then peak (`service_cpu` aligned peak; same scope as per-scenario proxy CPU plots) | Yes — time-aligned sum of `rss_mb` across the same proxy/LB CSVs, then peak |
| **HAProxy** | Included in proxy-tier rollup (pgBouncer scenario only) | Included in proxy-tier rollup |

Hikari runs have no proxy/LB CSVs; those components contribute **0** in the rollup.

### How totals are computed

**Total CPU (reported %)** — sum of independent peaks (components may peak at
different timestamps):

```
total_cpu_pct ≈ bench_cpu_sum_pct
              + postgres_cpu_pct_peak
              + proxy_service_cpu_aligned_peak_pct
```

where `bench_cpu_sum_pct = Σ appCpuMedian` over all replicas present in the
bundle (`replicas_in_bundle` / `bench_replica_count` in `run_metadata.json`).

Units: each term is **% of one CPU core** for the measured process (or aligned
sum across nodes). The total is a **virtual core budget** across machines, useful
for comparing topologies, not a single-host utilization percentage.

**Total memory (reported MB)** — **partial**; bench/LG memory is **excluded**:

```
total_rss_mb_peak ≈ postgres_rss_mb_peak + proxy_rss_mb_aligned_peak
```

Proxy RSS uses OS RSS from `*_proc_metrics.csv`. For OJP proxy nodes, OS RSS can
overstate live JVM heap; see `stressar-docs/METRICS.md` (prefer `heap_used_mb` in
`*_jvm_metrics.csv` for OJP heap analysis — that series is **not** folded into
`total_rss_mb_peak` today).

There is **no** `appRssMedian` (or other LG side-car) in exported runs; total
memory charts and CSV columns must **not** be read as “application + infra RAM”.

### Cross-technology charts (when emitted)

Grouped bar charts at each shared load point place **one bar per technology**
(OJP, Hikari, pgBouncer) side by side, using the fixed colour palette above.
Per-component breakdown (bench vs PostgreSQL vs proxy) is available in
`comparison_summary.csv`, not in these total figures.

### `comparison_summary.csv` columns

| Column | Meaning |
|--------|---------|
| `bench_cpu_sum_pct` | Σ `appCpuMedian` across replicas |
| `total_cpu_pct` | bench + PostgreSQL + proxy aligned peak (see formula above) |
| `proxy_rss_mb_aligned_peak` | Time-aligned peak sum of proxy/LB `rss_mb` |
| `total_rss_mb_peak` | PostgreSQL RSS peak + proxy RSS aligned peak (**excludes bench**) |

### Interpretation notes

- **Throughput** in comparison outputs remains the **sum across bench replicas**;
  resource totals use the same replica set as the bundle on disk (not necessarily
  the full 16-replica production layout unless the export contains all replicas).
- **PgBouncer** scenarios still use **local HikariCP** on bench JVMs
  (`clientPooling: hikari`); only **OJP** removes the client-side pool. Compare
  bench CPU between Hikari and OJP for “pool in every microservice vs centralized
  proxy” on the application tier.
- Including PostgreSQL in totals reflects **different connection budgets per
  topology** (~300 direct for Hikari vs ~48 via proxy), not only pooling overhead.
  Use per-component CSV columns (`bench_cpu_sum_pct`, `postgres_*`, `proxy_*`) to
  see where cost sits.

### Per-technology bar charts (subfolders)

For each technology prefix in the config (e.g. all labels starting with `Hikari`), one bar chart is written per metric. Bars are load points for that technology only (prefix stripped from axis labels when every label shares it).

| Subfolder / base name | Metric | Source |
|-----------------------|--------|--------|
| `comparison_total_throughput/` | Successful throughput (RPS) | Sum of replica `successfulThroughputRps` |
| `comparison_total_completed_rps/` | Completed throughput (RPS) | Successful + error RPS, stacked |
| `comparison_total_successful_requests/` | Total successful requests | Sum of replica `successfulRequests` |
| `comparison_latency_p50/` … `comparison_latency_p999/` | Latency percentiles (ms) | HDR merge or summary.json median |
| `comparison_error_rate/` | Aggregate error rate (%) | Across replicas |
| `comparison_proxy_host_cpu_aligned_peak/` | Proxy tier host CPU peak (%) | Time-aligned sum across proxy/LB processes |
| `comparison_open_loop_missed_opportunities/` | Open-loop missed opportunities | Sum across replicas; only if open-loop runs present |
| `comparison_open_loop_scheduling_delay/` | Open-loop scheduling delay (ms) | Sum across replicas; only if open-loop runs present |

Example path: `comparison_latency_p95/comparison_latency_p95__Hikari.png`.

### Per-scenario time series (subfolders)

One PNG per configured run label. Each plot is a time series over the run (X = seconds since sample start). Skipped silently when the CSV is missing.

| Subfolder / base name | Y-axis | Source file |
|-----------------------|--------|-------------|
| `comparison_pg_numbackends/` | Active backends | `node_metrics/**/pg_metrics.csv` (`active_backends` or `numbackends`) |
| `comparison_postgres_process_cpu/` | `cpu_pct` (%) | `node_metrics/db/db_proc_metrics.csv` |
| `comparison_postgres_process_rss/` | `rss_mb` (MB) | `node_metrics/db/db_proc_metrics.csv` |
| `comparison_jvm_heap/` | `heap_used_mb` | First `jvm_metrics.csv` under the run (OJP proxy) |
| `comparison_proxy_service_cpu_aligned_peak/` | Proxy `service_cpu` sum (%) | Proxy/LB `*_proc_metrics.csv` (`cpu_pct`, time-aligned sum); title includes aligned peak |
| `comparison_proxy_host_cpu_aligned_peak/` | Proxy `host_cpu` sum (%) | Same CSVs (`host_cpu_pct`, time-aligned sum) |

Example path: `comparison_postgres_process_rss/comparison_postgres_process_rss__OJP_L.png`.

For OJP, prefer `heap_used_mb` (JVM heap via `jstat`) over `appRssMedian` in bench summaries — see `stressar-docs/METRICS.md`.

### Global timeseries overlay (batch root)

| File | Content | Requirements |
|------|---------|--------------|
| `comparison_timeseries_rps_p99.png` | All scenarios on one figure: top panel = sum of per-second `achieved_rps` across replicas; bottom panel = median `p99_ms` across replicas | Each run must have `replica-*/timeseries.csv` with `timestamp_iso`, `achieved_rps`, `p99_ms`. **Not** HDR-based. |

## Interpretation

See `stressar-docs/` (especially `METRICS.md` and `RESULTS_FORMAT.md`). Aggregate client throughput is the **sum** of per-replica `achievedThroughputRps`. Latency bars in comparison figures use **HDR histogram merge across replicas** when readable `.hlog` files are found under each run; otherwise they use the **median** of per-replica `summary.json` percentiles (indicative only).
