# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T10:59:09Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 3 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260715-114737` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.29 RPS (per instance) |
| **Total throughput** | 20.60 RPS (all instances) |
| **p50 latency** | 21126.06 ms |
| **p95 latency** | 145620.00 ms |
| **p99 latency** | 391595.00 ms |
| **p999 latency** | 437569.38 ms |
| **Error rate** | 57.00% (0.57) |
| **Total requests** | 44543 |
| **Failed requests** | 25285 |
| **Total successful** | 19258 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 300 |
| observed_postgres_backends_max_numbackends | 317 |
| observed_postgres_backends_avg_numbackends | 313.32 |
| observed_postgres_backends_median_numbackends | 313 |
| observed_client_backends_active_median | 33792 |
| observed_client_backends_active_max | 48983 |
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
| p95 latency | < 1500 ms | ❌ FAIL (145620.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (57.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.32 RPS (all instances) |
| **Achieved throughput** | 20.60 RPS (all instances) |
| **Attempted − achieved gap** | 25.72 RPS (55.53%) |
| **Total attempted ops** | 43211 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 20299.775 | 143654.911 | 400556.031 | 1.1625581412759478 | 60.74% | 0.025021894157387717 | 0 |
| 10 | 21430.271 | 152436.735 | 398721.023 | 1.2791361766662461 | 57.15% | 0.025025025025025023 | 0 |
| 11 | 22872.063 | 149291.007 | 408682.495 | 1.1636276519854931 | 61.02% | 0.025021894157387717 | 0 |
| 12 | 20856.831 | 145883.135 | 390070.271 | 1.32940323377604 | 55.11% | 0.025021894157387717 | 0 |
| 13 | 20201.471 | 142999.551 | 399245.311 | 1.211756929902054 | 59.05% | 0.02501876407305479 | 0 |
| 14 | 21512.191 | 146931.711 | 360185.855 | 1.3807398027392337 | 53.36% | 0.025021894157387717 | 0 |
| 15 | 20234.239 | 138805.247 | 374079.487 | 1.398920008085501 | 52.75% | 0.025021894157387717 | 0 |
| 1 | 20267.007 | 150208.511 | 406585.343 | 1.2663006801018604 | 57.58% | 0.025021894157387717 | 0 |
| 2 | 19677.183 | 144048.127 | 391380.991 | 1.2673715462788475 | 57.54% | 0.025021894157387717 | 0 |
| 3 | 22036.479 | 146014.207 | 390070.271 | 1.3208457262886804 | 55.77% | 0.025021894157387717 | 0 |
| 4 | 21495.807 | 146931.711 | 393215.999 | 1.2138959536088538 | 59.33% | 0.025025025025025023 | 0 |
| 5 | 21381.119 | 142344.191 | 410517.503 | 1.2395642380904508 | 58.47% | 0.025021894157387717 | 0 |
| 6 | 22527.999 | 155844.607 | 403701.759 | 1.1999922995146555 | 59.81% | 0.025021894157387717 | 0 |
| 7 | 20807.679 | 142082.047 | 379060.223 | 1.3807383260232278 | 53.68% | 0.02501876407305479 | 0 |
| 8 | 20824.063 | 138543.103 | 375652.351 | 1.4192422294616291 | 52.49% | 0.025025025025025023 | 0 |
| 9 | 21594.111 | 143917.055 | 383778.815 | 1.3625566439609544 | 54.37% | 0.025021894157387717 | 0 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 1682 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=77) |
| 10 | SQLTransientConnectionException | 1595 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 11 | SQLTransientConnectionException | 1703 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 12 | SQLTransientConnectionException | 1526 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=66) |
| 13 | SQLTransientConnectionException | 1634 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=66) |
| 14 | SQLTransientConnectionException | 1477 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 15 | SQLTransientConnectionException | 1460 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=80) |
| 1 | SQLTransientConnectionException | 1607 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 2 | SQLTransientConnectionException | 1606 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 3 | SQLTransientConnectionException | 1557 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 4 | SQLTransientConnectionException | 1656 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 5 | SQLTransientConnectionException | 1632 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 6 | SQLTransientConnectionException | 1670 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 7 | SQLTransientConnectionException | 1496 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 8 | SQLTransientConnectionException | 1466 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 9 | SQLTransientConnectionException | 1518 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T10:59:09Z → 2026-07-15T11:14:09Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 313 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 33792 / 48983 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2751328042 | Cumulative since stats reset |
| Transactions rolled back | 975 | Non-zero → contention or application errors |
| Temp file bytes written | -1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4823 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 335257 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T10:59:09Z → 2026-07-15T11:14:09Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 1090.9 | 1095.0 | 1152.8 | 1160.1 | 1160.1 | 1599.5 | 1599.6 | 1599.7 | 1599.8 | 1599.8 | 367843.8 | 394180.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T11:17:55Z*
