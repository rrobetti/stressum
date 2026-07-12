# Graph rationale

## How to read the latency and throughput strip plots

- `p95_latency_vs_load.png`, `p99_latency_vs_load.png`, and `throughput_vs_load.png` use per-run strip plots instead of mean ± CI. Each dot is the value from one of the n=5 repetitions. The line connects the per-technology medians across load levels.
- All latency values in these charts are derived directly from merged HdrHistogram logs. HDR histograms record every individual request latency at full precision, so the per-run p95 and p99 values are exact percentiles of the observed request population, not estimates.
- A t-distribution CI would assert that the five per-run HDR percentiles are exchangeable draws from a normal population. That assumption is not warranted: HDR-derived percentiles capture non-linear tail behaviour and can be bimodal under load variation. Showing the n=5 raw values is more honest and more informative.
- `summary_stats.csv` records mean, median, stddev, min, and max for all metrics. The ci95_low and ci95_high columns are set to NaN for p95_latency_ms and p99_latency_ms for the reason above. CI is retained for throughput and other non-latency metrics.

## How to read the other line graphs

- The main line in a line graph is the mean across the five repetitions at that load level.
- The shaded band above and below a line is the Min/Max Range: the absolute minimum and maximum values observed across the five repeated runs at that load level.
- Narrower shaded bands mean the repetitions were more consistent. Wider bands mean the result moved around more from run to run.

## Where mean with Min/Max Range is used

- Mean with Min/Max Range is used in these report line graphs: `error_rate_vs_load.png`, `postgres_backend_connections_vs_load.png`, `rps_per_db_connection_vs_load.png`, `postgres_cpu_vs_load.png`, `postgres_rss_vs_load.png`, `proxy_tier_cpu_vs_load.png`, `proxy_tier_rss_vs_load.png`, and `ojp_heap_utilisation_vs_load.png`.
- Mean with Min/Max Range is also used in the measured panels of `attempted_completed_success_error_rps.png`: attempted RPS, successful RPS, and error RPS. The offered RPS panel does not show a shaded band because it is the configured target load, not an observed metric with run to run variation.
- The combined OJP heap report graph (`ojp_heap_used_committed_vs_load.png`) shows mean lines without shaded bands to keep the two JVM series easy to compare on one view.
- Boxplots, the error breakdown chart, and the SLO heatmap do not use mean with Min/Max Range because they are showing raw repetition spread, composition, or pass/fail status rather than one averaged line per load.
- For `proxy_tier_cpu_vs_load.png` and `proxy_tier_rss_vs_load.png`, each run first time-aligns the proxy/LB node metrics and sums them across the tier. The report line then shows the mean of those per-run totals across repetitions, so the plotted value is not a per-node median.

## Core comparison figures

- `throughput_vs_load.png`: the top-level throughput view. It shows how much useful work each technology completes as load rises. Each dot is one run; the line is the per-technology median across runs.
- `attempted_completed_success_error_rps.png`: separates target load, work actually attempted, work completed successfully, and work that failed so it is easy to see where a system starts falling behind.
- `error_rate_vs_load.png`: the simplest reliability view. It shows when errors begin to grow with load.
- `p95_latency_vs_load.png`: the main tail-latency view for normal service quality comparisons. Shows HDR-derived p95 per run (dots) with median line. All latency values are exact percentiles from merged HdrHistogram logs.
- `p99_latency_vs_load.png`: a stricter tail-latency view that highlights worse outliers than p95. Uses the same per-run HDR strip-plot format.
- `mean_failed_latency_vs_load.png`: shows how long failed requests took, which helps separate fast rejections from slow timeouts under load.
- `p95_latency_boxplot.png`: shows the full repetition-to-repetition spread of p95 latency at each load, instead of only the average.
- `p99_latency_boxplot.png`: shows the repetition spread for p99 latency so unstable tail behaviour is easier to spot.
- `throughput_boxplot.png`: shows the repetition spread of successful throughput at each load.
- `postgres_backend_connections_vs_load.png`: explains how much backend connection pressure reaches PostgreSQL as load rises.
- `rps_per_db_connection_vs_load.png`: shows how efficiently each backend connection is being used.
- `postgres_cpu_vs_load.png`: shows how much database CPU the workload costs.
- `postgres_rss_vs_load.png`: shows the database memory footprint seen by the operating system.
- `proxy_tier_cpu_vs_load.png`: shows total CPU cost across the proxy/application-tier nodes for technologies that actually have that tier.
- `proxy_tier_rss_vs_load.png`: shows total RSS memory footprint across the proxy/application-tier nodes for technologies that actually have that tier.
- `error_type_breakdown.png`: groups failures by kind so total error rate can be tied back to concrete failure modes.
- `slo_heatmap.png`: gives a quick pass/fail view against the configured p95 latency and error-rate thresholds.

## OJP heap diagnostics

OJP runs on the JVM, so RSS alone can overstate live application memory pressure. Java may retain committed heap for reuse, which means high RSS does not necessarily mean high live object usage. For that reason, Stressum reports RSS, heap used, heap committed, and heap max separately. RSS shows memory reserved from the operating system. Heap used shows active Java object memory. Heap committed shows memory retained by the JVM for reuse. Heap max shows the configured JVM ceiling.

- `ojp_heap_used_committed_vs_load.png`: keeps heap used and heap committed on the same graph so the gap between live object demand and JVM reserved space is easy to see. Each plotted value is the cluster total (sum of per-node medians).
- `ojp_heap_utilisation_vs_load.png`: shows how close OJP is to the configured JVM heap ceiling.
- `debug/ojp_heap_per_node_boxplot.png`: shows whether one OJP node uses materially more heap than the others at the same load.
