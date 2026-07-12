# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-12T02:46:43Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260712-033451` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 2.38 RPS (per instance) |
| **Total throughput** | 9.52 RPS (all instances) |
| **p50 latency** | 12.71 ms |
| **p95 latency** | 4447.75 ms |
| **p99 latency** | 32487.50 ms |
| **p999 latency** | 158531.75 ms |
| **Error rate** | 70.00% (0.70) |
| **Total requests** | 29117 |
| **Failed requests** | 20338 |
| **Total successful** | 8779 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 26 |
| observed_postgres_backends_avg_numbackends | 16.67 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 26172 |
| observed_client_backends_active_max | 38463 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.1% / 3.9% / 17.6% / 36.2% / 67.2% |
| OJP proxy-tier host_cpu (avg / peak) | 17.9% / 102.9% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 112.10% |
| OJP proxy-tier RSS (avg / peak, summed) | 666.20 MiB / 678.50 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.1% / 3.9% / 17.6% / 36.2% / 67.2% |
| PgBouncer tier RSS (avg / peak, summed) | 666.20 MiB / 678.50 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.1% / 3.9% / 17.6% / 36.2% / 67.2% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 17.9% / 102.9% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 112.10% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 666.20 MiB / 678.50 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.29% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 821 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (4447.75 ms) |
| Error rate | < 0.1% | ❌ FAIL (70.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 31.18 RPS (all instances) |
| **Achieved throughput** | 9.52 RPS (all instances) |
| **Attempted − achieved gap** | 21.66 RPS (69.47%) |
| **Total attempted ops** | 28803 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 11.023 | 3897.343 | 9674.751 | 3.1685022026431717 | 60.84% | 0.35070140280561124 | 219 |
| 1 | 9.055 | 4235.263 | 27246.591 | 2.252046263249467 | 71.15% | 0.2506265664160401 | 188 |
| 2 | 18.287 | 4898.815 | 17399.807 | 2.1015146847512542 | 73.15% | 0.2506265664160401 | 173 |
| 3 | 12.487 | 4759.551 | 75628.543 | 1.9983823643294127 | 74.38% | 0.3003003003003003 | 241 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 4469 | Server overloaded: too many concurrent requests |
| 1 | SQLTransientConnectionException | 5162 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | SQLTransientConnectionException | 5314 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | SQLTransientConnectionException | 5393 | Client throttle limit reached; request rejected to avoid overloading the database |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-12T02:46:43Z → 2026-07-12T03:01:43Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 25.5 | 40.0 | 0.017 | 6 | 0 |
| ojp-2 | 26.7 | 40.0 | 0.056 | 23 | 0 |
| ojp-3 | 26.2 | 41.0 | 1.326 | 213 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-12T02:46:43Z → 2026-07-12T03:01:43Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 26172 / 38463 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 286026048 | Cumulative since stats reset |
| Transactions rolled back | 3901 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5248 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 533960 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-12T02:46:43Z → 2026-07-12T03:01:43Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 0.5 | 0.0 | 2.0 | 5.9 | 16.6 | 3.9 | 2.9 | 6.9 | 33.2 | 35.3 | 217.3 | 217.9 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.1 | 0.0 | 5.9 | 22.5 | 43.8 | 4.7 | 2.9 | 14.6 | 34.3 | 72.5 | 221.5 | 224.7 |
| Proxy (OJP / pgBouncer) | ojp-3 | 4.6 | 2.9 | 14.7 | 20.6 | 51.7 | 9.8 | 5.9 | 34.3 | 48.3 | 96.0 | 227.4 | 235.9 |
| PostgreSQL | db | 47.3 | 2.6 | 177.5 | 250.7 | 295.2 | 288.0 | 340.5 | 400.0 | 400.0 | 400.0 | 5452.5 | 9005.5 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-12T03:04:51Z*
