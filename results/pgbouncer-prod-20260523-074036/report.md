# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-23T06:53:02Z |
| **Duration** | 1800 s |
| **Instances**| 4 |
| **Target RPS**| 5 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260523-074036` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.77 RPS (per instance) |
| **Total throughput** | 3.08 RPS (all instances) |
| **p50 latency** | 29171.75 ms |
| **p95 latency** | 60031.00 ms |
| **p99 latency** | 60514.25 ms |
| **p999 latency** | 65921.00 ms |
| **Error rate** | 81.00% (0.81) |
| **Total requests** | 36633 |
| **Failed requests** | 29687 |
| **Total successful** | 6946 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 24 |
| observed_postgres_backends_avg_numbackends | 21.44 |
| observed_postgres_backends_median_numbackends | 23 |
| observed_client_backends_active_median | 17373 |
| observed_client_backends_active_max | 27169 |
| observed_client_backends_idle_median | 1 |
| observed_client_backends_idle_max | 1 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | pgbouncer-prod |
| Configured replicas | 4 |
| Configured client pool size (per replica) | 20 |
| OJP servers | N/A |
| Real DB connections per OJP server | N/A |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 8.8% / 2.9% / 30.1% / 42.0% / 68.8% |
| OJP proxy-tier host_cpu (avg / peak) | 18.1% / 94.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 140.90% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.30 MiB / 34.30 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 5 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 8.8% / 2.9% / 30.1% / 42.0% / 68.8% |
| PgBouncer tier RSS (avg / peak, summed) | 34.30 MiB / 34.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 7.1% / 3.9% / 24.1% / 33.8% / 55.8% |
| HAProxy RSS (avg / peak, summed) | 22.00 MiB / 22.00 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 15.7% / 7.8% / 53.4% / 75.7% / 111.5% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 29.1% / 173.2% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 196.70% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.30 MiB / 56.30 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.13% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 15416 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 150 ms | ❌ FAIL (60031.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (81.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.97 RPS (all instances) |
| **Achieved throughput** | 3.08 RPS (all instances) |
| **Attempted − achieved gap** | 12.89 RPS (80.71%) |
| **Total attempted ops** | 42004 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.52 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29245.439 | 60030.975 | 60882.943 | 0.7991081208365003 | 80.32% | 0.15037593984962408 | 4368 |
| 1 | 29114.367 | 60030.975 | 60030.975 | 0.7166204957896328 | 82.36% | 0.10030090270812438 | 3256 |
| 2 | 29163.519 | 60030.975 | 60522.495 | 0.7392415302077947 | 81.80% | 0.1503006012024048 | 4327 |
| 3 | 29163.519 | 60030.975 | 60620.799 | 0.8252724041945656 | 79.68% | 0.10025062656641603 | 3465 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 7355 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=150) |
| 1 | SQLTransientConnectionException | 7544 | HikariPool-1 - Connection is not available, request timed out after 30015ms (total=9, active=9, idle=0, waiting=150) |
| 2 | SQLTransientConnectionException | 7491 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=150) |
| 3 | SQLTransientConnectionException | 7297 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=150) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-23T06:53:02Z → 2026-05-23T07:23:02Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 23 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 17373 / 27169 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 1 / 1 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 541618462 | Cumulative since stats reset |
| Transactions rolled back | 0 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 6503 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 663164 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-23T06:53:02Z → 2026-05-23T07:23:02Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 2.5 | 0.0 | 15.6 | 22.5 | 33.1 | 5.5 | 2.9 | 19.8 | 32.4 | 70.0 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 3.6 | 0.0 | 17.6 | 25.3 | 39.0 | 6.8 | 2.9 | 23.4 | 33.2 | 62.4 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 2.8 | 0.0 | 16.6 | 28.2 | 68.8 | 6.3 | 2.9 | 23.6 | 35.5 | 76.7 | 11.5 | 11.5 |
| PostgreSQL | db | 295.8 | 305.5 | 326.4 | 333.4 | 339.4 | 400.0 | 400.0 | 400.0 | 400.0 | 400.0 | 110127.7 | 121939.0 |
| HAProxy | lb | 7.1 | 3.9 | 24.1 | 33.8 | 55.8 | 11.3 | 7.9 | 32.4 | 43.8 | 147.6 | 22.0 | 22.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-23T07:26:04Z*
