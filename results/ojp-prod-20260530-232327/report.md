# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-30T22:35:47Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260530-232327` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.47 RPS (per instance) |
| **Total throughput** | 2.93 RPS (all instances) |
| **p50 latency** | 15.20 ms |
| **p95 latency** | 22675.45 ms |
| **p99 latency** | 45039.60 ms |
| **p999 latency** | 64569.50 ms |
| **Error rate** | 45.00% (0.45) |
| **Total requests** | 7225 |
| **Failed requests** | 3260 |
| **Total successful** | 3965 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 25 |
| observed_postgres_backends_avg_numbackends | 20.24 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 19012 |
| observed_client_backends_active_max | 27425 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.0% / 2.0% / 9.8% / 15.7% / 32.3% |
| OJP proxy-tier host_cpu (avg / peak) | 19.2% / 94.0% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 56.80% |
| OJP proxy-tier RSS (avg / peak, summed) | 674.00 MiB / 678.80 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.0% / 2.0% / 9.8% / 15.7% / 32.3% |
| PgBouncer tier RSS (avg / peak, summed) | 674.00 MiB / 678.80 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.0% / 2.0% / 9.8% / 15.7% / 32.3% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 19.2% / 94.0% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 56.80% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 674.00 MiB / 678.80 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.30% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 239 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (22675.45 ms) |
| Error rate | < 0.1% | ❌ FAIL (45.00%) |

## Open-Loop Sanity (2/2 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 5.33 RPS (all instances) |
| **Achieved throughput** | 2.93 RPS (all instances) |
| **Attempted − achieved gap** | 2.39 RPS (44.95%) |
| **Total attempted ops** | 9602 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.38 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 16.607 | 22740.991 | 42696.703 | 1.4170140791738128 | 46.97% | 0.30045067601402103 | 109 |
| 1 | 13.799 | 22609.919 | 47382.527 | 1.514936430339541 | 43.27% | 0.3003003003003003 | 130 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 44 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 0 | SQLTransientException | 1597 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 56 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLException | 47 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 1 | SQLTransientException | 1467 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 49 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-30T22:35:47Z → 2026-05-30T22:50:47Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 27.0 | 45.0 | 0.035 | 18 | 0 |
| ojp-2 | 24.5 | 45.0 | 0.046 | 22 | 0 |
| ojp-3 | 27.0 | 43.0 | 0.058 | 23 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-30T22:35:47Z → 2026-05-30T22:50:47Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 19012 / 27425 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 387327236 | Cumulative since stats reset |
| Transactions rolled back | 1676 | Non-zero → contention or application errors |
| Temp file bytes written | -8 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 9 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5182 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 526338 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-30T22:35:47Z → 2026-05-30T22:50:47Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.0 | 1.0 | 3.9 | 9.8 | 19.6 | 4.6 | 3.9 | 9.8 | 33.3 | 43.4 | 226.6 | 228.3 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.0 | 1.0 | 2.9 | 9.8 | 18.6 | 4.4 | 3.0 | 8.9 | 33.5 | 38.2 | 222.7 | 224.2 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.0 | 1.0 | 3.9 | 9.8 | 18.6 | 10.6 | 3.9 | 35.5 | 50.2 | 69.6 | 224.7 | 226.3 |
| PostgreSQL | db | 171.2 | 183.0 | 222.3 | 233.5 | 238.6 | 398.9 | 400.0 | 400.0 | 400.0 | 400.0 | 12220.2 | 20695.1 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-30T22:53:48Z*
