# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-11T13:44:18Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260711-143229` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.00 RPS (per instance) |
| **Total throughput** | 4.00 RPS (all instances) |
| **p50 latency** | 2.50 ms |
| **p95 latency** | 876.93 ms |
| **p99 latency** | 6799.35 ms |
| **p999 latency** | 10585.08 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 3604 |
| **Failed requests** | 0 |
| **Total successful** | 3604 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 13.61 |
| observed_postgres_backends_median_numbackends | 13 |
| observed_client_backends_active_median | 14174 |
| observed_client_backends_active_max | 21194 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.3% / 0.0% / 1.0% / 2.0% / 3.9% |
| OJP proxy-tier host_cpu (avg / peak) | 9.0% / 62.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 5.00% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.10 MiB / 34.10 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.3% / 0.0% / 1.0% / 2.0% / 3.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.10 MiB / 34.10 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.3% / 0.0% / 1.0% / 1.9% / 1.9% |
| HAProxy RSS (avg / peak, summed) | 22.00 MiB / 22.00 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 2.9% / 3.9% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 13.5% / 86.6% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 6.90% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.10 MiB / 56.10 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.10% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 12 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ✅ PASS (876.93 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 4.00 RPS (all instances) |
| **Achieved throughput** | 4.00 RPS (all instances) |
| **Attempted − achieved gap** | 0.00 RPS (0.00%) |
| **Total attempted ops** | 3604 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 2.621 | 619.007 | 4399.103 | 1.0002286871360155 | 0.00% | 0.10010010010010009 | 3 |
| 1 | 2.665 | 817.663 | 6209.535 | 1.0002020385915913 | 0.00% | 0.10010010010010009 | 4 |
| 2 | 2.385 | 625.151 | 8945.663 | 0.9999311923041921 | 0.00% | 0.10010010010010009 | 2 |
| 3 | 2.341 | 1445.887 | 7643.135 | 1.0001132203645695 | 0.00% | 0.10005002501250625 | 3 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-11T13:44:18Z → 2026-07-11T13:59:18Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 13 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 14174 / 21194 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 88704515 | Cumulative since stats reset |
| Transactions rolled back | 1299 | Non-zero → contention or application errors |
| Temp file bytes written | 1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1336 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 134016 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-11T13:44:18Z → 2026-07-11T13:59:18Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.1 | 0.0 | 1.0 | 1.0 | 1.0 | 3.0 | 2.0 | 3.9 | 32.4 | 34.1 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.1 | 0.0 | 1.0 | 1.0 | 2.0 | 3.2 | 2.9 | 3.9 | 32.4 | 57.6 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.1 | 0.0 | 1.0 | 1.0 | 2.0 | 3.0 | 2.0 | 3.9 | 32.4 | 49.0 | 11.3 | 11.3 |
| PostgreSQL | db | 34.1 | 0.7 | 203.0 | 265.4 | 304.6 | 166.5 | 127.5 | 399.5 | 400.0 | 400.0 | 12330.1 | 15828.1 |
| HAProxy | lb | 0.3 | 0.0 | 1.0 | 1.9 | 1.9 | 4.7 | 3.9 | 5.8 | 34.1 | 50.5 | 22.0 | 22.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-11T14:01:52Z*
