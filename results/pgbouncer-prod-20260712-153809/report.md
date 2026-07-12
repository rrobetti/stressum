# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-12T14:49:59Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260712-153809` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.74 RPS (per instance) |
| **Total throughput** | 18.97 RPS (all instances) |
| **p50 latency** | 29954.00 ms |
| **p95 latency** | 38977.50 ms |
| **p99 latency** | 45129.75 ms |
| **p999 latency** | 60555.25 ms |
| **Error rate** | 60.00% (0.60) |
| **Total requests** | 44682 |
| **Failed requests** | 26962 |
| **Total successful** | 17720 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 18.85 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 28379 |
| observed_client_backends_active_max | 40960 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 3.9% / 8.8% |
| OJP proxy-tier host_cpu (avg / peak) | 9.9% / 70.6% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 11.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.40 MiB / 34.30 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 3.9% / 8.8% |
| PgBouncer tier RSS (avg / peak, summed) | 34.40 MiB / 34.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 2.9% / 8.7% |
| HAProxy RSS (avg / peak, summed) | 22.10 MiB / 22.20 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.3% / 1.0% / 3.9% / 6.8% / 17.5% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 22.1% / 142.0% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 20.40% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.50 MiB / 56.50 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.15% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 55 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (38977.50 ms) |
| Error rate | < 0.1% | ❌ FAIL (60.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.25 RPS (all instances) |
| **Achieved throughput** | 18.97 RPS (all instances) |
| **Attempted − achieved gap** | 27.28 RPS (58.99%) |
| **Total attempted ops** | 43204 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29917.183 | 38666.239 | 43515.903 | 5.17215379136199 | 56.69% | 0.1502253380070105 | 14 |
| 1 | 29949.951 | 39387.135 | 45252.607 | 4.624101820111526 | 61.31% | 0.1502253380070105 | 15 |
| 2 | 29982.719 | 39157.759 | 46170.111 | 4.625403331531831 | 61.32% | 0.1502253380070105 | 12 |
| 3 | 29966.335 | 38699.007 | 45580.287 | 4.547955726080059 | 62.04% | 0.1502253380070105 | 14 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 6331 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=360) |
| 1 | SQLTransientConnectionException | 6849 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=360) |
| 2 | SQLTransientConnectionException | 6852 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=13, active=13, idle=0, waiting=360) |
| 3 | SQLTransientConnectionException | 6930 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=360) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-12T14:49:59Z → 2026-07-12T15:04:59Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 28379 / 40960 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 568124128 | Cumulative since stats reset |
| Transactions rolled back | 5207 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 8004 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 740594 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-12T14:49:59Z → 2026-07-12T15:04:59Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 4.9 | 3.8 | 2.9 | 6.9 | 33.3 | 52.2 | 11.5 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 3.6 | 2.9 | 4.9 | 33.2 | 68.6 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 2.8 | 2.9 | 3.9 | 28.3 | 36.1 | 11.5 | 11.5 |
| PostgreSQL | db | 297.2 | 297.1 | 352.9 | 359.4 | 368.4 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 14624.8 | 16515.4 |
| HAProxy | lb | 0.6 | 0.0 | 1.9 | 2.9 | 8.7 | 12.5 | 4.8 | 35.1 | 60.8 | 99.0 | 22.1 | 22.2 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-12T15:08:11Z*
