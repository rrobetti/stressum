# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T18:12:16Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260715-190015` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.65 RPS (per instance) |
| **Total throughput** | 26.35 RPS (all instances) |
| **p50 latency** | 31346.62 ms |
| **p95 latency** | 48250.81 ms |
| **p99 latency** | 82395.00 ms |
| **p999 latency** | 105307.50 ms |
| **Error rate** | 59.00% (0.59) |
| **Total requests** | 59560 |
| **Failed requests** | 34919 |
| **Total successful** | 24641 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 60 |
| observed_postgres_backends_avg_numbackends | 55.99 |
| observed_postgres_backends_median_numbackends | 56 |
| observed_client_backends_active_median | 39808 |
| observed_client_backends_active_max | 59462 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | pgbouncer-prod |
| Configured replicas | 16 |
| Configured client pool size (per replica) | 20 |
| OJP servers | N/A |
| Real DB connections per OJP server | N/A |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.8% / 1.0% / 2.9% / 4.9% / 8.8% |
| OJP proxy-tier host_cpu (avg / peak) | 24.2% / 103.7% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 13.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.90 MiB / 35.20 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 16 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.8% / 1.0% / 2.9% / 4.9% / 8.8% |
| PgBouncer tier RSS (avg / peak, summed) | 34.90 MiB / 35.20 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.0% / 1.0% / 2.9% / 4.9% / 9.7% |
| HAProxy RSS (avg / peak, summed) | 23.00 MiB / 23.10 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.8% / 1.0% / 5.8% / 7.8% / 14.6% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 28.6% / 107.6% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 23.40% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 57.90 MiB / 58.30 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.03% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 27 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (48250.81 ms) |
| Error rate | < 0.1% | ❌ FAIL (59.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 61.62 RPS (all instances) |
| **Achieved throughput** | 26.35 RPS (all instances) |
| **Attempted − achieved gap** | 35.27 RPS (57.23%) |
| **Total attempted ops** | 57614 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 31211.519 | 49381.375 | 74842.111 | 1.6384904070236908 | 58.82% | 0.025015634771732333 | 2 |
| 10 | 31473.663 | 50659.327 | 76611.583 | 1.6245867677995995 | 59.19% | 0.02501876407305479 | 1 |
| 11 | 31457.279 | 47579.135 | 74448.895 | 1.6203069920257367 | 59.29% | 0.02502815667626079 | 2 |
| 12 | 31604.735 | 45940.735 | 70778.879 | 1.7101476245632388 | 57.13% | 0.02501876407305479 | 2 |
| 13 | 31506.431 | 49053.695 | 73269.247 | 1.7486518803087896 | 56.12% | 0.025031289111389236 | 2 |
| 14 | 30949.375 | 43876.351 | 70778.879 | 1.8737827631236987 | 53.02% | 0.025015634771732333 | 1 |
| 15 | 31801.343 | 48496.639 | 96862.207 | 1.4523939902118483 | 63.51% | 0.025037556334501748 | 2 |
| 1 | 31539.199 | 50987.007 | 95813.631 | 1.459882118529594 | 63.27% | 0.02502815667626079 | 1 |
| 2 | 31309.823 | 52658.175 | 94765.055 | 1.6267275290212042 | 59.12% | 0.025015634771732333 | 2 |
| 3 | 31358.975 | 47251.455 | 80740.351 | 1.5935709572227803 | 59.97% | 0.025031289111389236 | 2 |
| 4 | 31326.207 | 44859.391 | 69468.159 | 1.6470500157753167 | 58.64% | 0.025015634771732333 | 1 |
| 5 | 30916.607 | 46989.311 | 92733.439 | 1.7582756064927858 | 55.88% | 0.02502815667626079 | 2 |
| 6 | 31440.895 | 49741.823 | 96731.135 | 1.6331428534759633 | 58.91% | 0.02501876407305479 | 1 |
| 7 | 31031.295 | 49512.447 | 75628.543 | 1.5925014465132348 | 60.02% | 0.025025025025025023 | 2 |
| 8 | 31440.895 | 47546.367 | 95682.559 | 1.7048018943193948 | 57.14% | 0.02501876407305479 | 2 |
| 9 | 31178.751 | 47480.831 | 79167.487 | 1.66950621760051 | 58.07% | 0.02502815667626079 | 2 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 2188 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=120) |
| 10 | SQLTransientConnectionException | 2203 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=115) |
| 11 | SQLTransientConnectionException | 2206 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=119) |
| 12 | SQLTransientConnectionException | 2131 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=119) |
| 13 | SQLTransientConnectionException | 2091 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=10, active=10, idle=0, waiting=120) |
| 14 | SQLTransientConnectionException | 1977 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=120) |
| 15 | SQLTransientConnectionException | 2364 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=119) |
| 1 | SQLTransientConnectionException | 2351 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=6, active=6, idle=0, waiting=120) |
| 2 | SQLTransientConnectionException | 2200 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=113) |
| 3 | SQLTransientConnectionException | 2232 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=120) |
| 4 | SQLTransientConnectionException | 2183 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=120) |
| 5 | SQLTransientConnectionException | 2082 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=9, active=9, idle=0, waiting=120) |
| 6 | SQLTransientConnectionException | 2189 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=120) |
| 7 | SQLTransientConnectionException | 2235 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=120) |
| 8 | SQLTransientConnectionException | 2125 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=120) |
| 9 | SQLTransientConnectionException | 2162 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=120) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T18:12:16Z → 2026-07-15T18:27:16Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 56 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 39808 / 59462 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2692241982 | Cumulative since stats reset |
| Transactions rolled back | 1106 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 6214 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 437626 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T18:12:16Z → 2026-07-15T18:27:16Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.3 | 0.0 | 2.0 | 2.9 | 3.9 | 3.3 | 2.9 | 4.9 | 32.3 | 34.2 | 11.6 | 11.7 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.3 | 0.0 | 1.9 | 2.9 | 5.9 | 9.9 | 3.9 | 33.3 | 39.1 | 67.4 | 11.7 | 11.8 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.3 | 0.0 | 1.9 | 2.9 | 3.9 | 11.6 | 3.9 | 34.2 | 40.0 | 59.7 | 11.6 | 11.7 |
| PostgreSQL | db | 1421.4 | 1421.2 | 1512.9 | 1535.8 | 1544.9 | 1599.4 | 1599.5 | 1600.0 | 1600.0 | 1600.0 | 146511.6 | 153293.0 |
| HAProxy | lb | 1.0 | 1.0 | 2.9 | 4.9 | 9.7 | 4.5 | 3.9 | 6.8 | 33.2 | 37.1 | 23.0 | 23.1 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T18:31:15Z*
