# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-01T11:08:07Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260701-115535` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.88 RPS (per instance) |
| **Total throughput** | 3.53 RPS (all instances) |
| **p50 latency** | 6.42 ms |
| **p95 latency** | 1602.82 ms |
| **p99 latency** | 5943.30 ms |
| **p999 latency** | 9997.30 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 3604 |
| **Failed requests** | 1 |
| **Total successful** | 3603 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 13.63 |
| observed_postgres_backends_median_numbackends | 13 |
| observed_client_backends_active_median | 10589 |
| observed_client_backends_active_max | 15689 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.1% / 2.0% / 8.8% / 17.6% / 24.5% |
| OJP proxy-tier host_cpu (avg / peak) | 14.6% / 71.4% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 61.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 637.50 MiB / 642.30 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.1% / 2.0% / 8.8% / 17.6% / 24.5% |
| PgBouncer tier RSS (avg / peak, summed) | 637.50 MiB / 642.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.1% / 2.0% / 8.8% / 17.6% / 24.5% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 14.6% / 71.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 61.70% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 637.50 MiB / 642.30 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.20% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 193 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (1602.82 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 3.53 RPS (all instances) |
| **Achieved throughput** | 3.53 RPS (all instances) |
| **Attempted − achieved gap** | 0.00 RPS (0.03%) |
| **Total attempted ops** | 3603 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.031 | 1657.855 | 4673.535 | 0.8827629991995368 | 0.00% | 0.20005002501250624 | 44 |
| 1 | 7.555 | 1604.607 | 5607.423 | 0.8827872169275673 | 0.00% | 0.2001000500250125 | 48 |
| 2 | 6.043 | 1653.759 | 6299.647 | 0.8816450320771851 | 0.11% | 0.20020020020020018 | 50 |
| 3 | 6.055 | 1495.039 | 7192.575 | 0.8827111085421159 | 0.00% | 0.20030045067601399 | 51 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 2 | StatusRuntimeException | 1 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-01T11:08:07Z → 2026-07-01T11:23:07Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 24.6 | 40.0 | 0.040 | 20 | 0 |
| ojp-2 | 25.3 | 45.0 | 0.044 | 16 | 0 |
| ojp-3 | 27.5 | 45.0 | 0.056 | 19 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-01T11:08:07Z → 2026-07-01T11:23:07Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 13 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 10589 / 15689 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 89098753 | Cumulative since stats reset |
| Transactions rolled back | 1296 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1396 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 139998 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-01T11:08:07Z → 2026-07-01T11:23:07Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 0.9 | 1.0 | 2.9 | 7.8 | 19.6 | 6.5 | 3.9 | 33.3 | 34.6 | 52.2 | 208.0 | 209.5 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.1 | 1.0 | 3.9 | 11.8 | 22.5 | 4.5 | 3.9 | 8.8 | 34.3 | 61.1 | 216.5 | 218.2 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.1 | 1.0 | 3.9 | 8.8 | 19.6 | 3.9 | 3.0 | 6.9 | 13.8 | 23.4 | 213.0 | 214.6 |
| PostgreSQL | db | 31.3 | 1.3 | 159.3 | 267.4 | 314.1 | 133.0 | 87.9 | 398.9 | 400.0 | 400.0 | 3767.3 | 8666.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-01T11:25:39Z*
