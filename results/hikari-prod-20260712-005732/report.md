# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-12T00:09:11Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260712-005732` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.44 RPS (per instance) |
| **Total throughput** | 13.77 RPS (all instances) |
| **p50 latency** | 9081.85 ms |
| **p95 latency** | 39059.50 ms |
| **p99 latency** | 110182.50 ms |
| **p999 latency** | 228917.25 ms |
| **Error rate** | 10.00% (0.10) |
| **Total requests** | 14345 |
| **Failed requests** | 1473 |
| **Total successful** | 12872 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 80 |
| observed_postgres_backends_max_numbackends | 89 |
| observed_postgres_backends_avg_numbackends | 85.98 |
| observed_postgres_backends_median_numbackends | 88 |
| observed_client_backends_active_median | 19688 |
| observed_client_backends_active_max | 28572 |
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
| **Bench JVM GC pause total** | 61 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (39059.50 ms) |
| Error rate | < 0.1% | ❌ FAIL (10.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.41 RPS (all instances) |
| **Achieved throughput** | 13.77 RPS (all instances) |
| **Attempted − achieved gap** | 1.64 RPS (10.64%) |
| **Total attempted ops** | 14403 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 5656.575 | 39419.903 | 109445.119 | 3.3293868388151107 | 13.17% | 0.1502253380070105 | 18 |
| 1 | 10649.599 | 37322.751 | 106889.215 | 3.525103528525959 | 8.11% | 0.1503006012024048 | 12 |
| 2 | 6742.015 | 40763.391 | 113180.671 | 3.361472160101475 | 12.35% | 0.1502253380070105 | 16 |
| 3 | 13279.231 | 38731.775 | 111214.591 | 3.550775555691027 | 7.44% | 0.15022533800701052 | 15 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 472 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=20, active=20, idle=0, waiting=101) |
| 1 | SQLTransientConnectionException | 291 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=20, active=20, idle=0, waiting=87) |
| 2 | SQLTransientConnectionException | 443 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=20, active=20, idle=0, waiting=96) |
| 3 | SQLTransientConnectionException | 267 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=20, active=20, idle=0, waiting=87) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-12T00:09:11Z → 2026-07-12T00:24:11Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 88 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 19688 / 28572 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 380041008 | Cumulative since stats reset |
| Transactions rolled back | 4114 | Non-zero → contention or application errors |
| Temp file bytes written | 62 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -32 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4603 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 347911 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-12T00:09:11Z → 2026-07-12T00:24:11Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 214.2 | 214.5 | 236.1 | 246.2 | 248.4 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 32205.8 | 40019.5 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-12T00:27:12Z*
