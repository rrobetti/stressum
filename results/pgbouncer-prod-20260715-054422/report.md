# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T04:56:18Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 2 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260715-054422` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.36 RPS (per instance) |
| **Total throughput** | 21.71 RPS (all instances) |
| **p50 latency** | 26337.31 ms |
| **p95 latency** | 45592.56 ms |
| **p99 latency** | 87191.88 ms |
| **p999 latency** | 119348.75 ms |
| **Error rate** | 31.00% (0.31) |
| **Total requests** | 29339 |
| **Failed requests** | 9060 |
| **Total successful** | 20279 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 58 |
| observed_postgres_backends_avg_numbackends | 55.43 |
| observed_postgres_backends_median_numbackends | 56 |
| observed_client_backends_active_median | 35827 |
| observed_client_backends_active_max | 52563 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.7% / 0.0% / 2.9% / 4.9% / 7.8% |
| OJP proxy-tier host_cpu (avg / peak) | 11.7% / 95.0% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 16.60% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.80 MiB / 35.00 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 16 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.7% / 0.0% / 2.9% / 4.9% / 7.8% |
| PgBouncer tier RSS (avg / peak, summed) | 34.80 MiB / 35.00 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.8% / 0.0% / 2.9% / 4.9% / 8.8% |
| HAProxy RSS (avg / peak, summed) | 23.10 MiB / 23.20 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.5% / 1.0% / 4.9% / 9.8% / 16.6% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 16.4% / 98.0% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 25.40% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 57.90 MiB / 58.20 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.03% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 25 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (45592.56 ms) |
| Error rate | < 0.1% | ❌ FAIL (31.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 30.86 RPS (all instances) |
| **Achieved throughput** | 21.71 RPS (all instances) |
| **Attempted − achieved gap** | 9.14 RPS (29.63%) |
| **Total attempted ops** | 28814 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 27525.119 | 46006.271 | 92798.975 | 1.2930398307604443 | 33.93% | 0.025015634771732333 | 2 |
| 10 | 27623.423 | 46989.311 | 86507.519 | 1.2502593566244495 | 36.43% | 0.02501876407305479 | 1 |
| 11 | 25034.751 | 47906.815 | 100073.471 | 1.4320763717024276 | 26.91% | 0.025021894157387717 | 1 |
| 12 | 28164.095 | 47841.279 | 100204.543 | 1.2748567657782242 | 35.01% | 0.02501876407305479 | 2 |
| 13 | 27426.815 | 43974.655 | 77791.231 | 1.3429870826130446 | 32.14% | 0.025021894157387717 | 2 |
| 14 | 27328.511 | 45187.071 | 75563.007 | 1.3674006548115811 | 30.96% | 0.02501876407305479 | 2 |
| 15 | 25772.031 | 46661.631 | 98041.855 | 1.3209884076309026 | 32.68% | 0.025021894157387717 | 1 |
| 1 | 21266.431 | 41811.967 | 84410.367 | 1.529401950361816 | 21.51% | 0.025021894157387717 | 2 |
| 2 | 26181.631 | 42237.951 | 79429.631 | 1.4286712497379694 | 27.10% | 0.02501876407305479 | 2 |
| 3 | 27328.511 | 46694.399 | 83492.863 | 1.3251237691268622 | 32.81% | 0.025021894157387717 | 2 |
| 4 | 26279.935 | 44630.015 | 83492.863 | 1.3315422574828397 | 32.08% | 0.02501876407305479 | 1 |
| 5 | 27705.343 | 47022.079 | 78446.591 | 1.2642756444249001 | 35.83% | 0.025021894157387717 | 2 |
| 6 | 24772.607 | 43253.759 | 75235.327 | 1.4737889102197315 | 24.82% | 0.02501876407305479 | 1 |
| 7 | 26705.919 | 44630.015 | 95813.631 | 1.3775297938945912 | 29.73% | 0.025021894157387717 | 1 |
| 8 | 27099.135 | 46628.863 | 103546.879 | 1.3358217335736173 | 31.64% | 0.025015634771732333 | 2 |
| 9 | 25182.207 | 48005.119 | 80216.063 | 1.3657651760895908 | 30.41% | 0.025021894157387717 | 1 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 621 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=18) |
| 10 | SQLTransientConnectionException | 670 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=42) |
| 11 | SQLTransientConnectionException | 493 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=9, active=9, idle=0, waiting=37) |
| 12 | SQLTransientConnectionException | 642 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=47) |
| 13 | SQLTransientConnectionException | 592 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=6, active=6, idle=0, waiting=36) |
| 14 | SQLTransientConnectionException | 573 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=35) |
| 15 | SQLTransientConnectionException | 599 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=47) |
| 1 | SQLTransientConnectionException | 392 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=6, active=6, idle=0, waiting=34) |
| 2 | SQLTransientConnectionException | 494 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=5, active=5, idle=0, waiting=47) |
| 3 | SQLTransientConnectionException | 605 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=9, active=9, idle=0, waiting=41) |
| 4 | SQLTransientConnectionException | 588 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=7, active=7, idle=0, waiting=34) |
| 5 | SQLTransientConnectionException | 655 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=6, active=6, idle=0, waiting=44) |
| 6 | SQLTransientConnectionException | 455 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=28) |
| 7 | SQLTransientConnectionException | 545 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=31) |
| 8 | SQLTransientConnectionException | 578 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=6, active=6, idle=0, waiting=43) |
| 9 | SQLTransientConnectionException | 558 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=31) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T04:56:18Z → 2026-07-15T05:11:18Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 56 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 35827 / 52563 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2157282776 | Cumulative since stats reset |
| Transactions rolled back | 1006 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4844 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 489339 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T04:56:18Z → 2026-07-15T05:11:18Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 2.9 | 2.9 | 3.9 | 9.8 | 57.9 | 11.6 | 11.6 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.9 | 5.9 | 4.9 | 2.9 | 31.3 | 34.2 | 62.6 | 11.6 | 11.7 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.3 | 0.0 | 1.9 | 2.9 | 6.8 | 4.2 | 2.9 | 5.9 | 34.2 | 64.5 | 11.6 | 11.7 |
| PostgreSQL | db | 1164.2 | 1169.7 | 1241.7 | 1254.8 | 1269.9 | 1598.6 | 1598.6 | 1599.3 | 1599.4 | 1599.5 | 149742.3 | 155688.0 |
| HAProxy | lb | 0.8 | 0.0 | 2.9 | 4.9 | 8.8 | 4.8 | 3.9 | 8.7 | 34.1 | 42.9 | 23.1 | 23.2 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T05:15:18Z*
