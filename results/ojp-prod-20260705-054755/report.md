# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-05T04:59:48Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260705-054755` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.92 RPS (per instance) |
| **Total throughput** | 19.70 RPS (all instances) |
| **p50 latency** | 6.50 ms |
| **p95 latency** | 4632.57 ms |
| **p99 latency** | 19550.20 ms |
| **p999 latency** | 56144.00 ms |
| **Error rate** | 38.00% (0.38) |
| **Total requests** | 28973 |
| **Failed requests** | 11131 |
| **Total successful** | 17842 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 17.02 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 25516 |
| observed_client_backends_active_max | 38900 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.8% / 4.9% / 13.7% / 20.6% / 24.5% |
| OJP proxy-tier host_cpu (avg / peak) | 15.6% / 72.1% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 61.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 674.50 MiB / 676.90 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.8% / 4.9% / 13.7% / 20.6% / 24.5% |
| PgBouncer tier RSS (avg / peak, summed) | 674.50 MiB / 676.90 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.8% / 4.9% / 13.7% / 20.6% / 24.5% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 15.6% / 72.1% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 61.70% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 674.50 MiB / 676.90 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.43% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1025 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (4632.57 ms) |
| Error rate | < 0.1% | ❌ FAIL (38.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 31.80 RPS (all instances) |
| **Achieved throughput** | 19.70 RPS (all instances) |
| **Attempted − achieved gap** | 12.10 RPS (38.06%) |
| **Total attempted ops** | 28804 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.607 | 4730.879 | 19529.727 | 4.766274514113646 | 39.81% | 0.4008016032064128 | 288 |
| 1 | 6.735 | 4804.607 | 17907.711 | 4.884629337285708 | 39.39% | 0.4511278195488722 | 239 |
| 2 | 6.315 | 4493.311 | 19709.951 | 5.013234585795026 | 37.23% | 0.4008016032064128 | 247 |
| 3 | 6.359 | 4501.503 | 21053.439 | 5.0343436215285475 | 37.24% | 0.45158053186151526 | 251 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 2754 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | SQLException | 115 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 1 | SQLTransientConnectionException | 2695 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | SQLException | 167 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 2 | SQLTransientConnectionException | 2584 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 2 | SQLException | 108 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 3 | SQLTransientConnectionException | 2576 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 3 | SQLException | 132 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-05T04:59:48Z → 2026-07-05T05:14:48Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 25.2 | 41.0 | 0.593 | 120 | 0 |
| ojp-2 | 24.6 | 40.0 | 0.506 | 95 | 0 |
| ojp-3 | 26.6 | 40.0 | 0.365 | 94 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-05T04:59:48Z → 2026-07-05T05:14:48Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 25516 / 38900 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 541753217 | Cumulative since stats reset |
| Transactions rolled back | 5505 | Non-zero → contention or application errors |
| Temp file bytes written | 5 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -5 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7118 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 536853 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-05T04:59:48Z → 2026-07-05T05:14:48Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 2.2 | 2.0 | 6.9 | 11.8 | 21.6 | 5.3 | 3.9 | 10.8 | 28.3 | 36.6 | 225.6 | 226.0 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.9 | 1.9 | 5.9 | 11.7 | 21.5 | 5.0 | 3.9 | 9.8 | 34.5 | 51.0 | 225.0 | 225.3 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.8 | 1.0 | 4.9 | 11.7 | 18.6 | 5.7 | 3.9 | 14.8 | 35.3 | 51.2 | 223.9 | 225.6 |
| PostgreSQL | db | 190.1 | 189.7 | 309.8 | 325.2 | 338.0 | 374.7 | 399.5 | 400.0 | 400.0 | 400.0 | 7128.1 | 10717.3 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-05T05:17:30Z*
