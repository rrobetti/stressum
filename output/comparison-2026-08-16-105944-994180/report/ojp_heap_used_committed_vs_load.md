# ojp_heap_used_committed_vs_load.png

Numbers used in the chart.

## Axis 1

- title: OJP heap used and committed vs load — multiple scenarios

- x_label: Load (per-node RPS / aggregate RPS)

- y_label: Cluster OJP heap (MiB, sum of per-node medians)

### X ticks

| value | label |
| --- | --- |
| 16 | 1/node<br>16 agg |
| 32 | 2/node<br>32 agg |
| 48 | 3/node<br>48 agg |
| 64 | 4/node<br>64 agg |

### Y ticks

| value | label |
| --- | --- |
| 80 | 80 |
| 90 | 90 |
| 100 | 100 |
| 110 | 110 |
| 120 | 120 |
| 130 | 130 |
| 140 | 140 |
| 150 | 150 |
| 160 | 160 |
| 170 | 170 |

### Line 1: Heap used (sum of per-node medians)

| x | y |
| --- | --- |
| 16 | 88.646 |
| 32 | 88.454 |
| 48 | 90.531 |
| 64 | 90.307 |

### Line 2: Heap committed (sum of per-node medians)

| x | y |
| --- | --- |
| 16 | 150.4 |
| 32 | 150.8 |
| 48 | 159.4 |
| 64 | 160.8 |

