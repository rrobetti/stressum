# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T08:13:49Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 2 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260715-090148` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.56 RPS (per instance) |
| **Total throughput** | 25.00 RPS (all instances) |
| **p50 latency** | 23133.25 ms |
| **p95 latency** | 40136.69 ms |
| **p99 latency** | 71729.38 ms |
| **p999 latency** | 100040.00 ms |
| **Error rate** | 19.00% (0.19) |
| **Total requests** | 28873 |
| **Failed requests** | 5564 |
| **Total successful** | 23309 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 60 |
| observed_postgres_backends_avg_numbackends | 55.98 |
| observed_postgres_backends_median_numbackends | 56 |
| observed_client_backends_active_median | 40427 |
| observed_client_backends_active_max | 59266 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.9% / 1.0% / 2.9% / 4.9% / 7.8% |
| OJP proxy-tier host_cpu (avg / peak) | 9.6% / 68.6% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 17.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 35.00 MiB / 35.00 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 16 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.9% / 1.0% / 2.9% / 4.9% / 7.8% |
| PgBouncer tier RSS (avg / peak, summed) | 35.00 MiB / 35.00 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.0% / 1.0% / 2.9% / 5.8% / 7.8% |
| HAProxy RSS (avg / peak, summed) | 23.00 MiB / 23.20 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.8% / 1.0% / 5.9% / 9.8% / 14.6% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 13.6% / 74.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 25.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 58.00 MiB / 58.20 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.03% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 26 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (40136.69 ms) |
| Error rate | < 0.1% | ❌ FAIL (19.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 30.91 RPS (all instances) |
| **Achieved throughput** | 25.00 RPS (all instances) |
| **Attempted − achieved gap** | 5.91 RPS (19.11%) |
| **Total attempted ops** | 28815 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 23789.567 | 40075.263 | 73596.927 | 1.5732485711352202 | 18.55% | 0.02501876407305479 | 1 |
| 10 | 22609.919 | 38797.311 | 65732.607 | 1.6598823964766003 | 13.83% | 0.025015634771732333 | 1 |
| 11 | 23281.663 | 39256.063 | 76021.759 | 1.5971191909071252 | 17.25% | 0.025025025025025023 | 1 |
| 12 | 25624.575 | 42827.775 | 73596.927 | 1.4984352055210917 | 22.35% | 0.02501719942239356 | 2 |
| 13 | 23085.055 | 40239.103 | 71696.383 | 1.5118688670734033 | 21.78% | 0.025021894157387717 | 1 |
| 14 | 26558.463 | 44859.391 | 77201.407 | 1.39671990567049 | 27.73% | 0.025015634771732333 | 2 |
| 15 | 26066.943 | 40402.943 | 72351.743 | 1.5189736955584303 | 21.85% | 0.025025025025025023 | 2 |
| 1 | 24526.847 | 39452.671 | 67698.687 | 1.5607633551682552 | 19.91% | 0.025025025025025023 | 2 |
| 2 | 22593.535 | 39911.423 | 69992.447 | 1.590809905255304 | 18.79% | 0.02501876407305479 | 2 |
| 3 | 22183.935 | 40370.175 | 79691.775 | 1.5871555904454089 | 17.74% | 0.025025025025025023 | 2 |
| 4 | 23904.255 | 39780.351 | 67895.295 | 1.5529295502600515 | 19.51% | 0.025015634771732333 | 2 |
| 5 | 20856.831 | 39747.583 | 73072.639 | 1.5876312498929446 | 17.88% | 0.025025025025025023 | 2 |
| 6 | 20725.759 | 38830.079 | 70123.519 | 1.5614873059638121 | 19.07% | 0.025015634771732333 | 2 |
| 7 | 20856.831 | 39059.455 | 73465.855 | 1.631765317219249 | 15.53% | 0.025025025025025023 | 2 |
| 8 | 21544.959 | 40009.727 | 70647.807 | 1.5631042928967385 | 19.35% | 0.02501876407305479 | 1 |
| 9 | 21921.791 | 38567.935 | 64880.639 | 1.610028113484875 | 17.19% | 0.025025025025025023 | 1 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 335 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=42) |
| 10 | SQLTransientConnectionException | 249 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=40) |
| 11 | SQLTransientConnectionException | 311 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=43) |
| 12 | SQLTransientConnectionException | 403 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=6, active=6, idle=0, waiting=43) |
| 13 | SQLTransientConnectionException | 393 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=42) |
| 14 | SQLTransientConnectionException | 500 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=44) |
| 15 | SQLTransientConnectionException | 394 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=6, active=6, idle=0, waiting=44) |
| 1 | SQLTransientConnectionException | 361 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=23) |
| 2 | SQLTransientConnectionException | 340 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=42) |
| 3 | SQLTransientConnectionException | 320 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=22) |
| 4 | SQLTransientConnectionException | 352 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=37) |
| 5 | SQLTransientConnectionException | 323 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=33) |
| 6 | SQLTransientConnectionException | 344 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=9, active=9, idle=0, waiting=33) |
| 7 | SQLTransientConnectionException | 280 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=41) |
| 8 | SQLTransientConnectionException | 349 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=8, active=8, idle=0, waiting=27) |
| 9 | SQLTransientConnectionException | 310 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=6, active=6, idle=0, waiting=38) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T08:13:49Z → 2026-07-15T08:28:49Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 56 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 40427 / 59266 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2596227722 | Cumulative since stats reset |
| Transactions rolled back | 1140 | Non-zero → contention or application errors |
| Temp file bytes written | 2 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4902 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 493490 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T08:13:49Z → 2026-07-15T08:28:49Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.3 | 0.0 | 1.0 | 2.9 | 6.9 | 3.2 | 2.9 | 4.9 | 32.4 | 34.3 | 11.7 | 11.7 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.3 | 0.0 | 1.9 | 2.9 | 5.9 | 3.6 | 2.9 | 5.8 | 32.3 | 34.3 | 11.6 | 11.6 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.3 | 0.0 | 1.9 | 2.9 | 4.9 | 3.0 | 2.9 | 4.9 | 6.8 | 33.2 | 11.7 | 11.7 |
| PostgreSQL | db | 1394.6 | 1421.6 | 1506.5 | 1534.5 | 1548.0 | 1573.9 | 1599.5 | 1600.0 | 1600.0 | 1600.0 | 145142.5 | 152781.0 |
| HAProxy | lb | 1.0 | 1.0 | 2.9 | 5.8 | 7.8 | 4.1 | 3.9 | 6.8 | 9.8 | 35.0 | 23.0 | 23.2 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T08:32:47Z*
