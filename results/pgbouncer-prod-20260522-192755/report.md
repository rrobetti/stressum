# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-22T18:40:17Z |
| **Duration** | 1800 s |
| **Instances**| 4 |
| **Target RPS**| 5 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260522-192755` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.68 RPS (per instance) |
| **Total throughput** | 2.72 RPS (all instances) |
| **p50 latency** | 29491.25 ms |
| **p95 latency** | 60031.00 ms |
| **p99 latency** | 60293.25 ms |
| **p999 latency** | 65503.25 ms |
| **Error rate** | 83.00% (0.83) |
| **Total requests** | 36633 |
| **Failed requests** | 30506 |
| **Total successful** | 6127 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 24 |
| observed_postgres_backends_avg_numbackends | 21.35 |
| observed_postgres_backends_median_numbackends | 23 |
| observed_client_backends_active_median | 16892 |
| observed_client_backends_active_max | 26019 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 9.0% / 3.9% / 29.4% / 42.0% / 75.8% |
| OJP proxy-tier host_cpu (avg / peak) | 18.1% / 87.0% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 140.00% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.50 MiB / 34.50 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 5 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 9.0% / 3.9% / 29.4% / 42.0% / 75.8% |
| PgBouncer tier RSS (avg / peak, summed) | 34.50 MiB / 34.50 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 7.2% / 4.8% / 23.2% / 31.8% / 49.8% |
| HAProxy RSS (avg / peak, summed) | 22.20 MiB / 22.20 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 16.0% / 9.7% / 52.5% / 73.2% / 124.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 29.3% / 141.2% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 189.80% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.70 MiB / 56.70 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.14% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 16411 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 150 ms | ❌ FAIL (60031.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (83.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.97 RPS (all instances) |
| **Achieved throughput** | 2.72 RPS (all instances) |
| **Attempted − achieved gap** | 13.25 RPS (82.98%) |
| **Total attempted ops** | 42004 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.50 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29409.279 | 60030.975 | 60030.975 | 0.772057633370628 | 81.00% | 0.15022533800701052 | 5203 |
| 1 | 29474.815 | 60030.975 | 60030.975 | 0.6607500710638919 | 83.72% | 0.14992503748125938 | 4040 |
| 2 | 29540.351 | 60030.975 | 60030.975 | 0.7090868212289686 | 82.54% | 0.1502253380070105 | 4316 |
| 3 | 29540.351 | 60030.975 | 61079.551 | 0.5751627262624533 | 85.84% | 0.1002004008016032 | 2852 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 7420 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=150) |
| 1 | SQLTransientConnectionException | 7664 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=3, active=3, idle=0, waiting=150) |
| 2 | SQLTransientConnectionException | 7560 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=150) |
| 3 | SQLTransientConnectionException | 7862 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=150) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-22T18:40:17Z → 2026-05-22T19:10:17Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 23 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 16892 / 26019 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 492436295 | Cumulative since stats reset |
| Transactions rolled back | 0 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5954 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 608154 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-22T18:40:17Z → 2026-05-22T19:10:17Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 2.5 | 0.0 | 15.6 | 22.4 | 39.0 | 5.0 | 2.0 | 18.7 | 28.0 | 64.0 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 3.2 | 0.0 | 16.6 | 25.5 | 44.7 | 6.6 | 2.9 | 24.5 | 36.1 | 55.2 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 3.4 | 0.0 | 16.6 | 25.2 | 56.3 | 6.8 | 2.9 | 23.6 | 42.9 | 62.4 | 11.6 | 11.6 |
| PostgreSQL | db | 297.1 | 305.6 | 327.6 | 336.6 | 345.2 | 400.0 | 400.0 | 400.0 | 400.0 | 400.0 | 111118.7 | 120619.0 |
| HAProxy | lb | 7.2 | 4.8 | 23.2 | 31.8 | 49.8 | 11.5 | 8.7 | 32.8 | 48.0 | 91.4 | 22.2 | 22.2 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-22T19:13:17Z*
