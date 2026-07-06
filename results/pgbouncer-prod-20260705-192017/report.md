# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-05T18:32:04Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260705-192017` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.62 RPS (per instance) |
| **Total throughput** | 18.48 RPS (all instances) |
| **p50 latency** | 29941.75 ms |
| **p95 latency** | 39043.00 ms |
| **p99 latency** | 45916.25 ms |
| **p999 latency** | 62652.50 ms |
| **Error rate** | 61.00% (0.61) |
| **Total requests** | 44690 |
| **Failed requests** | 27438 |
| **Total successful** | 17252 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 18.55 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 26197 |
| observed_client_backends_active_max | 38145 |
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
| OJP proxy-tier host_cpu (avg / peak) | 15.8% / 151.4% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 13.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.30 MiB / 34.20 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 3.9% / 6.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.30 MiB / 34.20 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 3.9% / 5.8% |
| HAProxy RSS (avg / peak, summed) | 21.80 MiB / 21.80 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.2% / 1.0% / 3.9% / 6.8% / 11.7% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 19.6% / 155.3% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 19.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.10 MiB / 56.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.19% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 40 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (39043.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (61.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.29 RPS (all instances) |
| **Achieved throughput** | 18.48 RPS (all instances) |
| **Attempted − achieved gap** | 27.80 RPS (60.07%) |
| **Total attempted ops** | 43202 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29933.567 | 38928.383 | 45219.839 | 4.767233302101459 | 60.15% | 0.20020020020020018 | 11 |
| 1 | 29917.183 | 39059.455 | 45514.751 | 4.626510257269962 | 61.34% | 0.20020020020020018 | 9 |
| 2 | 29949.951 | 38764.543 | 46399.487 | 4.67152533873916 | 60.99% | 0.1503006012024048 | 10 |
| 3 | 29966.335 | 39419.903 | 46530.559 | 4.418701152765253 | 63.11% | 0.2004008016032064 | 10 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 6720 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=360) |
| 1 | SQLTransientConnectionException | 6852 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=360) |
| 2 | SQLTransientConnectionException | 6816 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=15, active=15, idle=0, waiting=360) |
| 3 | SQLTransientConnectionException | 7050 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=360) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-05T18:32:04Z → 2026-07-05T18:47:04Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 26197 / 38145 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 551565557 | Cumulative since stats reset |
| Transactions rolled back | 5117 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 8084 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 746583 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-05T18:32:04Z → 2026-07-05T18:47:04Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 4.9 | 9.7 | 3.0 | 33.2 | 35.3 | 118.2 | 11.5 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 3.3 | 2.9 | 4.9 | 32.5 | 34.3 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.9 | 4.9 | 3.1 | 2.0 | 3.9 | 32.4 | 34.1 | 11.4 | 11.4 |
| PostgreSQL | db | 300.4 | 300.7 | 354.2 | 361.0 | 370.2 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 14561.6 | 16527.2 |
| HAProxy | lb | 0.6 | 0.0 | 1.9 | 3.9 | 5.8 | 3.9 | 3.9 | 5.8 | 7.9 | 35.1 | 21.8 | 21.8 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-05T18:50:06Z*
