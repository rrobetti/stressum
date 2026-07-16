# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T14:17:48Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 3 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260715-150544` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.30 RPS (per instance) |
| **Total throughput** | 20.77 RPS (all instances) |
| **p50 latency** | 21431.44 ms |
| **p95 latency** | 142917.50 ms |
| **p99 latency** | 374620.62 ms |
| **p999 latency** | 430900.00 ms |
| **Error rate** | 56.00% (0.56) |
| **Total requests** | 44589 |
| **Failed requests** | 25169 |
| **Total successful** | 19420 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 300 |
| observed_postgres_backends_max_numbackends | 317 |
| observed_postgres_backends_avg_numbackends | 313.27 |
| observed_postgres_backends_median_numbackends | 313 |
| observed_client_backends_active_median | 34080 |
| observed_client_backends_active_max | 49491 |
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
| p95 latency | < 1500 ms | ❌ FAIL (142917.50 ms) |
| Error rate | < 0.1% | ❌ FAIL (56.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.34 RPS (all instances) |
| **Achieved throughput** | 20.77 RPS (all instances) |
| **Attempted − achieved gap** | 25.57 RPS (55.18%) |
| **Total attempted ops** | 43215 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 18612.223 | 136314.879 | 357564.415 | 1.3999910161004314 | 52.52% | 0.025015634771732333 | 0 |
| 10 | 20824.063 | 136314.879 | 354942.975 | 1.4310053293718656 | 52.06% | 0.025015634771732333 | 0 |
| 11 | 20922.367 | 138280.959 | 385613.823 | 1.3058739730012427 | 56.17% | 0.025021894157387717 | 0 |
| 12 | 19120.127 | 138674.175 | 381419.519 | 1.3818063588760738 | 53.74% | 0.025015634771732333 | 0 |
| 13 | 22003.711 | 150470.655 | 381419.519 | 1.2427741028122845 | 58.35% | 0.025021894157387717 | 0 |
| 14 | 22478.847 | 156106.751 | 398196.735 | 1.1219191341222774 | 62.41% | 0.025015634771732333 | 0 |
| 15 | 23609.343 | 159776.767 | 406847.487 | 1.0759289245202706 | 63.94% | 0.025021894157387717 | 0 |
| 1 | 23330.815 | 140509.183 | 319029.247 | 1.4256577758241382 | 52.19% | 0.025021894157387717 | 0 |
| 2 | 21184.511 | 136314.879 | 375914.495 | 1.4470495376500259 | 51.54% | 0.02501876407305479 | 0 |
| 3 | 21020.671 | 138412.031 | 378798.079 | 1.3187067048695893 | 55.84% | 0.025021894157387717 | 0 |
| 4 | 22380.543 | 147324.927 | 378798.079 | 1.1967837639544558 | 59.56% | 0.02501876407305479 | 0 |
| 5 | 21954.559 | 142606.335 | 360185.855 | 1.2898299157118611 | 56.79% | 0.025021894157387717 | 0 |
| 6 | 20955.135 | 136445.951 | 382468.095 | 1.3732532197654348 | 53.93% | 0.02501876407305479 | 0 |
| 7 | 21790.719 | 150601.727 | 383778.815 | 1.1989215054004945 | 59.85% | 0.025021894157387717 | 0 |
| 8 | 21479.423 | 141557.759 | 376963.071 | 1.2598849633050484 | 57.79% | 0.025015634771732333 | 0 |
| 9 | 21233.663 | 136970.239 | 371982.335 | 1.300525022807316 | 56.43% | 0.025025025025025023 | 0 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 1448 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=71) |
| 10 | SQLTransientConnectionException | 1453 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 11 | SQLTransientConnectionException | 1565 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 12 | SQLTransientConnectionException | 1501 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 13 | SQLTransientConnectionException | 1628 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 14 | SQLTransientConnectionException | 1742 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 15 | SQLTransientConnectionException | 1784 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 1 | SQLTransientConnectionException | 1455 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 2 | SQLTransientConnectionException | 1439 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 3 | SQLTransientConnectionException | 1559 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 4 | SQLTransientConnectionException | 1648 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=66) |
| 5 | SQLTransientConnectionException | 1585 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 6 | SQLTransientConnectionException | 1503 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 7 | SQLTransientConnectionException | 1671 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 8 | SQLTransientConnectionException | 1613 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 9 | SQLTransientConnectionException | 1575 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T14:17:48Z → 2026-07-15T14:32:48Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 313 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 34080 / 49491 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2831661718 | Cumulative since stats reset |
| Transactions rolled back | 937 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5227 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 346425 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T14:17:48Z → 2026-07-15T14:32:48Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 1081.7 | 1082.9 | 1173.9 | 1176.6 | 1176.6 | 1599.6 | 1599.6 | 1599.8 | 1599.9 | 1599.9 | 362823.0 | 394573.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T14:36:45Z*
