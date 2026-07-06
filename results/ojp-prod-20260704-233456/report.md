# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-04T22:46:47Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260704-233456` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.71 RPS (per instance) |
| **Total throughput** | 14.85 RPS (all instances) |
| **p50 latency** | 6.08 ms |
| **p95 latency** | 4993.02 ms |
| **p99 latency** | 12273.67 ms |
| **p999 latency** | 21741.60 ms |
| **Error rate** | 7.00% (0.07) |
| **Total requests** | 14445 |
| **Failed requests** | 957 |
| **Total successful** | 13488 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 16.30 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 21700 |
| observed_client_backends_active_max | 32715 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.8% / 3.9% / 10.8% / 19.6% / 33.3% |
| OJP proxy-tier host_cpu (avg / peak) | 14.7% / 57.0% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 71.60% |
| OJP proxy-tier RSS (avg / peak, summed) | 668.40 MiB / 671.20 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.8% / 3.9% / 10.8% / 19.6% / 33.3% |
| PgBouncer tier RSS (avg / peak, summed) | 668.40 MiB / 671.20 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.8% / 3.9% / 10.8% / 19.6% / 33.3% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 14.7% / 57.0% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 71.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 668.40 MiB / 671.20 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.36% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 691 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (4993.02 ms) |
| Error rate | < 0.1% | ❌ FAIL (7.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.86 RPS (all instances) |
| **Achieved throughput** | 14.85 RPS (all instances) |
| **Attempted − achieved gap** | 1.01 RPS (6.36%) |
| **Total attempted ops** | 14403 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.375 | 4165.631 | 10928.127 | 3.74861208549001 | 5.96% | 0.3501750875437719 | 170 |
| 1 | 6.311 | 4980.735 | 12795.903 | 3.7002673635320535 | 6.70% | 0.35070140280561124 | 157 |
| 2 | 5.511 | 5373.951 | 12632.063 | 3.7008345557734885 | 6.76% | 0.35052578868302453 | 181 |
| 3 | 6.107 | 5451.775 | 12738.559 | 3.7001357928893905 | 7.09% | 0.4008016032064128 | 183 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 171 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 0 | SQLException | 44 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 1 | SQLTransientConnectionException | 200 | Timeout waiting for fast operation slot for operation: e98e4f987f09ed4e |
| 1 | SQLException | 42 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 2 | SQLTransientConnectionException | 199 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 2 | SQLException | 45 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 3 | SQLTransientConnectionException | 205 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 3 | SQLException | 51 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-04T22:46:47Z → 2026-07-04T23:01:47Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 25.1 | 40.0 | 0.327 | 81 | 0 |
| ojp-2 | 26.0 | 40.0 | 0.392 | 84 | 0 |
| ojp-3 | 29.4 | 50.0 | 0.129 | 56 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-04T22:46:47Z → 2026-07-04T23:01:47Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 21700 / 32715 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 428323966 | Cumulative since stats reset |
| Transactions rolled back | 3786 | Non-zero → contention or application errors |
| Temp file bytes written | -8 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 8 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4616 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 322349 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-04T22:46:47Z → 2026-07-04T23:01:47Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.6 | 1.0 | 4.9 | 8.8 | 21.6 | 5.3 | 3.9 | 9.8 | 34.5 | 38.2 | 219.0 | 219.7 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.8 | 1.0 | 5.9 | 12.7 | 19.6 | 5.0 | 3.9 | 9.8 | 33.5 | 43.4 | 222.1 | 222.7 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.5 | 1.0 | 3.9 | 7.8 | 30.4 | 4.6 | 3.9 | 7.8 | 33.3 | 35.9 | 227.3 | 228.8 |
| PostgreSQL | db | 156.8 | 159.8 | 300.9 | 324.7 | 354.0 | 330.2 | 398.9 | 400.0 | 400.0 | 400.0 | 6332.0 | 10513.5 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-04T23:04:31Z*
