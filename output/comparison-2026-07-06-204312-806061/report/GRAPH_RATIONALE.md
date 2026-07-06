# Graph rationale

## How to read the line graphs

- The main line in a line graph is the mean across the five repetitions at that load level.
- The shaded band above and below a line is the 95% confidence interval. In simple words, it shows the range where the true average is likely to sit based on the five repeated runs.
- Narrower shaded bands mean the repetitions were more consistent. Wider bands mean the result moved around more from run to run.

## Where mean ± 95% CI is used

- Mean ± 95% CI is used in these report line graphs: `throughput_vs_load.png`, `error_rate_vs_load.png`, `p95_latency_vs_load.png`, `p99_latency_vs_load.png`, `mean_failed_latency_vs_load.png`, `postgres_backend_connections_vs_load.png`, `rps_per_db_connection_vs_load.png`, `postgres_cpu_vs_load.png`, `postgres_rss_vs_load.png`, `proxy_tier_cpu_vs_load.png`, `proxy_tier_rss_vs_load.png`, and `ojp_heap_utilisation_vs_load.png`.
- Mean ± 95% CI is also used in the measured panels of `attempted_completed_success_error_rps.png`: attempted RPS, successful RPS, and error RPS. The offered RPS panel does not use a confidence interval because it is the configured target load, not an observed metric with run to run variation.
- The combined OJP heap report graph (`ojp_heap_used_committed_vs_load.png`) shows mean lines without shaded bands to keep the two JVM series easy to compare on one view.
- Boxplots, the error breakdown chart, and the SLO heatmap do not use mean ± 95% CI because they are showing raw repetition spread, composition, or pass/fail status rather than one averaged line per load.
- `summary_stats.csv` stores mean, median, stddev, min, max, and 95% confidence intervals for the report metrics, while `repetition_values.csv` keeps the repetition-level raw values used by the boxplots and downstream analysis.

## Core comparison figures

- `throughput_vs_load.png`: the top-level throughput view. It shows how much useful work each technology completes as load rises.
- `attempted_completed_success_error_rps.png`: separates target load, work actually attempted, work completed successfully, and work that failed so it is easy to see where a system starts falling behind.
- `error_rate_vs_load.png`: the simplest reliability view. It shows when errors begin to grow with load.
- `p95_latency_vs_load.png`: the main tail-latency view for normal service quality comparisons.
- `p99_latency_vs_load.png`: a stricter tail-latency view that highlights worse outliers than p95.
- `mean_failed_latency_vs_load.png`: shows how long failed requests took, which helps separate fast rejections from slow timeouts under load.
- `p95_latency_boxplot.png`: shows the full repetition-to-repetition spread of p95 latency at each load, instead of only the average.
- `p99_latency_boxplot.png`: shows the repetition spread for p99 latency so unstable tail behaviour is easier to spot.
- `throughput_boxplot.png`: shows the repetition spread of successful throughput at each load.
- `postgres_backend_connections_vs_load.png`: explains how much backend connection pressure reaches PostgreSQL as load rises.
- `rps_per_db_connection_vs_load.png`: shows how efficiently each backend connection is being used.
- `postgres_cpu_vs_load.png`: shows how much database CPU the workload costs.
- `postgres_rss_vs_load.png`: shows the database memory footprint seen by the operating system.
- `proxy_tier_cpu_vs_load.png`: shows CPU cost in the proxy/application tier for technologies that actually have that tier.
- `proxy_tier_rss_vs_load.png`: shows the proxy/application-tier RSS memory footprint for technologies that actually have that tier.
- `error_type_breakdown.png`: groups failures by kind so total error rate can be tied back to concrete failure modes.
- `slo_heatmap.png`: gives a quick pass/fail view against the configured p95 latency and error-rate thresholds.

## OJP heap diagnostics

OJP runs on the JVM, so RSS alone can overstate live application memory pressure. Java may retain committed heap for reuse, which means high RSS does not necessarily mean high live object usage. For that reason, Stressum reports RSS, heap used, heap committed, and heap max separately. RSS shows memory reserved from the operating system. Heap used shows active Java object memory. Heap committed shows memory retained by the JVM for reuse. Heap max shows the configured JVM ceiling.

- `ojp_heap_used_committed_vs_load.png`: keeps heap used and heap committed on the same graph so the gap between live object demand and JVM reserved space is easy to see.
- `ojp_heap_utilisation_vs_load.png`: shows how close OJP is to the configured JVM heap ceiling.
- `debug/ojp_heap_per_node_boxplot.png`: shows whether one OJP node uses materially more heap than the others at the same load.
