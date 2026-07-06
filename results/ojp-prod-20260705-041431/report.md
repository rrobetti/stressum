# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-05T03:26:20Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260705-041431` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.73 RPS (per instance) |
| **Total throughput** | 14.92 RPS (all instances) |
| **p50 latency** | 5.92 ms |
| **p95 latency** | 4803.07 ms |
| **p99 latency** | 10246.12 ms |
| **p999 latency** | 25890.75 ms |
| **Error rate** | 6.00% (0.06) |
| **Total requests** | 14452 |
| **Failed requests** | 905 |
| **Total successful** | 13547 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 16.05 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 21961 |
| observed_client_backends_active_max | 32996 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.9% / 3.9% / 11.7% / 18.6% / 31.3% |
| OJP proxy-tier host_cpu (avg / peak) | 14.3% / 72.4% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 73.50% |
| OJP proxy-tier RSS (avg / peak, summed) | 666.60 MiB / 669.10 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.9% / 3.9% / 11.7% / 18.6% / 31.3% |
| PgBouncer tier RSS (avg / peak, summed) | 666.60 MiB / 669.10 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.9% / 3.9% / 11.7% / 18.6% / 31.3% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 14.3% / 72.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 73.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 666.60 MiB / 669.10 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.34% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 639 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (4803.07 ms) |
| Error rate | < 0.1% | ❌ FAIL (6.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.87 RPS (all instances) |
| **Achieved throughput** | 14.92 RPS (all instances) |
| **Attempted − achieved gap** | 0.94 RPS (5.95%) |
| **Total attempted ops** | 14403 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 5.659 | 4118.527 | 9535.487 | 3.7394717114256735 | 6.09% | 0.3007518796992481 | 161 |
| 1 | 5.735 | 4882.431 | 9682.943 | 3.7093476884941854 | 6.89% | 0.35070140280561124 | 152 |
| 2 | 5.863 | 4988.927 | 11149.311 | 3.74885320470914 | 5.62% | 0.30075187969924816 | 161 |
| 3 | 6.419 | 5222.399 | 10616.831 | 3.723350332115357 | 6.45% | 0.4006009013520281 | 165 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 179 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 0 | SQLException | 41 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 1 | SQLTransientConnectionException | 200 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLException | 49 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 2 | SQLTransientConnectionException | 166 | Timeout waiting for fast operation slot for operation: e98e4f987f09ed4e |
| 2 | SQLException | 37 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 3 | SQLTransientConnectionException | 193 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 3 | SQLException | 40 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-05T03:26:20Z → 2026-07-05T03:41:20Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 24.2 | 40.0 | 0.397 | 85 | 0 |
| ojp-2 | 27.4 | 41.0 | 0.353 | 84 | 0 |
| ojp-3 | 24.4 | 40.0 | 0.394 | 79 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-05T03:26:20Z → 2026-07-05T03:41:20Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 21961 / 32996 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 423184270 | Cumulative since stats reset |
| Transactions rolled back | 3895 | Non-zero → contention or application errors |
| Temp file bytes written | -9 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 9 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4704 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 333969 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-05T03:26:20Z → 2026-07-05T03:41:20Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.7 | 1.0 | 4.9 | 9.8 | 25.5 | 5.2 | 3.9 | 10.8 | 34.3 | 37.2 | 217.1 | 218.0 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.7 | 1.0 | 5.8 | 8.8 | 27.4 | 4.4 | 3.9 | 7.9 | 11.7 | 32.2 | 230.3 | 231.3 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.6 | 1.0 | 4.9 | 8.8 | 20.6 | 5.0 | 3.9 | 8.9 | 34.5 | 37.2 | 219.2 | 219.8 |
| PostgreSQL | db | 153.9 | 153.8 | 304.6 | 328.4 | 358.6 | 316.5 | 396.1 | 400.0 | 400.0 | 400.0 | 6452.6 | 10162.9 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-05T03:43:57Z*
