# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-31T01:22:57Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260531-021001` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.14 RPS (per instance) |
| **Total throughput** | 2.28 RPS (all instances) |
| **p50 latency** | 28655.65 ms |
| **p95 latency** | 60031.00 ms |
| **p99 latency** | 60031.00 ms |
| **p999 latency** | 66060.50 ms |
| **Error rate** | 79.00% (0.79) |
| **Total requests** | 14899 |
| **Failed requests** | 11812 |
| **Total successful** | 3087 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 25 |
| observed_postgres_backends_avg_numbackends | 21.48 |
| observed_postgres_backends_median_numbackends | 23 |
| observed_client_backends_active_median | 14993 |
| observed_client_backends_active_max | 20741 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.1% / 0.0% / 1.0% / 2.0% / 2.9% |
| OJP proxy-tier host_cpu (avg / peak) | 14.1% / 96.1% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 6.90% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.30 MiB / 34.30 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 5 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.1% / 0.0% / 1.0% / 2.0% / 2.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.30 MiB / 34.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.1% / 0.0% / 1.0% / 1.9% / 2.9% |
| HAProxy RSS (avg / peak, summed) | 22.00 MiB / 22.00 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.3% / 0.0% / 1.9% / 2.9% / 5.8% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 17.3% / 98.0% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 9.80% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.30 MiB / 56.30 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.15% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 13 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (60031.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (79.00%) |

## Open-Loop Sanity (2/2 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 10.63 RPS (all instances) |
| **Achieved throughput** | 2.28 RPS (all instances) |
| **Attempted − achieved gap** | 8.35 RPS (78.57%) |
| **Total attempted ops** | 19202 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.21 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 28819.455 | 60030.975 | 60030.975 | 0.9778503970072613 | 82.21% | 0.15022533800701052 | 7 |
| 1 | 28491.775 | 60030.975 | 60030.975 | 1.3003574876089659 | 76.35% | 0.15 | 6 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 6125 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=240) |
| 1 | SQLTransientConnectionException | 5687 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=240) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-31T01:22:57Z → 2026-05-31T01:37:57Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 23 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 14993 / 20741 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 472481791 | Cumulative since stats reset |
| Transactions rolled back | 950 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 3464 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 354617 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-31T01:22:57Z → 2026-05-31T01:37:57Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.1 | 0.0 | 0.0 | 1.0 | 2.0 | 3.7 | 2.0 | 11.8 | 33.3 | 93.1 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.1 | 0.0 | 0.0 | 1.0 | 2.0 | 2.5 | 2.0 | 3.0 | 6.9 | 33.2 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.1 | 0.0 | 0.0 | 1.0 | 2.9 | 8.2 | 2.9 | 32.5 | 45.1 | 49.0 | 11.4 | 11.4 |
| PostgreSQL | db | 202.5 | 203.3 | 223.2 | 229.1 | 237.7 | 400.0 | 400.0 | 400.0 | 400.0 | 400.0 | 42527.4 | 48503.9 |
| HAProxy | lb | 0.1 | 0.0 | 1.0 | 1.9 | 2.9 | 3.2 | 2.9 | 3.9 | 4.9 | 12.6 | 22.0 | 22.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-31T01:40:57Z*
