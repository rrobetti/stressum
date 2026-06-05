# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-30T19:15:48Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260530-200328` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.35 RPS (per instance) |
| **Total throughput** | 2.71 RPS (all instances) |
| **p50 latency** | 17.54 ms |
| **p95 latency** | 22200.30 ms |
| **p99 latency** | 55787.50 ms |
| **p999 latency** | 64192.50 ms |
| **Error rate** | 49.00% (0.49) |
| **Total requests** | 7227 |
| **Failed requests** | 3566 |
| **Total successful** | 3661 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 24 |
| observed_postgres_backends_avg_numbackends | 20.48 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 18766 |
| observed_client_backends_active_max | 27061 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 2.9% / 2.0% / 8.8% / 15.7% / 32.3% |
| OJP proxy-tier host_cpu (avg / peak) | 17.5% / 87.2% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 51.90% |
| OJP proxy-tier RSS (avg / peak, summed) | 671.30 MiB / 676.30 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 2.9% / 2.0% / 8.8% / 15.7% / 32.3% |
| PgBouncer tier RSS (avg / peak, summed) | 671.30 MiB / 676.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 2.9% / 2.0% / 8.8% / 15.7% / 32.3% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 17.5% / 87.2% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 51.90% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 671.30 MiB / 676.30 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.28% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 225 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (22200.30 ms) |
| Error rate | < 0.1% | ❌ FAIL (49.00%) |

## Open-Loop Sanity (2/2 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 5.33 RPS (all instances) |
| **Achieved throughput** | 2.71 RPS (all instances) |
| **Attempted − achieved gap** | 2.62 RPS (49.17%) |
| **Total attempted ops** | 9602 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.26 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 17.471 | 22085.631 | 51544.063 | 1.381068656310989 | 48.21% | 0.3006012024048096 | 116 |
| 1 | 17.599 | 22315.007 | 60030.975 | 1.3266482121747765 | 50.47% | 0.2503755633450175 | 109 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 48 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 0 | SQLTransientException | 1617 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 77 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLException | 62 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 1 | SQLTransientException | 1697 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 65 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-30T19:15:48Z → 2026-05-30T19:30:48Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 28.4 | 45.0 | 0.032 | 15 | 0 |
| ojp-2 | 26.0 | 45.0 | 0.042 | 19 | 0 |
| ojp-3 | 26.2 | 43.0 | 0.051 | 22 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-30T19:15:48Z → 2026-05-30T19:30:48Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 18766 / 27061 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 354741548 | Cumulative since stats reset |
| Transactions rolled back | 1693 | Non-zero → contention or application errors |
| Temp file bytes written | -9 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 9 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5454 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 553774 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-30T19:15:48Z → 2026-05-30T19:30:48Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.0 | 1.0 | 3.9 | 8.8 | 18.6 | 3.8 | 3.0 | 6.9 | 11.8 | 33.3 | 225.5 | 227.2 |
| Proxy (OJP / pgBouncer) | ojp-2 | 0.9 | 1.0 | 2.9 | 8.8 | 14.7 | 4.0 | 3.0 | 6.9 | 15.8 | 34.3 | 224.7 | 226.2 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.1 | 1.0 | 3.9 | 11.7 | 18.6 | 10.1 | 3.9 | 34.3 | 49.0 | 56.6 | 221.1 | 222.9 |
| PostgreSQL | db | 170.9 | 184.2 | 221.3 | 230.0 | 234.3 | 398.8 | 400.0 | 400.0 | 400.0 | 400.0 | 15340.2 | 25612.3 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-30T19:33:49Z*
