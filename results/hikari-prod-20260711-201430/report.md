# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-11T19:26:13Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260711-201430` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.45 RPS (per instance) |
| **Total throughput** | 13.79 RPS (all instances) |
| **p50 latency** | 11670.02 ms |
| **p95 latency** | 39379.00 ms |
| **p99 latency** | 110035.00 ms |
| **p999 latency** | 231932.00 ms |
| **Error rate** | 10.00% (0.10) |
| **Total requests** | 14348 |
| **Failed requests** | 1459 |
| **Total successful** | 12889 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 80 |
| observed_postgres_backends_max_numbackends | 90 |
| observed_postgres_backends_avg_numbackends | 86.55 |
| observed_postgres_backends_median_numbackends | 88 |
| observed_client_backends_active_median | 19592 |
| observed_client_backends_active_max | 28350 |
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
| **bench_jvm_cpu (median)** | 0.15% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 67 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (39379.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (10.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.41 RPS (all instances) |
| **Achieved throughput** | 13.79 RPS (all instances) |
| **Attempted − achieved gap** | 1.62 RPS (10.52%) |
| **Total attempted ops** | 14403 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 2246.655 | 35520.511 | 103481.343 | 3.5571964244079717 | 7.30% | 0.1502253380070105 | 19 |
| 1 | 14311.423 | 39419.903 | 112590.847 | 3.4021099284712 | 11.32% | 0.15015015015015015 | 16 |
| 2 | 16261.119 | 45121.535 | 113573.887 | 3.3197612424292013 | 13.44% | 0.15015015015015015 | 15 |
| 3 | 13860.863 | 37453.823 | 110493.695 | 3.505852356343475 | 8.61% | 0.1500750375187594 | 17 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 262 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=20, active=20, idle=0, waiting=86) |
| 1 | SQLTransientConnectionException | 406 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=20, active=20, idle=0, waiting=81) |
| 2 | SQLTransientConnectionException | 482 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=20, active=20, idle=0, waiting=90) |
| 3 | SQLTransientConnectionException | 309 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=20, active=20, idle=0, waiting=91) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-11T19:26:13Z → 2026-07-11T19:41:13Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 88 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 19592 / 28350 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 383064354 | Cumulative since stats reset |
| Transactions rolled back | 4120 | Non-zero → contention or application errors |
| Temp file bytes written | 53 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -33 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4724 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 353396 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-11T19:26:13Z → 2026-07-11T19:41:13Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 212.2 | 212.6 | 238.7 | 250.0 | 250.0 | 400.0 | 400.0 | 400.0 | 400.0 | 400.0 | 32236.0 | 39677.3 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-11T19:44:16Z*
