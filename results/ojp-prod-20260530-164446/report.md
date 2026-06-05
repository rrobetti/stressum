# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-30T15:57:03Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260530-164446` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.52 RPS (per instance) |
| **Total throughput** | 3.03 RPS (all instances) |
| **p50 latency** | 13.95 ms |
| **p95 latency** | 19603.45 ms |
| **p99 latency** | 46088.20 ms |
| **p999 latency** | 62685.00 ms |
| **Error rate** | 44.00% (0.44) |
| **Total requests** | 7237 |
| **Failed requests** | 3180 |
| **Total successful** | 4057 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 25 |
| observed_postgres_backends_avg_numbackends | 20.26 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 19404 |
| observed_client_backends_active_max | 27906 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | ojp-prod |
| Configured replicas | 2 |
| Configured client pool size (per replica) | 15 |
| OJP servers | 3 |
| Real DB connections per OJP server | 5 |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.0% / 2.0% / 8.8% / 16.6% / 30.4% |
| OJP proxy-tier host_cpu (avg / peak) | 19.2% / 83.3% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 69.30% |
| OJP proxy-tier RSS (avg / peak, summed) | 674.30 MiB / 679.20 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.0% / 2.0% / 8.8% / 16.6% / 30.4% |
| PgBouncer tier RSS (avg / peak, summed) | 674.30 MiB / 679.20 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.0% / 2.0% / 8.8% / 16.6% / 30.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 19.2% / 83.3% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 69.30% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 674.30 MiB / 679.20 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.33% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 232 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (19603.45 ms) |
| Error rate | < 0.1% | ❌ FAIL (44.00%) |

## Open-Loop Sanity (2/2 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 5.38 RPS (all instances) |
| **Achieved throughput** | 3.03 RPS (all instances) |
| **Attempted − achieved gap** | 2.35 RPS (43.67%) |
| **Total attempted ops** | 9602 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.31 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 14.351 | 18907.135 | 43352.063 | 1.5560747454001624 | 42.44% | 0.35052578868302453 | 127 |
| 1 | 13.551 | 20299.775 | 48824.319 | 1.4762911380672323 | 45.44% | 0.3 | 105 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 53 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 0 | SQLTransientException | 1382 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 100 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLException | 56 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 1 | SQLTransientException | 1491 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 98 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-30T15:57:03Z → 2026-05-30T16:12:03Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 29.0 | 45.0 | 0.042 | 19 | 0 |
| ojp-2 | 28.6 | 45.0 | 0.041 | 18 | 0 |
| ojp-3 | 27.3 | 45.0 | 0.051 | 23 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-30T15:57:03Z → 2026-05-30T16:12:03Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 19404 / 27906 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 335724197 | Cumulative since stats reset |
| Transactions rolled back | 1666 | Non-zero → contention or application errors |
| Temp file bytes written | -9 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 9 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5073 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 514174 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-30T15:57:03Z → 2026-05-30T16:12:03Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.1 | 1.0 | 3.9 | 9.8 | 26.4 | 6.0 | 3.9 | 31.4 | 35.3 | 49.8 | 222.5 | 224.2 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.0 | 1.0 | 3.9 | 8.8 | 17.5 | 3.9 | 3.0 | 6.9 | 14.7 | 35.1 | 224.0 | 225.5 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.1 | 1.0 | 3.9 | 8.8 | 25.4 | 9.7 | 3.9 | 34.5 | 38.4 | 74.5 | 227.8 | 229.5 |
| PostgreSQL | db | 163.1 | 179.8 | 221.1 | 228.2 | 253.9 | 396.0 | 400.0 | 400.0 | 400.0 | 400.0 | 12395.6 | 21375.3 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-30T16:14:46Z*
