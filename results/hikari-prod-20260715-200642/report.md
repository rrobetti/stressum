# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T19:18:30Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260715-200642` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.37 RPS (per instance) |
| **Total throughput** | 21.89 RPS (all instances) |
| **p50 latency** | 24914.00 ms |
| **p95 latency** | 150264.38 ms |
| **p99 latency** | 388317.50 ms |
| **p999 latency** | 439780.00 ms |
| **Error rate** | 66.00% (0.66) |
| **Total requests** | 59408 |
| **Failed requests** | 38941 |
| **Total successful** | 20467 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 300 |
| observed_postgres_backends_max_numbackends | 316 |
| observed_postgres_backends_avg_numbackends | 312.96 |
| observed_postgres_backends_median_numbackends | 313 |
| observed_client_backends_active_median | 32923 |
| observed_client_backends_active_max | 49477 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | hikari-prod |
| Configured replicas | 16 |
| Configured client pool size (per replica) | 19 |
| OJP servers | N/A |
| Real DB connections per OJP server | N/A |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| OJP proxy-tier host_cpu (avg / peak) | N/A% / N/A% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 0% |
| OJP proxy-tier RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| PgBouncer tier RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | N/A% / N/A% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 0.00% |
| Total PgBouncer proxy-tier RSS (avg / peak) | N/A MiB / 0.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.03% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 0 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (150264.38 ms) |
| Error rate | < 0.1% | ❌ FAIL (66.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 61.69 RPS (all instances) |
| **Achieved throughput** | 21.89 RPS (all instances) |
| **Attempted − achieved gap** | 39.80 RPS (64.52%) |
| **Total attempted ops** | 57613 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 24559.615 | 137756.671 | 374865.919 | 1.5967811971260077 | 59.64% | 0.02502815667626079 | 0 |
| 10 | 24608.767 | 149159.935 | 390070.271 | 1.3967824805402318 | 64.90% | 0.02502815667626079 | 0 |
| 11 | 24559.615 | 149553.151 | 384565.247 | 1.4245897887286285 | 64.24% | 0.025025025025025023 | 0 |
| 12 | 24002.559 | 144834.559 | 391905.279 | 1.4053385753674308 | 64.70% | 0.025025025025025023 | 0 |
| 13 | 25231.359 | 140378.111 | 378273.791 | 1.421381253168429 | 64.28% | 0.025021894157387717 | 0 |
| 14 | 24346.623 | 155713.535 | 405798.911 | 1.2994569018808435 | 67.06% | 0.025025025025025023 | 0 |
| 15 | 26017.791 | 168427.519 | 404226.047 | 1.1743227590809482 | 70.44% | 0.025025025025025023 | 0 |
| 1 | 26116.095 | 161742.847 | 382468.095 | 1.3144286620314074 | 66.97% | 0.02502815667626079 | 0 |
| 2 | 23625.727 | 137232.383 | 375390.207 | 1.529401950361816 | 61.52% | 0.025025025025025023 | 0 |
| 3 | 24788.991 | 149684.223 | 378011.647 | 1.3743212617659548 | 65.42% | 0.025021894157387717 | 0 |
| 4 | 23838.719 | 139722.751 | 404226.047 | 1.3882263857130328 | 65.13% | 0.025025025025025023 | 0 |
| 5 | 25116.671 | 149684.223 | 368050.175 | 1.4096166227810303 | 64.33% | 0.025025025025025023 | 0 |
| 6 | 25919.487 | 172228.607 | 387448.831 | 1.2181740010224533 | 69.40% | 0.025021894157387717 | 0 |
| 7 | 25346.047 | 156368.895 | 412352.511 | 1.180741086153458 | 70.05% | 0.025025025025025023 | 0 |
| 8 | 25034.751 | 144441.343 | 400031.743 | 1.4192422294616291 | 64.35% | 0.025025025025025023 | 0 |
| 9 | 25509.887 | 147324.927 | 375390.207 | 1.3368883869318626 | 66.37% | 0.025025025025025023 | 0 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 2206 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=98) |
| 10 | SQLTransientConnectionException | 2415 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 11 | SQLTransientConnectionException | 2393 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 12 | SQLTransientConnectionException | 2408 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 13 | SQLTransientConnectionException | 2392 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 14 | SQLTransientConnectionException | 2474 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 15 | SQLTransientConnectionException | 2616 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 1 | SQLTransientConnectionException | 2492 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 2 | SQLTransientConnectionException | 2286 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 3 | SQLTransientConnectionException | 2431 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 4 | SQLTransientConnectionException | 2424 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 5 | SQLTransientConnectionException | 2377 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=93) |
| 6 | SQLTransientConnectionException | 2583 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 7 | SQLTransientConnectionException | 2582 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 8 | SQLTransientConnectionException | 2395 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 9 | SQLTransientConnectionException | 2467 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T19:18:30Z → 2026-07-15T19:33:30Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 313 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 32923 / 49477 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2953262895 | Cumulative since stats reset |
| Transactions rolled back | 1054 | Non-zero → contention or application errors |
| Temp file bytes written | -2 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5816 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 423421 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T19:18:30Z → 2026-07-15T19:33:30Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 1076.9 | 1066.9 | 1167.7 | 1221.4 | 1221.4 | 1599.5 | 1599.6 | 1599.7 | 1599.7 | 1599.7 | 358494.7 | 397675.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T19:37:18Z*
