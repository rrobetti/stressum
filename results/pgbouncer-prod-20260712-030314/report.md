# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-12T02:15:04Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260712-030314` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.19 RPS (per instance) |
| **Total throughput** | 16.74 RPS (all instances) |
| **p50 latency** | 29495.25 ms |
| **p95 latency** | 38953.00 ms |
| **p99 latency** | 46096.25 ms |
| **p999 latency** | 66281.50 ms |
| **Error rate** | 47.00% (0.47) |
| **Total requests** | 29750 |
| **Failed requests** | 14120 |
| **Total successful** | 15630 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 18.66 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 23784 |
| observed_client_backends_active_max | 35212 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.5% / 0.0% / 2.0% / 2.9% / 5.9% |
| OJP proxy-tier host_cpu (avg / peak) | 9.0% / 40.2% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 10.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.10 MiB / 34.00 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.5% / 0.0% / 2.0% / 2.9% / 5.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.10 MiB / 34.00 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 3.9% / 5.8% |
| HAProxy RSS (avg / peak, summed) | 22.00 MiB / 22.00 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.1% / 1.0% / 3.9% / 5.8% / 11.7% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 27.1% / 133.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 16.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.10 MiB / 56.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.11% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 36 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (38953.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (47.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 30.85 RPS (all instances) |
| **Achieved throughput** | 16.74 RPS (all instances) |
| **Attempted − achieved gap** | 14.11 RPS (45.74%) |
| **Total attempted ops** | 28804 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29605.887 | 39124.991 | 44924.927 | 4.0469145898192895 | 49.29% | 0.1002004008016032 | 9 |
| 1 | 29310.975 | 38404.095 | 44793.855 | 4.351839077140599 | 45.28% | 0.15007503751875936 | 12 |
| 2 | 29474.815 | 38993.919 | 46989.311 | 4.237220126795602 | 46.70% | 0.1002757646372702 | 6 |
| 3 | 29589.503 | 39288.831 | 47677.439 | 4.104373247202221 | 48.58% | 0.1002004008016032 | 9 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 3665 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=235) |
| 1 | SQLTransientConnectionException | 3367 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=9, active=9, idle=0, waiting=236) |
| 2 | SQLTransientConnectionException | 3469 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=238) |
| 3 | SQLTransientConnectionException | 3619 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=240) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-12T02:15:04Z → 2026-07-12T02:30:04Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 23784 / 35212 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 464239568 | Cumulative since stats reset |
| Transactions rolled back | 4930 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 6512 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 665207 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-12T02:15:04Z → 2026-07-12T02:30:04Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 4.9 | 3.0 | 2.0 | 3.9 | 32.4 | 33.3 | 11.3 | 11.3 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 3.0 | 2.0 | 3.9 | 31.5 | 33.3 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 3.3 | 2.9 | 4.0 | 33.2 | 33.5 | 11.4 | 11.3 |
| PostgreSQL | db | 246.4 | 247.6 | 296.8 | 311.1 | 316.5 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 15394.2 | 17054.5 |
| HAProxy | lb | 0.6 | 0.0 | 1.9 | 3.9 | 5.8 | 18.7 | 7.7 | 52.4 | 83.9 | 101.9 | 22.0 | 22.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-12T02:33:13Z*
