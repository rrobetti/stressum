# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-14T20:40:37Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260714-212837` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.97 RPS (per instance) |
| **Total throughput** | 15.44 RPS (all instances) |
| **p50 latency** | 4.29 ms |
| **p95 latency** | 15815.69 ms |
| **p99 latency** | 38421.62 ms |
| **p999 latency** | 63836.25 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 14441 |
| **Failed requests** | 2 |
| **Total successful** | 14439 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 58 |
| observed_postgres_backends_avg_numbackends | 51.51 |
| observed_postgres_backends_median_numbackends | 49 |
| observed_client_backends_active_median | 43134 |
| observed_client_backends_active_max | 66886 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.9% / 1.0% / 2.9% / 2.9% / 4.9% |
| OJP proxy-tier host_cpu (avg / peak) | 10.7% / 57.7% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 5.90% |
| OJP proxy-tier RSS (avg / peak, summed) | 35.00 MiB / 35.10 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 16 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.9% / 1.0% / 2.9% / 2.9% / 4.9% |
| PgBouncer tier RSS (avg / peak, summed) | 35.00 MiB / 35.10 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.0% / 1.0% / 2.9% / 3.9% / 5.8% |
| HAProxy RSS (avg / peak, summed) | 23.20 MiB / 23.40 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.9% / 1.9% / 4.9% / 5.8% / 9.8% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 15.1% / 59.6% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 11.70% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 58.20 MiB / 58.50 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.03% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 28 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (15815.69 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.42 RPS (all instances) |
| **Achieved throughput** | 15.44 RPS (all instances) |
| **Attempted − achieved gap** | -0.02 RPS (-0.16%) |
| **Total attempted ops** | 14414 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 4.299 | 12484.607 | 23281.663 | 0.9646996917666839 | 0.00% | 0.02501876407305479 | 1 |
| 10 | 4.799 | 15572.991 | 38830.079 | 0.9657681707195775 | 0.00% | 0.025021894157387717 | 2 |
| 11 | 3.977 | 16859.135 | 41943.039 | 0.9657681707195775 | 0.00% | 0.025025025025025023 | 1 |
| 12 | 4.419 | 17956.863 | 40927.231 | 0.968009686514609 | 0.00% | 0.02501876407305479 | 1 |
| 13 | 4.267 | 17268.735 | 43417.599 | 0.9668387154734837 | 0.00% | 0.02502815667626079 | 2 |
| 14 | 4.091 | 15081.471 | 39813.119 | 0.9657681707195775 | 0.00% | 0.02501876407305479 | 1 |
| 15 | 4.089 | 15515.647 | 39288.831 | 0.9668376814291231 | 0.00% | 0.02502815667626079 | 2 |
| 1 | 4.543 | 12992.511 | 25821.183 | 0.964697628255587 | 0.00% | 0.025025025025025023 | 2 |
| 2 | 4.063 | 14131.199 | 38764.543 | 0.964698660010032 | 0.00% | 0.025015634771732333 | 2 |
| 3 | 4.563 | 16908.287 | 37781.503 | 0.964697628255587 | 0.00% | 0.025025025025025023 | 2 |
| 4 | 4.175 | 16375.807 | 40337.407 | 0.964698660010032 | 0.00% | 0.02501876407305479 | 2 |
| 5 | 4.187 | 15515.647 | 40828.927 | 0.9636291493004866 | 0.00% | 0.02502815667626079 | 2 |
| 6 | 4.327 | 15876.095 | 42270.719 | 0.963630179913284 | 0.11% | 0.02501876407305479 | 2 |
| 7 | 4.343 | 17186.815 | 41451.519 | 0.964697628255587 | 0.00% | 0.02502815667626079 | 2 |
| 8 | 4.175 | 16400.383 | 41156.607 | 0.9636291493004866 | 0.11% | 0.02501876407305479 | 2 |
| 9 | 4.247 | 16924.671 | 38830.079 | 0.9646996917666839 | 0.00% | 0.02502815667626079 | 2 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 6 | SQLTransientConnectionException | 1 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=7, active=7, idle=0, waiting=10) |
| 8 | SQLTransientConnectionException | 1 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=5, active=5, idle=0, waiting=1) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-14T20:40:37Z → 2026-07-14T20:55:37Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 49 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 43134 / 66886 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1397482111 | Cumulative since stats reset |
| Transactions rolled back | 897 | Non-zero → contention or application errors |
| Temp file bytes written | 13 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -13 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 2185 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 220548 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-14T20:40:37Z → 2026-07-14T20:55:37Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.4 | 0.0 | 1.0 | 2.0 | 2.0 | 3.4 | 2.9 | 4.9 | 32.3 | 34.2 | 11.6 | 11.7 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.3 | 0.0 | 1.0 | 1.9 | 2.0 | 4.2 | 2.9 | 8.8 | 34.2 | 35.2 | 11.7 | 11.7 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.3 | 0.0 | 1.0 | 1.9 | 1.9 | 3.3 | 2.9 | 4.9 | 5.8 | 35.1 | 11.7 | 11.7 |
| PostgreSQL | db | 647.8 | 821.2 | 1236.3 | 1253.0 | 1294.6 | 1134.6 | 1429.7 | 1597.8 | 1598.8 | 1598.9 | 137769.7 | 151187.0 |
| HAProxy | lb | 1.0 | 1.0 | 2.9 | 3.9 | 5.8 | 4.6 | 3.9 | 6.8 | 24.2 | 44.7 | 23.2 | 23.4 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-14T20:59:40Z*
