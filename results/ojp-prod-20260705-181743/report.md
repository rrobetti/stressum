# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-05T17:29:36Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260705-181743` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.95 RPS (per instance) |
| **Total throughput** | 19.81 RPS (all instances) |
| **p50 latency** | 5.55 ms |
| **p95 latency** | 3802.62 ms |
| **p99 latency** | 10502.15 ms |
| **p999 latency** | 45015.25 ms |
| **Error rate** | 57.00% (0.57) |
| **Total requests** | 43429 |
| **Failed requests** | 24908 |
| **Total successful** | 18521 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 24 |
| observed_postgres_backends_avg_numbackends | 16.50 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 33560 |
| observed_client_backends_active_max | 47077 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.4% / 4.9% / 15.7% / 28.3% / 37.1% |
| OJP proxy-tier host_cpu (avg / peak) | 22.4% / 75.2% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 79.10% |
| OJP proxy-tier RSS (avg / peak, summed) | 707.70 MiB / 709.00 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.4% / 4.9% / 15.7% / 28.3% / 37.1% |
| PgBouncer tier RSS (avg / peak, summed) | 707.70 MiB / 709.00 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.4% / 4.9% / 15.7% / 28.3% / 37.1% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 22.4% / 75.2% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 79.10% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 707.70 MiB / 709.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.58% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1599 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (3802.62 ms) |
| Error rate | < 0.1% | ❌ FAIL (57.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.21 RPS (all instances) |
| **Achieved throughput** | 19.81 RPS (all instances) |
| **Attempted − achieved gap** | 26.40 RPS (57.13%) |
| **Total attempted ops** | 43203 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.259 | 4550.655 | 12263.423 | 4.728251220832112 | 59.07% | 0.5513784461152882 | 395 |
| 1 | 5.367 | 3614.719 | 10379.263 | 5.086549413645771 | 56.43% | 0.6009013520280421 | 400 |
| 2 | 5.443 | 3588.095 | 9412.607 | 5.159170682563415 | 55.30% | 0.6009013520280421 | 404 |
| 3 | 5.143 | 3457.023 | 9953.279 | 4.834141875647048 | 58.61% | 0.551654964894684 | 400 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 5650 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | SQLException | 730 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 1 | SQLTransientConnectionException | 5454 | Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 1 | SQLException | 706 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 2 | SQLTransientConnectionException | 5306 | Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 2 | SQLException | 661 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 3 | SQLTransientConnectionException | 5653 | Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 3 | SQLException | 748 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-05T17:29:36Z → 2026-07-05T17:44:36Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 27.8 | 41.0 | 0.028 | 8 | 0 |
| ojp-2 | 25.9 | 41.0 | 0.897 | 138 | 0 |
| ojp-3 | 24.8 | 40.0 | 1.154 | 212 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-05T17:29:36Z → 2026-07-05T17:44:36Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 33560 / 47077 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 554760994 | Cumulative since stats reset |
| Transactions rolled back | 5700 | Non-zero → contention or application errors |
| Temp file bytes written | 3 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -3 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 9186 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 806743 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-05T17:29:36Z → 2026-07-05T17:44:36Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 0.5 | 0.0 | 2.0 | 6.8 | 17.6 | 10.1 | 3.9 | 33.5 | 37.1 | 63.4 | 239.9 | 240.4 |
| Proxy (OJP / pgBouncer) | ojp-2 | 2.8 | 2.0 | 8.8 | 15.7 | 27.4 | 6.2 | 4.9 | 14.6 | 33.5 | 38.2 | 226.1 | 226.4 |
| Proxy (OJP / pgBouncer) | ojp-3 | 3.2 | 2.0 | 9.8 | 17.6 | 34.1 | 6.6 | 4.9 | 15.6 | 35.5 | 47.3 | 241.7 | 242.2 |
| PostgreSQL | db | 167.3 | 164.9 | 317.7 | 343.9 | 378.5 | 345.0 | 393.6 | 400.0 | 400.0 | 400.0 | 6849.3 | 10189.3 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-05T17:47:43Z*
