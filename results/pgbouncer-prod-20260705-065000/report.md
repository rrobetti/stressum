# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-05T06:01:49Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260705-065000` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.46 RPS (per instance) |
| **Total throughput** | 17.84 RPS (all instances) |
| **p50 latency** | 29466.50 ms |
| **p95 latency** | 38453.25 ms |
| **p99 latency** | 44941.50 ms |
| **p999 latency** | 61882.50 ms |
| **Error rate** | 44.00% (0.44) |
| **Total requests** | 29785 |
| **Failed requests** | 13106 |
| **Total successful** | 16679 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 18.53 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 23540 |
| observed_client_backends_active_max | 34825 |
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
| OJP proxy-tier host_cpu (avg / peak) | 10.0% / 104.9% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 10.80% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.20 MiB / 34.20 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 3.9% / 5.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.20 MiB / 34.20 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 3.9% / 4.9% |
| HAProxy RSS (avg / peak, summed) | 22.30 MiB / 22.30 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.2% / 1.0% / 3.9% / 5.8% / 9.8% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 13.8% / 107.8% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 15.70% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.50 MiB / 56.50 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.15% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 42 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (38453.25 ms) |
| Error rate | < 0.1% | ❌ FAIL (44.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 30.81 RPS (all instances) |
| **Achieved throughput** | 17.84 RPS (all instances) |
| **Attempted − achieved gap** | 12.97 RPS (42.09%) |
| **Total attempted ops** | 28804 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29442.047 | 38174.719 | 44466.175 | 4.549849407899241 | 42.86% | 0.15 | 10 |
| 1 | 29556.735 | 38502.399 | 44367.871 | 4.33920450413064 | 45.51% | 0.1503006012024048 | 11 |
| 2 | 29278.207 | 38240.255 | 45383.679 | 4.5946180082074255 | 42.30% | 0.15007503751875936 | 9 |
| 3 | 29589.503 | 38895.615 | 45547.519 | 4.355038293749044 | 45.33% | 0.1503006012024048 | 12 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 3191 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=12, active=12, idle=0, waiting=239) |
| 1 | SQLTransientConnectionException | 3389 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=240) |
| 2 | SQLTransientConnectionException | 3149 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=12, active=12, idle=0, waiting=236) |
| 3 | SQLTransientConnectionException | 3377 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=238) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-05T06:01:49Z → 2026-07-05T06:16:49Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 23540 / 34825 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 540183459 | Cumulative since stats reset |
| Transactions rolled back | 5060 | Non-zero → contention or application errors |
| Temp file bytes written | -1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 6844 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 699126 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-05T06:01:49Z → 2026-07-05T06:16:49Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 3.9 | 2.9 | 7.9 | 33.3 | 95.6 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 4.9 | 2.9 | 2.9 | 4.8 | 31.2 | 33.3 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 2.0 | 3.5 | 2.0 | 4.9 | 32.4 | 99.0 | 11.4 | 11.4 |
| PostgreSQL | db | 275.7 | 275.2 | 328.2 | 337.8 | 344.5 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 15524.5 | 17186.0 |
| HAProxy | lb | 0.6 | 0.0 | 1.9 | 3.9 | 4.9 | 3.8 | 3.9 | 5.8 | 7.8 | 35.8 | 22.3 | 22.3 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-05T06:19:50Z*
