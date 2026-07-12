# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-12T11:41:18Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260712-122924` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.56 RPS (per instance) |
| **Total throughput** | 18.22 RPS (all instances) |
| **p50 latency** | 29982.75 ms |
| **p95 latency** | 39084.00 ms |
| **p99 latency** | 45006.75 ms |
| **p999 latency** | 61563.00 ms |
| **Error rate** | 62.00% (0.62) |
| **Total requests** | 44672 |
| **Failed requests** | 27640 |
| **Total successful** | 17032 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 18.93 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 27507 |
| observed_client_backends_active_max | 39470 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 3.9% / 4.9% |
| OJP proxy-tier host_cpu (avg / peak) | 9.1% / 41.0% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 10.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.30 MiB / 34.30 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 3.9% / 4.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.30 MiB / 34.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 2.9% / 5.8% |
| HAProxy RSS (avg / peak, summed) | 22.00 MiB / 22.00 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.2% / 1.0% / 3.9% / 5.8% / 10.7% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 19.5% / 73.0% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 16.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.30 MiB / 56.30 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.15% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 44 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (39084.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (62.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.22 RPS (all instances) |
| **Achieved throughput** | 18.22 RPS (all instances) |
| **Attempted − achieved gap** | 28.00 RPS (60.58%) |
| **Total attempted ops** | 43202 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29999.103 | 39321.599 | 44924.927 | 4.2662690947359865 | 64.28% | 0.1502253380070105 | 12 |
| 1 | 30015.487 | 39157.759 | 46104.575 | 4.469480475033368 | 62.57% | 0.1502253380070105 | 9 |
| 2 | 29949.951 | 38699.007 | 43810.815 | 4.711194675547884 | 60.56% | 0.15015015015015015 | 10 |
| 3 | 29966.335 | 39157.759 | 45187.071 | 4.774319961882532 | 60.08% | 0.1502253380070105 | 13 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 7177 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=360) |
| 1 | SQLTransientConnectionException | 6986 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=360) |
| 2 | SQLTransientConnectionException | 6765 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=360) |
| 3 | SQLTransientConnectionException | 6712 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=360) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-12T11:41:18Z → 2026-07-12T11:56:18Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 27507 / 39470 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 540444623 | Cumulative since stats reset |
| Transactions rolled back | 5128 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7903 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 721614 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-12T11:41:18Z → 2026-07-12T11:56:18Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 4.9 | 3.1 | 2.9 | 4.8 | 32.4 | 34.3 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 3.1 | 2.0 | 3.9 | 32.4 | 33.3 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 3.1 | 2.9 | 3.9 | 32.4 | 34.3 | 11.4 | 11.4 |
| PostgreSQL | db | 296.5 | 296.1 | 352.0 | 367.1 | 375.6 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 14621.1 | 16305.4 |
| HAProxy | lb | 0.6 | 0.0 | 1.9 | 2.9 | 5.8 | 10.7 | 4.8 | 34.1 | 35.9 | 39.8 | 22.0 | 22.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-12T11:59:29Z*
