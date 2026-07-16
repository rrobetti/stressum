# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T02:44:06Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 2 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260715-033223` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.08 RPS (per instance) |
| **Total throughput** | 17.35 RPS (all instances) |
| **p50 latency** | 1640.93 ms |
| **p95 latency** | 137355.00 ms |
| **p99 latency** | 376406.25 ms |
| **p999 latency** | 566083.12 ms |
| **Error rate** | 44.00% (0.44) |
| **Total requests** | 28733 |
| **Failed requests** | 12509 |
| **Total successful** | 16224 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 300 |
| observed_postgres_backends_max_numbackends | 313 |
| observed_postgres_backends_avg_numbackends | 311.87 |
| observed_postgres_backends_median_numbackends | 312 |
| observed_client_backends_active_median | 32858 |
| observed_client_backends_active_max | 44501 |
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
| p95 latency | < 1500 ms | ❌ FAIL (137355.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (44.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 30.82 RPS (all instances) |
| **Achieved throughput** | 17.35 RPS (all instances) |
| **Attempted − achieved gap** | 13.47 RPS (43.70%) |
| **Total attempted ops** | 28813 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 132.479 | 117112.831 | 358612.991 | 1.0866240430542693 | 43.37% | 0.025015634771732333 | 0 |
| 10 | 55.039 | 166068.223 | 445906.943 | 0.8983889960182116 | 53.26% | 0.025015634771732333 | 0 |
| 11 | 2258.943 | 139198.463 | 348651.519 | 1.1037350522509457 | 42.54% | 0.025021894157387717 | 0 |
| 12 | 1617.919 | 143654.911 | 384303.103 | 1.0769984363736704 | 43.96% | 0.02501876407305479 | 0 |
| 13 | 207.231 | 133758.975 | 360972.287 | 1.0470509846450349 | 45.43% | 0.02501876407305479 | 0 |
| 14 | 2138.111 | 146931.711 | 387973.119 | 1.0876923916077634 | 43.41% | 0.02501876407305479 | 0 |
| 15 | 226.047 | 156368.895 | 394788.863 | 1.0630936452882171 | 44.72% | 0.025021894157387717 | 0 |
| 1 | 2344.959 | 128122.879 | 378798.079 | 1.1604203609388604 | 39.55% | 0.025021894157387717 | 0 |
| 2 | 4143.103 | 72876.031 | 386138.111 | 1.2470494873300415 | 35.04% | 0.025021894157387717 | 0 |
| 3 | 208.127 | 150732.799 | 411041.791 | 0.9796707621752968 | 49.05% | 0.025021894157387717 | 0 |
| 4 | 166.399 | 142737.407 | 413925.375 | 1.139028905665947 | 40.73% | 0.025015634771732333 | 0 |
| 5 | 370.175 | 146014.207 | 325058.559 | 1.0834155074940697 | 43.63% | 0.025021894157387717 | 0 |
| 6 | 5890.047 | 120979.455 | 340787.199 | 1.0983886734416677 | 42.85% | 0.02501250625312656 | 0 |
| 7 | 229.503 | 151257.087 | 409206.783 | 1.0449130807716742 | 45.63% | 0.025021894157387717 | 0 |
| 8 | 3563.519 | 151781.375 | 343670.783 | 1.1475849913423108 | 40.29% | 0.02501876407305479 | 0 |
| 9 | 2703.359 | 130088.959 | 332660.735 | 1.0876923916077634 | 43.09% | 0.025021894157387717 | 0 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 778 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=46) |
| 10 | SQLTransientConnectionException | 957 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=46) |
| 11 | SQLTransientConnectionException | 764 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 12 | SQLTransientConnectionException | 790 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=46) |
| 13 | SQLTransientConnectionException | 815 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 14 | SQLTransientConnectionException | 780 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 15 | SQLTransientConnectionException | 804 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=46) |
| 1 | SQLTransientConnectionException | 710 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 2 | SQLTransientConnectionException | 629 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 3 | SQLTransientConnectionException | 882 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=31) |
| 4 | SQLTransientConnectionException | 732 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=45) |
| 5 | SQLTransientConnectionException | 784 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=46) |
| 6 | SQLTransientConnectionException | 770 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 7 | SQLTransientConnectionException | 820 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 8 | SQLTransientConnectionException | 724 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
| 9 | SQLTransientConnectionException | 770 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=46) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T02:44:06Z → 2026-07-15T02:59:06Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 312 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 32858 / 44501 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1929510324 | Cumulative since stats reset |
| Transactions rolled back | 830 | Non-zero → contention or application errors |
| Temp file bytes written | 103 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -102 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 3703 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 382998 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T02:44:06Z → 2026-07-15T02:59:06Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 828.3 | 815.6 | 930.3 | 969.7 | 969.7 | 1599.5 | 1599.5 | 1599.7 | 1599.7 | 1599.7 | 348255.9 | 382127.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T03:02:58Z*
