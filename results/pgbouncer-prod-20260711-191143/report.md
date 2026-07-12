# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-11T18:23:34Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260711-191143` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.76 RPS (per instance) |
| **Total throughput** | 15.02 RPS (all instances) |
| **p50 latency** | 8588.30 ms |
| **p95 latency** | 26931.25 ms |
| **p99 latency** | 34779.25 ms |
| **p999 latency** | 49659.75 ms |
| **Error rate** | 3.00% (0.03) |
| **Total requests** | 14479 |
| **Failed requests** | 487 |
| **Total successful** | 13992 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 17.95 |
| observed_postgres_backends_median_numbackends | 19 |
| observed_client_backends_active_median | 21615 |
| observed_client_backends_active_max | 32517 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.5% / 0.0% / 2.0% / 2.9% / 3.9% |
| OJP proxy-tier host_cpu (avg / peak) | 9.1% / 67.3% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 9.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.20 MiB / 34.20 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.5% / 0.0% / 2.0% / 2.9% / 3.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.20 MiB / 34.20 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.5% / 0.0% / 1.9% / 2.9% / 3.9% |
| HAProxy RSS (avg / peak, summed) | 22.10 MiB / 22.20 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.1% / 1.0% / 3.9% / 5.8% / 7.8% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 19.8% / 77.7% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 13.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.30 MiB / 56.40 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.10% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 37 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (26931.25 ms) |
| Error rate | < 0.1% | ❌ FAIL (3.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.46 RPS (all instances) |
| **Achieved throughput** | 15.02 RPS (all instances) |
| **Attempted − achieved gap** | 0.44 RPS (2.86%) |
| **Total attempted ops** | 14404 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 8732.671 | 29949.951 | 38928.383 | 3.548920813231885 | 8.28% | 0.1002004008016032 | 9 |
| 1 | 7237.631 | 24231.935 | 31195.135 | 3.835350737098107 | 1.02% | 0.10012516271905354 | 9 |
| 2 | 7610.367 | 28262.399 | 36372.479 | 3.7945809514186144 | 2.57% | 0.10015022533800699 | 9 |
| 3 | 10772.479 | 25280.511 | 32620.543 | 3.8423111204998346 | 1.60% | 0.10005002501250625 | 10 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 299 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=8, active=8, idle=0, waiting=45) |
| 1 | SQLTransientConnectionException | 37 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=11, active=11, idle=0, waiting=64) |
| 2 | SQLTransientConnectionException | 93 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=63) |
| 3 | SQLTransientConnectionException | 58 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=85) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-11T18:23:34Z → 2026-07-11T18:38:34Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 19 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 21615 / 32517 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 425998512 | Cumulative since stats reset |
| Transactions rolled back | 4463 | Non-zero → contention or application errors |
| Temp file bytes written | -1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5537 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 409214 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-11T18:23:34Z → 2026-07-11T18:38:34Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 3.1 | 2.9 | 3.9 | 31.5 | 60.5 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 3.3 | 2.9 | 4.8 | 33.0 | 51.0 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 2.8 | 2.0 | 3.9 | 26.5 | 35.3 | 11.4 | 11.4 |
| PostgreSQL | db | 231.5 | 242.7 | 295.5 | 307.6 | 319.3 | 386.3 | 400.0 | 400.0 | 400.0 | 400.0 | 15059.4 | 16936.6 |
| HAProxy | lb | 0.5 | 0.0 | 1.9 | 2.9 | 3.9 | 11.0 | 4.8 | 34.1 | 36.1 | 64.1 | 22.1 | 22.2 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-11T18:41:45Z*
