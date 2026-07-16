# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T20:57:55Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260715-214604` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.30 RPS (per instance) |
| **Total throughput** | 20.87 RPS (all instances) |
| **p50 latency** | 24910.94 ms |
| **p95 latency** | 151600.62 ms |
| **p99 latency** | 396788.12 ms |
| **p999 latency** | 441336.88 ms |
| **Error rate** | 67.00% (0.67) |
| **Total requests** | 59413 |
| **Failed requests** | 39902 |
| **Total successful** | 19511 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 300 |
| observed_postgres_backends_max_numbackends | 316 |
| observed_postgres_backends_avg_numbackends | 312.73 |
| observed_postgres_backends_median_numbackends | 313 |
| observed_client_backends_active_median | 33049 |
| observed_client_backends_active_max | 48768 |
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
| p95 latency | < 1500 ms | ❌ FAIL (151600.62 ms) |
| Error rate | < 0.1% | ❌ FAIL (67.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 61.68 RPS (all instances) |
| **Achieved throughput** | 20.87 RPS (all instances) |
| **Attempted − achieved gap** | 40.82 RPS (66.17%) |
| **Total attempted ops** | 57614 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 25264.127 | 153223.167 | 395313.151 | 1.2909021876888358 | 67.53% | 0.025021894157387717 | 0 |
| 10 | 25657.343 | 163053.567 | 411566.079 | 1.1572130630317485 | 70.72% | 0.025025025025025023 | 0 |
| 11 | 25116.671 | 154664.959 | 413401.087 | 1.2171044891690534 | 69.36% | 0.025025025025025023 | 0 |
| 12 | 24936.447 | 162660.351 | 409206.783 | 1.2331471669700516 | 68.78% | 0.025025025025025023 | 0 |
| 13 | 23920.639 | 145752.063 | 403177.471 | 1.3058725763550434 | 67.19% | 0.025025025025025023 | 0 |
| 14 | 24428.543 | 143261.695 | 376438.783 | 1.555070234843413 | 60.67% | 0.025025025025025023 | 0 |
| 15 | 25772.031 | 141426.687 | 393478.143 | 1.4096166227810303 | 64.57% | 0.025025025025025023 | 0 |
| 1 | 25329.663 | 149946.367 | 401866.751 | 1.1925044411432215 | 70.03% | 0.025021894157387717 | 0 |
| 2 | 25198.591 | 159252.479 | 362020.863 | 1.3540005582845904 | 65.92% | 0.025025025025025023 | 0 |
| 3 | 24330.239 | 141164.543 | 386400.255 | 1.4427714902364264 | 63.74% | 0.025025025025025023 | 0 |
| 4 | 24231.935 | 143785.983 | 406847.487 | 1.32940323377604 | 66.60% | 0.025021894157387717 | 0 |
| 5 | 23314.431 | 151912.447 | 402653.183 | 1.3294018119650441 | 66.60% | 0.025025025025025023 | 0 |
| 6 | 26017.791 | 161742.847 | 401604.607 | 1.072720388960071 | 73.06% | 0.025025025025025023 | 0 |
| 7 | 25608.191 | 152043.519 | 421265.407 | 1.2438422855040503 | 68.69% | 0.025025025025025023 | 0 |
| 8 | 24870.911 | 151126.015 | 383254.527 | 1.3850178501528332 | 65.19% | 0.025021894157387717 | 0 |
| 9 | 24575.999 | 150601.727 | 380108.799 | 1.348653004736863 | 65.91% | 0.025025025025025023 | 0 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 2510 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 10 | SQLTransientConnectionException | 2613 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 11 | SQLTransientConnectionException | 2576 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 12 | SQLTransientConnectionException | 2540 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=92) |
| 13 | SQLTransientConnectionException | 2500 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 14 | SQLTransientConnectionException | 2243 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 15 | SQLTransientConnectionException | 2402 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 1 | SQLTransientConnectionException | 2605 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 2 | SQLTransientConnectionException | 2449 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 3 | SQLTransientConnectionException | 2371 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 4 | SQLTransientConnectionException | 2479 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 5 | SQLTransientConnectionException | 2479 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 6 | SQLTransientConnectionException | 2720 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 7 | SQLTransientConnectionException | 2552 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 8 | SQLTransientConnectionException | 2425 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 9 | SQLTransientConnectionException | 2438 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=19, active=19, idle=0, waiting=112) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T20:57:55Z → 2026-07-15T21:12:55Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 313 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 33049 / 48768 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2855102376 | Cumulative since stats reset |
| Transactions rolled back | 936 | Non-zero → contention or application errors |
| Temp file bytes written | -2 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5865 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 420861 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T20:57:55Z → 2026-07-15T21:12:55Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 1086.8 | 1090.7 | 1177.1 | 1198.8 | 1198.8 | 1599.5 | 1599.5 | 1599.7 | 1599.7 | 1599.7 | 365504.2 | 408165.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T21:16:42Z*
