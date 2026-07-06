# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-05T12:47:36Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260705-133544` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 5.06 RPS (per instance) |
| **Total throughput** | 20.25 RPS (all instances) |
| **p50 latency** | 6.50 ms |
| **p95 latency** | 3564.55 ms |
| **p99 latency** | 7361.55 ms |
| **p999 latency** | 18919.42 ms |
| **Error rate** | 57.00% (0.57) |
| **Total requests** | 43219 |
| **Failed requests** | 24570 |
| **Total successful** | 18649 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 16.85 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 27846 |
| observed_client_backends_active_max | 41372 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.0% / 4.9% / 12.7% / 17.6% / 31.3% |
| OJP proxy-tier host_cpu (avg / peak) | 15.3% / 95.1% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 62.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 706.50 MiB / 707.70 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.0% / 4.9% / 12.7% / 17.6% / 31.3% |
| PgBouncer tier RSS (avg / peak, summed) | 706.50 MiB / 707.70 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.0% / 4.9% / 12.7% / 17.6% / 31.3% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 15.3% / 95.1% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 62.70% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 706.50 MiB / 707.70 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.48% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1206 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (3564.55 ms) |
| Error rate | < 0.1% | ❌ FAIL (57.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.92 RPS (all instances) |
| **Achieved throughput** | 20.25 RPS (all instances) |
| **Attempted − achieved gap** | 26.66 RPS (56.83%) |
| **Total attempted ops** | 43203 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.631 | 3336.191 | 6811.647 | 4.895463587362959 | 57.95% | 0.4012036108324975 | 306 |
| 1 | 7.131 | 3817.471 | 7012.351 | 4.899309367958862 | 58.00% | 0.5007511266900351 | 294 |
| 2 | 5.823 | 3733.503 | 7798.783 | 5.265325936649588 | 54.92% | 0.4506760140210316 | 306 |
| 3 | 6.431 | 3371.007 | 7823.359 | 5.192789781544706 | 56.52% | 0.5513784461152882 | 300 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 5711 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | SQLException | 551 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 1 | SQLTransientConnectionException | 5724 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | SQLException | 544 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 2 | SQLTransientConnectionException | 5410 | Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 2 | SQLException | 523 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 3 | SQLTransientConnectionException | 5560 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 3 | SQLException | 547 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-05T12:47:36Z → 2026-07-05T13:02:36Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 24.8 | 40.0 | 0.119 | 53 | 0 |
| ojp-2 | 25.3 | 41.0 | 0.727 | 123 | 0 |
| ojp-3 | 26.8 | 41.0 | 0.720 | 134 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-05T12:47:36Z → 2026-07-05T13:02:36Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 27846 / 41372 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 561263539 | Cumulative since stats reset |
| Transactions rolled back | 6251 | Non-zero → contention or application errors |
| Temp file bytes written | 6 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -6 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 10833 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 770862 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-05T12:47:36Z → 2026-07-05T13:02:36Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.3 | 1.0 | 3.9 | 6.8 | 18.6 | 4.9 | 3.9 | 7.9 | 34.3 | 92.2 | 239.6 | 240.2 |
| Proxy (OJP / pgBouncer) | ojp-2 | 2.5 | 2.0 | 5.9 | 9.8 | 23.5 | 5.1 | 4.9 | 8.9 | 11.9 | 25.6 | 225.6 | 225.9 |
| Proxy (OJP / pgBouncer) | ojp-3 | 2.4 | 2.0 | 6.9 | 10.7 | 20.6 | 5.6 | 4.9 | 10.8 | 34.3 | 43.6 | 241.3 | 241.6 |
| PostgreSQL | db | 213.5 | 209.8 | 343.4 | 360.8 | 365.2 | 375.0 | 399.5 | 400.0 | 400.0 | 400.0 | 7347.3 | 10718.8 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-05T13:05:30Z*
