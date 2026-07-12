# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-11T21:32:19Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260711-222025` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.81 RPS (per instance) |
| **Total throughput** | 15.24 RPS (all instances) |
| **p50 latency** | 9733.12 ms |
| **p95 latency** | 26095.50 ms |
| **p99 latency** | 32784.50 ms |
| **p999 latency** | 49209.25 ms |
| **Error rate** | 2.00% (0.02) |
| **Total requests** | 14441 |
| **Failed requests** | 239 |
| **Total successful** | 14202 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 18.13 |
| observed_postgres_backends_median_numbackends | 19 |
| observed_client_backends_active_median | 21800 |
| observed_client_backends_active_max | 32934 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.5% / 0.0% / 2.0% / 3.9% / 4.9% |
| OJP proxy-tier host_cpu (avg / peak) | 8.8% / 60.1% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 11.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.10 MiB / 34.10 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.5% / 0.0% / 2.0% / 3.9% / 4.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.10 MiB / 34.10 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 2.9% / 4.8% |
| HAProxy RSS (avg / peak, summed) | 21.90 MiB / 21.90 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.1% / 1.0% / 3.9% / 5.8% / 9.8% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 19.9% / 86.7% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 16.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.00 MiB / 56.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.13% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 26 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (26095.50 ms) |
| Error rate | < 0.1% | ❌ FAIL (2.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.46 RPS (all instances) |
| **Achieved throughput** | 15.24 RPS (all instances) |
| **Attempted − achieved gap** | 0.22 RPS (1.40%) |
| **Total attempted ops** | 14404 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 13238.271 | 26968.063 | 33406.975 | 3.766816719019216 | 2.30% | 0.10015022533800699 | 6 |
| 1 | 8085.503 | 22478.847 | 29523.967 | 3.8404840921071983 | 1.00% | 0.15015015015015015 | 8 |
| 2 | 8376.319 | 26509.311 | 32686.079 | 3.8354688009893 | 1.02% | 0.1002004008016032 | 5 |
| 3 | 9232.383 | 28426.239 | 35520.511 | 3.798079871575407 | 2.30% | 0.1500750375187594 | 7 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 83 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=8, active=8, idle=0, waiting=62) |
| 1 | SQLTransientConnectionException | 36 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=13, active=13, idle=0, waiting=38) |
| 2 | SQLTransientConnectionException | 37 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=59) |
| 3 | SQLTransientConnectionException | 83 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=9, active=9, idle=0, waiting=78) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-11T21:32:19Z → 2026-07-11T21:47:19Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 19 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 21800 / 32934 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 429129914 | Cumulative since stats reset |
| Transactions rolled back | 4514 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5568 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 412848 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-11T21:32:19Z → 2026-07-11T21:47:19Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 2.8 | 2.0 | 3.9 | 23.5 | 34.3 | 11.3 | 11.3 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 4.9 | 3.3 | 2.9 | 4.9 | 32.4 | 34.3 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 2.9 | 2.0 | 3.9 | 23.5 | 34.5 | 11.4 | 11.4 |
| PostgreSQL | db | 228.3 | 239.9 | 294.6 | 303.4 | 306.8 | 384.4 | 400.0 | 400.0 | 400.0 | 400.0 | 15103.5 | 17227.1 |
| HAProxy | lb | 0.6 | 0.0 | 1.9 | 2.9 | 4.8 | 11.3 | 4.8 | 34.3 | 37.4 | 78.9 | 21.9 | 21.9 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-11T21:50:31Z*
