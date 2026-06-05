# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-30T23:08:47Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260530-235628` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.04 RPS (per instance) |
| **Total throughput** | 2.09 RPS (all instances) |
| **p50 latency** | 27803.65 ms |
| **p95 latency** | 60031.00 ms |
| **p99 latency** | 60031.00 ms |
| **p999 latency** | 60031.00 ms |
| **Error rate** | 81.00% (0.81) |
| **Total requests** | 14937 |
| **Failed requests** | 12110 |
| **Total successful** | 2827 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 75 |
| observed_postgres_backends_max_numbackends | 96 |
| observed_postgres_backends_avg_numbackends | 85.40 |
| observed_postgres_backends_median_numbackends | 85 |
| observed_client_backends_active_median | 13803 |
| observed_client_backends_active_max | 18861 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | hikari-prod |
| Configured replicas | 2 |
| Configured client pool size (per replica) | 38 |
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
| **Bench JVM GC pause total** | 27 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (60031.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (81.00%) |

## Open-Loop Sanity (2/2 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 10.66 RPS (all instances) |
| **Achieved throughput** | 2.09 RPS (all instances) |
| **Attempted − achieved gap** | 8.58 RPS (80.44%) |
| **Total attempted ops** | 19202 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.23 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 27557.887 | 60030.975 | 60030.975 | 1.0088464095916423 | 81.76% | 0.15037593984962408 | 14 |
| 1 | 28049.407 | 60030.975 | 60030.975 | 1.0774820278211763 | 80.38% | 0.15007503751875936 | 13 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 6128 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=38, active=38, idle=0, waiting=225) |
| 1 | SQLTransientConnectionException | 5982 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=38, active=38, idle=0, waiting=225) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-30T23:08:47Z → 2026-05-30T23:23:47Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 85 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 13803 / 18861 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 383306154 | Cumulative since stats reset |
| Transactions rolled back | 819 | Non-zero → contention or application errors |
| Temp file bytes written | -8 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -2 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 3322 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 350072 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-30T23:08:47Z → 2026-05-30T23:23:47Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 183.7 | 182.5 | 198.6 | 203.3 | 203.3 | 400.0 | 400.0 | 400.0 | 400.0 | 400.0 | 100325.2 | 116256.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-30T23:26:43Z*
