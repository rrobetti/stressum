# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-12T16:24:33Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260712-171239` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.78 RPS (per instance) |
| **Total throughput** | 19.11 RPS (all instances) |
| **p50 latency** | 29929.50 ms |
| **p95 latency** | 38936.50 ms |
| **p99 latency** | 44974.00 ms |
| **p999 latency** | 60653.50 ms |
| **Error rate** | 60.00% (0.60) |
| **Total requests** | 44687 |
| **Failed requests** | 26820 |
| **Total successful** | 17867 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 18.72 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 27291 |
| observed_client_backends_active_max | 40413 |
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
| OJP proxy-tier host_cpu (avg / peak) | 8.6% / 41.2% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 12.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.40 MiB / 34.30 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.9% / 3.9% / 5.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.40 MiB / 34.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 3.9% / 4.9% |
| HAProxy RSS (avg / peak, summed) | 21.90 MiB / 21.90 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.3% / 1.0% / 4.8% / 6.8% / 8.8% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 19.5% / 111.7% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 17.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.30 MiB / 56.20 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.15% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 48 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (38936.50 ms) |
| Error rate | < 0.1% | ❌ FAIL (60.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.21 RPS (all instances) |
| **Achieved throughput** | 19.11 RPS (all instances) |
| **Attempted − achieved gap** | 27.10 RPS (58.65%) |
| **Total attempted ops** | 43204 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29884.415 | 39157.759 | 45285.375 | 4.741130834034752 | 60.31% | 0.15007503751875936 | 11 |
| 1 | 29949.951 | 39321.599 | 44269.567 | 4.780717984697424 | 59.97% | 0.1502253380070105 | 13 |
| 2 | 29917.183 | 38436.863 | 44761.087 | 5.029903487456791 | 57.91% | 0.15007503751875936 | 13 |
| 3 | 29966.335 | 38830.079 | 45580.287 | 4.558730702157934 | 61.88% | 0.1502253380070105 | 11 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 6736 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=360) |
| 1 | SQLTransientConnectionException | 6698 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=360) |
| 2 | SQLTransientConnectionException | 6470 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=14, active=14, idle=0, waiting=360) |
| 3 | SQLTransientConnectionException | 6916 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=16, active=16, idle=0, waiting=360) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-12T16:24:33Z → 2026-07-12T16:39:33Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 27291 / 40413 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 572007004 | Cumulative since stats reset |
| Transactions rolled back | 5228 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 8380 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 801670 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-12T16:24:33Z → 2026-07-12T16:39:33Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 4.9 | 3.0 | 2.0 | 4.9 | 31.5 | 33.3 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 3.2 | 2.9 | 4.9 | 32.4 | 33.3 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 2.7 | 2.9 | 3.9 | 5.9 | 34.5 | 11.5 | 11.4 |
| PostgreSQL | db | 299.3 | 300.1 | 356.5 | 361.7 | 368.9 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 14554.0 | 16652.8 |
| HAProxy | lb | 0.6 | 0.0 | 1.9 | 3.9 | 4.9 | 11.2 | 4.8 | 34.8 | 36.3 | 102.9 | 21.9 | 21.9 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-12T16:42:46Z*
