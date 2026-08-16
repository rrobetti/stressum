# postgres_backend_connections_vs_load.png

Numbers used in the chart.

## Axis 1

- title: Observed PostgreSQL backend connections vs load — multiple scenarios

- x_label: Load (per-node RPS / aggregate RPS)

- y_label: Observed PostgreSQL backend connections

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
| 50 | 50 |
| 100 | 100 |
| 150 | 150 |
| 200 | 200 |
| 250 | 250 |
| 300 | 300 |
| 350 | 350 |

### Line 1: HikariCP

| x | y |
| --- | --- |
| 16 | 151.5 |
| 32 | 306.2 |
| 48 | 312 |
| 64 | 312 |

### Line 2: OJP

| x | y |
| --- | --- |
| 16 | 49 |
| 32 | 52 |
| 48 | 52.4 |
| 64 | 52.6 |

### Line 3: PgBouncer

| x | y |
| --- | --- |
| 16 | 49 |
| 32 | 54.6 |
| 48 | 56 |
| 64 | 56 |

### Collection 1 offsets: Min/Max Range

| x | y |
| --- | --- |
| 0 | 0 |

### Collection 1 paths: Min/Max Range

| path | vertex | x | y |
| --- | --- | --- | --- |
| 1 | 1 | 16 | 152 |
| 1 | 2 | 16 | 151 |
| 1 | 3 | 32 | 288 |
| 1 | 4 | 48 | 312 |
| 1 | 5 | 64 | 312 |
| 1 | 6 | 64 | 312 |
| 1 | 7 | 64 | 312 |
| 1 | 8 | 48 | 312 |
| 1 | 9 | 32 | 311 |
| 1 | 10 | 16 | 152 |
| 1 | 11 | 16 | 152 |

### Collection 2 offsets: unlabeled

| x | y |
| --- | --- |
| 0 | 0 |

### Collection 2 paths: unlabeled

| path | vertex | x | y |
| --- | --- | --- | --- |
| 1 | 1 | 16 | 49 |
| 1 | 2 | 16 | 49 |
| 1 | 3 | 32 | 52 |
| 1 | 4 | 48 | 52 |
| 1 | 5 | 64 | 52 |
| 1 | 6 | 64 | 53 |
| 1 | 7 | 64 | 53 |
| 1 | 8 | 48 | 53 |
| 1 | 9 | 32 | 52 |
| 1 | 10 | 16 | 49 |
| 1 | 11 | 16 | 49 |

### Collection 3 offsets: unlabeled

| x | y |
| --- | --- |
| 0 | 0 |

### Collection 3 paths: unlabeled

| path | vertex | x | y |
| --- | --- | --- | --- |
| 1 | 1 | 16 | 49 |
| 1 | 2 | 16 | 49 |
| 1 | 3 | 32 | 50 |
| 1 | 4 | 48 | 56 |
| 1 | 5 | 64 | 56 |
| 1 | 6 | 64 | 56 |
| 1 | 7 | 64 | 56 |
| 1 | 8 | 48 | 56 |
| 1 | 9 | 32 | 56 |
| 1 | 10 | 16 | 49 |
| 1 | 11 | 16 | 49 |

