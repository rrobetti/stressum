# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-05T13:49:56Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260705-143808` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.84 RPS (per instance) |
| **Total throughput** | 19.36 RPS (all instances) |
| **p50 latency** | 29941.75 ms |
| **p95 latency** | 38854.75 ms |
| **p99 latency** | 44523.50 ms |
| **p999 latency** | 61259.75 ms |
| **Error rate** | 59.00% (0.59) |
| **Total requests** | 44679 |
| **Failed requests** | 26581 |
| **Total successful** | 18098 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 18.66 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 26400 |
| observed_client_backends_active_max | 38412 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.9% / 3.9% / 5.9% |
| OJP proxy-tier host_cpu (avg / peak) | 11.6% / 92.2% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 13.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.40 MiB / 34.40 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.9% / 3.9% / 5.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.40 MiB / 34.40 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 3.9% / 6.8% |
| HAProxy RSS (avg / peak, summed) | 21.70 MiB / 21.70 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.3% / 1.0% / 4.9% / 6.8% / 12.7% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 16.0% / 96.0% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 20.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.10 MiB / 56.10 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.18% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 54 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (38854.75 ms) |
| Error rate | < 0.1% | ❌ FAIL (59.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.21 RPS (all instances) |
| **Achieved throughput** | 19.36 RPS (all instances) |
| **Attempted − achieved gap** | 26.85 RPS (58.11%) |
| **Total attempted ops** | 43204 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29949.951 | 38862.847 | 43876.351 | 4.642745990136972 | 61.13% | 0.1502253380070105 | 10 |
| 1 | 29949.951 | 38895.615 | 43679.743 | 4.79781991170129 | 59.82% | 0.2001000500250125 | 14 |
| 2 | 29933.567 | 38928.383 | 45088.767 | 4.94220370306992 | 58.64% | 0.1502253380070105 | 15 |
| 3 | 29933.567 | 38731.775 | 45449.215 | 4.973224799386529 | 58.38% | 0.20020020020020018 | 15 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 6827 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=360) |
| 1 | SQLTransientConnectionException | 6679 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=360) |
| 2 | SQLTransientConnectionException | 6552 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=16, active=16, idle=0, waiting=360) |
| 3 | SQLTransientConnectionException | 6523 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=14, active=14, idle=0, waiting=360) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-05T13:49:56Z → 2026-07-05T14:04:56Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 26400 / 38412 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 579392086 | Cumulative since stats reset |
| Transactions rolled back | 5180 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 8509 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 800666 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-05T13:49:56Z → 2026-07-05T14:04:56Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.9 | 3.9 | 5.1 | 2.9 | 32.4 | 34.5 | 87.2 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.9 | 4.9 | 3.0 | 2.0 | 3.9 | 32.2 | 34.3 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 4.9 | 3.8 | 2.9 | 7.8 | 33.3 | 37.2 | 11.5 | 11.5 |
| PostgreSQL | db | 299.6 | 300.7 | 355.3 | 364.3 | 369.5 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 14516.1 | 16220.1 |
| HAProxy | lb | 0.6 | 0.0 | 1.9 | 3.9 | 6.8 | 4.5 | 3.9 | 6.8 | 34.0 | 36.1 | 21.7 | 21.7 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-05T14:08:00Z*
