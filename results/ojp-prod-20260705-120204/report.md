# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-05T11:13:54Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260705-120204` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 5.26 RPS (per instance) |
| **Total throughput** | 21.04 RPS (all instances) |
| **p50 latency** | 5.98 ms |
| **p95 latency** | 4450.82 ms |
| **p99 latency** | 14678.02 ms |
| **p999 latency** | 31248.50 ms |
| **Error rate** | 34.00% (0.34) |
| **Total requests** | 28820 |
| **Failed requests** | 9706 |
| **Total successful** | 19114 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 17.02 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 27804 |
| observed_client_backends_active_max | 41255 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.1% / 4.9% / 13.7% / 20.6% / 39.2% |
| OJP proxy-tier host_cpu (avg / peak) | 15.1% / 76.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 81.40% |
| OJP proxy-tier RSS (avg / peak, summed) | 672.10 MiB / 673.20 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.1% / 4.9% / 13.7% / 20.6% / 39.2% |
| PgBouncer tier RSS (avg / peak, summed) | 672.10 MiB / 673.20 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.1% / 4.9% / 13.7% / 20.6% / 39.2% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 15.1% / 76.5% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 81.40% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 672.10 MiB / 673.20 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.45% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1053 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (4450.82 ms) |
| Error rate | < 0.1% | ❌ FAIL (34.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 31.71 RPS (all instances) |
| **Achieved throughput** | 21.04 RPS (all instances) |
| **Attempted − achieved gap** | 10.67 RPS (33.64%) |
| **Total attempted ops** | 28802 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 5.855 | 4003.839 | 13459.455 | 5.4269254599703824 | 31.47% | 0.4511278195488722 | 283 |
| 1 | 5.975 | 4595.711 | 14950.399 | 5.2808645798311895 | 33.71% | 0.5012531328320802 | 252 |
| 2 | 5.831 | 4771.839 | 14458.879 | 5.2726802791418965 | 33.45% | 0.4012036108324975 | 269 |
| 3 | 6.255 | 4431.871 | 15843.327 | 5.062030484306057 | 36.09% | 0.4513540621865596 | 249 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 2174 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | SQLException | 94 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 1 | SQLTransientConnectionException | 2337 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | SQLException | 91 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 2 | SQLTransientConnectionException | 2298 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | SQLException | 112 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 3 | SQLTransientConnectionException | 2503 | Timeout waiting for fast operation slot for operation: e9cb50da3e8545 |
| 3 | SQLException | 97 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-05T11:13:54Z → 2026-07-05T11:28:54Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 24.5 | 40.0 | 0.607 | 115 | 0 |
| ojp-2 | 26.3 | 41.0 | 0.590 | 107 | 0 |
| ojp-3 | 26.1 | 41.0 | 0.440 | 104 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-05T11:13:54Z → 2026-07-05T11:28:54Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 27804 / 41255 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 551629357 | Cumulative since stats reset |
| Transactions rolled back | 5650 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7587 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 722724 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-05T11:13:54Z → 2026-07-05T11:28:54Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 2.1 | 2.0 | 5.9 | 8.8 | 20.6 | 5.3 | 3.9 | 9.8 | 33.2 | 35.6 | 227.0 | 227.3 |
| Proxy (OJP / pgBouncer) | ojp-2 | 2.2 | 2.0 | 6.8 | 10.8 | 29.4 | 4.8 | 3.9 | 9.8 | 12.9 | 33.2 | 221.3 | 221.6 |
| Proxy (OJP / pgBouncer) | ojp-3 | 2.0 | 1.0 | 6.8 | 12.7 | 31.4 | 5.3 | 3.9 | 10.8 | 34.5 | 46.1 | 223.8 | 224.3 |
| PostgreSQL | db | 213.8 | 218.4 | 340.8 | 357.7 | 371.0 | 365.2 | 399.5 | 400.0 | 400.0 | 400.0 | 6332.1 | 10068.7 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-05T11:31:36Z*
