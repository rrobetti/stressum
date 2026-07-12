# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-11T22:35:03Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260711-232319` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.37 RPS (per instance) |
| **Total throughput** | 13.46 RPS (all instances) |
| **p50 latency** | 13240.30 ms |
| **p95 latency** | 45203.25 ms |
| **p99 latency** | 123289.50 ms |
| **p999 latency** | 235700.25 ms |
| **Error rate** | 12.00% (0.12) |
| **Total requests** | 14355 |
| **Failed requests** | 1766 |
| **Total successful** | 12589 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 80 |
| observed_postgres_backends_max_numbackends | 89 |
| observed_postgres_backends_avg_numbackends | 86.57 |
| observed_postgres_backends_median_numbackends | 88 |
| observed_client_backends_active_median | 19309 |
| observed_client_backends_active_max | 28028 |
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
| **bench_jvm_cpu (median)** | 0.18% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 56 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (45203.25 ms) |
| Error rate | < 0.1% | ❌ FAIL (12.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.41 RPS (all instances) |
| **Achieved throughput** | 13.46 RPS (all instances) |
| **Attempted − achieved gap** | 1.94 RPS (12.60%) |
| **Total attempted ops** | 14403 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 11010.047 | 35323.903 | 107020.287 | 3.50264757376148 | 8.72% | 0.15022533800701052 | 14 |
| 1 | 14082.047 | 46727.167 | 129761.279 | 3.3004994598988247 | 14.02% | 0.20020020020020018 | 13 |
| 2 | 12730.367 | 47546.367 | 125173.759 | 3.3507770530060204 | 12.71% | 0.1502253380070105 | 16 |
| 3 | 15138.815 | 51216.383 | 131203.071 | 3.310135646043292 | 13.76% | 0.20030045067601399 | 13 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 313 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=20, active=20, idle=0, waiting=74) |
| 1 | SQLTransientConnectionException | 503 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=20, active=20, idle=0, waiting=66) |
| 2 | SQLTransientConnectionException | 456 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=20, active=20, idle=0, waiting=80) |
| 3 | SQLTransientConnectionException | 494 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=20, active=20, idle=0, waiting=61) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-11T22:35:03Z → 2026-07-11T22:50:03Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 88 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 19309 / 28028 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 378745845 | Cumulative since stats reset |
| Transactions rolled back | 4037 | Non-zero → contention or application errors |
| Temp file bytes written | 52 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -36 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4689 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 350305 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-11T22:35:03Z → 2026-07-11T22:50:03Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 214.0 | 214.5 | 242.0 | 251.6 | 251.6 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 33190.9 | 39810.3 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-11T22:53:05Z*
