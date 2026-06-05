# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-30T20:55:43Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260530-214320` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.44 RPS (per instance) |
| **Total throughput** | 2.88 RPS (all instances) |
| **p50 latency** | 16.07 ms |
| **p95 latency** | 19423.20 ms |
| **p99 latency** | 45596.65 ms |
| **p999 latency** | 64651.50 ms |
| **Error rate** | 46.00% (0.46) |
| **Total requests** | 7224 |
| **Failed requests** | 3345 |
| **Total successful** | 3879 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 25 |
| observed_postgres_backends_avg_numbackends | 20.05 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 19489 |
| observed_client_backends_active_max | 27883 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.0% / 2.0% / 9.8% / 17.6% / 31.3% |
| OJP proxy-tier host_cpu (avg / peak) | 18.4% / 111.8% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 64.60% |
| OJP proxy-tier RSS (avg / peak, summed) | 662.90 MiB / 668.00 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.0% / 2.0% / 9.8% / 17.6% / 31.3% |
| PgBouncer tier RSS (avg / peak, summed) | 662.90 MiB / 668.00 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.0% / 2.0% / 9.8% / 17.6% / 31.3% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 18.4% / 111.8% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 64.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 662.90 MiB / 668.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.30% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 234 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (19423.20 ms) |
| Error rate | < 0.1% | ❌ FAIL (46.00%) |

## Open-Loop Sanity (2/2 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 5.34 RPS (all instances) |
| **Achieved throughput** | 2.88 RPS (all instances) |
| **Attempted − achieved gap** | 2.46 RPS (46.13%) |
| **Total attempted ops** | 9602 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.26 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 16.031 | 18710.527 | 46039.039 | 1.5066431292390596 | 43.88% | 0.3501750875437719 | 124 |
| 1 | 16.119 | 20135.935 | 45154.303 | 1.3686249383860127 | 48.73% | 0.2503755633450175 | 110 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 42 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 0 | SQLTransientException | 1498 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 45 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLException | 39 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 1 | SQLTransientException | 1671 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 50 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-30T20:55:43Z → 2026-05-30T21:10:43Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 27.4 | 45.0 | 0.041 | 18 | 0 |
| ojp-2 | 24.8 | 40.0 | 0.051 | 22 | 0 |
| ojp-3 | 27.4 | 45.0 | 0.057 | 23 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-30T20:55:43Z → 2026-05-30T21:10:43Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 19489 / 27883 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 391013517 | Cumulative since stats reset |
| Transactions rolled back | 1751 | Non-zero → contention or application errors |
| Temp file bytes written | -7 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 7 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5532 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 561902 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-30T20:55:43Z → 2026-05-30T21:10:43Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.0 | 1.0 | 3.9 | 8.8 | 17.6 | 4.3 | 3.9 | 7.8 | 34.1 | 39.6 | 222.3 | 224.0 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.0 | 1.0 | 2.9 | 8.8 | 17.6 | 4.1 | 3.0 | 6.9 | 30.1 | 39.4 | 217.6 | 219.2 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.1 | 1.0 | 3.9 | 10.8 | 29.4 | 10.4 | 3.9 | 35.3 | 49.0 | 53.9 | 223.0 | 224.8 |
| PostgreSQL | db | 173.5 | 185.0 | 219.3 | 232.1 | 242.0 | 399.0 | 400.0 | 400.0 | 400.0 | 400.0 | 12434.3 | 21059.3 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-30T21:13:41Z*
