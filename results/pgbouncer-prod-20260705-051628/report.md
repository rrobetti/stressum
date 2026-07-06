# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-05T04:28:17Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260705-051628` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.48 RPS (per instance) |
| **Total throughput** | 17.92 RPS (all instances) |
| **p50 latency** | 29393.00 ms |
| **p95 latency** | 38428.75 ms |
| **p99 latency** | 44851.25 ms |
| **p999 latency** | 63791.00 ms |
| **Error rate** | 44.00% (0.44) |
| **Total requests** | 29754 |
| **Failed requests** | 13020 |
| **Total successful** | 16734 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 18.82 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 24619 |
| observed_client_backends_active_max | 35684 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.9% / 3.9% / 7.8% |
| OJP proxy-tier host_cpu (avg / peak) | 14.3% / 71.6% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 13.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 33.90 MiB / 33.90 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.9% / 3.9% / 7.8% |
| PgBouncer tier RSS (avg / peak, summed) | 33.90 MiB / 33.90 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 3.9% / 8.7% |
| HAProxy RSS (avg / peak, summed) | 22.10 MiB / 22.10 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.2% / 1.0% / 4.9% / 5.9% / 16.6% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 18.2% / 76.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 22.40% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.00 MiB / 56.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.15% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 44 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (38428.75 ms) |
| Error rate | < 0.1% | ❌ FAIL (44.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 30.85 RPS (all instances) |
| **Achieved throughput** | 17.92 RPS (all instances) |
| **Attempted − achieved gap** | 12.93 RPS (41.90%) |
| **Total attempted ops** | 28804 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29425.663 | 38174.719 | 44072.959 | 4.615998348678996 | 41.79% | 0.1500750375187594 | 11 |
| 1 | 29458.431 | 38436.863 | 44072.959 | 4.470103570081279 | 44.00% | 0.1502253380070105 | 12 |
| 2 | 29360.127 | 38404.095 | 45613.055 | 4.412315023208884 | 44.74% | 0.15007503751875936 | 11 |
| 3 | 29327.359 | 38699.007 | 45645.823 | 4.425205249415792 | 44.50% | 0.1502253380070105 | 10 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 3099 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=222) |
| 1 | SQLTransientConnectionException | 3277 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=240) |
| 2 | SQLTransientConnectionException | 3331 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=239) |
| 3 | SQLTransientConnectionException | 3313 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=229) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-05T04:28:17Z → 2026-07-05T04:43:17Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 24619 / 35684 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 520387155 | Cumulative since stats reset |
| Transactions rolled back | 5141 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7211 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 731507 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-05T04:28:17Z → 2026-07-05T04:43:17Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 4.9 | 7.6 | 2.9 | 33.3 | 35.5 | 66.7 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 3.5 | 2.0 | 5.0 | 33.2 | 34.3 | 11.2 | 11.2 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.9 | 4.9 | 3.5 | 2.0 | 5.9 | 32.5 | 35.9 | 11.3 | 11.3 |
| PostgreSQL | db | 271.3 | 271.8 | 325.2 | 331.3 | 340.3 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 15541.2 | 17443.4 |
| HAProxy | lb | 0.6 | 0.0 | 1.9 | 3.9 | 8.7 | 4.1 | 3.9 | 6.8 | 10.6 | 36.5 | 22.1 | 22.1 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-05T04:46:20Z*
