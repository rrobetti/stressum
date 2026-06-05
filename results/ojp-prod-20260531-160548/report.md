# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-31T15:18:18Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260531-160548` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 2.49 RPS (per instance) |
| **Total throughput** | 4.98 RPS (all instances) |
| **p50 latency** | 16.84 ms |
| **p95 latency** | 12386.30 ms |
| **p99 latency** | 39338.00 ms |
| **p999 latency** | 60162.00 ms |
| **Error rate** | 69.00% (0.69) |
| **Total requests** | 21620 |
| **Failed requests** | 14876 |
| **Total successful** | 6744 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 25 |
| observed_postgres_backends_avg_numbackends | 20.26 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 19239 |
| observed_client_backends_active_max | 29057 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.6% / 2.9% / 9.8% / 16.7% / 23.5% |
| OJP proxy-tier host_cpu (avg / peak) | 13.8% / 68.4% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 59.80% |
| OJP proxy-tier RSS (avg / peak, summed) | 677.20 MiB / 682.40 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.6% / 2.9% / 9.8% / 16.7% / 23.5% |
| PgBouncer tier RSS (avg / peak, summed) | 677.20 MiB / 682.40 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.6% / 2.9% / 9.8% / 16.7% / 23.5% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 13.8% / 68.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 59.80% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 677.20 MiB / 682.40 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.48% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 507 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (12386.30 ms) |
| Error rate | < 0.1% | ❌ FAIL (69.00%) |

## Open-Loop Sanity (2/2 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.94 RPS (all instances) |
| **Achieved throughput** | 4.98 RPS (all instances) |
| **Attempted − achieved gap** | 10.97 RPS (68.78%) |
| **Total attempted ops** | 28802 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.23 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 17.455 | 12591.103 | 38731.775 | 2.4826110219368647 | 68.88% | 0.501002004008016 | 248 |
| 1 | 16.231 | 12181.503 | 39944.191 | 2.4944557400157192 | 68.74% | 0.4502251125562781 | 259 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 356 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 0 | SQLTransientException | 6820 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 269 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLException | 360 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 1 | SQLTransientException | 6822 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 249 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-31T15:18:18Z → 2026-05-31T15:33:18Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 27.7 | 45.0 | 0.050 | 26 | 0 |
| ojp-2 | 26.3 | 43.0 | 0.081 | 38 | 0 |
| ojp-3 | 27.9 | 45.0 | 0.059 | 27 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-31T15:18:18Z → 2026-05-31T15:33:18Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 19239 / 29057 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 375615650 | Cumulative since stats reset |
| Transactions rolled back | 4247 | Non-zero → contention or application errors |
| Temp file bytes written | -4 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 4 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 11537 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 539935 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-31T15:18:18Z → 2026-05-31T15:33:18Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.2 | 1.0 | 3.9 | 10.8 | 18.6 | 4.4 | 3.9 | 7.8 | 26.5 | 37.1 | 223.2 | 224.9 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.2 | 1.0 | 3.9 | 9.8 | 19.6 | 5.2 | 3.9 | 13.7 | 35.3 | 38.2 | 230.9 | 232.8 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.2 | 1.0 | 3.9 | 10.8 | 21.6 | 4.5 | 3.9 | 7.8 | 32.5 | 59.1 | 223.1 | 224.7 |
| PostgreSQL | db | 165.8 | 180.2 | 214.4 | 229.1 | 231.6 | 399.8 | 400.0 | 400.0 | 400.0 | 400.0 | 18212.0 | 26565.7 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-31T15:36:22Z*
