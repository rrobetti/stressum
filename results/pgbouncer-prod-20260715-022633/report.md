# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T01:38:28Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 2 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260715-022633` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.35 RPS (per instance) |
| **Total throughput** | 21.65 RPS (all instances) |
| **p50 latency** | 26086.44 ms |
| **p95 latency** | 46723.06 ms |
| **p99 latency** | 84893.75 ms |
| **p999 latency** | 120332.50 ms |
| **Error rate** | 31.00% (0.31) |
| **Total requests** | 29316 |
| **Failed requests** | 9091 |
| **Total successful** | 20225 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 58 |
| observed_postgres_backends_avg_numbackends | 55.32 |
| observed_postgres_backends_median_numbackends | 56 |
| observed_client_backends_active_median | 35283 |
| observed_client_backends_active_max | 52489 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.7% / 0.0% / 2.9% / 4.9% / 8.8% |
| OJP proxy-tier host_cpu (avg / peak) | 11.5% / 69.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 19.60% |
| OJP proxy-tier RSS (avg / peak, summed) | 35.00 MiB / 35.00 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 16 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.7% / 0.0% / 2.9% / 4.9% / 8.8% |
| PgBouncer tier RSS (avg / peak, summed) | 35.00 MiB / 35.00 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.8% / 0.0% / 2.9% / 5.8% / 11.7% |
| HAProxy RSS (avg / peak, summed) | 23.10 MiB / 23.20 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.5% / 1.0% / 5.8% / 9.7% / 17.5% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 15.8% / 74.3% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 31.30% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 58.10 MiB / 58.20 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.03% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 28 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (46723.06 ms) |
| Error rate | < 0.1% | ❌ FAIL (31.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 30.85 RPS (all instances) |
| **Achieved throughput** | 21.65 RPS (all instances) |
| **Attempted − achieved gap** | 9.20 RPS (29.81%) |
| **Total attempted ops** | 28815 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 26836.991 | 48758.783 | 92798.975 | 1.291968937130952 | 33.70% | 0.025015634771732333 | 1 |
| 10 | 25411.583 | 46465.023 | 83689.471 | 1.3090797084089119 | 33.30% | 0.025015634771732333 | 1 |
| 11 | 25460.735 | 44892.159 | 79560.703 | 1.4132585627634375 | 28.58% | 0.025021894157387717 | 2 |
| 12 | 23986.175 | 47022.079 | 84017.151 | 1.4031965501899448 | 28.85% | 0.025015634771732333 | 2 |
| 13 | 25493.503 | 46268.415 | 83689.471 | 1.3433054511891356 | 31.52% | 0.025021894157387717 | 2 |
| 14 | 27426.815 | 43548.671 | 81395.711 | 1.3796688153136822 | 29.62% | 0.025015634771732333 | 2 |
| 15 | 26574.847 | 45121.535 | 94502.911 | 1.3518615368654994 | 31.27% | 0.02501876407305479 | 2 |
| 1 | 27885.567 | 48857.087 | 101974.015 | 1.2834142240798456 | 34.10% | 0.02501876407305479 | 2 |
| 2 | 25559.039 | 48758.783 | 91095.039 | 1.359397194649824 | 30.66% | 0.02501876407305479 | 1 |
| 3 | 25870.335 | 47841.279 | 90243.071 | 1.3101520204148422 | 32.80% | 0.02501876407305479 | 2 |
| 4 | 26722.303 | 49577.983 | 75431.935 | 1.303734949294443 | 33.42% | 0.025015634771732333 | 2 |
| 5 | 26247.167 | 45514.751 | 75694.079 | 1.405665367946323 | 28.77% | 0.02501876407305479 | 1 |
| 6 | 23838.719 | 47284.223 | 87359.487 | 1.4074760937618649 | 27.97% | 0.025015634771732333 | 2 |
| 7 | 27426.815 | 46465.023 | 74055.679 | 1.3048030656454979 | 33.48% | 0.02501876407305479 | 2 |
| 8 | 26476.543 | 44630.015 | 74973.183 | 1.4051079807771782 | 28.70% | 0.025015634771732333 | 1 |
| 9 | 26165.247 | 46563.327 | 87818.239 | 1.3807368493103802 | 29.49% | 0.02501876407305479 | 3 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 614 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=49) |
| 10 | SQLTransientConnectionException | 611 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=6, active=6, idle=0, waiting=44) |
| 11 | SQLTransientConnectionException | 525 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=4, active=4, idle=0, waiting=50) |
| 12 | SQLTransientConnectionException | 532 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=33) |
| 13 | SQLTransientConnectionException | 578 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=4, active=4, idle=0, waiting=51) |
| 14 | SQLTransientConnectionException | 543 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=28) |
| 15 | SQLTransientConnectionException | 575 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=9, active=9, idle=0, waiting=44) |
| 1 | SQLTransientConnectionException | 621 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=5, active=5, idle=0, waiting=41) |
| 2 | SQLTransientConnectionException | 561 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=43) |
| 3 | SQLTransientConnectionException | 598 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=5, active=5, idle=0, waiting=38) |
| 4 | SQLTransientConnectionException | 612 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=4, active=4, idle=0, waiting=40) |
| 5 | SQLTransientConnectionException | 529 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=7, active=7, idle=0, waiting=27) |
| 6 | SQLTransientConnectionException | 511 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=7, active=7, idle=0, waiting=38) |
| 7 | SQLTransientConnectionException | 614 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=39) |
| 8 | SQLTransientConnectionException | 527 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=28) |
| 9 | SQLTransientConnectionException | 540 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=4, active=4, idle=0, waiting=44) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T01:38:28Z → 2026-07-15T01:53:28Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 56 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 35283 / 52489 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2173754700 | Cumulative since stats reset |
| Transactions rolled back | 998 | Non-zero → contention or application errors |
| Temp file bytes written | -1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4552 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 459187 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T01:38:28Z → 2026-07-15T01:53:28Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.3 | 0.0 | 1.0 | 3.9 | 5.9 | 4.7 | 2.9 | 26.5 | 34.2 | 39.3 | 11.7 | 11.7 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.9 | 8.8 | 3.6 | 2.9 | 5.8 | 32.4 | 34.3 | 11.6 | 11.6 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.9 | 4.9 | 3.5 | 2.9 | 4.9 | 33.2 | 34.2 | 11.7 | 11.7 |
| PostgreSQL | db | 1166.6 | 1169.3 | 1236.8 | 1249.8 | 1257.9 | 1598.5 | 1598.5 | 1599.1 | 1599.2 | 1599.3 | 149046.3 | 155368.0 |
| HAProxy | lb | 0.8 | 0.0 | 2.9 | 5.8 | 11.7 | 4.5 | 3.9 | 7.8 | 33.2 | 36.1 | 23.1 | 23.2 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T01:57:25Z*
