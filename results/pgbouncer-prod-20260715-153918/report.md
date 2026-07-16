# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T14:51:14Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 3 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260715-153918` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.63 RPS (per instance) |
| **Total throughput** | 26.08 RPS (all instances) |
| **p50 latency** | 29876.19 ms |
| **p95 latency** | 46815.19 ms |
| **p99 latency** | 80695.62 ms |
| **p999 latency** | 103919.38 ms |
| **Error rate** | 45.00% (0.45) |
| **Total requests** | 44633 |
| **Failed requests** | 20246 |
| **Total successful** | 24387 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 59 |
| observed_postgres_backends_avg_numbackends | 55.93 |
| observed_postgres_backends_median_numbackends | 56 |
| observed_client_backends_active_median | 40549 |
| observed_client_backends_active_max | 60802 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | pgbouncer-prod |
| Configured replicas | 16 |
| Configured client pool size (per replica) | 20 |
| OJP servers | N/A |
| Real DB connections per OJP server | N/A |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.9% / 1.0% / 2.9% / 4.9% / 9.8% |
| OJP proxy-tier host_cpu (avg / peak) | 16.9% / 80.3% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 20.50% |
| OJP proxy-tier RSS (avg / peak, summed) | 35.20 MiB / 35.20 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 16 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.9% / 1.0% / 2.9% / 4.9% / 9.8% |
| PgBouncer tier RSS (avg / peak, summed) | 35.20 MiB / 35.20 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.0% / 1.0% / 2.9% / 4.9% / 10.7% |
| HAProxy RSS (avg / peak, summed) | 23.10 MiB / 23.20 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.8% / 1.0% / 5.8% / 9.7% / 20.5% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 21.9% / 96.7% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 31.20% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 58.30 MiB / 58.40 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.03% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 27 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (46815.19 ms) |
| Error rate | < 0.1% | ❌ FAIL (45.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.22 RPS (all instances) |
| **Achieved throughput** | 26.08 RPS (all instances) |
| **Attempted − achieved gap** | 20.14 RPS (43.57%) |
| **Total attempted ops** | 43215 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29933.567 | 50298.879 | 90701.823 | 1.6395599177332363 | 45.15% | 0.02501876407305479 | 2 |
| 10 | 29704.191 | 43909.119 | 81395.711 | 1.7293969677264793 | 42.15% | 0.025021894157387717 | 2 |
| 11 | 29884.415 | 47153.151 | 79691.775 | 1.629934321347327 | 45.49% | 0.02502815667626079 | 2 |
| 12 | 30031.871 | 46465.023 | 76152.831 | 1.682340346115056 | 43.76% | 0.025021894157387717 | 1 |
| 13 | 29736.959 | 43646.975 | 67960.831 | 1.7090781138536932 | 42.91% | 0.025025025025025023 | 2 |
| 14 | 29802.495 | 46333.951 | 95027.199 | 1.5925014465132348 | 46.30% | 0.025021894157387717 | 2 |
| 15 | 29999.103 | 47710.207 | 94765.055 | 1.5721773801107797 | 47.35% | 0.025025025025025023 | 1 |
| 1 | 30162.943 | 48365.567 | 86441.983 | 1.5486515074218696 | 48.16% | 0.025025025025025023 | 1 |
| 2 | 29523.967 | 48562.175 | 74252.287 | 1.7507909040155893 | 41.31% | 0.025021894157387717 | 2 |
| 3 | 29736.959 | 46301.183 | 86179.839 | 1.6919659425009654 | 43.24% | 0.02502815667626079 | 2 |
| 4 | 29966.335 | 48365.567 | 75628.543 | 1.6053355750277807 | 46.26% | 0.02501876407305479 | 1 |
| 5 | 29753.343 | 46694.399 | 74973.183 | 1.5807385193250096 | 46.49% | 0.025025025025025023 | 2 |
| 6 | 29851.647 | 43909.119 | 73007.103 | 1.6181697035423266 | 45.79% | 0.02501876407305479 | 2 |
| 7 | 30588.927 | 48857.087 | 79560.703 | 1.5112186325877774 | 49.35% | 0.025025025025025023 | 2 |
| 8 | 29982.719 | 46727.167 | 70909.951 | 1.5422344431645967 | 48.30% | 0.02501876407305479 | 1 |
| 9 | 29360.127 | 45744.127 | 84475.903 | 1.678062303276874 | 43.80% | 0.025021894157387717 | 2 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 1262 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=85) |
| 10 | SQLTransientConnectionException | 1178 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=88) |
| 11 | SQLTransientConnectionException | 1272 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=88) |
| 12 | SQLTransientConnectionException | 1224 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=90) |
| 13 | SQLTransientConnectionException | 1201 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=87) |
| 14 | SQLTransientConnectionException | 1284 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=13, active=13, idle=0, waiting=71) |
| 15 | SQLTransientConnectionException | 1322 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=90) |
| 1 | SQLTransientConnectionException | 1345 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=86) |
| 2 | SQLTransientConnectionException | 1152 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=10, active=10, idle=0, waiting=83) |
| 3 | SQLTransientConnectionException | 1205 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=86) |
| 4 | SQLTransientConnectionException | 1292 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=90) |
| 5 | SQLTransientConnectionException | 1284 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=58) |
| 6 | SQLTransientConnectionException | 1278 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=86) |
| 7 | SQLTransientConnectionException | 1377 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=87) |
| 8 | SQLTransientConnectionException | 1347 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=80) |
| 9 | SQLTransientConnectionException | 1223 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=87) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T14:51:14Z → 2026-07-15T15:06:14Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 56 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 40549 / 60802 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2816395872 | Cumulative since stats reset |
| Transactions rolled back | 1192 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5817 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 402144 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T14:51:14Z → 2026-07-15T15:06:14Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.3 | 0.0 | 1.0 | 2.9 | 3.9 | 3.9 | 2.9 | 6.8 | 33.3 | 43.2 | 11.7 | 11.7 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.3 | 0.0 | 1.9 | 2.9 | 6.8 | 9.8 | 3.9 | 33.3 | 37.2 | 73.4 | 11.7 | 11.7 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.3 | 0.0 | 1.9 | 2.9 | 9.8 | 3.6 | 2.9 | 4.9 | 32.3 | 67.5 | 11.8 | 11.8 |
| PostgreSQL | db | 1417.6 | 1418.7 | 1493.5 | 1537.5 | 1557.3 | 1599.3 | 1599.3 | 1599.8 | 1600.0 | 1600.0 | 146556.5 | 152315.0 |
| HAProxy | lb | 1.0 | 1.0 | 2.9 | 4.9 | 10.7 | 5.1 | 3.9 | 9.8 | 35.0 | 53.7 | 23.1 | 23.2 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T15:10:05Z*
