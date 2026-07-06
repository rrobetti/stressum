# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-05T10:42:29Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260705-113040` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.96 RPS (per instance) |
| **Total throughput** | 19.86 RPS (all instances) |
| **p50 latency** | 29307.00 ms |
| **p95 latency** | 37503.00 ms |
| **p99 latency** | 43384.75 ms |
| **p999 latency** | 59269.00 ms |
| **Error rate** | 38.00% (0.38) |
| **Total requests** | 29736 |
| **Failed requests** | 11195 |
| **Total successful** | 18541 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 18.91 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 26102 |
| observed_client_backends_active_max | 38347 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.9% / 3.9% / 5.9% |
| OJP proxy-tier host_cpu (avg / peak) | 10.0% / 68.6% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 14.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.40 MiB / 34.30 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.9% / 3.9% / 5.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.40 MiB / 34.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 3.9% / 6.8% |
| HAProxy RSS (avg / peak, summed) | 21.90 MiB / 21.90 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.3% / 1.0% / 3.9% / 7.8% / 12.7% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 14.5% / 72.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 21.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.30 MiB / 56.20 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.15% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 43 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (37503.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (38.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 30.85 RPS (all instances) |
| **Achieved throughput** | 19.86 RPS (all instances) |
| **Attempted − achieved gap** | 10.99 RPS (35.63%) |
| **Total attempted ops** | 28804 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29392.895 | 37748.735 | 44204.031 | 4.695146993394709 | 41.04% | 0.15007503751875936 | 11 |
| 1 | 29327.359 | 37552.127 | 42565.631 | 5.116794532939767 | 35.83% | 0.15037593984962408 | 10 |
| 2 | 29392.895 | 37519.359 | 44400.639 | 5.025630824154258 | 36.86% | 0.15015015015015015 | 12 |
| 3 | 29114.367 | 37191.679 | 42369.023 | 5.020169749989536 | 36.85% | 0.15037593984962408 | 10 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 3056 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=240) |
| 1 | SQLTransientConnectionException | 2666 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=240) |
| 2 | SQLTransientConnectionException | 2743 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=240) |
| 3 | SQLTransientConnectionException | 2730 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=13, active=13, idle=0, waiting=181) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-05T10:42:29Z → 2026-07-05T10:57:29Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 26102 / 38347 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 555088390 | Cumulative since stats reset |
| Transactions rolled back | 5354 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7449 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 724700 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-05T10:42:29Z → 2026-07-05T10:57:29Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 4.7 | 2.9 | 30.4 | 33.3 | 35.0 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.9 | 5.9 | 2.5 | 2.0 | 3.9 | 4.9 | 10.8 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 4.9 | 3.1 | 2.0 | 3.9 | 32.5 | 33.3 | 11.5 | 11.4 |
| PostgreSQL | db | 303.9 | 302.8 | 358.4 | 369.5 | 373.3 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 14577.9 | 16368.0 |
| HAProxy | lb | 0.6 | 0.0 | 1.9 | 3.9 | 6.8 | 4.6 | 3.9 | 6.8 | 33.8 | 35.3 | 21.9 | 21.9 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-05T11:00:32Z*
