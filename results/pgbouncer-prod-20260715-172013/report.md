# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T16:32:08Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 3 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260715-172013` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.59 RPS (per instance) |
| **Total throughput** | 25.41 RPS (all instances) |
| **p50 latency** | 30108.62 ms |
| **p95 latency** | 48042.12 ms |
| **p99 latency** | 78540.62 ms |
| **p999 latency** | 104836.88 ms |
| **Error rate** | 47.00% (0.47) |
| **Total requests** | 44573 |
| **Failed requests** | 20816 |
| **Total successful** | 23757 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 60 |
| observed_postgres_backends_avg_numbackends | 55.93 |
| observed_postgres_backends_median_numbackends | 56 |
| observed_client_backends_active_median | 39771 |
| observed_client_backends_active_max | 60067 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.8% / 0.0% / 2.9% / 4.9% / 9.8% |
| OJP proxy-tier host_cpu (avg / peak) | 24.4% / 98.6% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 19.50% |
| OJP proxy-tier RSS (avg / peak, summed) | 35.20 MiB / 35.20 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 16 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.8% / 0.0% / 2.9% / 4.9% / 9.8% |
| PgBouncer tier RSS (avg / peak, summed) | 35.20 MiB / 35.20 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.0% / 1.0% / 2.9% / 5.8% / 10.7% |
| HAProxy RSS (avg / peak, summed) | 22.90 MiB / 23.00 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.8% / 1.0% / 5.8% / 9.8% / 18.5% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 29.0% / 102.5% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 30.20% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 58.10 MiB / 58.20 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.03% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 27 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (48042.12 ms) |
| Error rate | < 0.1% | ❌ FAIL (47.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.22 RPS (all instances) |
| **Achieved throughput** | 25.41 RPS (all instances) |
| **Attempted − achieved gap** | 20.81 RPS (45.03%) |
| **Total attempted ops** | 43215 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 30130.175 | 47546.367 | 73727.999 | 1.6064068038066066 | 46.26% | 0.025021894157387717 | 2 |
| 10 | 30081.023 | 46563.327 | 77463.551 | 1.5668348652308115 | 47.53% | 0.025021894157387717 | 1 |
| 11 | 29999.103 | 47972.351 | 76414.975 | 1.5593482822570124 | 47.63% | 0.025025025025025023 | 1 |
| 12 | 30081.023 | 46366.719 | 73727.999 | 1.5486531637230136 | 48.16% | 0.025021894157387717 | 1 |
| 13 | 29835.263 | 46006.271 | 73596.927 | 1.7582774869893885 | 41.20% | 0.025025025025025023 | 2 |
| 14 | 29802.495 | 45645.823 | 73203.711 | 1.6609501319241462 | 44.50% | 0.025021894157387717 | 1 |
| 15 | 30146.559 | 43352.063 | 77398.015 | 1.742231082514802 | 41.72% | 0.025025025025025023 | 2 |
| 1 | 29982.719 | 51445.759 | 85852.159 | 1.5219137396832323 | 48.46% | 0.025025025025025023 | 2 |
| 2 | 30523.391 | 50069.503 | 94896.127 | 1.5326088467786874 | 48.77% | 0.025021894157387717 | 1 |
| 3 | 30507.007 | 49446.911 | 85393.407 | 1.4566751443306247 | 50.90% | 0.02502815667626079 | 2 |
| 4 | 30277.631 | 49184.767 | 81657.855 | 1.503733665880219 | 49.41% | 0.025021894157387717 | 2 |
| 5 | 30130.175 | 50298.879 | 73531.391 | 1.547580341558575 | 47.80% | 0.025025025025025023 | 2 |
| 6 | 29556.735 | 47808.511 | 81461.247 | 1.7133579891465938 | 42.17% | 0.025021894157387717 | 2 |
| 7 | 30244.863 | 48365.567 | 75890.687 | 1.5358173789073237 | 48.23% | 0.025025025025025023 | 2 |
| 8 | 30310.399 | 49971.199 | 76152.831 | 1.554000722990013 | 48.00% | 0.025021894157387717 | 2 |
| 9 | 30130.175 | 48627.711 | 76283.903 | 1.5999880214800533 | 46.55% | 0.025025025025025023 | 2 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 1293 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=88) |
| 10 | SQLTransientConnectionException | 1327 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=88) |
| 11 | SQLTransientConnectionException | 1326 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=79) |
| 12 | SQLTransientConnectionException | 1345 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=6, active=6, idle=0, waiting=90) |
| 13 | SQLTransientConnectionException | 1152 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=90) |
| 14 | SQLTransientConnectionException | 1245 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=88) |
| 15 | SQLTransientConnectionException | 1166 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=88) |
| 1 | SQLTransientConnectionException | 1338 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=11, active=11, idle=0, waiting=68) |
| 2 | SQLTransientConnectionException | 1364 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=90) |
| 3 | SQLTransientConnectionException | 1412 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=66) |
| 4 | SQLTransientConnectionException | 1373 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=74) |
| 5 | SQLTransientConnectionException | 1325 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=13, active=13, idle=0, waiting=76) |
| 6 | SQLTransientConnectionException | 1168 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=82) |
| 7 | SQLTransientConnectionException | 1338 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=9, active=9, idle=0, waiting=65) |
| 8 | SQLTransientConnectionException | 1341 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=90) |
| 9 | SQLTransientConnectionException | 1303 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=89) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T16:32:08Z → 2026-07-15T16:47:08Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 56 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 39771 / 60067 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2760261402 | Cumulative since stats reset |
| Transactions rolled back | 1159 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5790 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 396578 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T16:32:08Z → 2026-07-15T16:47:08Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.3 | 0.0 | 2.0 | 2.9 | 6.8 | 3.2 | 2.9 | 4.9 | 33.2 | 45.1 | 11.7 | 11.7 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.3 | 0.0 | 1.0 | 2.9 | 7.8 | 10.1 | 3.9 | 33.3 | 47.9 | 71.2 | 11.8 | 11.8 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.3 | 0.0 | 1.9 | 2.9 | 4.9 | 11.6 | 3.9 | 34.2 | 43.9 | 54.7 | 11.7 | 11.7 |
| PostgreSQL | db | 1428.6 | 1433.4 | 1514.8 | 1541.3 | 1588.3 | 1599.4 | 1599.5 | 1600.0 | 1600.0 | 1600.0 | 146559.4 | 152918.0 |
| HAProxy | lb | 1.0 | 1.0 | 2.9 | 5.8 | 10.7 | 4.8 | 3.9 | 7.8 | 34.0 | 36.2 | 22.9 | 23.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T16:51:08Z*
