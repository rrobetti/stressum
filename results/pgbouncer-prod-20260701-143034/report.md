# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-01T13:42:26Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260701-143034` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.88 RPS (per instance) |
| **Total throughput** | 3.53 RPS (all instances) |
| **p50 latency** | 2.69 ms |
| **p95 latency** | 1018.75 ms |
| **p99 latency** | 6098.45 ms |
| **p999 latency** | 10607.62 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 3604 |
| **Failed requests** | 0 |
| **Total successful** | 3604 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 13.72 |
| observed_postgres_backends_median_numbackends | 13 |
| observed_client_backends_active_median | 12567 |
| observed_client_backends_active_max | 18979 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.3% / 0.0% / 1.0% / 2.0% / 2.9% |
| OJP proxy-tier host_cpu (avg / peak) | 7.6% / 38.2% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 6.00% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.40 MiB / 34.40 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.3% / 0.0% / 1.0% / 2.0% / 2.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.40 MiB / 34.40 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.3% / 0.0% / 1.0% / 1.9% / 1.9% |
| HAProxy RSS (avg / peak, summed) | 21.70 MiB / 21.70 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 2.9% / 3.9% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 11.1% / 42.9% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 7.90% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.10 MiB / 56.10 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.10% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 11 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ✅ PASS (1018.75 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 3.53 RPS (all instances) |
| **Achieved throughput** | 3.53 RPS (all instances) |
| **Attempted − achieved gap** | 0.00 RPS (0.00%) |
| **Total attempted ops** | 3603 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 2.773 | 1128.447 | 3737.599 | 0.8825883249531523 | 0.00% | 0.1002004008016032 | 3 |
| 1 | 2.729 | 1213.439 | 5545.983 | 0.8825381837344589 | 0.00% | 0.10015022533800699 | 3 |
| 2 | 2.693 | 1291.263 | 7913.471 | 0.8825390481899623 | 0.00% | 0.1002004008016032 | 2 |
| 3 | 2.565 | 441.855 | 7196.671 | 0.8827024606923091 | 0.00% | 0.10015022533800699 | 3 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-01T13:42:26Z → 2026-07-01T13:57:26Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 13 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 12567 / 18979 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 88451115 | Cumulative since stats reset |
| Transactions rolled back | 1300 | Non-zero → contention or application errors |
| Temp file bytes written | 2 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -2 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1333 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 133568 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-01T13:42:26Z → 2026-07-01T13:57:26Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.1 | 0.0 | 1.0 | 1.0 | 2.0 | 2.4 | 2.0 | 2.9 | 3.9 | 33.2 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.1 | 0.0 | 1.0 | 1.0 | 2.0 | 2.4 | 2.0 | 2.9 | 3.9 | 4.8 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.1 | 0.0 | 1.0 | 1.0 | 2.0 | 3.1 | 2.0 | 3.9 | 31.5 | 34.3 | 11.5 | 11.5 |
| PostgreSQL | db | 33.2 | 0.7 | 189.2 | 269.3 | 311.9 | 126.7 | 84.8 | 399.1 | 400.0 | 400.0 | 11510.0 | 15255.7 |
| HAProxy | lb | 0.3 | 0.0 | 1.0 | 1.9 | 1.9 | 3.6 | 2.9 | 4.8 | 5.8 | 34.0 | 21.7 | 21.7 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-01T14:00:01Z*
