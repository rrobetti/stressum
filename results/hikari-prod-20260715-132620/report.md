# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T12:37:55Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 3 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260715-132620` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.29 RPS (per instance) |
| **Total throughput** | 20.70 RPS (all instances) |
| **p50 latency** | 21628.00 ms |
| **p95 latency** | 145113.12 ms |
| **p99 latency** | 388562.50 ms |
| **p999 latency** | 432701.25 ms |
| **Error rate** | 57.00% (0.57) |
| **Total requests** | 44580 |
| **Failed requests** | 25229 |
| **Total successful** | 19351 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 300 |
| observed_postgres_backends_max_numbackends | 317 |
| observed_postgres_backends_avg_numbackends | 312.73 |
| observed_postgres_backends_median_numbackends | 312 |
| observed_client_backends_active_median | 34390 |
| observed_client_backends_active_max | 49442 |
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
| p95 latency | < 1500 ms | ❌ FAIL (145113.12 ms) |
| Error rate | < 0.1% | ❌ FAIL (57.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.33 RPS (all instances) |
| **Achieved throughput** | 20.70 RPS (all instances) |
| **Attempted − achieved gap** | 25.63 RPS (55.33%) |
| **Total attempted ops** | 43213 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 21446.655 | 146931.711 | 402653.183 | 1.25453606229686 | 57.59% | 0.02501876407305479 | 0 |
| 10 | 21397.503 | 140771.327 | 394788.863 | 1.3839483382994333 | 53.67% | 0.02501876407305479 | 0 |
| 11 | 20774.911 | 138543.103 | 368050.175 | 1.4053385753674308 | 52.92% | 0.025025025025025023 | 0 |
| 12 | 22003.711 | 159252.479 | 396886.015 | 1.1679069439126595 | 60.89% | 0.025021894157387717 | 0 |
| 13 | 21004.287 | 138543.103 | 373555.199 | 1.3400983523100387 | 55.06% | 0.025021894157387717 | 0 |
| 14 | 22691.839 | 141164.543 | 390856.703 | 1.3518629826974373 | 54.73% | 0.025021894157387717 | 0 |
| 15 | 21315.583 | 144441.343 | 399245.311 | 1.2598836158445874 | 57.46% | 0.025021894157387717 | 0 |
| 1 | 19529.727 | 139198.463 | 376963.071 | 1.3786007790324342 | 53.82% | 0.02501876407305479 | 0 |
| 2 | 22298.623 | 144703.487 | 400293.887 | 1.221382536582653 | 59.10% | 0.025021894157387717 | 0 |
| 3 | 21348.351 | 144572.415 | 367263.743 | 1.3208457262886804 | 55.78% | 0.025021894157387717 | 0 |
| 4 | 22265.855 | 147849.215 | 403963.903 | 1.241701933782314 | 58.37% | 0.02501876407305479 | 0 |
| 5 | 22036.479 | 146931.711 | 387448.831 | 1.263093498865248 | 57.53% | 0.025025025025025023 | 0 |
| 6 | 21446.655 | 156106.751 | 405274.623 | 1.1326130527504636 | 62.08% | 0.025021894157387717 | 0 |
| 7 | 22855.679 | 144310.271 | 382468.095 | 1.3251237691268622 | 55.61% | 0.025021894157387717 | 0 |
| 8 | 22298.623 | 150339.583 | 387973.119 | 1.2427727736506504 | 58.35% | 0.02501876407305479 | 0 |
| 9 | 21331.967 | 138149.887 | 379322.367 | 1.4064065830523196 | 52.51% | 0.025021894157387717 | 0 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 1593 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=71) |
| 10 | SQLTransientConnectionException | 1499 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 11 | SQLTransientConnectionException | 1477 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 12 | SQLTransientConnectionException | 1700 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 13 | SQLTransientConnectionException | 1535 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 14 | SQLTransientConnectionException | 1528 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 15 | SQLTransientConnectionException | 1591 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=67) |
| 1 | SQLTransientConnectionException | 1502 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 2 | SQLTransientConnectionException | 1650 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 3 | SQLTransientConnectionException | 1558 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 4 | SQLTransientConnectionException | 1628 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 5 | SQLTransientConnectionException | 1600 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=68) |
| 6 | SQLTransientConnectionException | 1734 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 7 | SQLTransientConnectionException | 1552 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 8 | SQLTransientConnectionException | 1628 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=68) |
| 9 | SQLTransientConnectionException | 1454 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T12:37:55Z → 2026-07-15T12:52:55Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 312 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 34390 / 49442 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2763844523 | Cumulative since stats reset |
| Transactions rolled back | 965 | Non-zero → contention or application errors |
| Temp file bytes written | -3 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 1 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4844 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 338741 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T12:37:55Z → 2026-07-15T12:52:55Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 1089.7 | 1090.3 | 1155.7 | 1169.6 | 1169.6 | 1599.6 | 1599.6 | 1599.8 | 1599.8 | 1599.8 | 366387.2 | 395643.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T12:56:36Z*
