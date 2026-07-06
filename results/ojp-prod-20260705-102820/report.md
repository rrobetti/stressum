# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-05T09:40:12Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260705-102820` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 2.41 RPS (per instance) |
| **Total throughput** | 9.63 RPS (all instances) |
| **p50 latency** | 7.19 ms |
| **p95 latency** | 703.30 ms |
| **p99 latency** | 3796.47 ms |
| **p999 latency** | 7058.43 ms |
| **Error rate** | 69.00% (0.69) |
| **Total requests** | 28845 |
| **Failed requests** | 19989 |
| **Total successful** | 8856 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 14.22 |
| observed_postgres_backends_median_numbackends | 13 |
| observed_client_backends_active_median | 20163 |
| observed_client_backends_active_max | 27481 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.6% / 2.9% / 7.8% / 17.6% / 29.4% |
| OJP proxy-tier host_cpu (avg / peak) | 16.8% / 129.4% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 64.60% |
| OJP proxy-tier RSS (avg / peak, summed) | 684.90 MiB / 689.00 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.6% / 2.9% / 7.8% / 17.6% / 29.4% |
| PgBouncer tier RSS (avg / peak, summed) | 684.90 MiB / 689.00 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.6% / 2.9% / 7.8% / 17.6% / 29.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 16.8% / 129.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 64.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 684.90 MiB / 689.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.33% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 675 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ✅ PASS (703.30 ms) |
| Error rate | < 0.1% | ❌ FAIL (69.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 31.32 RPS (all instances) |
| **Achieved throughput** | 9.63 RPS (all instances) |
| **Attempted − achieved gap** | 21.69 RPS (69.25%) |
| **Total attempted ops** | 28804 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.891 | 1189.887 | 3381.247 | 2.501009351505298 | 68.22% | 0.30045067601402103 | 166 |
| 1 | 7.047 | 1120.255 | 3577.855 | 2.4345369733687674 | 69.12% | 0.35017508754377186 | 180 |
| 2 | 7.311 | 431.871 | 3958.783 | 2.3982144331868542 | 69.39% | 0.300450676014021 | 165 |
| 3 | 7.503 | 71.167 | 4268.031 | 2.2961790717830852 | 70.47% | 0.3501750875437719 | 164 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 4504 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | SQLException | 415 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 1 | SQLTransientConnectionException | 4570 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | SQLException | 414 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 2 | SQLTransientConnectionException | 4614 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | SQLException | 390 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 3 | SQLTransientConnectionException | 4691 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | SQLException | 391 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-05T09:40:12Z → 2026-07-05T09:55:12Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 28.1 | 47.0 | 0.006 | 3 | 0 |
| ojp-2 | 28.5 | 48.0 | 0.101 | 46 | 0 |
| ojp-3 | 28.2 | 46.0 | 0.201 | 62 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-05T09:40:12Z → 2026-07-05T09:55:12Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 13 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 20163 / 27481 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 213095455 | Cumulative since stats reset |
| Transactions rolled back | 4677 | Non-zero → contention or application errors |
| Temp file bytes written | 2 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -2 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 6791 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 662693 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-05T09:40:12Z → 2026-07-05T09:55:12Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 0.5 | 0.0 | 2.0 | 4.9 | 23.5 | 6.7 | 3.9 | 33.3 | 35.3 | 118.6 | 224.2 | 226.4 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.6 | 1.0 | 3.9 | 8.8 | 23.5 | 5.3 | 3.9 | 8.9 | 35.3 | 38.0 | 232.4 | 233.6 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.6 | 1.0 | 3.9 | 8.8 | 17.6 | 5.2 | 3.9 | 9.8 | 35.1 | 46.3 | 228.3 | 229.0 |
| PostgreSQL | db | 60.4 | 22.6 | 239.4 | 322.7 | 355.5 | 151.9 | 90.6 | 400.0 | 400.0 | 400.0 | 4360.2 | 9873.6 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-05T09:58:10Z*
