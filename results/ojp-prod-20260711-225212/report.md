# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-11T22:04:05Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260711-225212` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.33 RPS (per instance) |
| **Total throughput** | 13.31 RPS (all instances) |
| **p50 latency** | 6.44 ms |
| **p95 latency** | 5277.70 ms |
| **p99 latency** | 17543.20 ms |
| **p999 latency** | 42828.00 ms |
| **Error rate** | 16.00% (0.16) |
| **Total requests** | 14444 |
| **Failed requests** | 2335 |
| **Total successful** | 12109 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 16.17 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 22032 |
| observed_client_backends_active_max | 33097 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.8% / 3.9% / 12.7% / 19.6% / 29.4% |
| OJP proxy-tier host_cpu (avg / peak) | 14.3% / 70.6% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 62.50% |
| OJP proxy-tier RSS (avg / peak, summed) | 666.00 MiB / 669.00 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.8% / 3.9% / 12.7% / 19.6% / 29.4% |
| PgBouncer tier RSS (avg / peak, summed) | 666.00 MiB / 669.00 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.8% / 3.9% / 12.7% / 19.6% / 29.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 14.3% / 70.6% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 62.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 666.00 MiB / 669.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.34% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 619 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (5277.70 ms) |
| Error rate | < 0.1% | ❌ FAIL (16.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.84 RPS (all instances) |
| **Achieved throughput** | 13.31 RPS (all instances) |
| **Attempted − achieved gap** | 2.52 RPS (15.93%) |
| **Total attempted ops** | 14404 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.215 | 4632.575 | 19873.791 | 3.3023232191634113 | 17.15% | 0.3003003003003003 | 143 |
| 1 | 6.775 | 5304.319 | 15818.751 | 3.3532425263867993 | 15.16% | 0.40040040040040037 | 172 |
| 2 | 6.507 | 5414.911 | 17956.863 | 3.376711568616032 | 14.97% | 0.30045067601402103 | 152 |
| 3 | 6.263 | 5758.975 | 16523.263 | 3.279899810770782 | 17.39% | 0.35052578868302453 | 152 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 619 | Connection admission timeout for hash: _R1oo6-0VGP4VoeSd7fpBbwrG_FsZi1RdIyq5wGF_58 after 30000ms (phase=admission) |
| 1 | SQLTransientConnectionException | 547 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 2 | SQLTransientConnectionException | 541 | Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 3 | SQLTransientConnectionException | 628 | Client throttle limit reached; request rejected to avoid overloading the database |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-11T22:04:05Z → 2026-07-11T22:19:05Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 28.6 | 48.0 | 0.130 | 57 | 0 |
| ojp-2 | 25.1 | 40.0 | 0.328 | 75 | 0 |
| ojp-3 | 25.0 | 40.0 | 0.338 | 69 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-11T22:04:05Z → 2026-07-11T22:19:05Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 22032 / 33097 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 388569917 | Cumulative since stats reset |
| Transactions rolled back | 3781 | Non-zero → contention or application errors |
| Temp file bytes written | -8 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 8 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4757 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 332351 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-11T22:04:05Z → 2026-07-11T22:19:05Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.7 | 1.0 | 4.9 | 11.8 | 21.5 | 5.1 | 3.9 | 9.8 | 34.3 | 46.1 | 227.0 | 228.5 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.6 | 1.0 | 4.9 | 12.7 | 16.6 | 4.9 | 3.9 | 8.9 | 32.4 | 36.1 | 219.9 | 220.7 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.6 | 1.0 | 4.9 | 10.8 | 24.4 | 4.6 | 3.9 | 7.9 | 33.5 | 39.0 | 219.1 | 219.8 |
| PostgreSQL | db | 139.9 | 137.0 | 272.8 | 291.6 | 314.9 | 340.3 | 398.8 | 400.0 | 400.0 | 400.0 | 6193.1 | 9734.3 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-11T22:21:58Z*
