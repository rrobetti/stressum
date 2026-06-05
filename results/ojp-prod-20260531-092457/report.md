# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-31T08:37:17Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260531-092457` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 2.45 RPS (per instance) |
| **Total throughput** | 4.90 RPS (all instances) |
| **p50 latency** | 17.77 ms |
| **p95 latency** | 10952.70 ms |
| **p99 latency** | 43040.75 ms |
| **p999 latency** | 63881.00 ms |
| **Error rate** | 69.00% (0.69) |
| **Total requests** | 21622 |
| **Failed requests** | 15022 |
| **Total successful** | 6600 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 24 |
| observed_postgres_backends_avg_numbackends | 19.97 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 19427 |
| observed_client_backends_active_max | 29326 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.5% / 2.9% / 8.8% / 16.6% / 50.9% |
| OJP proxy-tier host_cpu (avg / peak) | 18.8% / 114.2% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 66.60% |
| OJP proxy-tier RSS (avg / peak, summed) | 675.50 MiB / 680.40 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.5% / 2.9% / 8.8% / 16.6% / 50.9% |
| PgBouncer tier RSS (avg / peak, summed) | 675.50 MiB / 680.40 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.5% / 2.9% / 8.8% / 16.6% / 50.9% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 18.8% / 114.2% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 66.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 675.50 MiB / 680.40 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.48% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 499 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (10952.70 ms) |
| Error rate | < 0.1% | ❌ FAIL (69.00%) |

## Open-Loop Sanity (2/2 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 16.04 RPS (all instances) |
| **Achieved throughput** | 4.90 RPS (all instances) |
| **Attempted − achieved gap** | 11.14 RPS (69.45%) |
| **Total attempted ops** | 28802 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.24 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 17.519 | 11026.431 | 44040.191 | 2.4949791613804315 | 68.99% | 0.501002004008016 | 251 |
| 1 | 18.031 | 10878.975 | 42041.343 | 2.40643118177486 | 69.96% | 0.4502251125562781 | 248 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 284 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 0 | SQLTransientException | 6968 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 207 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLException | 279 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 1 | SQLTransientException | 7058 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 226 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-31T08:37:17Z → 2026-05-31T08:52:17Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 27.6 | 45.0 | 0.059 | 29 | 0 |
| ojp-2 | 27.8 | 45.0 | 0.054 | 25 | 0 |
| ojp-3 | 24.0 | 40.0 | 0.064 | 32 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-31T08:37:17Z → 2026-05-31T08:52:17Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 19427 / 29326 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 431543573 | Cumulative since stats reset |
| Transactions rolled back | 4404 | Non-zero → contention or application errors |
| Temp file bytes written | -8 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 8 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 12004 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 539458 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-31T08:37:17Z → 2026-05-31T08:52:17Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.3 | 1.0 | 3.9 | 9.8 | 19.6 | 4.4 | 3.9 | 6.9 | 22.6 | 51.0 | 227.9 | 229.6 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.0 | 1.0 | 2.9 | 6.8 | 29.4 | 4.1 | 3.0 | 5.9 | 31.5 | 35.3 | 223.8 | 225.2 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.3 | 1.0 | 3.9 | 10.8 | 17.6 | 10.7 | 4.9 | 35.3 | 53.2 | 101.5 | 223.8 | 225.6 |
| PostgreSQL | db | 171.6 | 182.1 | 220.0 | 236.1 | 252.7 | 399.2 | 400.0 | 400.0 | 400.0 | 400.0 | 13263.7 | 20452.7 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-31T08:55:09Z*
