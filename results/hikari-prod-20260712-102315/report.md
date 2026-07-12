# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-12T09:34:56Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260712-102315` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.92 RPS (per instance) |
| **Total throughput** | 15.70 RPS (all instances) |
| **p50 latency** | 29429.75 ms |
| **p95 latency** | 82329.50 ms |
| **p99 latency** | 169607.25 ms |
| **p999 latency** | 197198.00 ms |
| **Error rate** | 67.00% (0.67) |
| **Total requests** | 44650 |
| **Failed requests** | 29972 |
| **Total successful** | 14678 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 80 |
| observed_postgres_backends_max_numbackends | 89 |
| observed_postgres_backends_avg_numbackends | 87.49 |
| observed_postgres_backends_median_numbackends | 88 |
| observed_client_backends_active_median | 23687 |
| observed_client_backends_active_max | 33666 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | hikari-prod |
| Configured replicas | 4 |
| Configured client pool size (per replica) | 20 |
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
| **bench_jvm_cpu (median)** | 0.20% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 78 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (82329.50 ms) |
| Error rate | < 0.1% | ❌ FAIL (67.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.21 RPS (all instances) |
| **Achieved throughput** | 15.70 RPS (all instances) |
| **Attempted − achieved gap** | 30.51 RPS (66.03%) |
| **Total attempted ops** | 43202 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29425.663 | 80936.959 | 117702.655 | 4.210663663480594 | 64.73% | 0.20020020020020018 | 19 |
| 1 | 29442.047 | 82771.967 | 189005.823 | 3.828852435171539 | 67.93% | 0.20020020020020018 | 20 |
| 2 | 29474.815 | 83165.183 | 187301.887 | 3.74221797269967 | 68.66% | 0.2001000500250125 | 19 |
| 3 | 29376.511 | 82444.287 | 184418.303 | 3.916548218355585 | 67.19% | 0.20020020020020018 | 20 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 7226 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=20, active=20, idle=0, waiting=360) |
| 1 | SQLTransientConnectionException | 7582 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=20, active=20, idle=0, waiting=360) |
| 2 | SQLTransientConnectionException | 7664 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=20, active=20, idle=0, waiting=360) |
| 3 | SQLTransientConnectionException | 7500 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=20, active=20, idle=0, waiting=360) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-12T09:34:56Z → 2026-07-12T09:49:56Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 88 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 23687 / 33666 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 599412292 | Cumulative since stats reset |
| Transactions rolled back | 4557 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 6864 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 695485 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-12T09:34:56Z → 2026-07-12T09:49:56Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 271.8 | 271.3 | 298.5 | 306.6 | 315.9 | 400.0 | 400.0 | 400.0 | 400.0 | 400.0 | 35251.4 | 42854.6 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-12T09:52:58Z*
