# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-30T23:42:41Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260531-003012` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.19 RPS (per instance) |
| **Total throughput** | 2.39 RPS (all instances) |
| **p50 latency** | 28712.95 ms |
| **p95 latency** | 60031.00 ms |
| **p99 latency** | 60031.00 ms |
| **p999 latency** | 61063.00 ms |
| **Error rate** | 78.00% (0.78) |
| **Total requests** | 14898 |
| **Failed requests** | 11664 |
| **Total successful** | 3234 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 25 |
| observed_postgres_backends_avg_numbackends | 21.33 |
| observed_postgres_backends_median_numbackends | 23 |
| observed_client_backends_active_median | 14846 |
| observed_client_backends_active_max | 20903 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.2% / 0.0% / 1.0% / 2.0% / 3.9% |
| OJP proxy-tier host_cpu (avg / peak) | 14.2% / 100.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 6.90% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.40 MiB / 34.40 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 5 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.2% / 0.0% / 1.0% / 2.0% / 3.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.40 MiB / 34.40 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.1% / 0.0% / 1.0% / 1.9% / 2.9% |
| HAProxy RSS (avg / peak, summed) | 22.10 MiB / 22.20 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.3% / 0.0% / 1.9% / 2.9% / 4.9% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 17.9% / 104.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 9.80% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.50 MiB / 56.60 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.15% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 16 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (60031.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (78.00%) |

## Open-Loop Sanity (2/2 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 10.63 RPS (all instances) |
| **Achieved throughput** | 2.39 RPS (all instances) |
| **Attempted − achieved gap** | 8.24 RPS (77.54%) |
| **Total attempted ops** | 19202 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.27 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 28737.535 | 60030.975 | 60030.975 | 1.0560784287678422 | 80.79% | 0.15015015015015015 | 8 |
| 1 | 28688.383 | 60030.975 | 60030.975 | 1.3306155222241576 | 75.79% | 0.15 | 8 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 6019 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=240) |
| 1 | SQLTransientConnectionException | 5645 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=240) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-30T23:42:41Z → 2026-05-30T23:57:41Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 23 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 14846 / 20903 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 492614015 | Cumulative since stats reset |
| Transactions rolled back | 969 | Non-zero → contention or application errors |
| Temp file bytes written | 1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 3428 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 350835 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-30T23:42:41Z → 2026-05-30T23:57:41Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.1 | 0.0 | 1.0 | 1.0 | 2.0 | 2.7 | 2.0 | 3.0 | 31.5 | 34.3 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.0 | 0.0 | 0.0 | 1.0 | 2.9 | 2.9 | 2.0 | 3.0 | 32.4 | 34.1 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.1 | 0.0 | 1.0 | 1.0 | 2.0 | 8.9 | 2.9 | 33.3 | 48.0 | 63.7 | 11.5 | 11.5 |
| PostgreSQL | db | 203.2 | 205.8 | 234.5 | 248.6 | 262.3 | 400.0 | 400.0 | 400.0 | 400.0 | 400.0 | 43472.1 | 49000.3 |
| HAProxy | lb | 0.1 | 0.0 | 1.0 | 1.9 | 2.9 | 3.8 | 2.9 | 4.8 | 33.0 | 34.8 | 22.1 | 22.2 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-31T00:00:38Z*
