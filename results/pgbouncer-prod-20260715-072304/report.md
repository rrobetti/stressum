# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T06:34:59Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 2 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260715-072304` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.29 RPS (per instance) |
| **Total throughput** | 20.68 RPS (all instances) |
| **p50 latency** | 26669.06 ms |
| **p95 latency** | 47308.88 ms |
| **p99 latency** | 84598.75 ms |
| **p999 latency** | 113946.88 ms |
| **Error rate** | 34.00% (0.34) |
| **Total requests** | 29303 |
| **Failed requests** | 9997 |
| **Total successful** | 19306 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 58 |
| observed_postgres_backends_avg_numbackends | 51.51 |
| observed_postgres_backends_median_numbackends | 55 |
| observed_client_backends_active_median | 35082 |
| observed_client_backends_active_max | 51994 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | pgbouncer-prod |
| Configured replicas | 16 |
| Configured client pool size (per replica) | 20 |
| OJP servers | N/A |
| Real DB connections per OJP server | N/A |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.9% / 4.9% / 9.8% |
| OJP proxy-tier host_cpu (avg / peak) | 13.5% / 144.6% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 17.60% |
| OJP proxy-tier RSS (avg / peak, summed) | 35.00 MiB / 35.00 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 16 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.9% / 4.9% / 9.8% |
| PgBouncer tier RSS (avg / peak, summed) | 35.00 MiB / 35.00 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.8% / 0.0% / 2.9% / 5.8% / 10.7% |
| HAProxy RSS (avg / peak, summed) | 23.40 MiB / 23.80 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.4% / 1.0% / 4.9% / 10.7% / 17.5% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 18.4% / 150.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 28.30% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 58.40 MiB / 58.80 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.03% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 22 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (47308.88 ms) |
| Error rate | < 0.1% | ❌ FAIL (34.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 30.86 RPS (all instances) |
| **Achieved throughput** | 20.68 RPS (all instances) |
| **Attempted − achieved gap** | 10.18 RPS (32.99%) |
| **Total attempted ops** | 28813 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 26132.479 | 46956.543 | 82509.823 | 1.2705787229400423 | 34.69% | 0.02501876407305479 | 1 |
| 10 | 25231.359 | 46759.935 | 93782.015 | 1.3540005582845904 | 30.78% | 0.025021894157387717 | 1 |
| 11 | 26738.687 | 44990.463 | 81330.175 | 1.2360502517622285 | 37.35% | 0.02502345959120637 | 2 |
| 12 | 25018.367 | 44793.855 | 93585.407 | 1.4670503072875645 | 25.31% | 0.02501876407305479 | 1 |
| 13 | 27852.799 | 46825.471 | 79233.023 | 1.1529325448900383 | 41.13% | 0.025021894157387717 | 1 |
| 14 | 28852.223 | 48365.567 | 79364.095 | 1.1529325448900383 | 41.19% | 0.02501876407305479 | 1 |
| 15 | 25919.487 | 49283.071 | 94633.983 | 1.442041887779756 | 27.64% | 0.025021894157387717 | 1 |
| 1 | 26116.095 | 44957.695 | 73465.855 | 1.3978519923936317 | 28.42% | 0.025021894157387717 | 2 |
| 2 | 26247.167 | 45252.607 | 98041.855 | 1.303734949294443 | 33.21% | 0.02501876407305479 | 1 |
| 3 | 28540.927 | 52953.087 | 85458.943 | 1.2138959536088538 | 38.62% | 0.025021894157387717 | 2 |
| 4 | 27541.503 | 49250.303 | 74776.575 | 1.2855532477866451 | 34.17% | 0.02501876407305479 | 1 |
| 5 | 27803.647 | 48070.655 | 68157.439 | 1.1882251274855402 | 39.16% | 0.025021894157387717 | 2 |
| 6 | 25788.415 | 49053.695 | 90439.679 | 1.3422373760168385 | 31.20% | 0.02501876407305479 | 1 |
| 7 | 27459.583 | 48201.727 | 75694.079 | 1.1971508238710589 | 39.53% | 0.025021894157387717 | 2 |
| 8 | 25853.951 | 44728.319 | 88801.279 | 1.2994569018808435 | 33.50% | 0.02501876407305479 | 1 |
| 9 | 25608.191 | 46497.791 | 94306.303 | 1.3753922434722345 | 29.84% | 0.025021894157387717 | 2 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 627 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=3, active=3, idle=0, waiting=45) |
| 0 | SQLException | 2 | Connection is closed |
| 0 | PSQLException | 2 | FATAL: server shutting down |
| 10 | SQLTransientConnectionException | 554 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=41) |
| 10 | SQLException | 1 | Connection is closed |
| 10 | PSQLException | 8 | FATAL: server shutting down |
| 11 | SQLTransientConnectionException | 682 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=6, active=6, idle=0, waiting=44) |
| 11 | SQLException | 1 | Connection is closed |
| 11 | PSQLException | 5 | FATAL: server shutting down |
| 12 | SQLTransientConnectionException | 456 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=8, active=8, idle=0, waiting=36) |
| 12 | SQLException | 3 | Connection is closed |
| 12 | PSQLException | 5 | FATAL: server shutting down |
| 13 | SQLTransientConnectionException | 744 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=9, active=9, idle=0, waiting=38) |
| 13 | SQLException | 1 | Connection is closed |
| 13 | PSQLException | 6 | FATAL: server shutting down |
| 14 | SQLTransientConnectionException | 750 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=7, active=7, idle=0, waiting=47) |
| 14 | SQLException | 1 | Connection is closed |
| 14 | PSQLException | 3 | FATAL: server shutting down |
| 15 | SQLTransientConnectionException | 494 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=44) |
| 15 | SQLException | 1 | Connection is closed |
| 15 | PSQLException | 11 | FATAL: server shutting down |
| 1 | SQLTransientConnectionException | 509 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=6, active=6, idle=0, waiting=36) |
| 1 | SQLException | 1 | Connection is closed |
| 1 | PSQLException | 9 | FATAL: server shutting down |
| 2 | SQLTransientConnectionException | 603 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=5, active=5, idle=0, waiting=39) |
| 2 | SQLException | 1 | Connection is closed |
| 2 | PSQLException | 2 | FATAL: server shutting down |
| 3 | SQLTransientConnectionException | 708 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=6, active=6, idle=0, waiting=45) |
| 3 | SQLException | 2 | Connection is closed |
| 3 | PSQLException | 4 | FATAL: server shutting down |
| 4 | SQLTransientConnectionException | 614 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=32) |
| 4 | SQLException | 4 | Connection is closed |
| 4 | PSQLException | 6 | FATAL: server shutting down |
| 5 | SQLTransientConnectionException | 706 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=7, active=7, idle=0, waiting=39) |
| 5 | SQLException | 3 | Connection is closed |
| 5 | PSQLException | 6 | FATAL: server shutting down |
| 6 | SQLTransientConnectionException | 560 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=39) |
| 6 | SQLException | 2 | Connection is closed |
| 6 | PSQLException | 7 | FATAL: server shutting down |
| 7 | SQLTransientConnectionException | 721 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=42) |
| 7 | SQLException | 1 | Connection is closed |
| 7 | PSQLException | 9 | FATAL: server shutting down |
| 8 | SQLTransientConnectionException | 602 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=42) |
| 8 | SQLException | 4 | Connection is closed |
| 8 | PSQLException | 6 | FATAL: server shutting down |
| 9 | SQLTransientConnectionException | 537 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=5, active=5, idle=0, waiting=43) |
| 9 | SQLException | 2 | Connection is closed |
| 9 | PSQLException | 8 | FATAL: server shutting down |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T06:34:59Z → 2026-07-15T06:49:59Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 55 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 35082 / 51994 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2136859248 | Cumulative since stats reset |
| Transactions rolled back | 1001 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4760 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 481514 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T06:34:59Z → 2026-07-15T06:49:59Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.3 | 0.0 | 2.0 | 2.9 | 6.8 | 4.9 | 2.9 | 28.4 | 33.4 | 47.1 | 11.7 | 11.7 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.3 | 0.0 | 1.0 | 2.9 | 4.9 | 4.3 | 2.9 | 15.6 | 33.3 | 35.2 | 11.7 | 11.7 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.9 | 5.9 | 9.1 | 2.9 | 96.2 | 107.9 | 132.0 | 11.6 | 11.6 |
| PostgreSQL | db | 1138.5 | 1154.6 | 1228.0 | 1251.5 | 1268.1 | 1598.5 | 1598.5 | 1599.2 | 1599.4 | 1599.5 | 129108.1 | 154359.0 |
| HAProxy | lb | 0.8 | 0.0 | 2.9 | 5.8 | 10.7 | 5.0 | 3.9 | 10.8 | 34.1 | 38.0 | 23.4 | 23.8 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T06:54:01Z*
