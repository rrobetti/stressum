# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-11T20:29:39Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260711-211744` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.61 RPS (per instance) |
| **Total throughput** | 14.46 RPS (all instances) |
| **p50 latency** | 6.42 ms |
| **p95 latency** | 5547.00 ms |
| **p99 latency** | 20082.70 ms |
| **p999 latency** | 34807.75 ms |
| **Error rate** | 9.00% (0.09) |
| **Total requests** | 14451 |
| **Failed requests** | 1306 |
| **Total successful** | 13145 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 16.39 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 22416 |
| observed_client_backends_active_max | 33629 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.8% / 3.9% / 12.7% / 20.6% / 29.4% |
| OJP proxy-tier host_cpu (avg / peak) | 15.9% / 61.8% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 64.60% |
| OJP proxy-tier RSS (avg / peak, summed) | 669.80 MiB / 672.80 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.8% / 3.9% / 12.7% / 20.6% / 29.4% |
| PgBouncer tier RSS (avg / peak, summed) | 669.80 MiB / 672.80 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.8% / 3.9% / 12.7% / 20.6% / 29.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 15.9% / 61.8% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 64.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 669.80 MiB / 672.80 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.33% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 659 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (5547.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (9.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.84 RPS (all instances) |
| **Achieved throughput** | 14.46 RPS (all instances) |
| **Attempted − achieved gap** | 1.38 RPS (8.74%) |
| **Total attempted ops** | 14403 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.163 | 5414.911 | 19759.103 | 3.5270733092847735 | 11.10% | 0.30022518766890954 | 153 |
| 1 | 6.695 | 5705.727 | 21135.359 | 3.6222225878816796 | 8.71% | 0.35070140280561124 | 174 |
| 2 | 6.355 | 5779.455 | 19431.423 | 3.6430777108978902 | 8.58% | 0.300450676014021 | 160 |
| 3 | 6.447 | 5287.935 | 20004.863 | 3.666228010334098 | 7.75% | 0.35070140280561124 | 172 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 401 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLTransientConnectionException | 315 | Timeout waiting for fast operation slot for operation: 5719e1e7b8f36461 |
| 2 | SQLTransientConnectionException | 310 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 3 | SQLTransientConnectionException | 280 | Timeout waiting for fast operation slot for operation: e9cb50da3e8545 |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-11T20:29:39Z → 2026-07-11T20:44:39Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 24.5 | 40.0 | 0.374 | 80 | 0 |
| ojp-2 | 28.5 | 48.0 | 0.120 | 56 | 0 |
| ojp-3 | 24.7 | 40.0 | 0.354 | 80 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-11T20:29:39Z → 2026-07-11T20:44:39Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 22416 / 33629 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 402684991 | Cumulative since stats reset |
| Transactions rolled back | 3889 | Non-zero → contention or application errors |
| Temp file bytes written | -9 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 9 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4761 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 329945 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-11T20:29:39Z → 2026-07-11T20:44:39Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.7 | 1.0 | 5.9 | 12.7 | 21.6 | 5.4 | 3.9 | 10.8 | 35.1 | 41.0 | 222.2 | 222.9 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.6 | 1.0 | 3.9 | 13.7 | 22.5 | 6.2 | 3.9 | 25.5 | 35.3 | 45.3 | 223.2 | 224.8 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.6 | 1.0 | 4.9 | 13.7 | 20.5 | 4.7 | 3.9 | 8.8 | 22.6 | 37.1 | 224.4 | 225.1 |
| PostgreSQL | db | 151.4 | 153.8 | 276.0 | 302.2 | 321.3 | 357.2 | 399.5 | 400.0 | 400.0 | 400.0 | 6370.7 | 9924.5 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-11T20:47:27Z*
