# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-14T22:53:03Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260714-234103` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.95 RPS (per instance) |
| **Total throughput** | 15.28 RPS (all instances) |
| **p50 latency** | 6.24 ms |
| **p95 latency** | 5221.64 ms |
| **p99 latency** | 30739.38 ms |
| **p999 latency** | 52893.62 ms |
| **Error rate** | 2.00% (0.02) |
| **Total requests** | 14452 |
| **Failed requests** | 218 |
| **Total successful** | 14234 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 56 |
| observed_postgres_backends_avg_numbackends | 52.03 |
| observed_postgres_backends_median_numbackends | 52 |
| observed_client_backends_active_median | 31286 |
| observed_client_backends_active_max | 47460 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.4% / 5.9% / 13.7% / 22.5% / 38.1% |
| OJP proxy-tier host_cpu (avg / peak) | 19.5% / 79.2% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 77.10% |
| OJP proxy-tier RSS (avg / peak, summed) | 1149.30 MiB / 1176.30 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.4% / 5.9% / 13.7% / 22.5% / 38.1% |
| PgBouncer tier RSS (avg / peak, summed) | 1149.30 MiB / 1176.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.4% / 5.9% / 13.7% / 22.5% / 38.1% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 19.5% / 79.2% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 77.10% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 1149.30 MiB / 1176.30 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.05% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 613 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (5221.64 ms) |
| Error rate | < 0.1% | ❌ FAIL (2.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.47 RPS (all instances) |
| **Achieved throughput** | 15.28 RPS (all instances) |
| **Attempted − achieved gap** | 0.19 RPS (1.24%) |
| **Total attempted ops** | 14407 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.995 | 5697.535 | 23609.343 | 0.9561333709797479 | 0.89% | 0.03755163349605708 | 35 |
| 10 | 6.935 | 1581.055 | 32980.991 | 0.9475753407955783 | 1.88% | 0.03755163349605708 | 35 |
| 11 | 5.519 | 7364.607 | 34045.951 | 0.9559017805550245 | 1.55% | 0.050043788314775434 | 41 |
| 12 | 6.087 | 6115.327 | 34340.863 | 0.9518523153005447 | 1.44% | 0.03754693366708385 | 34 |
| 13 | 7.491 | 729.087 | 34045.951 | 0.9515567209613737 | 2.21% | 0.05003752814610958 | 41 |
| 14 | 5.739 | 47.519 | 33193.983 | 0.9494028557435106 | 2.43% | 0.050031269543464665 | 35 |
| 15 | 6.035 | 57.375 | 33538.047 | 0.9494038777012801 | 2.43% | 0.05003752814610958 | 41 |
| 1 | 6.695 | 6201.343 | 24461.311 | 0.9541903074803386 | 1.22% | 0.050043788314775434 | 45 |
| 2 | 5.395 | 7118.847 | 29310.975 | 0.9569655804211293 | 1.44% | 0.03754223501439119 | 33 |
| 3 | 6.015 | 6512.639 | 28524.543 | 0.9515409826239412 | 1.55% | 0.04379145151976087 | 40 |
| 4 | 6.295 | 7020.543 | 27607.039 | 0.9590927047598339 | 1.33% | 0.03754693366708385 | 37 |
| 5 | 5.675 | 3979.263 | 31457.279 | 0.9633973588918885 | 0.89% | 0.05003752814610958 | 47 |
| 6 | 6.955 | 9068.543 | 28671.999 | 0.9657457013525835 | 1.00% | 0.05002501250625312 | 33 |
| 7 | 5.815 | 8814.591 | 30867.455 | 0.9576394830893965 | 1.33% | 0.050043788314775434 | 41 |
| 8 | 6.571 | 6914.047 | 32948.223 | 0.9529248697348495 | 1.22% | 0.05002501250625312 | 34 |
| 9 | 5.659 | 6324.223 | 32227.327 | 0.9554314292975381 | 1.33% | 0.043785973086668484 | 41 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 8 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 10 | SQLTransientConnectionException | 17 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 11 | SQLTransientConnectionException | 14 | Timeout waiting for fast operation slot for operation: f891f847dfafb38c |
| 12 | SQLTransientConnectionException | 13 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 13 | SQLTransientConnectionException | 20 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 14 | SQLTransientConnectionException | 22 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 15 | SQLTransientConnectionException | 22 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 1 | SQLTransientConnectionException | 11 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 2 | SQLTransientConnectionException | 13 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 3 | SQLTransientConnectionException | 14 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 4 | SQLTransientConnectionException | 12 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 5 | SQLTransientConnectionException | 8 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 6 | SQLTransientConnectionException | 9 | Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 7 | SQLTransientConnectionException | 12 | Connection admission timeout for hash: aHOSqngG4Q5gGB3v_yO2tnMrfevlSwgapbfCQ1r0rIA after 30000ms (phase=admission) |
| 8 | SQLTransientConnectionException | 11 | Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 9 | SQLTransientConnectionException | 12 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-14T22:53:03Z → 2026-07-14T23:08:03Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 30.6 | 50.0 | 0.117 | 80 | 0 |
| ojp-2 | 29.3 | 48.0 | 0.146 | 77 | 0 |
| ojp-3 | 30.8 | 50.0 | 0.172 | 93 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-14T22:53:03Z → 2026-07-14T23:08:03Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 52 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 31286 / 47460 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1242978820 | Cumulative since stats reset |
| Transactions rolled back | 721 | Non-zero → contention or application errors |
| Temp file bytes written | 1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1963 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 197794 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-14T22:53:03Z → 2026-07-14T23:08:03Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 2.1 | 2.0 | 4.9 | 14.7 | 21.5 | 7.4 | 4.9 | 33.3 | 37.2 | 65.6 | 373.6 | 379.8 |
| Proxy (OJP / pgBouncer) | ojp-2 | 2.2 | 2.0 | 5.9 | 13.7 | 36.1 | 6.0 | 4.9 | 14.7 | 35.2 | 39.2 | 401.4 | 413.8 |
| Proxy (OJP / pgBouncer) | ojp-3 | 2.2 | 1.9 | 5.9 | 10.7 | 19.5 | 6.5 | 4.9 | 12.8 | 36.1 | 66.3 | 374.3 | 382.7 |
| PostgreSQL | db | 404.1 | 425.8 | 979.4 | 1131.4 | 1198.5 | 1105.4 | 1129.8 | 1596.2 | 1597.1 | 1598.4 | 20027.1 | 63976.2 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-14T23:12:07Z*
