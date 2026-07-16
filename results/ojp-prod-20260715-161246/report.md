# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T15:24:24Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 3 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260715-161246` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 2.40 RPS (per instance) |
| **Total throughput** | 38.47 RPS (all instances) |
| **p50 latency** | 4.71 ms |
| **p95 latency** | 38.83 ms |
| **p99 latency** | 36122.69 ms |
| **p999 latency** | 45784.88 ms |
| **Error rate** | 17.00% (0.17) |
| **Total requests** | 43309 |
| **Failed requests** | 7518 |
| **Total successful** | 35791 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 57 |
| observed_postgres_backends_avg_numbackends | 53.29 |
| observed_postgres_backends_median_numbackends | 53 |
| observed_client_backends_active_median | 55189 |
| observed_client_backends_active_max | 82834 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | ojp-prod |
| Configured replicas | 16 |
| Configured client pool size (per replica) | 48 |
| OJP servers | 3 |
| Real DB connections per OJP server | 16 |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 9.7% / 8.8% / 17.6% / 20.6% / 24.5% |
| OJP proxy-tier host_cpu (avg / peak) | 28.5% / 103.7% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 40.10% |
| OJP proxy-tier RSS (avg / peak, summed) | 1155.50 MiB / 1163.40 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 9.7% / 8.8% / 17.6% / 20.6% / 24.5% |
| PgBouncer tier RSS (avg / peak, summed) | 1155.50 MiB / 1163.40 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 9.7% / 8.8% / 17.6% / 20.6% / 24.5% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 28.5% / 103.7% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 40.10% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 1155.50 MiB / 1163.40 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.07% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1299 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ✅ PASS (38.83 ms) |
| Error rate | < 0.1% | ❌ FAIL (17.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.45 RPS (all instances) |
| **Achieved throughput** | 38.47 RPS (all instances) |
| **Attempted − achieved gap** | 7.98 RPS (17.18%) |
| **Total attempted ops** | 43212 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 4.671 | 51.551 | 34930.687 | 2.3767881003647418 | 18.32% | 0.06257822277847308 | 76 |
| 10 | 4.215 | 29.007 | 35946.495 | 2.367404443386546 | 18.46% | 0.06256256256256257 | 68 |
| 11 | 4.859 | 36.959 | 38305.791 | 2.353342464959975 | 18.92% | 0.0750703787736191 | 84 |
| 12 | 4.443 | 35.999 | 36306.943 | 2.488849780446354 | 14.71% | 0.06257039169065198 | 75 |
| 13 | 5.727 | 35.711 | 38338.559 | 2.3032028041977104 | 20.64% | 0.06258605582676179 | 84 |
| 14 | 4.643 | 50.335 | 39845.887 | 2.340036405359007 | 19.87% | 0.06257822277847308 | 69 |
| 15 | 6.075 | 37.471 | 36339.711 | 2.2785700113011895 | 21.97% | 0.07507507507507508 | 84 |
| 1 | 4.783 | 49.823 | 35160.063 | 2.4241784040088947 | 16.89% | 0.07506568247216314 | 87 |
| 2 | 4.203 | 46.079 | 35061.759 | 2.5484435064607447 | 12.33% | 0.06257039169065198 | 78 |
| 3 | 4.351 | 34.815 | 34045.951 | 2.5032014572668517 | 13.82% | 0.07507977255192873 | 95 |
| 4 | 4.591 | 36.127 | 35356.671 | 2.4903231623669235 | 14.26% | 0.06881570479781703 | 83 |
| 5 | 4.775 | 34.591 | 35422.207 | 2.3832420903332565 | 18.12% | 0.0750938673341677 | 95 |
| 6 | 4.291 | 36.639 | 35815.423 | 2.4107306442436576 | 16.82% | 0.06257822277847308 | 77 |
| 7 | 4.431 | 37.567 | 35618.815 | 2.447872184407809 | 16.17% | 0.06259389083625437 | 84 |
| 8 | 4.391 | 33.503 | 35880.959 | 2.3991109303709157 | 17.62% | 0.06257039169065198 | 77 |
| 9 | 4.847 | 35.039 | 35586.047 | 2.355278427556972 | 18.80% | 0.06259389083625437 | 83 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 496 | Client throttle limit reached; request rejected to avoid overloading the database |
| 10 | SQLTransientConnectionException | 500 | Client throttle limit reached; request rejected to avoid overloading the database |
| 11 | SQLTransientConnectionException | 512 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 12 | SQLTransientConnectionException | 398 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 13 | SQLTransientConnectionException | 558 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 14 | SQLTransientConnectionException | 538 | Client throttle limit reached; request rejected to avoid overloading the database |
| 15 | SQLTransientConnectionException | 595 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | SQLTransientConnectionException | 457 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 2 | SQLTransientConnectionException | 334 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | SQLTransientConnectionException | 374 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 4 | SQLTransientConnectionException | 386 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 5 | SQLTransientConnectionException | 491 | Client throttle limit reached; request rejected to avoid overloading the database |
| 6 | SQLTransientConnectionException | 455 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 7 | SQLTransientConnectionException | 438 | Client throttle limit reached; request rejected to avoid overloading the database |
| 8 | SQLTransientConnectionException | 477 | Client throttle limit reached; request rejected to avoid overloading the database |
| 9 | SQLTransientConnectionException | 509 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-15T15:24:24Z → 2026-07-15T15:39:24Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 30.4 | 52.0 | 0.414 | 174 | 0 |
| ojp-2 | 31.5 | 56.0 | 0.342 | 138 | 0 |
| ojp-3 | 33.1 | 56.0 | 0.424 | 164 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T15:24:24Z → 2026-07-15T15:39:24Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 53 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 55189 / 82834 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2354604550 | Cumulative since stats reset |
| Transactions rolled back | 1366 | Non-zero → contention or application errors |
| Temp file bytes written | 7 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -6 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4903 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 491895 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T15:24:24Z → 2026-07-15T15:39:24Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 3.3 | 2.9 | 7.8 | 10.8 | 13.7 | 6.1 | 4.9 | 10.8 | 33.4 | 41.3 | 397.9 | 402.5 |
| Proxy (OJP / pgBouncer) | ojp-2 | 3.2 | 2.9 | 7.8 | 10.8 | 13.7 | 13.1 | 6.8 | 37.2 | 47.1 | 67.4 | 380.8 | 382.6 |
| Proxy (OJP / pgBouncer) | ojp-3 | 3.4 | 2.9 | 7.8 | 10.8 | 12.7 | 10.0 | 5.9 | 36.2 | 40.1 | 63.5 | 376.8 | 378.3 |
| PostgreSQL | db | 757.0 | 744.8 | 998.0 | 1055.6 | 1157.1 | 1408.8 | 1455.4 | 1597.0 | 1598.6 | 1598.8 | 19660.0 | 29000.6 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T15:43:20Z*
