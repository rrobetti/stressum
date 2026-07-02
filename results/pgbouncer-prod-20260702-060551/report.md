# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-02T05:17:44Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260702-060551` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.12 RPS (per instance) |
| **Total throughput** | 16.48 RPS (all instances) |
| **p50 latency** | 29487.00 ms |
| **p95 latency** | 38314.00 ms |
| **p99 latency** | 44638.25 ms |
| **p999 latency** | 62316.25 ms |
| **Error rate** | 42.00% (0.42) |
| **Total requests** | 29781 |
| **Failed requests** | 12413 |
| **Total successful** | 17368 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 18.61 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 24638 |
| observed_client_backends_active_max | 36290 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 3.9% / 5.9% |
| OJP proxy-tier host_cpu (avg / peak) | 13.0% / 69.8% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 14.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.30 MiB / 34.20 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 3.9% / 5.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.30 MiB / 34.20 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 3.9% / 5.8% |
| HAProxy RSS (avg / peak, summed) | 21.90 MiB / 21.90 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.2% / 1.0% / 3.9% / 6.8% / 11.7% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 19.7% / 89.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 20.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.20 MiB / 56.10 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.15% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 43 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (38314.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (42.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 27.33 RPS (all instances) |
| **Achieved throughput** | 16.48 RPS (all instances) |
| **Attempted − achieved gap** | 10.85 RPS (39.70%) |
| **Total attempted ops** | 28804 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29458.431 | 37978.111 | 43941.887 | 4.0786420576905575 | 42.20% | 0.1503006012024048 | 10 |
| 1 | 29523.967 | 38600.703 | 44924.927 | 3.9891735993035558 | 43.58% | 0.1503006012024048 | 10 |
| 2 | 29327.359 | 37978.111 | 43614.207 | 4.187645970457096 | 40.59% | 0.1503006012024048 | 12 |
| 3 | 29638.655 | 38699.007 | 46071.807 | 4.221545171008194 | 40.35% | 0.1503006012024048 | 11 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 3141 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=240) |
| 1 | SQLTransientConnectionException | 3246 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=240) |
| 2 | SQLTransientConnectionException | 3019 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=16, active=16, idle=0, waiting=218) |
| 3 | SQLTransientConnectionException | 3007 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=240) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-02T05:17:44Z → 2026-07-02T05:32:44Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 24638 / 36290 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 536568539 | Cumulative since stats reset |
| Transactions rolled back | 5229 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7047 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 709637 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-02T05:17:44Z → 2026-07-02T05:32:44Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 4.9 | 3.8 | 2.0 | 12.7 | 32.5 | 63.4 | 11.5 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.9 | 5.9 | 5.3 | 2.9 | 33.3 | 34.5 | 65.7 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 4.1 | 2.9 | 11.7 | 33.5 | 48.8 | 11.4 | 11.4 |
| PostgreSQL | db | 274.5 | 278.1 | 331.0 | 343.9 | 346.5 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 15575.2 | 17685.1 |
| HAProxy | lb | 0.6 | 0.0 | 1.9 | 3.9 | 5.8 | 6.9 | 3.9 | 34.0 | 36.9 | 79.6 | 21.9 | 21.9 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-02T05:35:49Z*
