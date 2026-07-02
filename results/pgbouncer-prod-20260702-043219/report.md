# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-02T03:44:07Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260702-043219` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.05 RPS (per instance) |
| **Total throughput** | 16.21 RPS (all instances) |
| **p50 latency** | 29380.50 ms |
| **p95 latency** | 38076.50 ms |
| **p99 latency** | 45031.25 ms |
| **p999 latency** | 61997.25 ms |
| **Error rate** | 43.00% (0.43) |
| **Total requests** | 29767 |
| **Failed requests** | 12685 |
| **Total successful** | 17082 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 18.61 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 24113 |
| observed_client_backends_active_max | 35532 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 3.9% / 5.9% |
| OJP proxy-tier host_cpu (avg / peak) | 14.9% / 122.9% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 10.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.30 MiB / 34.20 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 3.9% / 5.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.30 MiB / 34.20 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 3.9% / 6.8% |
| HAProxy RSS (avg / peak, summed) | 22.00 MiB / 22.00 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.1% / 1.0% / 3.9% / 6.8% / 10.7% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 20.1% / 125.9% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 17.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.30 MiB / 56.20 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.15% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 37 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (38076.50 ms) |
| Error rate | < 0.1% | ❌ FAIL (43.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 27.34 RPS (all instances) |
| **Achieved throughput** | 16.21 RPS (all instances) |
| **Attempted − achieved gap** | 11.12 RPS (40.70%) |
| **Total attempted ops** | 28804 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29196.287 | 37781.503 | 44662.783 | 4.314659225332888 | 38.78% | 0.1503006012024048 | 9 |
| 1 | 29605.887 | 38699.007 | 45744.127 | 3.7516267633735825 | 46.74% | 0.1502253380070105 | 9 |
| 2 | 29376.511 | 37814.271 | 45580.287 | 4.104991255162114 | 42.01% | 0.1503006012024048 | 10 |
| 3 | 29343.743 | 38010.879 | 44138.495 | 4.039876076254918 | 42.94% | 0.15015015015015015 | 9 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 2883 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=226) |
| 1 | SQLTransientConnectionException | 3473 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=240) |
| 2 | SQLTransientConnectionException | 3130 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=240) |
| 3 | SQLTransientConnectionException | 3199 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=240) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-02T03:44:07Z → 2026-07-02T03:59:07Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 24113 / 35532 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 510320268 | Cumulative since stats reset |
| Transactions rolled back | 5281 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7169 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 706207 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-02T03:44:07Z → 2026-07-02T03:59:07Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 5.7 | 2.9 | 32.4 | 34.3 | 116.1 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 5.6 | 2.9 | 33.3 | 35.3 | 60.8 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.9 | 3.9 | 3.9 | 2.9 | 5.9 | 33.7 | 35.1 | 11.5 | 11.4 |
| PostgreSQL | db | 277.1 | 278.0 | 331.6 | 343.3 | 349.4 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 15529.7 | 17273.5 |
| HAProxy | lb | 0.6 | 0.0 | 1.9 | 3.9 | 6.8 | 5.4 | 3.9 | 25.4 | 35.0 | 36.9 | 22.0 | 22.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-02T04:02:09Z*
