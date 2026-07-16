# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-16T00:50:28Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260716-013822` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.66 RPS (per instance) |
| **Total throughput** | 26.48 RPS (all instances) |
| **p50 latency** | 31386.62 ms |
| **p95 latency** | 48326.69 ms |
| **p99 latency** | 82141.88 ms |
| **p999 latency** | 105103.75 ms |
| **Error rate** | 58.00% (0.58) |
| **Total requests** | 59508 |
| **Failed requests** | 34748 |
| **Total successful** | 24760 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 59 |
| observed_postgres_backends_avg_numbackends | 55.96 |
| observed_postgres_backends_median_numbackends | 56 |
| observed_client_backends_active_median | 41189 |
| observed_client_backends_active_max | 61424 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.9% / 1.0% / 2.9% / 4.9% / 8.8% |
| OJP proxy-tier host_cpu (avg / peak) | 10.7% / 69.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 12.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 35.20 MiB / 35.20 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 16 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.9% / 1.0% / 2.9% / 4.9% / 8.8% |
| PgBouncer tier RSS (avg / peak, summed) | 35.20 MiB / 35.20 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.0% / 1.0% / 2.9% / 5.8% / 9.7% |
| HAProxy RSS (avg / peak, summed) | 23.10 MiB / 23.30 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.9% / 1.0% / 5.8% / 8.8% / 16.6% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 16.8% / 103.8% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 22.40% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 58.30 MiB / 58.50 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.03% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 25 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (48326.69 ms) |
| Error rate | < 0.1% | ❌ FAIL (58.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 61.62 RPS (all instances) |
| **Achieved throughput** | 26.48 RPS (all instances) |
| **Attempted − achieved gap** | 35.14 RPS (57.03%) |
| **Total attempted ops** | 57616 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 30818.303 | 47120.383 | 71368.703 | 1.7646945581097875 | 55.66% | 0.02501876407305479 | 1 |
| 10 | 31375.359 | 47022.079 | 74645.503 | 1.7133579891465938 | 56.99% | 0.02501876407305479 | 1 |
| 11 | 31342.591 | 46366.719 | 73531.391 | 1.665228174762328 | 58.18% | 0.02502815667626079 | 2 |
| 12 | 31784.959 | 48365.567 | 93126.655 | 1.529401950361816 | 61.61% | 0.025015634771732333 | 1 |
| 13 | 31227.903 | 47775.743 | 80871.423 | 1.7187037102396026 | 56.72% | 0.025031289111389236 | 2 |
| 14 | 31080.447 | 49676.287 | 91881.471 | 1.645978742382402 | 58.64% | 0.025015634771732333 | 2 |
| 15 | 31752.191 | 49741.823 | 91947.007 | 1.5796690074716098 | 60.38% | 0.02502815667626079 | 2 |
| 1 | 31703.039 | 50987.007 | 93126.655 | 1.5443734645836877 | 61.18% | 0.025031289111389236 | 1 |
| 2 | 31440.895 | 50069.503 | 94502.911 | 1.6673689794503992 | 58.11% | 0.025015634771732333 | 1 |
| 3 | 30785.535 | 48562.175 | 75366.399 | 1.7176360365601933 | 56.78% | 0.025031289111389236 | 2 |
| 4 | 31850.495 | 51740.671 | 79626.239 | 1.511220248854018 | 61.95% | 0.025015634771732333 | 1 |
| 5 | 31621.119 | 48431.103 | 94044.159 | 1.6812726335445976 | 57.66% | 0.025031289111389236 | 2 |
| 6 | 31440.895 | 49381.375 | 73465.855 | 1.5561380823886881 | 60.87% | 0.02501876407305479 | 2 |
| 7 | 30998.527 | 45547.519 | 70057.983 | 1.8427689234079783 | 53.63% | 0.025031289111389236 | 2 |
| 8 | 31358.975 | 45842.431 | 70516.735 | 1.719773220949148 | 56.72% | 0.02501876407305479 | 1 |
| 9 | 31604.735 | 46596.095 | 86179.839 | 1.623517257090054 | 59.17% | 0.025034422330704718 | 2 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 2071 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=116) |
| 10 | SQLTransientConnectionException | 2123 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=14, active=14, idle=0, waiting=109) |
| 11 | SQLTransientConnectionException | 2166 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=120) |
| 12 | SQLTransientConnectionException | 2295 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=120) |
| 13 | SQLTransientConnectionException | 2106 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=8, active=8, idle=0, waiting=118) |
| 14 | SQLTransientConnectionException | 2182 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=6, active=6, idle=0, waiting=120) |
| 15 | SQLTransientConnectionException | 2251 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=120) |
| 1 | SQLTransientConnectionException | 2276 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=5, active=5, idle=0, waiting=120) |
| 2 | SQLTransientConnectionException | 2163 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=120) |
| 3 | SQLTransientConnectionException | 2110 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=7, active=7, idle=0, waiting=115) |
| 4 | SQLTransientConnectionException | 2301 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=120) |
| 5 | SQLTransientConnectionException | 2141 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=6, active=6, idle=0, waiting=120) |
| 6 | SQLTransientConnectionException | 2263 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=6, active=6, idle=0, waiting=120) |
| 7 | SQLTransientConnectionException | 1993 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=120) |
| 8 | SQLTransientConnectionException | 2107 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=116) |
| 9 | SQLTransientConnectionException | 2200 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=110) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-16T00:50:28Z → 2026-07-16T01:05:28Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 56 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 41189 / 61424 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2685384530 | Cumulative since stats reset |
| Transactions rolled back | 1162 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 6509 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 459190 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-16T00:50:28Z → 2026-07-16T01:05:28Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.3 | 0.0 | 2.0 | 2.9 | 4.9 | 4.1 | 2.9 | 13.7 | 33.3 | 35.2 | 11.8 | 11.8 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.3 | 0.0 | 1.9 | 2.0 | 3.9 | 3.4 | 2.9 | 4.9 | 32.3 | 34.2 | 11.7 | 11.7 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.3 | 0.0 | 1.9 | 2.9 | 3.9 | 3.4 | 2.9 | 4.9 | 30.3 | 36.1 | 11.7 | 11.7 |
| PostgreSQL | db | 1421.3 | 1421.9 | 1528.1 | 1561.3 | 1575.6 | 1599.4 | 1599.5 | 1600.0 | 1600.0 | 1600.0 | 146228.9 | 152519.0 |
| HAProxy | lb | 1.0 | 1.0 | 2.9 | 5.8 | 9.7 | 6.2 | 3.9 | 29.3 | 35.0 | 44.8 | 23.1 | 23.3 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-16T01:09:47Z*
