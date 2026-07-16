# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T06:01:49Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 2 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260715-065010` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.08 RPS (per instance) |
| **Total throughput** | 17.30 RPS (all instances) |
| **p50 latency** | 2709.99 ms |
| **p95 latency** | 141221.25 ms |
| **p99 latency** | 378011.25 ms |
| **p999 latency** | 580289.38 ms |
| **Error rate** | 44.00% (0.44) |
| **Total requests** | 28759 |
| **Failed requests** | 12582 |
| **Total successful** | 16177 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 300 |
| observed_postgres_backends_max_numbackends | 314 |
| observed_postgres_backends_avg_numbackends | 311.99 |
| observed_postgres_backends_median_numbackends | 312 |
| observed_client_backends_active_median | 32353 |
| observed_client_backends_active_max | 43825 |
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
| p95 latency | < 1500 ms | ❌ FAIL (141221.25 ms) |
| Error rate | < 0.1% | ❌ FAIL (44.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 30.82 RPS (all instances) |
| **Achieved throughput** | 17.30 RPS (all instances) |
| **Attempted − achieved gap** | 13.52 RPS (43.86%) |
| **Total attempted ops** | 28812 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 263.679 | 123404.287 | 337379.327 | 1.1326130527504636 | 40.97% | 0.025015634771732333 | 0 |
| 10 | 3731.455 | 151781.375 | 356515.839 | 1.0973191615882678 | 42.90% | 0.02501876407305479 | 0 |
| 11 | 1579.007 | 138149.887 | 396099.583 | 1.086622880898218 | 43.49% | 0.02501876407305479 | 0 |
| 12 | 4167.679 | 151126.015 | 353107.967 | 0.9796718099436689 | 49.08% | 0.025015634771732333 | 0 |
| 13 | 327.679 | 121372.671 | 391118.847 | 1.1614886305664023 | 39.60% | 0.025015634771732333 | 0 |
| 14 | 251.775 | 127270.911 | 324009.983 | 1.1540032898184611 | 39.92% | 0.025015634771732333 | 0 |
| 15 | 3788.799 | 142213.119 | 407109.631 | 1.055608199305673 | 45.08% | 0.02501876407305479 | 0 |
| 1 | 4341.759 | 147193.855 | 330301.439 | 1.088761902317309 | 43.38% | 0.02501876407305479 | 0 |
| 2 | 391.679 | 155058.175 | 340262.911 | 1.039563297854136 | 45.91% | 0.025015634771732333 | 0 |
| 3 | 4110.335 | 139460.607 | 402391.039 | 1.0812753273504905 | 43.68% | 0.02501876407305479 | 0 |
| 4 | 219.391 | 154664.959 | 428081.151 | 0.9871583849104874 | 48.55% | 0.025015634771732333 | 0 |
| 5 | 193.407 | 148242.431 | 417333.247 | 0.9839498527818509 | 48.83% | 0.02501876407305479 | 0 |
| 6 | 7032.831 | 140771.327 | 457441.279 | 1.0470509846450349 | 45.55% | 0.025015634771732333 | 0 |
| 7 | 2543.615 | 116981.759 | 418906.111 | 1.115499670055946 | 42.02% | 0.02501876407305479 | 0 |
| 8 | 10231.807 | 152436.735 | 351010.815 | 1.2053398587816548 | 37.42% | 0.02501876407305479 | 0 |
| 9 | 184.959 | 149422.079 | 337117.183 | 1.0855533701886724 | 43.61% | 0.02501876407305479 | 0 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 735 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=46) |
| 10 | SQLTransientConnectionException | 771 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 11 | SQLTransientConnectionException | 782 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 12 | SQLTransientConnectionException | 883 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=41) |
| 13 | SQLTransientConnectionException | 712 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=39) |
| 14 | SQLTransientConnectionException | 717 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 15 | SQLTransientConnectionException | 810 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 1 | SQLTransientConnectionException | 780 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 2 | SQLTransientConnectionException | 825 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 3 | SQLTransientConnectionException | 784 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 4 | SQLTransientConnectionException | 871 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=46) |
| 5 | SQLTransientConnectionException | 878 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 6 | SQLTransientConnectionException | 819 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 7 | SQLTransientConnectionException | 756 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 8 | SQLTransientConnectionException | 674 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=46) |
| 9 | SQLTransientConnectionException | 785 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T06:01:49Z → 2026-07-15T06:16:49Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 312 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 32353 / 43825 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1939137438 | Cumulative since stats reset |
| Transactions rolled back | 799 | Non-zero → contention or application errors |
| Temp file bytes written | 84 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -84 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 3723 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 385290 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T06:01:49Z → 2026-07-15T06:16:49Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 828.1 | 823.8 | 938.5 | 959.7 | 959.7 | 1599.4 | 1599.4 | 1599.7 | 1599.7 | 1599.7 | 347424.1 | 381923.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T06:20:37Z*
