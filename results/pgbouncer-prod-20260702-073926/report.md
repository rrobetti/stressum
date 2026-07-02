# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-02T06:51:14Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260702-073926` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.69 RPS (per instance) |
| **Total throughput** | 14.75 RPS (all instances) |
| **p50 latency** | 29507.50 ms |
| **p95 latency** | 38961.00 ms |
| **p99 latency** | 45400.00 ms |
| **p999 latency** | 63963.25 ms |
| **Error rate** | 48.00% (0.48) |
| **Total requests** | 29786 |
| **Failed requests** | 14233 |
| **Total successful** | 15553 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 18.85 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 22885 |
| observed_client_backends_active_max | 33634 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.5% / 0.0% / 2.0% / 2.9% / 5.9% |
| OJP proxy-tier host_cpu (avg / peak) | 10.8% / 66.7% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 10.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.30 MiB / 34.30 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.5% / 0.0% / 2.0% / 2.9% / 5.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.30 MiB / 34.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.5% / 0.0% / 1.9% / 3.9% / 6.8% |
| HAProxy RSS (avg / peak, summed) | 21.70 MiB / 21.80 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.0% / 1.0% / 3.9% / 5.9% / 9.7% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 15.1% / 70.6% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 17.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.00 MiB / 56.10 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.15% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 35 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (38961.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (48.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 27.32 RPS (all instances) |
| **Achieved throughput** | 14.75 RPS (all instances) |
| **Attempted − achieved gap** | 12.57 RPS (46.01%) |
| **Total attempted ops** | 28804 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29458.431 | 38371.327 | 45350.911 | 3.795231884497558 | 46.21% | 0.1503006012024048 | 10 |
| 1 | 29261.823 | 38502.399 | 44302.335 | 3.9667945645909795 | 43.77% | 0.1502253380070105 | 10 |
| 2 | 29540.351 | 39190.527 | 46628.863 | 3.6246170645151503 | 48.67% | 0.1502253380070105 | 8 |
| 3 | 29769.727 | 39780.351 | 45318.143 | 3.3625929581224194 | 52.48% | 0.15015015015015015 | 7 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 3440 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=240) |
| 1 | SQLTransientConnectionException | 3258 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=234) |
| 2 | SQLTransientConnectionException | 3626 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=240) |
| 3 | SQLTransientConnectionException | 3909 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=13, active=13, idle=0, waiting=235) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-02T06:51:14Z → 2026-07-02T07:06:14Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 22885 / 33634 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 490694219 | Cumulative since stats reset |
| Transactions rolled back | 4857 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 6890 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 700505 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-02T06:51:14Z → 2026-07-02T07:06:14Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 2.7 | 2.0 | 3.9 | 31.4 | 34.3 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 5.6 | 2.9 | 33.3 | 34.3 | 63.7 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 2.6 | 2.0 | 3.9 | 6.8 | 35.5 | 11.4 | 11.4 |
| PostgreSQL | db | 274.9 | 275.5 | 329.5 | 341.8 | 352.6 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 15556.3 | 17228.3 |
| HAProxy | lb | 0.5 | 0.0 | 1.9 | 3.9 | 6.8 | 4.4 | 3.9 | 5.9 | 33.2 | 36.1 | 21.7 | 21.8 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-02T07:09:20Z*
