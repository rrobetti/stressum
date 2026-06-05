# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-30T12:39:34Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260530-132733` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.67 RPS (per instance) |
| **Total throughput** | 1.34 RPS (all instances) |
| **p50 latency** | 12.34 ms |
| **p95 latency** | 12550.15 ms |
| **p99 latency** | 28368.90 ms |
| **p999 latency** | 44990.45 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 1808 |
| **Failed requests** | 7 |
| **Total successful** | 1801 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 24 |
| observed_postgres_backends_avg_numbackends | 18.04 |
| observed_postgres_backends_median_numbackends | 16 |
| observed_client_backends_active_median | 16384 |
| observed_client_backends_active_max | 23279 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 2.8% / 2.0% / 7.8% / 18.6% / 43.1% |
| OJP proxy-tier host_cpu (avg / peak) | 25.2% / 102.9% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 92.00% |
| OJP proxy-tier RSS (avg / peak, summed) | 655.60 MiB / 665.90 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 2.8% / 2.0% / 7.8% / 18.6% / 43.1% |
| PgBouncer tier RSS (avg / peak, summed) | 655.60 MiB / 665.90 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 2.8% / 2.0% / 7.8% / 18.6% / 43.1% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 25.2% / 102.9% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 92.00% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 655.60 MiB / 665.90 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.20% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 99 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (12550.15 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (2/2 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 1.34 RPS (all instances) |
| **Achieved throughput** | 1.34 RPS (all instances) |
| **Attempted − achieved gap** | 0.00 RPS (0.06%) |
| **Total attempted ops** | 2402 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.28 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 11.743 | 12623.871 | 27508.735 | 0.6677741825145557 | 0.44% | 0.20030045067601399 | 51 |
| 1 | 12.927 | 12476.415 | 29229.055 | 0.6691163802066316 | 0.33% | 0.19990004997501248 | 48 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 1 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 0 | StatusRuntimeException | 3 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: f891f847dfafb38c |
| 1 | StatusRuntimeException | 3 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: f891f847dfafb38c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-30T12:39:34Z → 2026-05-30T12:54:34Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 26.1 | 45.0 | 0.032 | 10 | 0 |
| ojp-2 | 24.1 | 43.0 | 0.025 | 10 | 0 |
| ojp-3 | 28.1 | 45.0 | 0.038 | 12 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-30T12:39:34Z → 2026-05-30T12:54:34Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 16 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 16384 / 23279 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 171346180 | Cumulative since stats reset |
| Transactions rolled back | 730 | Non-zero → contention or application errors |
| Temp file bytes written | 6 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -6 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1489 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 150713 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-30T12:39:34Z → 2026-05-30T12:54:34Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.0 | 1.0 | 3.9 | 12.7 | 21.5 | 6.7 | 3.9 | 33.3 | 35.5 | 72.9 | 217.8 | 223.4 |
| Proxy (OJP / pgBouncer) | ojp-2 | 0.9 | 0.0 | 2.9 | 8.8 | 42.1 | 5.6 | 3.9 | 21.8 | 35.3 | 53.2 | 219.6 | 222.4 |
| Proxy (OJP / pgBouncer) | ojp-3 | 0.9 | 0.0 | 2.9 | 11.8 | 28.4 | 13.4 | 4.9 | 37.1 | 85.3 | 96.1 | 218.2 | 220.1 |
| PostgreSQL | db | 58.8 | 1.5 | 206.8 | 217.1 | 222.6 | 326.7 | 307.3 | 400.0 | 400.0 | 400.0 | 6167.9 | 17281.5 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-30T12:57:27Z*
