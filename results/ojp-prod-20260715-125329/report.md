# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T12:05:29Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 3 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260715-125329` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 2.44 RPS (per instance) |
| **Total throughput** | 39.05 RPS (all instances) |
| **p50 latency** | 4.62 ms |
| **p95 latency** | 38.60 ms |
| **p99 latency** | 36108.25 ms |
| **p999 latency** | 46471.00 ms |
| **Error rate** | 16.00% (0.16) |
| **Total requests** | 43310 |
| **Failed requests** | 7008 |
| **Total successful** | 36302 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 57 |
| observed_postgres_backends_avg_numbackends | 53.65 |
| observed_postgres_backends_median_numbackends | 54 |
| observed_client_backends_active_median | 54016 |
| observed_client_backends_active_max | 82000 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 10.0% / 8.8% / 16.6% / 21.5% / 34.2% |
| OJP proxy-tier host_cpu (avg / peak) | 20.7% / 81.2% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 62.60% |
| OJP proxy-tier RSS (avg / peak, summed) | 1203.90 MiB / 1209.10 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 10.0% / 8.8% / 16.6% / 21.5% / 34.2% |
| PgBouncer tier RSS (avg / peak, summed) | 1203.90 MiB / 1209.10 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 10.0% / 8.8% / 16.6% / 21.5% / 34.2% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 20.7% / 81.2% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 62.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 1203.90 MiB / 1209.10 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.07% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1317 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ✅ PASS (38.60 ms) |
| Error rate | < 0.1% | ❌ FAIL (16.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.48 RPS (all instances) |
| **Achieved throughput** | 39.05 RPS (all instances) |
| **Attempted − achieved gap** | 7.44 RPS (16.00%) |
| **Total attempted ops** | 43211 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 5.855 | 51.455 | 35684.351 | 2.455619732836365 | 16.18% | 0.06259389083625437 | 82 |
| 10 | 4.319 | 34.751 | 36077.567 | 2.4198348818551203 | 17.10% | 0.06257822277847308 | 70 |
| 11 | 4.883 | 35.359 | 37486.591 | 2.3607947042618838 | 18.77% | 0.07508447002878238 | 87 |
| 12 | 4.563 | 42.847 | 37453.823 | 2.491341005388774 | 14.33% | 0.06259389083625437 | 76 |
| 13 | 4.411 | 33.727 | 36667.391 | 2.5280714779172473 | 13.08% | 0.0750938673341677 | 93 |
| 14 | 4.479 | 36.639 | 37715.967 | 2.472677080019626 | 15.29% | 0.06258605582676179 | 77 |
| 15 | 4.683 | 34.399 | 36110.335 | 2.4910829332877675 | 14.40% | 0.07508447002878237 | 90 |
| 1 | 4.659 | 51.167 | 35192.831 | 2.5318822653253563 | 12.93% | 0.07507977255192871 | 93 |
| 2 | 4.135 | 37.855 | 33914.879 | 2.445276599766104 | 15.88% | 0.06257822277847308 | 74 |
| 3 | 4.815 | 37.119 | 34766.847 | 2.3834114562643998 | 17.96% | 0.07508447002878238 | 91 |
| 4 | 4.487 | 37.791 | 35848.191 | 2.273447274172157 | 21.80% | 0.06257039169065198 | 70 |
| 5 | 4.675 | 38.047 | 36012.031 | 2.476295771870444 | 15.11% | 0.07507507507507508 | 87 |
| 6 | 4.351 | 36.863 | 35553.279 | 2.448933141226463 | 15.71% | 0.06258605582676179 | 74 |
| 7 | 4.659 | 40.351 | 36569.087 | 2.3387627837097087 | 19.84% | 0.07507507507507508 | 90 |
| 8 | 4.343 | 33.983 | 35848.191 | 2.5227911860453607 | 13.34% | 0.06259389083625437 | 80 |
| 9 | 4.607 | 35.295 | 36831.231 | 2.4069984311049013 | 17.17% | 0.0626017278076875 | 83 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 438 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 10 | SQLTransientConnectionException | 463 | Client throttle limit reached; request rejected to avoid overloading the database |
| 11 | SQLTransientConnectionException | 508 | Client throttle limit reached; request rejected to avoid overloading the database |
| 12 | SQLTransientConnectionException | 388 | Timeout waiting for slow operation slot for operation: ac3451c82f425cef |
| 13 | SQLTransientConnectionException | 354 | Timeout waiting for slow operation slot for operation: ac3451c82f425cef |
| 14 | SQLTransientConnectionException | 414 | Client throttle limit reached; request rejected to avoid overloading the database |
| 15 | SQLTransientConnectionException | 390 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | SQLTransientConnectionException | 350 | Timeout waiting for slow operation slot for operation: ac3451c82f425cef |
| 2 | SQLTransientConnectionException | 430 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 3 | SQLTransientConnectionException | 486 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 4 | SQLTransientConnectionException | 590 | Client throttle limit reached; request rejected to avoid overloading the database |
| 5 | SQLTransientConnectionException | 409 | Client throttle limit reached; request rejected to avoid overloading the database |
| 6 | SQLTransientConnectionException | 425 | Timeout waiting for slow operation slot for operation: ac3451c82f425cef |
| 7 | SQLTransientConnectionException | 537 | Client throttle limit reached; request rejected to avoid overloading the database |
| 8 | SQLTransientConnectionException | 361 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 9 | SQLTransientConnectionException | 465 | Client throttle limit reached; request rejected to avoid overloading the database |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-15T12:05:29Z → 2026-07-15T12:20:29Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 30.0 | 52.0 | 0.433 | 172 | 0 |
| ojp-2 | 32.3 | 56.0 | 0.376 | 150 | 0 |
| ojp-3 | 31.3 | 56.0 | 0.440 | 152 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T12:05:29Z → 2026-07-15T12:20:29Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 54 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 54016 / 82000 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2402701213 | Cumulative since stats reset |
| Transactions rolled back | 1366 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4961 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 497742 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T12:05:29Z → 2026-07-15T12:20:29Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 3.2 | 2.9 | 7.8 | 10.8 | 15.7 | 7.8 | 5.9 | 31.4 | 37.3 | 55.9 | 405.1 | 406.2 |
| Proxy (OJP / pgBouncer) | ojp-2 | 3.4 | 2.9 | 7.8 | 10.8 | 27.4 | 6.3 | 5.9 | 10.8 | 18.6 | 46.0 | 394.1 | 395.4 |
| Proxy (OJP / pgBouncer) | ojp-3 | 3.5 | 2.9 | 8.8 | 10.8 | 19.5 | 7.0 | 5.9 | 12.7 | 36.2 | 46.9 | 404.7 | 407.5 |
| PostgreSQL | db | 769.1 | 764.8 | 980.5 | 1040.7 | 1091.0 | 1409.8 | 1468.8 | 1597.3 | 1598.3 | 1599.3 | 22647.5 | 32495.7 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T12:24:29Z*
