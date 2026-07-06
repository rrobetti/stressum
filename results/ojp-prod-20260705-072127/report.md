# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-05T06:33:21Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260705-072127` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 5.43 RPS (per instance) |
| **Total throughput** | 21.72 RPS (all instances) |
| **p50 latency** | 5.60 ms |
| **p95 latency** | 4788.20 ms |
| **p99 latency** | 11390.98 ms |
| **p999 latency** | 31740.00 ms |
| **Error rate** | 32.00% (0.32) |
| **Total requests** | 28806 |
| **Failed requests** | 9192 |
| **Total successful** | 19614 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 17.14 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 28417 |
| observed_client_backends_active_max | 42482 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.8% / 4.9% / 11.8% / 18.6% / 36.2% |
| OJP proxy-tier host_cpu (avg / peak) | 17.5% / 72.3% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 55.80% |
| OJP proxy-tier RSS (avg / peak, summed) | 688.60 MiB / 691.80 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.8% / 4.9% / 11.8% / 18.6% / 36.2% |
| PgBouncer tier RSS (avg / peak, summed) | 688.60 MiB / 691.80 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.8% / 4.9% / 11.8% / 18.6% / 36.2% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 17.5% / 72.3% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 55.80% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 688.60 MiB / 691.80 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.48% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1132 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (4788.20 ms) |
| Error rate | < 0.1% | ❌ FAIL (32.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 31.90 RPS (all instances) |
| **Achieved throughput** | 21.72 RPS (all instances) |
| **Attempted − achieved gap** | 10.18 RPS (31.91%) |
| **Total attempted ops** | 28803 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 5.367 | 4665.343 | 11263.999 | 5.57055707778688 | 29.95% | 0.4511278195488722 | 276 |
| 1 | 5.839 | 4841.471 | 12279.807 | 5.470070661095525 | 31.61% | 0.5012531328320802 | 321 |
| 2 | 5.459 | 4669.439 | 10182.655 | 5.44615698411713 | 31.77% | 0.45090180360721444 | 278 |
| 3 | 5.751 | 4976.639 | 11837.439 | 5.233510844874534 | 34.31% | 0.5007511266900351 | 257 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 1830 | Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 0 | SQLException | 327 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 1 | SQLTransientConnectionException | 1940 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLException | 336 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 2 | SQLTransientConnectionException | 1944 | Timeout waiting for fast operation slot for operation: e9cb50da3e8545 |
| 2 | SQLException | 344 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 3 | SQLTransientConnectionException | 2109 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 3 | SQLException | 362 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-05T06:33:21Z → 2026-07-05T06:48:21Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 26.8 | 40.0 | 0.596 | 116 | 0 |
| ojp-2 | 28.4 | 46.0 | 0.218 | 89 | 0 |
| ojp-3 | 29.2 | 48.0 | 0.215 | 87 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-05T06:33:21Z → 2026-07-05T06:48:21Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 28417 / 42482 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 580213588 | Cumulative since stats reset |
| Transactions rolled back | 5545 | Non-zero → contention or application errors |
| Temp file bytes written | 6 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -6 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7682 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 758602 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-05T06:33:21Z → 2026-07-05T06:48:21Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 2.2 | 2.0 | 6.9 | 13.7 | 19.6 | 5.5 | 3.9 | 10.8 | 33.5 | 41.2 | 219.3 | 219.8 |
| Proxy (OJP / pgBouncer) | ojp-2 | 2.0 | 2.0 | 5.9 | 9.8 | 18.6 | 5.6 | 3.9 | 10.8 | 35.1 | 60.5 | 218.8 | 220.4 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.7 | 1.0 | 3.9 | 8.8 | 17.6 | 6.8 | 3.9 | 33.5 | 36.3 | 57.8 | 250.5 | 251.6 |
| PostgreSQL | db | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-05T06:50:58Z*
