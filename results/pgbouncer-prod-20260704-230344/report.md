# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-04T22:15:36Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260704-230344` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.95 RPS (per instance) |
| **Total throughput** | 15.80 RPS (all instances) |
| **p50 latency** | 22.89 ms |
| **p95 latency** | 13750.27 ms |
| **p99 latency** | 22917.12 ms |
| **p999 latency** | 35618.75 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 14443 |
| **Failed requests** | 8 |
| **Total successful** | 14435 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 16.87 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 21596 |
| observed_client_backends_active_max | 33091 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 2.9% / 4.9% |
| OJP proxy-tier host_cpu (avg / peak) | 8.4% / 60.8% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 8.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.10 MiB / 34.00 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 2.9% / 4.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.10 MiB / 34.00 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 1.0% / 1.9% / 2.9% / 3.9% |
| HAProxy RSS (avg / peak, summed) | 22.20 MiB / 22.30 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.2% / 1.0% / 3.9% / 5.8% / 6.8% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 12.0% / 73.2% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 12.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.30 MiB / 56.30 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.13% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 39 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (13750.27 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.77 RPS (all instances) |
| **Achieved throughput** | 15.80 RPS (all instances) |
| **Attempted − achieved gap** | -0.03 RPS (-0.21%) |
| **Total attempted ops** | 14404 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 20.975 | 15097.855 | 26705.919 | 3.947815600504303 | 0.19% | 0.12518797011344188 | 10 |
| 1 | 18.671 | 13377.535 | 21446.655 | 3.950109189564699 | 0.03% | 0.1502253380070105 | 10 |
| 2 | 17.647 | 11255.807 | 19136.511 | 3.945500993471473 | 0.00% | 0.10025062656641603 | 10 |
| 3 | 34.271 | 15269.887 | 24379.391 | 3.956531779760726 | 0.00% | 0.15015015015015015 | 9 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 7 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=5, active=5, idle=0, waiting=87) |
| 1 | SQLTransientConnectionException | 1 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=52) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-04T22:15:36Z → 2026-07-04T22:30:36Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 21596 / 33091 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 439303536 | Cumulative since stats reset |
| Transactions rolled back | 4300 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5048 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 361588 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-04T22:15:36Z → 2026-07-04T22:30:36Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 2.6 | 2.0 | 3.9 | 4.9 | 35.3 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 3.0 | 2.0 | 3.9 | 32.4 | 34.3 | 11.3 | 11.3 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 3.1 | 2.9 | 3.9 | 32.4 | 34.1 | 11.4 | 11.3 |
| PostgreSQL | db | 209.1 | 245.1 | 324.0 | 335.4 | 345.7 | 339.8 | 399.6 | 400.0 | 400.0 | 400.0 | 14571.8 | 16971.4 |
| HAProxy | lb | 0.6 | 1.0 | 1.9 | 2.9 | 3.9 | 3.7 | 3.9 | 4.9 | 5.9 | 35.9 | 22.2 | 22.3 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-04T22:33:22Z*
