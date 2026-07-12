# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-11T21:00:31Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260711-214850` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.40 RPS (per instance) |
| **Total throughput** | 13.59 RPS (all instances) |
| **p50 latency** | 14077.95 ms |
| **p95 latency** | 42016.75 ms |
| **p99 latency** | 116391.75 ms |
| **p999 latency** | 233242.75 ms |
| **Error rate** | 11.00% (0.11) |
| **Total requests** | 14351 |
| **Failed requests** | 1648 |
| **Total successful** | 12703 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 80 |
| observed_postgres_backends_max_numbackends | 89 |
| observed_postgres_backends_avg_numbackends | 86.37 |
| observed_postgres_backends_median_numbackends | 88 |
| observed_client_backends_active_median | 19492 |
| observed_client_backends_active_max | 28177 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | hikari-prod |
| Configured replicas | 4 |
| Configured client pool size (per replica) | 20 |
| OJP servers | N/A |
| Real DB connections per OJP server | N/A |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| OJP proxy-tier host_cpu (avg / peak) | N/A% / N/A% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 0% |
| OJP proxy-tier RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| PgBouncer tier RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | N/A% / N/A% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 0.00% |
| Total PgBouncer proxy-tier RSS (avg / peak) | N/A MiB / 0.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.18% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 71 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (42016.75 ms) |
| Error rate | < 0.1% | ❌ FAIL (11.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.41 RPS (all instances) |
| **Achieved throughput** | 13.59 RPS (all instances) |
| **Attempted − achieved gap** | 1.82 RPS (11.81%) |
| **Total attempted ops** | 14404 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 14704.639 | 43286.527 | 109903.871 | 3.4031830777737495 | 11.29% | 0.1502253380070105 | 20 |
| 1 | 11608.063 | 38633.471 | 109838.335 | 3.494091488085116 | 8.92% | 0.19990004997501248 | 21 |
| 2 | 14991.359 | 46694.399 | 132448.255 | 3.278050324756927 | 14.58% | 0.1502253380070105 | 16 |
| 3 | 15007.743 | 39452.671 | 113377.279 | 3.4106660049967488 | 11.15% | 0.19990004997501248 | 14 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 405 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=20, active=20, idle=0, waiting=97) |
| 1 | SQLTransientConnectionException | 320 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=20, active=20, idle=0, waiting=47) |
| 2 | SQLTransientConnectionException | 523 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=20, active=20, idle=0, waiting=57) |
| 3 | SQLTransientConnectionException | 400 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=20, active=20, idle=0, waiting=77) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-11T21:00:31Z → 2026-07-11T21:15:31Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 88 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 19492 / 28177 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 380991904 | Cumulative since stats reset |
| Transactions rolled back | 4101 | Non-zero → contention or application errors |
| Temp file bytes written | 53 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -35 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4686 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 356442 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-11T21:00:31Z → 2026-07-11T21:15:31Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 213.6 | 211.7 | 240.7 | 250.6 | 250.6 | 400.0 | 400.0 | 400.0 | 400.0 | 400.0 | 32693.0 | 40131.3 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-11T21:18:33Z*
