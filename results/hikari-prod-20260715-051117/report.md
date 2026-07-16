# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T04:23:06Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 2 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260715-051117` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.08 RPS (per instance) |
| **Total throughput** | 17.23 RPS (all instances) |
| **p50 latency** | 1956.21 ms |
| **p95 latency** | 134917.50 ms |
| **p99 latency** | 405946.25 ms |
| **p999 latency** | 584975.00 ms |
| **Error rate** | 44.00% (0.44) |
| **Total requests** | 28753 |
| **Failed requests** | 12640 |
| **Total successful** | 16113 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 300 |
| observed_postgres_backends_max_numbackends | 315 |
| observed_postgres_backends_avg_numbackends | 312.10 |
| observed_postgres_backends_median_numbackends | 312 |
| observed_client_backends_active_median | 32568 |
| observed_client_backends_active_max | 43824 |
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
| **bench_jvm_cpu (median)** | 0.02% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 0 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (134917.50 ms) |
| Error rate | < 0.1% | ❌ FAIL (44.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 30.82 RPS (all instances) |
| **Achieved throughput** | 17.23 RPS (all instances) |
| **Attempted − achieved gap** | 13.59 RPS (44.08%) |
| **Total attempted ops** | 28813 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 86.655 | 132907.007 | 322699.263 | 1.0973179879936727 | 42.87% | 0.02501876407305479 | 0 |
| 10 | 235.391 | 143261.695 | 444858.367 | 1.0545375596118531 | 45.19% | 0.02501876407305479 | 0 |
| 11 | 6197.247 | 135659.519 | 425721.855 | 1.0481193743796844 | 45.46% | 0.025025025025025023 | 0 |
| 12 | 3977.215 | 130940.927 | 353370.111 | 1.1561410770186749 | 39.88% | 0.02501876407305479 | 0 |
| 13 | 55.967 | 145620.991 | 515899.391 | 0.918709699499576 | 52.14% | 0.025025025025025023 | 0 |
| 14 | 969.727 | 135397.375 | 391118.847 | 1.1101521165082187 | 42.20% | 0.02501876407305479 | 0 |
| 15 | 2289.663 | 160432.127 | 461373.439 | 1.0470509846450349 | 45.61% | 0.025025025025025023 | 0 |
| 1 | 182.783 | 134348.799 | 403701.759 | 0.9999925134250333 | 47.94% | 0.025025025025025023 | 0 |
| 2 | 68.479 | 149028.863 | 382205.951 | 0.9914364277486694 | 48.41% | 0.02501876407305479 | 0 |
| 3 | 5468.159 | 145883.135 | 443809.791 | 1.113361839389266 | 42.10% | 0.025025025025025023 | 0 |
| 4 | 108.159 | 136708.095 | 368574.463 | 1.137960612017463 | 40.89% | 0.025015634771732333 | 0 |
| 5 | 2633.727 | 76873.727 | 331350.015 | 1.2320763373964045 | 35.82% | 0.025025025025025023 | 0 |
| 6 | 3037.183 | 152043.519 | 397148.159 | 1.029939914824076 | 46.44% | 0.025015634771732333 | 0 |
| 7 | 4837.375 | 125042.687 | 412090.367 | 1.1529325448900383 | 40.04% | 0.025025025025025023 | 0 |
| 8 | 616.447 | 118489.087 | 432799.743 | 1.0545375596118531 | 44.98% | 0.012515644555694618 | 0 |
| 9 | 535.039 | 136052.735 | 408420.351 | 1.088761902317309 | 43.38% | 0.025025025025025023 | 0 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 770 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=46) |
| 10 | SQLTransientConnectionException | 813 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 11 | SQLTransientConnectionException | 817 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 12 | SQLTransientConnectionException | 717 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 13 | SQLTransientConnectionException | 936 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=38) |
| 14 | SQLTransientConnectionException | 758 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 15 | SQLTransientConnectionException | 821 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 1 | SQLTransientConnectionException | 861 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 2 | SQLTransientConnectionException | 870 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=41) |
| 3 | SQLTransientConnectionException | 757 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=46) |
| 4 | SQLTransientConnectionException | 736 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=45) |
| 5 | SQLTransientConnectionException | 643 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=46) |
| 6 | SQLTransientConnectionException | 835 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=43) |
| 7 | SQLTransientConnectionException | 720 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=46) |
| 8 | SQLTransientConnectionException | 806 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 9 | SQLTransientConnectionException | 780 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=46) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T04:23:06Z → 2026-07-15T04:38:06Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 312 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 32568 / 43824 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1907698904 | Cumulative since stats reset |
| Transactions rolled back | 784 | Non-zero → contention or application errors |
| Temp file bytes written | 87 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -87 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 1 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 3767 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 390048 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T04:23:06Z → 2026-07-15T04:38:06Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 840.3 | 832.2 | 929.0 | 944.8 | 944.8 | 1599.4 | 1599.4 | 1599.5 | 1599.6 | 1599.6 | 349865.6 | 392317.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T04:41:57Z*
