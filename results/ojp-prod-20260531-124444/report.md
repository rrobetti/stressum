# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-31T11:56:58Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260531-124444` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 2.33 RPS (per instance) |
| **Total throughput** | 4.67 RPS (all instances) |
| **p50 latency** | 20.22 ms |
| **p95 latency** | 12201.95 ms |
| **p99 latency** | 45662.20 ms |
| **p999 latency** | 61751.50 ms |
| **Error rate** | 71.00% (0.71) |
| **Total requests** | 21619 |
| **Failed requests** | 15327 |
| **Total successful** | 6292 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 25 |
| observed_postgres_backends_avg_numbackends | 20.41 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 19200 |
| observed_client_backends_active_max | 28811 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.6% / 2.9% / 9.8% / 18.6% / 31.3% |
| OJP proxy-tier host_cpu (avg / peak) | 19.0% / 78.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 66.50% |
| OJP proxy-tier RSS (avg / peak, summed) | 680.00 MiB / 684.80 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.6% / 2.9% / 9.8% / 18.6% / 31.3% |
| PgBouncer tier RSS (avg / peak, summed) | 680.00 MiB / 684.80 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.6% / 2.9% / 9.8% / 18.6% / 31.3% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 19.0% / 78.5% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 66.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 680.00 MiB / 684.80 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.48% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 495 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (12201.95 ms) |
| Error rate | < 0.1% | ❌ FAIL (71.00%) |

## Open-Loop Sanity (2/2 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 16.03 RPS (all instances) |
| **Achieved throughput** | 4.67 RPS (all instances) |
| **Attempted − achieved gap** | 11.36 RPS (70.87%) |
| **Total attempted ops** | 28802 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.35 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 21.023 | 14622.719 | 46235.647 | 2.3140542557635784 | 71.21% | 0.501002004008016 | 245 |
| 1 | 19.423 | 9781.247 | 45088.767 | 2.3558636103924786 | 70.59% | 0.4502251125562781 | 250 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 326 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 0 | SQLTransientException | 7159 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 213 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLException | 325 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 1 | SQLTransientException | 7082 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 222 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-31T11:56:58Z → 2026-05-31T12:11:58Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 28.9 | 45.0 | 0.060 | 28 | 0 |
| ojp-2 | 28.2 | 45.0 | 0.054 | 23 | 0 |
| ojp-3 | 29.4 | 45.0 | 0.056 | 26 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-31T11:56:58Z → 2026-05-31T12:11:58Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 19200 / 28811 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 345573590 | Cumulative since stats reset |
| Transactions rolled back | 4346 | Non-zero → contention or application errors |
| Temp file bytes written | -6 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 6 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 11713 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 539572 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-31T11:56:58Z → 2026-05-31T12:11:58Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.3 | 1.0 | 3.9 | 10.8 | 18.6 | 5.5 | 3.9 | 16.7 | 35.3 | 55.9 | 231.3 | 232.8 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.2 | 1.0 | 3.9 | 10.8 | 17.6 | 3.9 | 3.9 | 6.8 | 12.9 | 18.7 | 224.0 | 225.4 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.2 | 1.0 | 3.9 | 11.8 | 30.3 | 10.1 | 4.9 | 34.3 | 49.0 | 55.6 | 224.7 | 226.6 |
| PostgreSQL | db | 177.5 | 186.7 | 219.1 | 235.9 | 260.9 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 15038.5 | 26022.5 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-31T12:14:55Z*
