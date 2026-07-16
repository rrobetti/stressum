# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T09:52:43Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 3 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260715-104040` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.52 RPS (per instance) |
| **Total throughput** | 24.34 RPS (all instances) |
| **p50 latency** | 31530.06 ms |
| **p95 latency** | 49500.19 ms |
| **p99 latency** | 84098.75 ms |
| **p999 latency** | 104321.25 ms |
| **Error rate** | 49.00% (0.49) |
| **Total requests** | 44640 |
| **Failed requests** | 21885 |
| **Total successful** | 22755 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 59 |
| observed_postgres_backends_avg_numbackends | 56.29 |
| observed_postgres_backends_median_numbackends | 56 |
| observed_client_backends_active_median | 38561 |
| observed_client_backends_active_max | 57904 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.8% / 0.0% / 2.9% / 3.9% / 6.8% |
| OJP proxy-tier host_cpu (avg / peak) | 9.9% / 55.7% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 10.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 35.10 MiB / 35.10 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 16 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.8% / 0.0% / 2.9% / 3.9% / 6.8% |
| PgBouncer tier RSS (avg / peak, summed) | 35.10 MiB / 35.10 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.9% / 1.0% / 2.9% / 4.8% / 5.8% |
| HAProxy RSS (avg / peak, summed) | 22.90 MiB / 23.10 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.7% / 1.0% / 4.9% / 7.8% / 11.7% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 14.2% / 58.7% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 16.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 58.00 MiB / 58.20 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.03% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 28 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (49500.19 ms) |
| Error rate | < 0.1% | ❌ FAIL (49.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.22 RPS (all instances) |
| **Achieved throughput** | 24.34 RPS (all instances) |
| **Attempted − achieved gap** | 21.88 RPS (47.35%) |
| **Total attempted ops** | 43212 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 30982.143 | 49446.911 | 93323.263 | 1.5711129126444108 | 47.16% | 0.025025025025025023 | 1 |
| 10 | 31014.911 | 49807.359 | 93585.407 | 1.5400970688958147 | 48.37% | 0.025025025025025023 | 2 |
| 11 | 31342.591 | 48365.567 | 73334.783 | 1.512288143297323 | 49.39% | 0.025025025025025023 | 2 |
| 12 | 31752.191 | 53379.071 | 95289.343 | 1.4566751443306247 | 51.24% | 0.025025025025025023 | 1 |
| 13 | 31768.575 | 49512.447 | 79953.919 | 1.5689738889376112 | 47.40% | 0.02502815667626079 | 2 |
| 14 | 31571.967 | 50561.023 | 79626.239 | 1.5828775430318094 | 46.97% | 0.025025025025025023 | 2 |
| 15 | 31866.879 | 44269.567 | 77529.087 | 1.4106846258905015 | 52.69% | 0.025025025025025023 | 2 |
| 1 | 31997.951 | 53051.391 | 92012.543 | 1.417100174543961 | 52.61% | 0.02502815667626079 | 2 |
| 2 | 31440.895 | 44859.391 | 76546.047 | 1.5582787704036125 | 47.91% | 0.02502815667626079 | 1 |
| 3 | 31260.671 | 50888.703 | 91029.503 | 1.562555146645961 | 47.14% | 0.02502815667626079 | 2 |
| 4 | 31490.047 | 49184.767 | 77791.231 | 1.4791348932520219 | 50.50% | 0.025025025025025023 | 1 |
| 5 | 31571.967 | 47382.527 | 95551.487 | 1.4652312391578237 | 50.97% | 0.02502815667626079 | 2 |
| 6 | 31490.047 | 49545.215 | 76283.903 | 1.6117526392850536 | 45.97% | 0.02502815667626079 | 2 |
| 7 | 31473.663 | 51478.527 | 93716.479 | 1.5946404679323258 | 46.58% | 0.025025025025025023 | 3 |
| 8 | 31866.879 | 48922.623 | 76349.439 | 1.5069405897495955 | 49.61% | 0.025025025025025023 | 1 |
| 9 | 31588.351 | 51347.455 | 73662.463 | 1.4983845040732315 | 49.87% | 0.02502815667626079 | 2 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 1311 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=84) |
| 10 | SQLTransientConnectionException | 1349 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=85) |
| 11 | SQLTransientConnectionException | 1380 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=90) |
| 12 | SQLTransientConnectionException | 1431 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=90) |
| 13 | SQLTransientConnectionException | 1322 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=87) |
| 14 | SQLTransientConnectionException | 1311 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=90) |
| 15 | SQLTransientConnectionException | 1469 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=90) |
| 1 | SQLTransientConnectionException | 1471 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=90) |
| 2 | SQLTransientConnectionException | 1340 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=89) |
| 3 | SQLTransientConnectionException | 1303 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=71) |
| 4 | SQLTransientConnectionException | 1411 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=86) |
| 5 | SQLTransientConnectionException | 1424 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=90) |
| 6 | SQLTransientConnectionException | 1282 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=83) |
| 7 | SQLTransientConnectionException | 1300 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=89) |
| 8 | SQLTransientConnectionException | 1387 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=85) |
| 9 | SQLTransientConnectionException | 1394 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=90) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T09:52:43Z → 2026-07-15T10:07:43Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 56 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 38561 / 57904 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2654551567 | Cumulative since stats reset |
| Transactions rolled back | 1100 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5735 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 384690 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T09:52:43Z → 2026-07-15T10:07:43Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.3 | 0.0 | 1.0 | 2.9 | 3.9 | 3.2 | 2.9 | 4.9 | 32.3 | 33.4 | 11.7 | 11.7 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.3 | 0.0 | 1.0 | 2.9 | 3.9 | 3.8 | 2.9 | 5.9 | 33.2 | 49.9 | 11.7 | 11.7 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.3 | 0.0 | 1.9 | 1.9 | 2.9 | 3.2 | 2.9 | 4.9 | 9.7 | 34.2 | 11.7 | 11.7 |
| PostgreSQL | db | 1422.7 | 1424.4 | 1500.2 | 1543.0 | 1579.8 | 1599.4 | 1599.5 | 1600.0 | 1600.0 | 1600.0 | 146835.3 | 153046.0 |
| HAProxy | lb | 0.9 | 1.0 | 2.9 | 4.8 | 5.8 | 4.4 | 3.9 | 6.8 | 32.1 | 36.0 | 22.9 | 23.1 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T10:12:10Z*
