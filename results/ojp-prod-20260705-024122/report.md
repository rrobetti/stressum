# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-05T01:53:18Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260705-024122` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.76 RPS (per instance) |
| **Total throughput** | 15.02 RPS (all instances) |
| **p50 latency** | 6.25 ms |
| **p95 latency** | 4303.35 ms |
| **p99 latency** | 9805.80 ms |
| **p999 latency** | 18612.22 ms |
| **Error rate** | 6.00% (0.06) |
| **Total requests** | 14451 |
| **Failed requests** | 816 |
| **Total successful** | 13635 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 16.25 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 21521 |
| observed_client_backends_active_max | 32682 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.8% / 3.9% / 10.8% / 19.6% / 31.4% |
| OJP proxy-tier host_cpu (avg / peak) | 17.0% / 76.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 66.60% |
| OJP proxy-tier RSS (avg / peak, summed) | 661.00 MiB / 663.70 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.8% / 3.9% / 10.8% / 19.6% / 31.4% |
| PgBouncer tier RSS (avg / peak, summed) | 661.00 MiB / 663.70 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.8% / 3.9% / 10.8% / 19.6% / 31.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 17.0% / 76.5% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 66.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 661.00 MiB / 663.70 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.36% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 645 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (4303.35 ms) |
| Error rate | < 0.1% | ❌ FAIL (6.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.87 RPS (all instances) |
| **Achieved throughput** | 15.02 RPS (all instances) |
| **Attempted − achieved gap** | 0.85 RPS (5.34%) |
| **Total attempted ops** | 14404 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.327 | 3553.279 | 8912.895 | 3.7497435082772363 | 5.77% | 0.3009027081243731 | 160 |
| 1 | 6.339 | 4550.655 | 9887.743 | 3.758607276778286 | 5.70% | 0.4008016032064128 | 167 |
| 2 | 6.039 | 4620.287 | 10428.415 | 3.756726906305141 | 5.51% | 0.35070140280561124 | 165 |
| 3 | 6.287 | 4489.215 | 9994.239 | 3.7596844952154984 | 5.62% | 0.40060090135202797 | 153 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 168 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 0 | SQLException | 40 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 1 | SQLTransientConnectionException | 162 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | SQLException | 44 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 2 | SQLTransientConnectionException | 162 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | SQLException | 37 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 3 | SQLTransientConnectionException | 171 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | SQLException | 32 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-05T01:53:18Z → 2026-07-05T02:08:18Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 26.6 | 41.0 | 0.383 | 81 | 0 |
| ojp-2 | 24.9 | 40.0 | 0.336 | 79 | 0 |
| ojp-3 | 25.5 | 40.0 | 0.319 | 79 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-05T01:53:18Z → 2026-07-05T02:08:18Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 21521 / 32682 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 421135341 | Cumulative since stats reset |
| Transactions rolled back | 3835 | Non-zero → contention or application errors |
| Temp file bytes written | -11 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 11 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4833 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 340925 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-05T01:53:18Z → 2026-07-05T02:08:18Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.6 | 1.0 | 4.9 | 9.8 | 17.6 | 4.8 | 3.9 | 7.9 | 29.4 | 50.7 | 221.9 | 222.8 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.6 | 1.0 | 4.9 | 9.8 | 23.5 | 7.6 | 3.9 | 34.1 | 39.0 | 62.1 | 219.5 | 220.1 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.6 | 1.0 | 4.9 | 8.8 | 25.5 | 5.0 | 3.9 | 9.8 | 34.3 | 39.0 | 219.6 | 220.8 |
| PostgreSQL | db | 158.4 | 165.3 | 302.5 | 322.4 | 332.4 | 319.2 | 396.5 | 400.0 | 400.0 | 400.0 | 6195.6 | 10410.3 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-05T02:10:56Z*
