# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-23T02:48:57Z |
| **Duration** | 1800 s |
| **Instances**| 4 |
| **Target RPS**| 5 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260523-033622` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.80 RPS (per instance) |
| **Total throughput** | 3.18 RPS (all instances) |
| **p50 latency** | 29233.25 ms |
| **p95 latency** | 60031.00 ms |
| **p99 latency** | 60883.00 ms |
| **p999 latency** | 65921.00 ms |
| **Error rate** | 80.00% (0.80) |
| **Total requests** | 36630 |
| **Failed requests** | 29453 |
| **Total successful** | 7177 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 24 |
| observed_postgres_backends_avg_numbackends | 21.70 |
| observed_postgres_backends_median_numbackends | 23 |
| observed_client_backends_active_median | 16962 |
| observed_client_backends_active_max | 26751 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 8.4% / 1.0% / 29.3% / 45.8% / 77.7% |
| OJP proxy-tier host_cpu (avg / peak) | 17.5% / 84.4% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 130.90% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.40 MiB / 34.30 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 5 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 8.4% / 1.0% / 29.3% / 45.8% / 77.7% |
| PgBouncer tier RSS (avg / peak, summed) | 34.40 MiB / 34.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.7% / 1.0% / 23.2% / 34.8% / 56.7% |
| HAProxy RSS (avg / peak, summed) | 22.10 MiB / 22.10 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 14.9% / 1.9% / 53.3% / 78.6% / 134.1% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 27.7% / 148.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 187.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.50 MiB / 56.40 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.13% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 15265 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 150 ms | ❌ FAIL (60031.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (80.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.97 RPS (all instances) |
| **Achieved throughput** | 3.18 RPS (all instances) |
| **Attempted − achieved gap** | 12.78 RPS (80.07%) |
| **Total attempted ops** | 42004 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.66 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29294.591 | 60030.975 | 63438.847 | 0.7591970604173632 | 81.30% | 0.15015015015015015 | 3876 |
| 1 | 29343.743 | 60030.975 | 60030.975 | 0.7906824525257936 | 80.53% | 0.10025062656641603 | 4375 |
| 2 | 29278.207 | 60030.975 | 60030.975 | 0.7791529361471531 | 80.81% | 0.15015015015015015 | 3999 |
| 3 | 29016.063 | 60030.975 | 60030.975 | 0.8536532367426544 | 78.98% | 0.10025062656641603 | 3015 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 7444 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=5, active=5, idle=0, waiting=150) |
| 1 | SQLTransientConnectionException | 7376 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=150) |
| 2 | SQLTransientConnectionException | 7400 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=150) |
| 3 | SQLTransientConnectionException | 7233 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=150) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-23T02:48:57Z → 2026-05-23T03:18:57Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 23 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 16962 / 26751 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 557073724 | Cumulative since stats reset |
| Transactions rolled back | 0 | Non-zero → contention or application errors |
| Temp file bytes written | -1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 6414 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 652201 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-23T02:48:57Z → 2026-05-23T03:18:57Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 3.1 | 0.0 | 15.6 | 22.5 | 40.6 | 5.7 | 2.9 | 19.0 | 31.5 | 49.0 | 11.5 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 2.8 | 0.0 | 15.7 | 25.4 | 43.9 | 6.0 | 2.9 | 21.7 | 36.8 | 50.5 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 2.7 | 0.0 | 15.6 | 24.4 | 46.4 | 6.2 | 2.9 | 22.7 | 35.1 | 53.7 | 11.5 | 11.5 |
| PostgreSQL | db | 297.9 | 305.0 | 328.4 | 334.5 | 341.2 | 400.0 | 400.0 | 400.0 | 400.0 | 400.0 | 113369.1 | 122655.0 |
| HAProxy | lb | 6.7 | 1.0 | 23.2 | 34.8 | 56.7 | 10.5 | 4.8 | 30.6 | 43.1 | 69.7 | 22.1 | 22.1 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-23T03:21:58Z*
