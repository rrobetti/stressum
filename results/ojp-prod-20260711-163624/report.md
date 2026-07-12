# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-11T15:48:15Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260711-163624` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.00 RPS (per instance) |
| **Total throughput** | 3.99 RPS (all instances) |
| **p50 latency** | 6.82 ms |
| **p95 latency** | 1707.26 ms |
| **p99 latency** | 7439.35 ms |
| **p999 latency** | 12410.88 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 3604 |
| **Failed requests** | 6 |
| **Total successful** | 3598 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 13.70 |
| observed_postgres_backends_median_numbackends | 13 |
| observed_client_backends_active_median | 12774 |
| observed_client_backends_active_max | 18755 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.1% / 2.0% / 8.8% / 16.6% / 46.8% |
| OJP proxy-tier host_cpu (avg / peak) | 11.9% / 56.9% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 82.10% |
| OJP proxy-tier RSS (avg / peak, summed) | 628.50 MiB / 642.20 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.1% / 2.0% / 8.8% / 16.6% / 46.8% |
| PgBouncer tier RSS (avg / peak, summed) | 628.50 MiB / 642.20 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.1% / 2.0% / 8.8% / 16.6% / 46.8% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 11.9% / 56.9% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 82.10% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 628.50 MiB / 642.20 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.18% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 182 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (1707.26 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 4.00 RPS (all instances) |
| **Achieved throughput** | 3.99 RPS (all instances) |
| **Attempted − achieved gap** | 0.01 RPS (0.17%) |
| **Total attempted ops** | 3603 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.787 | 1685.503 | 5320.703 | 0.9982101060167975 | 0.22% | 0.15033827052601445 | 46 |
| 1 | 6.707 | 1808.383 | 6569.983 | 0.9990497926416653 | 0.11% | 0.2001000500250125 | 47 |
| 2 | 6.931 | 1651.711 | 9781.247 | 0.9978345104228754 | 0.22% | 0.15030060120240482 | 43 |
| 3 | 6.843 | 1683.455 | 8085.503 | 0.9989411224102452 | 0.11% | 0.2001000500250125 | 46 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 2 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLTransientConnectionException | 1 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 2 | SQLTransientConnectionException | 2 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 3 | SQLTransientConnectionException | 1 | Connection admission timeout for hash: _R1oo6-0VGP4VoeSd7fpBbwrG_FsZi1RdIyq5wGF_58 after 30000ms (phase=admission) |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-11T15:48:15Z → 2026-07-11T16:03:15Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 23.2 | 40.0 | 0.047 | 20 | 0 |
| ojp-2 | 25.6 | 40.0 | 0.047 | 23 | 0 |
| ojp-3 | 25.1 | 40.0 | 0.060 | 26 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-11T15:48:15Z → 2026-07-11T16:03:15Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 13 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 12774 / 18755 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 89817343 | Cumulative since stats reset |
| Transactions rolled back | 1304 | Non-zero → contention or application errors |
| Temp file bytes written | -1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1469 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 147174 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-11T15:48:15Z → 2026-07-11T16:03:15Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.1 | 1.0 | 2.9 | 7.8 | 41.0 | 4.3 | 3.9 | 7.8 | 28.4 | 44.1 | 209.3 | 219.8 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.1 | 1.0 | 3.9 | 8.8 | 18.6 | 4.1 | 3.9 | 6.8 | 18.6 | 38.4 | 208.5 | 210.0 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.1 | 1.0 | 3.9 | 7.8 | 22.5 | 3.9 | 3.0 | 6.8 | 11.8 | 23.5 | 210.7 | 212.4 |
| PostgreSQL | db | 28.5 | 1.3 | 175.1 | 232.4 | 267.3 | 171.6 | 134.9 | 399.1 | 400.0 | 400.0 | 3756.4 | 9067.6 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-11T16:05:55Z*
