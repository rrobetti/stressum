# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T09:19:22Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 3 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260715-100738` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.34 RPS (per instance) |
| **Total throughput** | 21.40 RPS (all instances) |
| **p50 latency** | 21023.69 ms |
| **p95 latency** | 142679.38 ms |
| **p99 latency** | 371491.25 ms |
| **p999 latency** | 433471.25 ms |
| **Error rate** | 55.00% (0.55) |
| **Total requests** | 44610 |
| **Failed requests** | 24603 |
| **Total successful** | 20007 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 300 |
| observed_postgres_backends_max_numbackends | 316 |
| observed_postgres_backends_avg_numbackends | 312.39 |
| observed_postgres_backends_median_numbackends | 312 |
| observed_client_backends_active_median | 34782 |
| observed_client_backends_active_max | 49761 |
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
| p95 latency | < 1500 ms | ❌ FAIL (142679.38 ms) |
| Error rate | < 0.1% | ❌ FAIL (55.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.35 RPS (all instances) |
| **Achieved throughput** | 21.40 RPS (all instances) |
| **Attempted − achieved gap** | 24.95 RPS (53.83%) |
| **Total attempted ops** | 43215 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 20119.551 | 139067.391 | 342622.207 | 1.3443763997236382 | 54.98% | 0.025021894157387717 | 0 |
| 10 | 19644.415 | 137232.383 | 369360.895 | 1.3582786011227723 | 54.50% | 0.025025025025025023 | 0 |
| 11 | 21118.975 | 140902.399 | 339738.623 | 1.4759247791727763 | 50.56% | 0.025025025025025023 | 0 |
| 12 | 21397.503 | 138805.247 | 393478.143 | 1.3507934708440374 | 54.73% | 0.025021894157387717 | 0 |
| 13 | 22118.399 | 141819.903 | 371458.047 | 1.2844809883979602 | 57.00% | 0.025021894157387717 | 0 |
| 14 | 18694.143 | 139853.823 | 345767.935 | 1.3529324945508372 | 54.69% | 0.025021894157387717 | 0 |
| 15 | 21250.047 | 136970.239 | 322174.975 | 1.47271624704414 | 50.65% | 0.025021894157387717 | 0 |
| 1 | 21610.495 | 149553.151 | 379060.223 | 1.2834142240798456 | 57.00% | 0.025021894157387717 | 0 |
| 2 | 23658.495 | 159252.479 | 416808.959 | 1.1828801098602577 | 60.39% | 0.025021894157387717 | 0 |
| 3 | 21561.343 | 153354.239 | 393478.143 | 1.2064080803673127 | 59.60% | 0.025021894157387717 | 0 |
| 4 | 21118.975 | 142344.191 | 393215.999 | 1.3219166508022409 | 55.35% | 0.025021894157387717 | 0 |
| 5 | 21102.591 | 132055.039 | 361496.575 | 1.4438394578864115 | 51.23% | 0.025021894157387717 | 0 |
| 6 | 21266.431 | 158203.903 | 395837.439 | 1.2064093706350547 | 59.58% | 0.02501876407305479 | 0 |
| 7 | 21921.791 | 141426.687 | 387710.975 | 1.3326117693362396 | 55.36% | 0.025021894157387717 | 0 |
| 8 | 20643.839 | 141295.615 | 360710.143 | 1.346515423430438 | 54.83% | 0.025021894157387717 | 0 |
| 9 | 19152.895 | 130744.319 | 370933.759 | 1.4342153954092274 | 51.95% | 0.02501876407305479 | 0 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 1535 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 10 | SQLTransientConnectionException | 1521 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 11 | SQLTransientConnectionException | 1411 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 12 | SQLTransientConnectionException | 1527 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 13 | SQLTransientConnectionException | 1592 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 14 | SQLTransientConnectionException | 1527 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 15 | SQLTransientConnectionException | 1413 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 1 | SQLTransientConnectionException | 1591 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 2 | SQLTransientConnectionException | 1686 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 3 | SQLTransientConnectionException | 1664 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 4 | SQLTransientConnectionException | 1532 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 5 | SQLTransientConnectionException | 1418 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 6 | SQLTransientConnectionException | 1663 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 7 | SQLTransientConnectionException | 1545 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 8 | SQLTransientConnectionException | 1528 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 9 | SQLTransientConnectionException | 1450 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T09:19:22Z → 2026-07-15T09:34:22Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 312 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 34782 / 49761 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2841605628 | Cumulative since stats reset |
| Transactions rolled back | 977 | Non-zero → contention or application errors |
| Temp file bytes written | -1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5226 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 370012 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T09:19:22Z → 2026-07-15T09:34:22Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 1076.0 | 1067.1 | 1139.8 | 1160.1 | 1160.1 | 1599.6 | 1599.6 | 1599.8 | 1599.8 | 1599.8 | 358601.5 | 385429.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T09:38:16Z*
