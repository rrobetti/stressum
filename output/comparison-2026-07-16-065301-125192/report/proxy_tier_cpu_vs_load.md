# proxy_tier_cpu_vs_load.png

Numbers used in the chart.

## Axis 1

- title: Proxy-tier total CPU across nodes vs load — multiple scenarios

- x_label: Load (per-node RPS / aggregate RPS)

- y_label: Proxy-tier total CPU across nodes (%)

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
| 0 | 0 |
| 2 | 2 |
| 4 | 4 |
| 6 | 6 |
| 8 | 8 |
| 10 | 10 |
| 12 | 12 |
| 14 | 14 |

### Line 1: OJP

| x | y |
| --- | --- |
| 16 | 7.2939533672 |
| 32 | 8.7938316655 |
| 48 | 10.0869769828 |
| 64 | 10.7848254189 |

### Line 2: PgBouncer

| x | y |
| --- | --- |
| 16 | 1.38269948894 |
| 32 | 1.25594538203 |
| 48 | 1.44520440257 |
| 64 | 1.43598465956 |

### Collection 1 offsets: Min/Max Range

| x | y |
| --- | --- |
| 0 | 0 |

### Collection 1 paths: Min/Max Range

| path | vertex | x | y |
| --- | --- | --- | --- |
| 1 | 1 | 16 | 7.63484743811 |
| 1 | 2 | 16 | 7.09516705069 |
| 1 | 3 | 32 | 8.62870553936 |
| 1 | 4 | 48 | 8.93065676756 |
| 1 | 5 | 64 | 9.54413142857 |
| 1 | 6 | 64 | 11.9684982739 |
| 1 | 7 | 64 | 11.9684982739 |
| 1 | 8 | 48 | 10.5964953811 |
| 1 | 9 | 32 | 8.99523920653 |
| 1 | 10 | 16 | 7.63484743811 |
| 1 | 11 | 16 | 7.63484743811 |

### Collection 2 offsets: unlabeled

| x | y |
| --- | --- |
| 0 | 0 |

### Collection 2 paths: unlabeled

| path | vertex | x | y |
| --- | --- | --- | --- |
| 1 | 1 | 16 | 1.42607122343 |
| 1 | 2 | 16 | 1.34113662457 |
| 1 | 3 | 32 | 1.18659758204 |
| 1 | 4 | 48 | 1.37240226629 |
| 1 | 5 | 64 | 1.41563719862 |
| 1 | 6 | 64 | 1.46467045455 |
| 1 | 7 | 64 | 1.46467045455 |
| 1 | 8 | 48 | 1.49403579677 |
| 1 | 9 | 32 | 1.4352710496 |
| 1 | 10 | 16 | 1.42607122343 |
| 1 | 11 | 16 | 1.42607122343 |

