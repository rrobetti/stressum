# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-02T14:40:58Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260702-152856` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.95 RPS (per instance) |
| **Total throughput** | 15.79 RPS (all instances) |
| **p50 latency** | 29958.25 ms |
| **p95 latency** | 39698.25 ms |
| **p99 latency** | 45007.00 ms |
| **p999 latency** | 64118.75 ms |
| **Error rate** | 63.00% (0.63) |
| **Total requests** | 44680 |
| **Failed requests** | 28021 |
| **Total successful** | 16659 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 18.98 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 25681 |
| observed_client_backends_active_max | 36614 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 3.9% / 4.9% |
| OJP proxy-tier host_cpu (avg / peak) | 12.0% / 92.6% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 11.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.40 MiB / 34.40 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 3.9% / 4.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.40 MiB / 34.40 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 2.9% / 3.9% |
| HAProxy RSS (avg / peak, summed) | 22.10 MiB / 22.10 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.1% / 1.0% / 3.9% / 5.9% / 8.8% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 19.9% / 128.5% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 15.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.50 MiB / 56.50 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.16% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 50 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (39698.25 ms) |
| Error rate | < 0.1% | ❌ FAIL (63.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 40.95 RPS (all instances) |
| **Achieved throughput** | 15.79 RPS (all instances) |
| **Attempted − achieved gap** | 25.16 RPS (61.44%) |
| **Total attempted ops** | 43204 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29982.719 | 39387.135 | 43876.351 | 4.001861595493498 | 62.19% | 0.15037593984962408 | 14 |
| 1 | 29949.951 | 39616.511 | 43810.815 | 3.996178228032394 | 62.25% | 0.15045135406218654 | 13 |
| 2 | 29949.951 | 40140.799 | 46235.647 | 3.8587275393337133 | 63.57% | 0.20030045067601399 | 12 |
| 3 | 29949.951 | 39649.279 | 46104.575 | 3.9336120036776903 | 62.85% | 0.15037593984962408 | 11 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 6943 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=348) |
| 1 | SQLTransientConnectionException | 6953 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=360) |
| 2 | SQLTransientConnectionException | 7104 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=14, active=14, idle=0, waiting=360) |
| 3 | SQLTransientConnectionException | 7021 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=360) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-02T14:40:58Z → 2026-07-02T14:55:58Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 25681 / 36614 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 528458043 | Cumulative since stats reset |
| Transactions rolled back | 5002 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7798 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 754601 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-02T14:40:58Z → 2026-07-02T14:55:58Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 3.8 | 2.0 | 11.8 | 33.3 | 64.7 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 5.7 | 2.9 | 33.2 | 35.3 | 88.7 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 2.7 | 2.0 | 3.9 | 13.7 | 36.1 | 11.5 | 11.5 |
| PostgreSQL | db | 273.3 | 273.8 | 327.4 | 341.0 | 352.9 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 15639.8 | 17644.6 |
| HAProxy | lb | 0.6 | 0.0 | 1.9 | 2.9 | 3.9 | 8.1 | 3.9 | 34.0 | 36.9 | 63.8 | 22.1 | 22.1 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-02T14:59:07Z*
