# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T23:10:44Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260715-235841` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.65 RPS (per instance) |
| **Total throughput** | 26.46 RPS (all instances) |
| **p50 latency** | 31589.25 ms |
| **p95 latency** | 48807.94 ms |
| **p99 latency** | 82780.00 ms |
| **p999 latency** | 105492.50 ms |
| **Error rate** | 58.00% (0.58) |
| **Total requests** | 59533 |
| **Failed requests** | 34790 |
| **Total successful** | 24743 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 59 |
| observed_postgres_backends_avg_numbackends | 55.90 |
| observed_postgres_backends_median_numbackends | 56 |
| observed_client_backends_active_median | 40261 |
| observed_client_backends_active_max | 60556 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.8% / 1.0% / 2.9% / 4.9% / 9.8% |
| OJP proxy-tier host_cpu (avg / peak) | 10.4% / 45.0% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 16.60% |
| OJP proxy-tier RSS (avg / peak, summed) | 35.30 MiB / 35.30 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 16 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.8% / 1.0% / 2.9% / 4.9% / 9.8% |
| PgBouncer tier RSS (avg / peak, summed) | 35.30 MiB / 35.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.0% / 1.0% / 2.9% / 5.8% / 8.8% |
| HAProxy RSS (avg / peak, summed) | 23.30 MiB / 23.40 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.8% / 1.0% / 5.8% / 8.8% / 17.6% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 14.8% / 49.9% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 25.40% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 58.60 MiB / 58.70 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.03% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 26 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (48807.94 ms) |
| Error rate | < 0.1% | ❌ FAIL (58.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 61.62 RPS (all instances) |
| **Achieved throughput** | 26.46 RPS (all instances) |
| **Attempted − achieved gap** | 35.16 RPS (57.06%) |
| **Total attempted ops** | 57615 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 31850.495 | 52232.191 | 96010.239 | 1.502664154026819 | 62.14% | 0.025021894157387717 | 1 |
| 10 | 31588.351 | 48168.959 | 75825.151 | 1.629934321347327 | 59.07% | 0.025025025025025023 | 2 |
| 11 | 31244.287 | 46956.543 | 75497.471 | 1.7165646888205115 | 56.97% | 0.025025025025025023 | 2 |
| 12 | 31244.287 | 48791.551 | 94437.375 | 1.7561365850736947 | 55.92% | 0.025021894157387717 | 1 |
| 13 | 31588.351 | 47611.903 | 90898.431 | 1.665228174762328 | 58.17% | 0.02502815667626079 | 2 |
| 14 | 31621.119 | 46497.791 | 74776.575 | 1.7048000710155111 | 57.25% | 0.025025025025025023 | 1 |
| 15 | 31866.879 | 48955.391 | 92471.295 | 1.678064097984398 | 57.85% | 0.025025025025025023 | 2 |
| 1 | 31916.031 | 52363.263 | 74317.823 | 1.5572092585502126 | 60.88% | 0.025025025025025023 | 2 |
| 2 | 31997.951 | 50528.255 | 72220.671 | 1.5711112323223249 | 60.30% | 0.025021894157387717 | 2 |
| 3 | 31719.423 | 48168.959 | 72089.599 | 1.6331446001416035 | 58.90% | 0.025025025025025023 | 2 |
| 4 | 31653.887 | 49250.303 | 70582.271 | 1.6588111105050551 | 58.35% | 0.025025025025025023 | 1 |
| 5 | 31965.183 | 51740.671 | 87228.415 | 1.5871538929655074 | 60.11% | 0.025025025025025023 | 2 |
| 6 | 31670.271 | 46039.039 | 95289.343 | 1.7005238469057953 | 57.30% | 0.025025025025025023 | 1 |
| 7 | 31145.983 | 48791.551 | 77660.159 | 1.7518604158689892 | 56.04% | 0.02502815667626079 | 2 |
| 8 | 31113.215 | 46727.167 | 80412.671 | 1.655600807693624 | 58.42% | 0.025021894157387717 | 2 |
| 9 | 31244.287 | 48103.423 | 94765.055 | 1.6941049639200563 | 57.38% | 0.025021894157387717 | 1 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 2306 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=109) |
| 10 | SQLTransientConnectionException | 2199 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=5, active=5, idle=0, waiting=120) |
| 11 | SQLTransientConnectionException | 2125 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=119) |
| 12 | SQLTransientConnectionException | 2083 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=119) |
| 13 | SQLTransientConnectionException | 2165 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=120) |
| 14 | SQLTransientConnectionException | 2135 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=13, active=13, idle=0, waiting=118) |
| 15 | SQLTransientConnectionException | 2153 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=120) |
| 1 | SQLTransientConnectionException | 2266 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=115) |
| 2 | SQLTransientConnectionException | 2231 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=97) |
| 3 | SQLTransientConnectionException | 2188 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=120) |
| 4 | SQLTransientConnectionException | 2173 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=120) |
| 5 | SQLTransientConnectionException | 2236 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=114) |
| 6 | SQLTransientConnectionException | 2134 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=120) |
| 7 | SQLTransientConnectionException | 2088 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=120) |
| 8 | SQLTransientConnectionException | 2175 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=5, active=5, idle=0, waiting=120) |
| 9 | SQLTransientConnectionException | 2133 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=117) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T23:10:44Z → 2026-07-15T23:25:44Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 56 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 40261 / 60556 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2718826766 | Cumulative since stats reset |
| Transactions rolled back | 1151 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 6254 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 435349 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T23:10:44Z → 2026-07-15T23:25:44Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.3 | 0.0 | 2.0 | 2.9 | 4.9 | 3.3 | 2.9 | 4.9 | 32.4 | 34.4 | 11.7 | 11.7 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.3 | 0.0 | 1.9 | 2.9 | 4.9 | 3.6 | 2.9 | 4.9 | 33.2 | 36.2 | 11.8 | 11.8 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.3 | 0.0 | 1.0 | 2.0 | 6.8 | 3.7 | 2.9 | 5.8 | 32.2 | 34.2 | 11.8 | 11.8 |
| PostgreSQL | db | 1425.9 | 1432.3 | 1505.4 | 1533.8 | 1545.7 | 1599.5 | 1599.5 | 1600.0 | 1600.0 | 1600.0 | 146851.2 | 152677.0 |
| HAProxy | lb | 1.0 | 1.0 | 2.9 | 5.8 | 8.8 | 4.5 | 3.9 | 6.9 | 32.2 | 37.9 | 23.3 | 23.4 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T23:29:52Z*
