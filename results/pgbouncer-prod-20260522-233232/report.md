# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-22T22:44:59Z |
| **Duration** | 1800 s |
| **Instances**| 4 |
| **Target RPS**| 5 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260522-233232` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.83 RPS (per instance) |
| **Total throughput** | 3.34 RPS (all instances) |
| **p50 latency** | 29118.50 ms |
| **p95 latency** | 60031.00 ms |
| **p99 latency** | 60031.00 ms |
| **p999 latency** | 66314.00 ms |
| **Error rate** | 79.00% (0.79) |
| **Total requests** | 36623 |
| **Failed requests** | 29092 |
| **Total successful** | 7531 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 25 |
| observed_postgres_backends_avg_numbackends | 21.53 |
| observed_postgres_backends_median_numbackends | 23 |
| observed_client_backends_active_median | 17327 |
| observed_client_backends_active_max | 27640 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 8.6% / 1.0% / 31.2% / 46.0% / 73.9% |
| OJP proxy-tier host_cpu (avg / peak) | 22.4% / 107.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 116.60% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.40 MiB / 34.40 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 5 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 8.6% / 1.0% / 31.2% / 46.0% / 73.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.40 MiB / 34.40 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.9% / 1.9% / 24.2% / 36.5% / 59.0% |
| HAProxy RSS (avg / peak, summed) | 22.30 MiB / 22.30 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 15.3% / 3.9% / 53.5% / 81.7% / 132.9% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 32.8% / 153.5% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 175.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.70 MiB / 56.70 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.13% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 15273 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 150 ms | ❌ FAIL (60031.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (79.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.97 RPS (all instances) |
| **Achieved throughput** | 3.34 RPS (all instances) |
| **Attempted − achieved gap** | 12.63 RPS (79.08%) |
| **Total attempted ops** | 42004 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.56 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29294.591 | 60030.975 | 60030.975 | 0.798664664609621 | 80.33% | 0.15037593984962408 | 4848 |
| 1 | 29097.983 | 60030.975 | 60030.975 | 0.8509924993813786 | 79.05% | 0.10055304172951231 | 3385 |
| 2 | 29114.367 | 60030.975 | 60030.975 | 0.8594181676920852 | 78.83% | 0.15037593984962408 | 3441 |
| 3 | 28966.911 | 60030.975 | 60030.975 | 0.8305935129449307 | 79.54% | 0.10015022533800699 | 3599 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 7356 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=6, active=6, idle=0, waiting=150) |
| 1 | SQLTransientConnectionException | 7239 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=150) |
| 2 | SQLTransientConnectionException | 7217 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=4, active=4, idle=0, waiting=150) |
| 3 | SQLTransientConnectionException | 7280 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=2, active=2, idle=0, waiting=150) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-22T22:44:59Z → 2026-05-22T23:14:59Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 23 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 17327 / 27640 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 563648371 | Cumulative since stats reset |
| Transactions rolled back | 0 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 6970 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 713142 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-22T22:44:59Z → 2026-05-22T23:14:59Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 3.7 | 0.0 | 17.5 | 31.2 | 48.4 | 6.7 | 2.9 | 22.6 | 39.2 | 55.1 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 2.2 | 0.0 | 14.7 | 21.4 | 31.2 | 5.5 | 2.0 | 21.6 | 33.3 | 54.8 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 2.9 | 0.0 | 15.6 | 25.2 | 37.0 | 10.7 | 2.9 | 33.3 | 49.0 | 75.1 | 11.4 | 11.4 |
| PostgreSQL | db | 296.2 | 305.7 | 330.3 | 337.3 | 347.2 | 400.0 | 400.0 | 400.0 | 400.0 | 400.0 | 113676.6 | 121451.0 |
| HAProxy | lb | 6.9 | 1.9 | 24.2 | 36.5 | 59.0 | 10.7 | 5.9 | 31.4 | 45.3 | 80.8 | 22.3 | 22.3 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-22T23:18:03Z*
