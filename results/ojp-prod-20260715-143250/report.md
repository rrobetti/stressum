# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T13:44:47Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 3 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260715-143250` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 2.46 RPS (per instance) |
| **Total throughput** | 39.29 RPS (all instances) |
| **p50 latency** | 4.57 ms |
| **p95 latency** | 38.59 ms |
| **p99 latency** | 35753.94 ms |
| **p999 latency** | 46030.88 ms |
| **Error rate** | 15.00% (0.15) |
| **Total requests** | 43298 |
| **Failed requests** | 6695 |
| **Total successful** | 36603 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 57 |
| observed_postgres_backends_avg_numbackends | 53.88 |
| observed_postgres_backends_median_numbackends | 55 |
| observed_client_backends_active_median | 54207 |
| observed_client_backends_active_max | 81605 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | ojp-prod |
| Configured replicas | 16 |
| Configured client pool size (per replica) | 48 |
| OJP servers | 3 |
| Real DB connections per OJP server | 16 |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 10.0% / 8.8% / 16.6% / 22.5% / 44.0% |
| OJP proxy-tier host_cpu (avg / peak) | 28.4% / 106.8% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 82.10% |
| OJP proxy-tier RSS (avg / peak, summed) | 1162.50 MiB / 1169.80 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 10.0% / 8.8% / 16.6% / 22.5% / 44.0% |
| PgBouncer tier RSS (avg / peak, summed) | 1162.50 MiB / 1169.80 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 10.0% / 8.8% / 16.6% / 22.5% / 44.0% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 28.4% / 106.8% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 82.10% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 1162.50 MiB / 1169.80 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.07% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1339 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ✅ PASS (38.59 ms) |
| Error rate | < 0.1% | ❌ FAIL (15.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.39 RPS (all instances) |
| **Achieved throughput** | 39.29 RPS (all instances) |
| **Attempted − achieved gap** | 7.10 RPS (15.30%) |
| **Total attempted ops** | 43209 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 4.439 | 56.927 | 35061.759 | 2.540105515381392 | 12.67% | 0.06258605582676179 | 81 |
| 10 | 4.463 | 33.183 | 36175.871 | 2.4544929520224166 | 15.19% | 0.06259389083625437 | 77 |
| 11 | 4.727 | 37.503 | 36896.767 | 2.4503582899326473 | 15.45% | 0.0750938673341677 | 91 |
| 12 | 4.371 | 34.367 | 37126.143 | 2.510414229131373 | 14.00% | 0.06257822277847308 | 77 |
| 13 | 4.751 | 32.639 | 35815.423 | 2.310108543016681 | 20.12% | 0.0626017278076875 | 87 |
| 14 | 4.463 | 37.311 | 36143.103 | 2.2820507313301404 | 21.41% | 0.06256256256256257 | 73 |
| 15 | 4.607 | 35.711 | 35913.727 | 2.514698590352058 | 13.41% | 0.07508447002878237 | 94 |
| 1 | 4.767 | 53.471 | 35651.583 | 2.466730257306039 | 15.07% | 0.07507507507507508 | 92 |
| 2 | 4.551 | 38.335 | 35520.511 | 2.4478897816430805 | 15.67% | 0.06257822277847308 | 77 |
| 3 | 4.643 | 35.871 | 35684.351 | 2.532140146819046 | 12.82% | 0.07508916868147504 | 94 |
| 4 | 4.283 | 37.279 | 35323.903 | 2.551394532294659 | 12.56% | 0.06259389083625437 | 79 |
| 5 | 4.679 | 41.759 | 34603.007 | 2.383984252423878 | 17.77% | 0.07507507625047274 | 87 |
| 6 | 4.371 | 39.263 | 36241.407 | 2.59992063286662 | 10.93% | 0.06258605582676179 | 80 |
| 7 | 4.527 | 35.071 | 35553.279 | 2.5217138648159803 | 13.08% | 0.07507977255192871 | 91 |
| 8 | 4.411 | 34.175 | 35323.903 | 2.3450564731164825 | 19.17% | 0.06257039169065198 | 69 |
| 9 | 4.987 | 34.623 | 35028.991 | 2.381527851629848 | 18.07% | 0.0750703787736191 | 90 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 343 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 10 | SQLTransientConnectionException | 411 | Client throttle limit reached; request rejected to avoid overloading the database |
| 11 | SQLTransientConnectionException | 418 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 12 | SQLTransientConnectionException | 379 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 13 | SQLTransientConnectionException | 544 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 14 | SQLTransientConnectionException | 579 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 15 | SQLTransientConnectionException | 363 | Timeout waiting for slow operation slot for operation: ac3451c82f425cef |
| 1 | SQLTransientConnectionException | 408 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 2 | SQLTransientConnectionException | 424 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 3 | SQLTransientConnectionException | 347 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 4 | SQLTransientConnectionException | 340 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 5 | SQLTransientConnectionException | 481 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 6 | SQLTransientConnectionException | 296 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 7 | SQLTransientConnectionException | 354 | Client throttle limit reached; request rejected to avoid overloading the database |
| 8 | SQLTransientConnectionException | 519 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 9 | SQLTransientConnectionException | 489 | Timeout waiting for slow operation slot for operation: ac3451c82f425cef |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-15T13:44:47Z → 2026-07-15T13:59:47Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 32.4 | 56.0 | 0.381 | 166 | 0 |
| ojp-2 | 31.4 | 54.0 | 0.396 | 155 | 0 |
| ojp-3 | 31.1 | 56.0 | 0.423 | 153 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T13:44:47Z → 2026-07-15T13:59:47Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 55 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 54207 / 81605 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2378234016 | Cumulative since stats reset |
| Transactions rolled back | 1353 | Non-zero → contention or application errors |
| Temp file bytes written | 2 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -2 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4918 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 493776 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T13:44:47Z → 2026-07-15T13:59:47Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 3.1 | 2.9 | 7.8 | 9.8 | 19.6 | 6.8 | 4.9 | 12.8 | 35.3 | 39.3 | 394.1 | 396.6 |
| Proxy (OJP / pgBouncer) | ojp-2 | 3.5 | 2.9 | 8.8 | 11.7 | 38.1 | 15.3 | 7.8 | 39.2 | 64.7 | 91.0 | 358.0 | 361.3 |
| Proxy (OJP / pgBouncer) | ojp-3 | 3.5 | 2.9 | 8.8 | 10.8 | 24.4 | 6.9 | 5.9 | 11.8 | 36.2 | 53.8 | 410.4 | 411.9 |
| PostgreSQL | db | 781.5 | 786.1 | 995.5 | 1060.5 | 1210.9 | 1439.8 | 1493.6 | 1596.4 | 1598.1 | 1598.7 | 29293.1 | 42426.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T14:03:50Z*
