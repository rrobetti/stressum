# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-30T22:02:28Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260530-225008` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.14 RPS (per instance) |
| **Total throughput** | 2.29 RPS (all instances) |
| **p50 latency** | 26869.75 ms |
| **p95 latency** | 60031.00 ms |
| **p99 latency** | 60031.00 ms |
| **p999 latency** | 65388.50 ms |
| **Error rate** | 58.00% (0.58) |
| **Total requests** | 7418 |
| **Failed requests** | 4320 |
| **Total successful** | 3098 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 25 |
| observed_postgres_backends_avg_numbackends | 21.83 |
| observed_postgres_backends_median_numbackends | 23 |
| observed_client_backends_active_median | 15391 |
| observed_client_backends_active_max | 21294 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | pgbouncer-prod |
| Configured replicas | 2 |
| Configured client pool size (per replica) | 20 |
| OJP servers | N/A |
| Real DB connections per OJP server | N/A |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.2% / 0.0% / 1.0% / 2.0% / 3.9% |
| OJP proxy-tier host_cpu (avg / peak) | 16.1% / 204.9% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 7.80% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.40 MiB / 34.30 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 5 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.2% / 0.0% / 1.0% / 2.0% / 3.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.40 MiB / 34.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.1% / 0.0% / 1.0% / 1.9% / 2.9% |
| HAProxy RSS (avg / peak, summed) | 22.20 MiB / 22.20 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.3% / 0.0% / 1.9% / 2.9% / 5.9% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 19.8% / 208.8% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 10.70% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.60 MiB / 56.50 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.10% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 14 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (60031.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (58.00%) |

## Open-Loop Sanity (2/2 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 5.32 RPS (all instances) |
| **Achieved throughput** | 2.29 RPS (all instances) |
| **Attempted − achieved gap** | 3.03 RPS (56.98%) |
| **Total attempted ops** | 9602 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.39 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 27213.823 | 60030.975 | 60030.975 | 1.1328304599291668 | 58.61% | 0.1002004008016032 | 7 |
| 1 | 26525.695 | 60030.975 | 60030.975 | 1.1534953195986457 | 57.86% | 0.10010010010010009 | 7 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 2174 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=120) |
| 1 | SQLTransientConnectionException | 2146 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=120) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-30T22:02:28Z → 2026-05-30T22:17:28Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 23 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 15391 / 21294 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 394848269 | Cumulative since stats reset |
| Transactions rolled back | 901 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 3558 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 364433 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-30T22:02:28Z → 2026-05-30T22:17:28Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.0 | 0.0 | 0.0 | 1.0 | 2.0 | 2.6 | 2.0 | 2.9 | 28.4 | 35.0 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.1 | 0.0 | 0.0 | 1.0 | 2.9 | 4.8 | 2.0 | 28.6 | 34.1 | 200.0 | 11.5 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.1 | 0.0 | 0.0 | 1.0 | 2.9 | 9.1 | 2.9 | 32.4 | 48.0 | 71.8 | 11.5 | 11.5 |
| PostgreSQL | db | 201.4 | 202.8 | 227.6 | 232.9 | 236.5 | 400.0 | 400.0 | 400.0 | 400.0 | 400.0 | 46566.8 | 51526.7 |
| HAProxy | lb | 0.1 | 0.0 | 1.0 | 1.9 | 2.9 | 3.8 | 2.9 | 4.8 | 32.9 | 34.1 | 22.2 | 22.2 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-30T22:20:28Z*
