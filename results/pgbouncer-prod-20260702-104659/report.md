# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-02T09:58:54Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260702-104659` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.82 RPS (per instance) |
| **Total throughput** | 15.28 RPS (all instances) |
| **p50 latency** | 29954.00 ms |
| **p95 latency** | 39444.50 ms |
| **p99 latency** | 45498.25 ms |
| **p999 latency** | 65478.50 ms |
| **Error rate** | 64.00% (0.64) |
| **Total requests** | 44692 |
| **Failed requests** | 28571 |
| **Total successful** | 16121 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 18.61 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 24745 |
| observed_client_backends_active_max | 35502 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.5% / 0.0% / 2.0% / 3.0% / 5.9% |
| OJP proxy-tier host_cpu (avg / peak) | 11.2% / 108.3% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 12.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.30 MiB / 34.30 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.5% / 0.0% / 2.0% / 3.0% / 5.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.30 MiB / 34.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 3.9% / 5.8% |
| HAProxy RSS (avg / peak, summed) | 21.70 MiB / 21.80 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.1% / 1.0% / 3.9% / 5.8% / 11.7% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 15.3% / 110.3% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 18.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.00 MiB / 56.10 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.16% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 44 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (39444.50 ms) |
| Error rate | < 0.1% | ❌ FAIL (64.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 40.95 RPS (all instances) |
| **Achieved throughput** | 15.28 RPS (all instances) |
| **Attempted − achieved gap** | 25.67 RPS (62.69%) |
| **Total attempted ops** | 43203 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29982.719 | 40042.495 | 46268.415 | 3.563006157299281 | 66.36% | 0.1503006012024048 | 11 |
| 1 | 29933.567 | 39157.759 | 44924.927 | 3.962999367777905 | 62.58% | 0.1503006012024048 | 10 |
| 2 | 29966.335 | 39518.207 | 46202.879 | 3.7004423658945087 | 65.07% | 0.1503006012024048 | 11 |
| 3 | 29933.567 | 39059.455 | 44597.247 | 4.054305127932901 | 61.71% | 0.20030045067601399 | 12 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 7414 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=15, active=15, idle=0, waiting=360) |
| 1 | SQLTransientConnectionException | 6991 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=360) |
| 2 | SQLTransientConnectionException | 7272 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=16, active=16, idle=0, waiting=360) |
| 3 | SQLTransientConnectionException | 6894 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=360) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-02T09:58:54Z → 2026-07-02T10:13:54Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 24745 / 35502 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 525297752 | Cumulative since stats reset |
| Transactions rolled back | 4830 | Non-zero → contention or application errors |
| Temp file bytes written | -1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7554 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 755824 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-02T09:58:54Z → 2026-07-02T10:13:54Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 5.9 | 3.0 | 2.0 | 3.9 | 32.4 | 103.4 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 5.5 | 2.9 | 33.2 | 35.0 | 37.4 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 2.9 | 2.0 | 3.9 | 31.5 | 34.3 | 11.4 | 11.4 |
| PostgreSQL | db | 274.0 | 273.4 | 329.0 | 341.5 | 349.6 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 15559.1 | 17814.4 |
| HAProxy | lb | 0.6 | 0.0 | 1.9 | 3.9 | 5.8 | 4.2 | 3.9 | 5.8 | 33.0 | 41.5 | 21.7 | 21.8 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-02T10:16:56Z*
