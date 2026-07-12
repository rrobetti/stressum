# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-12T10:06:37Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260712-105444` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.75 RPS (per instance) |
| **Total throughput** | 19.00 RPS (all instances) |
| **p50 latency** | 29941.75 ms |
| **p95 latency** | 38715.25 ms |
| **p99 latency** | 45334.50 ms |
| **p999 latency** | 60817.50 ms |
| **Error rate** | 60.00% (0.60) |
| **Total requests** | 44667 |
| **Failed requests** | 26908 |
| **Total successful** | 17759 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 18.61 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 27642 |
| observed_client_backends_active_max | 39866 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 3.9% / 6.9% |
| OJP proxy-tier host_cpu (avg / peak) | 9.8% / 74.9% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 12.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.30 MiB / 34.30 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 3.9% / 6.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.30 MiB / 34.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 2.9% / 7.8% |
| HAProxy RSS (avg / peak, summed) | 22.00 MiB / 21.90 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.2% / 1.0% / 3.9% / 6.8% / 9.8% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 20.5% / 102.3% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 20.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.30 MiB / 56.20 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.15% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 47 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (38715.25 ms) |
| Error rate | < 0.1% | ❌ FAIL (60.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.23 RPS (all instances) |
| **Achieved throughput** | 19.00 RPS (all instances) |
| **Attempted − achieved gap** | 27.23 RPS (58.90%) |
| **Total attempted ops** | 43204 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29966.335 | 38961.151 | 45514.751 | 4.587131433240607 | 61.57% | 0.1502253380070105 | 10 |
| 1 | 29933.567 | 38600.703 | 45645.823 | 4.882494907827397 | 59.14% | 0.1502253380070105 | 14 |
| 2 | 29917.183 | 38666.239 | 44662.783 | 4.915471221071073 | 58.85% | 0.1502253380070105 | 11 |
| 3 | 29949.951 | 38633.471 | 45514.751 | 4.6161870723199065 | 61.41% | 0.1502253380070105 | 12 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 6872 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=357) |
| 1 | SQLTransientConnectionException | 6605 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=360) |
| 2 | SQLTransientConnectionException | 6573 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=360) |
| 3 | SQLTransientConnectionException | 6858 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=360) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-12T10:06:37Z → 2026-07-12T10:21:37Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 27642 / 39866 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 557455249 | Cumulative since stats reset |
| Transactions rolled back | 5080 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7765 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 730583 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-12T10:06:37Z → 2026-07-12T10:21:37Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 3.0 | 2.9 | 3.9 | 32.4 | 34.1 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 3.6 | 2.9 | 4.9 | 32.5 | 70.9 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.9 | 4.9 | 3.5 | 2.9 | 4.9 | 32.5 | 63.5 | 11.4 | 11.4 |
| PostgreSQL | db | 295.8 | 296.7 | 351.9 | 361.7 | 371.1 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 14490.0 | 16478.5 |
| HAProxy | lb | 0.6 | 0.0 | 1.9 | 2.9 | 7.8 | 11.1 | 4.8 | 34.8 | 36.7 | 40.6 | 22.0 | 21.9 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-12T10:24:48Z*
