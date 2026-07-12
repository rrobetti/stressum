# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-12T13:15:52Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260712-140359` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.66 RPS (per instance) |
| **Total throughput** | 18.64 RPS (all instances) |
| **p50 latency** | 29945.75 ms |
| **p95 latency** | 39206.75 ms |
| **p99 latency** | 45564.00 ms |
| **p999 latency** | 61284.25 ms |
| **Error rate** | 61.00% (0.61) |
| **Total requests** | 44682 |
| **Failed requests** | 27282 |
| **Total successful** | 17400 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 18.39 |
| observed_postgres_backends_median_numbackends | 19 |
| observed_client_backends_active_median | 27791 |
| observed_client_backends_active_max | 40170 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 3.9% / 3.9% |
| OJP proxy-tier host_cpu (avg / peak) | 9.9% / 68.3% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 10.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.10 MiB / 34.10 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 3.9% / 3.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.10 MiB / 34.10 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 3.9% / 4.8% |
| HAProxy RSS (avg / peak, summed) | 21.80 MiB / 21.80 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.2% / 1.0% / 3.9% / 6.8% / 8.8% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 21.1% / 101.0% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 15.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 55.90 MiB / 55.90 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.15% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 48 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (39206.75 ms) |
| Error rate | < 0.1% | ❌ FAIL (61.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.28 RPS (all instances) |
| **Achieved throughput** | 18.64 RPS (all instances) |
| **Attempted − achieved gap** | 27.64 RPS (59.73%) |
| **Total attempted ops** | 43203 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29999.103 | 39387.135 | 45711.359 | 4.575366815435607 | 61.70% | 0.1502253380070105 | 12 |
| 1 | 29933.567 | 39223.295 | 44957.695 | 4.52477547393999 | 62.16% | 0.1502253380070105 | 11 |
| 2 | 29949.951 | 39157.759 | 46366.719 | 4.851189104175668 | 59.49% | 0.1503006012024048 | 10 |
| 3 | 29900.799 | 39059.455 | 45219.839 | 4.688645003052447 | 60.87% | 0.15015015015015015 | 15 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 6893 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=360) |
| 1 | SQLTransientConnectionException | 6945 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=360) |
| 2 | SQLTransientConnectionException | 6646 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=360) |
| 3 | SQLTransientConnectionException | 6798 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=360) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-12T13:15:52Z → 2026-07-12T13:30:52Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 19 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 27791 / 40170 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 535167477 | Cumulative since stats reset |
| Transactions rolled back | 5053 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7839 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 737557 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-12T13:15:52Z → 2026-07-12T13:30:52Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 3.1 | 2.9 | 4.9 | 6.9 | 33.5 | 11.3 | 11.3 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 3.2 | 2.9 | 4.9 | 32.4 | 33.3 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 3.8 | 2.9 | 5.9 | 33.3 | 35.9 | 11.4 | 11.4 |
| PostgreSQL | db | 300.9 | 301.9 | 355.9 | 370.0 | 386.2 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 14548.1 | 16183.3 |
| HAProxy | lb | 0.6 | 0.0 | 1.9 | 3.9 | 4.8 | 11.6 | 4.8 | 35.0 | 37.1 | 91.3 | 21.8 | 21.8 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-12T13:33:59Z*
