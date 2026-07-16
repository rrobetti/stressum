# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T22:37:17Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260715-232528` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.32 RPS (per instance) |
| **Total throughput** | 21.09 RPS (all instances) |
| **p50 latency** | 25150.44 ms |
| **p95 latency** | 152166.88 ms |
| **p99 latency** | 391053.75 ms |
| **p999 latency** | 436403.75 ms |
| **Error rate** | 67.00% (0.67) |
| **Total requests** | 59421 |
| **Failed requests** | 39705 |
| **Total successful** | 19716 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 300 |
| observed_postgres_backends_max_numbackends | 317 |
| observed_postgres_backends_avg_numbackends | 313.12 |
| observed_postgres_backends_median_numbackends | 313 |
| observed_client_backends_active_median | 32991 |
| observed_client_backends_active_max | 48536 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | hikari-prod |
| Configured replicas | 16 |
| Configured client pool size (per replica) | 19 |
| OJP servers | N/A |
| Real DB connections per OJP server | N/A |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| OJP proxy-tier host_cpu (avg / peak) | N/A% / N/A% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 0% |
| OJP proxy-tier RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| PgBouncer tier RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | N/A% / N/A% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 0.00% |
| Total PgBouncer proxy-tier RSS (avg / peak) | N/A MiB / 0.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.03% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 0 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (152166.88 ms) |
| Error rate | < 0.1% | ❌ FAIL (67.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 61.69 RPS (all instances) |
| **Achieved throughput** | 21.09 RPS (all instances) |
| **Attempted − achieved gap** | 40.60 RPS (65.82%) |
| **Total attempted ops** | 57614 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 25214.975 | 140378.111 | 367263.743 | 1.4342153954092274 | 63.97% | 0.02501876407305479 | 0 |
| 10 | 25673.727 | 166068.223 | 394002.431 | 1.1518642661116614 | 71.06% | 0.02501876407305479 | 0 |
| 11 | 25460.735 | 161611.775 | 373030.911 | 1.255606915891449 | 68.27% | 0.025025025025025023 | 0 |
| 12 | 26165.247 | 150077.439 | 399245.311 | 1.3219152369982257 | 66.79% | 0.02501876407305479 | 0 |
| 13 | 25542.655 | 162136.063 | 408420.351 | 1.1679069439126595 | 70.65% | 0.02502815667626079 | 0 |
| 14 | 24936.447 | 147455.999 | 386924.543 | 1.3026668306586595 | 67.27% | 0.025021894157387717 | 0 |
| 15 | 24788.991 | 146276.351 | 401866.751 | 1.3529324945508372 | 65.75% | 0.025025025025025023 | 0 |
| 1 | 25509.887 | 168427.519 | 418906.111 | 1.1015972090018673 | 72.32% | 0.025025025025025023 | 0 |
| 2 | 23904.255 | 143917.055 | 402653.183 | 1.4267288124354283 | 64.15% | 0.025021894157387717 | 0 |
| 3 | 25526.271 | 145489.919 | 371195.903 | 1.4673686934964123 | 62.90% | 0.025025025025025023 | 0 |
| 4 | 26001.407 | 165937.151 | 400818.175 | 1.0994570094127638 | 72.32% | 0.02501876407305479 | 0 |
| 5 | 24575.999 | 139591.679 | 377749.503 | 1.4930369505255041 | 62.43% | 0.025025025025025023 | 0 |
| 6 | 23658.495 | 141426.687 | 398983.167 | 1.3903654094198326 | 64.83% | 0.025021894157387717 | 0 |
| 7 | 25460.735 | 158466.047 | 395313.151 | 1.2844837359332455 | 67.75% | 0.025025025025025023 | 0 |
| 8 | 24526.847 | 137101.311 | 354156.543 | 1.5785978072891433 | 60.27% | 0.025021894157387717 | 0 |
| 9 | 25460.735 | 160301.055 | 406323.199 | 1.2577459395982487 | 68.35% | 0.025025025025025023 | 0 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 2381 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 10 | SQLTransientConnectionException | 2644 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 11 | SQLTransientConnectionException | 2526 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=99) |
| 12 | SQLTransientConnectionException | 2486 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 13 | SQLTransientConnectionException | 2629 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 14 | SQLTransientConnectionException | 2503 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 15 | SQLTransientConnectionException | 2428 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 1 | SQLTransientConnectionException | 2691 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 2 | SQLTransientConnectionException | 2387 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 3 | SQLTransientConnectionException | 2326 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=97) |
| 4 | SQLTransientConnectionException | 2686 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 5 | SQLTransientConnectionException | 2320 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 6 | SQLTransientConnectionException | 2396 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 7 | SQLTransientConnectionException | 2523 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 8 | SQLTransientConnectionException | 2239 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 9 | SQLTransientConnectionException | 2540 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T22:37:17Z → 2026-07-15T22:52:17Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 313 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 32991 / 48536 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2925703372 | Cumulative since stats reset |
| Transactions rolled back | 1000 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5747 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 416704 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T22:37:17Z → 2026-07-15T22:52:17Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 1085.7 | 1082.2 | 1155.6 | 1173.6 | 1173.6 | 1599.6 | 1599.6 | 1599.8 | 1599.9 | 1599.9 | 362078.5 | 394571.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T22:56:09Z*
