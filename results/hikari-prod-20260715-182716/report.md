# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T17:39:06Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260715-182716` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.33 RPS (per instance) |
| **Total throughput** | 21.31 RPS (all instances) |
| **p50 latency** | 25025.56 ms |
| **p95 latency** | 151027.50 ms |
| **p99 latency** | 377798.12 ms |
| **p999 latency** | 443530.62 ms |
| **Error rate** | 66.00% (0.66) |
| **Total requests** | 59331 |
| **Failed requests** | 39404 |
| **Total successful** | 19927 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 300 |
| observed_postgres_backends_max_numbackends | 317 |
| observed_postgres_backends_avg_numbackends | 312.91 |
| observed_postgres_backends_median_numbackends | 313 |
| observed_client_backends_active_median | 32585 |
| observed_client_backends_active_max | 48747 |
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
| p95 latency | < 1500 ms | ❌ FAIL (151027.50 ms) |
| Error rate | < 0.1% | ❌ FAIL (66.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 61.67 RPS (all instances) |
| **Achieved throughput** | 21.31 RPS (all instances) |
| **Attempted − achieved gap** | 40.35 RPS (65.44%) |
| **Total attempted ops** | 57614 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 24805.375 | 139853.823 | 264110.079 | 1.503733665880219 | 62.03% | 0.025015634771732333 | 0 |
| 10 | 25264.127 | 148373.503 | 385875.967 | 1.3668361486450356 | 65.63% | 0.02501876407305479 | 0 |
| 11 | 25362.431 | 147455.999 | 398458.879 | 1.2481203329176498 | 68.36% | 0.025025025025025023 | 0 |
| 12 | 25526.271 | 146014.207 | 418643.967 | 1.228869119556452 | 69.14% | 0.02501876407305479 | 0 |
| 13 | 25280.511 | 152567.807 | 395313.151 | 1.3582786011227723 | 65.58% | 0.025021894157387717 | 0 |
| 14 | 25001.983 | 160432.127 | 401080.319 | 1.2064093706350547 | 69.63% | 0.025015634771732333 | 0 |
| 15 | 25395.199 | 164626.431 | 394788.863 | 1.2277982945582226 | 68.96% | 0.025025025025025023 | 0 |
| 1 | 24788.991 | 142475.263 | 386400.255 | 1.4224492436955019 | 64.02% | 0.025021894157387717 | 0 |
| 2 | 24346.623 | 153747.455 | 378798.079 | 1.4021285402141375 | 64.77% | 0.02501876407305479 | 0 |
| 3 | 22986.751 | 152698.879 | 386138.111 | 1.303734949294443 | 67.01% | 0.025025025025025023 | 0 |
| 4 | 25903.103 | 149291.007 | 329252.863 | 1.4203102222764108 | 64.26% | 0.02501876407305479 | 0 |
| 5 | 26312.703 | 175243.263 | 414449.663 | 1.0727192416741265 | 72.99% | 0.025021894157387717 | 0 |
| 6 | 24920.063 | 148766.719 | 262275.071 | 1.4876909880792208 | 62.63% | 0.02501876407305479 | 0 |
| 7 | 24723.455 | 146669.567 | 409993.215 | 1.3197762155791348 | 66.55% | 0.02501876407305479 | 0 |
| 8 | 24985.599 | 145883.135 | 410517.503 | 1.3850178501528332 | 65.21% | 0.025015634771732333 | 0 |
| 9 | 24805.375 | 142344.191 | 408682.495 | 1.3582786011227723 | 65.88% | 0.025025025025025023 | 0 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 2297 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 10 | SQLTransientConnectionException | 2440 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 11 | SQLTransientConnectionException | 2521 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 12 | SQLTransientConnectionException | 2574 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 13 | SQLTransientConnectionException | 2420 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 14 | SQLTransientConnectionException | 2586 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 15 | SQLTransientConnectionException | 2550 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 1 | SQLTransientConnectionException | 2366 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=94) |
| 2 | SQLTransientConnectionException | 2410 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 3 | SQLTransientConnectionException | 2476 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 4 | SQLTransientConnectionException | 2388 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 5 | SQLTransientConnectionException | 2711 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 6 | SQLTransientConnectionException | 2331 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 7 | SQLTransientConnectionException | 2455 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 8 | SQLTransientConnectionException | 2427 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 9 | SQLTransientConnectionException | 2452 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T17:39:06Z → 2026-07-15T17:54:06Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 313 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 32585 / 48747 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 3055378627 | Cumulative since stats reset |
| Transactions rolled back | 966 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 2 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5806 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 416975 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T17:39:06Z → 2026-07-15T17:54:06Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 1077.3 | 1076.5 | 1167.6 | 1231.6 | 1231.6 | 1599.5 | 1599.5 | 1599.8 | 1599.8 | 1599.8 | 357840.2 | 405416.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T17:57:54Z*
