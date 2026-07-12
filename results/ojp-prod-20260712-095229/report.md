# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-12T09:04:23Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260712-095229` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.80 RPS (per instance) |
| **Total throughput** | 19.21 RPS (all instances) |
| **p50 latency** | 5.69 ms |
| **p95 latency** | 4633.60 ms |
| **p99 latency** | 24444.90 ms |
| **p999 latency** | 79159.25 ms |
| **Error rate** | 40.00% (0.40) |
| **Total requests** | 28999 |
| **Failed requests** | 11702 |
| **Total successful** | 17297 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 16.34 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 26911 |
| observed_client_backends_active_max | 40762 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.7% / 4.9% / 13.7% / 23.5% / 33.3% |
| OJP proxy-tier host_cpu (avg / peak) | 14.5% / 57.6% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 86.20% |
| OJP proxy-tier RSS (avg / peak, summed) | 676.10 MiB / 677.90 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.7% / 4.9% / 13.7% / 23.5% / 33.3% |
| PgBouncer tier RSS (avg / peak, summed) | 676.10 MiB / 677.90 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.7% / 4.9% / 13.7% / 23.5% / 33.3% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 14.5% / 57.6% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 86.20% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 676.10 MiB / 677.90 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.39% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1005 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (4633.60 ms) |
| Error rate | < 0.1% | ❌ FAIL (40.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 31.99 RPS (all instances) |
| **Achieved throughput** | 19.21 RPS (all instances) |
| **Attempted − achieved gap** | 12.78 RPS (39.95%) |
| **Total attempted ops** | 28804 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 5.683 | 4431.871 | 24526.847 | 4.943174053280505 | 38.97% | 0.40050065087621417 | 248 |
| 1 | 5.851 | 4722.687 | 23035.903 | 4.989811496010151 | 38.50% | 0.4008016032064128 | 265 |
| 2 | 5.555 | 4423.679 | 23314.431 | 4.606202441986718 | 42.40% | 0.35052578868302453 | 246 |
| 3 | 5.671 | 4956.159 | 26902.527 | 4.6705943464497715 | 41.58% | 0.4012036108324975 | 246 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 2841 | Connection admission timeout for hash: _R1oo6-0VGP4VoeSd7fpBbwrG_FsZi1RdIyq5wGF_58 after 30000ms (phase=admission) |
| 1 | SQLTransientConnectionException | 2812 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 2 | SQLTransientConnectionException | 3054 | Timeout waiting for fast operation slot for operation: e9cb50da3e8545 |
| 3 | SQLTransientConnectionException | 2995 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-12T09:04:23Z → 2026-07-12T09:19:23Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 25.3 | 41.0 | 0.348 | 86 | 0 |
| ojp-2 | 25.9 | 41.0 | 0.725 | 129 | 0 |
| ojp-3 | 25.8 | 41.0 | 0.476 | 92 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-12T09:04:23Z → 2026-07-12T09:19:23Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 26911 / 40762 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 521318153 | Cumulative since stats reset |
| Transactions rolled back | 5450 | Non-zero → contention or application errors |
| Temp file bytes written | 5 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -3 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 6870 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 525610 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-12T09:04:23Z → 2026-07-12T09:19:23Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.8 | 1.0 | 6.8 | 13.7 | 27.4 | 5.2 | 3.9 | 10.8 | 33.3 | 38.8 | 227.6 | 228.6 |
| Proxy (OJP / pgBouncer) | ojp-2 | 2.3 | 2.0 | 7.8 | 10.8 | 30.4 | 5.0 | 3.9 | 9.9 | 15.6 | 35.3 | 225.2 | 225.6 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.8 | 1.0 | 5.9 | 11.8 | 28.4 | 4.5 | 3.9 | 8.8 | 16.7 | 35.1 | 223.3 | 223.7 |
| PostgreSQL | db | 192.5 | 192.9 | 328.8 | 350.8 | 365.6 | 352.1 | 399.1 | 400.0 | 400.0 | 400.0 | 6233.7 | 10197.7 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-12T09:21:57Z*
