# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-05T19:03:36Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260705-195142` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 2.95 RPS (per instance) |
| **Total throughput** | 11.80 RPS (all instances) |
| **p50 latency** | 8.33 ms |
| **p95 latency** | 1148.80 ms |
| **p99 latency** | 4534.27 ms |
| **p999 latency** | 8611.85 ms |
| **Error rate** | 75.00% (0.75) |
| **Total requests** | 43274 |
| **Failed requests** | 32406 |
| **Total successful** | 10868 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 14.32 |
| observed_postgres_backends_median_numbackends | 13 |
| observed_client_backends_active_median | 21712 |
| observed_client_backends_active_max | 30708 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.4% / 3.9% / 10.8% / 17.6% / 27.4% |
| OJP proxy-tier host_cpu (avg / peak) | 20.9% / 92.2% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 61.60% |
| OJP proxy-tier RSS (avg / peak, summed) | 725.10 MiB / 726.40 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.4% / 3.9% / 10.8% / 17.6% / 27.4% |
| PgBouncer tier RSS (avg / peak, summed) | 725.10 MiB / 726.40 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.4% / 3.9% / 10.8% / 17.6% / 27.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 20.9% / 92.2% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 61.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 725.10 MiB / 726.40 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.44% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 936 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ✅ PASS (1148.80 ms) |
| Error rate | < 0.1% | ❌ FAIL (75.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.90 RPS (all instances) |
| **Achieved throughput** | 11.80 RPS (all instances) |
| **Attempted − achieved gap** | 35.10 RPS (74.84%) |
| **Total attempted ops** | 43203 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 8.351 | 1002.495 | 4374.527 | 2.9398050251038312 | 74.95% | 0.45090180360721444 | 237 |
| 1 | 8.575 | 597.503 | 4214.783 | 2.8595973281681655 | 75.49% | 0.4511278195488722 | 264 |
| 2 | 8.067 | 1519.615 | 4632.575 | 2.958200189160887 | 74.66% | 0.4008016032064128 | 218 |
| 3 | 8.335 | 1475.583 | 4915.199 | 3.0401797020381647 | 74.45% | 0.4506760140210316 | 217 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 7428 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | SQLException | 682 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 1 | SQLTransientConnectionException | 7517 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | SQLException | 652 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 2 | SQLTransientConnectionException | 7404 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | SQLException | 677 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 3 | SQLTransientConnectionException | 7380 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | SQLException | 666 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-05T19:03:36Z → 2026-07-05T19:18:36Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 25.3 | 41.0 | 0.469 | 83 | 0 |
| ojp-2 | 27.3 | 40.0 | 0.011 | 5 | 0 |
| ojp-3 | 25.6 | 41.0 | 0.291 | 75 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-05T19:03:36Z → 2026-07-05T19:18:36Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 13 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 21712 / 30708 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 238822943 | Cumulative since stats reset |
| Transactions rolled back | 5328 | Non-zero → contention or application errors |
| Temp file bytes written | 5 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -5 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 9677 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 539106 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-05T19:03:36Z → 2026-07-05T19:18:36Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 2.0 | 2.0 | 4.9 | 8.8 | 21.5 | 12.3 | 5.8 | 36.1 | 42.2 | 85.3 | 242.3 | 242.9 |
| Proxy (OJP / pgBouncer) | ojp-2 | 0.6 | 0.0 | 2.0 | 5.9 | 23.5 | 3.7 | 3.0 | 4.9 | 30.4 | 35.3 | 238.7 | 238.9 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.9 | 2.0 | 4.9 | 9.8 | 16.6 | 5.3 | 3.9 | 9.8 | 34.3 | 37.6 | 244.1 | 244.6 |
| PostgreSQL | db | 69.1 | 27.5 | 247.1 | 330.1 | 352.9 | 164.3 | 93.8 | 400.0 | 400.0 | 400.0 | 5005.6 | 9614.3 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-05T19:21:37Z*
