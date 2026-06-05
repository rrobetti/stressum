# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-31T09:43:57Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260531-103129` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.05 RPS (per instance) |
| **Total throughput** | 2.10 RPS (all instances) |
| **p50 latency** | 29220.85 ms |
| **p95 latency** | 60031.00 ms |
| **p99 latency** | 60031.00 ms |
| **p999 latency** | 65011.50 ms |
| **Error rate** | 87.00% (0.87) |
| **Total requests** | 22336 |
| **Failed requests** | 19485 |
| **Total successful** | 2851 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 25 |
| observed_postgres_backends_avg_numbackends | 21.61 |
| observed_postgres_backends_median_numbackends | 23 |
| observed_client_backends_active_median | 14550 |
| observed_client_backends_active_max | 20533 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | pgbouncer-prod |
| Configured replicas | 2 |
| Configured client pool size (per replica) | 20 |
| OJP servers | N/A |
| Real DB connections per OJP server | N/A |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.1% / 0.0% / 1.0% / 2.0% / 3.9% |
| OJP proxy-tier host_cpu (avg / peak) | 14.6% / 84.3% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 7.80% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.50 MiB / 34.50 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 5 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.1% / 0.0% / 1.0% / 2.0% / 3.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.50 MiB / 34.50 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.1% / 0.0% / 1.0% / 1.9% / 1.9% |
| HAProxy RSS (avg / peak, summed) | 22.30 MiB / 22.30 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.3% / 0.0% / 1.0% / 2.9% / 4.9% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 18.8% / 88.2% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 9.70% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.80 MiB / 56.80 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.18% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 15 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (60031.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (87.00%) |

## Open-Loop Sanity (2/2 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.94 RPS (all instances) |
| **Achieved throughput** | 2.10 RPS (all instances) |
| **Attempted − achieved gap** | 13.84 RPS (86.80%) |
| **Total attempted ops** | 28802 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.63 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29245.439 | 60030.975 | 60030.975 | 1.0324616572227299 | 87.47% | 0.2001000500250125 | 7 |
| 1 | 29196.287 | 60030.975 | 60030.975 | 1.0715764350600328 | 87.00% | 0.15007503751875936 | 8 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 9766 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=4, active=4, idle=0, waiting=360) |
| 1 | SQLTransientConnectionException | 9719 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=360) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-31T09:43:57Z → 2026-05-31T09:58:57Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 23 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 14550 / 20533 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 420336448 | Cumulative since stats reset |
| Transactions rolled back | 1082 | Non-zero → contention or application errors |
| Temp file bytes written | 2 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 3571 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 365127 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-31T09:43:57Z → 2026-05-31T09:58:57Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.0 | 0.0 | 0.0 | 1.0 | 2.9 | 3.1 | 2.0 | 3.9 | 33.3 | 34.6 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.1 | 0.0 | 0.0 | 1.0 | 2.9 | 2.8 | 2.0 | 3.0 | 31.5 | 34.1 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.0 | 0.0 | 0.0 | 1.0 | 2.0 | 9.0 | 2.9 | 47.1 | 48.0 | 49.5 | 11.5 | 11.5 |
| PostgreSQL | db | 199.6 | 202.7 | 218.3 | 223.6 | 235.3 | 400.0 | 400.0 | 400.0 | 400.0 | 400.0 | 44507.3 | 50732.3 |
| HAProxy | lb | 0.1 | 0.0 | 1.0 | 1.9 | 1.9 | 4.3 | 2.9 | 4.9 | 33.8 | 34.8 | 22.3 | 22.3 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-31T10:01:54Z*
