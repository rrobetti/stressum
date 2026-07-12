# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-11T23:38:25Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260712-002632` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.51 RPS (per instance) |
| **Total throughput** | 14.03 RPS (all instances) |
| **p50 latency** | 6.41 ms |
| **p95 latency** | 5607.43 ms |
| **p99 latency** | 19001.35 ms |
| **p999 latency** | 30380.00 ms |
| **Error rate** | 12.00% (0.12) |
| **Total requests** | 14453 |
| **Failed requests** | 1721 |
| **Total successful** | 12732 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 16.53 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 22521 |
| observed_client_backends_active_max | 33623 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.8% / 3.9% / 11.8% / 17.6% / 27.4% |
| OJP proxy-tier host_cpu (avg / peak) | 16.0% / 143.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 57.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 664.20 MiB / 666.50 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.8% / 3.9% / 11.8% / 17.6% / 27.4% |
| PgBouncer tier RSS (avg / peak, summed) | 664.20 MiB / 666.50 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.8% / 3.9% / 11.8% / 17.6% / 27.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 16.0% / 143.5% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 57.70% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 664.20 MiB / 666.50 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.34% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 610 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (5607.43 ms) |
| Error rate | < 0.1% | ❌ FAIL (12.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.87 RPS (all instances) |
| **Achieved throughput** | 14.03 RPS (all instances) |
| **Attempted − achieved gap** | 1.84 RPS (11.61%) |
| **Total attempted ops** | 14404 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.599 | 5009.407 | 18169.855 | 3.54301411243577 | 11.16% | 0.300450676014021 | 152 |
| 1 | 6.651 | 5595.135 | 18874.367 | 3.544873189866678 | 11.23% | 0.40040040040040037 | 171 |
| 2 | 5.979 | 5672.959 | 19824.639 | 3.456941868504516 | 12.86% | 0.3003003003003003 | 148 |
| 3 | 6.419 | 6152.191 | 19136.511 | 3.4835839957721357 | 12.38% | 0.35052578868302453 | 139 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 403 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLTransientConnectionException | 406 | Timeout waiting for fast operation slot for operation: e9cb50da3e8545 |
| 2 | SQLTransientConnectionException | 465 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | SQLTransientConnectionException | 447 | Client throttle limit reached; request rejected to avoid overloading the database |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-11T23:38:25Z → 2026-07-11T23:53:25Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 26.1 | 40.0 | 0.416 | 84 | 0 |
| ojp-2 | 25.7 | 40.0 | 0.273 | 77 | 0 |
| ojp-3 | 25.0 | 40.0 | 0.293 | 69 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-11T23:38:25Z → 2026-07-11T23:53:25Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 22521 / 33623 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 401717498 | Cumulative since stats reset |
| Transactions rolled back | 3899 | Non-zero → contention or application errors |
| Temp file bytes written | -4 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 5 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4926 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 347321 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-11T23:38:25Z → 2026-07-11T23:53:25Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.7 | 1.0 | 5.9 | 10.8 | 18.6 | 7.4 | 3.9 | 20.5 | 104.4 | 124.9 | 216.5 | 216.9 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.6 | 1.0 | 4.9 | 9.8 | 18.6 | 4.6 | 3.9 | 7.9 | 20.6 | 34.5 | 223.7 | 224.8 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.6 | 1.0 | 4.9 | 10.8 | 20.5 | 4.4 | 3.9 | 8.7 | 19.7 | 32.4 | 224.0 | 224.8 |
| PostgreSQL | db | 150.6 | 146.4 | 280.1 | 300.9 | 309.1 | 357.3 | 399.4 | 400.0 | 400.0 | 400.0 | 6237.3 | 9980.3 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-11T23:56:13Z*
