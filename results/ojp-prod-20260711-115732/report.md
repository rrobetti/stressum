# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-11T11:09:22Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260711-115732` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.00 RPS (per instance) |
| **Total throughput** | 3.99 RPS (all instances) |
| **p50 latency** | 6.35 ms |
| **p95 latency** | 1628.67 ms |
| **p99 latency** | 7566.35 ms |
| **p999 latency** | 11669.50 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 3604 |
| **Failed requests** | 9 |
| **Total successful** | 3595 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 13.61 |
| observed_postgres_backends_median_numbackends | 13 |
| observed_client_backends_active_median | 11920 |
| observed_client_backends_active_max | 17663 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.1% / 2.0% / 8.8% / 16.6% / 58.7% |
| OJP proxy-tier host_cpu (avg / peak) | 14.2% / 67.8% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 77.30% |
| OJP proxy-tier RSS (avg / peak, summed) | 630.30 MiB / 650.70 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.1% / 2.0% / 8.8% / 16.6% / 58.7% |
| PgBouncer tier RSS (avg / peak, summed) | 630.30 MiB / 650.70 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.1% / 2.0% / 8.8% / 16.6% / 58.7% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 14.2% / 67.8% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 77.30% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 630.30 MiB / 650.70 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.18% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 177 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (1628.67 ms) |
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
| **Attempted − achieved gap** | 0.01 RPS (0.25%) |
| **Total attempted ops** | 3603 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.603 | 1548.287 | 5177.343 | 0.9970521453830823 | 0.33% | 0.15022533800701052 | 44 |
| 1 | 5.899 | 1649.663 | 6950.911 | 0.9978356179588211 | 0.22% | 0.2001000500250125 | 43 |
| 2 | 6.347 | 1808.383 | 9453.567 | 0.997678372463633 | 0.22% | 0.1502253380070105 | 44 |
| 3 | 6.567 | 1508.351 | 8683.519 | 0.9978223276897361 | 0.22% | 0.20005002501250624 | 46 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 3 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLTransientConnectionException | 2 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 2 | SQLTransientConnectionException | 2 | Connection admission timeout for hash: _R1oo6-0VGP4VoeSd7fpBbwrG_FsZi1RdIyq5wGF_58 after 30000ms (phase=admission) |
| 3 | SQLTransientConnectionException | 2 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-11T11:09:22Z → 2026-07-11T11:24:22Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 24.1 | 40.0 | 0.041 | 19 | 0 |
| ojp-2 | 23.5 | 40.0 | 0.056 | 23 | 0 |
| ojp-3 | 24.5 | 40.0 | 0.063 | 27 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-11T11:09:22Z → 2026-07-11T11:24:22Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 13 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 11920 / 17663 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 90043095 | Cumulative since stats reset |
| Transactions rolled back | 1303 | Non-zero → contention or application errors |
| Temp file bytes written | -1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1475 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 147882 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-11T11:09:22Z → 2026-07-11T11:24:22Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.1 | 1.0 | 3.9 | 12.7 | 18.6 | 5.8 | 3.9 | 23.4 | 36.1 | 57.8 | 207.4 | 209.0 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.1 | 1.0 | 3.9 | 8.8 | 35.2 | 4.8 | 3.9 | 10.7 | 34.3 | 43.1 | 212.8 | 220.1 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.1 | 1.0 | 3.9 | 9.8 | 23.5 | 3.9 | 3.9 | 6.9 | 13.7 | 32.5 | 210.1 | 221.6 |
| PostgreSQL | db | 30.7 | 1.3 | 199.6 | 253.2 | 296.4 | 164.6 | 122.1 | 399.5 | 400.0 | 400.0 | 3793.6 | 9186.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-11T11:27:03Z*
