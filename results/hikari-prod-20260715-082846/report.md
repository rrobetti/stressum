# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T07:40:31Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 2 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260715-082846` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.49 RPS (per instance) |
| **Total throughput** | 23.77 RPS (all instances) |
| **p50 latency** | 47.87 ms |
| **p95 latency** | 56596.44 ms |
| **p99 latency** | 235643.12 ms |
| **p999 latency** | 413778.12 ms |
| **Error rate** | 22.00% (0.22) |
| **Total requests** | 28656 |
| **Failed requests** | 6431 |
| **Total successful** | 22225 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 300 |
| observed_postgres_backends_max_numbackends | 318 |
| observed_postgres_backends_avg_numbackends | 301.52 |
| observed_postgres_backends_median_numbackends | 312 |
| observed_client_backends_active_median | 41013 |
| observed_client_backends_active_max | 53790 |
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
| p95 latency | < 1500 ms | ❌ FAIL (56596.44 ms) |
| Error rate | < 0.1% | ❌ FAIL (22.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 30.82 RPS (all instances) |
| **Achieved throughput** | 23.77 RPS (all instances) |
| **Attempted − achieved gap** | 7.05 RPS (22.87%) |
| **Total attempted ops** | 28811 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 42.047 | 53608.447 | 227672.063 | 1.5443734645836877 | 19.42% | 0.02502815667626079 | 0 |
| 10 | 41.439 | 56098.815 | 229769.215 | 1.4866198862682312 | 22.39% | 0.02502815667626079 | 0 |
| 11 | 57.887 | 58458.111 | 236453.887 | 1.465228105000171 | 23.46% | 0.025025025025025023 | 0 |
| 12 | 36.159 | 74842.111 | 247070.719 | 1.4074760937618649 | 26.60% | 0.025025025025025023 | 0 |
| 13 | 48.127 | 46432.255 | 241041.407 | 1.5443734645836877 | 19.33% | 0.025025025025025023 | 0 |
| 14 | 62.783 | 47808.511 | 228982.783 | 1.5614856359364155 | 18.44% | 0.02502815667626079 | 0 |
| 15 | 38.079 | 49971.199 | 249823.231 | 1.4716467363345944 | 23.21% | 0.025025025025025023 | 0 |
| 1 | 26.527 | 61669.375 | 229507.071 | 1.4374223936291386 | 24.92% | 0.02502815667626079 | 0 |
| 2 | 43.327 | 67829.759 | 231079.935 | 1.4887589076873222 | 22.36% | 0.02502815667626079 | 0 |
| 3 | 76.863 | 43646.975 | 238813.183 | 1.566833189484143 | 18.20% | 0.025025025025025023 | 0 |
| 4 | 41.407 | 55607.295 | 240517.119 | 1.394643456833432 | 27.15% | 0.025025025025025023 | 0 |
| 5 | 41.919 | 61603.839 | 239861.759 | 1.4662976145658646 | 23.41% | 0.025025025025025023 | 0 |
| 6 | 47.295 | 47874.047 | 228458.495 | 1.4930385473462202 | 22.01% | 0.025025025025025023 | 0 |
| 7 | 52.799 | 65339.391 | 230555.647 | 1.4652296720773215 | 23.59% | 0.025021894157387717 | 0 |
| 8 | 37.855 | 53280.767 | 241303.551 | 1.4331443507909567 | 25.18% | 0.025025025025025023 | 0 |
| 9 | 71.359 | 61472.767 | 229375.999 | 1.5433056044560143 | 19.39% | 0.025025025025025023 | 0 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 348 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=45) |
| 10 | SQLTransientConnectionException | 401 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=46) |
| 11 | SQLTransientConnectionException | 420 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=32) |
| 12 | SQLTransientConnectionException | 477 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=32) |
| 13 | SQLTransientConnectionException | 346 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=44) |
| 14 | SQLTransientConnectionException | 330 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=18) |
| 15 | SQLTransientConnectionException | 416 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=35) |
| 1 | SQLTransientConnectionException | 446 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=40) |
| 2 | SQLTransientConnectionException | 401 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=39) |
| 3 | SQLTransientConnectionException | 326 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=35) |
| 4 | SQLTransientConnectionException | 486 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=32) |
| 5 | SQLTransientConnectionException | 419 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=46) |
| 6 | SQLTransientConnectionException | 394 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=35) |
| 7 | SQLTransientConnectionException | 423 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 8 | SQLTransientConnectionException | 451 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=35) |
| 9 | SQLTransientConnectionException | 347 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=17) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T07:40:31Z → 2026-07-15T07:55:31Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 312 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 41013 / 53790 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2386519745 | Cumulative since stats reset |
| Transactions rolled back | 913 | Non-zero → contention or application errors |
| Temp file bytes written | 207 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -140 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 3889 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 397598 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T07:40:31Z → 2026-07-15T07:55:31Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 1116.5 | 1108.7 | 1267.1 | 1338.4 | 1338.4 | 1599.4 | 1599.4 | 1599.8 | 1599.8 | 1599.8 | 282381.6 | 382801.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T07:59:21Z*
