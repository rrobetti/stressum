# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-05T16:58:06Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260705-174614` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.95 RPS (per instance) |
| **Total throughput** | 19.80 RPS (all instances) |
| **p50 latency** | 29954.00 ms |
| **p95 latency** | 38289.50 ms |
| **p99 latency** | 43933.75 ms |
| **p999 latency** | 60637.25 ms |
| **Error rate** | 59.00% (0.59) |
| **Total requests** | 44681 |
| **Failed requests** | 26192 |
| **Total successful** | 18489 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 18.70 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 27712 |
| observed_client_backends_active_max | 39855 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.7% / 0.0% / 2.9% / 3.9% / 6.9% |
| OJP proxy-tier host_cpu (avg / peak) | 16.7% / 86.3% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 14.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.40 MiB / 34.40 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.7% / 0.0% / 2.9% / 3.9% / 6.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.40 MiB / 34.40 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.7% / 0.0% / 1.9% / 3.9% / 5.8% |
| HAProxy RSS (avg / peak, summed) | 21.90 MiB / 21.90 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.3% / 1.0% / 3.9% / 5.9% / 12.7% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 20.8% / 89.2% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 20.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.30 MiB / 56.30 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.18% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 48 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (38289.50 ms) |
| Error rate | < 0.1% | ❌ FAIL (59.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.27 RPS (all instances) |
| **Achieved throughput** | 19.80 RPS (all instances) |
| **Attempted − achieved gap** | 26.47 RPS (57.21%) |
| **Total attempted ops** | 43204 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29949.951 | 38338.559 | 45219.839 | 5.022416920496937 | 57.96% | 0.20030045067601399 | 12 |
| 1 | 29933.567 | 38273.023 | 43286.527 | 4.987993256515881 | 58.32% | 0.15030060120240482 | 11 |
| 2 | 29949.951 | 38109.183 | 43188.223 | 5.1826950870919735 | 56.65% | 0.17532577713119338 | 12 |
| 3 | 29982.719 | 38436.863 | 44040.191 | 4.6054881978333295 | 61.55% | 0.20020020020020018 | 13 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 6473 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=360) |
| 1 | SQLTransientConnectionException | 6517 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=14, active=14, idle=0, waiting=359) |
| 2 | SQLTransientConnectionException | 6326 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=360) |
| 3 | SQLTransientConnectionException | 6876 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=360) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-05T16:58:06Z → 2026-07-05T17:13:06Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 27712 / 39855 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 595921969 | Cumulative since stats reset |
| Transactions rolled back | 5291 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 8440 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 765746 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-05T16:58:06Z → 2026-07-05T17:13:06Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.9 | 4.9 | 10.1 | 3.0 | 33.3 | 36.9 | 71.6 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 5.9 | 3.8 | 2.9 | 6.8 | 34.3 | 44.3 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 3.1 | 2.0 | 4.0 | 32.4 | 33.3 | 11.5 | 11.5 |
| PostgreSQL | db | 305.0 | 304.5 | 357.3 | 368.5 | 377.6 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 14636.5 | 16756.0 |
| HAProxy | lb | 0.7 | 0.0 | 1.9 | 3.9 | 5.8 | 4.2 | 3.9 | 5.8 | 29.3 | 35.9 | 21.9 | 21.9 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-05T17:16:11Z*
