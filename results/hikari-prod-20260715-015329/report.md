# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T01:05:17Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 2 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260715-015329` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.09 RPS (per instance) |
| **Total throughput** | 17.48 RPS (all instances) |
| **p50 latency** | 2092.79 ms |
| **p95 latency** | 132817.50 ms |
| **p99 latency** | 392069.38 ms |
| **p999 latency** | 581206.88 ms |
| **Error rate** | 43.00% (0.43) |
| **Total requests** | 28742 |
| **Failed requests** | 12398 |
| **Total successful** | 16344 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 300 |
| observed_postgres_backends_max_numbackends | 315 |
| observed_postgres_backends_avg_numbackends | 311.87 |
| observed_postgres_backends_median_numbackends | 312 |
| observed_client_backends_active_median | 32527 |
| observed_client_backends_active_max | 44334 |
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
| p95 latency | < 1500 ms | ❌ FAIL (132817.50 ms) |
| Error rate | < 0.1% | ❌ FAIL (43.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 30.82 RPS (all instances) |
| **Achieved throughput** | 17.48 RPS (all instances) |
| **Attempted − achieved gap** | 13.34 RPS (43.28%) |
| **Total attempted ops** | 28815 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 5119.999 | 92471.295 | 299368.447 | 1.2534678921846492 | 34.74% | 0.025015634771732333 | 0 |
| 10 | 366.079 | 128843.775 | 337903.615 | 1.1828801098602577 | 38.42% | 0.025015634771732333 | 0 |
| 11 | 187.775 | 160432.127 | 433586.175 | 0.9786022992341235 | 48.97% | 0.02501876407305479 | 0 |
| 12 | 5963.775 | 141295.615 | 427294.719 | 1.1614898727922602 | 39.63% | 0.025015634771732333 | 0 |
| 13 | 150.527 | 155713.535 | 439091.199 | 0.9497255100763952 | 50.47% | 0.02501876407305479 | 0 |
| 14 | 413.695 | 119930.879 | 400818.175 | 1.1144313512426658 | 41.98% | 0.02501250625312656 | 0 |
| 15 | 7200.767 | 108986.367 | 315097.087 | 1.23314584810595 | 35.87% | 0.02501876407305479 | 0 |
| 1 | 103.359 | 120193.023 | 316145.663 | 1.1251252664418556 | 41.46% | 0.02501876407305479 | 0 |
| 2 | 119.615 | 140509.183 | 400293.887 | 1.0310083240018524 | 46.41% | 0.025015634771732333 | 0 |
| 3 | 5484.543 | 120586.239 | 427294.719 | 1.1165691807654916 | 41.94% | 0.02501876407305479 | 0 |
| 4 | 301.567 | 131530.751 | 406061.055 | 1.072720388960071 | 44.15% | 0.025015634771732333 | 0 |
| 5 | 166.911 | 156499.967 | 433061.887 | 0.9796718099436689 | 49.05% | 0.02501876407305479 | 0 |
| 6 | 90.879 | 152829.951 | 464519.167 | 0.9454474672382133 | 50.81% | 0.02501876407305479 | 0 |
| 7 | 3866.623 | 119799.807 | 312737.791 | 1.2256579622848147 | 36.12% | 0.02501876407305479 | 0 |
| 8 | 3405.823 | 146538.495 | 435945.471 | 1.063094782279472 | 44.65% | 0.025015634771732333 | 0 |
| 9 | 542.719 | 128909.311 | 423886.847 | 1.0470509846450349 | 45.49% | 0.025015634771732333 | 0 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 624 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 10 | SQLTransientConnectionException | 690 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=46) |
| 11 | SQLTransientConnectionException | 878 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 12 | SQLTransientConnectionException | 713 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 13 | SQLTransientConnectionException | 905 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=46) |
| 14 | SQLTransientConnectionException | 754 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=39) |
| 15 | SQLTransientConnectionException | 645 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 1 | SQLTransientConnectionException | 745 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 2 | SQLTransientConnectionException | 835 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=39) |
| 3 | SQLTransientConnectionException | 754 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=43) |
| 4 | SQLTransientConnectionException | 793 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 5 | SQLTransientConnectionException | 882 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 6 | SQLTransientConnectionException | 913 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 7 | SQLTransientConnectionException | 648 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=29) |
| 8 | SQLTransientConnectionException | 802 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=46) |
| 9 | SQLTransientConnectionException | 817 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=43) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T01:05:17Z → 2026-07-15T01:20:17Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 312 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 32527 / 44334 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1973935853 | Cumulative since stats reset |
| Transactions rolled back | 819 | Non-zero → contention or application errors |
| Temp file bytes written | 86 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -82 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 1 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 3784 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 392173 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T01:05:17Z → 2026-07-15T01:20:17Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 824.9 | 819.7 | 911.1 | 979.4 | 979.4 | 1599.4 | 1599.5 | 1599.7 | 1599.7 | 1599.7 | 351327.3 | 388826.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T01:24:06Z*
