# Graph rationale

## Core comparison figures

- Throughput, latency, error-rate, backend-connection, and proxy/database resource graphs stay grouped by load level so repeated runs can be compared statistically.
- `summary_stats.csv` stores mean, median, stddev, min, max, and 95% confidence intervals for the report figures.
- `repetition_values.csv` keeps repetition-level raw values for boxplots and downstream analysis.

## OJP heap diagnostics

OJP runs on the JVM, so RSS alone can overstate live application memory pressure. Java may retain committed heap for reuse, which means high RSS does not necessarily mean high live object usage. For that reason, Stressum reports RSS, heap used, heap committed, and heap max separately. RSS shows memory reserved from the operating system. Heap used shows active Java object memory. Heap committed shows memory retained by the JVM for reuse. Heap max shows the configured JVM ceiling.

- `ojp_heap_used_vs_load.png`: shows live Java heap demand as load rises.
- `ojp_heap_committed_vs_load.png`: shows how much heap the JVM keeps reserved for reuse.
- `ojp_heap_used_committed_max_vs_load.png`: shows the relationship between live usage, retained heap, and configured heap ceiling.
- `ojp_heap_utilisation_vs_load.png`: shows how close OJP is to the configured JVM heap ceiling.
- `debug/ojp_heap_per_node_boxplot.png`: shows whether one OJP node uses materially more heap than the others at the same load.
