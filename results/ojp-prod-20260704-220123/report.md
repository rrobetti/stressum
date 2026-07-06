# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-04T21:13:18Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260704-220123` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.60 RPS (per instance) |
| **Total throughput** | 14.40 RPS (all instances) |
| **p50 latency** | 6.03 ms |
| **p95 latency** | 4674.55 ms |
| **p99 latency** | 12070.90 ms |
| **p999 latency** | 35659.75 ms |
| **Error rate** | 9.00% (0.09) |
| **Total requests** | 14438 |
| **Failed requests** | 1262 |
| **Total successful** | 13176 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 16.19 |
| observed_postgres_backends_median_numbackends | 16 |
| observed_client_backends_active_median | 21266 |
| observed_client_backends_active_max | 32265 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.9% / 3.9% / 11.8% / 19.6% / 32.3% |
| OJP proxy-tier host_cpu (avg / peak) | 15.5% / 93.1% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 73.90% |
| OJP proxy-tier RSS (avg / peak, summed) | 674.70 MiB / 679.70 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.9% / 3.9% / 11.8% / 19.6% / 32.3% |
| PgBouncer tier RSS (avg / peak, summed) | 674.70 MiB / 679.70 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.9% / 3.9% / 11.8% / 19.6% / 32.3% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 15.5% / 93.1% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 73.90% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 674.70 MiB / 679.70 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.36% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 660 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (4674.55 ms) |
| Error rate | < 0.1% | ❌ FAIL (9.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.74 RPS (all instances) |
| **Achieved throughput** | 14.40 RPS (all instances) |
| **Attempted − achieved gap** | 1.34 RPS (8.53%) |
| **Total attempted ops** | 14404 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.143 | 3723.263 | 9781.247 | 3.590863658238626 | 8.62% | 0.35052578868302453 | 184 |
| 1 | 6.159 | 4562.943 | 12066.815 | 3.6099222984231667 | 8.83% | 0.4001000500250125 | 166 |
| 2 | 5.863 | 5091.327 | 12648.447 | 3.5931299704873467 | 8.98% | 0.35035035035035034 | 158 |
| 3 | 5.967 | 5320.703 | 13787.135 | 3.6056615115580084 | 8.54% | 0.3509651762304457 | 152 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 252 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 0 | SQLException | 59 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 1 | SQLTransientConnectionException | 253 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLException | 66 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 2 | SQLTransientConnectionException | 263 | Timeout waiting for fast operation slot for operation: e9cb50da3e8545 |
| 2 | SQLException | 61 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 3 | SQLTransientConnectionException | 249 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 3 | SQLException | 59 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-04T21:13:18Z → 2026-07-04T21:28:18Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 29.9 | 50.0 | 0.118 | 48 | 0 |
| ojp-2 | 25.5 | 40.0 | 0.370 | 86 | 0 |
| ojp-3 | 24.7 | 40.0 | 0.306 | 84 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-04T21:13:18Z → 2026-07-04T21:28:18Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 16 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 21266 / 32265 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 406732932 | Cumulative since stats reset |
| Transactions rolled back | 3821 | Non-zero → contention or application errors |
| Temp file bytes written | -7 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 7 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4695 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 324417 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-04T21:13:18Z → 2026-07-04T21:28:18Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.6 | 1.0 | 4.9 | 14.7 | 31.3 | 5.2 | 3.9 | 12.8 | 34.3 | 69.3 | 237.4 | 239.3 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.9 | 1.0 | 5.9 | 10.8 | 19.5 | 5.2 | 3.9 | 9.8 | 34.3 | 37.1 | 220.8 | 223.2 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.6 | 1.0 | 4.9 | 13.7 | 23.1 | 5.4 | 3.9 | 15.6 | 34.3 | 56.7 | 216.5 | 217.2 |
| PostgreSQL | db | 149.0 | 152.7 | 293.5 | 319.1 | 343.3 | 323.1 | 394.4 | 400.0 | 400.0 | 400.0 | 6377.8 | 10589.4 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-04T21:31:05Z*
