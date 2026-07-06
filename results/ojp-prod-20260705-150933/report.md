# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-05T14:21:24Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260705-150933` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 2.91 RPS (per instance) |
| **Total throughput** | 11.64 RPS (all instances) |
| **p50 latency** | 8.19 ms |
| **p95 latency** | 759.36 ms |
| **p99 latency** | 3629.07 ms |
| **p999 latency** | 6487.02 ms |
| **Error rate** | 75.00% (0.75) |
| **Total requests** | 43244 |
| **Failed requests** | 32375 |
| **Total successful** | 10869 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 14.34 |
| observed_postgres_backends_median_numbackends | 13 |
| observed_client_backends_active_median | 22004 |
| observed_client_backends_active_max | 31117 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.4% / 3.9% / 9.8% / 17.6% / 68.4% |
| OJP proxy-tier host_cpu (avg / peak) | 17.4% / 107.4% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 108.60% |
| OJP proxy-tier RSS (avg / peak, summed) | 728.40 MiB / 730.50 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.4% / 3.9% / 9.8% / 17.6% / 68.4% |
| PgBouncer tier RSS (avg / peak, summed) | 728.40 MiB / 730.50 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.4% / 3.9% / 9.8% / 17.6% / 68.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 17.4% / 107.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 108.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 728.40 MiB / 730.50 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.40% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1023 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ✅ PASS (759.36 ms) |
| Error rate | < 0.1% | ❌ FAIL (75.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.28 RPS (all instances) |
| **Achieved throughput** | 11.64 RPS (all instances) |
| **Attempted − achieved gap** | 34.64 RPS (74.84%) |
| **Total attempted ops** | 43203 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 8.079 | 882.175 | 3123.199 | 2.8984072213713676 | 75.09% | 0.35052578868302453 | 231 |
| 1 | 8.311 | 416.511 | 3629.055 | 2.9036936266331272 | 74.88% | 0.4506760140210316 | 287 |
| 2 | 8.107 | 961.535 | 3674.111 | 2.942198788254734 | 74.56% | 0.3508771929824561 | 286 |
| 3 | 8.279 | 777.215 | 4089.855 | 2.8983027282547087 | 74.94% | 0.4511278195488722 | 219 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 7468 | Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 0 | SQLException | 651 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 1 | SQLTransientConnectionException | 7453 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | SQLException | 638 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 2 | SQLTransientConnectionException | 7411 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | SQLException | 652 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 3 | SQLTransientConnectionException | 7459 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | SQLException | 643 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-05T14:21:24Z → 2026-07-05T14:36:24Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 26.1 | 41.0 | 0.428 | 91 | 0 |
| ojp-2 | 27.3 | 40.0 | 0.009 | 5 | 0 |
| ojp-3 | 26.0 | 41.0 | 0.372 | 87 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-05T14:21:24Z → 2026-07-05T14:36:24Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 13 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 22004 / 31117 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 256321529 | Cumulative since stats reset |
| Transactions rolled back | 5285 | Non-zero → contention or application errors |
| Temp file bytes written | -2 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 2 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 10453 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 752748 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-05T14:21:24Z → 2026-07-05T14:36:24Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.9 | 2.0 | 4.9 | 7.8 | 20.6 | 8.5 | 4.9 | 35.1 | 41.4 | 98.5 | 247.6 | 248.1 |
| Proxy (OJP / pgBouncer) | ojp-2 | 0.6 | 0.0 | 2.0 | 5.9 | 21.5 | 4.0 | 3.0 | 4.9 | 33.3 | 48.3 | 238.2 | 238.4 |
| Proxy (OJP / pgBouncer) | ojp-3 | 2.0 | 2.0 | 4.9 | 8.8 | 66.5 | 5.3 | 3.9 | 9.8 | 34.5 | 70.2 | 242.6 | 244.0 |
| PostgreSQL | db | 68.0 | 33.0 | 234.3 | 287.9 | 359.9 | 171.7 | 112.5 | 400.0 | 400.0 | 400.0 | 4056.2 | 9166.5 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-05T14:39:26Z*
