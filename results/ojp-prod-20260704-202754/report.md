# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-04T19:39:45Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260704-202754` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.00 RPS (per instance) |
| **Total throughput** | 4.00 RPS (all instances) |
| **p50 latency** | 6.54 ms |
| **p95 latency** | 1510.65 ms |
| **p99 latency** | 6412.27 ms |
| **p999 latency** | 10999.80 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 3604 |
| **Failed requests** | 5 |
| **Total successful** | 3599 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 13.64 |
| observed_postgres_backends_median_numbackends | 13 |
| observed_client_backends_active_median | 10236 |
| observed_client_backends_active_max | 15127 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.2% / 2.0% / 8.8% / 15.7% / 35.3% |
| OJP proxy-tier host_cpu (avg / peak) | 14.0% / 79.1% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 77.40% |
| OJP proxy-tier RSS (avg / peak, summed) | 624.80 MiB / 637.40 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.2% / 2.0% / 8.8% / 15.7% / 35.3% |
| PgBouncer tier RSS (avg / peak, summed) | 624.80 MiB / 637.40 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.2% / 2.0% / 8.8% / 15.7% / 35.3% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 14.0% / 79.1% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 77.40% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 624.80 MiB / 637.40 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.20% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 194 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (1510.65 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 4.00 RPS (all instances) |
| **Achieved throughput** | 4.00 RPS (all instances) |
| **Attempted − achieved gap** | 0.01 RPS (0.14%) |
| **Total attempted ops** | 3601 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.899 | 1499.135 | 4698.111 | 0.9982677445145244 | 0.22% | 0.20020020020020018 | 44 |
| 1 | 7.579 | 1507.327 | 5849.087 | 0.9988779271285256 | 0.11% | 0.20030045067601399 | 51 |
| 2 | 5.611 | 1650.687 | 7950.335 | 0.9990309399882114 | 0.11% | 0.20015012511260633 | 49 |
| 3 | 6.063 | 1385.471 | 7151.615 | 0.9991651420146722 | 0.11% | 0.20030045067601399 | 50 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 2 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLTransientConnectionException | 1 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 2 | SQLTransientConnectionException | 1 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 3 | SQLException | 1 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-04T19:39:45Z → 2026-07-04T19:54:45Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 22.8 | 40.0 | 0.043 | 21 | 0 |
| ojp-2 | 25.2 | 40.0 | 0.048 | 21 | 0 |
| ojp-3 | 26.0 | 40.0 | 0.051 | 25 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-04T19:39:45Z → 2026-07-04T19:54:45Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 13 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 10236 / 15127 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 90786490 | Cumulative since stats reset |
| Transactions rolled back | 1295 | Non-zero → contention or application errors |
| Temp file bytes written | -2 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 2 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1482 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 148576 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-04T19:39:45Z → 2026-07-04T19:54:45Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.0 | 1.0 | 3.9 | 7.8 | 23.5 | 4.8 | 3.9 | 8.8 | 34.3 | 49.3 | 205.9 | 208.1 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.2 | 1.0 | 3.9 | 9.8 | 35.3 | 4.3 | 3.9 | 7.8 | 26.3 | 54.6 | 207.9 | 216.5 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.0 | 1.0 | 3.9 | 8.8 | 18.6 | 5.1 | 3.9 | 14.8 | 35.1 | 40.2 | 211.0 | 212.8 |
| PostgreSQL | db | 29.7 | 0.7 | 177.1 | 244.2 | 304.9 | 129.5 | 85.8 | 398.0 | 400.0 | 400.0 | 3789.5 | 8826.7 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-04T19:57:15Z*
