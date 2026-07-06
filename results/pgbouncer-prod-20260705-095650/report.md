# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-05T09:08:41Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260705-095650` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 5.03 RPS (per instance) |
| **Total throughput** | 20.14 RPS (all instances) |
| **p50 latency** | 29266.00 ms |
| **p95 latency** | 37249.00 ms |
| **p99 latency** | 43294.75 ms |
| **p999 latency** | 58703.75 ms |
| **Error rate** | 37.00% (0.37) |
| **Total requests** | 29769 |
| **Failed requests** | 10971 |
| **Total successful** | 18798 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 18.83 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 25921 |
| observed_client_backends_active_max | 38489 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.9% / 3.9% / 6.8% |
| OJP proxy-tier host_cpu (avg / peak) | 12.7% / 129.6% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 13.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.50 MiB / 34.40 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.9% / 3.9% / 6.8% |
| PgBouncer tier RSS (avg / peak, summed) | 34.50 MiB / 34.40 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.7% / 0.0% / 1.9% / 3.9% / 6.8% |
| HAProxy RSS (avg / peak, summed) | 21.90 MiB / 21.90 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.3% / 1.0% / 3.9% / 6.8% / 13.7% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 17.8% / 162.6% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 20.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.40 MiB / 56.30 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.16% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 49 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (37249.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (37.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 30.85 RPS (all instances) |
| **Achieved throughput** | 20.14 RPS (all instances) |
| **Attempted − achieved gap** | 10.72 RPS (34.74%) |
| **Total attempted ops** | 28803 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29523.967 | 37912.575 | 43843.583 | 4.772179863587689 | 40.20% | 0.15026296960470764 | 12 |
| 1 | 29261.823 | 37126.143 | 42237.951 | 5.235153498813308 | 34.36% | 0.17532577713119338 | 13 |
| 2 | 29196.287 | 37257.215 | 44597.247 | 4.9181784223083005 | 38.26% | 0.1503006012024048 | 12 |
| 3 | 29081.599 | 36700.159 | 42500.095 | 5.209527339573768 | 34.58% | 0.1503006012024048 | 12 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 2993 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=4, active=4, idle=0, waiting=240) |
| 1 | SQLTransientConnectionException | 2559 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=240) |
| 2 | SQLTransientConnectionException | 2848 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=4, active=4, idle=0, waiting=239) |
| 3 | SQLTransientConnectionException | 2571 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=236) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-05T09:08:41Z → 2026-07-05T09:23:41Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 25921 / 38489 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 578542236 | Cumulative since stats reset |
| Transactions rolled back | 5470 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7663 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 754620 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-05T09:08:41Z → 2026-07-05T09:23:41Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.9 | 4.9 | 6.1 | 2.9 | 32.4 | 34.1 | 64.7 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 3.4 | 2.9 | 4.9 | 32.4 | 38.2 | 11.5 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 4.9 | 3.4 | 2.9 | 4.9 | 32.4 | 35.3 | 11.5 | 11.5 |
| PostgreSQL | db | 299.2 | 297.1 | 359.9 | 366.1 | 373.1 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 14418.9 | 16246.1 |
| HAProxy | lb | 0.7 | 0.0 | 1.9 | 3.9 | 6.8 | 5.3 | 3.9 | 13.5 | 34.6 | 38.2 | 21.9 | 21.9 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-05T09:26:47Z*
