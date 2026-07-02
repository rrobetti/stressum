# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-02T13:06:24Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260702-135435` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.12 RPS (per instance) |
| **Total throughput** | 16.46 RPS (all instances) |
| **p50 latency** | 29917.25 ms |
| **p95 latency** | 39510.00 ms |
| **p99 latency** | 45310.00 ms |
| **p999 latency** | 63275.25 ms |
| **Error rate** | 61.00% (0.61) |
| **Total requests** | 44674 |
| **Failed requests** | 27305 |
| **Total successful** | 17369 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 18.77 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 25404 |
| observed_client_backends_active_max | 37012 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | pgbouncer-prod |
| Configured replicas | 4 |
| Configured client pool size (per replica) | 20 |
| OJP servers | N/A |
| Real DB connections per OJP server | N/A |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 3.9% / 5.9% |
| OJP proxy-tier host_cpu (avg / peak) | 12.1% / 90.6% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 14.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.20 MiB / 34.20 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 3.9% / 5.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.20 MiB / 34.20 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 3.9% / 4.9% |
| HAProxy RSS (avg / peak, summed) | 21.80 MiB / 21.80 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.2% / 1.0% / 3.9% / 5.9% / 10.7% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 16.4% / 95.5% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 19.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.00 MiB / 56.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.15% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 40 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (39510.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (61.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 40.95 RPS (all instances) |
| **Achieved throughput** | 16.46 RPS (all instances) |
| **Attempted − achieved gap** | 24.49 RPS (59.80%) |
| **Total attempted ops** | 43203 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29868.031 | 39124.991 | 44367.871 | 4.162997661631323 | 60.67% | 0.15037593984962408 | 9 |
| 1 | 29917.183 | 39649.279 | 44826.623 | 4.166793048014801 | 60.65% | 0.15037593984962408 | 11 |
| 2 | 29917.183 | 39485.439 | 45744.127 | 4.196172734071463 | 60.36% | 0.15037593984962408 | 11 |
| 3 | 29966.335 | 39780.351 | 46301.183 | 3.9373959727472294 | 62.80% | 0.1503006012024048 | 9 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 6776 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=360) |
| 1 | SQLTransientConnectionException | 6775 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=360) |
| 2 | SQLTransientConnectionException | 6740 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=359) |
| 3 | SQLTransientConnectionException | 7014 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=360) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-02T13:06:24Z → 2026-07-02T13:21:24Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 25404 / 37012 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 520359673 | Cumulative since stats reset |
| Transactions rolled back | 5180 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7863 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 735598 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-02T13:06:24Z → 2026-07-02T13:21:24Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 2.9 | 2.0 | 3.9 | 31.4 | 34.3 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 5.9 | 6.2 | 2.9 | 33.3 | 34.6 | 83.3 | 11.3 | 11.3 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 4.9 | 3.3 | 2.9 | 4.8 | 33.2 | 85.7 | 11.4 | 11.4 |
| PostgreSQL | db | 273.1 | 272.7 | 329.3 | 342.7 | 347.2 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 15633.8 | 17238.4 |
| HAProxy | lb | 0.6 | 0.0 | 1.9 | 3.9 | 4.9 | 4.4 | 3.9 | 5.9 | 33.5 | 36.7 | 21.8 | 21.8 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-02T13:24:30Z*
