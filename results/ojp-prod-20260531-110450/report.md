# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-31T10:17:19Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260531-110450` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.81 RPS (per instance) |
| **Total throughput** | 3.62 RPS (all instances) |
| **p50 latency** | 12.00 ms |
| **p95 latency** | 8372.20 ms |
| **p99 latency** | 28287.00 ms |
| **p999 latency** | 42385.40 ms |
| **Error rate** | 78.00% (0.78) |
| **Total requests** | 21617 |
| **Failed requests** | 16757 |
| **Total successful** | 4860 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 23 |
| observed_postgres_backends_avg_numbackends | 18.75 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 18282 |
| observed_client_backends_active_max | 26487 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.0% / 2.0% / 7.8% / 14.7% / 29.4% |
| OJP proxy-tier host_cpu (avg / peak) | 18.4% / 83.8% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 52.90% |
| OJP proxy-tier RSS (avg / peak, summed) | 680.30 MiB / 683.90 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.0% / 2.0% / 7.8% / 14.7% / 29.4% |
| PgBouncer tier RSS (avg / peak, summed) | 680.30 MiB / 683.90 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.0% / 2.0% / 7.8% / 14.7% / 29.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 18.4% / 83.8% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 52.90% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 680.30 MiB / 683.90 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.45% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 432 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (8372.20 ms) |
| Error rate | < 0.1% | ❌ FAIL (78.00%) |

## Open-Loop Sanity (2/2 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 16.10 RPS (all instances) |
| **Achieved throughput** | 3.62 RPS (all instances) |
| **Attempted − achieved gap** | 12.48 RPS (77.51%) |
| **Total attempted ops** | 28802 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.31 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 11.887 | 8208.383 | 25624.575 | 1.9157999598551811 | 76.15% | 0.5002501250625313 | 217 |
| 1 | 12.119 | 8536.063 | 30949.375 | 1.7054125746351438 | 78.88% | 0.4 | 215 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 656 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 0 | SQLTransientException | 6665 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 908 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 1 | SQLException | 716 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 1 | SQLTransientException | 7100 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 712 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-31T10:17:19Z → 2026-05-31T10:32:19Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 26.4 | 45.0 | 0.056 | 26 | 0 |
| ojp-2 | 29.3 | 45.0 | 0.081 | 39 | 0 |
| ojp-3 | 26.4 | 45.0 | 0.004 | 2 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-31T10:17:19Z → 2026-05-31T10:32:19Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 18282 / 26487 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 273551275 | Cumulative since stats reset |
| Transactions rolled back | 3902 | Non-zero → contention or application errors |
| Temp file bytes written | -2 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 2 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 11176 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 539641 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-31T10:17:19Z → 2026-05-31T10:32:19Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.2 | 1.0 | 3.9 | 7.8 | 15.7 | 5.0 | 3.9 | 10.7 | 34.3 | 63.4 | 228.3 | 229.5 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.2 | 1.0 | 2.9 | 9.8 | 27.4 | 4.1 | 3.9 | 5.9 | 18.7 | 35.5 | 228.0 | 229.6 |
| Proxy (OJP / pgBouncer) | ojp-3 | 0.6 | 0.0 | 2.0 | 3.9 | 9.8 | 9.7 | 3.9 | 34.3 | 49.0 | 52.9 | 224.0 | 224.8 |
| PostgreSQL | db | 112.4 | 98.3 | 211.8 | 221.6 | 226.5 | 378.9 | 398.0 | 400.0 | 400.0 | 400.0 | 18478.7 | 27654.2 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-31T10:35:11Z*
