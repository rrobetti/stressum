# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-11T14:15:23Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260711-150331` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.00 RPS (per instance) |
| **Total throughput** | 3.99 RPS (all instances) |
| **p50 latency** | 6.57 ms |
| **p95 latency** | 1730.30 ms |
| **p99 latency** | 7132.18 ms |
| **p999 latency** | 10807.30 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 3604 |
| **Failed requests** | 6 |
| **Total successful** | 3598 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 13.81 |
| observed_postgres_backends_median_numbackends | 13 |
| observed_client_backends_active_median | 12738 |
| observed_client_backends_active_max | 18250 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.1% / 2.0% / 8.8% / 17.6% / 35.3% |
| OJP proxy-tier host_cpu (avg / peak) | 13.0% / 57.6% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 64.60% |
| OJP proxy-tier RSS (avg / peak, summed) | 639.70 MiB / 644.90 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.1% / 2.0% / 8.8% / 17.6% / 35.3% |
| PgBouncer tier RSS (avg / peak, summed) | 639.70 MiB / 644.90 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.1% / 2.0% / 8.8% / 17.6% / 35.3% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 13.0% / 57.6% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 64.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 639.70 MiB / 644.90 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.18% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 183 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (1730.30 ms) |
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
| **Total attempted ops** | 3602 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 7.055 | 1761.279 | 5181.439 | 0.9958135863610175 | 0.44% | 0.15022533800701052 | 47 |
| 1 | 6.827 | 1812.479 | 6811.647 | 1.0002320183039128 | 0.00% | 0.19990004997501248 | 44 |
| 2 | 6.199 | 1649.663 | 8749.055 | 0.9988269332572745 | 0.11% | 0.15022533800701052 | 45 |
| 3 | 6.215 | 1697.791 | 7786.495 | 0.9988014382740711 | 0.11% | 0.2001000500250125 | 47 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 4 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 2 | SQLTransientConnectionException | 1 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 3 | SQLTransientConnectionException | 1 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-11T14:15:23Z → 2026-07-11T14:30:23Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 24.9 | 40.0 | 0.059 | 21 | 0 |
| ojp-2 | 23.8 | 40.0 | 0.044 | 20 | 0 |
| ojp-3 | 26.2 | 47.0 | 0.058 | 19 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-11T14:15:23Z → 2026-07-11T14:30:23Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 13 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 12738 / 18250 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 90470527 | Cumulative since stats reset |
| Transactions rolled back | 1299 | Non-zero → contention or application errors |
| Temp file bytes written | -2 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 2 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1364 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 136792 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-11T14:15:23Z → 2026-07-11T14:30:23Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.1 | 1.0 | 3.9 | 12.7 | 28.4 | 4.5 | 3.9 | 7.8 | 33.2 | 35.3 | 209.3 | 211.3 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.0 | 1.0 | 3.9 | 6.8 | 18.6 | 4.4 | 3.9 | 7.8 | 34.1 | 49.3 | 208.9 | 210.5 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.0 | 1.0 | 3.9 | 9.8 | 17.6 | 4.4 | 3.9 | 7.8 | 33.3 | 49.8 | 221.5 | 223.1 |
| PostgreSQL | db | 29.0 | 1.3 | 175.0 | 227.2 | 254.1 | 165.5 | 124.3 | 399.6 | 400.0 | 400.0 | 3838.5 | 8282.1 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-11T14:33:02Z*
