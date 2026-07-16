# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T03:17:21Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 2 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260715-040527` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.30 RPS (per instance) |
| **Total throughput** | 20.76 RPS (all instances) |
| **p50 latency** | 27504.62 ms |
| **p95 latency** | 46610.38 ms |
| **p99 latency** | 88424.38 ms |
| **p999 latency** | 118276.88 ms |
| **Error rate** | 34.00% (0.34) |
| **Total requests** | 29351 |
| **Failed requests** | 9962 |
| **Total successful** | 19389 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 58 |
| observed_postgres_backends_avg_numbackends | 55.26 |
| observed_postgres_backends_median_numbackends | 56 |
| observed_client_backends_active_median | 35006 |
| observed_client_backends_active_max | 51325 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.7% / 0.0% / 2.9% / 4.9% / 8.8% |
| OJP proxy-tier host_cpu (avg / peak) | 10.1% / 55.9% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 13.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.90 MiB / 34.90 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 16 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.7% / 0.0% / 2.9% / 4.9% / 8.8% |
| PgBouncer tier RSS (avg / peak, summed) | 34.90 MiB / 34.90 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.8% / 0.0% / 2.9% / 4.9% / 7.8% |
| HAProxy RSS (avg / peak, summed) | 23.10 MiB / 23.20 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.5% / 1.0% / 4.9% / 8.8% / 16.6% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 14.6% / 91.8% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 21.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 58.00 MiB / 58.10 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.03% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 29 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (46610.38 ms) |
| Error rate | < 0.1% | ❌ FAIL (34.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 30.85 RPS (all instances) |
| **Achieved throughput** | 20.76 RPS (all instances) |
| **Attempted − achieved gap** | 10.09 RPS (32.71%) |
| **Total attempted ops** | 28814 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 27394.047 | 44630.015 | 76218.367 | 1.2930384478404975 | 33.43% | 0.025015634771732333 | 1 |
| 10 | 27885.567 | 48726.015 | 104529.919 | 1.3004277892405696 | 33.95% | 0.025015634771732333 | 1 |
| 11 | 28033.023 | 47316.991 | 76021.759 | 1.2620212875183956 | 35.38% | 0.025021894157387717 | 3 |
| 12 | 27754.495 | 45514.751 | 77987.839 | 1.2823447122264457 | 34.45% | 0.025015634771732333 | 2 |
| 13 | 26820.607 | 43515.903 | 84606.975 | 1.3015959255876433 | 34.71% | 0.025025025025025023 | 2 |
| 14 | 26640.383 | 46202.879 | 99680.255 | 1.3546998284549423 | 31.18% | 0.025015634771732333 | 2 |
| 15 | 28229.631 | 47316.991 | 89522.175 | 1.3329449160513442 | 32.90% | 0.025025025025025023 | 2 |
| 1 | 25853.951 | 42532.863 | 75235.327 | 1.3753922434722345 | 29.80% | 0.025025025025025023 | 2 |
| 2 | 27279.359 | 45744.127 | 80281.599 | 1.3582771484308156 | 31.20% | 0.02501876407305479 | 2 |
| 3 | 26574.847 | 46399.487 | 94896.127 | 1.3144286620314074 | 32.88% | 0.025021894157387717 | 2 |
| 4 | 29065.215 | 49512.447 | 103481.343 | 1.2160349773156536 | 38.07% | 0.025015634771732333 | 1 |
| 5 | 28884.991 | 50561.023 | 106954.751 | 1.130472819989583 | 42.93% | 0.025025025025025023 | 2 |
| 6 | 26902.527 | 48955.391 | 82378.751 | 1.3326103440936807 | 32.36% | 0.025015634771732333 | 1 |
| 7 | 27754.495 | 46563.327 | 83361.791 | 1.2384934016536775 | 36.34% | 0.025021894157387717 | 2 |
| 8 | 27656.191 | 47218.687 | 100990.975 | 1.2930384478404975 | 33.86% | 0.025015634771732333 | 2 |
| 9 | 27344.895 | 45055.999 | 78643.199 | 1.3711127296373182 | 29.52% | 0.025025025025025023 | 2 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 607 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=7, active=7, idle=0, waiting=32) |
| 10 | SQLTransientConnectionException | 623 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=4, active=4, idle=0, waiting=53) |
| 11 | SQLTransientConnectionException | 646 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=2, active=2, idle=0, waiting=49) |
| 12 | SQLTransientConnectionException | 630 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=4, active=4, idle=0, waiting=52) |
| 13 | SQLTransientConnectionException | 647 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=53) |
| 14 | SQLTransientConnectionException | 570 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=10, active=10, idle=0, waiting=29) |
| 15 | SQLTransientConnectionException | 608 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=7, active=7, idle=0, waiting=52) |
| 1 | SQLTransientConnectionException | 546 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=30) |
| 2 | SQLTransientConnectionException | 576 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=38) |
| 3 | SQLTransientConnectionException | 602 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=34) |
| 4 | SQLTransientConnectionException | 699 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=6, active=6, idle=0, waiting=56) |
| 5 | SQLTransientConnectionException | 795 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=13, active=13, idle=0, waiting=47) |
| 6 | SQLTransientConnectionException | 596 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=41) |
| 7 | SQLTransientConnectionException | 661 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=3, active=3, idle=0, waiting=57) |
| 8 | SQLTransientConnectionException | 619 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=5, active=5, idle=0, waiting=50) |
| 9 | SQLTransientConnectionException | 537 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=50) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T03:17:21Z → 2026-07-15T03:32:21Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 56 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 35006 / 51325 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2170123376 | Cumulative since stats reset |
| Transactions rolled back | 959 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4589 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 464144 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T03:17:21Z → 2026-07-15T03:32:21Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 2.0 | 2.9 | 4.9 | 3.9 | 2.9 | 6.8 | 33.3 | 51.0 | 11.6 | 11.6 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.9 | 4.9 | 3.2 | 2.9 | 4.9 | 32.3 | 35.2 | 11.6 | 11.6 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.9 | 3.9 | 3.3 | 2.9 | 4.9 | 32.3 | 34.2 | 11.7 | 11.7 |
| PostgreSQL | db | 1175.6 | 1180.5 | 1248.1 | 1264.5 | 1300.7 | 1598.6 | 1598.6 | 1599.2 | 1599.4 | 1599.4 | 149460.5 | 155543.0 |
| HAProxy | lb | 0.8 | 0.0 | 2.9 | 4.9 | 7.8 | 4.5 | 3.9 | 6.9 | 34.0 | 35.9 | 23.1 | 23.2 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T03:36:20Z*
