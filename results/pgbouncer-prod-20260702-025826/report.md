# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-02T02:10:19Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260702-025826` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.98 RPS (per instance) |
| **Total throughput** | 15.90 RPS (all instances) |
| **p50 latency** | 29519.75 ms |
| **p95 latency** | 38518.75 ms |
| **p99 latency** | 45039.50 ms |
| **p999 latency** | 61480.75 ms |
| **Error rate** | 44.00% (0.44) |
| **Total requests** | 29754 |
| **Failed requests** | 12981 |
| **Total successful** | 16773 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 18.71 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 24226 |
| observed_client_backends_active_max | 35457 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 3.9% / 6.9% |
| OJP proxy-tier host_cpu (avg / peak) | 12.5% / 97.2% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 12.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.30 MiB / 34.30 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 3.9% / 6.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.30 MiB / 34.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 2.9% / 5.8% |
| HAProxy RSS (avg / peak, summed) | 21.90 MiB / 21.90 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.1% / 1.0% / 3.9% / 5.9% / 11.7% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 16.9% / 101.1% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 18.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.20 MiB / 56.20 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.15% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 44 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (38518.75 ms) |
| Error rate | < 0.1% | ❌ FAIL (44.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 27.31 RPS (all instances) |
| **Achieved throughput** | 15.90 RPS (all instances) |
| **Attempted − achieved gap** | 11.41 RPS (41.77%) |
| **Total attempted ops** | 28804 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29622.271 | 38633.471 | 43974.655 | 3.841506303316681 | 45.50% | 0.15018774407858032 | 12 |
| 1 | 29589.503 | 38666.239 | 44466.175 | 4.1326622496469225 | 41.48% | 0.15015015015015015 | 10 |
| 2 | 29163.519 | 37945.343 | 44597.247 | 4.047355001374394 | 42.66% | 0.1502253380070105 | 11 |
| 3 | 29704.191 | 38830.079 | 47120.383 | 3.882431334708993 | 44.87% | 0.1502253380070105 | 11 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 3379 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=225) |
| 1 | SQLTransientConnectionException | 3091 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=240) |
| 2 | SQLTransientConnectionException | 3177 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=6, active=6, idle=0, waiting=240) |
| 3 | SQLTransientConnectionException | 3334 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=10, active=10, idle=0, waiting=222) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-02T02:10:19Z → 2026-07-02T02:25:19Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 24226 / 35457 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 528125677 | Cumulative since stats reset |
| Transactions rolled back | 5135 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7085 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 722208 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-02T02:10:19Z → 2026-07-02T02:25:19Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 5.2 | 2.0 | 31.5 | 33.3 | 49.0 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.9 | 4.9 | 4.6 | 2.9 | 26.5 | 34.3 | 43.3 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 3.0 | 2.0 | 3.9 | 32.4 | 34.3 | 11.4 | 11.4 |
| PostgreSQL | db | 275.6 | 275.8 | 327.5 | 336.1 | 358.3 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 15498.9 | 17336.2 |
| HAProxy | lb | 0.6 | 0.0 | 1.9 | 2.9 | 5.8 | 4.6 | 3.9 | 6.8 | 34.8 | 48.5 | 21.9 | 21.9 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-02T02:28:25Z*
