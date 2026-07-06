# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-05T08:06:40Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260705-085452` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 5.02 RPS (per instance) |
| **Total throughput** | 20.06 RPS (all instances) |
| **p50 latency** | 6.08 ms |
| **p95 latency** | 4676.62 ms |
| **p99 latency** | 17948.67 ms |
| **p999 latency** | 31621.25 ms |
| **Error rate** | 37.00% (0.37) |
| **Total requests** | 28836 |
| **Failed requests** | 10711 |
| **Total successful** | 18125 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 16.83 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 27421 |
| observed_client_backends_active_max | 40530 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | ojp-prod |
| Configured replicas | 4 |
| Configured client pool size (per replica) | 12 |
| OJP servers | 3 |
| Real DB connections per OJP server | 4 |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.8% / 4.9% / 13.7% / 19.6% / 34.2% |
| OJP proxy-tier host_cpu (avg / peak) | 16.2% / 137.4% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 67.50% |
| OJP proxy-tier RSS (avg / peak, summed) | 669.20 MiB / 670.80 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.8% / 4.9% / 13.7% / 19.6% / 34.2% |
| PgBouncer tier RSS (avg / peak, summed) | 669.20 MiB / 670.80 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.8% / 4.9% / 13.7% / 19.6% / 34.2% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 16.2% / 137.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 67.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 669.20 MiB / 670.80 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.43% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1056 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (4676.62 ms) |
| Error rate | < 0.1% | ❌ FAIL (37.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 31.88 RPS (all instances) |
| **Achieved throughput** | 20.06 RPS (all instances) |
| **Attempted − achieved gap** | 11.82 RPS (37.07%) |
| **Total attempted ops** | 28804 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.027 | 4198.399 | 19120.127 | 5.199387472458992 | 34.94% | 0.40060090135202797 | 309 |
| 1 | 6.071 | 5050.367 | 16400.383 | 4.92083089222608 | 38.14% | 0.45203415369161226 | 248 |
| 2 | 5.927 | 4714.495 | 18776.063 | 5.090916342783197 | 36.25% | 0.4007012522792204 | 267 |
| 3 | 6.303 | 4743.167 | 17498.111 | 4.8495327578687295 | 39.25% | 0.4514672970240375 | 232 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 2445 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | SQLException | 73 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 1 | SQLTransientConnectionException | 2630 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | SQLException | 120 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 2 | SQLTransientConnectionException | 2526 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | SQLException | 87 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 3 | SQLTransientConnectionException | 2732 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | SQLException | 98 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-05T08:06:40Z → 2026-07-05T08:21:40Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 24.6 | 41.0 | 0.572 | 106 | 0 |
| ojp-2 | 25.3 | 40.0 | 0.584 | 104 | 0 |
| ojp-3 | 24.7 | 40.0 | 0.544 | 109 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-05T08:06:40Z → 2026-07-05T08:21:40Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 27421 / 40530 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 558653452 | Cumulative since stats reset |
| Transactions rolled back | 5650 | Non-zero → contention or application errors |
| Temp file bytes written | -5 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 5 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7622 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 710704 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-05T08:06:40Z → 2026-07-05T08:21:40Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 2.0 | 1.9 | 5.9 | 9.8 | 26.4 | 5.3 | 3.9 | 9.8 | 34.5 | 40.2 | 224.9 | 225.6 |
| Proxy (OJP / pgBouncer) | ojp-2 | 2.1 | 2.0 | 6.8 | 10.7 | 18.6 | 5.8 | 3.9 | 11.8 | 35.5 | 64.0 | 222.3 | 222.8 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.9 | 1.0 | 5.9 | 9.8 | 22.5 | 5.4 | 3.9 | 10.7 | 34.5 | 42.0 | 222.0 | 222.4 |
| PostgreSQL | db | 211.5 | 212.9 | 343.4 | 364.3 | 368.6 | 356.2 | 399.5 | 400.0 | 400.0 | 400.0 | 6087.4 | 10310.9 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-05T08:24:20Z*
